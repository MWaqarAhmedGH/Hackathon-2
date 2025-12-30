# Acceptance Criteria — Phase 1 CLI Todo App

## General Behavior

1. Application starts without errors using:
   python main.py
2. Application displays a clear menu on start.
3. Application runs continuously until user chooses Exit.

## Add Todo

1. When user selects "Add Todo":
   - User is prompted for todo description.
   - Todo is added with a unique numeric ID.
   - Status is set to PENDING.
   - Confirmation message is shown.

## List Todos

1. When user selects "List Todos":
   - All todos are displayed in tabular format.
   - Each row shows ID, Description, and Status.
2. If no todos exist:
   - A friendly message is displayed.

## Mark Todo as Done

1. When user selects "Mark Todo as Done":
   - User is prompted for todo ID.
2. If ID exists and status is PENDING:
   - Status changes to DONE.
   - Confirmation message is shown.
3. If ID does not exist:
   - Error message is displayed.
4. If todo is already DONE:
   - Informational message is displayed.

## Delete Todo

1. When user selects "Delete Todo":
   - User is prompted for todo ID.
2. If ID exists:
   - Todo is removed.
   - Confirmation message is shown.
3. If ID does not exist:
   - Error message is displayed.

## Exit Application

1. When user selects "Exit":
   - Application terminates gracefully.
   - Goodbye message is shown.

## Constraints Verification

1. No files are created or written.
2. No external libraries are used.
3. All data is lost after application exits.
