def is_palindrome(s):
    original_str = s
    reversed_str = reversed(s)

    if original_str == reversed_str:
        return True

    return False


def reversed(data):
    data = list(data)
    start = 0
    end = len(data) - 1

    while end > start:
        data[start], data[end] = data[end], data[start]
        start += 1
        end -= 1

    return "".join(data)


if __name__ == "__main__":
    print(is_palindrome("car"))
