from dotenv import load_dotenv
import openai
import os
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

MODEL = "text-davinci-003"
TEMPERATURE = 0.9
MAX_TOKENS = 1024

def openai_answer(message):
    completion = openai.Completion().create(model=MODEL, prompt=message, temperature=TEMPERATURE, max_tokens=MAX_TOKENS)
    response = completion.choices[0].text
    return response

def generate_image(message):
    response = openai.Image.create(prompt=message, n=1, size="1024x1024")
    return response['data'][0]['url']


