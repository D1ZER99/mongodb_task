"""
Test Script for Web Counter Application
Tests all 4 scenarios and saves results to task01_part01_results.txt
"""
import time
from client import make_requests_sequential, make_requests_parallel, get_count, reset_counter


BASE_URL = "http://127.0.0.1:8080"  # Use IP instead of localhost for speed
REQUESTS_PER_CLIENT = 10000


def progress_tracker(completed, total):
    """Print progress updates"""
    percentage = (completed / total) * 100
    print(f"Progress: {completed}/{total} ({percentage:.1f}%) - {completed} requests completed", end='\r')


def run_scenario_1():
    """Scenario 1: One client makes 10K calls in sequence"""
    print("\n" + "="*60)
    print("Scenario 1: One client, 10K sequential requests")
    print("="*60)
    
    reset_counter(BASE_URL)
    time.sleep(0.5)  # Brief pause to ensure reset
    
    print("Running requests...")
    elapsed_time = make_requests_sequential(BASE_URL, REQUESTS_PER_CLIENT, progress_callback=progress_tracker)
    print()  # New line after progress
    
    final_count = get_count(BASE_URL)
    requests_per_second = REQUESTS_PER_CLIENT / elapsed_time
    
    print(f"Total requests: {REQUESTS_PER_CLIENT}")
    print(f"Final count: {final_count}")
    print(f"Time elapsed: {elapsed_time:.2f} seconds")
    print(f"Requests per second: {requests_per_second:.2f}")
    
    return {
        'scenario': 1,
        'clients': 1,
        'requests_per_client': REQUESTS_PER_CLIENT,
        'total_requests': REQUESTS_PER_CLIENT,
        'final_count': final_count,
        'time': elapsed_time,
        'requests_per_second': requests_per_second
    }


def run_scenario_2():
    """Scenario 2: Two clients simultaneously make 10K calls each"""
    print("\n" + "="*60)
    print("Scenario 2: Two clients, 10K requests each (20K total)")
    print("="*60)
    
    reset_counter(BASE_URL)
    time.sleep(0.5)
    
    num_clients = 2
    total_requests = num_clients * REQUESTS_PER_CLIENT
    
    print("Running requests with 2 concurrent clients...")
    elapsed_time = make_requests_parallel(BASE_URL, REQUESTS_PER_CLIENT, num_clients, progress_callback=progress_tracker)
    print()  # New line after progress
    
    final_count = get_count(BASE_URL)
    requests_per_second = total_requests / elapsed_time
    
    print(f"Total requests: {total_requests}")
    print(f"Final count: {final_count}")
    print(f"Time elapsed: {elapsed_time:.2f} seconds")
    print(f"Requests per second: {requests_per_second:.2f}")
    
    return {
        'scenario': 2,
        'clients': num_clients,
        'requests_per_client': REQUESTS_PER_CLIENT,
        'total_requests': total_requests,
        'final_count': final_count,
        'time': elapsed_time,
        'requests_per_second': requests_per_second
    }


def run_scenario_3():
    """Scenario 3: Five clients simultaneously make 10K calls each"""
    print("\n" + "="*60)
    print("Scenario 3: Five clients, 10K requests each (50K total)")
    print("="*60)
    
    reset_counter(BASE_URL)
    time.sleep(0.5)
    
    num_clients = 5
    total_requests = num_clients * REQUESTS_PER_CLIENT
    
    print("Running requests with 5 concurrent clients...")
    elapsed_time = make_requests_parallel(BASE_URL, REQUESTS_PER_CLIENT, num_clients, progress_callback=progress_tracker)
    print()  # New line after progress
    
    final_count = get_count(BASE_URL)
    requests_per_second = total_requests / elapsed_time
    
    print(f"Total requests: {total_requests}")
    print(f"Final count: {final_count}")
    print(f"Time elapsed: {elapsed_time:.2f} seconds")
    print(f"Requests per second: {requests_per_second:.2f}")
    
    return {
        'scenario': 3,
        'clients': num_clients,
        'requests_per_client': REQUESTS_PER_CLIENT,
        'total_requests': total_requests,
        'final_count': final_count,
        'time': elapsed_time,
        'requests_per_second': requests_per_second
    }


def run_scenario_4():
    """Scenario 4: Ten clients simultaneously make 10K calls each"""
    print("\n" + "="*60)
    print("Scenario 4: Ten clients, 10K requests each (100K total)")
    print("="*60)
    
    reset_counter(BASE_URL)
    time.sleep(0.5)
    
    num_clients = 10
    total_requests = num_clients * REQUESTS_PER_CLIENT
    
    print("Running requests with 10 concurrent clients...")
    elapsed_time = make_requests_parallel(BASE_URL, REQUESTS_PER_CLIENT, num_clients, progress_callback=progress_tracker)
    print()  # New line after progress
    
    final_count = get_count(BASE_URL)
    requests_per_second = total_requests / elapsed_time
    
    print(f"Total requests: {total_requests}")
    print(f"Final count: {final_count}")
    print(f"Time elapsed: {elapsed_time:.2f} seconds")
    print(f"Requests per second: {requests_per_second:.2f}")
    
    return {
        'scenario': 4,
        'clients': num_clients,
        'requests_per_client': REQUESTS_PER_CLIENT,
        'total_requests': total_requests,
        'final_count': final_count,
        'time': elapsed_time,
        'requests_per_second': requests_per_second
    }


def save_results(results):
    """Save results to task01_part01_results.txt"""
    with open('task01_part01_results.txt', 'w') as f:
        f.write("Web Counter Application - Performance Test Results\n")
        f.write("="*60 + "\n")
        f.write("Part I: Counter in RAM\n")
        f.write("="*60 + "\n\n")
        
        for result in results:
            f.write(f"Scenario {result['scenario']}:\n")
            f.write(f"  Number of clients: {result['clients']}\n")
            f.write(f"  Requests per client: {result['requests_per_client']}\n")
            f.write(f"  Total requests: {result['total_requests']}\n")
            f.write(f"  Final count: {result['final_count']}\n")
            f.write(f"  Time elapsed: {result['time']:.2f} seconds\n")
            f.write(f"  Requests per second: {result['requests_per_second']:.2f}\n")
            f.write("\n")
        
        f.write("-"*60 + "\n")
        f.write("Summary:\n")
        f.write("-"*60 + "\n")
        for result in results:
            f.write(f"Scenario {result['scenario']}: {result['requests_per_second']:.2f} requests/second\n")


def main():
    print("\n" + "="*60)
    print("Web Counter Application - Performance Testing")
    print("="*60)
    print("\nMake sure the web application is running on http://127.0.0.1:8080")
    print("Start the server with: python server.py")
    print("\nPress Enter to continue or Ctrl+C to cancel...")
    input()
    
    # Verify server is running
    try:
        count = get_count(BASE_URL)
        print(f"Server is running. Current count: {count}")
    except Exception as e:
        print(f"ERROR: Cannot connect to server at {BASE_URL}")
        print(f"Error: {e}")
        print("Please start the server first with: python app.py")
        return
    
    results = []
    
    # Run all scenarios
    results.append(run_scenario_1())
    results.append(run_scenario_2())
    results.append(run_scenario_3())
    results.append(run_scenario_4())
    
    # Save results
    save_results(results)
    
    print("\n" + "="*60)
    print("Testing Complete!")
    print("="*60)
    print("\nResults saved to: task01_part01_results.txt")
    print("\nSummary:")
    print("-"*60)
    for result in results:
        print(f"Scenario {result['scenario']}: {result['requests_per_second']:.2f} requests/second")


if __name__ == '__main__':
    main()
