import pytesseract
from PIL import Image
import requests
from io import BytesIO

# URL of the image
image_url = 'https://graph.org/file/3e1776a2ece811418f1fe.jpg'

# Download the image from the URL
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# Use pytesseract to do OCR on the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(f"your text: ${text}")
