#!/usr/bin/env python
import argparse
import sys

def init():
    parser = argparse.ArgumentParser(description=
            "get items in file2 which is not shown in file1")
    parser.add_argument("file1")
    parser.add_argument("file2")
    parser.add_argument("--seq2", default=",")
    args = parser.parse_args()
    return args

def unique(file1, file2, seq2):
    f = open(file1)
    s = set()
    for l in f.readlines():
        s.add(l.strip())
    f.close()
    f = open(file2)
    for l in f.readlines():
        key = l.strip().split(seq2)[0]
        if key not in s:
            print l,
        else:
            print >> sys.stderr, key
    f.close()

if __name__ == '__main__':
    args = init()
    unique(args.file1, args.file2, args.seq2)
