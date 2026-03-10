---

Docs/node-reference.md
```markdown
# Node Reference

Tinkerflow provides a variety of nodes to build Python programs visually. Nodes are grouped by category.

---

## 🧱 Basic Nodes
| Node      | Purpose                                      | Example                                   |
|-----------|----------------------------------------------|-------------------------------------------|
| `Number`  | Represents an integer or float.              | `42`, `3.14`                              |
| `String`  | Represents text.                             | `"Hello"`                                 |
| `Boolean` | Represents `True` or `False`.                | `True`                                    |
| `Variable`| Stores a value for later use.                 | `x = 5`                                   |

---

## ➕ Operators
| Node       | Description                | Inputs          | Output           |
|------------|----------------------------|-----------------|------------------|
| `Add`      | Addition (`+`)             | a, b            | a + b            |
| `Subtract` | Subtraction (`-`)          | a, b            | a - b            |
| `Multiply` | Multiplication (`*`)       | a, b            | a * b            |
| `Divide`   | Division (`/`)             | a, b            | a / b            |
| `Modulo`   | Remainder (`%`)            | a, b            | a % b            |
| `Equals`   | Equality comparison (`==`) | a, b            | True/False       |
| `Greater`  | Greater than (`>`)         | a, b            | True/False       |

---

## 🔁 Control Flow
| Node         | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `If`         | Conditional branch. Connect a condition and two outputs (true/false).      |
| `For Loop`   | Loop over a range or collection. Provides the loop variable as output.     |
| `While Loop` | Repeat while a condition is true.                                           |
| `Break`      | Exit a loop prematurely.                                                    |

---

## 📦 Data Structures
| Node        | Purpose                                          |
|-------------|--------------------------------------------------|
| `List`      | Create a list. You can add items dynamically.    |
| `Dict`      | Create a dictionary (key‑value pairs).           |
| `Get Item`  | Access an element from a list or dictionary.     |
| `Set Item`  | Modify an element in a list or dictionary.       |

---

## 🖨️ Input/Output
| Node      | Description                                       |
|-----------|---------------------------------------------------|
| `Print`   | Output a value to the console.                    |
| `Input`   | Prompt the user for input (returns a string).     |
| `File Read` | Read contents from a file (path as input).      |
| `File Write`| Write data to a file.                           |

---

## 🤖 AI‑Assisted Nodes
| Node          | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `AI Explain`  | Attach to any node to get a plain‑English explanation of its purpose.      |
| `AI Generate` | Describe what you want in natural language, and the AI builds a sub‑graph. |

> 💡 *The AI nodes require an internet connection and may use API credits if you're using a remote service.*

---

## 📐 Functions
| Node          | Description                                           |
|---------------|-------------------------------------------------------|
| `Function Def`| Define a reusable function with inputs and outputs.   |
| `Function Call`| Call a previously defined function.                  |
| `Return`      | Return a value from a function.                       |

---

## ⚙️ Advanced
| Node        | Description                                   |
|-------------|-----------------------------------------------|
| `Python`    | Write raw Python code inside a node (advanced).|
| `Comment`   | Add notes to your graph (ignored during execution).|

---

> *New nodes are added regularly. Check the [changelog](../CHANGELOG.md) for updates.*
