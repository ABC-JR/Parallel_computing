import threading
import time

counter = 0
INCREMENTS = 1_000_000
THREADS = 10
RUNS = 10


def increment_counter():
    global counter

    for _ in range(INCREMENTS):
        counter += 1


def run_without_lock():
    global counter

    counter = 0

    threads = []

    start = time.perf_counter()

    for _ in range(THREADS):
        thread = threading.Thread(target=increment_counter)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end = time.perf_counter()

    return counter, end - start


def main():
    expected = THREADS * INCREMENTS

    print("=" * 70)
    print("TASK 3 - RACE CONDITION WITHOUT LOCK")
    print("=" * 70)
    print(f"Threads: {THREADS}")
    print(f"Increments per thread: {INCREMENTS:,}")
    print(f"Expected counter: {expected:,}")
    print()

    results = []

    for run in range(1, RUNS + 1):
        counter_value, elapsed = run_without_lock()

        results.append((counter_value, elapsed))

        print(
            f"Run {run:2}: "
            f"Counter = {counter_value:,} | "
            f"Time = {elapsed:.4f} s"
        )

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)

    average_counter = sum(x[0] for x in results) / RUNS
    average_time = sum(x[1] for x in results) / RUNS

    print(f"Expected counter : {expected:,}")
    print(f"Average counter  : {average_counter:,.0f}")
    print(f"Average time     : {average_time:.4f} s")


if __name__ == "__main__":
    main()