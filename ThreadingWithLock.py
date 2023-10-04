import threading

# Shared resource
counter = 0

# Create a lock
lock = threading.Lock()

# Function to increment the counter
def increment_counter():
    global counter
    for _ in range(1000000):
        lock.acquire()
        try:
            counter += 1
        finally:
            lock.release()

# Create two threads to increment the counter
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

# Print the final counter value
print("Final counter value:", counter)
