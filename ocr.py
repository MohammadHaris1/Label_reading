try:
    from PIL import Image
except ImportError:
    import Image
    
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"D:\Master_class\warrior_way\d16_label_reading\Tesseract-OCR\tesseract.exe"

def recText (filename):
    text = pytesseract.image_to_string(Image.open (filename))
    return text

info = recText ('3.jpeg')
print (info)

file = open("result.txt", "w")
file.write (info)
file.close()
print ("Written Successful")
