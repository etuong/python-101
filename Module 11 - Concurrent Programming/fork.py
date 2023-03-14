from threading import Lock


class Fork:
    def __init__(self):
        # Add a lock as an instance variable
        self.lock = Lock()

    def acquire_fork(self):
        # Return True if you can acquire self.lock, False otherwise
        return self.lock.acquire()

    def release_fork(self):
        # Release lock
        self.lock.release()
