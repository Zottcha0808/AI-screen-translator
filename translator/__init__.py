def get_translator(name, config):
    if name == "gpt":
        from .gpt import GPTTranslator
        return GPTTranslator(config)
    elif name == "deepl":
        from .deepl import DeepLTranslator
        return DeepLTranslator(config)
    elif name == "google":
        from .google import GoogleTranslator
        return GoogleTranslator(config)
    else:
        raise ValueError(f"未対応の翻訳エンジンです: {name}")
