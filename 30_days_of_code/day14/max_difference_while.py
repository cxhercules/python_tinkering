class Difference:
    def __init__(self, a):
        self.__elements = a
    # Add your code here
    global maximumDifference
    def computeDifference(self):
        self.maximumDifference = 0
        if len(self.__elements) == 1:
            self.maximumDifference = self.__elements[0]
        else:
            while self.__elements:
                print (self.__elements)
                if len(self.__elements) == 1:
                    return
                x = self.__elements[0]
                del self.__elements[0]
                for y in self.__elements:
                    print ("X:", x, "Y:", y)
                    if abs(x-y) >= self.maximumDifference:
                        self.maximumDifference = abs(x-y)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
#print(d.__Difference_elements)
