Explanation
Initialization:

We initialize a list dp of size total + 1 with all values set to infinity (float('inf')), except dp[0] which is set to 0.
Dynamic Programming Update:

For each coin in coins, we iterate through the amounts from the coin's value up to the total.
We update dp[i] by taking the minimum of its current value and dp[i - coin] + 1, which represents using one more coin.
Result:

If dp[total] is still infinity, it means it's not possible to form the amount with the given coins, so we return -1.
Otherwise, we return dp[total], the minimum number of coins needed.
This approach ensures we efficiently find the minimum number of coins for any given total, leveraging the principles of dynamic programming.







