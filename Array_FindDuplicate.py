def find_duplicates(nums):
    for num in nums:
        if nums[abs(num)] >= 0:
            nums[abs(num)] = -nums[abs(num)]
        else:
            print("Repetition found: %s" % str(abs(num)))


if __name__ == "__main__":
    n = [2, 6, 5, 1, 4, 2, 1]
    find_duplicates(n)
