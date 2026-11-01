from fit_tool.profile.profile_type import *

# Map a Tonal movement ID to a Garmin exercise.  Garmin's FIT files use a 
# Category / Subtype system.  Mappings are not exact, but should get close
# enough for most purposes.

# Matching was done with AI and spot checked, so I'm happy to take PRs if 
# there's a better match for anything.

MOVEMENT_MAP = {
    # ==========================================
    # BENCH PRESS / CHEST PRESS
    # ==========================================
    "eb067021-46de-433c-9262-deea70debde2": { "category": ExerciseCategory.BENCH_PRESS, "subtype": BenchPressExerciseName.ALTERNATING_DUMBBELL_CHEST_PRESS }, # AlternatingBenchPress
    "c9afad76-751b-4f7a-99b7-6b5dc09d3901": { "category": ExerciseCategory.BENCH_PRESS, "subtype": BenchPressExerciseName.BARBELL_BENCH_PRESS }, # BarbellBenchPress
    "8edc0211-4594-4e5e-8e1b-b05dfc1d67c7": { "category": ExerciseCategory.BENCH_PRESS, "subtype": BenchPressExerciseName.DUMBBELL_BENCH_PRESS }, # BenchPress
    "3b3f0628-37ce-4985-ab71-8ae10141ed98": { "category": ExerciseCategory.BENCH_PRESS, "subtype": BenchPressExerciseName.CLOSE_GRIP_BARBELL_BENCH_PRESS }, # CloseGripBarbellBenchPress
    "8e82d264-dc5b-4ff1-8548-5a75142cb442": { "category": ExerciseCategory.BENCH_PRESS, "subtype": BenchPressExerciseName.SINGLE_ARM_CABLE_CHEST_PRESS }, # InlineChestPress
    "656d4ed1-df6b-48bf-9c6d-9e5a40ffb269": { "category": ExerciseCategory.BENCH_PRESS, "subtype": BenchPressExerciseName.SINGLE_ARM_CABLE_CHEST_PRESS }, # SingleArmBenchPress
    "327a3b0b-f58f-4eb2-a552-ac31acf27a2d": { "category": ExerciseCategory.BENCH_PRESS, "subtype": BenchPressExerciseName.SINGLE_ARM_CABLE_CHEST_PRESS }, # SingleLegStandingChestPress
    "ce9f5bf6-df1f-430b-a69e-89b455664b53": { "category": ExerciseCategory.BENCH_PRESS, "subtype": BenchPressExerciseName.SINGLE_ARM_CABLE_CHEST_PRESS }, # StandingChestPress
    "fed3841a-f6a4-4bb0-a8b6-ee3bdd69edc6": { "category": ExerciseCategory.BENCH_PRESS, "subtype": BenchPressExerciseName.DECLINE_DUMBBELL_BENCH_PRESS }, # StandingDeclineChestPress
    "408611a4-684c-4fbc-bc7f-215939e854a3": { "category": ExerciseCategory.BENCH_PRESS, "subtype": BenchPressExerciseName.SINGLE_ARM_CABLE_CHEST_PRESS }, # TallKneelingSingleArmChestPress
    "d5fd808e-e883-4109-9371-cbcc727144cf": { "category": ExerciseCategory.BENCH_PRESS, "subtype": BenchPressExerciseName.WIDE_GRIP_BARBELL_BENCH_PRESS }, # WideGripBarbellBenchPress

    # ==========================================
    # SQUAT
    # ==========================================
    "84df58e8-4b42-46ee-abb3-c953d1148fda": { "category": ExerciseCategory.SQUAT, "subtype": SquatExerciseName.SQUAT }, # AssistedSquat
    "f2f15034-7c0f-4a9d-8f21-24ca3abadd93": { "category": ExerciseCategory.SQUAT, "subtype": SquatExerciseName.BARBELL_FRONT_SQUAT }, # BarbellFrontSquat
    "16323ff6-8dab-4f03-afec-0488986d1784": { "category": ExerciseCategory.SQUAT, "subtype": SquatExerciseName.THRUSTERS }, # BarbellSquattoPress
    "99a561e8-ecf0-423f-848d-7116e8bb1189": { "category": ExerciseCategory.SQUAT, "subtype": SquatExerciseName.DUMBBELL_SPLIT_SQUAT }, # BodyweightSplitSquat
    "02ba615d-2fa1-4216-81ee-127b9b58644c": { "category": ExerciseCategory.SQUAT, "subtype": SquatExerciseName.AIR_SQUAT }, # BodyweightSquat
    "4bb481a8-567d-430b-b014-9f27bba7a802": { "category": ExerciseCategory.SQUAT, "subtype": SquatExerciseName.GOBLET_SQUAT }, # GobletSplitSquat
    "2bd4de7e-d0d0-4aab-ac2d-8511cc80d918": { "category": ExerciseCategory.SQUAT, "subtype": SquatExerciseName.GOBLET_SQUAT }, # GobletSquat
    "b74bbdaf-8a92-497e-ab9e-88e8e1c161b0": { "category": ExerciseCategory.SQUAT, "subtype": SquatExerciseName.GOBLET_SQUAT }, # GobletSquattoBench
    "c4adea15-ee05-4082-92d5-4702af424191": { "category": ExerciseCategory.SQUAT, "subtype": SquatExerciseName.DUMBBELL_SPLIT_SQUAT }, # IsoSplitSquat
    "124bbdb1-482d-4045-ae84-72b4e2eb65e0": { "category": ExerciseCategory.SQUAT, "subtype": SquatExerciseName.BODY_WEIGHT_WALL_SQUAT }, # IsoSquatHold
    "43079c20-bbd1-4cfb-85fc-6e79e4f25967": { "category": ExerciseCategory.PLYO, "subtype": PlyoExerciseName.JUMP_SQUAT }, # JumpSquat
    "ae08e77e-ab5e-4b17-aeba-20e8ed12d9f5": { "category": ExerciseCategory.SQUAT, "subtype": SquatExerciseName.SQUAT }, # LowSquatWalkOut
    "9b9c5754-bbfe-4ae4-b531-e4adc6fa4fec": { "category": ExerciseCategory.SQUAT, "subtype": SquatExerciseName.SUMO_SQUAT }, # MiniSumoSquat
    "d4634ec3-7a7f-49b2-b2a5-e965aaa67744": { "category": ExerciseCategory.SQUAT, "subtype": SquatExerciseName.DUMBBELL_SPLIT_SQUAT }, # RackedOffsetSplitSquatw_Rotation
    "03157c8a-2c1b-41cb-a8c3-7169033bb094": { "category": ExerciseCategory.SQUAT, "subtype": SquatExerciseName.SQUAT }, # RackedOffsetSquat
    "7d6175b3-1351-4dad-830e-632ab3e6ecb6": { "category": ExerciseCategory.SQUAT, "subtype": SquatExerciseName.SQUAT }, # RackedSquat
    "cc0aaa36-dd08-4be3-852e-cf6365f840ce": { "category": ExerciseCategory.SQUAT, "subtype": SquatExerciseName.SQUAT }, # RackedSquattoBench
    "4b4e3a95-d62a-40b5-873c-1287432c1824": { "category": ExerciseCategory.SQUAT, "subtype": SquatExerciseName.STEP_UP }, # ResistedStepUp
    "c7737825-dd6f-44b4-9b25-6ee66b43d07d": { "category": ExerciseCategory.SQUAT, "subtype": SquatExerciseName.DUMBBELL_SPLIT_SQUAT }, # SplitSquat
    "ceda4364-ca24-491c-8138-70d9a330747d": { "category": ExerciseCategory.SQUAT, "subtype": SquatExerciseName.THRUSTERS }, # SquattoPress
    "19af8704-2730-409f-b668-013554ffa510": { "category": ExerciseCategory.SQUAT, "subtype": SquatExerciseName.STEP_UP }, # StepUp

    # ==========================================
    # LUNGE (Includes Split Squats & Bulgarians per Garmin Schema)
    # ==========================================
    "380f1643-9a10-4ef5-bda3-ef7bde449c57": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.BARBELL_SPLIT_SQUAT }, # BarbellFrontRackedSplitSquat
    "b930fb0b-f492-47ca-b776-9c53654e345c": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.DUMBBELL_BULGARIAN_SPLIT_SQUAT }, # BodyweightBulgarianSplitSquat
    "88135233-36ea-43f4-aee8-1d33f18fe185": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.DUMBBELL_BULGARIAN_SPLIT_SQUAT }, # BulgarianSplitSquat
    "2b1e45e5-1d18-4332-806b-2f833176dffc": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.DUMBBELL_BULGARIAN_SPLIT_SQUAT }, # BulgarianSplitSquatw_HipInternalRotation
    "91b999fa-d906-4785-b128-9c5aebfb22ac": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.ALTERNATING_DUMBBELL_LUNGE }, # AlternatingGobletReverseLunge
    "db0df66c-2a8f-4336-bbf5-0f8c3eea544d": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.DUMBBELL_REVERSE_LUNGE }, # AssistedReverseLunge
    "1b74ca5c-1633-42d3-a9dd-eebc3b505d75": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.BARBELL_REVERSE_LUNGE }, # BarbellFrontRackedReverseLunge
    "0b8f03ae-b64a-45c5-8443-dd955637777f": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.LUNGE }, # BodyweightAlternatingReverseLunge
    "8c86cb06-c6bc-4566-a99a-16baf7215789": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.CURTSY_LUNGE }, # GobletCurtseyLunge
    "8905f979-603d-4ed3-890b-d245c5cf9ba4": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.DUMBBELL_REVERSE_LUNGE }, # GobletReverseLunge
    "d1e3eb78-ebf3-4725-9676-f3a61535fa41": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.SIFF_JUMP_LUNGE }, # JumpLunge
    "a4718680-b481-46bc-9309-6101a342d9bc": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.SIDE_LUNGE }, # LateralLunge
    "7e9109b1-47cc-44ce-ad5f-957c52eea105": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.DUMBBELL_REVERSE_LUNGE }, # RackedReverseLunge
    "d0211436-8cfe-43b7-841e-638f67ec2b60": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.LUNGE }, # ResistedAlternatingLunge
    "206dbbce-c14b-4c34-8d68-37b7aafbea00": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.LUNGE }, # ResistedDeepLunge
    "f8bad1ec-c502-4379-b2f4-e9198245e534": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.SIDE_LUNGE }, # ResistedLateralLunge
    "963ff377-e0cf-4760-962c-d8924bcaa67f": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.DUMBBELL_REVERSE_LUNGE }, # ReverseLunge
    "01c29777-688d-4174-861e-e1de32a292f5": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.DUMBBELL_REVERSE_LUNGE }, # ReverseLungew_Hop
    "f5aa94ec-bdc1-4cf6-b306-a5c359dc248d": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.REVERSE_LUNGE_WITH_TWIST_AND_OVERHEAD_REACH }, # ReverseLungew_Rotation
    "2f5153ed-1360-4263-850b-4ace86efad46": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.RUNNERS_LUNGE_TO_BALANCE }, # RunnersLunge
    "61402e4e-bded-4ef8-ba91-77c0c72dbb35": { "category": ExerciseCategory.LUNGE, "subtype": LungeExerciseName.DUMBBELL_REVERSE_LUNGE }, # SuitcaseReverseLunge

    # ==========================================
    # DEADLIFT
    # ==========================================
    "c4f3f895-61c4-4916-9e11-6f3ec68e8dba": { "category": ExerciseCategory.DEADLIFT, "subtype": DeadliftExerciseName.BARBELL_DEADLIFT }, # BarbellDeadlift
    "ef5f1802-a99e-4e56-b473-32bbf353fb73": { "category": ExerciseCategory.DEADLIFT, "subtype": DeadliftExerciseName.ROMANIAN_DEADLIFT }, # BarbellRDL
    "2815c323-5b94-47f2-b946-3b10af26d02b": { "category": ExerciseCategory.DEADLIFT, "subtype": DeadliftExerciseName.SINGLE_LEG_ROMANIAN_DEADLIFT_WITH_DUMBBELL }, # BarbellSingleLegRDL
    "7f71d0b7-43ba-4f06-b47c-3527a6421432": { "category": ExerciseCategory.DEADLIFT, "subtype": DeadliftExerciseName.SUMO_DEADLIFT }, # BarbellSumoDeadlift
    "391cc5b7-5074-4e88-b9d9-098231476a15": { "category": ExerciseCategory.DEADLIFT, "subtype": DeadliftExerciseName.SINGLE_LEG_ROMANIAN_DEADLIFT_WITH_DUMBBELL }, # BodyweightSingleLegRDL
    "a9756142-cce9-4720-ba97-2a84a1cf865b": { "category": ExerciseCategory.DEADLIFT, "subtype": DeadliftExerciseName.DUMBBELL_DEADLIFT }, # NeutralGripDeadlift
    "b551d374-8525-4528-be61-7fc828c9ce58": { "category": ExerciseCategory.DEADLIFT, "subtype": DeadliftExerciseName.ROMANIAN_DEADLIFT }, # RDL
    "d02af998-53da-4042-8441-2f6f7c22b8b0": { "category": ExerciseCategory.DEADLIFT, "subtype": DeadliftExerciseName.SINGLE_ARM_DEADLIFT }, # SingleArmDeadlift
    "5276eb41-fd52-4d32-8e25-033f2b2a7d1c": { "category": ExerciseCategory.DEADLIFT, "subtype": DeadliftExerciseName.SINGLE_LEG_ROMANIAN_DEADLIFT_WITH_DUMBBELL }, # SingleArmSingleLegRDL
    "465987e9-92f2-4c8e-9df8-890e1355f3c6": { "category": ExerciseCategory.DEADLIFT, "subtype": DeadliftExerciseName.SINGLE_LEG_ROMANIAN_DEADLIFT_WITH_DUMBBELL }, # SingleLegRDL
    "0cbe3d68-2026-41fe-a2fc-a598f7dc0b2c": { "category": ExerciseCategory.DEADLIFT, "subtype": DeadliftExerciseName.DUMBBELL_DEADLIFT }, # SuitcaseDeadlift

    # ==========================================
    # PULL UP / PULLDOWN
    # ==========================================
    "1f5e8776-3b9c-4fe7-80d1-75b5b28a4455": { "category": ExerciseCategory.PULL_UP, "subtype": PullUpExerciseName.LAT_PULLDOWN }, # AlternatingNeutralLatPulldown
    "56d65783-2054-4517-aa07-03051b2224cc": { "category": ExerciseCategory.PULL_UP, "subtype": PullUpExerciseName.CHIN_UP }, # BarbellChinup
    "04b05efe-4873-4dc1-b178-a5173e0588d9": { "category": ExerciseCategory.PULL_UP, "subtype": PullUpExerciseName.LAT_PULLDOWN }, # BarbellSeatedLatPulldown
    "f94f667d-5fe2-4bf7-b87e-ca705d5b627d": { "category": ExerciseCategory.PULL_UP, "subtype": PullUpExerciseName.STRAIGHT_ARM_PULLDOWN }, # BarbellStraightArmPulldown
    "1c432cc6-60ff-46eb-9d1d-72cd1c08174d": { "category": ExerciseCategory.PULL_UP, "subtype": PullUpExerciseName.KNEELING_LAT_PULLDOWN }, # HalfKneelingSingleArmPulldownContralateral
    "bc730d06-ef89-4fc9-8e23-886a6d22dcd9": { "category": ExerciseCategory.PULL_UP, "subtype": PullUpExerciseName.KNEELING_LAT_PULLDOWN }, # HalfKneelingSingleArmPulldownIpsilateral
    "0c498470-12f9-4b8b-83e8-940e70f7b967": { "category": ExerciseCategory.PULL_UP, "subtype": PullUpExerciseName.LAT_PULLDOWN }, # NeutralLatPulldown
    "9eeb123a-e072-439a-aa28-3fc490fadfa4": { "category": ExerciseCategory.PULL_UP, "subtype": PullUpExerciseName.STRAIGHT_ARM_PULLDOWN }, # NeutralSingleArmStraightArmPulldown
    "5ac0e785-c473-43d6-b1de-cc7befeac449": { "category": ExerciseCategory.PULL_UP, "subtype": PullUpExerciseName.LAT_PULLDOWN }, # SeatedLatPulldown
    "7a9bbcf9-22d3-4447-9096-585e162bc5c3": { "category": ExerciseCategory.PULL_UP, "subtype": PullUpExerciseName.LAT_PULLDOWN }, # SeatedSingleArmLatPulldown
    "59bc17c2-b92f-4c70-a157-fcc6b8aa44e2": { "category": ExerciseCategory.PULL_UP, "subtype": PullUpExerciseName.STRAIGHT_ARM_PULLDOWN }, # StraightArmPulldown
    "406f12cb-3aaa-43e8-af19-23c6f28c31d3": { "category": ExerciseCategory.PULL_UP, "subtype": PullUpExerciseName.KNEELING_LAT_PULLDOWN }, # TallKneelingSingleArmLatPulldown
    "6663cf19-28e2-42eb-9c80-2b101f35280d": { "category": ExerciseCategory.PULL_UP, "subtype": PullUpExerciseName.LAT_PULLDOWN }, # X_Pulldown
    "d5555c40-95d3-4587-9fb7-f92c69ecc490": { "category": ExerciseCategory.PULL_UP, "subtype": PullUpExerciseName.LAT_PULLDOWN }, # X_Pulldownw_TricepExtension
    "9806547f-2029-4c0a-94cc-d43b7b46da6c": { "category": ExerciseCategory.PULL_UP, "subtype": PullUpExerciseName.EZ_BAR_PULLOVER }, # BarbellPullover

    # ==========================================
    # ROW (Back)
    # ==========================================
    "ec9edd5f-4745-45b7-b78b-b7368839ca38": { "category": ExerciseCategory.ROW, "subtype": RowExerciseName.BARBELL_ROW }, # BarbellBentOverRow
    "b49810b9-44bd-4e7d-9b5d-88029681d855": { "category": ExerciseCategory.ROW, "subtype": RowExerciseName.BENT_OVER_ROW_WITH_DUMBELL }, # BentOverRow
    "3fbe5a3b-2140-473a-be43-2d19f19a1b59": { "category": ExerciseCategory.ROW, "subtype": RowExerciseName.ONE_ARM_BENT_OVER_ROW }, # BirdDogw_Row
    "b4caae56-c6f8-430f-ac33-15d4fed8d8af": { "category": ExerciseCategory.ROW, "subtype": RowExerciseName.SINGLE_ARM_CABLE_ROW }, # HalfKneelingSingleArmRow
    "3d0c5a39-646a-4d21-b6b0-734e415b62c6": { "category": ExerciseCategory.ROW, "subtype": RowExerciseName.SINGLE_ARM_CABLE_ROW_AND_ROTATION }, # RotationalRow
    "dda6c9c4-4142-43a0-ab41-092d842e8bf0": { "category": ExerciseCategory.ROW, "subtype": RowExerciseName.SEATED_CABLE_ROW }, # SeatedAlternatingRow
    "517eadf3-84a0-4800-96f3-072f4a53c7f8": { "category": ExerciseCategory.ROW, "subtype": RowExerciseName.SEATED_CABLE_ROW }, # SeatedRow
    "97854f66-63ce-4d82-8d62-554a19174113": { "category": ExerciseCategory.ROW, "subtype": RowExerciseName.ONE_ARM_BENT_OVER_ROW }, # SingleArmBentOverRow
    "0ba88eb7-9505-4439-95de-c0bfbaa6e060": { "category": ExerciseCategory.ROW, "subtype": RowExerciseName.CABLE_ROW_STANDING }, # SingleArmSquatRow
    "fbc2ac0a-3051-458b-9c76-0f4c3093400e": { "category": ExerciseCategory.ROW, "subtype": RowExerciseName.CABLE_ROW_STANDING }, # StandingAlternatingPush_Pull
    "2e706f78-af9a-41cb-aaaf-20df3212b690": { "category": ExerciseCategory.ROW, "subtype": RowExerciseName.FACE_PULL }, # StandingFacePull
    "6143f6f7-a9ad-4c8b-a63e-c44f59526014": { "category": ExerciseCategory.ROW, "subtype": RowExerciseName.SINGLE_ARM_CABLE_ROW }, # StandingSingleArmRow
    "c6f063ad-ffdc-4606-8352-c4bbf97c50ff": { "category": ExerciseCategory.SHRUG, "subtype": ShrugExerciseName.UPRIGHT_ROW }, # UprightRow
    "69191b43-d000-480e-9f9b-3ca676aa46bb": { "category": ExerciseCategory.ROW, "subtype": RowExerciseName.FACE_PULL }, # Y_Pull
    "b5aa04b0-19d9-4553-ab28-18959d33abe4": { "category": ExerciseCategory.ROW, "subtype": RowExerciseName.CABLE_ROW_STANDING }, # ReverseLungew_SingleArmRow
    "0f17a471-36bb-4209-b8bf-8e895240d4d5": { "category": ExerciseCategory.ROW, "subtype": RowExerciseName.CABLE_ROW_STANDING }, # Squatw_Row

    # ==========================================
    # SHOULDER PRESS
    # ==========================================
    "a906fa8b-a55d-4acf-b350-c6b12f77bf40": { "category": ExerciseCategory.SHOULDER_PRESS, "subtype": ShoulderPressExerciseName.SEATED_BARBELL_SHOULDER_PRESS }, # BarbellSeatedOverheadPress
    "77c3e119-33e8-4a70-85d1-9c29ace43f20": { "category": ExerciseCategory.SHOULDER_PRESS, "subtype": ShoulderPressExerciseName.ALTERNATING_DUMBBELL_SHOULDER_PRESS }, # HalfKneelingAlternatingOverheadPress
    "ead86c43-e68b-403b-a54f-25f9213a35bc": { "category": ExerciseCategory.SHOULDER_PRESS, "subtype": ShoulderPressExerciseName.OVERHEAD_DUMBBELL_PRESS }, # HalfKneelingOverheadPress
    "b5909b6d-21b0-41c0-b3ee-852f529c6afc": { "category": ExerciseCategory.SHOULDER_PRESS, "subtype": ShoulderPressExerciseName.SINGLE_ARM_DUMBBELL_SHOULDER_PRESS }, # HalfKneelingSingleArmOverheadPress
    "d2454e78-e0ad-40ba-bf4f-9e4d981a2966": { "category": ExerciseCategory.SHOULDER_PRESS, "subtype": ShoulderPressExerciseName.SEATED_DUMBBELL_SHOULDER_PRESS }, # SeatedAlternatingOverheadPress
    "c3387b0d-c4e4-470f-aa7a-1fe20a3ce071": { "category": ExerciseCategory.SHOULDER_PRESS, "subtype": ShoulderPressExerciseName.SEATED_DUMBBELL_SHOULDER_PRESS }, # SeatedOverheadPress
    "f15f586b-90f6-426c-b445-3415c1d4fea0": { "category": ExerciseCategory.SHOULDER_PRESS, "subtype": ShoulderPressExerciseName.SEATED_DUMBBELL_SHOULDER_PRESS }, # SeatedSingleArmOverheadPress
    "eabcfa09-599a-4efd-8997-de107832de01": { "category": ExerciseCategory.SHOULDER_PRESS, "subtype": ShoulderPressExerciseName.OVERHEAD_BARBELL_PRESS }, # StandingBarbellOverheadPress
    "15e61478-bbe3-41dc-a45c-7dd857bb8968": { "category": ExerciseCategory.SHOULDER_PRESS, "subtype": ShoulderPressExerciseName.OVERHEAD_DUMBBELL_PRESS }, # StandingOverheadPress

    # ==========================================
    # CURL (Biceps)
    # ==========================================
    "92eb9caf-b1ea-4b3c-94ec-7d5e5fb1f476": { "category": ExerciseCategory.CURL, "subtype": CurlExerciseName.ALTERNATING_DUMBBELL_BICEPS_CURL }, # AlternatingBicepCurl
    "0b5e580d-f813-4f4e-81ae-2ed559f88a93": { "category": ExerciseCategory.CURL, "subtype": CurlExerciseName.BARBELL_BICEPS_CURL }, # BarbellBicepCurl
    "dffe549f-179e-4cae-b43e-9a4af6cb1bc7": { "category": ExerciseCategory.CURL, "subtype": CurlExerciseName.DUMBBELL_BICEPS_CURL }, # BicepCurl
    "2cb2b3f2-ff44-49f6-9938-915295db1e82": { "category": ExerciseCategory.CURL, "subtype": CurlExerciseName.DUMBBELL_HAMMER_CURL }, # HammerCurl
    "af1785f9-cd7b-4725-ba56-3ea4eae038c2": { "category": ExerciseCategory.CURL, "subtype": CurlExerciseName.CABLE_BICEPS_CURL }, # LyingBicepCurl
    "6b526e88-90a3-4724-931c-f667e2add45c": { "category": ExerciseCategory.CURL, "subtype": CurlExerciseName.CABLE_BICEPS_CURL }, # LyingFaceCurl
    "bbf70900-fc6f-4057-86fb-34e0dd0f328f": { "category": ExerciseCategory.CURL, "subtype": CurlExerciseName.REVERSE_GRIP_BARBELL_BICEPS_CURL }, # ReverseGripBarbellBicepCurl
    "4172950f-6e31-4f42-be04-45f2ca641d21": { "category": ExerciseCategory.CURL, "subtype": CurlExerciseName.REVERSE_GRIP_BARBELL_BICEPS_CURL }, # ReverseGripBicepCurl
    "a136ca01-f0d8-46ed-a4e1-9e94c457422e": { "category": ExerciseCategory.CURL, "subtype": CurlExerciseName.SEATED_ALTERNATING_DUMBBELL_BICEPS_CURL }, # SeatedAlternatingBicepCurl
    "65ebd242-b9d3-405d-9922-0c6e3df0ce22": { "category": ExerciseCategory.CURL, "subtype": CurlExerciseName.SEATED_DUMBBELL_BICEPS_CURL }, # SeatedBicepCurl

    # ==========================================
    # TRICEPS EXTENSION
    # ==========================================
    "7e40f53a-78a5-4620-b903-4bc81d05cbe2": { "category": ExerciseCategory.TRICEPS_EXTENSION, "subtype": TricepsExtensionExerciseName.LYING_EZ_BAR_TRICEPS_EXTENSION }, # BarbellSkullCrusher
    "9b0b0dad-6f86-4832-9dee-e6eaf4fad8b9": { "category": ExerciseCategory.TRICEPS_EXTENSION, "subtype": TricepsExtensionExerciseName.OVERHEAD_DUMBBELL_TRICEPS_EXTENSION }, # OverheadTricepExtension
    "3ab05f57-b729-4abe-a15e-00a1680f2547": { "category": ExerciseCategory.TRICEPS_EXTENSION, "subtype": TricepsExtensionExerciseName.REVERSE_GRIP_PRESSDOWN }, # ReverseGripBarbellTricepExtension
    "0e17b36b-37b4-4c6f-accb-979dfaaf30d2": { "category": ExerciseCategory.TRICEPS_EXTENSION, "subtype": TricepsExtensionExerciseName.REVERSE_GRIP_PRESSDOWN }, # ReverseGripTricepExtension
    "3671753e-8f7a-43b9-b20c-fce4a0991a0a": { "category": ExerciseCategory.TRICEPS_EXTENSION, "subtype": TricepsExtensionExerciseName.CABLE_KICKBACK }, # SingleArmTricepExtension
    "52f1a3a8-6a76-46b7-ba3b-d5ceba0ddbc9": { "category": ExerciseCategory.TRICEPS_EXTENSION, "subtype": TricepsExtensionExerciseName.DUMBBELL_LYING_TRICEPS_EXTENSION }, # SkullCrusher
    "8571813d-b302-4cbe-a3b5-cc805a046b7d": { "category": ExerciseCategory.TRICEPS_EXTENSION, "subtype": TricepsExtensionExerciseName.TRICEPS_EXTENSION_ON_FLOOR }, # TricepExtension
    "2f5a1f17-32cd-4fb6-9213-46a19a889837": { "category": ExerciseCategory.TRICEPS_EXTENSION, "subtype": TricepsExtensionExerciseName.CABLE_KICKBACK }, # TricepKickback

    # ==========================================
    # HIP RAISE / GLUTE BRIDGE
    # ==========================================
    "d44826e1-f6b3-4bed-9d6f-8456d9cde3ec": { "category": ExerciseCategory.HIP_RAISE, "subtype": HipRaiseExerciseName.BARBELL_HIP_THRUST_WITH_BENCH }, # BarbellHipThrust
    "b686f885-427c-4e64-9aa3-4b485c82678e": { "category": ExerciseCategory.HIP_RAISE, "subtype": HipRaiseExerciseName.BARBELL_HIP_THRUST_ON_FLOOR }, # BarbellLyingGluteBridge
    "d9f6fb59-9bb9-469c-ad65-a9b620535a7d": { "category": ExerciseCategory.HIP_RAISE, "subtype": HipRaiseExerciseName.HIP_RAISE_WITH_FEET_ON_SWISS_BALL }, # ElevatedGluteBridge
    "636f95b7-1c65-4428-a1a5-14cc0f18c4da": { "category": ExerciseCategory.HIP_RAISE, "subtype": HipRaiseExerciseName.SINGLE_LEG_HIP_RAISE }, # ElevatedSingleLegGluteBridge
    "d9966062-96ae-43e5-a896-8df13eb31c48": { "category": ExerciseCategory.HIP_RAISE, "subtype": HipRaiseExerciseName.HIP_RAISE }, # GluteBridge
    "79df9602-0aca-4e39-b9d3-d49b5f76b12f": { "category": ExerciseCategory.HIP_RAISE, "subtype": HipRaiseExerciseName.HIP_RAISE }, # HipRaise
    "bf0bbda8-9515-46dd-8d82-bd57c0cfb85b": { "category": ExerciseCategory.HIP_RAISE, "subtype": HipRaiseExerciseName.MARCHING_HIP_RAISE }, # MarchingGluteBridge
    "93457225-18db-41bc-974e-e874fb4d07d1": { "category": ExerciseCategory.HIP_RAISE, "subtype": HipRaiseExerciseName.WEIGHTED_HIP_RAISE }, # ResistedGluteBridge
    "3f86da6a-6e2c-44fa-8279-d8a361be2d6c": { "category": ExerciseCategory.HIP_RAISE, "subtype": HipRaiseExerciseName.WEIGHTED_HIP_RAISE }, # ResistedHipRaise
    "e1f02f99-0117-48e6-8c4c-ddc104630615": { "category": ExerciseCategory.HIP_RAISE, "subtype": HipRaiseExerciseName.SINGLE_LEG_HIP_RAISE }, # SingleArmPulloverw_SingleLegHipThrustContralateral
    "4ccc12f5-f15a-4345-8b13-290f5fdb74c1": { "category": ExerciseCategory.HIP_RAISE, "subtype": HipRaiseExerciseName.SINGLE_LEG_HIP_RAISE }, # SingleLegGluteBridge
    "ec99fdf6-a953-4d7f-bb46-6ab34b18d4ef": { "category": ExerciseCategory.HIP_RAISE, "subtype": HipRaiseExerciseName.CLAMS }, # Clamshells

    # ==========================================
    # FLYE (Chest/Back Fly)
    # ==========================================
    "03c61400-a790-4fa9-bd34-961500820437": { "category": ExerciseCategory.FLYE, "subtype": FlyeExerciseName.DUMBBELL_FLYE }, # BenchChestFly
    "f4d78bdf-f70c-4f3c-bccb-78e9ff80f9fb": { "category": ExerciseCategory.FLYE, "subtype": FlyeExerciseName.DECLINE_DUMBBELL_FLYE }, # DeclineChestFly
    "f99ab88a-190a-42bb-b145-298b83b39233": { "category": ExerciseCategory.FLYE, "subtype": FlyeExerciseName.INCLINE_DUMBBELL_FLYE }, # InclineChestFly
    "e12dd59c-f1c3-4e2d-bc54-593863b643d0": { "category": ExerciseCategory.FLYE, "subtype": FlyeExerciseName.CABLE_CROSSOVER }, # MiddleChestFly
    "b5734d70-a131-4f7e-8553-8f4874d858e6": { "category": ExerciseCategory.FLYE, "subtype": FlyeExerciseName.SINGLE_ARM_STANDING_CABLE_REVERSE_FLYE }, # ReverseFly
    "f46db1df-b6eb-4a37-b34b-74b7ea2826da": { "category": ExerciseCategory.FLYE, "subtype": FlyeExerciseName.DECLINE_DUMBBELL_FLYE }, # SingleArmDeclineChestFly
    "c4c247a4-20d5-4cf7-8fec-9548c8a68a8f": { "category": ExerciseCategory.FLYE, "subtype": FlyeExerciseName.INCLINE_DUMBBELL_FLYE }, # SingleArmInclineChestFly

    # ==========================================
    # PUSH UP
    # ==========================================
    "856961a3-6f59-49fa-98e8-42562309a7ca": { "category": ExerciseCategory.PUSH_UP, "subtype": PushUpExerciseName.DECLINE_PUSH_UP }, # FootElevatedPushup
    "a4c2835f-332c-4064-9933-2b9586d6e648": { "category": ExerciseCategory.PUSH_UP, "subtype": PushUpExerciseName.INCLINE_PUSH_UP }, # InclinePushup
    "6d6ad0f3-a332-418f-8746-d47f2ff17c6a": { "category": ExerciseCategory.PUSH_UP, "subtype": PushUpExerciseName.PUSH_UP }, # Pushup
    "76fad22d-5fc5-4e4e-bcff-cbcfa9d5a4f6": { "category": ExerciseCategory.PUSH_UP, "subtype": PushUpExerciseName.PUSH_UP_PLUS }, # PushuptoPlank
    "52d7ed26-f38c-4e32-babe-fb9be48d515b": { "category": ExerciseCategory.PUSH_UP, "subtype": PushUpExerciseName.SHOULDER_PUSH_UP }, # ScapularPushup

    # ==========================================
    # CORE / PLANK / CRUNCH / SIT UP
    # ==========================================
    "c1233ebd-7114-445b-a4f5-30ed444b4d50": { "category": ExerciseCategory.PLANK, "subtype": PlankExerciseName.BEAR_CRAWL }, # BearHold
    "6463dfb7-0bf5-474e-8ce1-93460346361c": { "category": ExerciseCategory.CRUNCH, "subtype": CrunchExerciseName.HOLLOW_ROCK }, # BentHollowRocking
    "41934390-f413-4df3-a350-61c6b116abea": { "category": ExerciseCategory.CRUNCH, "subtype": CrunchExerciseName.CRUNCH }, # Crunch
    "7656bbe3-3333-4a57-8d44-09e6b70be19f": { "category": ExerciseCategory.CORE, "subtype": CoreExerciseName.HALF_TURKISH_GET_UP }, # HalfTurkishGet_up
    "d45ce363-e14c-4442-9061-d75e5a6ff4f9": { "category": ExerciseCategory.CRUNCH, "subtype": CrunchExerciseName.HOLLOW_ROCK }, # HollowBodyRocking
    "ae6fddf5-0ec6-4169-9aab-dc35828508f1": { "category": ExerciseCategory.PLANK, "subtype": PlankExerciseName.PLANK }, # InclinePillarBridge
    "f1910308-4e18-4d18-a3c8-19e2c7c460ca": { "category": ExerciseCategory.CRUNCH, "subtype": CrunchExerciseName.KNEELING_CABLE_CRUNCH }, # KneelingCableCrunch
    "de161117-9b21-44f0-9165-1a379474e749": { "category": ExerciseCategory.CRUNCH, "subtype": CrunchExerciseName.KNEELING_OBLIQUE_CABLE_CRUNCH }, # KneelingObliqueCableCrunch
    "d7f2eac2-d0b5-4d85-9977-97278607e34b": { "category": ExerciseCategory.PLANK, "subtype": PlankExerciseName.SIDE_PLANK }, # LateralBridge
    "7e662049-f067-46f2-b83a-33d9ce1ea6a3": { "category": ExerciseCategory.PLANK, "subtype": PlankExerciseName.ROLLING_SIDE_PLANK }, # LateralBridgew_Rotation
    "d509c836-0e78-48d5-8daf-3900add72be4": { "category": ExerciseCategory.PLANK, "subtype": PlankExerciseName.SIDE_PLANK_AND_ROW }, # LateralBridgew_Row
    "518e3e7b-99f9-4c1d-b374-f7905eced882": { "category": ExerciseCategory.CARDIO, "subtype": CardioExerciseName.CARDIO_CORE_CRAWL }, # LateralCrawl
    "7bc2c77c-7726-4bbe-ab3f-99e5add3ab8c": { "category": ExerciseCategory.PLANK, "subtype": PlankExerciseName.MOUNTAIN_CLIMBER }, # LateralMountainClimber
    "481e4edf-06ab-48b3-a576-ad67365ff052": { "category": ExerciseCategory.PLANK, "subtype": PlankExerciseName.BEAR_CRAWL }, # LeopardCrawl
    "8a1062fa-0e41-4fac-828d-88d3139102d4": { "category": ExerciseCategory.PLANK, "subtype": PlankExerciseName.MOUNTAIN_CLIMBER }, # MountainClimber
    "13e0435f-41bc-4332-8efa-a1b4afcb21bb": { "category": ExerciseCategory.PLANK, "subtype": PlankExerciseName.CROSS_BODY_MOUNTAIN_CLIMBER }, # MountainClimberTwist
    "596e53e7-6213-4626-b64e-d8cd0c947fd1": { "category": ExerciseCategory.PLANK, "subtype": PlankExerciseName.PLANK }, # PillarBridge
    "526891db-c314-4bc4-9656-25e78f2e2ae5": { "category": ExerciseCategory.PLANK, "subtype": PlankExerciseName.SIDE_PLANK_AND_ROW }, # PillarBridgew_Row
    "006e2157-32cf-4044-9be3-2a04b04cbceb": { "category": ExerciseCategory.PLANK, "subtype": PlankExerciseName.PLANK_JACKS_WITH_FEET_ON_SLIDING_DISCS }, # PlankJack
    "6696ef4a-72d3-4754-bc1f-4c5036a524ce": { "category": ExerciseCategory.PLANK, "subtype": PlankExerciseName.EXTENDED_PLANK }, # PlankWalkOut
    "7fb8d820-514b-4936-a4d5-f19ed68ed7b6": { "category": ExerciseCategory.PLANK, "subtype": PlankExerciseName.PLANK_PIKES }, # PlanktoToeTap
    "f19f734d-704e-4e71-984d-bcbc61de692b": { "category": ExerciseCategory.PLANK, "subtype": PlankExerciseName.PLANK_WITH_ARM_RAISE }, # Plankw_Reach
    "cdbed252-5ddb-4106-9180-d535df59f52e": { "category": ExerciseCategory.CRUNCH, "subtype": CrunchExerciseName.CRUNCH }, # PulloverCrunch
    "5c43660f-c700-4bda-9ce5-16b12f2db2dd": { "category": ExerciseCategory.PLANK, "subtype": PlankExerciseName.STRAIGHT_ARM_PLANK_WITH_SHOULDER_TOUCH }, # ShoulderTapPlank
    "ad514cdb-b02e-4376-9497-eed35dca7b46": { "category": ExerciseCategory.PLANK, "subtype": PlankExerciseName.SPIDERMAN_PLANK }, # SpidermanCrawl
    "a0fab5e9-8413-4114-b7d5-10bb526a8279": { "category": ExerciseCategory.CRUNCH, "subtype": CrunchExerciseName.CRUNCH }, # SprinterCrunch
    "a4775f44-28da-4f84-8867-fb191949a442": { "category": ExerciseCategory.SIT_UP, "subtype": SitUpExerciseName.V_UP }, # V_Up

    # ==========================================
    # PALLOF PRESS / CHOP / LIFT
    # ==========================================
    "1ccf6cfe-26a5-4f9a-96be-0dab6b5f96f5": { "category": ExerciseCategory.CHOP, "subtype": ChopExerciseName.HALF_KNEELING_ROTATIONAL_CHOP }, # HalfKneelingChop
    "56b1c9b5-8240-4f2d-aa92-badc0dd62176": { "category": ExerciseCategory.CHOP, "subtype": ChopExerciseName.HALF_KNEELING_ROTATIONAL_REVERSE_CHOP }, # HalfKneelingLift
    "6f306d4c-897a-49d3-b300-0a07de26bc0c": { "category": ExerciseCategory.CORE, "subtype": CoreExerciseName.CABLE_CORE_PRESS }, # HalfKneelingPallofPress
    "e990622a-b138-4283-9475-7201ddb9edd4": { "category": ExerciseCategory.CHOP, "subtype": ChopExerciseName.CABLE_WOODCHOP }, # InlineChop
    "b62564d5-f986-4a75-afc5-1bf2d3d7c3c1": { "category": ExerciseCategory.CHOP, "subtype": ChopExerciseName.CABLE_ROTATIONAL_LIFT }, # InlineLift
    "329bc87e-d7a2-47f4-9a65-fd19cf24b144": { "category": ExerciseCategory.CHOP, "subtype": ChopExerciseName.STANDING_ROTATIONAL_CHOP }, # RotationalChop
    "d9b1c1a7-4809-475a-b28b-565069c46452": { "category": ExerciseCategory.CHOP, "subtype": ChopExerciseName.CABLE_ROTATIONAL_LIFT }, # RotationalLift
    "ee792812-174b-4d87-bdfe-be33f1fa5e23": { "category": ExerciseCategory.CORE, "subtype": CoreExerciseName.CABLE_CORE_PRESS }, # SeatedPallofPress
    "b935c139-fd87-49bb-b83e-f38a33494a02": { "category": ExerciseCategory.CHOP, "subtype": ChopExerciseName.STANDING_ROTATIONAL_CHOP }, # SingleLegChop
    "15acaa71-011b-4dc1-b932-1b3d00c1115b": { "category": ExerciseCategory.CORE, "subtype": CoreExerciseName.CABLE_CORE_PRESS }, # SingleLegPallofPress
    "596e7a05-1086-4045-84fb-2b8a2edc88dd": { "category": ExerciseCategory.CHOP, "subtype": ChopExerciseName.STANDING_ROTATIONAL_CHOP }, # StandingChop
    "12d4e320-fc8a-43cd-842c-5934b4bba3c8": { "category": ExerciseCategory.CHOP, "subtype": ChopExerciseName.CABLE_ROTATIONAL_LIFT }, # StandingLift
    "ea30d4b4-4b45-4dc6-a4ee-1b8a85eb88f9": { "category": ExerciseCategory.CORE, "subtype": CoreExerciseName.CABLE_CORE_PRESS }, # StandingPallofPress
    "40244ea9-22a6-4112-86c8-662aaa2da058": { "category": ExerciseCategory.CORE, "subtype": CoreExerciseName.CABLE_CORE_PRESS }, # TallKneelingPallofPress
    "ca4839e2-8f10-47a2-97d8-808ea80f9288": { "category": ExerciseCategory.CORE, "subtype": CoreExerciseName.CABLE_CORE_PRESS }, # HalfKneelingVerticalPush_Pull

    # ==========================================
    # LATERAL / LEG RAISE / ABDUCTION
    # ==========================================
    "5c740fbf-6d28-4fba-912d-040e4d1c92e1": { "category": ExerciseCategory.LATERAL_RAISE, "subtype": LateralRaiseExerciseName.CABLE_FRONT_RAISE }, # BarbellFrontRaise
    "f80654dc-d987-4734-bf8b-b135ef30a7d3": { "category": ExerciseCategory.HIP_STABILITY, "subtype": HipStabilityExerciseName.STANDING_HIP_ABDUCTION }, # BarbellLateralLegRaise
    "794e3822-200b-49c0-b722-debf341d4a5d": { "category": ExerciseCategory.LATERAL_RAISE, "subtype": LateralRaiseExerciseName.CABLE_FRONT_RAISE }, # FrontRaise
    "7dad8063-0eba-4cf7-bcd8-9c12e9515be0": { "category": ExerciseCategory.LATERAL_RAISE, "subtype": LateralRaiseExerciseName.DUMBBELL_LATERAL_RAISE }, # LateralRaise
    "5b5155a1-d1c4-4bf7-8f26-097fc9568cf5": { "category": ExerciseCategory.LEG_RAISE, "subtype": LegRaiseExerciseName.LYING_STRAIGHT_LEG_RAISE }, # ResistedLegRaise
    "9dd867e1-4304-4d85-b0bb-fcddce573c3c": { "category": ExerciseCategory.HIP_STABILITY, "subtype": HipStabilityExerciseName.STANDING_HIP_ABDUCTION }, # SingleArmLateralLegSwing
    "7bcf844b-0f88-492b-a018-6f874c80b99a": { "category": ExerciseCategory.LEG_RAISE, "subtype": LegRaiseExerciseName.LYING_STRAIGHT_LEG_RAISE }, # SingleArmResistedLegRaise
    "9bb67ac6-735c-4830-b2af-d3c0945892b3": { "category": ExerciseCategory.HIP_STABILITY, "subtype": HipStabilityExerciseName.STANDING_HIP_ABDUCTION }, # StandingHipAbduction
    "fe132c4a-69bc-427d-8a94-93413709be25": { "category": ExerciseCategory.LEG_RAISE, "subtype": LegRaiseExerciseName.LEG_LOWERING_DRILL }, # ResistedLegLowering
    "61ff1f2b-f821-4078-a36f-675e40c8b694": { "category": ExerciseCategory.CRUNCH, "subtype": CrunchExerciseName.LEG_EXTENSIONS }, # StandingLegExtension

    # ==========================================
    # CARRY / MARCH
    # ==========================================
    "a8468ca2-8951-4a99-a298-4eb8adb9a3b4": { "category": ExerciseCategory.CARRY, "subtype": CarryExerciseName.OVERHEAD_CARRY }, # BarbellStraightArmMarch
    "b11f89b0-5470-44a2-b70a-5391e972eb71": { "category": ExerciseCategory.CARRY, "subtype": CarryExerciseName.FARMERS_WALK }, # FarmerMarch
    "2e98a197-beea-4c29-afe6-5e8b9f27ca6e": { "category": ExerciseCategory.CARRY, "subtype": CarryExerciseName.FARMERS_WALK }, # SuitcaseMarch
    "ac8db33c-898a-45a7-90e9-c1cc671b42db": { "category": ExerciseCategory.CARRY, "subtype": CarryExerciseName.DUMBBELL_WAITER_CARRY }, # WaiterMarch

    # ==========================================
    # CALF RAISE / LEG CURL
    # ==========================================
    "36df9b2c-629e-4b62-9361-d64272c71215": { "category": ExerciseCategory.CALF_RAISE, "subtype": CalfRaiseExerciseName.SEATED_CALF_RAISE }, # BentKneeCalfRaise
    "32d2ea05-024b-4b98-95eb-079b9f62864d": { "category": ExerciseCategory.LEG_CURL, "subtype": LegCurlExerciseName.SLIDING_LEG_CURL }, # HamstringWalkout
    "bb513fde-19c8-4490-bfc8-d8e71b81b52a": { "category": ExerciseCategory.LEG_CURL, "subtype": LegCurlExerciseName.LEG_CURL }, # ProneBenchHamstringCurl
    "752e2f27-11d5-4758-801d-f030ac5eac7c": { "category": ExerciseCategory.LEG_CURL, "subtype": LegCurlExerciseName.LEG_CURL }, # ProneBenchSingleLegHamstringCurl
    "46fd7421-c0f3-4d92-9488-27471a4097c7": { "category": ExerciseCategory.CALF_RAISE, "subtype": CalfRaiseExerciseName.WEIGHTED_STANDING_CALF_RAISE }, # ResistedCalfRaise
    "27b7f142-837d-4ecf-93dd-7c13269106df": { "category": ExerciseCategory.LEG_CURL, "subtype": LegCurlExerciseName.LEG_CURL }, # StandingSingleLegHamstringCurl

    # ==========================================
    # SHRUG
    # ==========================================
    "772c57de-5c39-4e9d-8e09-32326437433f": { "category": ExerciseCategory.SHRUG, "subtype": ShrugExerciseName.BARBELL_SHRUG }, # ShoulderShrug

    # ==========================================
    # HIP / SHOULDER STABILITY
    # ==========================================
    "4b6c5ef1-ef10-437e-8aa3-835bc8ecfc8e": { "category": ExerciseCategory.HIP_STABILITY, "subtype": HipStabilityExerciseName.DEAD_BUG }, # DeadBug
    "926ba82f-8b50-4c59-ac8f-87ae81732f47": { "category": ExerciseCategory.HIP_STABILITY, "subtype": HipStabilityExerciseName.DEAD_BUG }, # ResistedDeadBug
    "e35a0d48-3858-41f2-b39b-97b12638da82": { "category": ExerciseCategory.HIP_STABILITY, "subtype": HipStabilityExerciseName.DEAD_BUG }, # SingleLegDeadBug
    "4a377a61-5a09-4ece-a627-74b70386e992": { "category": ExerciseCategory.HIP_STABILITY, "subtype": HipStabilityExerciseName.DEAD_BUG }, # ResistedDNSStar
    "daa55e45-1f8a-4c36-93f9-5ddccebf08e6": { "category": ExerciseCategory.HIP_STABILITY, "subtype": HipStabilityExerciseName.QUADRUPED_HIP_EXTENSION }, # QuadrupedDonkeyKick
    "2d9bf227-a36c-4b97-b1c3-049ffa48a344": { "category": ExerciseCategory.HIP_STABILITY, "subtype": HipStabilityExerciseName.HIP_CIRCLES }, # QuadrupedHipCircle
    "08758d6d-a9c0-4b67-bd71-3a3a0431a454": { "category": ExerciseCategory.HIP_STABILITY, "subtype": HipStabilityExerciseName.QUADRUPED_WITH_LEG_LIFT }, # SingleLimbBirdDog
    "7b635e41-d9d1-475b-b4a6-e2779cfe5bf1": { "category": ExerciseCategory.HIP_STABILITY, "subtype": HipStabilityExerciseName.STANDING_REAR_LEG_RAISE }, # StandingDiagonalGluteKickback
    "029ea28e-328b-422e-a410-f1a8fc39c324": { "category": ExerciseCategory.HIP_STABILITY, "subtype": HipStabilityExerciseName.STANDING_REAR_LEG_RAISE }, # StandingDonkeyKick
    "05b255f5-89a9-4e1c-819d-0bfa7bab2e27": { "category": ExerciseCategory.HIP_STABILITY, "subtype": HipStabilityExerciseName.STANDING_REAR_LEG_RAISE }, # StandingStraightLegGluteKickback
    "5bd3f11f-989d-4b7a-8399-0df678113b73": { "category": ExerciseCategory.SHOULDER_STABILITY, "subtype": ShoulderStabilityExerciseName.CABLE_EXTERNAL_ROTATION }, # ExternalShoulderRotation
    "2d93569f-e374-44fc-bf76-917a3ad61594": { "category": ExerciseCategory.SHOULDER_STABILITY, "subtype": ShoulderStabilityExerciseName.CABLE_INTERNAL_ROTATION }, # InternalShoulderRotation
    "6c06db83-63df-40ba-b1b7-71720f06e75a": { "category": ExerciseCategory.SHOULDER_STABILITY, "subtype": ShoulderStabilityExerciseName.FLOOR_T_RAISE }, # ProneShoulderSweep
    "5ae24d6a-9dfa-4972-8efa-78c966bfc18a": { "category": ExerciseCategory.SHOULDER_STABILITY, "subtype": ShoulderStabilityExerciseName.INCLINE_W_RAISE }, # W_Hold

    # ==========================================
    # PLYO / CARDIO / TOTAL_BODY
    # ==========================================
    "e4797e87-bef3-40cc-a1b3-ec160337ca00": { "category": ExerciseCategory.PLYO, "subtype": PlyoExerciseName.LATERAL_LEAP_AND_HOP }, # BroadJumptoBackpedal
    "1df7c409-4ca1-4ce0-9b5d-8767ca3c6770": { "category": ExerciseCategory.PLYO, "subtype": PlyoExerciseName.LATERAL_LEAP_AND_HOP }, # LateralBenchJump
    "0720ba8b-e731-4022-b0d9-ff741e266c39": { "category": ExerciseCategory.PLYO, "subtype": PlyoExerciseName.LATERAL_LEAP_AND_HOP }, # SkaterBound
    "de6a9c09-dd23-4a00-916b-11d6b75642e9": { "category": ExerciseCategory.CARDIO, "subtype": CardioExerciseName.JUMPING_JACKS }, # JumpingJack
    "2df095be-63ee-4300-bef6-18870c797ff2": { "category": ExerciseCategory.TOTAL_BODY, "subtype": TotalBodyExerciseName.BURPEE }, # Burp
    "3e429dce-dc23-4ba8-91d0-d36d1c255a41": { "category": ExerciseCategory.TOTAL_BODY, "subtype": TotalBodyExerciseName.BURPEE }, # Burpee

    # ==========================================
    # HYPEREXTENSION
    # ==========================================
    "99624d39-7233-4f2b-8d47-d1f92a684bf4": { "category": ExerciseCategory.HYPEREXTENSION, "subtype": HyperextensionExerciseName.SUPERMAN_FROM_FLOOR }, # SuperheroIsoHold

    # ==========================================
    # WARM UP
    # ==========================================
    "820c93fa-3d44-48a3-903e-6d1e8b32823c": { "category": ExerciseCategory.WARM_UP, "subtype": WarmUpExerciseName.STRETCH_LYING_SPINAL_TWIST }, # BretzelStretch
    "5f31af31-f322-4b88-9ec2-8a2ae8e6e936": { "category": ExerciseCategory.WARM_UP, "subtype": WarmUpExerciseName.CAT_CAMEL }, # Cat_Cow
    "48af40e8-1b93-4658-a31b-ccbfa3b14472": { "category": ExerciseCategory.WARM_UP, "subtype": WarmUpExerciseName.SLIDE_OUT }, # FloorSlide
    "f8516030-50ee-4a65-baed-15b38d1ce63e": { "category": ExerciseCategory.WARM_UP, "subtype": WarmUpExerciseName.WALKING_HIGH_KNEES }, # HighKnee
    "7f8ad867-c219-4320-a50d-900e9baabf76": { "category": ExerciseCategory.WARM_UP, "subtype": WarmUpExerciseName.STRETCH_HAMSTRING }, # LyingHamstringStretch
    "87f2a7e5-f7e8-4dcd-b628-e9cc95270c5b": { "category": ExerciseCategory.WARM_UP, "subtype": WarmUpExerciseName.STRETCH_90_90 }, # NinetyNinetyArmSweep
    "50e2a938-eee8-4aa4-a82c-17bc9cd12340": { "category": ExerciseCategory.WARM_UP, "subtype": WarmUpExerciseName.STRETCH_90_90 }, # NinetyNinetyHipStretch
    "aed09583-aaf2-4b99-b991-f4d76a3ea494": { "category": ExerciseCategory.WARM_UP, "subtype": WarmUpExerciseName.STRETCH_HIP_FLEXOR_AND_QUAD }, # QuadHipStretch
    "4bc167d1-a598-49f5-897b-c7a7724e9df2": { "category": ExerciseCategory.WARM_UP, "subtype": WarmUpExerciseName.STRETCH_HIP_FLEXOR_AND_QUAD }, # QuadHipStretchw_Bench
    "fb0ceb84-2a21-4428-aa52-58abbce66a5f": { "category": ExerciseCategory.WARM_UP, "subtype": WarmUpExerciseName.REACH_ROLL_AND_LIFT }, # ReachandRotateCloser
    "280df243-f928-4662-9851-b703614b3e87": { "category": ExerciseCategory.WARM_UP, "subtype": WarmUpExerciseName.REACH_ROLL_AND_LIFT }, # ReachandRotateOpener
    "aee454a3-0d31-41c6-825b-6c7537cd17e5": { "category": ExerciseCategory.WARM_UP, "subtype": WarmUpExerciseName.STRETCH_STRADDLE }, # SumoSquatStretch

    # ==========================================
    # UNKNOWN / UNMAPPED
    # ==========================================
    "00000000-0000-0000-0000-000000000005": { "category": ExerciseCategory.UNKNOWN, "subtype": 0 }, # Rest
    "db8e5581-d56e-4925-bfb2-f47e3b692f4d": { "category": ExerciseCategory.UNKNOWN, "subtype": 0 }, # LateralWalkOut
    "70bc255e-0662-44bc-b632-dd093f7ae7a9": { "category": ExerciseCategory.UNKNOWN, "subtype": 0 }, # SingleArmRotationalPunch
    "1ade96ac-867d-4c84-a5ac-ce6b674989ad": { "category": ExerciseCategory.RUN, "subtype": RunExerciseName.JOG }, # ButtKicker
}

# Tonal movements performed on the barbell. Tonal shows the combined load of both
# cables for these (e.g. 31 lb for a 15.5 lb/cable bar), while for everything else
# it shows the weight per handle, and so should the Garmin file.
BARBELL_MOVEMENTS = {
    "c9afad76-751b-4f7a-99b7-6b5dc09d3901",  # BarbellBenchPress
    "ec9edd5f-4745-45b7-b78b-b7368839ca38",  # BarbellBentOverRow
    "0b5e580d-f813-4f4e-81ae-2ed559f88a93",  # BarbellBicepCurl
    "56d65783-2054-4517-aa07-03051b2224cc",  # BarbellChinup
    "c4f3f895-61c4-4916-9e11-6f3ec68e8dba",  # BarbellDeadlift
    "1b74ca5c-1633-42d3-a9dd-eebc3b505d75",  # BarbellFrontRackedReverseLunge
    "380f1643-9a10-4ef5-bda3-ef7bde449c57",  # BarbellFrontRackedSplitSquat
    "5c740fbf-6d28-4fba-912d-040e4d1c92e1",  # BarbellFrontRaise
    "f2f15034-7c0f-4a9d-8f21-24ca3abadd93",  # BarbellFrontSquat
    "d44826e1-f6b3-4bed-9d6f-8456d9cde3ec",  # BarbellHipThrust
    "f80654dc-d987-4734-bf8b-b135ef30a7d3",  # BarbellLateralLegRaise
    "b686f885-427c-4e64-9aa3-4b485c82678e",  # BarbellLyingGluteBridge
    "9806547f-2029-4c0a-94cc-d43b7b46da6c",  # BarbellPullover
    "ef5f1802-a99e-4e56-b473-32bbf353fb73",  # BarbellRDL
    "04b05efe-4873-4dc1-b178-a5173e0588d9",  # BarbellSeatedLatPulldown
    "a906fa8b-a55d-4acf-b350-c6b12f77bf40",  # BarbellSeatedOverheadPress
    "2815c323-5b94-47f2-b946-3b10af26d02b",  # BarbellSingleLegRDL
    "7e40f53a-78a5-4620-b903-4bc81d05cbe2",  # BarbellSkullCrusher
    "16323ff6-8dab-4f03-afec-0488986d1784",  # BarbellSquattoPress
    "a8468ca2-8951-4a99-a298-4eb8adb9a3b4",  # BarbellStraightArmMarch
    "f94f667d-5fe2-4bf7-b87e-ca705d5b627d",  # BarbellStraightArmPulldown
    "7f71d0b7-43ba-4f06-b47c-3527a6421432",  # BarbellSumoDeadlift
    "3b3f0628-37ce-4985-ab71-8ae10141ed98",  # CloseGripBarbellBenchPress
    "bbf70900-fc6f-4057-86fb-34e0dd0f328f",  # ReverseGripBarbellBicepCurl
    "3ab05f57-b729-4abe-a15e-00a1680f2547",  # ReverseGripBarbellTricepExtension
    "eabcfa09-599a-4efd-8997-de107832de01",  # StandingBarbellOverheadPress
    "d5fd808e-e883-4109-9371-cbcc727144cf",  # WideGripBarbellBenchPress
}
