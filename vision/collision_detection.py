class CollisionDetector:

    def __init__(self):

        self.warning_threshold = 25000

    def check(self, vehicles):

        fcw_status = "SAFE"

        ttc = 99.0

        for vehicle in vehicles:

            x1, y1, x2, y2 = vehicle

            area = (

                (x2 - x1)

                *

                (y2 - y1)
            )

            # =========================
            # FORWARD COLLISION WARNING
            # =========================

            if area > self.warning_threshold:

                fcw_status = "WARNING"

                # Fake TTC estimation
                # based on vehicle size

                ttc = max(

                    0.5,

                    50000 / area
                )

                break

        return fcw_status, ttc