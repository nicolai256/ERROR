with tf.compat.v1.Session() as sess:

  a = tf.constant(5.0)
  b = tf.constant(6.0)
  c = tf.multiply(a, b)

  result = sess.run(c)
  print(result)

/job:localhost/replica:0/task:0/device:XLA_CPU:0
/job:localhost/replica:0/task:0/device:GPU:1

neural_style.py --content_img face.jpg  --style_imgs starry-night.jpg --max_iterations 500 --img_name skrt