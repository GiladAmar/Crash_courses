import os
import subprocess
import sys
import random

def safe_shuffle(xs):

    new_xs = list(xs)
    random.shuffle(new_xs)
    return new_xs


def safe_reverse(xs):
    return list(reversed(xs))


def launch(filename):
    """Pass filename to the OS, which should select the correct
    program to open it.
    """
    if sys.platform == "win32":
        os.startfile(filename)
    elif sys.platform == "darwin":
        subprocess.Popen(["open", filename])
    else:
        try:
            subprocess.Popen(["xdg-open", filename])
        except OSError:
            print("File open failed: " + filename)


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
    # raw_path = path
    if len(path) > 255:
        path = os.path.abspath(_filename(path))
        npath = os.path.dirname(path)
        res = [path]
        while path != npath:
            path, npath = npath, os.path.dirname(npath)
            res.append(path)
        msg = {True: "passed", False: "failed"}
        return "\n".join(["%s: %s" % (msg[os.path.exists(i)], i[4:]) for i in res])
    else:
        path = os.path.abspath(path)
        npath = os.path.dirname(path)
        res = [path]
        while path != npath:
            path, npath = npath, os.path.dirname(npath)
            res.append(path)
        msg = {True: "passed", False: "failed"}
        return "\n".join(["%s: %s" % (msg[os.path.exists(i)], i) for i in res])


def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


import sys

_cnt = 0


def print_status(msg):
    global _cnt
    CURSOR_UP_ONE = "\x1b[1A"
    ERASE_LINE = "\x1b[2K"
    print(ERASE_LINE + CURSOR_UP_ONE)
    msg = "\r[{0:>2}] - {1}".format(_cnt, msg)
    sys.stdout.write(msg)
    sys.stdout.flush()
    _cnt += 1


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


def run_terminal_cmd(command_str, args=None, capture_output=False):
    import subprocess

    shell = True if args else False
    # allows arguments in the command string and not require them to be input separately

    return subprocess.run(check=True, shell=shell, capture_output=capture_output)
    # raises the CalledProcessError if fails


# An @enforce decorator that checks if types are correct in runtime
def enforce(func):
    """ Decorator to enforce type decorators at runtime via
    type assertion. Usage:
    @enforce
    def foo(a : str, b : int, c = True : bool) -> str:
      return None
    """

    def enforce_wrapper(*args, **kwargs):
        for k, v in dict(
            zip(func.__code__.co_varnames, args),
            **dict(
                zip(
                    func.__code__.co_varnames[len(args) : func.__code__.co_argcount],
                    func.__defaults__,
                )
                if func.__defaults__
                else {},
                **kwargs
            )
        ).items():
            assert type(v) == func.__annotations__.get(k, type(v)), (
                "Argument `%s : %s` received type `%s`."
                % (k, func.__annotations__.get(k), type(v))
            )
        ret = func(*args, **kwargs)
        assert type(ret) == func.__annotations__.get("return", type(ret)), (
            "`%s(...) -> %s` returned type `%s`."
            % (func.__name__, func.__annotations__.get("return"), type(ret))
        )
        return ret

    return enforce_wrapper


# Python program to find SHA256 hash string of a file
import hashlib


def sha256file(fname):
    sha256_hash = hashlib.sha256()
    with open(fname, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()


# function caching:
import functools


@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def strip_extra_whitespace(string: str) -> str:
    r"""
    Replace consecutive whitespace characters with a single space.
    Whitespace characters include spaces, tabs, and newlines.
    Examples
    --------
    >>> strip_extra_whitespace("   This\tis    a\nsentence \n")
    'This is a sentence'
    """
    return re.sub(r"\s+", " ", string.strip())


# Set resource limits
import signal
import resource
import os


def set_max_runtime(seconds):
    # Install the signal handler and set a resource limit
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)


# To limit memory usage
def set_max_memory(size):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (size, hard))


# TODO
from pandas.testing import assert_frame_equal
