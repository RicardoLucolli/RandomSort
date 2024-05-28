import random
import time

def generate_large_list(size):
    """Generate a large list of random integers."""
    return [random.randint(0, 1000000) for _ in range(size)]

def sort_large_list(lst):
    """Sort a large list of integers."""
    return sorted(lst)

def consume_memory_and_process():
    allocated_memory = []
    try:
        while True:
            # Generate a large list of 1 million integers (about 7.6 MB per list)
            large_list = generate_large_list(1_000_000)
            allocated_memory.append(large_list)
            
            # Sort the list to simulate intensive processing
            sorted_list = sort_large_list(large_list)
            allocated_memory.append(sorted_list)
            
            # Print the first 10 elements of the initial and sorted lists
            print(f"Initial list (first 10 elements): {large_list[:100]}")
            print(f"Sorted list (first 10 elements): {sorted_list[:100]}")
            
            print(f"Allocated and processed {len(allocated_memory) // 2} pairs of lists")
            # Pause for a short while to observe the behavior
            time.sleep(0.5)
    except MemoryError:
        print("MemoryError encountered: System is out of memory!")
    except KeyboardInterrupt:
        print("Memory consumption interrupted by user.")

if __name__ == "__main__":
    consume_memory_and_process()
