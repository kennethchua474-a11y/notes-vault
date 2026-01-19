from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Note:
    id: int
    title: str
    content: str


class NotesVault:
    def __init__(self) -> None:
        self._notes: Dict[int, Note] = {}
        self._next_id: int = 1

    def create_note(self, title: str, content: str) -> Note:
        note = Note(
            id=self._next_id,
            title=title,
            content=content,
        )
        self._notes[note.id] = note
        self._next_id += 1
        return note

    def edit_note(self, note_id: int, title: str, content: str) -> None:
        if note_id not in self._notes:
            raise KeyError("Note not found")
        self._notes[note_id].title = title
        self._notes[note_id].content = content

    def delete_note(self, note_id: int) -> None:
        if note_id not in self._notes:
            raise KeyError("Notes not found")

        del self._notes[note_id]

    def list_notes(self) -> List[Note]:
        return list(self._notes.values())
