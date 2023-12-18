import threading
import time

class Watchdog:
    def __init__(self, timeout_seconds):
        self.timeout_seconds = timeout_seconds
        self.timeout_occurred = False

    def start(self):
        timer_thread = threading.Thread(target=self._timer)
        timer_thread.start()

    def _timer(self):
        time.sleep(self.timeout_seconds)
        self.timeout_occurred = True

    def check_timeout(self):
        return self.timeout_occurred