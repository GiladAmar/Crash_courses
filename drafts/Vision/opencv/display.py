cv2.namedWindow(frame_name)
cv2.resizeWindow(frame_name, width, height)
cv2.moveWindow(frame_name, xpos, ypos)
cv2.destroyAllWindows()


# trackbars
def nothing(x):
    pass

cv2.createTrackbar("trackbar_name", frame_name, 50, 500, nothing)
while True:
    _, frame = cap.read()
    test = cv2.getTrackbarPos("trackbar_name", "frameport")


# Events
def on_mouse_click(event, x, y, flags, user_params):
   if event == cv2.EVENT_LBUTTONDOWN:
       pass

cv2.setMouseCallback('Snapshot', on_mouse_click)



