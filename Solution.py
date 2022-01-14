class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        elif n < 0:
            return 1 / (x * Solution.myPow(Solution, x, -1 * (n + 1)))
        else:
            return x * Solution.myPow(Solution, x, n - 1)


def main():
    X = Solution
    print(X.myPow(X, 2, 31))


if __name__ == '__main__':
    main()
