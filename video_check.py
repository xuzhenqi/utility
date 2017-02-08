#!/usr/bin/env python
import subprocess
import sys 
import argparse
#TODO: check file existence?

def init():
    parser = argparse.ArgumentParser(description=
            "check video integrity.") 
    parser.add_argument("filelist")
    args = parser.parse_args()
    return args

def check(filename):
    child = subprocess.Popen(["ffmpeg", "-v", "error", "-i", filename, "-f",
        "null", "-"], stderr=subprocess.PIPE)
    _, value = child.communicate()
    return value

if __name__ == '__main__':
    a = init()
    f = open(a.filelist)
    count = 0
    for l in f.readlines():
        count += 1
        if count % 100 == 0:
            print >> sys.stderr, "processing", count
        filename = l.strip()
        value = check(filename)
        if value:
            print filename
            print >> sys.stderr, filename, "is corrupted."
            print >> sys.stderr, value
