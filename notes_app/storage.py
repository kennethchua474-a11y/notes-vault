import json
from pathlib import Path

from notes_app.core import NotesVault


class NotesStorage:
    def __init__(self, path: Path) -> None:
        self._path = path

    def save(self, vault: NotesVault) -> None:
        data = [
            {
                "id": note.id,
                "title": note.title,
                "content": note.content,
            }
            for note in vault.list_notes()
        ]

        self._path.parent.mkdir(parents=True, exist_ok=True)

        with self._path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load(self) -> NotesVault:
        vault = NotesVault()

        if not self._path.exists():
            return vault

        with self._path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            vault.create_note(item["title"], item["content"])

        return vault
