
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def EnglishtoFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    ans = english_to_french(textToTranslate)
    return "Translated text to French: {ans}"

@app.route("/frenchToEnglish")
def FrenchtoEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    ans = french_to_english(textToTranslate)
    return "Translated text to English: {ans}"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
