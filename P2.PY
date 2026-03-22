class date:
    def __init__(self, a, b, c):
        self.d = a
        self.m = b
        self.y = c

    def day(self):
        print("day =", self.d)

    def month(self):
        print("month =", self.m)

    def year(self):
        print("year =", self.y)

    def monthName(self):
        months = ["unknown", "january", "february", "march", "april", "may", "june", "july",
                  "august", "september", "october", "november", "december"]
        if 1 <= self.m <= 12:
            print("month name:", months[self.m])
        else:
            print("Invalid month number")

    def isLeapYear(self):
        if (self.y % 400 == 0) or ((self.y % 4 == 0) and (self.y % 100 != 0)):
            print("It is a Leap year")
        else:
            print("It is not a leap year")

    def __str__(self):
        return f"Date: {self.d}/{self.m}/{self.y}"

d1 = date(3, 8, 2000)
d1.day()
d1.month()
d1.year()
d1.monthName()
d1.isLeapYear()
print(d1)
# End of P2.PY