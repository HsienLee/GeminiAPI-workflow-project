# 📰 AI 新聞自動分析系統

自動抓取「台新新光合併案」相關新聞，透過 **Gemini 2.5 Flash** 進行綜合分析，
產出 HTML 視覺化報告，並由 **GitHub Actions** 每日自動執行與更新。

> 🤖 每天早上 8:00（台灣時間）自動執行，無需人工介入。

## 📊 最新報告

- [查看最新 AI 分析報告](./analysis_report.html)
- [原始分析文件（Markdown）](./analysis_report.md)
- [爬蟲原始資料（CSV）](./news.csv)

## ⚙️ 系統流程

```
Google News RSS ──> 爬蟲 (crawler.py)
                        │
                        ▼
                   news.csv
                        │
                        ▼
              Gemini 2.5 Flash 分析 (analyzer.py)
                        │
                        ▼
              analysis_report.md
                        │
                        ▼
              HTML 報告 (make_html.py)
                        │
                        ▼
        GitHub Actions 自動 commit 回 repo
```

## 🌟 核心功能

- **批量分析**：一次整合多篇新聞餵給 AI，節省 API 額度並實現跨篇章對比
- **自動排程**：GitHub Actions cron 排程，每日定時執行（已處理 UTC 時區轉換）
- **故障韌性**：
  - Gemini API 503 高流量 → 自動重試 3 次（間隔 60 秒）
  - 新聞來源 503 限流 → 自動重試 3 次（間隔 30 秒）
  - 爬蟲無資料 → 優雅中止，保留上次報告，不產出空內容
  - Git 推送衝突 → workflow 內建 `pull --rebase` 自癒
- **金鑰安全**：本機使用 `.env.secret`（已 gitignore），雲端使用 GitHub Secrets，程式碼零金鑰

## 📁 檔案結構

```
.
├── .github/workflows/
│   └── daily_new.yml        # GitHub Actions 每日排程
├── crawler.py               # 爬蟲模組（Google News RSS）
├── analyzer.py              # Gemini AI 分析模組
├── make_html.py             # Markdown 轉 HTML 報告
├── main.py                  # 主程式：串接完整流程
├── news.csv                 # 爬蟲結果（每日更新）
├── analysis_report.md       # AI 分析原始輸出（每日更新）
├── analysis_report.html     # 最終視覺化報告（每日更新）
├── .env.secret.example      # 環境變數範本
├── .gitignore
└── requirements.txt
```

## 🚀 本機執行

### 1. 環境準備

```bash
python3 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 設定金鑰

到 [Google AI Studio](https://aistudio.google.com/) 申請 API Key，
在專案根目錄建立 `.env.secret`：

```text
GEMINI_API_KEY=你的金鑰
```

### 3. 執行

```bash
python main.py
```

完成後用瀏覽器打開 `analysis_report.html` 查看報告。

## ☁️ 雲端自動化設定

1. Fork 或 clone 本專案並推上你的 GitHub repo
2. 到 repo 的 **Settings → Secrets and variables → Actions** 新增 Secret：
   - Name: `GEMINI_API_KEY`
   - Value: 你的金鑰
3. 排程會每日自動觸發，也可到 **Actions** 頁籤手動 **Run workflow** 立即測試

## 🛠️ 技術棧

| 用途 | 套件 |
|---|---|
| AI 分析 | `google-genai`（Gemini 2.5 Flash） |
| 爬蟲 | `requests` + `beautifulsoup4` |
| 資料處理 | `pandas` |
| 報告轉檔 | `markdown` |
| 金鑰管理 | `python-dotenv` |
| 自動化 | GitHub Actions |

## 📝 備註

- 分析內容由 AI 生成，僅供參考，不構成投資建議
- 想更換追蹤主題，修改 `main.py` 中的關鍵字即可