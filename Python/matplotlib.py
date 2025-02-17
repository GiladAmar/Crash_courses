# Text
ax.text(
  x=xmax-0.5, y=ymax-2, s='High frequency, high amount',
  color='darkgreen', ha='right', va='top')

# Shade Region
ax.axhspan(
  ymin=0, ymax=y.mean(), xmin=0, xmax=x_mean_fraction,
  alpha=0.25, color='pink')

# Add arrow
ax.annotate(
    text='The sweet spot', xy=(20, 170), xytext=(30, 200),
    arrowprops={'facecolor': 'black', 'arrowstyle': '->',
      'connectionstyle': 'arc3,rad=0.2',}
  )

# Remove top and right spine
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)