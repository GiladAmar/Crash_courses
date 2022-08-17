pandas apply numba functopns with apply(numb, fun, egnine='numba',raw=True)

df.convert_dtypes


from pandas.core.arrays.string.string_arrow import (ArrowStringArray,
                                                    ArrowStringDtype)

contains( regex=False)


df['arrow str'] = df.arrow_str.astype(ArrowStringDtype())


https://pandas.pydata.org/pandas-docs/stable/user_guide/enhancingperf.html
https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html#install-recommended-dependencies






Nowadays, plotly is becoming vastly popular, so it would be nice to set it as default plotting backed for pandas. By doing so, you will get interactive plotly diagrams whenever you call .plot on pandas DataFrames:
pd.set_option(‘plotting.backend’, ‘plotly’)





 %load_ext autoreload

In [2]: %autoreload 2


cv.CAP_PROP_ORIENTATION_AUTO
