import numpy as np 
import cv2
from pdf2image import convert_from_path

def Recognize(page):
    # #load the image
    # image = cv2.imread('ROI_image.png')


    # pages = convert_from_path("./a.pdf", 600)[0]

    image = np.array(page)

    # grayscale
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

    pocet = 0
    # hranice = []
    Xs = []
    Ys = []
    Ws = []
    Hs = []
    for c in cnts:
        pocet += 1
        if cv2.contourArea(c) > area_treshold :
            x,y,w,h = cv2.boundingRect(c)
            # print(x,y,w,h) #TODO: Toto chceš!!!
            # hranice.append([x,y,w,h])
            Xs.append(x)
            Ys.append(y)
            Ws.append(w)
            Hs.append(h)
            # cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 3)
            # cv2.imwrite(f'test{pocet}.png', image)



    X0 = sorted([each for each in set(Xs) if each > 10])
    Y0 = sorted([each for each in set(Ys) if each > 10])
    sirka = sum(set(Ws))/len(set(Ws))
    vyska = sum(set(Hs))/len(set(Hs))

    # image.shape
    
    return (X0, Y0, sirka, vyska, pocet)

# https://stackoverflow.com/questions/67302143/opencv-python-how-to-detect-filled-rectangular-shapes-on-picture
# https://stackoverflow.com/questions/14134892/convert-image-from-pil-to-opencv-format