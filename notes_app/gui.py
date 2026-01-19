import tkinter as tk
from tkinter import messagebox
from typing import Optional

from notes_app.core import NotesVault
from notes_app.storage import NotesStorage


class NotesGui:
    def __init__(
        self,
        root: tk.Tk,
        vault: NotesVault,
        storage: NotesStorage,
    ) -> None:
        self.root = root
        self.vault = vault
        self.storage = storage
        self.selected_note_id: Optional[int] = None

        root.title("Personal Notes Vault")

        self.listbox = tk.Listbox(root, width=40)
        self.listbox.pack(padx=10, pady=10)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        self.title_entry = tk.Entry(root, width=40)
        self.title_entry.pack(padx=10, pady=5)

        self.text = tk.Text(root, width=40, height=10)
        self.text.pack(padx=10, pady=5)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="New", command=self.new_note).grid(
            row=0, column=0, padx=5
        )
        tk.Button(btn_frame, text="Save", command=self.save_note).grid(
            row=0, column=1, padx=5
        )
        tk.Button(btn_frame, text="Delete", command=self.delete_note).grid(
            row=0, column=2, padx=5
        )

        self.refresh_list()

    # ---------- UI helpers ----------

    def refresh_list(self) -> None:
        self.listbox.delete(0, tk.END)
        for note in self.vault.list_notes():
            self.listbox.insert(tk.END, f"{note.id}: {note.title}")

    def clear_editor(self) -> None:
        self.selected_note_id = None
        self.title_entry.delete(0, tk.END)
        self.text.delete("1.0", tk.END)

    # ---------- Callbacks ----------

    def on_select(self, event: object) -> None:
        selection = self.listbox.curselection()  # type: ignore[no-untyped-call]
        if not selection:
            return

        index = selection[0]
        note = self.vault.list_notes()[index]

        self.selected_note_id = note.id
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, note.title)

        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, note.content)

    def new_note(self) -> None:
        self.clear_editor()

    def save_note(self) -> None:
        title = self.title_entry.get().strip()
        content = self.text.get("1.0", tk.END).strip()

        if not title:
            messagebox.showwarning("Validation", "Title is required")
            return

        if self.selected_note_id is None:
            self.vault.create_note(title, content)
        else:
            try:
                self.vault.edit_note(self.selected_note_id, title, content)
            except KeyError:
                messagebox.showerror("Error", "Note not found")

        self.storage.save(self.vault)
        self.refresh_list()
        self.clear_editor()

    def delete_note(self) -> None:
        if self.selected_note_id is None:
            return

        try:
            self.vault.delete_note(self.selected_note_id)
        except KeyError:
            messagebox.showerror("Error", "Note not found")

        self.storage.save(self.vault)
        self.refresh_list()
        self.clear_editor()
