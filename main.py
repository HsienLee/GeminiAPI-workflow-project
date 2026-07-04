from crawler import crawl_google_news
from analyzer import analyze
from make_html import md_to_html
import pandas as pd

if __name__ == "__main__":
    news = crawl_google_news("台新 新光 合併")
    pd.DataFrame(news).to_csv("news.csv", index=False, encoding="utf-8-sig")
    analyze()
    md_to_html()
    print('全流程完成～～～')
