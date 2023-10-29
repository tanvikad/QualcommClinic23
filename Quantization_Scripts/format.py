import os

for i in range(1,6):
    file_name = f"\inputs\pre-tokenized\q{i}.txt"
    with open(file_name, 'r') as file:
        content = file.read()
    size = os.path.getsize(file_name)
    if 1540 % size != 0:
        numPadding = size - (1540%size)
        content = content + " " * numPadding
    with open(file_name, 'w') as file:
        file.write(content)

for i in range(1,6):
    file_name = f"\inputs\pre-tokenized\a{i}.txt"
    with open(file_name, 'r') as file:
        content = file.read()
    size = os.path.getsize(file_name)
    if size != 1540:
        numPadding = 1540-size
        content = content + " " * numPadding
    with open(file_name, 'w') as file:
        file.write(content)