!pip install openai 

openai.api_key = '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'
     
Method 1 - using OpenAI Python Package

import openai

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]
