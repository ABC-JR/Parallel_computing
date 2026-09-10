import time
import math
from concurrent.futures import ThreadPoolExecutor


# Amount of CPU work for each thread
WORK = 2_000_000


def cpu_work(n):
    total = 0.0

    for i in range(WORK):
        total += math.sqrt(i + 1) * math.sin(i + 1)

    return total


def run_benchmark(threads):
    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []

        for _ in range(threads):
            futures.append(executor.submit(cpu_work, threads))

        for future in futures:
            future.result()

    end = time.perf_counter()

    return end - start


def main():
    thread_counts = [1, 2, 4, 8, 16, 32]

    results = {}

    print("=" * 60)
    print("TASK 2 - MULTI-THREAD CPU BENCHMARK")
    print("CPU: AMD Ryzen 7 7735HS")
    print("=" * 60)

    for threads in thread_counts:
        print(f"\nThreads: {threads}")

        times = []

        for run in range(1, 4):
            elapsed = run_benchmark(threads)
            times.append(elapsed)

            print(f"Run {run}: {elapsed:.4f} seconds")

        average = sum(times) / len(times)
        results[threads] = average

        print(f"Average: {average:.4f} seconds")

    # T1 is our baseline
    t1 = results[1]

    print("\n" + "=" * 75)
    print("FINAL RESULTS")
    print("=" * 75)

    print(
        f"{'Threads':<10}"
        f"{'Average(s)':<15}"
        f"{'Speedup':<15}"
        f"{'Efficiency':<15}"
    )

    print("-" * 75)

    for threads in thread_counts:
        average = results[threads]

        speedup = t1 / average
        efficiency = speedup / threads

        print(
            f"{threads:<10}"
            f"{average:<15.4f}"
            f"{speedup:<15.2f}"
            f"{efficiency * 100:<15.2f}%"
        )


if __name__ == "__main__":
    main()