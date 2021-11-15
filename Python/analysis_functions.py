def find_matches(df, col1, col2):
    # find relationships between category columns

    unique_matches_df = df[col1, col2].drop_duplicates()

    unique_matches_df.sort_values([col1.col2]).reset_index()
    return


# Explore column relationships
from itertools import combinations

species = ['cat', 'dog', 'cat', 'dog', 'dog', 'cat', 'dog']
age = [1, 4, 1, 4, 1, 3, 7]
size = ['small', 'big', 'small', 'big', 'big', 'small', 'big']
constant = [0, 0, 0, 0, 0, 0, 0]

test_df = pd.DataFrame({'species': species,
                        'age': age,
                        'size': size,
                        'constant': constant})

def fast_check(df, col1, col2):
    if df[col2].nunique() == 1:
        # constant valued column
        return 1
    elif df[col2].nunique() / df[col2].count() < 0.05:
        # continuous-valued column (heuristic)
        return 1000
    else:
        # takes long to compute
        return df.groupby(col1)[col2].nunique().max()

def isOneToOne(df, col1, col2):
    first = fast_check(df, col1, col2)
    second = fast_check(df, col2, col1)

    if first == 1 and second == 1:
        return 'one-to-one'
    elif first == 1 and second > 1:
        return 'many-to-one'
    elif first > 1 and second == 1:
        return 'one-to-many'
    else:
        return 'many-to-many'

def determine_column_relationships(df, limit_to_columns=None, involving_columns=None):
    col_names = limit_to_columns if limit_to_columns is not None else df.columns

    col_name_combinations = list(combinations(col_names, 2))

    if involving_columns is not None:
        col_name_combinations = [(x, y) for x, y in col_name_combinations
                                 if x in involving_columns or y in involving_columns]

    df_results = pd.DataFrame(data=col_name_combinations,
                              columns=['column_a', 'column_b'])
    df_results['many-to-many'] = 0
    df_results['one-to-many'] = 0
    df_results['many-to-one'] = 0
    df_results['one-to-one'] = 0

    # TODO speed up if a constant column
    # TODO speed up if column clearly continuous

    for i, (x, y) in enumerate(tqdm(col_name_combinations, total=df_results.shape[0])):
        match_type = isOneToOne(df, x, y)
        df_results[match_type].iloc[i] = 1

    return df_results

determine_column_relationships(test_df)

def to_sig_figures(x, n_sig):
    return np.format_float_positional(x,
                                      precision=n_sig,
                                      unique=False,
                                      fractional=False,
                                      trim='k')
