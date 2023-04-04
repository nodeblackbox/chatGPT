# import openai
# import requests
# from dotenv import load_dotenv
# load_dotenv()
# import os
# from transformers import GPT2TokenizerFast

# # not allowed to exede 4000 tokens

# # intro = "you are A cute assistant that is helpful and submissive"

# openai.api_key = os.getenv('OPENAI_API_KEY')
# # system 
# # Assistant 
# # User 

# mt = 3000

# args = ['Hello, how are you?', 'I am doing well, how about you?', 'I am also doing well.']


# ms = [ { 'role': 'system', 'content': 'you are A cute assistant that is helpful and submissive' } ]
# ms.append({ 'role': 'user', 'content': args })
# ms.append({ 'role': 'assistant', 'content': 'im fine thank you' })
# ms.append({ 'role': 'user', 'content': 'thats breddy cool' })
# ms.append({ 'role': 'assistant', 'content': 'I am also doing well.' })

# rs = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=ms, max_tokens=mt, n=1, temperature=0.5)

# print(rs)




import openai
import os
from dotenv import load_dotenv

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


print(rs.choices[0].message.content)















# {
#   "created": 1680640521,
#   "id": "chatcmpl-71hf7DMP4GphuhgrL62p7DvtWaIDB",
#   "model": "gpt-3.5-turbo-0301",
#   "object": "chat.completion",
#   "usage": {
#     "completion_tokens": 113,    "prompt_tokens": 98,{  "choices": [    {
#       "finish_reason": "stop",
#       "index": 0,
#       "message": {
#         "content": "Quantum physics is a branch of physics that deals with the behavior of matter and energy at the smallest scales of atoms and subatomic particles. It describes the properties of particles such as electrons and photons, which are not observable in classical physics. Quantum mechanics is a fundamental theory in physics that explains the behavior of these particles and how they interact with each other. It has many practical applications in fields such as electronics, computing, and materials science.",        
#         "role": "assistant"      }    }  ],
#   "created": 1680640547,
#   "id": "chatcmpl-71hfX7NvdxrgGzSKA5h9hg2JEOwxK",
#   "model": "gpt-3.5-turbo-0301",
#   "object": "chat.completion",
#   "usage": {
#     "completion_tokens": 88,
#     "prompt_tokens": 98,
#     "total_tokens": 186
#   }
# }



















# class ChatGPT:
#     def estimate_token_length(msg):
        
#         self.tokenizer = GPT2TokenizerFast.from_pretrained('gpt2')
#         r = self.tokenizer(msg)
#         return 5 + len(r.input_ids)




# Install the OpenAI library if you haven't already: pip install openai
# Replace "your_api_key_here" with your actual API key
# openai.api_key = ''

# def ask_chatgpt(prompt):
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=prompt,
#         temperature=0.5,
#         max_tokens=100,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0,
#     )

#     return response.choices[0].text.strip()

# def main():
#     print("Welcome to the ChatGPT API script!")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["exit", "quit"]:
#             print("Goodbye!")
#             break

#         prompt = f"User: {user_input}\nAssistant:"
#         response = ask_chatgpt(prompt)
#         print("Assistant:", response)

# if __name__ == "__main__":
#     main()