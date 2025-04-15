import tkinter as tk
import threading
import yaml

active_root = None  # 現在表示中のウィンドウを保持

def show_text(text, config, timeout=None):
    def run():
        global active_root

        # 古いウィンドウがあれば破棄
        try:
            if active_root and active_root.winfo_exists():
                active_root.after(0, active_root.destroy)
        except Exception as e:
            print(f"[WARN] 既存ウィンドウ破棄中に例外: {e}")
        active_root = None

        root = tk.Tk()
        active_root = root
        root.title("翻訳結果")
        root.attributes("-topmost", True)

        # 表示位置取得
        x = config.get("overlay_position", {}).get("x", 100)
        y = config.get("overlay_position", {}).get("y", 100)
        root.geometry(f"700x400+{x}+{y}")
        root.resizable(True, True)

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

        if timeout:
            root.after(timeout * 1000, lambda: root.destroy())
        else:
            close_button = tk.Button(root, text="閉じる", command=root.destroy, font=("Meiryo", 12))
            close_button.pack(pady=(0, 10))

        root.protocol("WM_DELETE_WINDOW", root.destroy)
        root.mainloop()

    threading.Thread(target=run, daemon=True).start()

def show_text_position_editor(text, config):
    def run():
        global active_root

        # 古いウィンドウがあれば破棄
        try:
            if active_root and active_root.winfo_exists():
                active_root.after(0, active_root.destroy)
        except Exception as e:
            print(f"[WARN] 既存ウィンドウ破棄中に例外: {e}")
        active_root = None

        root = tk.Tk()
        active_root = root
        root.title("表示位置調整モード")
        root.attributes("-topmost", True)
        root.geometry("700x400+100+100")
        root.resizable(True, True)

        label = tk.Label(root, text=text, font=("Meiryo", 14), bg="black", fg="white", wraplength=640, justify="left")
        label.pack(pady=20, padx=20)

        def save_position():
            x, y = root.winfo_x(), root.winfo_y()
            config["overlay_position"] = {"x": x, "y": y}
            with open("config.yaml", "w", encoding="utf-8") as f:
                yaml.safe_dump(config, f, allow_unicode=True)
            print(f"[INFO] 表示位置を保存しました: x={x}, y={y}")
            root.destroy()

        button = tk.Button(root, text="この位置を保存", command=save_position, font=("Meiryo", 12))
        button.pack(pady=10)

        root.protocol("WM_DELETE_WINDOW", root.destroy)
        root.mainloop()

    threading.Thread(target=run, daemon=True).start()
