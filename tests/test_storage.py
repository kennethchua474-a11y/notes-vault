from pathlib import Path

from notes_app.storage import NotesStorage


def test_save_and_load(tmp_path: Path) -> None:
    from notes_app.core import NotesVault

    vault = NotesVault()
    vault.create_note("A", "1")
    vault.create_note("B", "2")

    file_path = tmp_path / "notes.json"
    storage = NotesStorage(file_path)

    storage.save(vault)
    loaded_vault = storage.load()

    notes = loaded_vault.list_notes()

    assert len(notes) == 2
    assert notes[0].title == "A"
    assert notes[1].content == "2"
