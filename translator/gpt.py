import openai
import re

class GPTTranslator:
    def __init__(self, config):
        self.api_key = config["openai_api_key"]
        self.client = openai.OpenAI(api_key=self.api_key)
        self.language_from = config.get("language_from", "en")
        self.language_to = config.get("language_to", "ja")
        self.model = config.get("gpt_model", "gpt-4")  # ← GPT-4oなどもここで切り替え可

    def translate(self, text):
        prompt = (
            f"Translate the following {self.language_from} text into natural, fluent {self.language_to}.\n"
            f"Text:\n{text}"
        )

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional translator. Return only the translated text."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3
            )

            translated_raw = response.choices[0].message.content.strip()
            translated_clean = self.extract_japanese(translated_raw)

            return translated_clean or translated_raw

        except Exception as e:
            print(f"[ERROR] GPT翻訳エラー: {e}")
            return "[翻訳エラー]"

    @staticmethod
    def extract_japanese(text):
        """
        GPTの返答から日本語らしい行だけを抽出（全角文字が含まれる行を返す）
        """
        lines = text.splitlines()
        jp_lines = [line.strip() for line in lines if re.search(r"[ぁ-んァ-ン一-龥]", line)]
        return "\n".join(jp_lines).strip()
