import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def crawl_google_news(keyword):
    # 1. 組出 RSS 網址
    url = f"https://news.google.com/rss/search?q={keyword}&hl=zh-TW&gl=TW&ceid=TW:zh-Hant"
    headers = {"User-Agent": "Mozilla/5.0"}

    # 2. 發出請求。User-Agent 是告訴網站「我是瀏覽器」
    
    # headers = {"User-Agent": "Mozilla/5.0"}
    # res = requests.get(url, headers=headers)
    # print(f"狀態碼: {res.status_code}")   # 200 代表成功

    for attempt in range(3):
        res = requests.get(url, headers=headers)
        print(f"狀態碼: {res.status_code}")
        if res.status_code == 200:
            break
        print(f"⚠️ 第 {attempt+1} 次失敗，30 秒後重試...")
        time.sleep(30)
    else:                    # for 迴圈跑完都沒 break 才會進來
        return []            # 三次都失敗，回傳空列表

    # 3. 解析 XML
    soup = BeautifulSoup(res.content, "xml")
    items = soup.find_all("item")         # 每則新聞是一個 <item>

    # 4. 把每則新聞整理成 dict
    news_list = []
    for item in items[:10]:
        news_list.append({
            "標題": item.title.text,
            "連結": item.link.text,
            "日期": item.pubDate.text,
            "來源": item.source.text,
        })
    return news_list

if __name__ == "__main__":
    news = crawl_google_news("台新 新光 合併")
    df = pd.DataFrame(news)
    print(df[["標題", "日期"]])           # 先印出來確認
    df.to_csv("news.csv", index=False, encoding="utf-8-sig")
    print(f"\n已存檔，共 {len(df)} 筆")