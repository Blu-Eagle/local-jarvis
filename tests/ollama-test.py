""" import ollama
response = ollama.chat(model='mistral', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content']) """

from ollama import Client
client = Client(host='http://localhost:11434')
response = client.chat(model='mistral', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])