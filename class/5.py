__author__ = 'hadeslee'
class HousePark:
    lastname = "박"
    def setname(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s여행을가다" %(self.fullname, where))
pey = HousePark()
pes = HousePark()
pey.setname("응용")
pey.travel("부산")

print(pey.fullname)
print(pes.lastname)



