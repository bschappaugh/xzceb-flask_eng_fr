import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-10-11',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(englishText):
    french_text = language_translator.translate(
        text=englishText,
        model_id='en-fr'
    ).get_result()['translations'][0]['translation']
    return french_text


def frenchToEnglish(frenchText):
    english_text = language_translator.translate(
        text=frenchText,
        model_id='fr-en'
    ).get_result()['translations'][0]['translation']
    return english_text

print(englishToFrench('This is English'))
print(frenchToEnglish('C\'est Anglais'))