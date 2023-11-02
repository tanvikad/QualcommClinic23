import os

def get_size(filename):
    size = os.path.getsize(filename)
    print("SIZE:", size)

print("ANSWER: ", end="")
get_size("./answers/posttokenized/answer1.txt")

print("QUESTION: ", end="")
get_size("./questions/posttokenized/question1.txt")