# Week 3 Homework — Distributed Data Processing with Spark

**Modern Data Engineering Course · Week 3 (Sessions 5 & 6)**
*Instructor: Ameer Ul Islam · Depthware*

---

## Overview

This week you learned to process data with Apache Spark — from your first `SparkSession` to lazy evaluation, transformations, actions, and Spark SQL. This homework has **two parts**, one per session. Do both.

**What to submit:** one `.ipynb` notebook (or two `.py` files) containing your solutions to both parts. Name it `week3_<yourname>.ipynb`.

**Due:** before Session 7.

**Datasets you'll need (in the course repo):**
- `dhaka_rides_500k.csv` — 500,000 synthetic Dhaka ride records (for Part 1)
- `nyc_taxi_jan2024.parquet` — ~3M NYC taxi trips (for Part 2)

---

## Part 1 — Build a Spark ETL pipeline (Session 5)

**Goal:** Take a raw CSV, clean and filter it, and write the result as Parquet — the bread-and-butter task of a data engineer.

### Tasks

1. Create a `SparkSession` in local mode with a descriptive `appName`.
2. Define an **explicit schema** (a `StructType`) for the rides data — don't use `inferSchema`.
3. Load `dhaka_rides_500k.csv` using your schema.
4. Filter the data to keep only:
   - rides where `status == "completed"`, **and**
   - rides where `fare_bdt > 200`
5. Write the filtered result to Parquet at `completed_high_fare_rides.parquet`.
6. Read the Parquet back and confirm the row count is lower than the original 500,000.
7. **Compare file sizes:** print the size of the original CSV vs your Parquet output, and the compression ratio.

### Deliverable checklist

- [ ] Explicit schema defined (no `inferSchema=True`)
- [ ] Both filters applied correctly
- [ ] Output written as Parquet
- [ ] Row count printed before and after filtering
- [ ] CSV-vs-Parquet size comparison printed
- [ ] `spark.stop()` called at the end

---

## Part 2 — Analytics with the DataFrame API and Spark SQL (Session 6)

**Goal:** Answer a real analytical question two different ways, and prove they produce the same result.

### The question

> *"For each pickup location (`PULocationID`), what is the average fare, the average tip percentage, and the total revenue — for trips with a passenger count between 1 and 4?"*

Where `tip_pct = tip_amount / fare_amount * 100`.

### Tasks

1. Load `nyc_taxi_jan2024.parquet` into a Spark DataFrame.
2. **Version A — DataFrame API:** build the full pipeline using `.filter()`, `.withColumn()`, `.groupBy()`, `.agg()`, and `.orderBy()`. Sort by total revenue, highest first. Show the top 10 pickup locations.
3. **Version B — Spark SQL:** register the DataFrame as a temp view and answer the **same** question with a single SQL query. Show the top 10.
4. Confirm both versions produce the same numbers for the top 10.

### Bonus (for extra credit)

5. Run `.explain()` on both versions. Paste the **physical plan** of each into a markdown cell (or as a comment).
6. In 2–3 sentences, describe what you notice. Are the physical plans similar? What does that tell you about how Spark SQL and the DataFrame API relate?

### Deliverable checklist

- [ ] DataFrame API version runs and shows top 10 by revenue
- [ ] Spark SQL version runs and shows top 10
- [ ] Both produce matching numbers
- [ ] (Bonus) `.explain()` output included for both
- [ ] (Bonus) 2–3 sentence reflection on the plans

---

## Starter scaffold

Use this as a skeleton — fill in the blanks:

```python
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, DateType
from pyspark.sql.functions import col, avg, count, round as spark_round, sum as spark_sum

spark = (
    SparkSession.builder
        .appName("Week3Homework")
        .master("local[*]")
        .getOrCreate()
)

# ============================================================
# PART 1 — Dhaka rides ETL
# ============================================================
schema = StructType([
    # TODO: define the 7 columns with correct types
])

rides = (
    spark.read
        .option("header", True)
        # TODO: use .schema(...) not inferSchema
        .csv("dhaka_rides_500k.csv")
)

# TODO: filter, write to parquet, compare sizes


# ============================================================
# PART 2 — NYC taxi analytics
# ============================================================
nyc = spark.read.parquet("nyc_taxi_jan2024.parquet")

# TODO: Version A — DataFrame API

# TODO: Version B — Spark SQL (register temp view first)


spark.stop()
```

---

## Grading rubric (100 points)

| Criteria | Points |
|---|---|
| **Part 1 — Pipeline correctness** | |
| Explicit schema defined correctly (no inferSchema) | 15 |
| Both filters applied correctly | 15 |
| Parquet written and read back successfully | 10 |
| File size comparison printed | 10 |
| **Part 2 — Analytics** | |
| DataFrame API version correct | 20 |
| Spark SQL version correct | 20 |
| Both versions produce matching results | 10 |
| **Code quality** | |
| Clean, readable, `spark.stop()` called, no leftover errors | 10 |
| **Bonus (extra credit, up to +10)** | |
| `.explain()` output + thoughtful reflection on the plans | +10 |
| **Total** | **100 (+10)** |

---

## Tips & common mistakes

- **Don't use `inferSchema=True` in Part 1.** The whole point is to practice explicit schemas. You'll lose points.
- **Watch your filter logic.** "completed AND fare > 200" — make sure you chain both conditions, not just one.
- **For Part 2, the two versions must match.** If they don't, you have a bug in one of them — usually a difference in how you computed `tip_pct` or a missing filter.
- **Don't `.collect()` or `.toPandas()` the full NYC dataset.** Use `.show(10)` to display results. Pulling 3M rows to the driver is the exact mistake we warned about.
- **`spark.stop()` at the end.** Especially if you're running in a notebook — leftover sessions hold onto resources.
- **Stuck on Java / setup?** Re-read `SETUP.md`. The #1 issue is Java 11 not installed or `JAVA_HOME` not set, followed by forgetting to restart the kernel after installing Java.

---

## What "good" looks like

A strong submission:
- Runs top to bottom with no errors when I press "Run All"
- Has an explicit schema, not inferred types
- Produces the same numbers in both Part 2 versions
- Includes the file-size comparison and shows Parquet winning
- Is clean enough that I can read it without hunting for the answer

Post questions in the course Slack — chances are someone else hit the same thing.

— Ameer
