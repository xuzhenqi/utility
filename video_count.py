#!/usr/bin/env python
import matplotlib as mpl
mpl.use('Agg')
from video import info_video
from matplotlib import pyplot as plt
import numpy as np
import argparse
import sys

def init():
    parser = argparse.ArgumentParser(description=
            "count video sizes and frames")
    parser.add_argument("filelist")
    parser.add_argument("output")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    a = init()
    f = open(a.filelist)
    plt.figure()
    plt.hold(True) 
    framess = []
    fpss = []
    count = 0
    for l in f.readlines():
        count += 1
        if count % 100 == 0:
            print "processing", count, "videos"
        filename = l.strip()
        fps, size, frames = info_video(filename)
        framess.append(frames)
        fpss.append(fps)
        plt.Rectangle((0, 0), size[0], size[1], linewidth=0.1)
    plt.savefig(a.output)
    print "fps mean:", np.mean(fpss)
    print "fps min:", np.min(fpss)
    print "fps max:", np.max(fpss)
    print "frames mean", np.mean(framess)
    print "frames min", np.min(framess)
    print "frames max", np.max(framess)
