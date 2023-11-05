from flask import Flask, render_template, request
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('9vkZ1HDH0CbC7EsgoWLI4Cm19BWEYH7elU4axTNPAdBi')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/33e0d3f6-90e7-4199-b88f-72a319b1b034')

def english_to_french(text1):
    """Translates English text to French"""
    frenchtranslation = language_translator.translate(
        text=text1,
        model_id='en-fr'
    ).get_result()
    return frenchtranslation['translations'][0]['translation']

def french_to_english(text1):
    """Translates French text to English"""
    englisgtranslation = language_translator.translate(
        text=text1,
        model_id='fr-en'
    ).get_result()
    return englisgtranslation['translations'][0]['translation']
app = Flask(__name__)


@app.route('/')
def hello_world():
    # Translate text
    english_text = "Hello, how are you?"
    french_text = english_to_french(english_text)
    translated_english_text = french_to_english(french_text)

    # Render HTML template with translated text
    return render_template('index.html',
                           english_text=english_text,
                           french_text=french_text,
                           translated_english_text=translated_english_text)


if __name__ == '__main__':
    app.run()
