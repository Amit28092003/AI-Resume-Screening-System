import re
from pdfminer.high_level import extract_text


def extract_resume_text(file_path):
    """
    Extract text from a PDF resume file
    """

    try:
        text = extract_text(file_path)

        if text is None:
            return ""

        return clean_text(text)

    except Exception as e:
        print("Error reading resume:", e)
        return ""


def clean_text(text):
    """
    Clean extracted text
    """

    # remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    return text.lower()