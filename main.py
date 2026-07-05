from crawler import crawl_google_news
from analyzer import analyze
from make_html import md_to_html
import pandas as pd

if __name__ == "__main__":
    news = crawl_google_news("台新 新光 合併")
    
    if not news:
        print("❌ 爬蟲沒有取得任何資料，跳過本次分析（保留上次的報告）")
        raise SystemExit(1)      # 帶錯誤碼結束，Actions 會顯示紅色通知你
    
    pd.DataFrame(news).to_csv("news.csv", index=False, encoding="utf-8-sig")
    analyze()
    md_to_html()
    print('全流程完成～～～')
