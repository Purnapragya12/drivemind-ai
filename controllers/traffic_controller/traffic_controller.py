from controller import Robot

robot = Robot()

timestep = int(
    robot.getBasicTimeStep()
)

left_wheel = robot.getDevice(
    "left_rear_wheel"
)

right_wheel = robot.getDevice(
    "right_rear_wheel"
)

left_wheel.setPosition(
    float('inf')
)

right_wheel.setPosition(
    float('inf')
)

left_wheel.setVelocity(3.0)
right_wheel.setVelocity(3.0)

while robot.step(timestep) != -1:
    pass