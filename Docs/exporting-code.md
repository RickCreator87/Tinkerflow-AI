 docs/exporting-code.md

```markdown
# Exporting Python Code from Your Graph

Once you've built a visual program in Tinkerflow, you can export it as a standard Python script to run anywhere.

---

## How to Export
1. Click the **"Export"** button in the top toolbar (or use `Ctrl+E`).
2. Choose your export options:
   - **Include comments** – Adds explanations from your nodes as comments.
   - **Minify** – Remove extra whitespace (useful for sharing).
3. Click **"Generate Code"**. The Python code will appear in a new panel.
4. Copy the code or click **"Download as .py"** to save it.

---

## What the Exported Code Looks Like
For a simple graph that adds two numbers, the generated code might be:
```python
# Tinkerflow generated code
def main():
    # Node: Number (value: 5)
    number_1 = 5

    # Node: Number (value: 3)
    number_2 = 3

    # Node: Add
    result = number_1 + number_2

    # Node: Print
    print(result)

if __name__ == "__main__":
    main()
```
