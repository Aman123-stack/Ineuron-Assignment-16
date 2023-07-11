q1>from collections import defaultdict

def find_nearest_element_with_higher_frequency(arr):
    frequency = defaultdict(int)
    answer = [-1] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        current_element = arr[i]

        # Check if there is an element with a higher frequency
        for j in range(i + 1, len(arr)):
            if frequency[arr[j]] > frequency[current_element]:
                answer[i] = arr[j]
                break

        frequency[current_element] += 1

    return answer


q2>def sort_stack(stack):
    temp_stack = []

    while stack:
        temp = stack.pop()

        while temp_stack and temp_stack[-1] > temp:
            stack.append(temp_stack.pop())

        temp_stack.append(temp)

    return temp_stack



q3>def delete_middle(stack):
    if is_empty(stack):
        return

    size = len(stack)
    delete_middle_recursive(stack, size, 1)

def delete_middle_recursive(stack, size, position):
    if position == (size // 2) + 1:
        stack.pop()
        return

    temp = stack.pop()
    delete_middle_recursive(stack, size, position + 1)
    stack.append(temp)

def is_empty(stack):
    return len(stack) == 0



q4>from queue import Queue

def check_queue_arrangement(queue):
    stack = []
    other_queue = Queue()
    expected_number = 1

    while not queue.empty():
        front_element = queue.queue[0]

        if front_element == expected_number:
            other_queue.put(front_element)
            expected_number += 1
            queue.get()
        elif stack and stack[-1] == expected_number:
            stack.pop()
            expected_number += 1
        else:
            stack.append(front_element)
            queue.get()

    while stack:
        if stack.pop() != expected_number:
            return False
        expected_number += 1

    while not other_queue.empty():
        if other_queue.get() != expected_number:
            return False
        expected_number += 1

    return True


q5>def reverse_number(number):
    number_str = str(number)
    stack = []

    for digit in number_str:
        stack.append(digit)

    reversed_number_str = ""

    while stack:
        reversed_number_str += stack.pop()

    reversed_number = int(reversed_number_str)

    return reversed_number



q6>from queue import Queue

def reverse_k_elements(queue, k):
    stack = []

    # Dequeue and push the first k elements onto the stack
    for _ in range(k):
        stack.append(queue.get())

    new_queue = Queue()

    # Enqueue the elements from the stack into the new queue
    while stack:
        new_queue.put(stack.pop())

    # Enqueue the remaining elements from the original queue into the new queue
    while not queue.empty():
        new_queue.put(queue.get())

    return new_queue


q7>def count_remaining_words(sequence):
    words = sequence.split()
    stack = []

    for word in words:
        if stack and word == stack[-1]:
            stack.pop()
        else:
            stack.append(word)

    return len(stack)



q8>def find_max_absolute_difference(arr):
    n = len(arr)
    stack = []
    left_smaller = [0] * n
    right_smaller = [0] * n

    # Find the nearest smaller element on the right side
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            right_smaller[stack.pop()] = arr[i]
        stack.append(i)

    stack.clear()

    # Find the nearest smaller element on the left side
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            left_smaller[stack.pop()] = arr[i]
        stack.append(i)

    max_difference = 0

    # Calculate the maximum absolute difference
    for i in range(n):
        difference = abs(right_smaller[i] - left_smaller[i])
        max_difference = max(max_difference, difference)

    return max_difference
