#!/usr/bin/python3
"""
Prime Game
"""

def isWinner(x, nums):
  """
  isWinner Function
  """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    
    is_prime = [True] * (max_num + 1)
    is_prime[0], is_prime[1] = False, False

    p = 2
    while (p * p <= max_num):
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)
    
    maria_wins, ben_wins = 0, 0
    
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
