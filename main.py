from GeminiAPI import GeminiAPI
from CameraHandler import CameraHandler

if __name__ == "__main__":
    # Ensure the API key is set in the environment variables

    # Webcam part
    webcam_handler = CameraHandler()
    webcam_handler.capture_frames()
