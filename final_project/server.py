import sys
sys.path.append(r"C:\Users\Base\Documents\translation_project_py\machinetranslation")
from translator import english_to_french
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

print(english_to_french("hello"))
@app.route("/englishtoFrench")
def EnglishtoFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return english_to_french("textToTranslate")

@app.route("/frenchToEnglish")
def FrenchtoEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    ans = translator.french_to_english(textToTranslate)
    return "Translated text to English: {ans}"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
