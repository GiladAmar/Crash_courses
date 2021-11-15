from socket import socket, gethostbyname, AF_INET, SOCK_STREAM
import cv2
from PIL import Image
import io
import time
import numpy as np

from tqdm import tqdm

PORT_NUMBER = 5000
SIZE = 150000

hostName = gethostbyname('0.0.0.0')

mySocket = socket(AF_INET, SOCK_STREAM)
mySocket.bind((hostName, PORT_NUMBER))
mySocket.listen(1)
conn, addr = mySocket.accept()

print("Test server listening on port {0}\n".format(PORT_NUMBER))

image = np.zeros((800, 600))

for i in tqdm(range(200000)):
    data = conn.recv(SIZE)
    last_time = time.time()

    tmp_img = np.frombuffer(data, dtype='uint8')
    if sum(tmp_img) > 0:
        image = tmp_img
    cv2.imshow('window', tmp_img)

    key_press = cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # print(image.sum())
sys.exit()
