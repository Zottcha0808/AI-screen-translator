# 🖥️ AIスクリーン翻訳ツール

ホットキーで画面をキャプチャし、OCR（文字認識）＋翻訳して、ポップアップで結果を表示する軽量ツールです。  
ゲーム・アプリ・動画など、どんな画面にも対応できます。

---

## 🚀 主な機能

- `Alt + T` のホットキーで翻訳を即実行
- TesseractによるOCR（画面内の文字を読み取り）
- 翻訳は GPT / DeepL / Google Translate から選択可能
- 結果をポップアップまたは透過オーバーレイで表示
- ローカル動作・バックグラウンド常駐なし

---

## 🔧 セットアップ方法

1. リポジトリをクローン：

    ```bash
    git clone https://github.com/Zottcha0808/AI-screen-translator.git
    cd AI-screen-translator
    ```

2. 必要なライブラリをインストール：

    ```bash
    pip install -r requirements.txt
    ```

3. 設定ファイルをコピーして編集：

    ```bash
    cp config.yaml.sample config.yaml
    # 自分のAPIキーやホットキー設定を記入
    ```

---

## 🧪 使い方

`Alt + T` を押すと：

1. 画面をキャプチャ  
2. テキストをOCRで抽出  
3. 翻訳APIで日本語に変換  
4. 翻訳結果を画面上に表示

---

## ⚙ 設定ファイル（config.yaml）の例

```yaml
hotkey: "alt+t"
translator: "gpt"  # または "deepl", "google"
openai_api_key: "sk-xxxx..."
language_from: "en"
language_to: "ja"
capture_region:
  x: 0
  y: 0
  width: 1920
  height: 1080
```
---


📝 ライセンス
MITライセンスです。
自由に使って改造してOK！

---

👤 作者
Zottcha0808（じむ）
GitHub: @Zottcha0808