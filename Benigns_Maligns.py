import time
import cv2 #cv2 kütüphanesi dahil olabilmesi için python 3.8 sürümü kullanılmalı.
import mss
import numpy
import pytesseract

# Hazırlayan Serhan HERGÜN

mon = {'top': 100, 'left': 0, 'width': 1200, 'height': 1000} # Taratılan alan. 
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract'#Tesseract-OCR indirdikten sonra okumayı gerçekleştirmesi için pathi tanımlama yeri.

with mss.mss() as sct:
    while True:
        im = numpy.asarray(sct.grab(mon)) #numpyi pytesseracta bağlama yeri.
        text = pytesseract.image_to_string(im) 

        """Benigns"""
        if("TIRADS: 2" in text):
            print("Benigns")
        if("TIRADS: 3" in text):
            print("Benigns")
        """Benigns"""

        """Maligns"""
        if("TIRADS: 4a" in text):
            print("Maligns")
        if("TIRADS: 4b" in text):
            print("Maligns")
        if("TIRADS: 4c" in text):
            print("Maligns")
        if("TIRADS: 5" in text):
            print("Maligns")
        """Maligns"""

        # in kullanmamın sebebi kodumun başlangıcında tanımladığım mon kısmı içerisinde "TIRADS" kelimesinin geçip geçmediğini ve yanındaki sayısını okutmama yarıyor.

        cv2.imshow('Image', im) # mon kısmının hangi alanı okuduğunu bize göstermesini sağlıyor.
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            cv2.destroyAllWindows()
            break

        time.sleep(1)   