# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__, template_folder = 'templates')

@app.route('/')
def index():
    # 此處會用到的 function
    #   1. render_template('index.html', ID = ....)
    ''' start of you code '''
    ID = 
    
    ''' end of you code '''

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 9808, debug = False)
    # host 填寫 Rpi 的 IP 位址
    # 以 ifconfig 指令查詢 Rpi IP 位址