import numpy as np
from transformers import AutoTokenizer

filename = "./output/Result_0/708.raw"

with open(filename, 'rb') as file:
    binary_data = file.read()

# data_types = [np.uint8, np.]

data = np.frombuffer(binary_data, dtype=np.int32)

print(data)

model_name = "deepset/tinyroberta-squad2"

tokenizer = AutoTokenizer.from_pretrained(model_name)

text = tokenizer.decode(data)

print(text)

print("here")
