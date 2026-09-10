import time
import math
import multiprocessing

TOTAL_WORK = 16_000_000


def cpu_work(iterations):
    total = 0.0

    for i in range(iterations):
        total += math.sqrt(i + 1) * math.sin(i + 1)

    return total


def run_benchmark(processes):
    base = TOTAL_WORK // processes
    remainder = TOTAL_WORK % processes

    chunks = []

    for i in range(processes):
        if i < remainder:
            chunks.append(base + 1)
        else:
            chunks.append(base)

    start = time.perf_counter()

    with multiprocessing.Pool(processes=processes) as pool:
        pool.map(cpu_work, chunks)

    end = time.perf_counter()

    return end - start


def main():
    process_counts = [1, 2, 4, 8, 16, 32]

    results = {}

    print("=" * 75)
    print("TASK 2 - CPU BENCHMARK")
    print("CPU: AMD Ryzen 7 7735HS")
    print(f"Total work: {TOTAL_WORK:,}")
    print("=" * 75)

    for processes in process_counts:

        print(f"\nThreads/Processes: {processes}")

        times = []

        for run in range(1, 4):
            elapsed = run_benchmark(processes)
            times.append(elapsed)

            print(f"Run {run}: {elapsed:.4f} seconds")

        average = sum(times) / len(times)

        results[processes] = average

        print(f"Average: {average:.4f} seconds")

    t1 = results[1]

    print("\n" + "=" * 80)
    print("FINAL RESULTS")
    print("=" * 80)

    print(
        f"{'N':<8}"
        f"{'Average(s)':<15}"
        f"{'Speedup':<15}"
        f"{'Efficiency':<15}"
    )

    print("-" * 80)

    for processes in process_counts:

        average = results[processes]

        speedup = t1 / average

        efficiency = speedup / processes

        print(
            f"{processes:<8}"
            f"{average:<15.4f}"
            f"{speedup:<15.2f}"
            f"{efficiency * 100:<15.2f}%"
        )


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()