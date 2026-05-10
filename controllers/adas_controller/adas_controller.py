from controller import Robot
import cv2
import numpy as np

# ======================================================
# DRIVEMIND AI - ADVANCED WEBOTS ADAS
# ======================================================

robot = Robot()

timestep = int(robot.getBasicTimeStep())

# ======================================================
# CAMERA
# ======================================================

camera = robot.getDevice("camera")
camera.enable(timestep)

# ======================================================
# DRIVE WHEELS
# ======================================================

left_wheel = robot.getDevice("left_rear_wheel")
right_wheel = robot.getDevice("right_rear_wheel")

left_wheel.setPosition(float('inf'))
right_wheel.setPosition(float('inf'))

# ======================================================
# STEERING
# ======================================================

left_steer = robot.getDevice("left_steer")
right_steer = robot.getDevice("right_steer")

# ======================================================
# SETTINGS
# ======================================================

BASE_SPEED = 4.5
CURVE_SPEED = 1.8

MAX_STEERING = 0.9

SMOOTHING = 0.88

previous_steering = 0.0
previous_lane_center = None

# ======================================================
# MAIN LOOP
# ======================================================

while robot.step(timestep) != -1:

    # ==================================================
    # CAMERA IMAGE
    # ==================================================

    image = camera.getImage()

    width = camera.getWidth()
    height = camera.getHeight()

    frame = np.frombuffer(
        image,
        np.uint8
    ).reshape((height, width, 4))

    frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGRA2BGR
    )

    # ==================================================
    # REGION OF INTEREST
    # ==================================================

    roi = frame[
        int(height * 0.60):height,
        :
    ]

    roi_height = roi.shape[0]
    roi_width = roi.shape[1]

    # ==================================================
    # PREPROCESS
    # ==================================================

    gray = cv2.cvtColor(
        roi,
        cv2.COLOR_BGR2GRAY
    )

    blur = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    edges = cv2.Canny(
        blur,
        50,
        150
    )

    # ==================================================
    # LANE DETECTION
    # ==================================================

    lines = cv2.HoughLinesP(
        edges,
        1,
        np.pi / 180,
        45,
        minLineLength=60,
        maxLineGap=80
    )

    left_lane = []
    right_lane = []

    if lines is not None:

        for line in lines:

            x1, y1, x2, y2 = line[0]

            dx = x2 - x1
            dy = y2 - y1

            if abs(dx) < 5:
                continue

            slope = dy / dx

            length = np.sqrt(
                (x2 - x1) ** 2 +
                (y2 - y1) ** 2
            )

            # ignore tiny noisy lines
            if length < 50:
                continue

            # LEFT LANE
            if slope < -0.18:

                left_lane.extend([x1, x2])

                cv2.line(
                    roi,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    3
                )

            # RIGHT LANE
            elif slope > 0.18:

                right_lane.extend([x1, x2])

                cv2.line(
                    roi,
                    (x1, y1),
                    (x2, y2),
                    (255, 0, 0),
                    3
                )

    # ==================================================
    # DEFAULTS
    # ==================================================

    frame_center = roi_width // 2

    if previous_lane_center is None:
        previous_lane_center = frame_center

    lane_center = previous_lane_center

    steering = 0.0
    speed = BASE_SPEED

    # ==================================================
    # COMPUTE LANE CENTER
    # ==================================================

    if len(left_lane) > 0 and len(right_lane) > 0:

        left_x = int(np.mean(left_lane))
        right_x = int(np.mean(right_lane))

        lane_center = (left_x + right_x) // 2

        # lane visuals

        cv2.line(
            roi,
            (left_x, 0),
            (left_x, roi_height),
            (0, 255, 0),
            3
        )

        cv2.line(
            roi,
            (right_x, 0),
            (right_x, roi_height),
            (255, 0, 0),
            3
        )

    elif len(left_lane) > 0:

        left_x = int(np.mean(left_lane))
        lane_center = left_x + 220

    elif len(right_lane) > 0:

        right_x = int(np.mean(right_lane))
        lane_center = right_x - 220

    # ==================================================
    # SAVE LANE MEMORY
    # ==================================================

    previous_lane_center = lane_center

    # ==================================================
    # OFFSET + STEERING
    # ==================================================

    error = lane_center - frame_center

    offset = error

    # MUCH STRONGER CURVE RESPONSE

    steering = error / 230.0

    # LIMIT

    steering = max(
        min(steering, MAX_STEERING),
        -MAX_STEERING
    )

    # ==================================================
    # SMOOTHING
    # ==================================================

    steering = (
        previous_steering * SMOOTHING
        +
        steering * (1 - SMOOTHING)
    )

    previous_steering = steering

    # ==================================================
    # DYNAMIC SPEED
    # ==================================================

    if abs(steering) > 0.25:

        speed = CURVE_SPEED

    else:

        speed = BASE_SPEED

    # ==================================================
    # APPLY CONTROLS
    # ==================================================

    left_steer.setPosition(
        steering
    )

    right_steer.setPosition(
        steering
    )

    left_wheel.setVelocity(
        speed
    )

    right_wheel.setVelocity(
        speed
    )

    # ==================================================
    # CENTER VISUALS
    # ==================================================

    cv2.line(
        roi,
        (frame_center, 0),
        (frame_center, roi_height),
        (0, 255, 255),
        2
    )

    cv2.line(
        roi,
        (lane_center, 0),
        (lane_center, roi_height),
        (255, 0, 255),
        3
    )

    # ==================================================
    # HUD
    # ==================================================

    overlay = frame.copy()

    cv2.rectangle(
        overlay,
        (20, 20),
        (480, 300),
        (10, 10, 10),
        -1
    )

    frame = cv2.addWeighted(
        overlay,
        0.60,
        frame,
        0.40,
        0
    )

    cv2.rectangle(
        frame,
        (20, 20),
        (480, 300),
        (255, 0, 255),
        2
    )

    cv2.putText(
        frame,
        "DriveMind AI",
        (40, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.1,
        (255, 255, 255),
        3
    )

    cv2.putText(
        frame,
        "WEBOTS AUTONOMOUS MODE",
        (40, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 0, 255),
        2
    )

    cv2.putText(
        frame,
        "LANE ASSIST ACTIVE",
        (40, 140),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"OFFSET: {offset}",
        (40, 180),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"STEERING: {steering:.2f}",
        (40, 220),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"SPEED: {speed:.1f}",
        (40, 260),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 150, 0),
        2
    )

    # ==================================================
    # DISPLAY
    # ==================================================

    cv2.imshow(
        "DriveMind AI Simulation",
        frame
    )

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()