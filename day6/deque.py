from collections import deque

dq=deque([1, 2, 3, 4, 5])

dq.append(6)  # Add to the right
dq.appendleft(0)  # Add to the left

print("Deque after appending:", dq)
