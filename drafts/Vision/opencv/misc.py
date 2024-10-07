cv2.useOptimized()
cv2.setUseOptimized(True)

# Align input images
alignMTB = cv2.createAlignMTB()
alignMTB.process(images, images)

# HDR
mergeMertens = cv2.createMergeMertens()
exposureFusion = mergeMertens.process(images)


# Structural Similarity
from skimage.measure import structural_similarity as ssim

s = ssim(imageA, imageB)

# Stereo to depth map
stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)


def mix_images(img1, img2, alpha_map):
    # Convert uint8 to float
    foreground = img1.astype(float)
    background = img2.astype(float)

    # Normalize the alpha mask to keep intensity between 0 and 1
    alpha = alpha_map.astype(float) / 255

    foreground = cv2.multiply(alpha, foreground)
    background = cv2.multiply(1.0 - alpha, background)

    # Add the masked foreground and background.
    return cv2.add(foreground, background)


# Seamless cloning region on source(identified with mask to target image)
output = cv2.seamlessClone(src, dst, mask, center, cv2.NORMAL_CLONE)
    # cv2.MIXED_CLONE


def get_black_or_white_font(background_rbg):
    # From stackoverflow/com/questions/1855884/determine-font-color-based-on-background-color
    luminance = 1 - (0.299 * background_rbg[0] + 0.587 * background_rbg[1] + 0.114 * background_rbg[2]) / 255
    if luminance < 0.5:
        text_color = [0, 0, 0]
    else:
        text_color = [255, 255, 255]
    return text_color