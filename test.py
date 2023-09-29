import requests
import json

prompt = input("enter some code to explain:")

url = "http://localhost:11434/api/generate"
data = {
    "model": "llama2-uncensored:7b",
    "prompt": prompt
}

response = requests.post(url, data=json.dumps(data), stream=True)

for line in response.iter_lines():
    if line:
        response_json = json.loads(line)
        response_value = response_json.get('response')
        if response_value is not None:
            print(response_value, end='', flush=True)
    else:
        break
