

















# # cook your dish here

# def largest_rectangle_area(arr):
#     n = len(arr)
#     max_area = 0

#     for i in range(n):
#         height = arr[i]

#         # expand left
#         left = i
#         while left > 0 and arr[left - 1] >= height:
#             left -= 1

#         # expand right
#         right = i
#         while right < n - 1 and arr[right + 1] >= height:
#             right += 1

#         width = right - left + 1
#         area = height * width

#         max_area = max(max_area, area)

#     return max_area


# # main
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     print(largest_rectangle_area(arr))