# Perl vs. FastAPI Benchmark

This repository contains a demo application for benchmarking a Perl endpoint using the Dancer web framework against a Python endpoint using FastAPI.

## Prerequisites

- Perl with Dancer framework
- Python 3.7+ with FastAPI and Uvicorn server
- `requests` library for Python
- `time` library for Python
- `concurrent.futures` library for Python

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/perl-fastapi-benchmark.git
cd perl-fastapi-benchmark
```

### install dependencies

```bash
pip install -r requirements.txt
```

## Running 

In one terminal, run `perl app.pl`

In another terminal, run `uvicorn app:app --host 0.0.0.0 --port 8000`

In a third terminal, run the benchmark script `python benchmark.py`

The benchmark script will output the average response time and throughput for each endpoint, allowing you to compare the performance of the Perl endpoint using Dancer against the Python endpoint using FastAPI.