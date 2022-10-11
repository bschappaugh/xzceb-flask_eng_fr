"""This module translates words from English to French and French to English."""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
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


def english_to_french(englishtext):
    """This function translates English text to French using IBM Watson."""
    french_text = language_translator.translate(
        text=englishtext,
        model_id='en-fr'
    ).get_result()['translations'][0]['translation']
    return french_text


def french_to_english(frenchtext):
    """This function translates French text to English using IBM Watson."""
    english_text = language_translator.translate(
        text=frenchtext,
        model_id='fr-en'
    ).get_result()['translations'][0]['translation']
    return english_text
