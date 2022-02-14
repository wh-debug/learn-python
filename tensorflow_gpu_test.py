import tensorflow as tf
gpu_device_name = tf.test.is_gpu_available()
gpu_ = tf.test.is_built_with_cuda()
_gpu = tf.config.list_physical_devices('GPU')

print(gpu_device_name)