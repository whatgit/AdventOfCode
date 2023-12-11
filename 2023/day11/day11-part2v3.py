import numpy as np
from scipy import interpolate


x = np.array([2, 10, 100])
y = np.array([9799681, 13904985, 60089655])
f = interpolate.interp1d(x, y, fill_value='extrapolate')
print("EXTRAPOLATE !!!")
print(f(1000000))