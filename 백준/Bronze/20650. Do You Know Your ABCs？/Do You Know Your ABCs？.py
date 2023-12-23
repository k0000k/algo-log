nums = list(map(int, input().split()))

nums.sort()

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums) - 1):
        for m in range(j + 1, len(nums) - 1):
            if (nums[i] + nums[j] + nums[m] == nums[6]):
                print(nums[i], nums[j], nums[m])

