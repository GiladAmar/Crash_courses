
def reshape_to_ratio(img, ratio, expand_to_fit=True):
    """Reshape an img to fit ratio=(width, height).
    The shape will be expanded in one dimension only.
    Whichever dimension will accomplish the final ratio after an expansion"""
    height, width = img.shape[0:2]

    img_ratio = height / width
    chosen_ratio = ratio[1] / ratio[0]

    if expand_to_fit:
        if img_ratio < chosen_ratio:
            img = cv2.resize(img, (width, int(chosen_ratio * width)))
        else:
            img = cv2.resize(img, (round(height / chosen_ratio), height))
    else:
        raise NotImplementedError
    return img


def pad_to_ratio(img, ratio, channels=None):
    in_h, in_w = img.shape[0:2]
    if channels is None and len(img.shape) == 3:
        channels = img.shape[2]

    img_ratio = in_h / in_w
    if img_ratio < ratio and (img_ratio - ratio) > 0.01:
        # height is too small
        h_new = in_h // ratio
        w_new = in_w
        offset = (h_new - in_h) // 2

        black_img = np.zeros((h_new, w_new, channels), dtype="uint8")
        black_img[offset : offset + in_h] = img
    elif img_ratio > ratio and (img_ratio - ratio) > 0.01:
        # width is too small
        h_new = in_h
        w_new = int(in_w * ratio)
        offset = (w_new - in_w) // 2

        black_img = np.zeros((h_new, w_new, channels), dtype="uint8")
        black_img[:, offset : offset + in_w] = img
    else:
        black_img = img

    return black_img


# def transform by pts
def perspective_transform(image, pts, target_pts=None, out_shape=None):
    """transform any parallelogram into a rectangle with similar aspect ratio"""
    M, status = cv2.findHomography(pts, target_pts)
    im_dst = cv2.warpPerspective(image, M, out_shape)
    return im_dst, M, status

