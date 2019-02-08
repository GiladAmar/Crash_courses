import tensorflow as tf

#Identify id the GPU is accessible
with tf.Session() as sess:
  devices = sess.list_devices()

