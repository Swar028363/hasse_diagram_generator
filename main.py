from hasse import Hasse
import math
from typing import List, Callable, Dict, Any, Set

def gcd_prime_relation(x: int, y: int) -> bool:
        # only connect upward
        if x >= y:
            return False
        d = math.gcd(x, y)
        # must share a prime gcd
        if d <= 1:
            return False
        # check primality of gcd
        def is_prime(n: int) -> bool:
            if n < 2 or (n % 2 == 0 and n != 2):
                return False
            p = 3
            while p*p <= n:
                if n % p == 0:
                    return False
                p += 2
            return True
        return is_prime(d)

if __name__ == "__main__":
    # Test 1: Divisibility Relation
    print("Divisibility Relation:")
    elements = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 30, 36, 40, 48, 60, 72]
    hasse_div = Hasse(elements, Hasse.divisibility_relation)
    hasse_div.draw()

    print("Divisibility Relation:")
    elements = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 30, 36, 40, 48, 60, 72]
    hasse_div = Hasse(elements, Hasse.divisibility_relation, show_arrows=True)
    hasse_div.draw()

    # Test 2: Subset Relation
    print("Subset Relation:")
    elements = [{1}, {1, 2}, {1, 2, 3}, {2}, {2, 3}]
    hasse_sub = Hasse(elements, Hasse.subset_relation)
    hasse_sub.draw()

    # Test 3: Less Than or Equal Relation
    print("Less Than or Equal Relation:")
    elements = [12, 9, 62, 96, 18]
    hasse_leq = Hasse(elements, Hasse.less_equal_relation)
    hasse_leq.draw()

    # Test 4: Greater Than or Equal Relation
    print("Greater Than or Equal Relation:")
    elements = [9, 13, 20, 27, 88]
    hasse_geq = Hasse(elements, Hasse.greater_equal_relation)
    hasse_geq.draw()

    # Test 5: GCD Prime Relation
    elements = [2, 3, 4, 5, 6, 9, 10, 12, 15]
    hasse_gcd_prime = Hasse(elements, gcd_prime_relation, show_arrows=True)
    hasse_gcd_prime.draw()