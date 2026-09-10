# Lab Practicum 01 — Empirical Parallel Computing

## Overview

This repository contains the completed work for **Lab Practicum 01: Empirical Parallel Computing**.

The lab covers:

1. Host CPU / cache / SIMD audit and Flynn's Taxonomy
2. CPU scaling benchmark with different numbers of parallel workers
3. Shared-counter concurrency experiment with and without a Lock
4. Amdahl's Law and Gustafson's Law analysis

## Host System

- **CPU:** AMD Ryzen 7 7735HS with Radeon Graphics
- **Physical cores:** 8
- **Logical processors:** 16
- **Operating System:** Windows 11
- **Language:** Python
- **Parallelism:** `multiprocessing` and `threading`

## Files

- `main2.py` — Task 2 CPU benchmark
- `main3.py` — Task 3 shared counter without Lock
- `main3_1.py` — Task 3 shared counter with Lock
- `Parallel_Computing_Lab_Practicum_01_Completed.docx` — completed lab report

## Task 2 Results

The benchmark used a fixed total workload of **16,000,000 iterations**.

| Workers | Average Time | Speedup | Efficiency |
|---:|---:|---:|---:|
| 1 | 4.4213 s | 1.00x | 100.00% |
| 2 | 2.4706 s | 1.79x | 89.48% |
| 4 | 1.4070 s | 3.14x | 78.56% |
| 8 | 0.9406 s | 4.70x | 58.76% |
| 16 | 0.8536 s | 5.18x | 32.37% |
| 32 | 1.1160 s | 3.96x | 12.38% |

The best measured result was at **16 workers**, with a speedup of **5.18x**.

At 32 workers, performance decreased because the system has 16 logical processors, so 32 concurrent processes create oversubscription and additional scheduling overhead.

## Task 3 Results

Configuration:

- 10 threads
- 1,000,000 increments per thread
- Expected counter: 10,000,000
- 10 runs

### Without Lock

- Average counter: **10,000,000**
- Average time: **0.8125 s**

### With Lock

- Average counter: **10,000,000**
- Average time: **3.5027 s**

The Lock version was approximately **4.31x slower**.

A visible race condition was not observed in the 10 unlocked runs. The experiment nevertheless demonstrates the concept of a read-modify-write operation:

`Load -> Add -> Store`

A Lock protects the critical section but introduces synchronization overhead.

## Task 4 Results

Using the measured Task 2 values:

- `T1 = 4.4213 s`
- `T2 = 2.4706 s`

Estimated parallel fraction:

- **p = 0.8824 (88.24%)**

Amdahl's Law:

- **Maximum theoretical speedup = 8.50x**
- **Theoretical speedup at 64 cores = 7.61x**

Gustafson's Law:

- **64x scaled speedup = 56.59x**

## Important Note

All benchmark timings and counter results in the report were obtained by actually running the programs on the host machine.

Before submission, include the required **Task 2 screenshot** showing the benchmark running with active CPU/workers.

