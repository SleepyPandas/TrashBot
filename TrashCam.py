from tkinter import*
import cv2 from PIL import Image, ImageTk

class TrashCam:
    #Creates application window
    root = Tk()
    root.geometry("1024x768")
    root.title("Trash Cam")


    #Creates Canvas to place Camera
    canvas = Canvas(root, bg = 'white', width = 600, height = 400)
    canvas.pack(padx = 400)

    canvas.place(relx = 0.95, rely = 0.5, anchor = E)



    #Create Label on Canvas, and then create a video capture 
    label_widget = Label(canvas)
    label_widget.place(x = 0, y = 0)
    vid = cv2.VideoCapture(0)
    cap = cv2.VideoCapture(0)
    width, height = 0, 0
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


    #open camera definition opens a live feed of the webcam
    def open_camera(): 
    
        # Capture the video frame by frame 
        _, frame = vid.read() 
    
        # Convert image from one color space to other 
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
    
        # Capture the latest frame and transform to image 
        captured_image = Image.fromarray(opencv_image) 
    
        # Convert captured image to photoimage 
        photo_image = ImageTk.PhotoImage(image=captured_image) 
    
        # Displaying photoimage in the label 
        label_widget.photo_image = photo_image 
    
        # Configure image in the label 
        label_widget.configure(image=photo_image) 
    
        # Repeat the same process after every 10 seconds 
        label_widget.after(10, open_camera) 

        open_camera()
        root.mainloop()

        cap.release()
        vid.release()
        cv2.destroyAllWindows()