import sys
import os
import subprocess


def safe_shuffle(xs):
    import random
    new_xs = list(xs)
    random.shuffle(new_xs)
    return new_xs


def safe_reverse(xs):
    return list(reversed(xs))


def launch(filename):
    """Pass filename to the OS, which should select the correct
    program to open it.
    """
    if sys.platform == 'win32':
        os.startfile(filename)
    elif sys.platform == 'darwin':
        subprocess.Popen(['open', filename])
    else:
        try:
            subprocess.Popen(['xdg-open', filename])
        except OSError:
            print('File open failed: ' + filename)


def swap_dict(dict_in):
    swapped = dict_in((v, k) for k, v in dict_in.items())
    return swapped


def print_bad_path(path):
    # type: (str) -> str
    """
    Prints information about the existence (access possibility) of the parts
    of the given path. Useful for debugging when the path to a given file is wrong.

    Parameters
    ----------
    path : str
        path to check

    Returns
    -------
    msg : str
        string with informations whether access to parts of the path
        is possible
    """
    #raw_path = path
    if len(path) > 255:
        path = os.path.abspath(_filename(path))
        npath = os.path.dirname(path)
        res = [path]
        while path != npath:
            path, npath = npath, os.path.dirname(npath)
            res.append(path)
        msg = {True: 'passed', False: 'failed'}
        return '\n'.join(['%s: %s' % (msg[os.path.exists(i)], i[4:]) for i in res])
    else:
        path = os.path.abspath(path)
        npath = os.path.dirname(path)
        res = [path]
        while path != npath:
            path, npath = npath, os.path.dirname(npath)
            res.append(path)
        msg = {True: 'passed', False: 'failed'}
        return '\n'.join(['%s: %s' % (msg[os.path.exists(i)], i) for i in res])


def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


#
#
# Type Hinting:
#     # Python 3.6
#     odd: List[int] = []
#
#     def add(a: int, b: int) -> int:
#         return a + b
#
#
#     run with mypy for warnings when icorrent use



modulo_three = lambda x: x%3
# Using lambda
new_l = map(lambda x: x%3, l)

# Using filter will give the same result
even = filter(lambda x: x%2 == 0, l) 



import sys

_cnt = 0


def print_status(msg):
    global _cnt
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    print(ERASE_LINE + CURSOR_UP_ONE)
    msg = "\r[{0:>2}] - {1}".format(_cnt, msg)
    sys.stdout.write(msg)
    sys.stdout.flush()
    _cnt += 1


def reduce_mem_usage(df):
    start_mem_usg = df.memory_usage().sum() / 1024**2
    print("Memory usage of properties dataframe is :",start_mem_usg," MB")
    NAlist = [] # Keeps track of columns that have missing values filled in.
    for col in df.columns:
        if df[col].dtype != object:  # Exclude strings

            # Print current column type
            print("******************************")
            print("Column: ",col)
            print("dtype before: ",df[col].dtype)

            # make variables for Int, max and min
            IsInt = False
            mx = df[col].max()
            mn = df[col].min()

            # Integer does not support NA, therefore, NA needs to be filled
            if not np.isfinite(df[col]).all():
                NAlist.append(col)
                df[col].fillna(mn-1,inplace=True)

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
            print("dtype after: ",df[col].dtype)
            print("******************************")

    # Print final result
    print("___MEMORY USAGE AFTER COMPLETION:___")
    mem_usg = df.memory_usage().sum() / 1024**2
    print("Memory usage is: ",mem_usg," MB")
    print("This is ",100*mem_usg/start_mem_usg,"% of the initial size")
    return df, NAlist

df_reduced, na_list = reduce_mem_usage(df)


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
        # continious-valued column (heuristic)
        return 1000
    else:
        # takes long to compute
        return df.groupby(col1)[col2].nunique().max()


def isOneToOne(df, col1, col2):
    first = fast_check(df, col1, col2)  # df.groupby(col1)[col2].nunique().max()
    second = fast_check(df, col2, col1)  # df.groupby(col2)[col1].nunique().max()

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
    # TODO speed up if column clearly continious

    for i, (x, y) in enumerate(tqdm(col_name_combinations, total=df_results.shape[0])):
        match_type = isOneToOne(df, x, y)
        df_results[match_type].iloc[i] = 1

    return df_results


determine_column_relationships(test_df)

