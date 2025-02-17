apply, applymap, map, iterrows, and itertuples


# DataFrame of stock prices
stocks_df = pd.DataFrame(
    columns=['date', 'company', 'price', 'volume']
)


threshold = 1e5


# Rows where the average volume for a company 
# is greater than some threshold
result = df.query(
    '(volume.groupby(company).transform("mean") > @threshold)'
)


# Set the default plotting backend to Plotly
pd.options.plotting.backend = 'plotly'


# Group by a date column, use a monthly frequency 
# and find the total revenue for `category`


grouped = df.groupby(['category', pd.Grouper(key='date', freq='M')])
monthly_revenue = grouped['revenue'].sum()


https://towardsdatascience.com/how-to-boost-pandas-speed-and-process-10m-row-datasets-in-milliseconds-48d5468e269


vectorisation speed up


pandas crosstab:
https://towardsdatascience.com/meet-the-hardest-functions-of-pandas-part-ii-f8029a2b0c9b
