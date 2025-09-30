import tkinter as tk  # 引入 Tkinter 庫來建立 GUI
import tkinter.messagebox as mb  # 引入訊息框庫，用於顯示贏家訊息
import random  # 引入隨機庫，用於電腦隨機下子

# 初始化全域變數
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # 建立 3x3 棋盤，0 表示空格
buttons = [[None, None, None], [None, None, None], [None, None, None]]  # 存放每個按鈕的引用
current_player = 1  # 玩家為 1，電腦為 2
player_choice = "X"  # 預設玩家符號
computer_choice = "O"  # 預設電腦符號
winning_combination = []  # 存放贏家連線組合

# 建立井字棋板
def create_board():
    for i in range(3):
        for j in range(3):
            button = tk.Button(window, text="", font=("Arial", 20), height=2, width=5,  # 調整字體和按鈕大小
                               command=lambda row=i, col=j: handle_click(row, col))
            button.grid(row=i, column=j, sticky="nsew")
            buttons[i][j] = button

# 檢查是否有贏家
def check_winner():
    global winning_combination
    for i in range(3):
        # 檢查行
        if board[i][0] == board[i][1] == board[i][2] != 0:
            winning_combination = [(i, 0), (i, 1), (i, 2)]
            return board[i][0]
        # 檢查列
        if board[0][i] == board[1][i] == board[2][i] != 0:
            winning_combination = [(0, i), (1, i), (2, i)]
            return board[0][i]
    # 檢查對角線
    if board[0][0] == board[1][1] == board[2][2] != 0:
        winning_combination = [(0, 0), (1, 1), (2, 2)]
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        winning_combination = [(0, 2), (1, 1), (2, 0)]
        return board[0][2]
    return None

# 標記贏家顏色
def mark_winner(winner):
    winning_symbol = player_choice if winner == 1 else computer_choice  # 確定贏家符號
    color = "green" if winning_symbol == "O" else "red"  # 設置贏家顏色
    for (r, c) in winning_combination:
        buttons[r][c].config(bg=color)
    play_again(f"Player {winning_symbol} wins! Do you want to restart the game?")  # 提示重啟遊戲

# 點擊事件處理
def handle_click(row, col):
    global current_player
    if board[row][col] == 0:  # 檢查該格是否已被佔用
        board[row][col] = current_player
        buttons[row][col]["text"] = player_choice if current_player == 1 else computer_choice
        winner = check_winner()
        if winner:
            mark_winner(winner)
        elif not any(0 in sublist for sublist in board):  # 檢查是否平局
            for i in range(3):
                for j in range(3):
                    buttons[i][j].config(bg="yellow")  # 平局顏色
            play_again("It's a tie! Do you want to restart the game?")
        else:
            computer_move()  # 切換至電腦操作

# 處理電腦移動
def computer_move():
    global current_player
    move_made = False  # 移動成功的旗標

    # 嘗試能贏的移動
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 2  # 電腦預設嘗試
                if check_winner() == 2:
                    buttons[i][j]["text"] = computer_choice
                    mark_winner(2)
                    return
                board[i][j] = 0

    # 嘗試阻止玩家獲勝
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 1  # 假設玩家要獲勝
                if check_winner() == 1:
                    board[i][j] = 2
                    buttons[i][j]["text"] = computer_choice
                    move_made = True
                    break
                board[i][j] = 0
        if move_made:
            break

    # 隨機移動
    if not move_made:
        while True:
            i = random.randint(0, 2)
            j = random.randint(0, 2)
            if board[i][j] == 0:
                board[i][j] = 2
                buttons[i][j]["text"] = computer_choice
                break

# 重啟遊戲
def play_again(message):
    if mb.askyesno("Game Over", message):
        reset_game()
    else:
        window.destroy()

# 重置遊戲
def reset_game():
    global board, current_player, winning_combination
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", bg="white")
    current_player = 1  # 重置為玩家起始
    winning_combination = []

# 設置玩家符號選擇
def set_choice(choice):
    global player_choice, computer_choice
    player_choice = choice
    computer_choice = "O" if choice == "X" else "X"
    choice_label.config(text=f"You are {player_choice}, computer is {computer_choice}")
    o_button.config(state=tk.DISABLED)
    x_button.config(state=tk.DISABLED)
    create_board()

# 初始化主視窗
window = tk.Tk()
window.title("OOXX")  # 視窗標題
window.geometry("300x400")  # 調整視窗大小以適應較小格子

# 初始訊息
choice_label = tk.Label(window, text=f"You are {player_choice}, computer is {computer_choice}", font=("Arial", 16))
choice_label.grid(row=0, column=0, columnspan=3)

# 符號選擇按鈕
o_button = tk.Button(window, text="Choose O", font=("Arial", 16), command=lambda: set_choice("O"))
o_button.grid(row=1, column=0, columnspan=3, sticky="nsew")

x_button = tk.Button(window, text="Choose X", font=("Arial", 16), command=lambda: set_choice("X"))
x_button.grid(row=2, column=0, columnspan=3, sticky="nsew")

window.mainloop()
