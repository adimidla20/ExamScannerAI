import re

def clean_text(text):

    text = text.replace('QE. 1.', '1.')
    text = text.replace('2,', '2.')
    text = text.replace('6:', '6.')
    text = text.replace('20.', '10.')
    text = text.replace('8,', '8.')

    text = re.sub(r'[“”]', '"', text)

    return text