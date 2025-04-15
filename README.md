# 🖥️ AIスクリーン翻訳ツール

ホットキーで画面をキャプチャし、OCR（文字認識）＋翻訳して、ポップアップで結果を表示する軽量ツールです。  
ゲーム・アプリ・動画など、どんな画面にも対応できます。

---

## 🚀 主な機能

- `Alt + T` のホットキーで翻訳を即実行
- TesseractによるOCR（画面内の文字を読み取り）
- 翻訳は GPT / DeepL / Google Translate（モジュール追加予定）から選択可能
- 結果をポップアップで表示（移動・スクロール・最小化も可）
- ローカル動作、常駐プロセスなし

---

## 🔧 セットアップ方法

1. リポジトリをクローン：

    ```bash
    git clone https://github.com/Zottcha0808/AI-screen-translator.git
    cd AI-screen-translator
    ```

2. 必要なPythonパッケージをインストール：

    ```bash
    pip install -r requirements.txt
    ```

3. Tesseract OCRをインストール（Windows）：

    - ダウンロード：https://github.com/tesseract-ocr/tesseract
    - インストール後、`ocr.py` の先頭で以下のようにパスを指定：

    ```python
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    ```

4. 設定ファイルをコピーして編集：

    ```bash
    cp config.yaml.sample config.yaml
    ```

    - `config.yaml` に自身の APIキーやホットキーを記載
    - Gitには **絶対に `config.yaml` をコミットしないでください！**
      `.gitignore` に以下の行を追加済みです：

    ```gitignore
    config.yaml
    ```

---

## 🧪 使い方

VSCodeなどで `main.py` を実行した状態で、  
画面内に英語が表示されている状態で `Alt + T` を押すと：

1. アクティブウィンドウをキャプチャ  
2. テキストをOCRで抽出（英語のみ抽出も可）  
3. GPT翻訳APIで日本語に変換  
4. 翻訳結果をポップアップで表示

画面内に英語が表示されている状態で Alt + Y を押すと：

1. 画面全体がうす暗くなり、マウスで任意の範囲をドラッグして選択
2. 選択した範囲をキャプチャ
3. テキストをOCRで抽出（英語のみ抽出も可）
4. GPT翻訳APIで日本語に変換
5. 翻訳結果をポップアップで表示
---

## 🧠 利用可能な翻訳エンジン

| エンジン | 特徴 | 精度 | 応答速度 | 利用コスト |
|----------|------|------|------------|-------------|
| `gpt`（OpenAI GPT-4o） | 高精度な自然翻訳・意訳が得意 | ◎ | ○ | 有料API（高精度・中速） |
| `google`（非公式Google Translate） | 簡単・無料・爆速 | ○ | ◎ | 無料（非公式のため安定性△） |
| `deepl`（公式API対応） | 文脈理解と自然な日本語訳に強い | ◎ | ○ | 有料API（無料枠あり・中速） |

### 🔧 各エンジンの特徴

- **`gpt`**：意訳や文体の調整が必要な場面で強力（例：ゲーム翻訳、長文解釈など）。やや遅めだが高精度。
- **`google`**：速報性と軽量さ重視。短文やUI翻訳など、軽めの用途に最適。
- **`deepl`**：文脈理解に優れ、自然で読みやすい日本語を生成。技術文書やビジネス文書翻訳におすすめ。

### 🔁 切り替え方法

`config.yaml` 内の以下の行を変更してください：

```yaml
translator: "gpt"    # または "google"
## ⚙ 設定ファイル（config.yaml）の例
```
---

```yaml
hotkey: "alt+t"
mouse_hotkey: "alt+y"
translator: "gpt"
gpt_model: "gpt-4o"  # または "gpt-3.5-turbo", "gpt-4"
openai_api_key: "sk-~~~"
language_from: "en"
language_to: "ja"
capture_region:
  x: 0
  y: 0
  width: 1920
  height: 1080
```

# OCRの対象画面範囲
capture_region:
  x: 0
  y: 0
  width: 1920
  height: 1080

# OCR設定
ocr_language: "eng+jpn"
extract_english_only: true


# セキュリティについて
config.yaml は .gitignore で保護されており、APIキーが誤って公開されるのを防ぎます。

GitHubに公開する際は、必ず APIキーが含まれないように注意してください。

# ライセンス
MITライセンスです。
自由に使って改造してOK！

# 作者
Zottcha0808（じむ）
GitHub: @Zottcha0808