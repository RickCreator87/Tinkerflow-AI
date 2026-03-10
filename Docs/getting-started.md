2. docs/getting-started.md

```markdown
# Getting Started with Tinkerflow-AI

Follow this guide to set up Tinkerflow and build your first visual program.

---

## 1. Installation

### Prerequisites
- Python 3.8 or higher (if running locally)
- A modern web browser (Chrome, Firefox, Edge)

### Option A: Run from Source
```bash
git clone https://github.com/rickcreator87/Tinkerflow-AI.git
cd Tinkerflow-AI
pip install -r requirements.txt   # if you have a requirements file
python app.py                     # or your start command
```

Then open http://localhost:5000 in your browser.

Option B: Use the Live Demo (if available)

Visit https://rickcreator87.github.io/Tinkerflow-AI/ to try the online version.

---

2. Your First Graph

When you open Tinkerflow, you'll see a blank canvas and a palette of nodes on the left.

Create a Simple "Hello World"

1. Drag a Print node from the palette onto the canvas.
2. Drag a String node and connect its output to the Print node's input.
3. Double‑click the String node to edit its text. Type "Hello, Tinkerflow!".
4. Click the "Run" button (or press Ctrl+Enter). You should see the output in the console panel.

🎉 Congratulations! You've just built your first visual program.

---

3. Understanding the Interface

· Node Palette – All available node types (variables, operators, control flow, etc.).
· Canvas – Where you build your graph. Pan by dragging the background, zoom with mouse wheel.
· Properties Panel – Appears when you select a node; lets you edit its parameters.
· Console – Shows output from Print nodes and any errors.
· AI Chat – Ask the AI questions about your graph or Python concepts.
