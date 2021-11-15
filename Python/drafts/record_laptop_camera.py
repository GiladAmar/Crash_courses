import cv2
import numpy as np

downscale_factor = 6
# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Unable to read camera feed")

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('outpy.avi',
                      fourcc=fourcc,
                      fps=10.0,
                      frameSize=(frame_width // downscale_factor, frame_height // downscale_factor),
                      isColor=False)

while (True):
    ret, frame = cap.read()

    if ret == True:

        frame = cv2.resize(frame, (frame_width // downscale_factor, frame_height // downscale_factor))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Write the frame into the file 'output.avi'
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # Press Q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

    # When everything done, release the video capture and video write objects
cap.release()
out.release()

# Closes all the frames
cv2.destroyAllWindows()
