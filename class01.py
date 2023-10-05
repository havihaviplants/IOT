class Automobile:
    name = ""
    velocity = ""

    def velocityPlus(self):
        self.velocity = self.velocity + 1
        print("속도는 %d입니다." % self.velocity)
    def velocityDw(self):
        self.velocity = self.velocity - 1
        if self.velocity < 0:
            self.velocity = 0
        print("속도는 %d입니다." % self.velocity)

ac = Automobile()
ac.velocityPlus()
ac.velocity = 20
ac.velocityDw()
    