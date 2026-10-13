'''
1. Download your programs from Moodle.
1. Put this grading program in a folder with your programs.
2. Run this grading program.
3. Read your test results from results.txt file.
'''

import sys
import unittest


class Test(unittest.TestCase):

    # (p1.py) Mexican wave
    def test_p1(self):
        import p1
        self.assertEqual(p1.f("water"), "Water-wAter-waTer-watEr-wateR")
        self.assertEqual(p1.f("a"), "A")
        self.assertEqual(p1.f(""), "")
        # test uodparniający: funkcja powinna działać sensownie nawet dla mieszanego case
        self.assertEqual(p1.f("waTer"), "Water-wAter-waTer-watEr-wateR")

    # (p2.py) Point class with quadrants
    def test_p2(self):
        import p2

        p = p2.C(2, 3)
        self.assertEqual(p.m1(), 1)
        self.assertTrue(p.m2(7, 4))
        self.assertFalse(p.m2(-3, 1))
        self.assertTrue(p.m3(8, 5))   # distance sqrt(6^2+2^2)=~6.32 > 5
        self.assertFalse(p.m3(4, 7))  # distance sqrt(2^2+4^2)=~4.47 <= 5

        p1 = p2.C(0, 5)
        self.assertEqual(p1.m1(), 0)
        self.assertFalse(p1.m2(4, 7))   # other point is in quadrant I, p1 is on axis => 0
        self.assertTrue(p1.m2(-7, 0))   # other point also on axis => 0

        # dodatkowe pokrycie kwadrantów
        self.assertEqual(p2.C(-1, 2).m1(), 2)
        self.assertEqual(p2.C(-1, -2).m1(), 3)
        self.assertEqual(p2.C(1, -2).m1(), 4)
        self.assertEqual(p2.C(5, 0).m1(), 0)
        self.assertEqual(p2.C(0, -5).m1(), 0)

    # (p3.py) flights above average passengers
    def test_p3(self):
        import p3
        self.assertEqual(p3.f({"LO231": 150, "BA787": 120, "NZ15": 30}), 2)
        self.assertEqual(p3.f({"LO231": 150, "BA787": 20, "NZ15": 30}), 1)
        # równe średniej nie liczymy
        self.assertEqual(p3.f({"A": 10, "B": 20, "C": 30}), 1)  # avg=20 => tylko 30

    # (p4.py) filter results then max-min of filtered
    def test_p4(self):
        import p4
        res = [95, 90, 20, 50, 70]

        fnc1 = lambda x: x > 50
        self.assertEqual(p4.f(fnc1, res), 25)  # [95,90,70] => 95-70

        fnc2 = lambda x: x > 30 and x < 90
        self.assertEqual(p4.f(fnc2, res), 20)  # [50,70] => 70-50

        # jeszcze jedno: filtr łapie większy zbiór
        fnc3 = lambda x: x >= 20
        self.assertEqual(p4.f(fnc3, res), 75)  # max=95 min=20

    # (p5.py) Metis number validity counter
    def test_p5(self):
        import p5
        self.assertEqual(p5.f(["A15", "-31", "7abC", "+D1", "-g4"]), 4)
        self.assertEqual(p5.f(["A05", "-3+1", "7ab8C", "+Bb7", "-22c55"]), 2)

        # edge cases: sign only at beginning; digits only 1..7; letters a..d any case
        self.assertEqual(p5.f(["+a", "-D7", "1234567", "abcd", "ABCD"]), 5)
        self.assertEqual(p5.f(["", "+", "-", "0", "8", "a0", "a8", "a+1", "1-2"]), 0)

    # (p6.py) Person class string representation depending on age
    def test_p6(self):
        import p6
        c1 = p6.C("John", "May", 21)
        c2 = p6.C("Anna", "Brown", 17)
        self.assertEqual(str(c1), "JM21")
        self.assertEqual(c1.__str__(), "JM21")
        self.assertEqual(str(c2), "ab17")

        # granica pełnoletności
        self.assertEqual(str(p6.C("Eva", "Stone", 18)), "ES18")
        self.assertEqual(str(p6.C("Eva", "Stone", 0)), "es0")

    # (p7.py) Counter class
    def test_p7(self):
        import p7
        c = p7.C(5)
        self.assertEqual(c.m1(), 5)
        c.m2()
        self.assertEqual(c.m1(), 6)
        c.m4(-8)
        self.assertEqual(c.m1(), -2)
        c.m3()
        self.assertEqual(c.m1(), -3)
        c.m4(10)
        self.assertEqual(c.m1(), 7)
        self.assertEqual(str(c), "7")
        self.assertEqual(c.__str__(), "7")

    # (p8.py) Map product names via fnc, return comma-separated string
    def test_p8(self):
        import p8
        prods = ["water", "cheese", "tomato"]

        fnc1 = lambda x: "id:" + x[:2]
        self.assertEqual(p8.f(fnc1, prods), "id:wa,id:ch,id:to")

        fnc2 = lambda x: (x[0] + x[-1]).upper()
        self.assertEqual(p8.f(fnc2, prods), "WR,CE,TO")

    # (p9.py) All IDs unique (case-sensitive)
    def test_p9(self):
        import p9
        self.assertTrue(p9.f(["john5", "ann123", "JOHN5", "xxx", "abc333", "a10"]))
        self.assertFalse(p9.f(["abc123", "ann", "abc123", "a10"]))
        self.assertTrue(p9.f([]))
        self.assertTrue(p9.f(["a"]))
        self.assertFalse(p9.f(["A", "A"]))

    # (p10.py) Closure multiplier
    def test_p10(self):
        import p10
        times_five = p10.f(5)
        self.assertEqual(times_five(8), 40)
        times_three = p10.f(3)
        self.assertEqual(times_three(7), 21)
        self.assertEqual(p10.f(0)(999), 0)
        self.assertEqual(p10.f(-2)(11), -22)

    # (p11.py) Sort cars list-of-singleton-dicts
    def test_p11(self):
        import p11
        cars = [{"KR333": 138}, {"WL555": 497}, {"DB444": 341}, {"MC222": 412}]
        self.assertEqual(
            p11.f(cars, 1),
            [{"DB444": 341}, {"KR333": 138}, {"MC222": 412}, {"WL555": 497}]
        )
        self.assertEqual(
            p11.f(cars, 2),
            [{"WL555": 497}, {"MC222": 412}, {"DB444": 341}, {"KR333": 138}]
        )

    # (p12.py) Filter ISO dates YYYY-MM-DD (with 2-digit month/day)
    def test_p12(self):
        import p12
        dates = "2021-1-3,05/12/2024,1998-12-11,9 maj 2007,2001-12-07,15-09-2011"
        self.assertEqual(p12.f(dates), ["1998-12-11", "2001-12-07"])

        dates2 = "2025-01-04,2025-1-04,2025-01-4,2025-01-05"
        self.assertEqual(p12.f(dates2), ["2025-01-04", "2025-01-05"])


if __name__ == '__main__':
    # zapis wyników jak w przykładowym check.py
    sys.stderr = open('results.txt', 'w', encoding="utf-8")
    unittest.main(verbosity=2)
