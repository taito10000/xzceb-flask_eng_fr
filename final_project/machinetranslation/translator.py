import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

lang_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

lang_translator.set_service_url(url)
lang_translator.set_disable_ssl_verification(True)


def english_2_french(txt):
    fr_txt = lang_translator.translate(
        text=txt,
        model_id='en-fr').get_result()
    translation = fr_txt['translations'][0]['translation']
    return translation

def french_2_english(txt):
    en_txt = lang_translator.translate(
        text=txt,
        model_id='fr-en').get_result()
    translation = en_txt['translations'][0]['translation']
    return translation
