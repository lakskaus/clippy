from pynput.mouse import Listener
from tkinter import Tk, Canvas
import threading
import time

import pyautogui


class clicker():

    def __init__(self) -> None:
        self.x, self.y = 0, 0
        self.has_clicked = False
        self.clickx, self.clicky = 0, 0
        
        self.winx, self.winy, self.width, self.height = 100, 100, 0, 0
        self.root = Tk()
        # Remove window decorations
        self.root.overrideredirect(True)
        
        
        print(self.root.wm_attributes())
        
        # Make window stay on top
        self.root.wm_attributes("-topmost", 1)
        # Make the window semi-transparent
        
        self.root.wm_attributes("-alpha", 0.3)


        print(self.root.wm_attributes())

        # Set the size and position of the window
        self.root.geometry(f'{self.width}x{self.height}+{self.winx}+{self.winy}')

        # Create a black canvas filling the window
        canvas = Canvas(self.root, bg='black', bd=0, highlightthickness=0)
        canvas.pack(fill='both', expand=True)


    
    def start_window(self):
        self.root.mainloop()


    
    def update_window(self):
        self.root.geometry(f'{self.width}x{self.height}+{self.winx}+{self.winy}')



    def on_move(self, x, y):
        self.x = x
        self.y = y

        if(self.has_clicked):
            self.winx, self.width = min(self.x, self.clickx), abs(self.x - self.clickx) + 10
            self.winy, self.height = min(self.y, self.clicky), abs(self.y - self.clicky) + 10
            self.update_window()
        else:
            self.winx, self.width = x - 2, 4
            self.winy, self.height = y - 2,  4
            self.update_window()


    def on_click(self, x, y, button, pressed):
        if pressed:
            print(f'Pressed at {(x, y)}')
            if self.has_clicked:
                self.root.wm_attributes("-alpha", 0.0)
                time.sleep(0.01)
                self.take_screen()
                print("Second Click happened")
                self.root.destroy()
                return True
            else:
                self.winx, self.winy = x, y
                self.clickx, self.clicky = x, y
                self.has_clicked = True
                self.update_window()


    def take_screen(self):
        # Take a screenshot of a specific region
        screenshot = pyautogui.screenshot(region=(self.winx, self.winy, self.width, self.height))

        now = time.localtime()
        timestamp = time.strftime('%Y%m%d_%H%M%S', now)

        # Save the screenshot
        screenshot.save(f'Pictures/Screenshots/screenshot_{timestamp}.png')


clicker_instance = clicker()
listener = Listener(on_click=clicker_instance.on_click, on_move=clicker_instance.on_move)
thread = threading.Thread(target=listener.start)
thread.start()

clicker_instance.start_window()