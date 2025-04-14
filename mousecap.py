from tkinter import Tk, Canvas

def get_mouse_selection_region():
    coords = {}

    def on_press(event):
        coords["x1"], coords["y1"] = event.x_root, event.y_root
        coords["rect"] = canvas.create_rectangle(event.x, event.y, event.x, event.y, outline="red", width=2)

    def on_drag(event):
        canvas.coords(coords["rect"], coords["x1"] - x, coords["y1"] - y, event.x, event.y)

    def on_release(event):
        coords["x2"], coords["y2"] = event.x_root, event.y_root
        root.quit()

    root = Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.attributes("-alpha", 0.3)
    root.configure(bg="black")

    x = root.winfo_x()
    y = root.winfo_y()

    canvas = Canvas(root, cursor="cross")
    canvas.pack(fill="both", expand=True)
    canvas.bind("<ButtonPress-1>", on_press)
    canvas.bind("<B1-Motion>", on_drag)
    canvas.bind("<ButtonRelease-1>", on_release)

    print("[INFO] ドラッグで範囲を選択してください")
    root.mainloop()
    root.destroy()

    if "x1" not in coords or "x2" not in coords:
        return None

    x1, y1 = coords["x1"], coords["y1"]
    x2, y2 = coords["x2"], coords["y2"]
    width, height = abs(x2 - x1), abs(y2 - y1)

    if width == 0 or height == 0:
        print("[WARN] 幅または高さが0のためキャンセル扱いします")
        return None

    return {
        "x": min(x1, x2),
        "y": min(y1, y2),
        "width": width,
        "height": height
    }
