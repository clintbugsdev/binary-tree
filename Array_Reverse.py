def reverse(nums):
    start = 0
    end = len(nums) - 1

    while end > start:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


if __name__ == "__main__":
    n = [1, 2, 3, 4]
    reverse(n)
    print(n)
