from controller import Supervisor
import math

robot = Supervisor()

timestep = int(
    robot.getBasicTimeStep()
)

car = robot.getSelf()

translation_field = car.getField(
    "translation"
)

rotation_field = car.getField(
    "rotation"
)

# ==========================================
# LOAD WAYPOINTS
# ==========================================

waypoint_names = [

    "WAYPOINT_1",
    "WAYPOINT_2",
    "WAYPOINT_3",
    "WAYPOINT_4",
    "WAYPOINT_5",
    "WAYPOINT_6",
    "WAYPOINT_7",
    "WAYPOINT_8"

]

waypoints = []

for name in waypoint_names:

    node = robot.getFromDef(name)

    if node is not None:

        pos = node.getPosition()

        waypoints.append(pos)

        print("Loaded:", name, pos)

# ==========================================
# SAFETY CHECK
# ==========================================

if len(waypoints) == 0:

    print("NO WAYPOINTS FOUND")
    exit()

# ==========================================
# SETTINGS
# ==========================================

current_waypoint = 0

speed = 0.15

# IMPORTANT:
# START EXACTLY AT FIRST WAYPOINT

position = [

    waypoints[0][0],
    1.2,
    waypoints[0][2]

]

# ==========================================
# MAIN LOOP
# ==========================================

while robot.step(timestep) != -1:

    target = waypoints[
        current_waypoint
    ]

    target_x = target[0]

    target_z = target[2]

    dx = target_x - position[0]

    dz = target_z - position[2]

    distance = math.sqrt(
        dx * dx +
        dz * dz
    )

    # ======================================
    # NEXT WAYPOINT
    # ======================================

    if distance < 2.0:

        current_waypoint += 1

        if current_waypoint >= len(waypoints):

            current_waypoint = 0

        continue

    # ======================================
    # NORMALIZED DIRECTION
    # ======================================

    direction_x = dx / distance

    direction_z = dz / distance

    # ======================================
    # MOVE FORWARD
    # ======================================

    position[0] += direction_x * speed

    position[2] += direction_z * speed

    # ======================================
    # APPLY POSITION
    # ======================================

    translation_field.setSFVec3f([

        position[0],
        1.2,
        position[2]

    ])

    # ======================================
    # FACE MOVEMENT DIRECTION
    # ======================================

    angle = math.atan2(
        direction_x,
        direction_z
    )

    rotation_field.setSFRotation([

        0,
        1,
        0,
        angle

    ])

    # ======================================
    # DEBUG
    # ======================================

    print(
        "Waypoint:",
        current_waypoint
    )