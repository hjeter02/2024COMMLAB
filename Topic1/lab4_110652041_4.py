# 引入 tkinter 模組來創建 GUI
import tkinter as tk

# 建立主視窗 top 並設定標題
top = tk.Tk()
top.title('Lab4')  # 主視窗的標題名稱

# 建立兩個 Frame 容器 f1 和 f2，用來放置不同的元件
f1 = tk.Frame(top)
f2 = tk.Frame(top)

# 使用 StringVar 來綁定顯示的文字內容
var = tk.StringVar()
var.set("0")  # 初始化顯示為 "0"

# 定義顯示區域（螢幕）的設定函數
def SetValue():
    # 顯示螢幕的 Label，textvariable 綁定 var
    Screen = tk.Label(f1, textvariable=var).grid(row=0, column=1)

# 定義數字或運算符號按鍵按下時的事件
def Click(x):
    global var
    temp = var.get()  # 取得當前顯示的內容
    # 如果顯示為 "Error" 或 "0"，將顯示內容改為按下的數字/符號
    if temp == "Error" or temp == "0":
        var.set(x)
    else:
        # 否則，在顯示內容後添加按下的數字/符號
        temp = temp + x
        var.set(temp)

# 定義清除按鈕的事件，將顯示內容設為 "0"
def Clear():
    global var
    var.set("0")

# 定義計算按鈕的事件，解析並計算顯示的算式
def cal():
    global var
    temp = var.get().split()  # 以空格分割顯示的內容
    a = 0
    b = 0
    op = ''  # 運算符號

    # 判斷負數的情況，處理正負號
    if len(temp) == 5:          # 若兩數皆為負數，陣列長度為 5
        a = int(temp[1]) * -1
        b = int(temp[4]) * -1
        op = temp[2]
    elif len(temp) == 4:        # 若一數為負數，長度為 4
        if temp[0] == '-':      # 第一數為負數
            a = int(temp[1]) * -1
            b = int(temp[3])
            op = temp[2]
        elif temp[2] == '-':    # 第二數為負數
            a = int(temp[0])
            b = int(temp[3]) * -1
            op = temp[1]
    else:                       # 若兩數皆為正數
        a = int(temp[0])
        b = int(temp[2])
        op = temp[1]

    # 根據運算符號執行加減乘除
    if op == '+':
        var.set(a + b)
    elif op == '-':
        var.set(a - b)
    elif op == '*':
        var.set(a * b)
    elif op == '/':
        if b == 0:
            var.set('Error')  # 分母為零時顯示 "Error"
        else:
            var.set(a // b)  # 正常除法（取整）

# 顯示初始的顯示區域
SetValue()
ft = 20  # 字型大小

# 建立按鍵並指定 grid 位置和對應的事件處理函數
Btn0 = tk.Button(f2, text="0", borderwidth=5, width=4, font=ft, command=lambda: Click("0")).grid(row=3, column=0)
Btncle = tk.Button(f2, text="C", borderwidth=5, width=4, font=ft, command=lambda: Clear()).grid(row=3, column=1)
BtnEqu = tk.Button(f2, text="=", borderwidth=5, width=4, font=ft, command=lambda: cal()).grid(row=3, column=2)
BtnDiv = tk.Button(f2, text=" / ", borderwidth=5, width=4, font=ft, command=lambda: Click(" / ")).grid(row=3, column=3)
Btn1 = tk.Button(f2, text="1", borderwidth=5, width=4, font=ft, command=lambda: Click("1")).grid(row=2, column=0)
Btn2 = tk.Button(f2, text="2", borderwidth=5, width=4, font=ft, command=lambda: Click("2")).grid(row=2, column=1)
Btn3 = tk.Button(f2, text="3", borderwidth=5, width=4, font=ft, command=lambda: Click("3")).grid(row=2, column=2)
BtnMul = tk.Button(f2, text=" * ", borderwidth=5, width=4, font=ft, command=lambda: Click(" * ")).grid(row=2, column=3)
Btn4 = tk.Button(f2, text="4", borderwidth=5, width=4, font=ft, command=lambda: Click("4")).grid(row=1, column=0)
Btn5 = tk.Button(f2, text="5", borderwidth=5, width=4, font=ft, command=lambda: Click("5")).grid(row=1, column=1)
Btn6 = tk.Button(f2, text="6", borderwidth=5, width=4, font=ft, command=lambda: Click("6")).grid(row=1, column=2)
BtnSub = tk.Button(f2, text=" - ", borderwidth=5, width=4, font=ft, command=lambda: Click(" - ")).grid(row=1, column=3)
Btn7 = tk.Button(f2, text="7", borderwidth=5, width=4, font=ft, command=lambda: Click("7")).grid(row=0, column=0)
Btn8 = tk.Button(f2, text="8", borderwidth=5, width=4, font=ft, command=lambda: Click("8")).grid(row=0, column=1)
Btn9 = tk.Button(f2, text="9", borderwidth=5, width=4, font=ft, command=lambda: Click("9")).grid(row=0, column=2)
BtnAdd = tk.Button(f2, text=" + ", borderwidth=5, width=4, font=ft, command=lambda: Click(" + ")).grid(row=0, column=3)

# 使用 pack() 布局 Frame 容器
f1.pack()
f2.pack()

# 進入主事件迴圈，保持 GUI 運行
top.mainloop()
