import tkinter as tk
import threading

def show_text(text):
    def run():
        root = tk.Tk()
        root.title("翻訳結果")
        root.attributes("-topmost", True)
        root.geometry("700x400+100+100")  # 初期位置は左上気味にした（調整OK）

        # ウィンドウを動かせるように（overrideredirectは使わない）
        root.resizable(True, True)  # サイズ変更もOK

        # スクロール対応のキャンバス＋フレーム
        frame = tk.Frame(root)
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        canvas = tk.Canvas(frame, bg="black", highlightthickness=0)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="black")

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # テキストラベル（長文でも自動調整）
        label = tk.Label(
            scroll_frame,
            text=text,
            font=("Meiryo", 14),
            bg="black",
            fg="white",
            wraplength=640,
            justify="left"
        )
        label.pack(anchor="w", pady=5)

        # 閉じるボタン（下部）
        close_button = tk.Button(root, text="閉じる", command=root.destroy, font=("Meiryo", 12))
        close_button.pack(pady=(0, 10))

        root.mainloop()

    threading.Thread(target=run, daemon=True).start()
