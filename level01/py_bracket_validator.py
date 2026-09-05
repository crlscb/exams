from termcolor import colored

"""
Write a function that checks whether the brackets in a string are correctly
matched and nested.

It supports three types: (), [], {}.

The function must:
- Return True if all brackets are correctly matched
- Return True if the string contains no brackets
- Return False if any brackets are missing or incorrectly nested
- Ignore characters that are not brackets
"""


def bracket_validator(s: str) -> bool:
    stack = []

    pairs = {
        ']': '[',
        '}': '{',
        ')': '('
    }

    for char in s:
        if char in '[{(':
            stack.append(char)
        elif char in ']})':
            if not stack:
                return False
            if stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    tests = [
        "[hola]",
        "",
        "[]{}()",
        "hola",
        "h(o[l]{a})!",
        "[(hola)}]",
        "[hola",
        "[{hola]",
        "[hola]}",
        "hola]}",
        ")(",
        "((()))",
        "([{}])",
        "([)]",
        "((())",
        "())"
    ]

    print("--- Bracket Validator Tests ---\n")
    for test in tests:
        result = bracket_validator(test)

        if result:
            print(colored(f" {test:<15} -> ✅ {result}", "green"))
        else:
            print(colored(f" {test:<15} -> ❌ {result}", "red"))
