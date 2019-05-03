   k = cv2.waitKey(1) & 0xff
    if k == 27:# escape pressed 
        break
    elif k == 115: # s pressed
        fname = input("File name")
        cv2.imwrite(os.path.join(IMAGES_FOLDER, '{}.jpg'.format(fname)), frame)
   if k != 255: # A key is pressed
    print(k)



    cv2.cvtColor(earth_img, cv2.COLOR_BGR2RGB)



    timer = cv2.getTickCount()
    
    # Read a new frame
    success, frame = video.read()
    if not success:
        # Frame not successfully read from video capture
        break
        
    fgmask = fgbg.apply(frame)
    
    # Apply erosion to clean up noise
    if ERODE:
        fgmask = cv2.erode(fgmask, np.ones((3,3), dtype=np.uint8), iterations=1)


    img = cv2.imread('j.png', 0)
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(img, kernel, iterations=1)
        #where the kernel can be quikly designed with
       # Rectangular Kernel
       >> > cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
       array([[1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1]], dtype=uint8)

       # Elliptical Kernel
       >> > cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
       array([[0, 0, 1, 0, 0],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [0, 0, 1, 0, 0]], dtype=uint8)

       # Cross-shaped Kernel
       >> > cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
       array([[0, 0, 1, 0, 0],
              [0, 0, 1, 0, 0],
              [1, 1, 1, 1, 1],
              [0, 0, 1, 0, 0],
              [0, 0, 1, 0, 0]], dtype=uint8)

    # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)




  cv2.putText(foreground_display, "hand pose: error", positions['hand_pose'], cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    
        
    # Draw bounding box

    cv2.rectangle(foreground_display, p1, p2, (255, 0, 0), 2, 1)

    cv2.circle(display, positions['null_pos'], 5, (0,0,255), -1)

    cv2.line(display,positions['null_pos'],hand_pos,(255,0,0),5)


markers = [cv2.MARKER_CROSS,
           cv2.MARKER_TILTED_CROSS,
           cv2.MARKER_STAR,
           cv2.MARKER_DIAMOND,
           cv2.MARKER_SQUARE,
           cv2.MARKER_TRIANGLE_UP,
           cv2.MARKER_TRIANGLE_DOWN]

img = np.zeros((100,400,3), dtype=np.uint8)
x = 50
for mt in markers:
    img = cv2.drawMarker(img, (x, 50), (0, 0, 255),
                         markerType=mt,
                         markerSize=30,
                         thickness=2,
                         line_type=cv2.LINE_AA)

cap.set(cv2.CAP_PROP_POS_FRAMES, 0) # set frame of video




# trackbars
def nothing(x):
    pass
cap = cv2.VideoCapture(0)
cv2.namedWindow("frame")
cv2.createTrackbar("test", "frame", 50, 500, nothing)
cv2.createTrackbar("color/gray", "frame", 0, 1, nothing)
while True:
    _, frame = cap.read()
    test = cv2.getTrackbarPos("test", "frame")