import tkinter as tk


def get_mouse_selection_region():
    region = {}
    done = False

    def on_mouse_down(event):
        region["x1"] = event.x_root
        region["y1"] = event.y_root
        canvas.delete("rect")

    def on_mouse_drag(event):
        canvas.delete("rect")
        x1, y1 = region.get("x1", 0), region.get("y1", 0)
        x2, y2 = event.x_root, event.y_root
        canvas.create_rectangle(x1, y1, x2, y2, outline="red", width=2, tags="rect")

    def on_mouse_up(event):
        region["x2"] = event.x_root
        region["y2"] = event.y_root
        root.quit()

    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-alpha", 0.3)
    root.configure(bg="black")
    root.attributes("-topmost", True)
    root.overrideredirect(True)

    canvas = tk.Canvas(root, bg="black")
    canvas.pack(fill="both", expand=True)

    canvas.bind("<ButtonPress-1>", on_mouse_down)
    canvas.bind("<B1-Motion>", on_mouse_drag)
    canvas.bind("<ButtonRelease-1>", on_mouse_up)

    print("[INFO] ドラッグで範囲を選択してください")
    root.mainloop()
    root.destroy()

    if not all(k in region for k in ("x1", "y1", "x2", "y2")):
        return None

    x1, y1, x2, y2 = region["x1"], region["y1"], region["x2"], region["y2"]
    return {
        "x": min(x1, x2),
        "y": min(y1, y2),
        "width": abs(x2 - x1),
        "height": abs(y2 - y1),
    }