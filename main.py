import cv2
import pygame


def FrameCapture(path):
    vidObj = cv2.VideoCapture(path)
    count = 0
    success = 1
    string = ""
    totalColorsLength = 0
    loopsCounter = 0
    pygame.init()
    screen = pygame.display.set_mode((480, 360))
    with open("bad_apple.s", "w") as file:
        string = ""
        for i in range(300):
            success, image = vidObj.read()
            #if i % 2 == 0:
            image = cv2.resize(image, (255, 186))
            #string += "li t0, 0x10010000\n"
            for i in range(186):
                colorsList = [0]
                currentIndex = 0
                prevColor = image[i, 0, 0]
                for j in range(1, 255):
                #    screen.set_at((j, i), (image[i, j, 0], image[i, j, 1], image[i, j, 2]))
                    colorDiff = abs(image[i, j, 0] - image[i, j-1, 0])
                    if image[i, j, 0] > 120 and prevColor <= 120:
                        colorsList.append(1)
                        prevColor = 200
                        currentIndex += 1
                    if (image[i, j, 0] <= 120 and prevColor > 120):
                        colorsList.append(1)
                        prevColor = 100
                        currentIndex += 1
                    colorsList[currentIndex] += 1
                if len(colorsList) == 1 and colorsList[0] == 254:
                    colorsList[0] = 255
            # cv2.imwrite("frame%d.jpg" % count, image)
                #colorsList[currentIndex]+=1 #ultimo pixel che prima era sempre mancante
                prevWidth = 0
                for j in range(len(colorsList)):
                    string += str(colorsList[j]) + ", "
                    colorValue = 255 * ((j+1)%2)
                    newWidth = prevWidth + colorsList[j]
                    if newWidth > 255:
                        colorsList[j] -= newWidth - 255
                    for k in range(colorsList[j]):
                        screen.set_at((k+prevWidth, i), (colorValue, colorValue, colorValue))
                    prevWidth += colorsList[j]
                    #string += "add t4, zero, zero\n"
                    #string += "addi t3, zero, %d\n" % colorsList[j]
                    #string += "LOOP%d:\n" % loopsCounter
                    #string += "bge t4, t3, ENDLOOP%d\n" % loopsCounter
                    #string += "addi t4, t4, 1\n"
                    #if j % 2 == 1:
                    #    string += "sw zero, 0(t0)\n"
                    #else:
                    #    string += "sw t1, 0(t0)\n"
                    #string += "addi t0, t0, 4\nj LOOP%d\n" % loopsCounter
                    #loopsCounter += 1
                #string += "addi t0, 152\n"
                totalColorsLength += len(colorsList)
            pygame.display.flip()
            pygame.time.wait(10)
        print(totalColorsLength)
        file.write(string)

if __name__ == '__main__':
    FrameCapture("./bad_apple_trim.mp4")
