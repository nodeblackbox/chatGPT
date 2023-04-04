

import json
import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

mt = 600

ms = [
    {'role': 'system', 'content': 'you are A cute assistant that is helpful and submissive'},
    {'role': 'user', 'content': 'Hello, how are you?'},
    {'role': 'assistant', 'content': 'I am doing well, how about you?'},
    {'role': 'user', 'content': 'I am also doing well.'},
    {'role': 'assistant', 'content': 'im fine thank you'},
    {'role': 'user', 'content': 'thats breddy cool'},
    {'role': 'assistant', 'content': 'I am also doing well.'},
    {'role': 'user', 'content': 'Can you explain to me what quantum physics is'}
]

rs = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=ms,
    max_tokens=mt,
    n=1,
    temperature=0.5
)

conversation = [m['content'] for m in ms] + [rs.choices[0].text.strip()]

with open('conversation.json', 'w') as f:
    json.dump(conversation, f)









