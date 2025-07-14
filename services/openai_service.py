import openai
from openai import OpenAI
import getpass
import os
from config import settings
from langchain_community.vectorstores import FAISS
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def generate_embedding(text: str) -> list:
    # dummy embedding, replace with real API call
    return [0.1] * 1536

def demo_chat():
    client = OpenAI(
        api_key = ""
    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": "write a haiku about ai"}
        ]
    )

    print(completion.choices[0].message);

def perform_similarity_search(self, vector_store: FAISS, query : str):
    result = vector_store.similarity_search(query, 2)
    for doc in result:
        print(doc.page_content)

def generate_query_or_response(input):
    model_id = "tiiuae/falcon-7b-instruct"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, device_map="auto")

    inputs = tokenizer("Some pointers on why AI is needed in financial world", return_tensors="pt").to("cuda")

    outputs = model.generate(**inputs, max_new_tokens=100)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(response)
    return {"messages": [response]}

