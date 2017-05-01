def collatz(n):
    " Find collatz sequence starting at n. "
    path = []
    while n != 1:
        path.append(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
    path.append(1)
    return path


def longest_collatz(n):
    " Find the number less than n that produces the longest collatz sequence. "
    seen = {}
    for x in range(1, n):
        path = collatz(x)
        ln = len(path)
        head = path.pop(0)
        while path and head not in seen:
            seen[head] = ln
            ln -= 1
            head = path.pop()

    return max(seen.items(), key=lambda t: t[1])


if __name__ == '__main__':
    print(longest_collatz(1000000))