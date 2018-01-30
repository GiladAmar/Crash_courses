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