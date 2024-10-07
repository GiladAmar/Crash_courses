cv2.cvtColor(image.copy(), cv2.COLOR_BGR2RGB)
YCrCb = cv2.cvtColor(Irgb, cv2.COLOR_RGB2YCR_CB)
HSI = cv2.cvtColor(Irgb, cv2.COLOR_RGB2HSV)

def grayscale_to_jet(img_f):
    import cv2

    min_f = img_f[img_f != 0].min()
    max_f = img_f.max()

    img_gray = (img_f + min_f) * 255 / (max_f - min_f)
    img_gray = np.uint8(img_gray)
    img_gray = cv2.applyColorMap(img_gray, cv2.COLORMAP_JET)
    img_gray[img_f == 0] = np.array([0, 0, 0])

    return img_gray

cv2.GaussianBlur(blur_img, (41, 41), 10)
cv2.dilate(dilate_img, np.ones((10,10), dtype=np.uint8), iterations=1)
cv2.erode(erosion_img, np.ones((10,10), dtype=np.uint8), iterations=1)
# Instead of np.ones use cv2 to get the kernel: cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    # cv2.MORPH_ELLIPSE
    # cv2.MORPH_CROSS

# Tone mapping:
hdr = cv2.imread(hdr_path, flags=cv2.IMREAD_ANYDEPTH)
# Tone-mapping and color space conversion ( There are other tone-mapping methods)
tonemap = cv2.createTonemapDrago(2.2)
scale = 5
ldr = scale * tonemap.process(hdr)
# Remap to 0-255 for the bit-depth conversion
cv2.imwrite(ldr_path, ldr * 255)









