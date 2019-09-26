import tkinter
import tkinter.messagebox
from tkinter import ttk
from tkinter import *
from mine import Mine

class New_button:
    def __init__(self, x, y, window, click):
        self.x = x
        self.y = y
        self.window = window
        new_button = Button(window, background="gray63")
        new_button.configure(width=2, command=lambda: click(x, y)) # 다른 클래스에서 click 함수를 받아올 수 있는지 확인
        new_button.grid(column=x, row=y + 1)
        self.new_button = new_button