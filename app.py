#!/usr/bin/env python3
from flask import Flask, render_template, jsonify, request
import openai
import aiapi
import os
import dotenv

config = dotenv.dotenv_values(".env")
openai.api_key = config['OPENAI_API_KEY']

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.register_error_handler(404, page_not_found)


@app.route('/', methods = ['POST', 'GET'])
def index():

    if request.method == 'POST':
        prompt = request.form['prompt']

        res = {}
        res['answer'] = aiapi.generateChatResponse(prompt)
        return jsonify(res), 200

    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
