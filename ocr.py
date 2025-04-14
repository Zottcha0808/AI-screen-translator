import mss
import pytesseract
from PIL import Image
import re

# Tesseractの実行パスを明示（Windows用）
pytesseract.pytesseract.tesseract_cmd = r"F:\\01_Software\\tesseract\\tesseract.exe"

def extract_english_lines(text, threshold=0.6):
    """各行のアルファベット比率を見て、英語っぽい行だけ残す"""
    lines = text.splitlines()
    english_lines = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        alphabet_count = len(re.findall(r"[A-Za-z]", line))
        ratio = alphabet_count / len(line)
        if ratio > threshold:
            english_lines.append(line)

    return "\n".join(english_lines)

def capture_and_ocr(config):
    region = config.get("capture_region", {})
    lang = config.get("ocr_language", "eng")
    extract_english = config.get("extract_english_only", True)

    x = region.get("x", 0)
    y = region.get("y", 0)
    width = region.get("width", 1920)
    height = region.get("height", 1080)

    with mss.mss() as sct:
        monitor = {"left": x, "top": y, "width": width, "height": height}
        screenshot = sct.grab(monitor)
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

        # OCR実行
        raw_text = pytesseract.image_to_string(img, lang=lang)
        print(f"[OCR DEBUG] raw:\n{raw_text}\n{'-'*40}")

        # 英語抽出（必要なら）
        if extract_english:
            filtered_text = extract_english_lines(raw_text)
            print(f"[OCR DEBUG] 英語抽出後:\n{filtered_text}\n{'-'*40}")
            return filtered_text.strip()
        else:
            return raw_text.strip()