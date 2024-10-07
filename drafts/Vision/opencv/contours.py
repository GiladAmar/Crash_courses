
# Contours:
contours, _ = cv2.findContours(coins_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

areas = [cv2.contourArea(cnt) for cnt in contours]

cv2.drawContours(contours, large_contours, -1, (255 ,0 ,0)) # TODO

# Bounding Shapes
x, y, w, h = cv2.boundingRect(contour)
((x, y), radius) = cv2.minEnclosingCircle(c)
cv2.rectangle(bounding_img, (x, y), (x + w, y + h), (0, 255, 0), 3)



# Hough transform:

# copy of image to draw lines
ines = np.copy(cups)

# find hough lines
num_pix_threshold = 110 # minimum number of pixels that must be on a line
lines = cv2.HoughLines(cups_edges, 1, np.pi /180, num_pix_threshold)
# find hough circles
# circles = cv2.HoughCircles(cups_edges, cv2.cv.CV_HOUGH_GRADIENT, dp=1.5, minDist=50, minRadius=20, maxRadius=130)

for rho, theta in lines[0]:
    # convert line equation into start and end points of line
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho

    x1 = int(x0 + 100.0 *(-b))
    y1 = int(y0 + 100.0 *(a))

    x2 = int(x0 - 100.0 *(-b))
    y2 = int(y0 - 100.0 *(a))

    cv2.line(cups_lines, (x1 ,y1), (x2 ,y2), (0 ,0 ,255), 1)

