# cook your dish here
def next_smallest_element(arr):
    n = len(arr)
    result = [-1] * n  # Initialize result with -1 for elements with no smaller element
    stack = []  # Stack to store indices

    for i in range(n - 1, -1, -1):  # Iterate from right to left
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        if stack:
            result[i] = arr[stack[-1]]
        stack.append(i)

    return result


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = next_smallest_element(arr)
    for e in result:
        print(e, end=" ")


if __name__ == "__main__":
    main()