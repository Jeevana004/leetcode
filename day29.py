# LeetCode 3660 - Jump Game IX
# User Input + Output Version

from collections import deque

def maxReachable(nums):
    n = len(nums)

    # Build graph
    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i < j and nums[j] < nums[i]:
                graph[i].append(j)

            elif i > j and nums[j] > nums[i]:
                graph[i].append(j)

    ans = []

    # BFS from every index
    for i in range(n):
        q = deque([i])
        visited = set([i])

        maxi = nums[i]

        while q:
            node = q.popleft()

            maxi = max(maxi, nums[node])

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        ans.append(maxi)

    return ans


# ---------- User Input ----------
n = int(input("Enter size of array: "))

nums = list(map(int, input("Enter array elements: ").split()))

result = maxReachable(nums)

print("Maximum reachable values:")
print(result)