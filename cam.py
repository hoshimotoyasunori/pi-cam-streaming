import cv2
from base_cam import BaseCamera


class Camera(BaseCamera):
    def __init__(self):
        super().__init__()

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            _, img = camera.read()

            yield cv2.imencode('.jpg', img)[1].tobytes()
