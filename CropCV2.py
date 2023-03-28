from PIL import Image
from pdf2image import convert_from_path
from pathlib import Path
import os
import cv2 #pip install opencv-python
import numpy as np
#nahrani pdfka
cesta_pdfka = Path('./a.pdf')
# cesta_pdfka = Path("C:\Users\Admin\Desktop\CropMasteikova\Ocni_terapeuticke_systemy_-_podklady_k_prednasce.pdf")
# cesta_pdfka = Path(input("Přetáhněte sem pdf_soubor(tím se sem nahraje jeho cesta) a potvrďte Enterem:\n\t"))
print("\nNyní prosím čekejte, pdf se nahrává a zpracovává.")
pages = convert_from_path(cesta_pdfka, 600)
type(pages[0])

Images = []
for each in pages:
    image = np.array(each)
    # Load image, grayscale, median blur, sharpen image
    # image = cv2.imread('1.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 5)
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv2.filter2D(blur, -1, sharpen_kernel)

    # Threshold and morph close
    thresh = cv2.threshold(sharpen, 160, 255, cv2.THRESH_BINARY_INV)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Find contours and filter using threshold area
    cnts = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    min_area = 1000
    max_area = 4000
    image_number = 0
    
    # cv2.imshow('sharpen', sharpen)
    # cv2.imshow('close', close)
    # cv2.imshow('thresh', thresh)
    # cv2.imshow('image', image)
    
    # cv2.imwrite('ROI_sharpen.png', sharpen)
    # cv2.imwrite('ROI_close.png', close)
    # cv2.imwrite('ROI_thresh.png',  thresh)
    # cv2.imwrite('ROI_image.png', image)
    # break
    
    
    for c in cnts:
        area = cv2.contourArea(c)
        cv2.imwrite("area.png", area)
        break
        if area > min_area and area < max_area:
            x,y,w,h = cv2.boundingRect(c)
            ROI = image[y:y+h, x:x+w]
            cv2.imwrite('ROI_{}.png'.format(image_number), ROI)
            cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
            image_number += 1
    break
    cv2.waitKey()
    
hranice = [317 ,2169 ,2353 ,4200 ,686 ,2074 ,2596 ,3978 ,4504 ,5890]
delky = []
for i in range(len(hranice)):
    delka = hranice[i+1] - hranice[i]
    delky.append(delka)
    print(hranice[i+1] - hranice[i])
    
    
    
    
    
import numpy as np
from PIL import Image


# Convert degree range (0 - 360) to uint8 value range (0 - 255)
def deg_to_uint8(deg):
    return deg / 360 * 255


# Convert percentage range (0 - 100) to uint8 value range (0 - 255)
def perc_to_uint8(perc):
    return perc / 100 * 255


# Open image, and convert to HSV color space for NumPy slicing
img = Image.open('ROI_image.png')
hsv = np.array(img.convert('HSV'))

# Masking color-ish area via NumPy slicing using upper and/or lower
# bounds for hue, saturation, and value
box = hsv[..., 0] > deg_to_uint8(55)        # Hue > 55°
box &= hsv[..., 0] < deg_to_uint8(65)       # Hue < 65°
box &= hsv[..., 1] > perc_to_uint8(80)      # Saturation > 80%
box &= hsv[..., 2] > perc_to_uint8(80)      # Value > 80%

# Find x, y coordinates of masked area; extract first and last elements
xy = np.argwhere(box)
t, b = xy[[0, -1], 0]
l, r = xy[[0, -1], 1]

# For better cropping, maybe add some additional border
bl, bt, br, bb = (3, 3, 3, 3)

# Actual cropping of the image
crop = img.crop((l + bl, t + bt, r - br, b - bb))
crop.save('crop.png')









import numpy as np
import cv2

im = cv2.imread('ROI_image.png')
rows,cols = im.shape[:2]
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,125,255,0)
thresh = (255-thresh)
thresh2=thresh.copy()
im2, contours = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# cv2.imshow('image1',im)
# cv2.imshow('image3',thresh2)
#cv2.drawContours(im, contours, -1, (0,255,0), 3) #draw all contours
contnumber=4
cv2.drawContours(im, contours, contnumber, (0,255,0), 3) #draw only contour contnumber
# cv2.imshow('contours', im)

[vx,vy,x,y] = cv2.fitLine(contours[contnumber], cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv2.line(im,(cols-1,righty),(0,lefty),(0,255,255),2)

cv2.imwrite('result.png', im)

# cv2.waitKey(0)
# cv2.destroyAllWindows()





import numpy as np 
import cv2

#load the image
image = cv2.imread('ROI_image.png')

# grayscale
result = image.copy()
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# adaptive threshold
thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,51,9)

# Fill rectangular contours
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    cv2.drawContours(thresh, [c], -1, (255,255,255), -1)

# Morph open
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=4)

# Draw rectangles, the 'area_treshold' value was determined empirically
cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
area_treshold = 4000
for c in cnts:
    print("jjjj")
    if cv2.contourArea(c) > area_treshold :
      x,y,w,h = cv2.boundingRect(c)
      print(x,y,w,h) #TODO: Toto chceš!!!
      cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 3)

cv2.imshow('thresh', thresh)
cv2.imshow('opening', opening)
cv2.imshow('image', image)

cv2.imwrite('thresh.png', thresh)
cv2.imwrite('opening.png', opening)
cv2.imwrite('image.png', image)
cv2.waitKey()
# https://stackoverflow.com/questions/67302143/opencv-python-how-to-detect-filled-rectangular-shapes-on-picture
# https://stackoverflow.com/questions/14134892/convert-image-from-pil-to-opencv-format