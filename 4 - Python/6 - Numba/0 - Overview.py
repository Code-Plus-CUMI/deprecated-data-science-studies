"""
	***********
	** Numba **
	***********

	Numba is a Python package designed to speed up the execution
time of functions converting the code into Machine Code and getting
faster results like C and FORTRAN Languages.

	But hold your horses, it's not all situations where you use
Numba and your code is executed way too faster than before, there
are some criterion that must be followed to use and get impressive
results from this library, such as:

	- the code is "numerically orientated" (does a lot of math) and;
	- uses NumPy package in most part;
	- and/or has lot of loops.

-*-*-*-*-

	Curiosities: 

	- The Machine Code generated is "Just-In-Time" (JIT)
and the package works better with NumPy arrays, loops and functions.

	- Numba supports Intel and AMD x86, POWER8/9, and ARM CPUs
(including Apple M1), NVIDIA GPUs, Python 3.7-3.10, as well as
Windows/macOS/Linux. Precompiled Numba binaries for most systems
are available as conda packages and pip-installable wheels.

-*-*-*-*-

	The "@jit" decorator have three boolean parameters:

	- nopython: tells if Numba should use the Python interpreter
if an error occurs to compile the code to Machine Code or to
execute it;

	- parallel: tells whether the code will be processed on CPU only
or will be distributed to CPU and GPU in async mode;

	- fastmath: tells if the code will have a boost in math
operations (just recommended when the function has a lot of math).

	
	About "@njit" decorator, it has the same parameters than "@jit"
but "nopython", because this parameter is already set as True
forever. Then:

					@jit(nopython=True) == @njit

"""


# ---- INSTALLING PACKAGE ----
#
# pip install numba
# conda install numba



# ---- SIMPLE EXAMPLE THAT NUMBA WORKS ----
#
# 	About "@jit(nopython=True)" mode is for best performance,
# being equivalent to "@njit".
#	So, "@jit(nopython=True)" == "@njit".
#
from numba import jit
import numpy as np

x = np.arange(100).reshape(10, 10)

@jit(nopython=True, parallel=Tue, fast_math=True)
def go_fast(a):
	trace = 0.0
	for i in range(a.shape[0]):    # Numba likes loops
		trace += np.tanh(a[i, i])  # Numba likes NumPy functions
	return a + trace               # Numba likes Numpy broadcasting

print(go_fast(x))



# ---- SIMPLE EXAMPLE THAT NUMBA DOES NOT WORK ----
#
# 	Numba understands just Numpy and not Pandas and as a result 
# it would simply run this code via the interpreter but with
# the added cost of the Numba internal overheads!
#
from numba import jit
import pandas as pd

x = { 'a': [1, 2, 3], 'b': [20, 30, 40] }

@jit(nopython=True, parallel=Tue, fast_math=True)
def use_pandas(a): # functions will not benefit from Numba jit
	df = pd.DataFrame.from_dict(a) # Numba does not know about pd.DataFrame
	df += 1 # so Numba does not understand what this is
	return df.cov() # and this too!

print(use_pandas(x))