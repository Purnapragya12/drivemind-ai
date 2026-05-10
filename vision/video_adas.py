import cv2
import time

from vision.object_detection import (
    VehicleDetector
)

from vision.lane_detection import (
    LaneDetector
)

from vision.collision_detection import (
    CollisionDetector
)


class VideoADAS:

    def __init__(self):

        self.detector = VehicleDetector()

        self.lanes = LaneDetector()

        self.collision = CollisionDetector()

        self.prev_time = 0

    def process(self, frame):

        image = frame.copy()

        # ======================================
        # VEHICLE DETECTION
        # ======================================

        image, vehicles = (

            self.detector.detect(
                image
            )
        )

        # ======================================
        # LANE DETECTION
        # ======================================

        (
            image,
            lane_center,
            offset,
            lane_status,
            lane_color

        ) = self.lanes.detect(
            image
        )

        # ======================================
        # COLLISION DETECTION
        # ======================================

        fcw_status, ttc = (

            self.collision.check(
                vehicles
            )
        )

        # ======================================
        # FPS
        # ======================================

        current_time = time.time()

        fps = int(

            1 / (
                current_time
                - self.prev_time
                + 0.0001
            )
        )

        self.prev_time = current_time

        # ======================================
        # PREMIUM HUD
        # ======================================

        overlay = image.copy()

        cv2.rectangle(

            overlay,

            (20, 20),

            (430, 330),

            (5, 10, 20),

            -1
        )

        image = cv2.addWeighted(

            overlay,

            0.45,

            image,

            0.55,

            0
        )

        # ======================================
        # TITLE
        # ======================================

        cv2.putText(

            image,

            "DriveMind AI",

            (40, 60),

            cv2.FONT_HERSHEY_SIMPLEX,

            1.3,

            (255, 255, 255),

            3
        )

        # ======================================
        # VEHICLES
        # ======================================

        cv2.putText(

            image,

            f"Vehicles: {len(vehicles)}",

            (40, 120),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.95,

            (0, 255, 255),

            2
        )

        # ======================================
        # LANE STATUS
        # ======================================

        cv2.putText(

            image,

            f"Lane: {lane_status}",

            (40, 170),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.95,

            lane_color,

            3
        )

        # ======================================
        # OFFSET
        # ======================================

        cv2.putText(

            image,

            f"Offset: {offset}",

            (40, 220),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.95,

            (255, 255, 255),

            2
        )

        # ======================================
        # FCW
        # ======================================

        fcw_color = (

            (0, 255, 0)

            if fcw_status == "SAFE"

            else

            (0, 0, 255)
        )

        cv2.putText(

            image,

            f"FCW: {fcw_status}",

            (40, 270),

            cv2.FONT_HERSHEY_SIMPLEX,

            1,

            fcw_color,

            3
        )

        # ======================================
        # TTC
        # ======================================

        cv2.putText(

            image,

            f"TTC: {ttc:.2f} sec",

            (40, 320),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.95,

            (255, 0, 255),

            2
        )

        # ======================================
        # FPS
        # ======================================

        cv2.putText(

            image,

            f"FPS: {fps}",

            (1100, 60),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.9,

            (0, 255, 255),

            2
        )

        return image