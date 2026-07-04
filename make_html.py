import markdown

def md_to_html(md_file="analysis_report.md", html_file="analysis_report.html"):
    # 1. 讀入 Markdown 原文
    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()

    # 2. 一行完成轉換：Markdown → HTML 片段
    body = markdown.markdown(md_text)

    # 3. 包上完整的 HTML 骨架 + CSS 樣式
    html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>新聞分析報告</title>
<style>
  body {{
    font-family: "Noto Sans TC", "Microsoft JhengHei", sans-serif;
    max-width: 800px;
    margin: 40px auto;
    padding: 0 20px;
    line-height: 1.8;
    background: #fffff0;      /* 象牙白背景，原專案叫 ivory 就是這個 */
    color: #333;
  }}
  h1 {{ border-bottom: 3px solid #2c5f8a; padding-bottom: 10px; }}
  h2 {{ color: #2c5f8a; margin-top: 32px; }}
  strong {{ color: #b03030; }}
</style>
</head>
<body>
{body}
</body>
</html>"""

    # 4. 寫檔
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ 已產出 {html_file}")

if __name__ == "__main__":
    md_to_html()