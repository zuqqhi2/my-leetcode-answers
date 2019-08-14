import time


class Foo:
    def __init__(self):
        self.firstFlg = False
        self.secondFlg = False
        self.sleepTime = 0.01

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

        self.firstFlg = True

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.firstFlg:
            time.sleep(self.sleepTime)

        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

        self.secondFlg = True

    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.secondFlg:
            time.sleep(self.sleepTime)

        # printThird() outputs "third". Do not change or remove this line.
        printThird()

# Sample Testcase:
#   Input:
#     [1,2,3]
#   Output:
#     "firstsecondthird"

# Performance Result:
#   Coding Time: 00:05:43
#   Runtime: 68 ms, faster than 64.27% of Python3 online submissions for Print in Order.
#   Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Print in Order.
