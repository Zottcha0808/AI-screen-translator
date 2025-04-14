def capture_and_ocr(config):
    region = config.get("capture_region", {})
    lang = config.get("ocr_language", "eng")
    extract_english = config.get("extract_english_only", True)

    x = region.get("x", 0)
    y = region.get("y", 0)
    width = region.get("width", 1920)
    height = region.get("height", 1080)

    if width == 0 or height == 0:
        print("[ERROR] キャプチャ範囲が無効（幅または高さが0）")
        return "[キャプチャエラー]"

    with mss.mss() as sct:
        monitor = {"left": x, "top": y, "width": width, "height": height}
        screenshot = sct.grab(monitor)
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

        raw_text = pytesseract.image_to_string(img, lang=lang)
        print(f"[OCR DEBUG] raw:\n{raw_text}\n{'-'*40}")

        if extract_english:
            filtered_text = extract_english_lines(raw_text)
            print(f"[OCR DEBUG] 英語抽出後:\n{filtered_text}\n{'-'*40}")
            return filtered_text.strip()
        else:
            return raw_text.strip()
