"""
HTTP Client Module
Makes concurrent requests to the web counter application
"""
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def make_request(session, url):
    """Make a single HTTP request using a session"""
    try:
        response = session.get(url, timeout=5)  # Reduced timeout to 5 seconds
        return response.status_code == 204 or response.status_code == 200
    except requests.exceptions.Timeout:
        print(f"\nRequest timeout after 5 seconds")
        return False
    except Exception as e:
        print(f"\nRequest failed: {e}")
        return False


def make_requests_sequential(base_url, num_requests, progress_callback=None):
    """Make requests sequentially from a single client"""
    url = f"{base_url}/inc"
    start_time = time.time()
    
    # Use session for connection pooling with keep-alive
    with requests.Session() as session:
        # Simple configuration - let requests handle connection pooling
        session.headers.update({'Connection': 'keep-alive'})
        
        for i in range(num_requests):
            make_request(session, url)
            if progress_callback and (i + 1) % 1000 == 0:
                progress_callback(i + 1, num_requests)
    
    end_time = time.time()
    return end_time - start_time


def make_requests_parallel(base_url, num_requests, num_clients, progress_callback=None):
    """
    Make requests in parallel using multiple clients
    Each client makes (num_requests) requests
    """
    url = f"{base_url}/inc"
    completed_count = [0]  # Use list to allow modification in nested function
    lock = __import__('threading').Lock()
    
    start_time = time.time()
    
    def client_worker(client_id, num_reqs):
        """Each client uses its own session"""
        with requests.Session() as session:
            # Simple configuration - let requests handle connection pooling
            session.headers.update({'Connection': 'keep-alive'})
            
            for i in range(num_reqs):
                make_request(session, url)
                if progress_callback:
                    with lock:
                        completed_count[0] += 1
                        if completed_count[0] % 1000 == 0:
                            progress_callback(completed_count[0], num_clients * num_reqs)
    
    # Use ThreadPoolExecutor to simulate multiple clients
    with ThreadPoolExecutor(max_workers=num_clients) as executor:
        futures = [executor.submit(client_worker, i, num_requests) for i in range(num_clients)]
        
        # Wait for all clients to complete
        for future in as_completed(futures):
            future.result()
    
    end_time = time.time()
    return end_time - start_time


def get_count(base_url):
    """Get the current counter value"""
    try:
        response = requests.get(f"{base_url}/count", timeout=5)
        if response.status_code == 200:
            return response.json()['count']
    except Exception as e:
        print(f"Failed to get count: {e}")
    return None


def reset_counter(base_url):
    """Reset the counter to 0"""
    try:
        response = requests.post(f"{base_url}/reset", timeout=5)
        return response.status_code == 204
    except Exception as e:
        print(f"Failed to reset counter: {e}")
        return False
