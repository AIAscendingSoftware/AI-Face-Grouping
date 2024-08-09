import queue
import threading
from concurrent.futures import ThreadPoolExecutor

task_queue = queue.Queue()
worker_pool = None

def init_task_queue(app):
    global worker_pool
    max_workers = app.config.get('MAX_WORKERS', 4)
    worker_pool = ThreadPoolExecutor(max_workers=max_workers)
    for _ in range(max_workers):
        worker_pool.submit(worker, app)

def add_task(func, *args, **kwargs):
    task_queue.put((func, args, kwargs))

def worker(app):
    while True:
        func, args, kwargs = task_queue.get()
        try:
            with app.app_context():
                func(*args, **kwargs)
        except Exception as e:
            print(f"Error processing task: {e}")
        finally:
            task_queue.task_done()