import os
from transformers import AutoTokenizer

# generate tokens for roBERTa
model_name = "deepset/tinyroberta-squad2"

tokenizer = AutoTokenizer.from_pretrained(model_name)

pre_tokenized_root = "./inputs/pre-tokenized"

def tokenize(filename):
    post_tokenized_root = "./inputs/post-tokenized"
    with open(f"{pre_tokenized_root}/{filename}") as f:
        lines = f.readlines()
        with open(f"{post_tokenized_root}/{filename}", "w") as id_file, open(f"./attention_masks/{filename}", "w") as mask_file:
            for line in lines:
                # tokenize the line
                inputs = tokenizer(line, return_tensors="pt", padding=True, truncation=True)

                # get the inputs_ids and attention_mask
                input_ids = inputs["input_ids"][0]
                attention_mask = inputs["attention_mask"][0]

                # convert tensor to list
                input_ids_list = input_ids.tolist()
                attention_mask_list = attention_mask.tolist()

                # write to the respective files
                id_file.write(" ".join(map(str, input_ids_list)) + "\n")
                mask_file.write(" ".join(map(str, attention_mask_list)) + "\n")

# get pre-tokenized root path
pre_tokenized_root = "./inputs/pre-tokenized"
for filename in os.listdir(pre_tokenized_root):
    tokenize(filename)

