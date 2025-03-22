from googletrans import Translator
import google.generativeai as genai


def translate_uz_en(text):
    t = Translator()
    result = t.translate(text, src='uz', dest='en')

    return result.text


def translate_en_uz(text):
    t = Translator()
    result = t.translate(text, src='en', dest='uz')

    return result.text


def ai_get(text):
    genai.configure(api_key="AIzaSyBpCkpP_CqXRIHoBEd2S34dltRzDMhPLt4")
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(text)
    return response.text


