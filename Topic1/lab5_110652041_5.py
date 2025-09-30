import tkinter as tk  # 匯入 Tkinter 作為 tk
from tkinter import messagebox  # 從 Tkinter 匯入 messagebox 顯示提示訊息
import pickle as pk  # 匯入 pickle 模組，用於資料序列化和反序列化
from PIL import Image, ImageTk  # 匯入 PIL 用於處理圖片

# 建立主視窗並命名
window = tk.Tk()
window.title('Lab5: Welcome to Login')  # 設定視窗的標題

# 建立兩個框架 f1 和 f2，用於組織視窗中的元素
f1 = tk.Frame(window)  # 用來放圖片的框架
f2 = tk.Frame(window)  # 用來放登入表單的框架

# 讀取並調整圖片大小
image1 = ImageTk.PhotoImage(Image.open('C:/Users/hjeter/Desktop/p.jpg').resize((400, 200)))
im = tk.Label(f1, image=image1)  # 將圖片放入標籤中，顯示在 f1 框架內

# 初始化 Tkinter 的字串變數，用於存放使用者輸入的帳號和密碼
var1 = tk.StringVar()  # 用於帳號的變數
var2 = tk.StringVar()  # 用於密碼的變數
var3 = tk.StringVar()  # 用於註冊帳號的變數
var4 = tk.StringVar()  # 用於註冊密碼的變數
var5 = tk.StringVar()  # 用於確認密碼的變數

# 建立登入界面的輸入欄位與標籤
entry1 = tk.Entry(f2, textvariable=var1)  # 帳號輸入欄位
entry2 = tk.Entry(f2, textvariable=var2, show='*')  # 密碼輸入欄位，'*' 用於隱藏輸入內容
Label1 = tk.Label(f2, text="User:").grid(row=0, column=0)  # 帳號標籤
Label2 = tk.Label(f2, text="Password:").grid(row=1, column=0)  # 密碼標籤

# 定義登入按鈕的功能
def login():
    entry_usr = entry1.get()  # 獲取輸入的帳號
    entry_pwd = entry2.get()  # 獲取輸入的密碼

    try:
        # 嘗試讀取 user_info.pickle 檔案以獲取現有的帳號資料
        try:
            with open('user_info.pickle', 'rb') as f:
                user_info = pk.load(f)  # 載入已存儲的帳號資料
        except EOFError:
            user_info = {}  # 若檔案為空，則初始化為空字典
    except FileNotFoundError:
        user_info = {}  # 若檔案不存在，則初始化為空字典

    # 驗證帳號密碼
    if entry_usr in user_info:
        if entry_pwd == user_info[entry_usr]:
            messagebox.showinfo(message="Successful")  # 若帳號和密碼匹配，顯示成功訊息
        else:
            messagebox.showerror(message="Password incorrect")  # 若密碼錯誤，顯示錯誤訊息
    else:
        # 若帳號不存在，詢問是否要建立新帳號
        sign_up = messagebox.askyesno(message="Do you want to create an account by your input?")
        if sign_up:
            with open('user_info.pickle', 'wb') as f:
                user_info[entry_usr] = entry_pwd  # 新增帳號和密碼
                pk.dump(user_info, f)  # 將更新後的資料儲存回檔案

# 設置登入和註冊按鈕
Btnlog = tk.Button(f2, text="Log In", borderwidth=3, width=4, height=1, command=lambda: login()).grid(row=2, column=0)
Btnsign = tk.Button(f2, text="Sign Up", borderwidth=3, width=10, height=1, command=lambda: signup1()).grid(row=2, column=1)

# 定義註冊功能
def signup1():
    # 開啟新視窗，用於註冊帳號
    window2 = tk.Toplevel()
    window2.geometry('700x400')  # 設定彈出視窗的大小
    f3 = tk.Frame(window2)  # 註冊視窗的框架

    # 註冊視窗的標籤與輸入欄位
    Label3 = tk.Label(f3, text="User Name:").grid(row=0, column=0)
    Label4 = tk.Label(f3, text="Password:").grid(row=1, column=0)
    Label5 = tk.Label(f3, text="Confirm Password:").grid(row=2, column=0)
    Btnsign2 = tk.Button(f3, text="Sign Up", borderwidth=5, width=10, height=1, command=lambda: signup2()).grid(row=3, column=0)
    
    entry3 = tk.Entry(f3, textvariable=var3)  # 註冊帳號輸入欄位
    entry4 = tk.Entry(f3, textvariable=var4, show='*')  # 註冊密碼輸入欄位
    entry5 = tk.Entry(f3, textvariable=var5, show='*')  # 確認密碼輸入欄位
    entry3.grid(row=0, column=1)
    entry4.grid(row=1, column=1)
    entry5.grid(row=2, column=1)
    f3.pack()

    # 註冊的確認功能
    def signup2():
        sign_usr = entry3.get()  # 取得註冊的帳號
        sign_pwd = entry4.get()  # 取得註冊的密碼
        sign_pwd_again = entry5.get()  # 取得確認密碼

        try:
            # 嘗試讀取現有的帳號資料
            try:
                with open('user_info.pickle', 'rb') as f:
                    user_info = pk.load(f)
            except EOFError:
                user_info = {}  # 若檔案為空，則初始化為空字典
        except FileNotFoundError:
            user_info = {}  # 若檔案不存在，則初始化為空字典

        # 驗證是否可以註冊
        if sign_usr in user_info:
            messagebox.showerror(message="User name exists!")  # 若帳號已存在，顯示錯誤訊息
        else:
            if sign_pwd == sign_pwd_again:
                with open('user_info.pickle', 'wb') as f:
                    user_info[sign_usr] = sign_pwd  # 將新帳號和密碼寫入字典
                    pk.dump(user_info, f)  # 儲存至檔案
                messagebox.showinfo(message="Successful!")  # 註冊成功訊息
                window2.destroy()  # 關閉註冊視窗
            else:
                messagebox.showerror(message="Password incorrect!")  # 若密碼不一致，顯示錯誤訊息

# 顯示圖片與框架，並啟動主視窗
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
im.pack()  # 顯示圖片
f1.pack()  # 顯示框架 f1
f2.pack()  # 顯示框架 f2
window.mainloop()  # 啟動 Tkinter 主迴圈，讓視窗保持打開
