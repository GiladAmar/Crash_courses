







# Reading Images:
# Read 8-bit grayscale image
img = cv2.imread(fname, flags)

cv2.IMREAD_GRAYSCALE # 8-bit grayscale

cv2.IMREAD_COLOR # Read 8-bit color image

cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH # Read 16-bit color image

cv2.IMREAD_UNCHANGED # Read transparent PNG / TIFF image

cv.CAP_PROP_ORIENTATION_AUTO # Fix orientation when reading file

# Write images
cv2.imwrite(image_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])



# Video
# Input
cap = cv2.VideoCapture(filename) # Or 0, 1, ... for camera 0, 1, ...
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # for windows backed
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Explicitly set input size
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

for img, in images:
    ret, frame = cap.read()

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)  # Calculate Frames per second (FPS)

    if ret == True:
        cv2.imshow('frame', frame)
        if cv2.waitKey(1):
            break
    else:
        break
cap.release()

cap.set(cv2.CAP_PROP_POS_FRAMES, 0) # set specific frame of video

# Output
out = cv2.VideoWriter("/home/giladamar/Desktop/out.avi",
                      fourcc = cv2.cv.FOURCC( *"MJPG" ),
                      fps=10,
                      capSize = (frame_width, frame_height))
# cv2.cv.FOURCC( *"XVID" )    1145656920
# cv2.cv.FOURCC( *"MJPG" )    1196444237
# cv2.cv.FOURCC( *"X264" )     875967064
# cv2.cv.FOURCC( *"DIB " )     541215044
# cv2.cv.FOURCC( *"WMV1" )     827739479
# cv2.cv.FOURCC( *"WMV2" )     844516695

for img in images:
        out.write(img)

out.release()
