import random
import threading
import time

from fork import Fork


class Philosopher(threading.Thread):
    running = True

    # Initialize a Philosophers name, left fork, and right fork
    def __init__(self, name: str, left_fork: Fork, right_fork: Fork):
        # call ‘threading’ superclass constructor
        super().__init__()

        # initialize ‘name’ instance variable
        self.name = name

        # initialize ‘left_fork’ instance variable
        self.left_fork = left_fork

        # initialize ‘right_fork’ instance variable
        self.right_fork = right_fork

    # run() is called by thread’s start() method; starts the thread running
    def run(self):
        while self.running:
            # Call think()
            self.think()

            # Call eat()
            self.eat()

            # Print <Philosopher name> is cleaning up.
            print(f"{self.name} is cleaning up")

    # Make philosopher think for a random number of seconds until hungry
    def think(self):
        # ‘thinking’ = random number of seconds between 3 and 5 using random.uniform()
        sleep_duration = random.uniform(3, 5)

        # Print <Philosopher name> is thinking for ‘thinking’ seconds.
        print(f"{self.name} is thinking for {sleep_duration} seconds")

        # Sleep for ‘thinking’ seconds
        time.sleep(sleep_duration)

        # Print <Philosopher name> is now hungry.
        print(f"{self.name} is now hungry")

    # Make philosopher eat for a random number of seconds until thinking again
    def eat(self):
        # Try to acquire left fork
        if self.left_fork.acquire_fork():
            # If successful, try to acquire right fork
            if self.right_fork.acquire_fork():
                # ‘eating’ = random num of seconds between 3 and 5 using random.uniform()
                eat_duration = random.uniform(3, 5)

                # Print <Philosopher name> is eating for ‘eating’ seconds.
                print(f"{self.name} is eating for {eat_duration} seconds")

                # Sleep for ‘eating’ seconds
                time.sleep(eat_duration)

                # Release right fork
                self.right_fork.release_fork()

                # Print <Philosopher name> has put down his right fork.
                print(f"{self.name} has put down his right fork")

            # Release left fork
            self.left_fork.release_fork()

            # print <Philosopher name> has put down his left fork.
            print(f"{self.name} has put down his left fork")

        else:
            return
