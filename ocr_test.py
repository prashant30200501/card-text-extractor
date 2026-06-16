import cv2
import pytesseract
import re


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

image = cv2.imread("images/card_1.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray)

phone_pattern = r'(\+?\d[\d\s-]{8,20}\d)'

phones = re.findall(phone_pattern, text)

print("Phones Found:")
print(phones)

email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

emails = re.findall(email_pattern, text)

print("Emails Found:")
print(emails)

