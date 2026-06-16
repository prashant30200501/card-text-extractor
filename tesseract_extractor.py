import cv2
import pytesseract
import re


def extract_contact_info(text):
    phone_pattern = r'\+?\d[\d -]{8,20}\d'
    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    phones = []

    for line in text.splitlines():
        matches = re.findall(phone_pattern, line)

        if matches:
            phones.extend(matches)

    emails = re.findall(email_pattern, text)

    return {
        "phones": phones,
        "emails": emails
    }


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

image = cv2.imread("images/card_4.jpg")

"""image =cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)"""

"""gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)"""

"""gray = cv2.resize(
    gray,
    None,
    fx=2,
    fy=2,
    interpolation=cv2.INTER_CUBIC
)"""


image = cv2.imread("images/card_4.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

height, width = gray.shape

contact_region = gray[
    int(height * 0.25):int(height * 0.75),
    int(width * 0.35):int(width * 0.95)
]

cv2.imwrite("output/contact_region.jpg", contact_region)

contact_region = cv2.resize(
    contact_region,
    None,
    fx=4,
    fy=4,
    interpolation=cv2.INTER_CUBIC
)

cv2.imwrite("output/contact_region_big.jpg", contact_region)

text = pytesseract.image_to_string(
    contact_region,
    config="--psm 11"
)

print("RAW OCR:")
print(repr(text))

result = extract_contact_info(text)

print(result)