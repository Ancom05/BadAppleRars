import cv2
import pygame


def FrameCapture(path):
    vidObj = cv2.VideoCapture(path)
    count = 0
    success = 1
    string = ""
    totalColorsLength = 0
    loopsCounter = 0
    size =  2569538
    byteArray = bytearray(size)
    with open("bad_apple.dat", "wb") as file:
        string = ""
        stringTmp = ""
        currentPosInByteArray = 0
        currentFrame = 0
        while success:
            currentFrame += 1
            success, image = vidObj.read()
            if success and currentFrame % 2 == 0:
                image = cv2.resize(image, (255, 186))
                for i in range(186):
                    colorsList = [0]
                    currentIndex = 0
                    prevColor = 200
                    for j in range(1, 255):
                        colorDiff = abs(image[i, j, 0] - image[i, j-1, 0])
                        if image[i, j, 0] > 120 and prevColor <= 120 :
                            colorsList.append(1)
                            prevColor = 200
                            currentIndex += 1
                        if (image[i, j, 0] <= 120 and prevColor > 120) :
                            colorsList.append(1)
                            prevColor = 100
                            currentIndex += 1
                        colorsList[currentIndex] += 1
                    if len(colorsList) == 1 and colorsList[0] == 254:
                        colorsList[0] = 255
                    prevWidth = 0
                    for j in range(len(colorsList)):
                        byteArray[currentPosInByteArray] = colorsList[j]
                        currentPosInByteArray+=1
                        colorValue = 255 * ((j+1)%2)
                        newWidth = prevWidth + colorsList[j]
                        if newWidth > 255:
                            colorsList[j] -= newWidth - 255
                        prevWidth += colorsList[j]
                    totalColorsLength += len(colorsList)
        print(totalColorsLength)
        file.write(byteArray)

if __name__ == '__main__':
    FrameCapture("./bad_apple.mp4")
