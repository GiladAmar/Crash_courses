from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

fig, ax = plt.subplots(figsize=(10,6))
# ax = plt.plot....

date_format = DateFormatter('%Y-%b')
ax.xaxis.set_major_formatter(date_format)
ax.xaxis.set_minor_locator(mdates.MonthLocator())


# Add some room at the top
ax.set_ylim(-20, 15)

# Remove Spines
ax.spines[['top', 'right']].set_visible(False)


# Consider replacing the Title/Substitle with one horizontally left alligned.
# Title in bold
# Subtitle in normal font
# Add Titles
ax.text(
  x=df['Date'].min()-timedelta(20),  # Can be the 'date' location on a Date x-axis
  y=18.5, s='Analyzing Stock Prices',
  ha='left', fontsize=18, weight='bold')
ax.text(
  x=df['Date'].min()-timedelta(20),
  y=16.5, s='April 2022 - Mar 2023',
  ha='left', fontsize=15)