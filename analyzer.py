import os
import pandas as pd
from google import genai
from dotenv import load_dotenv

# # 1. 讀取金鑰
# load_dotenv(".env.secret")
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# # 2. 讀第一課存的 CSV
# df = pd.read_csv("news.csv", encoding="utf-8-sig")

# # 3. 把多則新聞合併成一段文字
# merged = "\n\n".join(
#     f"【{row['日期']}】{row['標題']}"
#     for _, row in df.iterrows()
# )
# print(merged)
# # 4. 設計 prompt
# prompt = f"""你是一位幽默的財經 YouTuber，請用專業、中立的口吻分析。

# 以下是抓取到的新聞列表：

# {merged}

# 請針對以上所有內容進行綜合評估：
# 1. [事件總結]：用 200 字以內總結核心事件。
# 2. [最新進度]：提取出最新的發展動態。
# 3. [風險與機會]：給出整體的觀察重點。
# 4. [名詞解釋]：解釋新聞中出現的專業術語

# 請直接輸出分析，不要回應我或加開場白。"""

# # 5. 呼叫 Gemini
# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents=prompt,
# )

# # 6. 存成 Markdown
# with open("analysis_report.md", "w", encoding="utf-8") as f:
#     f.write("# 新聞分析報告\n\n")
#     f.write(f"分析時間：{pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\n\n")
#     f.write(response.text)

# print(response.text)
# print("\n✅ 已存檔 analysis_report.md")

def analyze(df_file = "news.csv", md_file = "analysis_report.md"):
    # 1. 讀取金鑰
    load_dotenv(".env.secret")
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    # 2. 讀第一課存的 CSV
    df = pd.read_csv(df_file, encoding="utf-8-sig")

    # 3. 把多則新聞合併成一段文字
    merged = "\n\n".join(
    f"【{row['日期']}】{row['標題']}"
    for _, row in df.iterrows()
    )
    # print(merged)
    # 4. 設計 prompt
    prompt = f"""你是一位資深的金融情報官，請用專業、中立的口吻分析。

    以下是抓取到的新聞列表：

    {merged}

    請針對以上所有內容進行綜合評估：
    1. [事件總結]：用 200 字以內總結核心事件。
    2. [最新進度]：提取出最新的發展動態。
    3. [風險與機會]：給出整體的觀察重點。
    4. [名詞解釋]：解釋新聞中出現的專業術語

    請直接輸出分析，不要回應我或加開場白。"""

    # 5. 呼叫 Gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    # 6. 存成 Markdown
    with open(md_file, "w", encoding="utf-8") as f:
        f.write("# 新聞分析報告\n\n")
        f.write(f"分析時間：{pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(response.text)

    return(response.text)
    print("\n✅ 已存檔 {md_file}")

if __name__ == "__main__":
    analyze()
