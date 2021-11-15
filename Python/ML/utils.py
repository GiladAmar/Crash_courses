from math import cos, sin, radians
import numpy as np
import cv2
import pandas as pd

from config import Config

config = Config()
import json

import matplotlib
if config.use_agg_backend:
    matplotlib.use('Agg')

import matplotlib.pyplot as plt


def reshape_to_ratio(img, ratio, expand_to_fit=True):
    '''Reshape an img to fit ratio=(width, height).
    The shape will be expanded in one dimension only.
    Whichever dimension will accomplish the final ratio after an expansion'''
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

        black_img = np.zeros((h_new, w_new, channels), dtype='uint8')
        black_img[offset: offset + in_h] = img
    elif img_ratio > ratio and (img_ratio - ratio) > 0.01:
        # width is too small
        h_new = in_h
        w_new = int(in_w * ratio)
        offset = (w_new - in_w) // 2

        black_img = np.zeros((h_new, w_new, channels), dtype='uint8')
        black_img[:, offset: offset + in_w] = img
    else:
        black_img = img

    return black_img


# def transform by pts
def perspective_transform(image, pts, target_pts=None, out_shape=None):
    """transform any parallelogram into a rectangle with similar aspect ratio"""
    M, status = cv2.findHomography(pts, target_pts)
    im_dst = cv2.warpPerspective(image, M, out_shape)
    return im_dst, M, status


def plot_keypoints(images, keypoints, confidences=None, save_file=None):
    if confidences is None:
        confidences = np.ones((len(keypoints), 1))
        # TODO show confidence

    for image, keypoint, conf in zip(images, keypoints, confidences):
        x, y = keypoint[:, 0], keypoint[:, 1]
        fig = plt.figure()
        ax = fig.add_subplot(111)

        if len(image.shape) == 3:
            plt.imshow(image[:, :, 0], cmap='gray')
        else:
            plt.imshow(image, cmap='gray')
        for label, (i, j, c) in enumerate(zip(x, y, 'bgrcmykwbgrcmykwbgrcmykw')):
            plt.plot(i, j, '{}x'.format(c), markersize=5)
        if save_file:
            plt.savefig(save_file, bbox_inches='tight')
        else:
            plt.show(block=True)
        plt.close()


def plot_superimposed_heatmaps(src_img, heatmaps, save_to_fname=None, keypoints=None):
    """ src img shape [h, w]
        heatmaps shape [h, w, n_keypoints]
    """
    Nplot = heatmaps.shape[2]

    fig = plt.figure(figsize=(20, 5))
    plt.subplot(1, Nplot + 1, 1)

    if keypoints is not None:
        for x, y in zip(keypoints[:, 0], keypoints[:, 1]):
            src_img = cv2.circle(src_img.copy(), (int(x), int(y)), 5, (0, 0, 255), 1)
    plt.imshow(src_img, cmap="gray")
    for j in range(Nplot):
        plt.subplot(1, Nplot + 1, j + 2)
        plt.imshow(heatmaps[:, :, j], cmap="gray")

    if save_to_fname is not None:
        plt.savefig(save_to_fname)
    plt.show(block=True)
    plt.close()


def hsv_equalize(image):
    H, S, V = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
    eq_V = cv2.equalizeHist(V)
    eq_image = cv2.cvtColor(cv2.merge([H, S, eq_V]), cv2.COLOR_HSV2BGR)
    return eq_image


def apply_to_imgs(imgs, operations):
    out_array = imgs.copy()
    if type(operations) == list:
        for operation in operations:
            out_array = np.array([operation(img) for img in out_array])
    else:
        out_array = np.array([operations(img) for img in out_array])
    return out_array


def img_to_batch(img, operation=nothing, n=8):
    return np.array([operation(img)] * n)


boxprops = dict(linewidth=1.0, color='black')
whiskerprops = dict(linestyle='--', linewidth=1.0, color='y')


def boxplot(df, x, y, x_title=None, y_title=None, figsize=(6, 6), showfliers=True):
    if x_title is None:
        x_title = x

    if y_title is None:
        y_title = y
    plt.figure(figsize=(5, 5))

    df.dropna().boxplot(column=[y], by=[x],
                        showfliers=showfliers,
                        figsize=figsize,
                        rot=90,
                        sym='r+',
                        boxprops=boxprops,
                        whiskerprops=whiskerprops)
    plt.tight_layout()
    plt.suptitle("")

    plt.ylabel(y_title, fontsize=18)
    plt.xlabel(x_title, fontsize=18)
    plt.title('')
    plt.show()


def threshold_population_curve(df, threshold, y_error,
                               thresh_title=None, y_title=None,
                               reverse_threshold=False,
                               xlim=None):
    if thresh_title is None:
        thresh_title = threshold
    if y_title is None:
        y_title = y_error

    mean_error = []
    remaining_population = []

    for i in np.unique(df[threshold]):
        if reverse_threshold:
            df_remainder = df[df[threshold] < i]
        else:
            df_remainder = df[df[threshold] > i]

        try:
            error = np.percentile(df_remainder[y_error], 95)
        except IndexError as e:
            print(e)
            error = 0

        mean_error.append([i, error])
        remaining_population.append([i, df_remainder.shape[0] / df.shape[0]])
        if remaining_population[-1][1] < 0.2 and reverse_threshold is False:
            break

    mean_error = np.array(mean_error)
    remaining_population = np.array(remaining_population)

    df_tmp = pd.DataFrame(columns=[thresh_title, y_title])
    df_tmp[thresh_title] = mean_error[:, 0]
    df_tmp[y_title] = mean_error[:, 1]
    df_tmp['Population Remaining (%)'] = remaining_population[:, 1]

    ax = df_tmp.plot(thresh_title, 'Population Remaining (%)')
    plt.ylabel('Population Remaining (%)', fontsize=16)
    plt.xlabel(thresh_title, fontsize=16)
    if xlim is not None:
        plt.xlim(*xlim)
    plt.ylim(ymin=0.1)

    ax = df_tmp.plot(thresh_title, y_title, secondary_y=y_title, ax=ax)

    plt.xlabel(thresh_title, fontsize=16)

    plt.ylabel(y_title, fontsize=16)
    if xlim is not None:
        plt.xlim(*xlim)


class NDArrayEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def jsonify(input):
    return json.dumps(input, cls=NDArrayEncoder, indent=4)

