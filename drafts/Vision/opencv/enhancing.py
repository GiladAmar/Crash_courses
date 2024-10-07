


import cv2

# Saliency map:
saliency = cv2.saliency.StaticSaliencyFineGrained_create()
(success, saliencyMap) = saliency.computeSaliency(image)

saliency_spectral = cv2.saliency.StaticSaliencySpectralResidual_create()

(success, saliencyMap_spectral) = saliency_spectral.computeSaliency(image)

# if we would like a *binary* map that we could process for contours,
# compute convex hull's, extract bounding boxes, etc., we can
# additionally threshold the saliency map
threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,
                          cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# SOBEL edge detector
from scipy import ndimage
from skimage import exposure

sx = ndimage.sobel(source_image, axis=0, mode='constant')  # x-axis
sy = ndimage.sobel(source_image, axis=1, mode='constant')  # y-axis
s = np.sqrt(sx ** 2 + sy ** 2)  # magnitude


def get_gradient(im):
    # Calculate the x and y gradients using Sobel operator
    grad_x = cv2.Sobel(im, cv2.CV_32F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(im, cv2.CV_32F, 0, 1, ksize=3)
    # Combine the two gradients
    grad = cv2.addWeighted(np.absolute(grad_x), 0.5, np.absolute(grad_y), 0.5, 0)
    return grad


# CANNY
def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged


contrast
hue
brightness
saturation


def contrast_stretch(img, pmin, pmax):
    pmin, pmax = np.percentile(img, (pmin, pmax))
    img_rescale = exposure.rescale_intensity(img, in_range=(pmin, pmax))
    return img_rescale


def adjust_gamma(image, gamma=1.0):
   # build a lookup table mapping the pixel values [0, 255] to
   # their adjusted gamma values
   invGamma = 1.0 / gamma
   table = np.array([((i / 255.0) ** invGamma) * 255
       for i in np.arange(0, 256)]).astype("uint8")

   # apply gamma correction using the lookup table
   return cv2.LUT(image, table)


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


def hsv_equalize(image):
    H, S, V = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
    eq_V = cv2.equalizeHist(V)
    eq_image = cv2.cvtColor(cv2.merge([H, S, eq_V]), cv2.COLOR_HSV2BGR)
    return eq_image


# Reused image functions:
def equalize_histogram(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # print(image.shape)
    if image is not None:
        cl1 = clahe.apply(image)
        # print(cl1.shape)
        return cl1
    else:
        return None

