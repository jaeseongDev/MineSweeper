from mine import Mine
from new_button import New_button
from tkinter import *
from tkinter import ttk, messagebox

class New_button_double_list:
    def __init__(self, window, width, height, mine_count):
        self.window = window
        self.width = width
        self.height = height
        self.mine_count = mine_count
        mine = Mine(self.width, self.height, self.mine_count)
        self.mine_list = mine.create_mine_list()
        self.mine_count_nearby_button_double_list = mine.create_mine_count_nearby_button_double_list(self.mine_list)

    def click_test(self, x, y):
        if self.mine_count_nearby_button_double_list[y][x] == '지뢰':
            for x in range(self.width):
                for y in range(self.height):
                    if self.mine_count_nearby_button_double_list[y][x] == '지뢰':
                        self.new_button_double_list[y][x].configure(text="지뢰", foreground="red", background="gray80",
                                                                    state="disabled")
            messagebox.showinfo("GameOver", "LOSE")

        else:
            if x == 0:
                if self.mine_count_nearby_button_double_list[y][x] != '지뢰':
                    self.new_button_double_list[y][x].configure(
                        text=self.mine_count_nearby_button_double_list[y][x],
                        state="disabled", background="gray80")
                    # self.new_button_double_list[y][x - 1].configure(
                    #     text=self.mine_count_nearby_button_double_list[y][x - 1],
                    #     state="disabled", background="gray80")
                if self.mine_count_nearby_button_double_list[y][x + 1] != '지뢰':
                    self.new_button_double_list[y][x + 1].configure(
                        text=self.mine_count_nearby_button_double_list[y][x + 1],
                        state="disabled", background="gray80")

                if y == 0:
                    if self.mine_count_nearby_button_double_list[y + 1][x] != '지뢰':
                        self.new_button_double_list[y + 1][x].configure(
                            text=self.mine_count_nearby_button_double_list[y + 1][x],
                            state="disabled", background="gray80")
                    # self.new_button_double_list[y + 1][x - 1].configure(
                    #     text=self.mine_count_nearby_button_double_list[y + 1][x - 1],
                    #     state="disabled", background="gray80")
                    if self.mine_count_nearby_button_double_list[y + 1][x + 1] != '지뢰':
                        self.new_button_double_list[y + 1][x + 1].configure(
                            text=self.mine_count_nearby_button_double_list[y + 1][x + 1],
                            state="disabled", background="gray80")

                elif y == self.height - 1:
                    # self.new_button_double_list[y - 1][x - 1].configure(
                    #     text=self.mine_count_nearby_button_double_list[y - 1][x - 1],
                    #     state="disabled", background="gray80")
                    if self.mine_count_nearby_button_double_list[y - 1][x + 1] != '지뢰':
                        self.new_button_double_list[y - 1][x + 1].configure(
                            text=self.mine_count_nearby_button_double_list[y - 1][x + 1],
                            state="disabled", background="gray80")
                    if self.mine_count_nearby_button_double_list[y - 1][x] != '지뢰':
                        self.new_button_double_list[y - 1][x].configure(
                            text=self.mine_count_nearby_button_double_list[y - 1][x],
                            state="disabled", background="gray80")
                else:
                    if self.mine_count_nearby_button_double_list[y + 1][x] != '지뢰':
                        self.new_button_double_list[y + 1][x].configure(
                            text=self.mine_count_nearby_button_double_list[y + 1][x],
                            state="disabled", background="gray80")
                    if self.mine_count_nearby_button_double_list[y + 1][x + 1] != '지뢰':
                        self.new_button_double_list[y + 1][x + 1].configure(
                            text=self.mine_count_nearby_button_double_list[y + 1][x + 1],
                            state="disabled", background="gray80")
                    if self.mine_count_nearby_button_double_list[y - 1][x + 1] != '지뢰':
                        self.new_button_double_list[y - 1][x + 1].configure(
                            text=self.mine_count_nearby_button_double_list[y - 1][x + 1],
                            state="disabled", background="gray80")
                    if self.mine_count_nearby_button_double_list[y - 1][x] != '지뢰':
                        self.new_button_double_list[y - 1][x].configure(
                            text=self.mine_count_nearby_button_double_list[y - 1][x],
                            state="disabled", background="gray80")

            elif x == self.width - 1:
                if self.mine_count_nearby_button_double_list[y][x] != '지뢰':
                    self.new_button_double_list[y][x].configure(
                        text=self.mine_count_nearby_button_double_list[y][x],
                        state="disabled", background="gray80")
                if self.mine_count_nearby_button_double_list[y][x -1] != '지뢰':
                    self.new_button_double_list[y][x - 1].configure(
                        text=self.mine_count_nearby_button_double_list[y][x - 1],
                        state="disabled", background="gray80")
                # self.new_button_double_list[y][x + 1].configure(
                #     text=self.mine_count_nearby_button_double_list[y][x + 1],
                #     state="disabled", background="gray80")

                if y == 0:
                    if self.mine_count_nearby_button_double_list[y + 1][x] != '지뢰':
                        self.new_button_double_list[y + 1][x].configure(
                            text=self.mine_count_nearby_button_double_list[y + 1][x],
                            state="disabled", background="gray80")
                    if self.mine_count_nearby_button_double_list[y + 1][x - 1] != '지뢰':
                        self.new_button_double_list[y + 1][x - 1].configure(
                            text=self.mine_count_nearby_button_double_list[y + 1][x - 1],
                            state="disabled", background="gray80")
                    # self.new_button_double_list[y + 1][x + 1].configure(
                    #     text=self.mine_count_nearby_button_double_list[y + 1][x + 1],
                    #     state="disabled", background="gray80")

                elif y == self.height - 1:
                    if self.mine_count_nearby_button_double_list[y - 1][x - 1] != '지뢰':
                        self.new_button_double_list[y - 1][x - 1].configure(
                            text=self.mine_count_nearby_button_double_list[y - 1][x - 1],
                            state="disabled", background="gray80")
                    # self.new_button_double_list[y - 1][x + 1].configure(
                    #     text=self.mine_count_nearby_button_double_list[y - 1][x + 1],
                    #     state="disabled", background="gray80")
                    if self.mine_count_nearby_button_double_list[y - 1][x] != '지뢰':
                        self.new_button_double_list[y - 1][x].configure(
                            text=self.mine_count_nearby_button_double_list[y - 1][x],
                            state="disabled", background="gray80")
                else:
                    if self.mine_count_nearby_button_double_list[y + 1][x] != '지뢰':
                        self.new_button_double_list[y + 1][x].configure(
                            text=self.mine_count_nearby_button_double_list[y + 1][x],
                            state="disabled", background="gray80")
                    if self.mine_count_nearby_button_double_list[y + 1][x - 1] != '지뢰':
                        self.new_button_double_list[y + 1][x - 1].configure(
                            text=self.mine_count_nearby_button_double_list[y + 1][x - 1],
                            state="disabled", background="gray80")
                    if self.mine_count_nearby_button_double_list[y - 1][x - 1] != '지뢰':
                        self.new_button_double_list[y - 1][x - 1].configure(
                            text=self.mine_count_nearby_button_double_list[y - 1][x - 1],
                            state="disabled", background="gray80")
                    if self.mine_count_nearby_button_double_list[y - 1][x] != '지뢰':
                        self.new_button_double_list[y - 1][x].configure(
                            text=self.mine_count_nearby_button_double_list[y - 1][x],
                            state="disabled", background="gray80")
            else:
                if self.mine_count_nearby_button_double_list[y][x] != '지뢰':
                    self.new_button_double_list[y][x].configure(
                        text=self.mine_count_nearby_button_double_list[y][x],
                        state="disabled", background="gray80")
                if self.mine_count_nearby_button_double_list[y][x - 1] != '지뢰':
                    self.new_button_double_list[y][x - 1].configure(
                        text=self.mine_count_nearby_button_double_list[y][x - 1],
                        state="disabled", background="gray80")
                if self.mine_count_nearby_button_double_list[y][x + 1] != '지뢰':
                    self.new_button_double_list[y][x + 1].configure(
                        text=self.mine_count_nearby_button_double_list[y][x + 1],
                        state="disabled", background="gray80")

                if y == 0:
                    if self.mine_count_nearby_button_double_list[y + 1][x] != '지뢰':
                        self.new_button_double_list[y + 1][x].configure(
                            text=self.mine_count_nearby_button_double_list[y + 1][x],
                            state="disabled", background="gray80")
                    if self.mine_count_nearby_button_double_list[y + 1][x - 1] != '지뢰':
                        self.new_button_double_list[y + 1][x - 1].configure(
                            text=self.mine_count_nearby_button_double_list[y + 1][x - 1],
                            state="disabled", background="gray80")
                    if self.mine_count_nearby_button_double_list[y + 1][x + 1] != '지뢰':
                        self.new_button_double_list[y + 1][x + 1].configure(
                            text=self.mine_count_nearby_button_double_list[y + 1][x + 1],
                            state="disabled", background="gray80")

                elif y == self.height - 1:
                    if self.mine_count_nearby_button_double_list[y - 1][x - 1] != '지뢰':
                        self.new_button_double_list[y - 1][x - 1].configure(
                            text=self.mine_count_nearby_button_double_list[y - 1][x - 1],
                            state="disabled", background="gray80")
                    if self.mine_count_nearby_button_double_list[y - 1][x + 1] != '지뢰':
                        self.new_button_double_list[y - 1][x + 1].configure(
                            text=self.mine_count_nearby_button_double_list[y - 1][x + 1],
                            state="disabled", background="gray80")
                    if self.mine_count_nearby_button_double_list[y - 1][x] != '지뢰':
                        self.new_button_double_list[y - 1][x].configure(
                            text=self.mine_count_nearby_button_double_list[y - 1][x],
                            state="disabled", background="gray80")
                else:
                    if self.mine_count_nearby_button_double_list[y + 1][x] != '지뢰':
                        self.new_button_double_list[y + 1][x].configure(
                            text=self.mine_count_nearby_button_double_list[y + 1][x],
                            state="disabled", background="gray80")
                    if self.mine_count_nearby_button_double_list[y + 1][x - 1] != '지뢰':
                        self.new_button_double_list[y + 1][x - 1].configure(
                            text=self.mine_count_nearby_button_double_list[y + 1][x - 1],
                            state="disabled", background="gray80")
                    if self.mine_count_nearby_button_double_list[y + 1][x + 1] != '지뢰':
                        self.new_button_double_list[y + 1][x + 1].configure(
                            text=self.mine_count_nearby_button_double_list[y + 1][x + 1],
                            state="disabled", background="gray80")
                    if self.mine_count_nearby_button_double_list[y - 1][x - 1] != '지뢰':
                        self.new_button_double_list[y - 1][x - 1].configure(
                            text=self.mine_count_nearby_button_double_list[y - 1][x - 1],
                            state="disabled", background="gray80")
                    if self.mine_count_nearby_button_double_list[y - 1][x + 1] != '지뢰':
                        self.new_button_double_list[y - 1][x + 1].configure(
                            text=self.mine_count_nearby_button_double_list[y - 1][x + 1],
                            state="disabled", background="gray80")
                    if self.mine_count_nearby_button_double_list[y - 1][x] != '지뢰':
                        self.new_button_double_list[y - 1][x].configure(
                            text=self.mine_count_nearby_button_double_list[y - 1][x],
                            state="disabled", background="gray80")

    def create(self):
        # 지뢰찾기 할 때 사용하는 버튼들
        new_buttons_frame = ttk.LabelFrame(self.window)
        new_buttons_frame.grid(column=0, row=1)


        # 이중 리스트
        new_button_double_list = []  # 아무것도 누르지 않은 상태의 버튼들이 모여있는 이중 리스트
        for y in range(self.height):
            # 변수 초기화
            temp_row = []
            for x in range(self.width):
                new_button_class = New_button(x, y, new_buttons_frame, self.click_test)
                new_button = new_button_class.new_button
                temp_row.append(new_button)
                # temp_row[x].grid(column=x, row=y + 1)
                # temp_row[x].configure(width=2, command=lambda: self.click(new_button.x, new_button.y))

            new_button_double_list.append(temp_row)
        # print('new_button_double_list : ', new_button_double_list)

        self.new_button_double_list = new_button_double_list # 인스턴스의 new_button_double_list에 값을 저장






