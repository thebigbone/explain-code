from flask import Flask, render_template, request
import openai
import requests
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    code = request.form.get("code")

    url = "http://localhost:11434/api/generate"
    data = {
        "model": "llama2-uncensored:7b",
        "prompt": code
    }

    response = requests.post(url, data=json.dumps(data), stream=True)

    response_values = ""

    for line in response.iter_lines():
        if line:
            line = line.rstrip()
            response_json = json.loads(line)
            response_value = response_json.get('response')
            if response_value is not None:
                response_values += response_value
            else:
                break

    return render_template("result.html", code=code, explanation=response_values)


if __name__ == "__main__":
    app.run(debug=True)
