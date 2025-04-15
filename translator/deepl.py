import deepl
import re

class DeepLTranslator:
    def __init__(self, config):
        self.api_key = config["deepl_api_key"]  # DeepLのAPIキーを使用
        self.client = deepl.Translator(self.api_key)  # DeepL APIクライアント
        self.language_from = config.get("language_from", "EN")  # 翻訳元の言語
        self.language_to = config.get("language_to", "JA")  # 翻訳先の言語

    def translate(self, text):
        try:
            # DeepL APIに翻訳をリクエスト
            result = self.client.translate_text(
                text, 
                source_lang=self.language_from, 
                target_lang=self.language_to
            )
            
            # DeepLの翻訳結果を取得
            translated_raw = result.text
            translated_clean = self.extract_japanese(translated_raw)
            
            return translated_clean or translated_raw

        except Exception as e:
            print(f"[ERROR] DeepL翻訳エラー: {e}")
            return "[翻訳エラー]"

    @staticmethod
    def extract_japanese(text):
        """
        DeepLの返答から日本語らしい行だけを抽出（全角文字が含まれる行を返す）
        """
        lines = text.splitlines()
        jp_lines = [line.strip() for line in lines if re.search(r"[ぁ-んァ-ン一-龥]", line)]
        return "\n".join(jp_lines).strip()