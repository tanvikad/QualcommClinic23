import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer

print("here")
print(torch.__version__)

model_name = "google/flan-t5-small"

model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model.eval()

onnx_path = "./flan_small.onnx"

sample_text = ["a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a", ]

tokens = tokenizer(sample_text, return_tensors="pt", padding=True, truncation=True)

input_ids = tokens["input_ids"]
attention_mask = tokens["attention_mask"]

torch.onnx.export(model,
                  (input_ids, attention_mask),
                  "flan-small.onnx",
                  opset_version=11,
                  verbose=True
                  )

