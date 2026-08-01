# Python Fluent Practice Project — DataOps Event Processing Lab

Goal:
Build a realistic mini data engineering project while learning selected parts of Fluent Python.

This project is intentionally:

* smaller than your major platform projects
* Python-heavy
* focused on clean engineering patterns
* aligned with ETL/DataOps/backend thinking
* compatible with Fluent Python chapters

You should NOT look at solutions immediately.

Workflow:

1. Read assigned Fluent Python section
2. Complete assignment
3. Test manually
4. Refactor
5. Only then check solution

---

# Project Overview

You are building:

"EventFlow"

A lightweight event processing system.

The system ingests:

* website events
* purchases
* logins
* errors
* support actions

Then:

* validates data
* transforms records
* aggregates metrics
* exports reports
* tracks pipeline execution

You will gradually evolve this into:

* generator pipelines
* typed codebase
* decorator-driven system
* mini orchestration framework

---

# Tech Constraints

Use only:

* Python standard library initially
* later:

  * pandas (minimal)
  * typing
  * dataclasses

Avoid frameworks.

The purpose is Python fluency.

---

# Folder Structure

Create:

```text
project/
│
├── data/
├── src/
│   ├── ingestion/
│   ├── processing/
│   ├── models/
│   ├── utils/
│   └── reports/
│
├── tests/
└── README.md
```

---

# Dataset

Create file:

```text
data/events.csv
```

Dataset:

```csv
event_id,user_id,event_type,source,country,device,revenue,timestamp
1,u001,page_view,web,US,mobile,0,2026-01-01T10:00:00
2,u002,purchase,web,DE,desktop,120,2026-01-01T10:03:00
3,u003,signup,ads,FR,mobile,0,2026-01-01T10:05:00
4,u001,purchase,web,US,mobile,75,2026-01-01T10:06:00
5,u004,error,api,IN,desktop,0,2026-01-01T10:10:00
6,u002,page_view,email,DE,tablet,0,2026-01-01T10:12:00
7,u005,purchase,ads,US,mobile,210,2026-01-01T10:15:00
8,u006,login,web,GB,desktop,0,2026-01-01T10:17:00
9,u003,purchase,email,FR,mobile,95,2026-01-01T10:20:00
10,u007,error,api,US,desktop,0,2026-01-01T10:25:00
11,u001,page_view,web,US,mobile,0,2026-01-01T10:30:00
12,u008,signup,ads,CA,tablet,0,2026-01-01T10:31:00
13,u009,purchase,web,JP,desktop,330,2026-01-01T10:35:00
14,u010,login,email,BR,mobile,0,2026-01-01T10:37:00
15,u011,purchase,web,US,tablet,60,2026-01-01T10:40:00
16,u004,error,api,IN,mobile,0,2026-01-01T10:42:00
17,u012,page_view,ads,DE,mobile,0,2026-01-01T10:45:00
18,u013,purchase,web,GB,desktop,180,2026-01-01T10:50:00
19,u014,signup,email,US,mobile,0,2026-01-01T10:52:00
20,u015,purchase,ads,CA,desktop,240,2026-01-01T10:55:00
```

---

# PHASE 1 — Pythonic Foundations

---

# STEP 1 — DataBatch Class

Fluent Python:

* Chapter 1
* Data model basics

---

# Assignment

Create:

```python
class DataBatch:
```

Requirements:

* stores event records internally
* supports:

  * iteration
  * indexing
  * slicing
  * len()
  * readable repr

Usage:

```python
batch = DataBatch(records)

len(batch)
batch[0]

for row in batch:
    print(row)
```

---

# Extra Tasks

Implement:

```python
if batch:
```

Truthy only if records exist.

---

# DO NOT CONTINUE UNTIL

You understand:

* **len**
* **iter**
* **getitem**
* **repr**
* **bool**

---

# SOLUTION — STEP 1

```python
class DataBatch:
    def __init__(self, records):
        self.records = records

    def __len__(self):
        return len(self.records)

    def __iter__(self):
        return iter(self.records)

    def __getitem__(self, item):
        return self.records[item]

    def __repr__(self):
        return f"DataBatch(records={len(self.records)})"

    def __bool__(self):
        return bool(self.records)
```

---

# STEP 2 — CSV Loader

Fluent Python:

* sequences
* comprehensions
* unpacking

---

# Assignment

Create:

```python
load_events(path)
```

Requirements:

* read CSV
* return list of dictionaries
* convert revenue to int
* preserve timestamps as strings initially

Restrictions:

* use csv module
* no pandas

---

# Extra Tasks

1. Remove rows where event_type == "error"
2. Return only purchases
3. Return top 3 purchases by revenue

---

# SOLUTION — STEP 2

```python
import csv


def load_events(path):
    with open(path, newline="") as file:
        reader = csv.DictReader(file)

        rows = [
            {
                **row,
                "revenue": int(row["revenue"])
            }
            for row in reader
        ]

    return rows
```

---

# STEP 3 — Aggregation Engine

Fluent Python:

* dicts
* defaultdict
* Counter
* sets

---

# Assignment

Build metrics:

1. events per country
2. revenue per country
3. purchases per device
4. unique users count
5. top revenue countries

---

# Constraints

Use:

* defaultdict
* Counter
* set operations

---

# Extra Challenge

Find:

* users that purchased more than once
* countries with zero purchases

---

# SOLUTION — STEP 3

```python
from collections import defaultdict, Counter


def revenue_per_country(events):
    revenue = defaultdict(int)

    for event in events:
        revenue[event["country"]] += event["revenue"]

    return dict(revenue)
```

---

# STEP 4 — Dataclasses

Fluent Python:

* dataclasses
* immutability
* mutability traps

---

# Assignment

Create:

```python
@dataclass(frozen=True)
class Event:
```

Fields:

* event_id
* user_id
* event_type
* source
* country
* device
* revenue
* timestamp

---

# Extra Tasks

1. Convert CSV dictionaries into Event objects
2. Sort events by revenue
3. Group by event_type

---

# Critical Exercise

Create intentionally broken code:

```python
def add_event(event, events=[]):
```

Explain WHY it breaks.

Fix it.

---

# SOLUTION — STEP 4

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    event_id: int
    user_id: str
    event_type: str
    source: str
    country: str
    device: str
    revenue: int
    timestamp: str
```

---

# STEP 5 — Functional Pipeline

Fluent Python:

* functions as objects
* higher-order functions
* partial
* callable patterns

---

# Assignment

Build:

```python
pipeline = [
    clean_events,
    validate_events,
    enrich_events,
]
```

Create executor:

```python
run_pipeline(events, pipeline)
```

---

# Extra Tasks

1. Add retry wrapper
2. Add execution logging
3. Add runtime measurement

---

# SOLUTION — STEP 5

```python
def run_pipeline(data, steps):
    for step in steps:
        data = step(data)

    return data
```

---

# STEP 6 — Type Hints

Fluent Python:

* practical typing
* Callable
* TypedDict
* generics basics

---

# Assignment

Add type hints everywhere.

Especially:

```python
list[dict[str, str]]
Callable
```

---

# Extra Tasks

Run:

```bash
mypy src/
```

Fix all typing issues.

---

# SOLUTION — STEP 6

```python
from typing import Callable


def run_pipeline(
    data: list[dict],
    steps: list[Callable]
) -> list[dict]:
    for step in steps:
        data = step(data)

    return data
```

---

# PHASE 2 — Production Python

---

# STEP 7 — Decorators

Fluent Python:

* decorators
* closures
* wrappers

---

# Assignment

Build decorators:

1. @timer
2. @retry
3. @log_execution

Apply to pipeline steps.

---

# Extra Challenge

Track:

* runtime
* retries
* failures
* row counts

---

# SOLUTION — STEP 7

```python
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"{func.__name__}: {end-start:.2f}s")

        return result

    return wrapper
```

---

# STEP 8 — Generators

Fluent Python:

* generators
* lazy evaluation
* iterator pipelines

---

# Assignment

Rewrite CSV loader lazily.

Requirements:

* yield one row at a time
* avoid loading entire file into memory

---

# Extra Tasks

Build lazy pipeline:

```text
read -> filter -> enrich -> aggregate
```

All generator-based.

---

# SOLUTION — STEP 8

```python
import csv


def stream_events(path):
    with open(path, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["revenue"] = int(row["revenue"])
            yield row
```

---

# STEP 9 — Context Managers

Fluent Python:

* with statement
* resource management

---

# Assignment

Build:

```python
with PipelineLogger():
```

Requirements:

* open log file
* write execution metadata
* close automatically

---

# Extra Tasks

Create:

```python
with Timer():
```

Measure block runtime.

---

# SOLUTION — STEP 9

```python
class PipelineLogger:
    def __enter__(self):
        self.file = open("pipeline.log", "a")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
```

---

# FINAL PROJECT

Build:

Mini DataOps Event Platform.

---

# Final Requirements

System must:

* ingest CSV
* validate rows
* filter bad events
* aggregate metrics
* export report
* use dataclasses
* use generators
* use decorators
* use type hints
* use context managers
* produce logs

---

# FINAL CHALLENGES

---

# Challenge 1 — Parallel Processing

Use:

```python
concurrent.futures
```

Process event batches concurrently.

---

# Challenge 2 — SQLite Export

Export metrics into SQLite.

Use:

```python
sqlite3
```

---

# Challenge 3 — JSON Config

Load pipeline config from JSON.

---

# Challenge 4 — Mini Airflow-lite

Build:

```python
@task
```

Store task metadata.

Create dependency graph.

---

# Challenge 5 — Streaming Mode

Simulate real-time events.

Use generators.

---

# HOW TO STUDY CORRECTLY

For every step:

1. Read Fluent Python section
2. Build from scratch
3. Refactor once
4. Compare with solution
5. Improve solution
6. Integrate into bigger projects later

---

# TARGET OUTCOME

After finishing this project, you should comfortably understand:

* Pythonic iteration
* generators
* dataclasses
* decorators
* context managers
* lazy pipelines
* typed code
* functional composition
* memory-efficient ETL
* reusable engineering patterns

This creates a strong foundation for:

* Airflow
* dbt Python models
* Spark jobs
* backend ETL services
* orchestration tooling
* data platform engineering
