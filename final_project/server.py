import sys
sys.path.append(r"C:\Users\Base\Documents\translation_project_py\xzceb-flask_eng_fr\machinetranslation")
from translator import *
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

print(english_to_french("hello"),"my little friend")

@app.route("/englishToFrench")
def EnglishtoFrench():
    textToTranslate = request.args.get('textToTranslate')
    ans = english_to_french(textToTranslate)
    return english_to_french(textToTranslate)

@app.route("/frenchToEnglish")
def FrenchtoEnglish():
    textToTranslate = request.args.get('textToTranslate')
    ans = french_to_english(textToTranslate)
    return french_to_english(textToTranslate)

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

print(english_to_french("my little friend"))
print(french_to_english("mon petit ami"))
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
