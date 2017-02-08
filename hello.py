import os
from video import info_video
import subprocess as sp
from gevent.wsgi import WSGIServer
from flask import Flask, request, render_template
app = Flask(__name__)

cwd = os.getcwd()
video_dir = cwd + '/static/data/videos'

label_serial = {}
with open(cwd + '/static/data/label_info.txt') as f:
    for l in f.readlines():
        l = l.strip().split()
        assert l[0] not in label_serial
        label_serial[l[0]] = l[1]

label_desc = {}
with open(cwd + '/static/data/label.txt') as f:
    f.readline()
    for l in f.readlines():
        l = l.strip().split(',')
        assert l[0] not in label_desc
        label_desc[l[0]] = l[3]


@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html")


@app.route('/templates/files.html')
def index2():
    video_files = [f for f in os.listdir(video_dir)]
    video_files_number = len(video_files)
    return render_template("files.html",
            video_files_number=video_files_number,
            video_files=video_files)

@app.route('/<filename>')
def movie(filename):
    fps, size, frames = info_video("static/data/videos/" + filename)
    label = filename.split('_')[1].split('.')[0]
    serial_label = label_serial[label]
    desc = label_desc[label]
    return render_template('play.html', title=filename,
            fps=str(fps), size=str(size), frames=str(frames),
            video_file=filename, serial_label=serial_label)

if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
