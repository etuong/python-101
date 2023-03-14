import time

from fork import Fork
from philosopher import Philosopher


def DiningPhilosophers():
    # Create array of 5 names: Plato, Aristotle, Buddha, Marx, and Nietzsche
    philosopher_names = ["Plato", "Aristotle", "Buddha", "Marx", "Nietzsche"]
    n = len(philosopher_names)

    # Use a list comprehension to create 5 Fork’s
    forks = [Fork() for i in range(n)]

    # Use a list comprehension to create 5 Philosopher’s and correctly assign each pair of forks to each philosopher
    philosophers = [Philosopher(philosopher_names[i], forks[i], forks[(i + 1) % n]) for i in range(n)]

    # Start all 5 Philosopher threads (should be non-blocking)
    for philosopher in philosophers:
        philosopher.start()

    # Sleep for 10 seconds
    time.sleep(10)

    # Set ‘running’ to False
    for philosopher in philosophers:
        philosopher.running = False

    # Exit all threads
    for philosopher in philosophers:
        philosopher.join()


if __name__ == "__main__":
    DiningPhilosophers()
