import json
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from fit_tool.fit_file import FitFile
from fit_tool.fit_file_builder import FitFileBuilder
from fit_tool.profile.messages.file_id_message import FileIdMessage
from fit_tool.profile.messages.event_message import EventMessage
from fit_tool.profile.messages.lap_message import LapMessage
from fit_tool.profile.messages.session_message import SessionMessage
from fit_tool.profile.messages.activity_message import ActivityMessage
from fit_tool.profile.messages.set_message import SetMessage
from fit_tool.profile.messages.record_message import RecordMessage
from fit_tool.profile.profile_type import (
    FileType, Manufacturer, Sport, SubSport, 
    Event, EventType, Activity, SetType
)

from movement_map import MOVEMENT_MAP

def merge_tonal_and_garmin(tonal_json_path, garmin_fit_path, output_fit_path):
    # --- 1. Load Tonal Metadata ---
    with open(tonal_json_path, 'r') as f:
        tonal_data = json.load(f)

    begin_time = datetime.fromisoformat(tonal_data['beginTime'].replace('Z', '+00:00'))
    end_time = datetime.fromisoformat(tonal_data['endTime'].replace('Z', '+00:00'))
    
    begin_ts = int(begin_time.timestamp() * 1000)
    end_ts = int(end_time.timestamp() * 1000)
    elapsed_time_seconds = (end_ts - begin_ts) / 1000.0

    tonal_tz = tonal_data.get('timezone', 'UTC')
    local_tz = ZoneInfo(tonal_tz)
    end_time_local = end_time.astimezone(local_tz)
    fit_epoch = datetime(1989, 12, 31, tzinfo=timezone.utc)
    end_time_local_naive_utc = end_time_local.replace(tzinfo=timezone.utc)
    local_timestamp_seconds = int((end_time_local_naive_utc - fit_epoch).total_seconds())

    # --- 2. Load Garmin Data & Sanity Check ---
    garmin_file = FitFile.from_file(garmin_fit_path)
    
    garmin_start_ts = None
    garmin_end_ts = None
    
# Do a quick pre-pass to find the Garmin session boundaries
    for record_obj in garmin_file.records:
        if isinstance(record_obj.message, SessionMessage):
            garmin_start_ts = record_obj.message.start_time
            # Calculate true end time: start_ts + (elapsed seconds * 1000 ms)
            elapsed_s = record_obj.message.total_elapsed_time or 0
            garmin_end_ts = garmin_start_ts + int(elapsed_s * 1000)
            break
            
    if not garmin_start_ts or not garmin_end_ts:
        print("Sanity Check Failed: Could not find start/end boundaries in Garmin file.")
        return False
        
    # Check 1: Garmin starts before, or less than 60,000ms (1 minute) after Tonal
    if garmin_start_ts > (begin_ts + 60000):
        print(f"Sanity Check Failed: Garmin watch started too late.")
        return False
        
    # Check 2: Garmin ends no more than 1 minute before Tonal
    if (garmin_end_ts + 60000) < end_ts:
        print(f"Sanity Check Failed: Garmin watch ended before Tonal workout finished.")
        print(f"Garmin end time: {garmin_end_ts}, Tonal end time: {end_ts}")
        return False

    print("Timeline sanity check passed. Proceeding with merge...")

    # --- 3. Extract Real Telemetry from Garmin Watch ---
    real_records = []
    total_cal = 0
    
    for record_obj in garmin_file.records:
        msg = record_obj.message
        
        if isinstance(msg, SessionMessage) and msg.total_calories is not None:
            total_cal = msg.total_calories
            
        if isinstance(msg, RecordMessage) and msg.timestamp is not None:
            unix_ms = msg.timestamp 
            
            if begin_ts <= unix_ms <= end_ts:
                new_record = RecordMessage()
                new_record.timestamp = int(unix_ms)
                
                if msg.heart_rate is not None:
                    new_record.heart_rate = msg.heart_rate
                if msg.calories is not None:
                    new_record.calories = msg.calories
                if msg.distance is not None:
                    new_record.distance = msg.distance
                    
                real_records.append(new_record)

    # --- 4. Build the Chronological Timeline ---
    timeline_messages = []

    start_event = EventMessage()
    start_event.timestamp = begin_ts
    start_event.event = Event.TIMER
    start_event.event_type = EventType.START
    timeline_messages.append(start_event)

    set_index = 0
    for block in tonal_data.get('workoutSetActivity', []):
        movement_id = block.get('movementId')
        rep_count = int(block.get('repCount', 0))
        
        if rep_count > 0 or movement_id:
            set_mesg = SetMessage()
            set_time = datetime.fromisoformat(block['endTime'].replace('Z', '+00:00'))
            set_mesg.timestamp = int(set_time.timestamp() * 1000)
            
            duration_s = float(block.get('duration', 0))
            set_mesg.duration = duration_s
            set_mesg.start_time = set_mesg.timestamp - int(duration_s * 1000)
            set_mesg.set_type = SetType.ACTIVE
            set_mesg.repetitions = rep_count
            
            weight_lbs = float(block.get('avgWeight', 0))
            if weight_lbs > 0:
                set_mesg.weight = weight_lbs * 0.453592 
            
            if movement_id in MOVEMENT_MAP:
                mapping = MOVEMENT_MAP[movement_id]
                set_mesg.category = [mapping['category']]
                set_mesg.category_subtype = [mapping['subtype']]
            
            set_mesg.message_index = set_index
            set_index += 1
            timeline_messages.append(set_mesg)

    timeline_messages.extend(real_records)

    stop_event = EventMessage()
    stop_event.timestamp = end_ts
    stop_event.event = Event.TIMER
    stop_event.event_type = EventType.STOP_ALL
    timeline_messages.append(stop_event)

    timeline_messages.sort(key=lambda m: m.timestamp)

    # --- 5. Construct the Final File ---
    builder = FitFileBuilder(auto_define=True, min_string_size=50)

    file_id = FileIdMessage()
    file_id.type = FileType.ACTIVITY
    file_id.manufacturer = Manufacturer.GARMIN.value
    file_id.product = 3121 
    file_id.time_created = begin_ts
    file_id.serial_number = 12345
    builder.add(file_id)

    for msg in timeline_messages:
        builder.add(msg)

    lap = LapMessage()
    lap.message_index = 0
    lap.timestamp = end_ts
    lap.start_time = begin_ts
    lap.total_elapsed_time = elapsed_time_seconds
    lap.total_timer_time = float(tonal_data['totalDuration'])
    lap.total_calories = int(total_cal)
    lap.event = Event.LAP
    lap.event_type = EventType.STOP
    builder.add(lap)

    session = SessionMessage()
    session.message_index = 0
    session.timestamp = end_ts
    session.start_time = begin_ts
    session.sport = Sport.TRAINING
    session.sub_sport = SubSport.STRENGTH_TRAINING
    session.total_elapsed_time = elapsed_time_seconds
    session.total_timer_time = float(tonal_data['totalDuration'])
    session.total_calories = int(total_cal) 
    session.first_lap_index = 0
    session.num_laps = 1
    session.event = Event.SESSION
    session.event_type = EventType.STOP
    builder.add(session)

    activity = ActivityMessage()
    activity.timestamp = end_ts
    activity.local_timestamp = local_timestamp_seconds
    activity.total_timer_time = float(tonal_data['totalDuration'])
    activity.num_sessions = 1
    activity.type = Activity.MANUAL
    activity.event = Event.ACTIVITY
    activity.event_type = EventType.STOP
    builder.add(activity)

    fit_file = builder.build()
    fit_file.to_file(output_fit_path)
    print(f"Successfully compiled combined FIT file: {output_fit_path}")
    
    # Return True so the caller knows it succeeded
    return True

if __name__ == "__main__":
    merge_tonal_and_garmin('workout.json', 'garmin_watch.fit', 'ultimate_workout.fit')