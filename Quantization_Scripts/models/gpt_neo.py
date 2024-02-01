from transformers import GPTNeoForCausalLM, GPT2Tokenizer
# from datasets import load_dataset
import torch
import torch.nn.functional as F

print(torch.__version__)

from aimet_torch.model_preparer import prepare_model



# dataset = load_dataset("EleutherAI/pile")

model_name = "EleutherAI/gpt-neo-1.3B"

model = GPTNeoForCausalLM.from_pretrained(model_name)
# model = prepare_model(model)

# tokenizer = GPT2Tokenizer.from_pretrained(model_name)

print(model)