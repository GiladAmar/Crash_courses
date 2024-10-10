import os
import subprocess
import sys
import numpy as np

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


# function caching:
import functools


@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

import resource
# Set resource limits
import signal


def set_max_runtime(seconds):
    # Install the signal handler and set a resource limit
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)


# To limit memory usage
def set_max_memory(size):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (size, hard))


class NDArrayEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def jsonify(input):
    return json.dumps(input, cls=NDArrayEncoder, indent=4)


# To instead make sure it is being compressed with jpeg first:
def img_to_base64_str(self, img):
    buffered = BytesIO()
    img.save(buffered, format="jpeg")
    buffered.seek(0)
    img_byte = buffered.getvalue()
    return base64.b64encode(img_byte).decode()


# Scheduling
import schedule

def do_something():
    print(datetime.now(), "Doing the thing...")

schedule.every(5).minutes.do(do_something)

while True:
    schedule.run_pending()
    time.sleep(1)