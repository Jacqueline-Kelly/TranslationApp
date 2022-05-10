import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Creating translator instance
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-05-07',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''
    Uses IBM Watson translator instance to translate an english input to french
    '''
    french_text = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    '''
    Uses IBM Watson translator instance to translate an french input to english
    '''
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return english_text['translations'][0]['translation']

