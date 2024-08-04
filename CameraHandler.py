import cam
import cv2
from GeminiAPI import GeminiAPI


# defines video capture object, what camera you are using
class CameraHandler:
    pictureValid = False

    def capture_frames(self):
        # change int based on port
        cam = cv2.VideoCapture(1)
        # Reduces Camera Buffer size to 1 meaning this might offload the data faster with less delay
        cam.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        # Set Width and Height Resolution
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # name of window
        cv2.namedWindow("Webcam Screenshot")

        while True:
            ret, frame = cam.read()  # capture the video frame by frame and stores it in variable 'frame'

            # Checks to see if frame captured
            if not ret:
                print("failed to grab frame")
                break

            # display the frame on screen
            cv2.imshow("test", frame)

            # detects and waits for user input
            k = cv2.waitKey(1)

            # closes app if escape key pressed
            if k % 256 == 27:
                print("Escape hit, closing the app")
                break

            # takes picture if space key pressed
            elif k % 256 == 32:
                img_name = "throw_away_item.png"
                cv2.imwrite(img_name, frame)
                print("screenshot taken")
                # Call gemini API in here instead of Main to not break loop
                # gemini_api = GeminiAPI()
                # gemini_api.classify_image()

        cam.release()

        cam.destroyAllWindows()

    pass
