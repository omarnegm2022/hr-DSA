# HR-DSA

A collection of Python exercises and experiments in data structures and algorithms, including HackerRank-style problems, implementation notes, and small demonstrations. This is a study repository rather than a packaged application; some scripts contain interactive or import-time examples.

## Repository contents

### Root-level exercises

- `srchAlg.py` — sequential and recursive binary-search experiments; uses NumPy and the selection sort in `srtAlg.py`.
- `srchApp.py` — search-related exercises: Intro Tutorial, Missing Numbers, Balanced Sums, and KnightL on a Chessboard.
- `srtAlg.py` — sorting experiments, including insertion sort, quicksort, bubble sort, exchange sort, selection sort, and a merge-sort attempt.
- `srtAlgComparison.py` — bubble, exchange, selection, insertion, and merge-sort experiments, with example calls.
- `srtApp.py` — HackerRank-style insertion-sort and quicksort exercises.
- `Notes on D&C in sorting.txt` — notes comparing the divide-and-conquer approaches used by quicksort and merge sort.

### `1-D structures`

- `customITERobj.py` — a stack-backed queue exercise with enqueue, dequeue, and front-item operations.
- `Queue/` — a printer-queue simulation. `CQ/` contains the queue, print-task manager, and printer classes; `app.py` runs the simulation.
- `stack/StackFam/` — stack implementations backed by a NumPy array (`ArrStack.py`) and a Python list (`LiStack.py`), plus the stack interface and package initializer.
- `stack/apps.py` — stack usage and a delimiter-validation example.

### `N-D structures`

- `DecisionTree/BinClass.py` — binary-tree classes and an example that builds and evaluates a fully parenthesized arithmetic expression.
- `linkedList/base.py` — linked-list node, unordered-list, and ordered-list experiments.

`.vscode/settings.json` enables pytest discovery in VS Code. NumPy is used by several exercises; the repository does not include a dependency manifest.
