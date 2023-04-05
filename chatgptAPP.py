
import json
import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

mt = 600

ms = [
    {'role': 'user', 'content': 'you are A cute assistant that is helpful and submissive'},
]

rs = openai.Completion.create(
    engine='davinci',
    prompt='\n'.join([f"{m['role']}: {m['content']}" for m in ms]),
    max_tokens=mt,
    n=1,
    temperature=0.5
)

conversation = [m['content'] for m in ms] + [rs.choices[0].text.strip()]

with open('conversation.json', 'w') as f:
    json.dump(conversation, f)





