import keyboard
import pyperclip
from ocr import capture_and_ocr
from translator import get_translator
from overlay import show_text, show_text_position_editor
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

        # 翻訳エンジンの種類を一瞬表示
        engine = config["translator"]
        if engine == "gpt":
            show_text("🧠 GPT翻訳中...", config, timeout=2)
        elif engine == "google":
            show_text("🌐 Google翻訳中...", config, timeout=2)

        translated = translator.translate(text)
        print(f"[TRANSLATED] 翻訳結果: {translated}")

        # 自動でクリップボードにコピー
        pyperclip.copy(translated)
        print("[INFO] 翻訳結果をクリップボードにコピーしました")

        show_text(translated, config)

    return trigger

def setup_hotkey(config):
    hotkey_screen = config.get("hotkey", "alt+t")
    hotkey_mouse = config.get("mouse_hotkey", "alt+m")

    keyboard.add_hotkey(hotkey_screen, make_trigger(lambda: config["capture_region"], config))
    keyboard.add_hotkey(hotkey_mouse, make_trigger(get_mouse_selection_region, config))

    # Alt+Pで表示位置調整モード
    keyboard.add_hotkey("alt+p", lambda: show_text_position_editor("🛠 表示位置を調整して保存", config))

    print(f"[INFO] ホットキー登録: {hotkey_screen}（全画面）")
    print(f"[INFO] ホットキー登録: {hotkey_mouse}（選択範囲）")
    print("[INFO] ホットキー登録: alt+p（表示位置調整モード）")
    print(f"[INFO] 使用翻訳エンジン: {config['translator']}")
    print("[INFO] ホットキー待機中...")
    keyboard.wait()
