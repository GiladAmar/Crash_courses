from numba import jit


@jit  # Automatic Optimization
def f(x, y):
    # A somewhat trivial example
    return x + y


# -------------------------------------------------------------------------------
from numba import int32, jit, njit
# use njit as that will break if there is an issue compiling the function - and not give
# you the illusion that it is compiling


@jit(int32(int32, int32))  # Define expected input and output types
# @jit(int32(int32, int32))
def f(x, y):
    # A somewhat trivial example
    return x + y


# -------------------------------------------------------------------------------
@jit(nopython=True)
# rather throw error than use object mode - i.e. If it fails to compile

# -------------------------------------------------------------------------------
@jit(nogil=True)  # Release the GIL - be careful of usual multi-threading issues

# -------------------------------------------------------------------------------
@jit(cache=True)  # save compiled func to avoid re-compiling every run

# -------------------------------------------------------------------------------
@jit(nopython=True, parallel=True)  # both options in conjunction
# for functions with parallel semantics
def add_to_each(items):
    for i, item in enumerate(items):
        items[i] = item + 1


# -------------------------------------------------------------------------------
# For a class:

import numpy as np
from numba import jitclass  # import the decorator
from numba import float32, int32  # import the types

spec = [
    ("value", int32),  # a simple scalar field
    ("array", float32[:]),
]  # an array field


@jitclass(spec)
class Bag(object):
    def __init__(self, value):
        self.value = value
        self.array = np.zeros(value, dtype=np.float32)

    @property
    def size(self):
        return self.array.size

    def increment(self, val):
        for i in range(self.size):
            self.array[i] = val
        return self.array


# -------------------------------------------------------------------------------
from numba import float64, vectorize


@vectorize([float64(float64, float64)])  # vectorize to form numpy-like function
def f(x, y):
    return x + y


@vectorize(["float32(float32, float32)"], target="cuda")
# Vectorize to form numpy-like function on GPU
def f(x, y):
    return x + y


# -------------------------------------------------------------------------------
from numba import njit, prange

# Use prange instead of range to specify that the loop can be operated in parallel


@njit(parallel=True)
def prange_test(A):
    s = 0
    for i in prange(A.shape[0]):
        s += A[i]
    return s

    # -------------------------------------------------------------------------------
    # Environment Variables
    # export <varname> = <x>
    NUMBA_WARNINGS = 1  # Show warnings
    NUMBA_ENABLE_AVX = 1  # Enable AVX optimization (not all processors can handle this)
    NUMBA_DISABLE_JIT = 1  # Prevent all numba optimizations
