#!/usr/bin/env python
import argparse
import numpy as np
import sys
from math import fabs

def init():
    parser = argparse.ArgumentParser(description=
            "diff two files")
    parser.add_argument("file1")
    parser.add_argument("file2")
    parser.add_argument("--eps", type=float, default=1e-5)
    args = parser.parse_args()
    return args

def diff(file1, file2, eps):
    d1 = np.loadtxt(file1)
    d2 = np.loadtxt(file2)
    for i in xrange(len(d1)):
        if fabs(d1[i] - d2[i]) > eps:
            print i, d1[i], d2[i]
    
if __name__ == '__main__':
    a = init()
    diff(a.file1, a.file2, a.eps)
