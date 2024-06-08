from flask import Flask, jsonify, request
import requests
import time
import threading

app = Flask(__name__)
WINDOW_SIZE = 10
THIRD_PARTY_API_URL = 'http://20.244.56.144/numbers'
QUALIFIED_IDS = ['p', 'f', 'e', 'r']
window = []
lock = threading.Lock()

def fetch_numbers(number_id):
    try:
        response = requests.get(f"{THIRD_PARTY_API_URL}/{number_id}", timeout=0.5)
        if response.status_code == 200:
            return response.json().get('numbers', [])
    except (requests.RequestException, requests.Timeout):
        pass
    return []

@app.route('/numbers/<string:number_id>', methods=['GET'])
def get_numbers(number_id):
    start_time = time.time()

    if number_id not in QUALIFIED_IDS:
        return jsonify({"error": "Invalid number ID"}), 400

    # fetch numbers from the third party API
    numbers = fetch_numbers(number_id)

    if not numbers:
        return jsonify({"error": "Failed to fetch numbers"}), 500

    with lock:
        prev_state = list(window)
        # adding new unique numbers to the window
        for num in numbers:
            if num not in window:
                if len(window) >= WINDOW_SIZE:
                    window.pop(0)
                window.append(num)

        curr_state = list(window)

    # calculation of average of the numbers in the window
    avg = sum(window) / len(window) if window else 0

    # response time
    elapsed_time = time.time() - start_time
    if elapsed_time >= 0.5:
        return jsonify({"error": "Request timed out"}), 500

    return jsonify({
        "windowPrevState": prev_state,
        "windowCurrState": curr_state,
        "numbers": numbers,
        "avg": round(avg, 2)
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9876)
