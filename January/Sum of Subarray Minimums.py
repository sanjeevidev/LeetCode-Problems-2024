MOD = 10**9 + 7
        stack = []
        result_sum = 0

        for i, num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                j = stack.pop()
                k = stack[-1] if stack else -1
                result_sum += arr[j] * (i - j) * (j - k)

            stack.append(i)

        while stack:
            j = stack.pop()
            k = stack[-1] if stack else -1
            result_sum += arr[j] * (len(arr) - j) * (j - k)

        return result_sum % MOD
