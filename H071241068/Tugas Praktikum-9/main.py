import time
from tester import Tester


def main():
    tester = Tester()

    tester.test_break_code(123, 738)
    tester.test_break_code(456, 912)
    tester.test_break_code(789, 303)
    tester.test_break_code(999, 973)
    tester.test_break_code(100, 55)

    time.sleep(2)
    tester.final_results()


main()
