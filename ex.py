def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount = amount % coin
    
    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)
    
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin
    
    result = {}
    current_amount = amount
    
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin
    
    return result

if __name__ == "__main__":
    amount = 113

    greedy_result = find_coins_greedy(amount)
    dp_result = find_min_coins(amount)

    print("Greedy Algorithm Result:", greedy_result)
    print("Dynamic Programming Result:", dp_result)
