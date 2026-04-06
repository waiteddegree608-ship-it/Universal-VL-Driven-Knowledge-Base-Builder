---
description: Transform the knowledge base extraction scripts into a full-stack local web application.
---

# Knowledge Base Extractor Application Development Plan

## 1. Backend Refactoring (Python)
The current script `build_kb_iterative.py` contains all logic in a single file. We need to decouple it for API usage.

- [ ] Create `backend/engine.py`: Encapsulate `process_folder_task`, `call_vl_api`, and worker pools into a `KnowledgeEngine` class.
- [ ] Add State Management: The engine must emit progress updates (e.g., via callbacks or queues) instead of just printing to console.
- [ ] Create `backend/main.py`: A FastAPI server.
    - `POST /config`: Set API keys, output paths, max workers.
    - `POST /scan`: Scan target directory for PDF/PPT structure.
    - `POST /start`: Start processing.
    - `POST /stop`: Stop/Pause processing.
    - `WS /ws`: WebSocket endpoint to stream real-time logs and task progress to the UI.

## 2. Frontend Development (React + Vite)
Build a premium, modern UI to control the engine.

- [ ] Initialize project: `npx create-vite@latest frontend --template react`
- [ ] Design System: Use CSS Variables for a dark/premium theme (Glassmorphism, Neon accents).
- [ ] **Components**:
    - **Sidebar**: Project switcher, Global Settings (API Keys).
    - **Dashboard**: Grid view of detected Chapters/Slides.
    - **TaskCard**: A card for each file showing:
        - Status Icon (Queued, Spinning, Checkmark, Error).
        - Progress Bar (e.g., "Page 5/14").
        - Live "Thought/Context" preview (optional).
    - **LogConsole**: A collapsible terminal-like view for low-level logs.
    - **Preview**: A Markdown renderer to see the generated KB in real-time.

## 3. Integration & Packaging
- [ ] Connect React to FastAPI.
- [ ] Ensure `win32com` and file paths work correctly in the local server context.
- [ ] (Optional) Create a startup script (Batch/PowerShell) to launch both Backend and Frontend with one click.

## 4. Execution Strategy
1.  **Stop current scripts**: Ensure no file locks.
2.  **Create Directory Structure**: `E:\workspace\ddl\KB_App`.
3.  **Move & Refactor Code**.
4.  **Build UI**.
5.  **Run & Test**.
