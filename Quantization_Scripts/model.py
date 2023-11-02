import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer

print(torch.__version__)

model_name = "deepset/tinyroberta-squad2"

model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model.eval()

# tokenize a sample input
text = "Convert this to BERT input format"
inputs = tokenizer(text, return_tensors="pt")

onnx_path = "./tiny_roberta.onnx"

sample_text = ["Sample text 1 Sample text 2 Sample text 3 Sample text 4"]

tokens = tokenizer(sample_text, return_tensors="pt", padding=True, truncation=True)

input_ids = tokens["input_ids"]
attention_mask = tokens["attention_mask"]

torch.onnx.export(model,
                  (input_ids, attention_mask),
                  "tiny_roberta_fixed_batch.onnx",
                  opset_version=11,
                  verbose=True
                  )

