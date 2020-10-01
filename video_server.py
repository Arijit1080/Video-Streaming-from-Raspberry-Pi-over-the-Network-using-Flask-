import io
import socket
import struct
from PIL import Image
import cv2
import numpy
import sys
from base_camera import BaseCamera

server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 4444))  
server_socket.listen(0)
print("Listening")

class Camera(BaseCamera):
    def frames():
       while True:
            connection = server_socket.accept()[0].makefile('rb')
            img = None
            while True:
              try:
                image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
                if not image_len:
                    break
                image_stream = io.BytesIO()
                image_stream.write(connection.read(image_len))
                image_stream.seek(0)
                image = Image.open(image_stream)
                im = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
                yield cv2.imencode('.jpg', im)[1].tobytes()
              
              except:
                break
            cv2.destroyAllWindows()
