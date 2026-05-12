# PySpark Setup Guide

This guide walks you through everything you need to run the Spark notebooks (Session 5 onward) **smoothly**, on Windows, macOS, or Linux.

The #1 thing that breaks PySpark setups isn't Python — it's Java. Read all of step 1 before you skip to `pip install`.

> 💡 **Important up front:** Java is installed **computer-wide**, not inside your Python virtual environment. `pip` cannot install Java because Java isn't a Python package — it's a runtime that PySpark talks to. Whether your venv is activated or not when you run `brew install openjdk@11` doesn't matter. One Java install on your machine serves every project, every venv, forever.

---

## Step 1 — Install Java 11

Spark runs on the JVM. You need **Java 11** specifically. Java 8 also works but is older. **Avoid Java 17 and Java 21** — they technically run Spark but cause subtle issues (especially with UDFs).

### Check what you have

Open a terminal and run:

```bash
java -version
```

If you see `openjdk version "11.x.x"` — you're done. Skip to step 2.

If you see Java 17, 21, or "command not found" — install Java 11.

### Install Java 11

**macOS (Homebrew)**

Run each of these **one at a time**, pressing Enter after each. Don't paste the whole block at once — multi-line commands with backslashes can leave your terminal stuck in a `quote>` state when pasted from a webpage.

```bash
brew install openjdk@11
```

Wait for that to finish (1–2 min download). Then:

```bash
sudo mkdir -p /Library/Java/JavaVirtualMachines
```

Then (this is **one line** — don't break it with a backslash):

```bash
sudo ln -sfn $(brew --prefix)/opt/openjdk@11/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-11.jdk
```

**Ubuntu / WSL**
```bash
sudo apt update
sudo apt install openjdk-11-jdk
```

**Windows**

> 💡 **Strongly recommended alternative:** install **WSL2** (Windows Subsystem for Linux) and follow the Ubuntu instructions instead. Spark, Docker, and most data engineering tools run more smoothly on Linux. To set up WSL2, open PowerShell as Administrator and run `wsl --install`, then restart. After that, follow the Ubuntu steps below from inside your WSL Ubuntu terminal.
>
> If you want to stay on native Windows, follow the steps below.

**Step 1a — Install Java 11 via Adoptium**

1. Go to [Adoptium Temurin 11 downloads](https://adoptium.net/temurin/releases/?version=11)
2. Pick the **Windows x64 MSI** installer (not the `.zip`)
3. Run the installer. **Important:** on the "Custom Setup" screen, change these from "Will be installed on local hard drive" to **"Entire feature will be installed on local hard drive"**:
   - **Set JAVA_HOME variable**
   - **Add to PATH**
   - **JavaSoft (Oracle) registry keys**

   These are off by default. If you skip this you'll spend an hour debugging.
4. Finish the install.

**Step 1b — Verify Java works (Windows)**

Open a **new** PowerShell window (not an old one — the install only affects new shells) and run:

```powershell
java -version
```

You should see `openjdk version "11.0.x"`.

Then check `JAVA_HOME` is set:

```powershell
echo $env:JAVA_HOME
```

You should see a path like `C:\Program Files\Eclipse Adoptium\jdk-11.0.x-hotspot`.

If `JAVA_HOME` is empty or the wrong version, set it manually:
1. Press **Win + R**, type `sysdm.cpl`, press Enter
2. Go to **Advanced → Environment Variables**
3. Under **System variables**, click **New**
4. Variable name: `JAVA_HOME`
5. Variable value: the full path to your JDK 11 install (something like `C:\Program Files\Eclipse Adoptium\jdk-11.0.x-hotspot`)
6. Click OK, close all dialogs, **open a new PowerShell window** and re-check.

> ⚠️ **Avoid paths with spaces if you can.** If your JDK installed to `C:\Program Files\...`, Spark will mostly cope with it, but some edge cases (especially in Hadoop on Windows) break. If you hit weird errors, reinstall the JDK to a path like `C:\Java\jdk-11` and update `JAVA_HOME`.

**Step 1c — Install winutils.exe (Windows-only requirement)**

This step is **not optional on Windows.** Spark needs a small Hadoop helper binary that doesn't ship with PySpark. Without it, you'll get cryptic errors when reading or writing files.

In PowerShell:

```powershell
mkdir C:\hadoop\bin
Invoke-WebRequest -Uri "https://github.com/cdarlint/winutils/raw/master/hadoop-3.3.5/bin/winutils.exe" -OutFile "C:\hadoop\bin\winutils.exe"
Invoke-WebRequest -Uri "https://github.com/cdarlint/winutils/raw/master/hadoop-3.3.5/bin/hadoop.dll" -OutFile "C:\hadoop\bin\hadoop.dll"
```

Then set `HADOOP_HOME`:

```powershell
[Environment]::SetEnvironmentVariable("HADOOP_HOME", "C:\hadoop", "User")
```

Open a **new** PowerShell window and verify:

```powershell
echo $env:HADOOP_HOME
# Should print: C:\hadoop
```

### Set `JAVA_HOME` (macOS / Linux only)

Add this line to your `~/.zshrc` (macOS) or `~/.bashrc` (Linux):

```bash
# macOS
export JAVA_HOME=$(/usr/libexec/java_home -v 11)

# Linux
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

Then reload:
```bash
source ~/.zshrc        # or ~/.bashrc
echo $JAVA_HOME        # should print a path
java -version          # should now say 11
```

> ⚠️ **Multiple Java versions installed?** That's fine — just make sure `JAVA_HOME` points to the **Java 11** installation. Spark will use whatever `JAVA_HOME` says, regardless of what `java -version` shows in your shell.

---

## Step 2 — Create a Python virtual environment

We don't want PySpark and its deps polluting your system Python. Use a virtual environment (we'll cover this formally in Session 14 — for now, just follow along).

```bash
# Make sure you're using Python 3.10 or newer
python3 --version

# Create a virtual environment named 'pandas_venv' (we'll keep this name across sessions)
python3 -m venv pandas_venv

# Activate it
# macOS / Linux:
source pandas_venv/bin/activate
# Windows (PowerShell):
pandas_venv\Scripts\Activate.ps1
# Windows (cmd.exe):
pandas_venv\Scripts\activate.bat
```

When the venv is active, your terminal prompt will start with `(pandas_venv)`.

---

## Step 3 — Install Python dependencies

With the venv active:

```bash
pip install -r requirements.txt
```

This installs PySpark, pandas, pyarrow, Jupyter, and matplotlib — everything the notebooks need.

> 💡 **First-time pip warning:** the install pulls ~290 MB for PySpark alone (it bundles the Spark JARs). Be patient.

---

## Step 4 — Verify it all works

Run this quick sanity check.

**macOS / Linux:**
```bash
python -c "
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('test').master('local[*]').getOrCreate()
print(f'Spark version: {spark.version}')
print(f'Java works: {spark.sparkContext.applicationId}')
spark.stop()
"
```

**Windows (PowerShell)** — multi-line `python -c` doesn't work well in PowerShell, so save to a file and run it:

```powershell
@"
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('test').master('local[*]').getOrCreate()
print(f'Spark version: {spark.version}')
print(f'Java works: {spark.sparkContext.applicationId}')
spark.stop()
"@ | Out-File -Encoding utf8 verify_spark.py
python verify_spark.py
```

If you see a Spark version printed and an application ID, **you're done**. Open a notebook and start working.

---

## Step 5 — Launch Jupyter

```bash
jupyter notebook
```

Or, if you prefer JupyterLab:
```bash
pip install jupyterlab
jupyter lab
```

---

## Step 6 — Restart the kernel if you installed Java mid-session

> ⚠️ **This step matters if you already had a notebook open while installing Java.**

The Jupyter kernel inherits the environment it was started in. If you opened your notebook *before* installing Java, the kernel doesn't know Java exists yet — even after `brew install openjdk@11` finishes. PySpark will keep failing with `JAVA_GATEWAY_EXITED` until you give the kernel a fresh environment.

**The fix is one click:**

- **In VS Code:** click **"Restart"** at the top of the notebook (circular arrow icon, not "Run All")
- **In Jupyter Notebook / Lab:** menu → **Kernel → Restart**

Then re-run your cells from the top. The SparkSession cell should now succeed.

Note: kernel **restart** is different from kernel **interrupt** — interrupt only stops a running cell, restart actually kills and replaces the Python process (which picks up the new Java).

---

## Common problems and fixes

### Just installed Java/winutils on Windows but it's not working
Windows environment variables only take effect in **new** shells. Close every PowerShell, cmd.exe, and VS Code window, then open a fresh one. Re-run `echo $env:JAVA_HOME` to confirm the variable is set in the new shell.

### Terminal stuck showing `quote>` after pasting commands
You pasted a multi-line command and the shell got stuck waiting for an unclosed quote. Fix:

1. Press **Ctrl + C** to cancel and get back to your normal prompt
2. Run the commands one at a time instead of pasting the whole block

This often happens when pasting from a web page, Slack, or PDF — invisible formatting characters or copied line continuations (`\`) confuse the shell.

### `Java gateway process exited before sending its port number`
Almost always a Java problem. Check, in order:
1. Is Java 11 installed? `java -version` should print `openjdk version "11.x.x"`
2. Is `JAVA_HOME` set? `echo $JAVA_HOME` (Mac/Linux) or `echo %JAVA_HOME%` (Windows)
3. Are you using Java 17+? Downgrade to Java 11.
4. **Did you restart the kernel after installing Java?** See Step 6 above.

### `winutils.exe not found` / `HADOOP_HOME not set` (Windows)
You skipped Step 1c. Go back and follow it — winutils is mandatory for Spark on native Windows. (Or switch to WSL2, which doesn't need winutils.)

### `MemoryError` when reading the NYC taxi parquet in Pandas
That's expected — that's the whole point of Session 6. Use Spark instead.

### Notebook kernel keeps dying during the Spark demos
Your laptop is probably running out of memory. Two things:
- Close other heavy apps (Chrome, Slack, Docker Desktop)
- In the notebook, after the Pandas demo cell, make sure `del pdf` and `gc.collect()` actually run before the Spark cells

### Python version too old (Spark 3.5 needs Python 3.10+)
Install Python 3.12:
- **macOS**: `brew install python@3.12`
- **Ubuntu**: `sudo apt install python3.12 python3.12-venv`
- **Windows**: Download from [python.org](https://www.python.org/downloads/)

Then create the venv with the new Python:
```bash
python3.12 -m venv pandas_venv
```

---

## What to install once vs once-per-session

| Install once (across all sessions) | Java 11, Python 3.12, virtual environment |
| Install once per session | `pip install -r requirements.txt` (the venv keeps things isolated) |

That's it. If something doesn't work, post in the course Slack — chances are someone else hit the same thing.

— Ameer
