import cv2
import sys

def info_video(filename):
    vid = cv2.VideoCapture(filename)
    assert vid.isOpened(), "Open failed: %s" % filename
    fps = vid.get(cv2.cv.CV_CAP_PROP_FPS)
    size = (int(vid.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
            int(vid.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
    frames = int(vid.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
    return fps, size, frames
