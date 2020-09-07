#giving behaviours to coins like rusting, fliping,cleaning & spending

class Pound:
    #self is a parameter which refers to a specific instance of the class.For example if I create coin1 -self will be coin1 & similarly
    #defining constructor.It does not return anything.Helps to set up initial properties of an object
    def __init__(self,rare=False):
        self.rare=rare
        if self.rare:
           self.value=1.25
        else:
           self.value=1.00
        self.color="gold"
        self.num_edges=1
        self.diameter=22.5# in millimeter
        self.thicknes=3.15#in mm
        self.heads=True

    def rust(self):
         self.color="greenish"

    def clean(self):
        pass



coin1=Pound(rare=True)
coin2=Pound()
print("coin1",coin1.value)
print("coin2",coin2.value)

print("coin1",coin1.value)
print("coin2",coin2.value)