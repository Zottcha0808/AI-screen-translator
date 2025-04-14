import keyboard
from ocr import capture_and_ocr
from translator import get_translator
from overlay import show_text
from mousecap import get_mouse_selection_region

def make_trigger(region_func, config):
    def trigger():
        region = region_func()
        if not region:
            print("[INFO] 範囲選択キャンセル")
            return

        print(f"[INFO] キャプチャ範囲: {region}")
        config["capture_region"] = region

        text = capture_and_ocr(config)
        print(f"[OCR] 認識されたテキスト: {text}")

        translator = get_translator(config["translator"], config)
        translated = translator.translate(text)
        print(f"[TRANSLATED] 翻訳結果: {translated}")

        show_text(translated)

    return trigger

def setup_hotkey(config):
    hotkey_screen = config.get("hotkey", "alt+t")
    hotkey_mouse = config.get("mouse_hotkey", "alt+m")

    # ホットキーに機能をバインド（configベースで翻訳エンジンを自動選択）
    keyboard.add_hotkey(hotkey_screen, make_trigger(lambda: config["capture_region"], config))
    keyboard.add_hotkey(hotkey_mouse, make_trigger(get_mouse_selection_region, config))

    print(f"[INFO] ホットキー登録: {hotkey_screen}（全画面）")
    print(f"[INFO] ホットキー登録: {hotkey_mouse}（選択範囲）")
    print(f"[INFO] 使用翻訳エンジン: {config['translator']}")
    print("[INFO] ホットキー待機中...")
    keyboard.wait()
