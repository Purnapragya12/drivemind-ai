import cv2
import numpy as np


class LaneDetector:

    def __init__(self):

        self.prev_lane_center = None

    def smooth_value(

        self,

        previous,

        current,

        alpha=0.85
    ):

        if previous is None:

            return current

        return int(

            previous * alpha +

            current * (1 - alpha)
        )

    def detect(self, frame):

        image = frame.copy()

        gray = cv2.cvtColor(

            image,

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

        height, width = edges.shape

        # =========================
        # ROI
        # =========================

        mask = np.zeros_like(edges)

        polygon = np.array([[

            (0, height),

            (width, height),

            (width, int(height * 0.60)),

            (0, int(height * 0.60))

        ]])

        cv2.fillPoly(

            mask,

            polygon,

            255
        )

        masked = cv2.bitwise_and(
            edges,
            mask
        )

        # =========================
        # LINES
        # =========================

        lines = cv2.HoughLinesP(

            masked,

            1,

            np.pi / 180,

            threshold=50,

            minLineLength=80,

            maxLineGap=50
        )

        left_x = []
        right_x = []

        if lines is not None:

            for line in lines:

                x1, y1, x2, y2 = line[0]

                slope = (

                    (y2 - y1)

                    /

                    (x2 - x1 + 1e-5)
                )

                # Ignore horizontal lines

                if abs(slope) < 0.5:

                    continue

                if slope < 0:

                    left_x.append(x1)

                else:

                    right_x.append(x1)

                cv2.line(

                    image,

                    (x1, y1),

                    (x2, y2),

                    (0, 255, 0),

                    5
                )

        # =========================
        # LANE CENTER
        # =========================

        frame_center = width // 2

        lane_center = frame_center

        if left_x and right_x:

            left_avg = int(np.mean(left_x))

            right_avg = int(np.mean(right_x))

            lane_center = (
                left_avg + right_avg
            ) // 2

            lane_center = self.smooth_value(

                self.prev_lane_center,

                lane_center
            )

            self.prev_lane_center = lane_center

        offset = (
            frame_center - lane_center
        )

        # =========================
        # CENTER VISUALIZATION
        # =========================

        cv2.line(

            image,

            (frame_center, height),

            (frame_center, height - 200),

            (255, 0, 0),

            5
        )

        cv2.line(

            image,

            (lane_center, height),

            (lane_center, height - 200),

            (0, 255, 255),

            5
        )

        # =========================
        # STATUS
        # =========================

        if abs(offset) > 80:

            status = "LANE WARNING"

            color = (0, 0, 255)

        else:

            status = "LANE TRACKING"

            color = (0, 255, 0)

        return (

            image,

            lane_center,

            offset,

            status,

            color
        )