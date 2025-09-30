import tkinter as tk
from tkinter import messagebox

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title('Lab3 tak-tak-tok')  # 設定視窗標題
        self.game_active = True  # 確認遊戲是否進行中
        self.current_player = "X"  # 設定初始玩家為 "X"
        self.board = [""] * 9  # 初始化遊戲板，包含 9 個空字串
        # 建立 9 個按鈕作為遊戲板上的每一格
        self.buttons = [tk.Button(root, font='Arial 20', width=5, height=2, 
                                  command=lambda i=i: self.on_button_click(i)) for i in range(9)]
        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)  # 設定每個按鈕的行與列
            button.grid(row=row, column=col)  # 將按鈕放置在適當位置

    # 遊戲進行
    def on_button_click(self, i):
        if self.game_active and not self.board[i]:  # 確認遊戲進行中且該格未被佔用
            self.board[i] = self.current_player  # 設定當前玩家的標記
            self.buttons[i].config(text=self.current_player, state="disabled")  # 更新按鈕顯示並禁用
            winner = self.check_winner()  # 檢查是否有玩家勝利
            if winner:
                self.highlight_winner(winner)  # 顯示勝利的三格
                self.game_over(f"player {self.current_player} win! Restart the game?")  # 顯示勝利訊息並詢問是否重啟遊戲
            elif not any(s == "" for s in self.board):  # 若棋盤已滿，則為平手
                self.highlight_draw()  # 顯示平手
                self.game_over("It's a tie! Restart the game?")  # 顯示平手訊息並詢問是否重啟遊戲
            else:
                self.current_player = "O" if self.current_player == "X" else "X"  # 切換玩家

    # 檢查是否達成勝利條件
    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                          (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                          (0, 4, 8), (2, 4, 6)]  # 所有可能的勝利組合
        for condition in win_conditions:
            a, b, c = condition
            if self.board[a] == self.board[b] == self.board[c] != "":
                return condition  # 若達成勝利條件，回傳勝利組合
        return None

    # 遊戲結束處理
    def game_over(self, message):
        self.game_active = False  # 停止遊戲
        # 顯示訊息並詢問是否重啟遊戲
        if messagebox.askyesno("game over", message):
            self.restart_game()  # 重啟遊戲
        else:
            self.root.quit()  # 結束遊戲並關閉視窗
    
    # 重啟遊戲
    def restart_game(self):
        self.board = [""] * 9  # 重置棋盤
        self.current_player = "X"  # 重置當前玩家為 "X"
        self.game_active = True  # 重置遊戲狀態為進行中
        # 重置按鈕文字與顏色
        for button in self.buttons:
            button.config(text="", state="normal", bg="SystemButtonFace")
    
    # 顯示勝利的三格
    def highlight_winner(self, win_condition):
        for i in win_condition:
            self.buttons[i].config(bg='light blue')
    
    # 當平手時，所有格子變成紅色
    def highlight_draw(self):
        for button in self.buttons:
            button.config(bg='red')

# 主程式執行區域
root = tk.Tk()
game = TicTacToeGame(root)
root.mainloop()
