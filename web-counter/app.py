"""
Web Counter Application with Production Server
Uses Waitress for Windows compatibility and high performance
"""
from flask import Flask, jsonify
import threading

app = Flask(__name__)

# Thread-safe counter
counter = 0
counter_lock = threading.Lock()


@app.route('/')
def home():
    """Home page to verify server is running"""
    with counter_lock:
        current_count = counter
    return jsonify({
        'status': 'running',
        'message': 'Web Counter Application is running!',
        'current_count': current_count,
        'endpoints': {
            '/inc': 'Increment counter (GET/POST)',
            '/count': 'Get current count (GET)',
            '/reset': 'Reset counter to 0 (POST)'
        }
    })


@app.route('/inc', methods=['GET', 'POST'])
def increment():
    """Increment the counter by 1"""
    global counter
    with counter_lock:
        counter += 1
    return '', 204  # No content response for faster processing


@app.route('/count', methods=['GET'])
def get_count():
    """Get the current counter value"""
    with counter_lock:
        current_count = counter
    return jsonify({'count': current_count})


@app.route('/reset', methods=['POST'])
def reset():
    """Reset the counter to 0"""
    global counter
    with counter_lock:
        counter = 0
    return '', 204


if __name__ == '__main__':
    print("=" * 60)
    print("Starting Web Counter Application")
    print("=" * 60)
    print("URL: http://127.0.0.1:8080")
    print("=" * 60)
    
    try:
        from waitress import serve
        print("Server: Waitress (Production WSGI Server)")
        print("Threads: 100")
        print("\nServer is ready to accept connections!")
        print("Test: Open http://127.0.0.1:8080 in your browser")
        print("Press Ctrl+C to stop\n")
        
        # Serve with waitress
        serve(
            app,
            host='0.0.0.0',
            port=8080,
            threads=100,
            channel_timeout=30
        )
    except ImportError:
        print("Server: Flask (Development - Install waitress for better performance)")
        print("\nServer is ready to accept connections!")
        print("Test: Open http://127.0.0.1:8080 in your browser")
        print("Press Ctrl+C to stop\n")
        app.run(host='0.0.0.0', port=8080, threaded=True, debug=False)
    except KeyboardInterrupt:
        print("\n\nServer stopped by user")
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
