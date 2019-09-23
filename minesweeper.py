import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.title("지뢰 찾기")

# 변수 설정
new_button = [] # 아무것도 누르지 않은 상태의 버튼들이 모여있는 이중 리스트

def new_button_click():
    pass


# 지뢰찾기의 행과 열 개수
width = 10
height = 15

# 지뢰 개수
mine_count = 10

# new_button에 width, height만큼 버튼들을 이중리스트로 생성
for i in range(height):
    temp_row = [] # 변수 초기화
    for j in range(width):
        # temp_row.append(0)
        temp_row.append(ttk.Button(window, text="N", command=new_button_click))
        temp_row[j].grid(column= j, row = i)
    new_button.append(temp_row)

# 지뢰 랜덤 생성
for i in range(mine_count):
    



window.mainloop()

