import pyautogui as pg
import time  # Importing the time module

# Create a popup window for text input
input_text = pg.prompt("Enter the text you want to print:", "Entering text")

# Checking that text has been entered
if input_text is not None:
    # Wait 2 seconds before printing text
    time.sleep(2)

    # Print entered text
    pg.typewrite(input_text)
