import json
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
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

# Import your custom mapping from the adjacent file
from movement_map import MOVEMENT_MAP

def convert_tonal_to_fit(json_path, fit_path):
    with open(json_path, 'r') as f:
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

    builder = FitFileBuilder(auto_define=True, min_string_size=50)

    # 1. Spoof a Garmin Device
    file_id = FileIdMessage()
    file_id.type = FileType.ACTIVITY
    file_id.manufacturer = Manufacturer.GARMIN.value
    file_id.product = 3121 
    file_id.time_created = begin_ts
    file_id.serial_number = 12345
    builder.add(file_id)

    # 2. Timer Start Event 
    start_event = EventMessage()
    start_event.timestamp = begin_ts
    start_event.event = Event.TIMER
    start_event.event_type = EventType.START
    builder.add(start_event)

    # 3. Dummy Record (Beginning of workout)
    start_record = RecordMessage()
    start_record.timestamp = begin_ts + 1000 
    builder.add(start_record)

    # 4. Workout Sets
    set_index = 0
    for block in tonal_data.get('workoutSetActivity', []):
        movement_id = block.get('movementId')
        rep_count = int(block.get('repCount', 0))
        
        # Process if there are reps, OR if it's a 0-rep timed movement (indicated by having a movementId)
        if rep_count > 0 or movement_id:
            set_mesg = SetMessage()
            set_time = datetime.fromisoformat(block['endTime'].replace('Z', '+00:00'))
            set_mesg.timestamp = int(set_time.timestamp() * 1000)
            
            duration_s = float(block.get('duration', 0))
            set_mesg.duration = duration_s
            
            set_mesg.start_time = set_mesg.timestamp - int(duration_s * 1000)
            set_mesg.set_type = SetType.ACTIVE
            
            # Garmin accepts 0 reps for timed bodyweight holds/moves
            set_mesg.repetitions = rep_count
            
            weight_lbs = float(block.get('avgWeight', 0))
            # Only append weight if it's > 0. Garmin assumes bodyweight if omitted.
            if weight_lbs > 0:
                set_mesg.weight = weight_lbs * 0.453592 
            
            if movement_id in MOVEMENT_MAP:
                mapping = MOVEMENT_MAP[movement_id]
                set_mesg.category = [mapping['category']]
                set_mesg.category_subtype = [mapping['subtype']]
            
            set_mesg.message_index = set_index
            set_index += 1
            
            builder.add(set_mesg)

    # 5. Dummy Record (End of workout)
    end_record = RecordMessage()
    end_record.timestamp = end_ts - 1000 
    builder.add(end_record)

    # 6. Timer Stop Event
    stop_event = EventMessage()
    stop_event.timestamp = end_ts
    stop_event.event = Event.TIMER
    stop_event.event_type = EventType.STOP_ALL
    builder.add(stop_event)

    # 7. Lap Message
    lap = LapMessage()
    lap.message_index = 0
    lap.timestamp = end_ts
    lap.start_time = begin_ts
    lap.total_elapsed_time = elapsed_time_seconds
    lap.total_timer_time = float(tonal_data['totalDuration'])
    lap.event = Event.LAP
    lap.event_type = EventType.STOP
    builder.add(lap)

    # 8. Session Message
    session = SessionMessage()
    session.message_index = 0
    session.timestamp = end_ts
    session.start_time = begin_ts
    session.sport = Sport.TRAINING
    session.sub_sport = SubSport.STRENGTH_TRAINING
    session.total_elapsed_time = elapsed_time_seconds
    session.total_timer_time = float(tonal_data['totalDuration'])
    session.first_lap_index = 0
    session.num_laps = 1
    session.event = Event.SESSION
    session.event_type = EventType.STOP
    builder.add(session)

    # 9. Activity Message 
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
    fit_file.to_file(fit_path)
    print(f"Successfully compiled FIT file: {fit_path}")

if __name__ == "__main__":
    convert_tonal_to_fit('workout.json', 'tonal_workout.fit')