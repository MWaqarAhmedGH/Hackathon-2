# Feature Specification — Phase 1 CLI Todo App

## Overview
The application is a simple command-line Todo manager.
All todos exist only in memory during runtime.

## Core Features

### 1. Add Todo
- User can add a new todo item.
- Todo consists of:
  - unique numeric ID (starting from 1)
  - text description
- After adding, system confirms the addition.

### 2. List Todos
- User can view all todos.
- Display format:
  ID | Description | Status
- Status is either:
  - PENDING
  - DONE
- If no todos exist, display a friendly message.

### 3. Mark Todo as Done
- User can mark a todo as completed using its ID.
- If ID does not exist, show an error message.
- If already marked DONE, inform the user.

### 4. Delete Todo
- User can delete a todo using its ID.
- If ID does not exist, show an error message.

### 5. Exit Application
- User can exit the application gracefully.

## CLI Interaction

- Application runs in a loop until exit.
- Menu options must be displayed clearly.
- User selects options via numeric input.

## Data Handling Rules

- Todos are stored in a Python list.
- Each todo is represented as a dictionary.

## Explicit Exclusions

- No file saving
- No databases
- No user authentication
- No due dates, priorities, or categories
