import cv2
import numpy as np
import argparse
import pandas as pd

# Using argparse library to create an argument parser. So that we can directly give an image path from the command prompt.
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Image Path")
args = vars(ap.parse_args())

image_path = args["image"]

# Read image using OpenCV
img = cv2.imread(image_path)

clicked = False
r = g = b = xpos = ypos = 0

# Read colors.csv using Pandas
index = ["color", "color_name", "hex", "R", "G", "B"]
df = pd.read_csv("colors.csv", names=index, header=None)


# The getColorName function will get the color name, we calculate a distance(d) which tells us how close we are to color and choose the one having minimum distance.
def getColorName(R, G, B):
    minimum = 10000
    for i in range(len(df)):
        dist = abs(R - int(df.loc[i, "R"])) + abs(G - int(df.loc[i, "G"])) + abs(B - int(df.loc[i, "B"]))
        if dist <= minimum:
            minimum = dist
            color_name = df.loc[i, "color_name"]
    return color_name


# The draw function will calculate the rgb values of the pixel which we double click
def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


# Name the window as "Image"
cv2.namedWindow("Image")

# Set a mouse callback event -- Calls the draw function whenever a mouse event occurs
cv2.setMouseCallback("Image", draw)


# Display the image
while True:
    cv2.imshow("Image", img)

    if clicked:
        cv2.rectangle(img, (20,20), (750, 60), (b,g,r), -1)

        # Create the string to be displayed (Color Name + RGB values)
        name = getColorName(r, g, b) + " | R=" + str(r) + " G=" + str(g) + " B=" + str(b)

        cv2.putText(img, name, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        # For light colors we want text to be displayed in black coloe
        if(r+g+b >= 600):
            cv2.putText(img, name, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    # Break the loop when user hits 'esc' key  
    if cv2.waitKey(20) & 0xFF ==27:
        break

cv2.destroyAllWindows()