from PIL import Image
import pytesseract

image_1='image_1.jpg'
img_obj=Image.open(image_1)
text=pytesseract.image_to_string(img_obj)
print(text)