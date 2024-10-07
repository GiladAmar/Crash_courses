import cv2

# Markers
markers = [cv2.MARKER_CROSS,
           cv2.MARKER_TILTED_CROSS,
           cv2.MARKER_STAR,
           cv2.MARKER_DIAMOND,
           cv2.MARKER_SQUARE,
           cv2.MARKER_TRIANGLE_UP,
           cv2.MARKER_TRIANGLE_DOWN]


cv2.drawMarker(img, (x, 50), (0, 0, 255),
                         markerType=markers[0],
                         markerSize=30,
                         thickness=2,
                         line_type=cv2.LINE_AA)

# Shapes
cv2.rectangle(foreground_display, p1, p2, (255, 0, 0), 2, 1)

cv2.circle(display, positions['null_pos'], 5, (0,0,255), -1)

cv2.line(display,positions['null_pos'],hand_pos,(255,0,0),5)

# Text
cv2.putText(img=img,
           text='Quick Fox',
           org=(15, 70),
           fontHeight=60,
           color=(255,  255, 255),
           thickness=-1,
           line_type=cv2.LINE_AA,
           bottomLeftOrigin=True)
# use of different fonts # TODO
ft = cv2.freetype.createFreeType2()
ft.loadFontData(fontFileName='Ubuntu-R.ttf',
                id=0)


#Border:
image = cv2.copyMakeBorder(image,
                           epn_width, epn_width, epn_width, epn_width,
                           cv2.BORDER_CONSTANT, value=[0, 0, 0])