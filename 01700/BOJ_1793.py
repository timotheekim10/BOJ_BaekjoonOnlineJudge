while True:
    try:
        n = int(input())

        dp = [1, 1, 3]
        if n == 0 or n == 1 or n == 2:
            print(dp[n])
        else:
            for i in range(3, n+1):
                dp.append(dp[i-1] + 2*dp[i-2])
            print(dp[n])
    except:
        break