import time

from PIL import ImageGrab, ImageOps
import numpy as np
import pyautogui


class Bot:
    # Dino Bot
    def __init__(self):
        self.restart_coords = (1284, 829)
        self.dino_coords = (600, 937)
        self.area = [
            self.dino_coords[0] + 90,
            self.dino_coords[1],
            self.dino_coords[0] + 150,
            self.dino_coords[1] + 5,
        ]

    def set_dino_coords(self, x, y):
        """
        Change default dino coordinates
        """
        self.dino_coords = (x, y)

    def set_area(self, x):
        """
        Change default area coordinates
        """
        self.area[0] += x
        self.area[2] += x

    def restart(self):
        """
        Restart the game and set default crawl run
        """
        pyautogui.click(self.restart_coords)
        pyautogui.keyDown("down")

    def jump(self):
        """
        jump, delay and duck again
        """
        pyautogui.keyUp("down")
        pyautogui.keyDown("space")
        time.sleep(0.085)
        pyautogui.keyUp("space")
        pyautogui.keyDown("down")

    def detectObj(self):
        """
        check color or the area
        """
        image = ImageGrab.grab(self.area)
        gray_img = ImageOps.grayscale(image)
        arr = np.array(gray_img.getcolors())
        return arr.mean()

    def main(self):
        self.restart()
        count = 0
        loop = 0
        while True:
            if self.detectObj() < 166.5:
                self.jump()
                count += 1
                print(count)
            """
            (820, 937, 880, 942)
            1156 points
            [875, 937, 935, 942]
            1394 points
            [900, 937, 960, 942]
            1440 points
            shitty code to move the area for detection 😂😂😂
            """
            if count == 5:
                self.set_area(10)
                print(self.area)
                loop += 1
                count = 0
            if loop == 3:
                self.set_area(10)
                print(self.area)
                loop = 0


"""
Start bot
chrome://dino/
resolution 2560x1440
"""
dino = Bot()
dino.main()
