package com.example.test;
import android.os.Bundle;
import android.util.TypedValue;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

/**
 * MainActivity: 應用程式的主畫面活動，負責顯示並控制文字的放大與縮小。
 */
public class MainActivity extends AppCompatActivity {

    // 宣告 TextView 和 Button 物件
    TextView showtext;     // 用於顯示文字的 TextView
    Button backbutton;     // 返回按鈕，用於將文字縮小
    Button demobutton;     // 演示按鈕，用於將文字放大
    int size;              // 用於存儲當前 TextView 的文字大小

    /**
     * 當活動創建時調用此方法。負責初始化畫面。
     * @param savedInstanceState 保存當前狀態的 Bundle 對象
     */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);  // 設定活動所使用的 XML 佈局檔案

        // 初始化畫面上的元件，將 XML 佈局檔案中的元件綁定到變數
        showtext = (TextView) findViewById(R.id.showtext);   // 綁定 TextView，顯示動態文字
        demobutton = (Button) findViewById(R.id.demobutton); // 綁定 Button，點擊後放大文字
        backbutton = (Button) findViewById(R.id.backbutton); // 綁定 Button，點擊後縮小文字

        /**
         * 設定 demobutton 的點擊事件監聽器。
         * 當按下按鈕時，將 TextView 的文字放大並更新顯示文字為 "Pass!"。
         */
        demobutton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                size = (int) showtext.getTextSize();  // 獲取當前 TextView 的文字大小（以像素為單位）
                size += 2;                            // 文字大小增加 2 像素
                showtext.setTextSize(TypedValue.COMPLEX_UNIT_PX, size); // 將新的大小應用到 TextView
                showtext.setText("Pass!");            // 更新 TextView 文字為 "Pass!"
            }
        });

        /**
         * 設定 backbutton 的點擊事件監聽器。
         * 當按下按鈕時，將 TextView 的文字縮小並恢復顯示為 "Android Lab1 demo"。
         */
        backbutton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                size = (int) showtext.getTextSize();  // 獲取當前 TextView 的文字大小
                if (size > 10) {                      // 檢查文字大小是否大於 10（避免過小）
                    size -= 2;                        // 文字大小減少 2 像素
                }
                showtext.setTextSize(TypedValue.COMPLEX_UNIT_PX, size); // 將縮小的大小應用到 TextView
                showtext.setText("Android Lab1 demo");  // 恢復 TextView 文字為 "Android Lab1 demo"
            }
        });
    }
}
