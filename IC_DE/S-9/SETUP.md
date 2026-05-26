# Session 9 — Setup Guide (SQL Core Concepts)

Good news: there is **nothing heavy to install** this week. Unlike the Spark
sessions, DuckDB has **no Java, no WSL2, and no `winutils.exe`** — it installs
with a single `pip` command and runs natively on macOS, Windows, and Linux.

You need **Python 3.10 or newer** (you already have this from earlier sessions).

---

## Folder layout — read this first

The notebook loads the CSV files using **relative paths** like
`read_csv('data/cities.csv')`. So the `data/` folder must sit **right next to**
the notebook:

```
Session_09/
├── Session_09_SQL_Core_Concepts.ipynb
├── requirements.txt
├── SETUP.md
└── data/
    ├── cities.csv
    ├── drivers.csv
    ├── riders.csv
    └── rides.csv
```

Keep them together and you'll never hit a "file not found" error.

---

## macOS / Linux

```bash
# 1. From inside the Session_09 folder:
cd path/to/Session_09

# 2. (Recommended) create and activate a virtual environment
python3 -m venv sql_venv
source sql_venv/bin/activate

# 3. Install the packages
pip install -r requirements.txt

# 4. Launch JupyterLab FROM THIS FOLDER (important — see note below)
jupyter lab
```

## Windows (PowerShell)

```powershell
# 1. From inside the Session_09 folder:
cd path\to\Session_09

# 2. (Recommended) create and activate a virtual environment
python -m venv sql_venv
sql_venv\Scripts\activate

# 3. Install the packages
pip install -r requirements.txt

# 4. Launch JupyterLab FROM THIS FOLDER
jupyter lab
```

---

## Verify it works

In a terminal (with your environment active):

```bash
python -c "import duckdb; print('DuckDB', duckdb.__version__)"
```

You should see `DuckDB 1.5.3` (or newer).

---

## Common issues

**`IOException ... No such file or directory: 'data/cities.csv'`**
This is the #1 issue. It means Jupyter was started from a different folder, so
the relative path `data/...` doesn't point where you expect. Fix: close Jupyter,
`cd` into the `Session_09` folder, and run `jupyter lab` **from there**. Confirm
with this cell inside the notebook:
```python
import os; print(os.getcwd()); print(os.listdir("data"))
```
The second line should list the four CSV files.

**`ModuleNotFoundError: No module named 'duckdb'`**
Your virtual environment isn't active, or the notebook is using a different
kernel. Re-activate the environment, reinstall, and pick the matching kernel via
**Kernel → Change Kernel** in JupyterLab.

**Numbers look slightly different from the notes**
The dataset is fixed (generated with a set seed), so your results should match
exactly. If they don't, you may have an edited copy of a CSV — re-copy the
original `data/` folder.
