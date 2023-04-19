import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

PERL_URL = "http://localhost:3000/hello"
PYTHON_URL = "http://localhost:8000/hello"
NUM_REQUESTS = 1000
NUM_WORKERS = 50


def make_request(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    return end_time - start_time


def benchmark(url, num_requests, num_workers):
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = [executor.submit(make_request, url)
                   for _ in range(num_requests)]

        total_time = 0
        for future in as_completed(futures):
            total_time += future.result()

    return total_time / num_requests, num_requests / total_time


if __name__ == "__main__":
    perl_avg_time, perl_throughput = benchmark(
        PERL_URL, NUM_REQUESTS, NUM_WORKERS)
    python_avg_time, python_throughput = benchmark(
        PYTHON_URL, NUM_REQUESTS, NUM_WORKERS)

    print(
        f"Perl (Dancer) Endpoint: Average Response Time: {perl_avg_time:.4f}s, Throughput: {perl_throughput:.2f} req/s")
    print(
        f"Python (FastAPI) Endpoint: Average Response Time: {python_avg_time:.4f}s, Throughput: {python_throughput:.2f} req/s")
