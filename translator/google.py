from deep_translator import GoogleTranslator as DeepTranslatorCore

class GoogleTranslator:
    def __init__(self, config):
        self.language_from = config.get("language_from", "en")
        self.language_to = config.get("language_to", "ja")
        try:
            self.translator = DeepTranslatorCore(source=self.language_from, target=self.language_to)
        except Exception as e:
            print(f"[ERROR] Google翻訳（内部：deep-translator）初期化エラー: {e}")
            self.translator = None

    def translate(self, text):
        if not self.translator:
            return "[翻訳初期化失敗]"

        try:
            return self.translator.translate(text)
        except Exception as e:
            print(f"[ERROR] Google翻訳（内部：deep-translator）エラー: {e}")
            return "[翻訳エラー]"
