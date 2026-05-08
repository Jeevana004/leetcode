from collections import defaultdict, deque
from math import isqrt

class Solution:
    def minJumps(self, nums):
        n = len(nums)

        # ---------- Prime Check ----------
        MAXV = max(nums)

        sieve = [True] * (MAXV + 1)
        sieve[0] = sieve[1] = False

        for i in range(2, isqrt(MAXV) + 1):
            if sieve[i]:
                for j in range(i * i, MAXV + 1, i):
                    sieve[j] = False

        # ---------- Build divisibility map ----------
        # prime p -> indices where nums[idx] % p == 0
        divisible = defaultdict(list)

        for idx, val in enumerate(nums):
            temp = val
            factors = set()

            d = 2
            while d * d <= temp:
                if temp % d == 0:
                    factors.add(d)
                    while temp % d == 0:
                        temp //= d
                d += 1

            if temp > 1:
                factors.add(temp)

            for f in factors:
                divisible[f].append(idx)

        # ---------- BFS ----------
        q = deque([0])
        visited = [False] * n
        visited[0] = True

        used_prime = set()
        steps = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()

                if i == n - 1:
                    return steps

                # Adjacent moves
                for nxt in [i - 1, i + 1]:
                    if 0 <= nxt < n and not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)

                # Prime teleportation
                val = nums[i]

                if sieve[val] and val not in used_prime:
                    for nxt in divisible[val]:
                        if not visited[nxt]:
                            visited[nxt] = True
                            q.append(nxt)

                    used_prime.add(val)

            steps += 1

        return -1