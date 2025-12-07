from queue import LifoQueue


def is_symmetric(input_string: str) -> bool:
    stack = LifoQueue()
    opening_brackets = "({["
    closing_brackets = ")}]"
    matching_brackets = {")": "(", "}": "{", "]": "["}

    for char in input_string:
        if char in opening_brackets:
            stack.put(char)
        elif char in closing_brackets:
            if stack.empty() or stack.get() != matching_brackets[char]:
                return False

    return stack.empty()


def main():
    test_strings = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",
        "( 23 ( 2 - 3);",
        "( 11 }",
    ]

    for s in test_strings:
        result = is_symmetric(s)
        print(f"{s}: {'Симетрично' if result else 'Несиметрично'}")


if __name__ == "__main__":
    main()
