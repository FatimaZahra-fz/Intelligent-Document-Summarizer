import pdfplumber
import re

def extract_text(file):
    try:
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = (page.extract_text())
                if page_text:
                    text += (page_text + " ")
        text = text.replace("\n"," ")
        text = re.sub(r"\s+"," ",text)
        return text.strip()
    except:
        return None
    

