from mine import Mine
from new_button_double_list import New_button_double_list
from new_button import New_button
from tkinter import *
from tkinter import ttk, messagebox

class MineSweeper:
    def __init__(self):
        window = Tk()
        window.title("지뢰 찾기")
        window.resizable(False, False)
        self.window = window

        width = 10 # 지뢰찾기의 너비
        height = 8 # 지뢰찾기의 높이
        mine_count = 10 # 지뢰 개수

        # new_button_double_list 클래스
        new_button_double_list = New_button_double_list(window, width, height, mine_count)
        new_button_double_list.create()

        # 스마일 이모티콘 버튼  -----------------------------------------------------------------------
        def home():
            messagebox.showinfo("Game Restart", "게임을 재시작하겠습니다.")
            self.window.destroy()
            MineSweeper()

        home_img = PhotoImage(file="picture/smile_imoticon.gif")
        home_img_resize = home_img.subsample(7, 7)
        home_button = Button(self.window, command=home, text="게임 종료", image=home_img_resize, width=40, height=17)
        home_button.grid(column=0, row=0)
        # ---------------------------------------------------------------------------------------------

        self.window.mainloop()

MineSweeper()

