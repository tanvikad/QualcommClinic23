import os

question_posttokenized_root = "./questions/posttokenized"
answer_posttokenized_root = "./answers/posttokenized"

space_tokens = " 0 1437 2"
TENSOR_EXTENT = 56

for filename in os.listdir(question_posttokenized_root):
    path = f"{question_posttokenized_root}/{filename}"
    with open(path, 'r') as f:
        content = f.read()
    size = os.path.getsize(path)

    if TENSOR_EXTENT % size != 0:
        num_padding = TENSOR_EXTENT % size
        content = content + (" " * num_padding)
    with open(path, 'w') as file:
        file.write(content)

for filename in os.listdir(answer_posttokenized_root):
    path = f"{answer_posttokenized_root}/{filename}"
    with open(path, 'r') as f:
        content = f.read()
    size = os.path.getsize(path)
    if TENSOR_EXTENT % size != 0:
        num_padding = TENSOR_EXTENT % size
        content = content + (" " * num_padding)
    with open(path, 'w') as file:
        file.write(content)
