from googletrans import Translator as GoogleTranslatorCore

class GoogleTranslator:
    def __init__(self, config):
        self.translator = GoogleTranslatorCore()
        self.language_from = config.get("language_from", "en")
        self.language_to = config.get("language_to", "ja")

    def translate(self, text):
        try:
            result = self.translator.translate(text, src=self.language_from, dest=self.language_to)
            return result.text
        except Exception as e:
            print(f"[ERROR] Google翻訳エラー: {e}")
            return "[翻訳エラー]"