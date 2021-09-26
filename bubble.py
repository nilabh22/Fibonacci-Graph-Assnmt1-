import time
import random

start = time.time()
def bubble_sort(list_data: list, length: int = 0) -> list:
    length = length or len(list_data)
    swapped = False
    for i in range(length - 1):
        if list_data[i] > list_data[i + 1]:
            list_data[i], list_data[i + 1] = list_data[i + 1], list_data[i]
            swapped = True

    return list_data if not swapped else bubble_sort(list_data, length - 1)


list_data = list(range(1,1001))
random.shuffle(list_data)
print(list_data)

end = time.time()
print(bubble_sort(list_data))
runtime = (end-start)
print("Runtime for bubbleSort: ",runtime)