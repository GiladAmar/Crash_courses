import matplotlib.pyplot as plt

fig = plt.figure()

# Easy way to make subplots in any configuration you like

subplots = fig.subplot_mosaic(
    """
    a.c 
    bbb
    .d.
    """)
# . is an empty cell
# d will be in the center
# b will occupy the whole row
subplots['a'] = ...
subplots['b'] = ...
subplots['c'] = ...
subplots['d'] = ...