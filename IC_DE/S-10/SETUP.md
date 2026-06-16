# Session 10 — Setup Guide (Advanced SQL)

**Same setup as Session 9.** If you already have that environment working, you
can reuse it — just point it at this session's folder. Nothing new to install.

You need **Python 3.10+** and the same single dependency, DuckDB. No Java, no
WSL2, no `winutils.exe`.

---

## Folder layout

The notebook loads the CSVs with **relative paths** (`read_csv('data/...')`),
so the `data/` folder must sit **right next to** the notebook:

```
Session_10/
├── Session_10_Advanced_SQL.ipynb
├── requirements.txt
├── SETUP.md
└── data/
    ├── cities.csv
    ├── drivers.csv
    ├── riders.csv
    └── rides.csv
```

> The dataset is **identical** to Session 9 (same files, same fixed seed), so
> your numbers will match the notebook exactly and carry the story across both
> sessions.

---

## Install & launch

**macOS / Linux**
```bash
cd path/to/Session_10
python3 -m venv sql_venv && source sql_venv/bin/activate   # or reuse Session 9's
pip install -r requirements.txt
jupyter lab          # launch FROM this folder
```

**Windows (PowerShell)**
```powershell
cd path\to\Session_10
python -m venv sql_venv ; sql_venv\Scripts\activate         # or reuse Session 9's
pip install -r requirements.txt
jupyter lab          # launch FROM this folder
```

---

## Common issues

**`IO Error: No files found that match the pattern "data/cities.csv"`**
The #1 issue — Jupyter was launched from the wrong folder, so `data/...` doesn't
resolve. Close it, `cd` into the `Session_10` folder, and run `jupyter lab` from
there. Confirm inside the notebook with:
```python
import os; print(os.getcwd()); print(os.listdir("data"))
```
The second line should list the four CSV files. (In VS Code, set
**Jupyter › Notebook File Root** to `${fileDirname}` so the working directory
follows the notebook.)

**`ModuleNotFoundError: No module named 'duckdb'`**
Your virtual environment isn't active or the notebook is on a different kernel.
Re-activate, `pip install -r requirements.txt`, then **Kernel → Change Kernel**.
