from hotkey import setup_hotkey
import yaml

def load_config():
    with open("config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    print("[INFO] 設定ファイル読み込み完了")
    setup_hotkey(config)
    print("[INFO] ホットキー待機中...")

if __name__ == "__main__":
    main()
