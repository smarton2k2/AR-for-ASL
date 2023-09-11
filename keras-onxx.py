import tf2onnx
import tensorflow as tf

model = tf.keras.models.load_model('asl_model_new.h5')

onnx_model, _ = tf2onnx.convert.from_keras(model)

with open("asl_model_new.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())
