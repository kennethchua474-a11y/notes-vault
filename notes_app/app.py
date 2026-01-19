import tkinter as tk
from pathlib import Path

from notes_app.gui import NotesGui
from notes_app.storage import NotesStorage


def main() -> None:
    data_path = Path.home() / ".notes_vault" / "notes.json"
    storage = NotesStorage(data_path)

    vault = storage.load()

    root = tk.Tk()
    NotesGui(root, vault, storage)
    root.mainloop()


if __name__ == "__main__":
    main()
