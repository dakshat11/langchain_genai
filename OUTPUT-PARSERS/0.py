from huggingface_hub import InferenceClient
import os



client = InferenceClient(model="google/gemma-2-2b-it")
response = client.text_generation("Hello world!")
print(response)
