import os
from transformers import AutoTokenizer

# generate tokens for roBERTa
model_name = "deepset/tinyroberta-squad2"

tokenizer = AutoTokenizer.from_pretrained(model_name)

pre_tokenized_root = "./inputs/pre-tokenized"
post_tokenized_root = "./inputs/post-tokenized"

question_pretokenized_root = "./questions/pretokenized"
question_posttokenized_root = "./questions/posttokenized"
answer_pretokenized_root = "./answers/pretokenized"
answer_posttokenized_root = "./answers/posttokenized"

print(tokenizer(" ", return_tensors="pt", padding=True, truncation=True))
print(tokenizer("What is the capital of France?", return_tensors="pt", padding=True, truncation=True))

def tokenize_and_attention_mask(filename):
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

def tokenize_only(filename1, filename2):
    with open(f"{question_pretokenized_root}/{filename1}") as f1, open(f"{answer_pretokenized_root}/{filename2}") as f2:
        q_lines = f1.readlines()
        a_lines = f2.readlines()
        with open(f"{question_posttokenized_root}/{filename1}", "w") as q_file, open(f"{answer_posttokenized_root}/{filename2}", "w") as a_file:
            for line in q_lines:
                # tokenize the line
                inputs = tokenizer(line, return_tensors="pt", padding=True, truncation=True)

                # get the inputs_ids and attention_mask
                input_ids = inputs["input_ids"][0]

                # convert tensor to list
                input_ids_list = input_ids.tolist()

                # write to the respective file
                q_file.write(" ".join(map(str, input_ids_list)) + "\n")

            for line in a_lines:
                # tokenize the line
                inputs = tokenizer(line, return_tensors="pt", padding=True, truncation=True)

                # get the inputs_ids and attention_mask
                input_ids = inputs["input_ids"][0]

                # convert tensor to list
                input_ids_list = input_ids.tolist()

                # write to the respective file
                a_file.write(" ".join(map(str, input_ids_list)) + "\n")


for filename1, filename2 in list(zip(os.listdir(question_pretokenized_root), os.listdir(answer_pretokenized_root))):
    tokenize_only(filename1, filename2)

