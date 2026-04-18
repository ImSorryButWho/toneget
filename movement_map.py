from fit_tool.profile.profile_type import *

# Map Tonal Movement IDs to Garmin's Category and Subtype integers.
# You will need to look up Garmin's specific subtype integers for each move 
# in the FIT SDK documentation or fit-tool's profile_type.py.
MOVEMENT_MAP = {
    # Tonal Barbell Bench Press
    "c9afad76-751b-4f7a-99b7-6b5dc09d3901": {
        "category": ExerciseCategory.BENCH_PRESS, # 4
        "subtype": BenchPressExerciseName.BARBELL_BENCH_PRESS # BARBELL_BENCH_PRESS
    },
    "f4d78bdf-f70c-4f3c-bccb-78e9ff80f9fb": {
        "category": ExerciseCategory.FLYE,
        "subtype": FlyeExerciseName.DECLINE_DUMBBELL_FLYE
    },
    "fed3841a-f6a4-4bb0-a8b6-ee3bdd69edc6": {
        "category": ExerciseCategory.BENCH_PRESS,
        "subtype": BenchPressExerciseName.DECLINE_DUMBBELL_BENCH_PRESS
    },
    "8edc0211-4594-4e5e-8e1b-b05dfc1d67c7": {
        "category": ExerciseCategory.BENCH_PRESS,
        "subtype": BenchPressExerciseName.DUMBBELL_BENCH_PRESS
    },
    "656d4ed1-df6b-48bf-9c6d-9e5a40ffb269": {
        "category": ExerciseCategory.BENCH_PRESS,
        "subtype": BenchPressExerciseName.SINGLE_ARM_DUMBBELL_BENCH_PRESS
    },
    "eb067021-46de-433c-9262-deea70debde2": {
        "category": ExerciseCategory.BENCH_PRESS,
        "subtype": BenchPressExerciseName.ALTERNATING_DUMBBELL_CHEST_PRESS,
    },
    "52d7ed26-f38c-4e32-babe-fb9be48d515b": {
        "category": ExerciseCategory.PUSH_UP,
        "subtype": PushUpExerciseName.SHOULDER_PUSH_UP
    }
    # Add your other Tonal IDs here...
}