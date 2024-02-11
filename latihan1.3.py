Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> P = 200000000
>>> A = 400000000
>>> r = 0.1
>>> n = 1
>>> t = math.log(A / P) / math.log(1 + r / n)
>>> t
7.272540897341713
