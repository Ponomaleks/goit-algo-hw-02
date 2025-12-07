from collections import deque


def is_palindrome(input_string: str) -> bool:
    normalized_str = "".join(input_string.lower().split())
    deq = deque(normalized_str)

    while len(deq) > 1:
        if deq.pop() != deq.popleft():
            return False
    return True
