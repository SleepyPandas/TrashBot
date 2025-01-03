from CameraHandler import CameraHandler


# wrapped in main to ensure no globals
def main():
    webcam_handler = CameraHandler()
    webcam_handler.capture_frames()


if __name__ == "__main__":
    main()
