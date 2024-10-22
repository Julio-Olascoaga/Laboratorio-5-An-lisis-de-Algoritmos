import heapq
import random

def generate_random_lists(k, max_length, value_range):
    lists = []
    for _ in range(k):
        length = random.randint(0, max_length)
        random_list = sorted(random.randint(value_range[0], value_range[1]) for _ in range(length))
        lists.append(random_list)
    return lists

def mergeKLists(lists):
    merged_list = []
    heap = []
    
    for i in range(len(lists)):
        for num in lists[i]:
            heapq.heappush(heap, num)
    
    while heap:
        merged_list.append(heapq.heappop(heap))
    
    return merged_list

k = 3
max_length = 10
value_range = (0, 50)

random_lists = generate_random_lists(k, max_length, value_range)
print("Listas generadas:", random_lists)
print("Lista fusionada:", mergeKLists(random_lists))
