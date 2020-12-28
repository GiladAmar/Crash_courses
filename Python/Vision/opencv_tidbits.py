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
    test = cv2.getTrackbarPos("test", "frameport")

# Convert affine transform to Rotation scale and translation components

a = np.random.random((3, 3))


def affine_to_components(affine_array):
    (a, b, t_x), \
    (c, d, t_y), \
    (_, _, _) = affine_array.tolist()

    #Translation matrix
    T = np.eye(3)
    T[0, 2] = t_x
    T[1, 2] = t_y

    s_x = math.sqrt(a ** 2 + b ** 2)
    s_y = math.sqrt(c ** 2 + d ** 2)

    r_00 = a / s_x
    r_11 = a / s_x

    r_01 = b / s_x
    r_10 = -b / s_x

    #Rotation matrix
    R = np.array([[r_00, r_01, 0],
                  [r_10, r_11, 0],
                  [0,       0, 1]])

    #Scale Matrix
    S = np.multiply(np.eye(3), np.array([[s_x, s_y, 1]]))

    # Translation, Rotation and Scale
    return T, R, S




v4l2-ctl --list-formats-ext -d N
uvcdynctrl -l
vlc v4l2:///dev/videoN:chroma=mjpg:width=1920:height=1080
import cv2


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # for windows backed


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, 1196444237.0) #https://shimat.github.io/opencvsharp_docs/html/5e5a9f7a-b360-809c-b542-799b01ac1aa2.htm

or get number from:
   cv2.VideoWriter_fourcc(*'MJPG')
   -> 1196444237.0

>>> cv2.cv.FOURCC( *"XVID" )    1145656920
>>> cv2.cv.FOURCC( *"MJPG" )    1196444237
>>> cv2.cv.FOURCC( *"X264" )     875967064
>>> cv2.cv.FOURCC( *"DIB " )     541215044
>>> cv2.cv.FOURCC( *"WMV1" )     827739479
>>> cv2.cv.FOURCC( *"WMV2" )     844516695

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)


def grayscale_to_jet(img_f):
    import cv2

    min_f = img_f[img_f != 0].min()
    max_f = img_f.max()

    img_gray = (img_f + min_f) * 255 / (max_f - min_f)
    img_gray = np.uint8(img_gray)
    img_gray = cv2.applyColorMap(img_gray, cv2.COLORMAP_JET)
    img_gray[img_f == 0] = np.array([0, 0, 0])

    return img_gray


import threading
#make a threadsafe generator:
class threadsafe_iter():
    """Takes an iterator/generator and makes it thread-safe by
    serializing call to the `next` method of given iterator/generator.
    """
    def __init__(self, it):
        self.it = it
        self.lock = threading.Lock()

    def __iter__(self):
        return self

    def __next__(self):
        with self.lock:
            return self.it.__next__()


def threadsafe_generator(f):
    """A decorator that takes a generator function and makes it thread-safe.
    """
    def g(*a, **kw):
        return threadsafe_iter(f(*a, **kw))
    return g


@threadsafe_generator
def genny():
    yield 1


#events
   def on_mouse_click(event, x, y, flags, userParams):
       if event == cv2.EVENT_LBUTTONDOWN:
           colorArray[:] = snapshot[y, x, :]
           rgb = snapshot[y, x, [2,1,0]]

           # From stackoverflow/com/questions/1855884/determine-font-color-based-on-background-color
           luminance = 1 - (0.299*rgb[0] + 0.587*rgb[1] + 0.114*rgb[2]) / 255
           if luminance < 0.5:
               textColor = [0,0,0]
           else:
               textColor = [255,255,255]

           cv2.putText(colorArray, str(rgb), (20, COLOR_ROWS - 20),
                       fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8, color=textColor)
           cv2.imshow('Color', colorArray)

   cv2.setMouseCallback('Snapshot', on_mouse_click)




   k = cv2.waitKey(1) & 0xff
   if k == 27:# escape pressed
       break
   elif k == 115: # s pressed
       fname = input("File name")
       cv2.imwrite(os.path.join(IMAGES_FOLDER, '{}.jpg'.format(fname)), frame)
   if k != 255: # A key is pressed
       print(k)



       timer = cv2.getTickCount()

       # Apply erosion to clean up noise
       cv2.erode(fgmask, np.ones((3,3), dtype=np.uint8), iterations=1)

       # Calculate Frames per second (FPS)
       fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)



   cv2.putText(foreground_display, "hand pose: error", positions['hand_pose'], cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)


   # Draw bounding box

   cv2.rectangle(foreground_display, p1, p2, (255, 0, 0), 2, 1)

   cv2.circle(display, positions['null_pos'], 5, (0,0,255), -1)

   cv2.line(display,positions['null_pos'],hand_pos,(255,0,0),5)




   record = True
   if record:
       fps = 10
       capSize = (1200, 675) # Size of video when is resized (original stream 1080x1920)
       fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v') # note the lower case
       vout = cv2.VideoWriter()
       success = vout.open('output.mov', fourcc, fps, capSize, True)
       vout.write(image)


   """
   all of these codecs worked for me on Ubuntu 14.04 and 16.04
       'MJPG' Motion JPEG
       'XVID' MPEG-4
       'FFV1' Lossless
       'FMP4' MPEG-4
   """
   
   
   HSI = cv2.cvtColor(Irgb, cv2.COLOR_RGB2HSV)
   H = HSI[:,:,0]
   S = HSI[:,:,1]
   I = HSI[:,:,2]
   
   YCrCb = cv2.cvtColor(Irgb, cv2.COLOR_RGB2YCR_CB)
   
   cv2.namedWindow(name)
   # Resize it to the size of the camera image
       cv2.resizeWindow(name, self.cam_width, self.cam_height)
   # Move to (xpos,ypos) on the screen
       cv2.moveWindow(name, xpos, ypos)
   
   cv2.useOptimized()
   cv2.setUseOptimized(True)
   
   cv2.GaussianBlur(blur_img, (41, 41), 10)
   
   cv2.cvtColor(image.copy(), cv2.COLOR_BGR2RGB)
   
   cv2.dilate(dilate_img, np.ones((10,10), dtype=np.uint8), iterations=1)
   erosion_img = cv2.erode(erosion_img, np.ones((10,10), dtype=np.uint8), iterations=1)
   
   # Align input images
       alignMTB = cv2.createAlignMTB()
       alignMTB.process(images, images)
   
   #HDR
       mergeMertens = cv2.createMergeMertens()
       exposureFusion = mergeMertens.process(images)
   
   
   def adjust_gamma(image, gamma=1.0):
       # build a lookup table mapping the pixel values [0, 255] to
       # their adjusted gamma values
       invGamma = 1.0 / gamma
       table = np.array([((i / 255.0) ** invGamma) * 255
           for i in np.arange(0, 256)]).astype("uint8")
    
       # apply gamma correction using the lookup table
       return cv2.LUT(image, table)
   
   
   #Multi-scale template matching:
   
   
   # loop over the images to find the template in
   for imagePath in glob.glob(args["images"] + "/*.jpg"):
       # load the image, convert it to grayscale, and initialize the
       # bookkeeping variable to keep track of the matched region
       image = cv2.imread(imagePath)
       gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
       found = None
    
       # loop over the scales of the image
       for scale in np.linspace(0.2, 1.0, 20)[::-1]:
           # resize the image according to the scale, and keep track
           # of the ratio of the resizing
           resized = imutils.resize(gray, width = int(gray.shape[1] * scale))
           r = gray.shape[1] / float(resized.shape[1])
    
           # if the resized image is smaller than the template, then break
           # from the loop
           if resized.shape[0] < tH or resized.shape[1] < tW:
               break
   
           # detect edges in the resized, grayscale image and apply template
           # matching to find the template in the image
           edged = cv2.Canny(resized, 50, 200)
           result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
           (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
    
           # check to see if the iteration should be visualized
           if args.get("visualize", False):
               # draw a bounding box around the detected region
               clone = np.dstack([edged, edged, edged])
               cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
                   (maxLoc[0] + tW, maxLoc[1] + tH), (0, 0, 255), 2)
               cv2.imshow("Visualize", clone)
               cv2.waitKey(0)
    
           # if we have found a new maximum correlation value, then ipdate
           # the bookkeeping variable
           if found is None or maxVal > found[0]:
               found = (maxVal, maxLoc, r)
    
       # unpack the bookkeeping varaible and compute the (x, y) coordinates
       # of the bounding box based on the resized ratio
       (_, maxLoc, r) = found
       (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
       (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
    
       # draw a bounding box around the detected result and display the image
       cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
       cv2.imshow("Image", image)
       cv2.waitKey(0)
   
   # import the necessary packages
   import numpy as np
   import argparse
   import glob
   import cv2
    
   from skimage.measure import structural_similarity as ssim
   s = ssim(imageA, imageB)
   
   # Create depth map from stero images:
       stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
       disparity = stereo.compute(imgL,imgR)
       plt.imshow(disparity,'gray')
       plt.show()
   
   
   ###################################################################################
   
   
   
   
   
   
   cv2.imwrite(image_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
   
   
   
   
   
   
   
   
   
   def _find_contours(image):
       """
   Helper function for finding contours of image.
   Returns coordinates of contours.
   """
   # Increase constrast in image to increase changes of finding
   # contours.
   processed = _increase_contrast(image)

   # Get the gray-scale of the image.
   gray = cv2.cvtColor(processed, cv2.COLOR_BGR2GRAY)

   # Detect contour(s) in the image.
   cnts = cv2.findContours(
       gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
   center = None

   # At least ensure that some contours were found.
   if len(cnts) > 0:
       # Find the largest contour in the mask.
       c = max(cnts, key=cv2.contourArea)
       ((x, y), radius) = cv2.minEnclosingCircle(c)

       # Assume the radius is of a certain size.
       if radius > 100:
           M = cv2.moments(c)
           center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

           return (center, radius)




#Handling Transparency:
# Read the images
foreground = cv2.imread("puppets.png")
background = cv2.imread("ocean.png")
alpha = cv2.imread("puppets_alpha.png")

# Convert uint8 to float
foreground = foreground.astype(float)
background = background.astype(float)

# Normalize the alpha mask to keep intensity between 0 and 1
alpha = alpha.astype(float)/255

# Multiply the foreground with the alpha matte
foreground = cv2.multiply(alpha, foreground)

# Multiply the background with ( 1 - alpha )
background = cv2.multiply(1.0 - alpha, background)

# Add the masked foreground and background.
outImage = cv2.add(foreground, background)



#Seamless cloning region on source(identified with mask to target image)
output = cv2.seamlessClone(src, dst, mask, center, cv2.NORMAL_CLONE)
    cv2.MIXED_CLONE





#Simple perspective transform:
   pts_src = np.array([[141, 131], [480, 159], [493, 630],[64, 601]], dtype=float)


   # Read destination image.
   im_dst = cv2.imread('book1.jpg')
   # Four corners of the book in destination image.
   pts_dst = np.array([[318, 256],[534, 372],[316, 670],[73, 473]], dtype=float)

   # Calculate Homography
   h, status = cv2.findHomography(pts_src, pts_dst)

   # Warp source image to destination based on homography
   im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))






#Reading Images:
# Read 8-bit grayscale image
   im = cv2.imread("earth-16-bit-per-channel.png", cv2.IMREAD_GRAYSCALE)

# Read 8-bit color image
   cv2.IMREAD_COLOR

# Read 16-bit color image
   cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH 

# Read transparent PNG / TIFF image
   cv2.IMREAD_UNCHANGED



















# COntours:
   # find contours
   coins_contours, _ = cv2.findContours(coins_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

   # make copy of image
   coins_and_contours = np.copy(coins)

   # find contours of large enough area
   min_coin_area = 60
   large_contours = [cnt for cnt in coins_contours if cv2.contourArea(cnt) > min_coin_area]

   # draw contours
   cv2.drawContours(coins_and_contours, large_contours, -1, (255,0,0))


#Bounding Rectangles
       
   for contour in large_contours:
       x, y, w, h = cv2.boundingRect(contour)
       cv2.rectangle(bounding_img, (x, y), (x + w, y + h), (0, 255, 0), 3)



# Hough transform:

# copy of image to draw lines
   ines = np.copy(cups)

# find hough lines
   num_pix_threshold = 110 # minimum number of pixels that must be on a line
   lines = cv2.HoughLines(cups_edges, 1, np.pi/180, num_pix_threshold)

for rho, theta in lines[0]:
   # convert line equation into start and end points of line
   a = np.cos(theta)
   b = np.sin(theta)
   x0 = a * rho
   y0 = b * rho

   x1 = int(x0 + 1000*(-b))
   y1 = int(y0 + 1000*(a))

   x2 = int(x0 - 1000*(-b))
   y2 = int(y0 - 1000*(a))

   cv2.line(cups_lines, (x1,y1), (x2,y2), (0,0,255), 1)


Hough Circles:

   # find hough circles
   circles = cv2.HoughCircles(cups_edges, cv2.cv.CV_HOUGH_GRADIENT, dp=1.5, minDist=50, minRadius=20, maxRadius=130)
   cups_circles = np.copy(cups)

   # if circles are detected, draw them
   if circles is not None and len(circles) > 0:
       # note: cv2.HoughCircles returns circles nested in an array.
       # the OpenCV documentation does not explain this return value format
       circles = circles[0]
       for (x, y, r) in circles:
           x, y, r = int(x), int(y), int(r)
           cv2.circle(cups_circles, (x, y), r, (255, 255, 0), 4)
       plt.imshow(cv2.cvtColor(cups_circles, cv2.COLOR_BGR2RGB))

   print('number of circles detected: %d' % len(circles[0]))











####################Filters################################

def _increase_contrast(image):
   """
   Helper function for increasing contrast of image.
   """
   # Create a local copy of the image.
   copy = image.copy()

   maxIntensity = 255.0
   x = arange(maxIntensity)

   # Parameters for manipulating image data.
   phi = 1.3
   theta = 1.5
   y = (maxIntensity/phi)*(x/(maxIntensity/theta))**0.5

   # Decrease intensity such that dark pixels become much darker,
   # and bright pixels become slightly dark.
   copy = (maxIntensity/phi)*(copy/(maxIntensity/theta))**2
   copy = array(copy, dtype=uint8)

   return copy

def equalize_hist(img, cast_to_black=False, debug=False):
   if len(img.shape) >= 3:
       if debug: print('Warning: Equalize hist on colour img')

       img[:, :, 0] = cv2.equalizeHist(img[:, :, 0])
       img[:, :, 1] = cv2.equalizeHist(img[:, :, 1])
       img[:, :, 2] = cv2.equalizeHist(img[:, :, 2])
       return img
   else:

   return cv2.equalizeHist(img)


def show_hsv_equalized(image):
   H, S, V = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
   eq_V = cv2.equalizeHist(V)
   eq_image = cv2.cvtColor(cv2.merge([H, S, eq_V]), cv2.COLOR_HSV2RGB)
   plt.imshow(eq_image)
   plt.show()


#Skeletonize:
def skeletonize(image, size, structuring=cv2.MORPH_RECT):
   # determine the area (i.e. total number of pixels in the image),
   # initialize the output skeletonized image, and construct the
   # morphological structuring element
   area = image.shape[0] * image.shape[1]
   skeleton = np.zeros(image.shape, dtype="uint8")
   elem = cv2.getStructuringElement(structuring, size)

   # keep looping until the erosions remove all pixels from the
   # image
   while True:
       # erode and dilate the image using the structuring element
       eroded = cv2.erode(image, elem)
       temp = cv2.dilate(eroded, elem)

       # subtract the temporary image from the original, eroded
       # image, then take the bitwise 'or' between the skeleton
       # and the temporary image
       temp = cv2.subtract(image, temp)
       skeleton = cv2.bitwise_or(skeleton, temp)
       image = eroded.copy()

       # if there are no more 'white' pixels in the image, then
       # break from the loop
       if area == area - cv2.countNonZero(image):
           break

   # return the skeletonized image
   return skeleton

#Thresholding:
   # Basic threhold example 
       th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY); 

   # Thresholding using THRESH_BINARY_INV 
       cv2.THRESH_BINARY_INV

   # Thresholding using THRESH_TRUNC 
       cv2.THRESH_TRUNC

   # Thresholding using THRESH_TOZERO 
       cv2.THRESH_TOZERO

   # Thresholding using THRESH_TOZERO_INV 
       cv2.THRESH_TOZERO_INV



# SWT:
   rewuires PIL image
   Stroke Width Transform
   img_out = pillowfight.swt(img_in, output_type=pillowfight.SWT_OUTPUT_ORIGINAL_BOXES)

or https://github.com/marrrcin/swt-python
   import ccvwrapper
   import numpy as np
   swt_result_raw = ccvwrapper.swt(open("test_input.jpg", "rb").read(), len(bytes), 1024, 1360)
   swt_result = np.reshape(swt_result_raw, (len(swt_result_raw) / 4, 4))


from skimage import exposure



# SOBEL
   from scipy import ndimage
   sx = ndimage.sobel(source_image, axis=0, mode='constant')  # x-axis
   sy = ndimage.sobel(source_image, axis=1, mode='constant')  # y-axis
   s = np.sqrt(sx ** 2 + sy ** 2)                             # magnitude
   filtered_image = s / np.max(filtered_image) * 255.0        # normalize the result





   def get_gradient(im) :
       # Calculate the x and y gradients using Sobel operator
       grad_x = cv2.Sobel(im,cv2.CV_32F,1,0,ksize=3)
       grad_y = cv2.Sobel(im,cv2.CV_32F,0,1,ksize=3)
       # Combine the two gradients
       grad = cv2.addWeighted(np.absolute(grad_x), 0.5, np.absolute(grad_y), 0.5, 0)
       return grad

#CANNY
def auto_canny(image, sigma=0.33):
   # compute the median of the single channel pixel intensities
   v = np.median(image)

   # apply automatic Canny edge detection using the computed median
   lower = int(max(0, (1.0 - sigma) * v))
   upper = int(min(255, (1.0 + sigma) * v))
   edged = cv2.Canny(image, lower, upper)

   # return the edged image
   return edged



contrast hue brightness saturation

def contrast_stretch(img, pmin, pmax):
   pmin, pmax = np.percentile(img, (pmin, pmax))
   img_rescale = exposure.rescale_intensity(img, in_range=(pmin, pmax))
   return img_rescale
   
   
   
Salieny map:
       
    import cv2
    import matplotlib.pyplot as plt
    
    fname = 'IMG_20190605_185730.jpg'
    
    image = cv2.imread(fname)
    
    # initialize OpenCV's static fine grained saliency detector and
    # compute the saliency map
    saliency = cv2.saliency.StaticSaliencyFineGrained_create()
    (success, saliencyMap) = saliency.computeSaliency(image)
    
    saliency_spectral = cv2.saliency.StaticSaliencySpectralResidual_create()
    
    (success, saliencyMap_spectral) = saliency_spectral.computeSaliency(image)
     
    # if we would like a *binary* map that we could process for contours,
    # compute convex hull's, extract bounding boxes, etc., we can
    # additionally threshold the saliency map
    threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
     
    # show the images
    plt.imshow(saliencyMap)
    plt.show()
    
    plt.imshow(saliencyMap_spectral)
    plt.show()
    
    
    # 1920x1080 - 2MP: 
        # 1.37ms
        # 350ms
    
    # 3264x2448 - 8MP 
        # 4.32ms
        # 1.43s
        
        
#Write Video:
   import cv2

    
    def video_processing(filename):
      cap = cv2.VideoCapture(filename)
      frame_width = int(cap.get(3))
      frame_height = int(cap.get(4))
    
      out = cv2.VideoWriter("/home/giladamar/Desktop/out.avi",
                            cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                            10,
                            (frame_width, frame_height))
    
      while True:
            ret, frame = cap.read()
    
            if ret == True:
                grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                out.write(grayFrame)
    
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
      cap.release()
      out.release()
      cv2.destroyAllWindows()
      print("Video successfully saved")
    
    _filename = "/home/giladamar/Desktop/VID_20181017_141954.mp4"
    video_processing(_filename)



# Multi thread video read and write:
    import time
    import cv2
    from concurrent.futures import ProcessPoolExecutor
    pool = ProcessPoolExecutor(max_workers=2)

    def read_and_write(camera, filename):
        cap = cv2.VideoCapture(camera)
        writer = cv2.VideoWriter(filename)

        for i in range(1000):
            ret, frame = cap.read()
            writer.write(frame)
        return True

    future_1 = pool.submit(read_and_write, 1, "out1.avi")
    future_2 = pool.submit(read_and_write, 2, "out2.avi")

    while not (future_1.done() and future_2.done()):
        print("still running")
        time.sleep(1)

# use of different fonts
ft = cv2.freetype.createFreeType2()
ft.loadFontData(fontFileName='Ubuntu-R.ttf',
                id=0)
ft.putText(img=img,
           text='Quick Fox',
           org=(15, 70),
           fontHeight=60,
           color=(255,  255, 255),
           thickness=-1,
           line_type=cv2.LINE_AA,
           bottomLeftOrigin=True)
