# Link:

# Solution 1:
import math

class Solution:
    def divisorGame(self, n: int) -> bool:
        if n == 2:
            return True
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

        def play_turn(n: int, turn: bool):
            if is_prime(n):
                return turn
            save = -1
            for x in range(n//2, 0, -1):
                if n % x == 0:
                    if is_prime(n-x):
                        return play_turn(n-x, not turn)
                    else:
                        save = x
            if save == -1:
                return turn
            return play_turn(n-save, not turn)

        return play_turn(n, False)

# Solution 2: Logic
class Solution:
    """
    1. Suppose n is even. Alice can always pick x=1, making n odd for Bob.
    2. Since Bob always receives an odd number, he can only subtract an odd
    divisor, which results in an even number for Alice.
    3. This process continues, and eventually, Bob is forced into  n=1, where
    he loses.
    4. On the other hand, if n starts odd, Alice's first move makes it
    even, and Bob follows the winning strategy.
    """
    def divisorGame(self, n: int) -> bool:
        return not n%2
