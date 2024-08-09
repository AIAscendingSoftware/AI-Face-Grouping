import os
import sys
import time
import subprocess

def run_app():
    python_executable = sys.executable
    app_path = os.path.join(os.path.dirname(__file__), 'app.py')
    
    print("Starting Flask app...")
    process = subprocess.Popen([python_executable, app_path])
    
    try:
        while True:
            time.sleep(1)
            if process.poll() is not None:
                print("Flask app has stopped. Restarting...")
                run_app()
                break
    except KeyboardInterrupt:
        print("Stopping Flask app...")
        process.terminate()
        process.wait()
        sys.exit(0)

if __name__ == '__main__':
    while True:
        run_app()
        time.sleep(1)