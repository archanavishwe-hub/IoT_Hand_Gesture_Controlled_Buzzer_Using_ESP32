import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision


# Create hand detector
base_options = python.BaseOptions(
    model_asset_path="hand_landmarker.task"
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)

detector = vision.HandLandmarker.create_from_options(options)


cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    # Convert OpenCV image to MediaPipe image
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    # Detect hand
    result = detector.detect(mp_image)

    if result.hand_landmarks:

        hand = result.hand_landmarks[0]

        fingers = 0

        # Index, middle, ring, little finger
        tips = [8, 12, 16, 20]

        for tip in tips:

            tip_y = hand[tip].y
            pip_y = hand[tip - 2].y

            if tip_y < pip_y:
                fingers += 1

        if fingers >= 3:
            status = "HAND OPEN"
        else:
            status = "HAND CLOSED"

        cv2.putText(
            frame,
            status,
            (30, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.2,
            (0, 255, 0),
            3
        )

        cv2.putText(
            frame,
            "Fingers: " + str(fingers),
            (30, 110),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

    cv2.imshow("Hand Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()