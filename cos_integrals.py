
from scipy import integrate
import numpy as np
import argparse


def f4(w, x, y, z):
    inner = np.cos(w) + np.cos(x) + np.cos(y) + np.cos(z)
    total = (inner / 4)
    return f4


def boundsz():
    return [-np.pi, np.pi]


def boundsy(z):
    return [-np.pi, np.pi]


def boundsx(y, z):
    return [-np.pi, np.pi]


def boundsw(x, y, z):
    return [-np.pi, np.pi]


def f4(w, x, y, z, n):
    temp = (np.cos(w)+np.cos(x) + np.cos(y) + np.cos(z)) / 4
    numer = np.power(temp, n)
    denom = np.power((2*np.pi), 4)
    return numer / denom


def f3(x, y, z, n):
    temp = (np.cos(x) + np.cos(y) + np.cos(z)) / 3
    numer = np.power(temp, n)
    denom = np.power((2*np.pi), 3)
    return numer / denom


def f2(y, z, n):
    temp = (np.cos(y) + np.cos(z)) / 2
    numer = np.power(temp, n)
    denom = np.power((2*np.pi), 2)
    return numer/denom


def f1(z, n):
    temp = (np.cos(z)) / 1
    numer = np.power(temp, n)
    denom = np.power((2*np.pi), 1)
    return numer/denom


def bounds_z(n):

    return [-np.pi, np.pi]


def bounds_y(z, n):

    return [-np.pi, np.pi]


def bounds_x(y, z, n):

    return [-np.pi, np.pi]


def bounds_w(x, y, z, n):

    return [-np.pi, np.pi]


def sum_4(N=20):
    sum = 0
    for n in range(N):
        if (n % 2 == 1):
            continue
        result = integrate.nquad(
            f4, [bounds_w, bounds_x, bounds_y, bounds_z], args=(n,))
        print(result)
        sum += result[0]
    print(sum)


def sum_3(N=20):
    sum = 0
    for n in range(N):
        if (n % 2 == 1):
            continue
        result = integrate.nquad(f3, [bounds_x, bounds_y, bounds_z], args=(n,))
        print(result)
        print(sum)
        sum += result[0]
    print(sum)


def sum_2(N=20):
    sum = 0
    for n in range(N):
        result = integrate.nquad(f2, [bounds_y, bounds_z], args=(n,))
        print(result)
        sum += result[0]
    print(sum)


def sum_1(N=20):
    sum = 0
    for n in range(N):
        result = integrate.nquad(f1, [bounds_z], args=(n,))
        print(result)
        sum += result[0]
    print(sum)


parser = argparse.ArgumentParser()
parser.add_argument('-N', '--limit', type=int, default=20)
parser.add_argument('-d', '--dim', type=int)
args = parser.parse_args()
if (args.dim == 1):
    sum_1(args.limit)

if (args.dim == 2):
    sum_2(args.limit)
if (args.dim == 3):
    sum_3(args.limit)

if (args.dim == 4):
    sum_4(args.limit)
