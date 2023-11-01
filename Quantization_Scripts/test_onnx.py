import onnx

onnx_model = onnx.load("./tiny_roberta_2.onnx")
onnx.checker.check_model(onnx_model)