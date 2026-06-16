import cv2
import easyocr
import re
import spacy

# Load spaCy's English model for Name Entity Recognition (NER)
nlp = spacy.load("en_core_web_sm")

# Initialize EasyOCR (loads model to memory once)
reader = easyocr.Reader(['en'])

def extract_card_details(text):
    # 1. Load image and run EasyOCR
    image = cv2.imread("images/card_4.jpg")
    results = reader.readtext(image)
    
    # Combine extracted text lines into a list and a single string block
    text_lines = [res[1] for res in results]
    full_text = "\n".join(text_lines)
    
    print("--- Extracted Raw Text ---")
    print(full_text)
    print("--------------------------\n")
    
    # 2. Extract Email using Regex
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, full_text)
    
    # 3. Extract Phone Number using Regex (handles common variations)
    phone_pattern = r'(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    phones = re.findall(phone_pattern, full_text)
    
    # 4. Extract Name using spaCy NER
    # Cards often have names in all caps or isolated lines, so we inspect individual lines first
    detected_names = []
    for line in text_lines:
        doc = nlp(line)
        for ent in doc.ents:
            if ent.label_ == "PERSON" and ent.text not in detected_names:
                detected_names.append(ent.text)
                
    # Fallback: Check the full block text if line-by-line misses it
    if not detected_names:
        doc = nlp(full_text)
        detected_names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]

    # Format Output
    return {
        "Name": detected_names[0] if detected_names else "Not Found",
        "Email": emails[0] if emails else "Not Found",
        "Phone": phones[0] if phones else "Not Found"
    }

# --- Execution Example ---
# data = extract_card_details("path_to_your_card.jpg")
# print("Structured Data:", data)
