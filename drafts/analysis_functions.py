def find_matches(df, col1, col2):
    # find relationships between category columns

    unique_matches_df = df[col1, col2].drop_duplicates()

    unique_matches_df.sort_values([col1.col2]).reset_index()
    return


# Explore column relationships
from itertools import combinations

species = ["cat", "dog", "cat", "dog", "dog", "cat", "dog"]
age = [1, 4, 1, 4, 1, 3, 7]
size = ["small", "big", "small", "big", "big", "small", "big"]
constant = [0, 0, 0, 0, 0, 0, 0]

test_df = pd.DataFrame(
    {"species": species, "age": age, "size": size, "constant": constant}
)


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
        return "one-to-one"
    elif first == 1 and second > 1:
        return "many-to-one"
    elif first > 1 and second == 1:
        return "one-to-many"
    else:
        return "many-to-many"


def determine_column_relationships(df, limit_to_columns=None, involving_columns=None):
    col_names = limit_to_columns if limit_to_columns is not None else df.columns

    col_name_combinations = list(combinations(col_names, 2))

    if involving_columns is not None:
        col_name_combinations = [
            (x, y)
            for x, y in col_name_combinations
            if x in involving_columns or y in involving_columns
        ]

    df_results = pd.DataFrame(
        data=col_name_combinations, columns=["column_a", "column_b"]
    )
    df_results["many-to-many"] = 0
    df_results["one-to-many"] = 0
    df_results["many-to-one"] = 0
    df_results["one-to-one"] = 0

    # TODO speed up if a constant column
    # TODO speed up if column clearly continuous

    for i, (x, y) in enumerate(tqdm(col_name_combinations, total=df_results.shape[0])):
        match_type = isOneToOne(df, x, y)
        df_results[match_type].iloc[i] = 1

    return df_results


determine_column_relationships(test_df)


def to_sig_figures(x, n_sig):
    return np.format_float_positional(
        x, precision=n_sig, unique=False, fractional=False, trim="k"
    )




def reduce_pandas_df_mem_usage(df):
    start_mem_usg = df.memory_usage().sum() / 1024 ** 2
    print("Memory usage of properties dataframe is :", start_mem_usg, " MB")
    NAlist = []  # Keeps track of columns that have missing values filled in.
    for col in df.columns:
        if df[col].dtype != object:  # Exclude strings

            # Print current column type
            print("******************************")
            print("Column: ", col)
            print("dtype before: ", df[col].dtype)

            # make variables for Int, max and min
            IsInt = False
            mx = df[col].max()
            mn = df[col].min()

            # Integer does not support NA, therefore, NA needs to be filled
            if not np.isfinite(df[col]).all():
                NAlist.append(col)
                df[col].fillna(mn - 1, inplace=True)

            # test if column can be converted to an integer
            asint = df[col].fillna(0).astype(np.int64)
            errors_from_convert_to_int = (df[col] - asint).sum()

            if -0.01 < errors_from_convert_to_int < 0.01:
                info = np.iinfo
                # Make Integer/unsigned Integer datatypes
                if mn >= 0:
                    types = (np.uint8, np.uint16, np.uint32, np.uint64)
                else:
                    types = (np.int8, np.int16, np.int32, np.int64)
            else:
                info = np.finfo
                types = (np.float16, np.float32, np.float64)

            for t in types:
                if info(t).min <= mn and mx <= info(t).max:
                    df[col] = df[col].astype(t)
                    break

            # Print new column type
            print("dtype after: ", df[col].dtype)
            print("******************************")

    # Print final result
    print("___MEMORY USAGE AFTER COMPLETION:___")
    mem_usg = df.memory_usage().sum() / 1024 ** 2
    print("Memory usage is: ", mem_usg, " MB")
    print("This is ", 100 * mem_usg / start_mem_usg, "% of the initial size")
    return df, NAlist


df_reduced, na_list = reduce_mem_usage(df)
