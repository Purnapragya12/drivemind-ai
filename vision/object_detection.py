from ultralytics import YOLO

import cv2


class VehicleDetector:

    def __init__(self):

        self.model = YOLO(
            "yolov8n.pt"
        )

    def detect(self, frame):

        results = self.model(

            frame,

            imgsz=640,

            conf=0.4,

            verbose=False,

            device="cpu"
        )

        vehicles = []

        image = frame.copy()

        for result in results:

            for box in result.boxes:

                cls = int(box.cls[0])

                label = result.names[cls]

                confidence = float(
                    box.conf[0]
                )

                if label not in [

                    "car",
                    "truck",
                    "bus",
                    "motorcycle"
                ]:
                    continue

                x1, y1, x2, y2 = map(

                    int,

                    box.xyxy[0]
                )

                vehicles.append(
                    (x1, y1, x2, y2)
                )

                cv2.rectangle(

                    image,

                    (x1, y1),

                    (x2, y2),

                    (0, 165, 255),

                    3
                )

                cv2.putText(

                    image,

                    f"{label} {confidence:.2f}",

                    (x1, y1 - 10),

                    cv2.FONT_HERSHEY_SIMPLEX,

                    0.7,

                    (0, 255, 255),

                    2
                )

        return image, vehicles