package com.example.app110652041;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

/**
 * MainActivity: 主活動負責顯示文字訊息，並根據使用者輸入的名字更新歡迎訊息。
 */
public class MainActivity extends AppCompatActivity {

    // 宣告 TextView、Button 和 EditText 物件
    TextView showtest;  // 顯示歡迎訊息的 TextView
    Button set;         // 用於設置歡迎訊息的按鈕
    Button reset;       // 用於重置訊息為預設值的按鈕
    EditText name;      // 用於輸入使用者名稱的 EditText

    /**
     * 當活動創建時調用此方法。負責初始化畫面。
     * @param savedInstanceState 保存當前狀態的 Bundle 對象
     */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);  // 設定活動所使用的 XML 佈局檔案

        // 初始化畫面上的元件，將 XML 佈局檔案中的元件綁定到變數
        showtest = (TextView) findViewById(R.id.showtext);   // 綁定 TextView，顯示歡迎訊息
        set = (Button) findViewById(R.id.set);               // 綁定 Button，點擊後設置新訊息
        reset = (Button) findViewById(R.id.reset);           // 綁定 Button，點擊後重置訊息
        name = (EditText) findViewById(R.id.name);           // 綁定 EditText，用戶輸入名稱的地方

        /**
         * 設定 set 按鈕的點擊事件監聽器。
         * 當按下按鈕時，從 EditText 中取得使用者的名字，並將 TextView 的文字更新為 "Welcome to Android, [名字]"。
         */
        set.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // 獲取使用者在 EditText 中輸入的名稱並更新顯示文字
                showtest.setText("Welcome to Android, " + name.getText().toString());
            }
        });

        /**
         * 設定 reset 按鈕的點擊事件監聽器。
         * 當按下按鈕時，將 TextView 的文字重置為預設的 "Hello world!"。
         */
        reset.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // 重置 TextView 的顯示文字
                showtest.setText("Hello world!");
            }
        });
    }
}
