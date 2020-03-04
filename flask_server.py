# app.py
# ref: https://qiita.com/Gyutan/items/1f81afacc7cac0b07526

import cv2
import os
from flask import Flask, render_template, Response

from camera import VideoCamera

app = Flask(__name__)


@app.route("/")
def index():
	return "Hello World!"

@app.route("/stream")
def stream():
	"""Video streaming home page."""
	return render_template("stream.html")

def gen(camera):
	"""Video streaming generator function."""
	while True:
		frame = camera.get_frame()

		# print("after get_frame")
		if frame is not None:
			yield (b"--frame\r\n"
				b"Content-Type: image/jpeg\r\n\r\n" + frame.tobytes() + b"\r\n")
		else:
			print("frame is none")

@app.route("/video_feed")
def video_feed():
	"""Video streaming route. Put this in the src attribute of an img tag."""
	return Response(gen(VideoCamera()),
			mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0", port=5010)
