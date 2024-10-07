
# Not used here but useful function to be included in Crash courses
def fig2data(fig):
    """
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    # draw the renderer
    fig.canvas.draw()

    # Get the RGBA buffer from the figure
    w, h = fig.canvas.get_width_height()
    buf = np.fromstring(fig.canvas.tostring_argb(), dtype=np.uint32)
    buf.shape = (w, h, 1)

    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    output = np.roll(buf, 3, axis=2)
    return output / ( 2**32 - 1)



def threshold_population_curve(
        df,
        threshold,
        y_error,
        thresh_title=None,
        y_title=None,
        reverse_threshold=False,
        xlim=None,
):
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
    df_tmp["Population Remaining (%)"] = remaining_population[:, 1]

    ax = df_tmp.plot(thresh_title, "Population Remaining (%)")
    plt.ylabel("Population Remaining (%)", fontsize=16)
    plt.xlabel(thresh_title, fontsize=16)
    if xlim is not None:
        plt.xlim(*xlim)
    plt.ylim(ymin=0.1)

    ax = df_tmp.plot(thresh_title, y_title, secondary_y=y_title, ax=ax)

    plt.xlabel(thresh_title, fontsize=16)

    plt.ylabel(y_title, fontsize=16)
    if xlim is not None:
        plt.xlim(*xlim)




boxprops = dict(linewidth=1.0, color="black")
whiskerprops = dict(linestyle="--", linewidth=1.0, color="y")


def boxplot(df, x, y, x_title=None, y_title=None, figsize=(6, 6), showfliers=True):
    if x_title is None:
        x_title = x

    if y_title is None:
        y_title = y
    plt.figure(figsize=(5, 5))

    df.dropna().boxplot(
        column=[y],
        by=[x],
        showfliers=showfliers,
        figsize=figsize,
        rot=90,
        sym="r+",
        boxprops=boxprops,
        whiskerprops=whiskerprops,
    )
    plt.tight_layout()
    plt.suptitle("")

    plt.ylabel(y_title, fontsize=18)
    plt.xlabel(x_title, fontsize=18)
    plt.title("")
    plt.show()




def plot_keypoints(images, keypoints, confidences=None, save_file=None):
    if confidences is None:
        confidences = np.ones((len(keypoints), 1))
        # TODO show confidence

    for image, keypoint, conf in zip(images, keypoints, confidences):
        x, y = keypoint[:, 0], keypoint[:, 1]
        fig = plt.figure()
        ax = fig.add_subplot(111)

        if len(image.shape) == 3:
            plt.imshow(image[:, :, 0], cmap="gray")
        else:
            plt.imshow(image, cmap="gray")
        for label, (i, j, c) in enumerate(zip(x, y, "bgrcmykwbgrcmykwbgrcmykw")):
            plt.plot(i, j, "{}x".format(c), markersize=5)
        if save_file:
            plt.savefig(save_file, bbox_inches="tight")
        else:
            plt.show(block=True)
        plt.close()


def plot_superimposed_heatmaps(src_img, heatmaps, save_to_fname=None, keypoints=None):
    """src img shape [h, w]
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



#plot image matrix:
def plot_multiple_img(img_matrix_list, title_list, ncols, main_title=""):
    fig, myaxes = plt.subplots(figsize=(20, 15), nrows=1, ncols=ncols, squeeze=False)
    fig.suptitle(main_title, fontsize = 30)
    fig.subplots_adjust(wspace=0.3)
    fig.subplots_adjust(hspace=0.3)
    for i, (img, title) in enumerate(zip(img_matrix_list, title_list)):
        myaxes[i // ncols][i % ncols].imshow(img)
        myaxes[i // ncols][i % ncols].set_title(title, fontsize=15)
    plt.show()
