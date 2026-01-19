import pytest

from notes_app.core import Note, NotesVault


def test_create_note() -> None:
    vault = NotesVault()

    note = vault.create_note("Title", "Content")

    assert note == Note(id=1, title="Title", content="Content")


def test_list_notes() -> None:
    vault = NotesVault()

    vault.create_note("A", "1")
    vault.create_note("B", "2")

    notes = vault.list_notes()

    assert len(notes) == 2
    assert notes[0].title == "A"
    assert notes[1].title == "B"


def test_edit_note() -> None:
    vault = NotesVault()
    note = vault.create_note("Old", "Text")

    vault.edit_note(note.id, "New", "Updated")

    updated = vault.list_notes()[0]
    assert updated.title == "New"
    assert updated.content == "Updated"


def test_delete_note() -> None:
    vault = NotesVault()
    note = vault.create_note("Delete", "Me")

    vault.delete_note(note.id)

    assert vault.list_notes() == []


def test_edit_nonexistent_note_raises() -> None:
    vault = NotesVault()

    with pytest.raises(KeyError):
        vault.edit_note(999, "X", "Y")


def test_delete_nonexistent_note_raises() -> None:
    vault = NotesVault()

    with pytest.raises(KeyError):
        vault.delete_note(999)
