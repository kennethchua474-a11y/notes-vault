==========================================
Personal Notes Vault Program Specification
==========================================

Description
-----------

A simple desktop application that lets a single user:
* create personal notes
* edit them
* delete them
* save them locally

Requirements
------------

The application must satisfy the following requirements:

Functional Requirements
~~~~~~~~~~~~~~~~~~~~~~~

* The user shall be able to create a new note.
* The user shall be able to select an existing note from a list.
* The user shall be able to edit the contents of a note.
* The user shall be able to delete a note.
* The application shall save notes locally on disk.
* The application shall load existing notes automatically on startup.

Non-Functional Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* The application shall run as a desktop GUI application.
* The application shall work offline.
* The application shall not require user authentication.
* The application shall not require an internet connection.
* The application shall be usable by non-technical users.

User Interface
--------------

The user interface shall consist of:

* A main application window
* A list of notes displayed on the left side
* A text editor area displayed on the right side
* Buttons for:

  * Creating a new note
  * Deleting the selected note
  * Saving notes (manual or automatic)

The interface shall prioritize simplicity and clarity over customization.

Data Storage
------------

* Notes shall be stored locally on the user's machine.
* Notes shall be persisted using a single storage format.
* The initial storage format shall be JSON.
* Each note shall contain:

  * A unique identifier
  * A title
  * Text content

* The storage layer shall be independent from the user interface.

Architecture Constraints
------------------------

* Business logic shall be separated from the GUI layer.
* The core logic shall not depend on any GUI framework.
* File I/O operations shall not be implemented inside the GUI layer.
* The system shall be structured to allow unit testing of core logic.

Target Platforms
----------------

* The application shall support:

  * Microsoft Windows
  * Apple macOS

* The application shall be packageable as a standalone executable for each platform.

Out of Scope
------------

The following features are explicitly out of scope for this version:

* Cloud synchronization
* Encryption of note contents
* Rich text or markdown formatting
* Search functionality
* Multi-user support

Definition of Done
------------------

The program shall be considered complete when:

* All functional requirements are implemented.
* Notes persist correctly across application restarts.
* The GUI operates without requiring a terminal.
* Automated tests for core logic pass.
* Continuous Integration checks pass successfully.
* The application can be packaged into a distributable desktop application.
