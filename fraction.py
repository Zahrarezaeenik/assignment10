
class Fraction:
    def __init__(self,s,m):
        self.numerator=s
        self.denominator=m

    def add(self, frac_2) :
        return Fraction((self.numerator * frac_2.denominator) + (frac_2.numerator * self.denominator),self.denominator * frac_2.denominator)

    def multiply(self,frac_2):
        return Fraction(self.numerator * frac_2.numerator,self.denominator * frac_2.denominator)

    def subtract(self,frac_2):
        return Fraction((self.numerator * frac_2.denominator) - (frac_2.numerator * self.denominator),self.denominator * frac_2.denominator)

    def divide(self, frac_2):
        return Fraction(self.numerator * frac_2.denominator,self.denominator * frac_2.numerator)
    
    def __str__(self) -> str:
        return f"{self.numerator:.0f}/{self.denominator:.0f}"

    def show(self):
        print(f"{self.numerator:.0f}/{self.denominator:.0f} = {(self.numerator / self.denominator):.4f}")

def menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    return int(input("Enter menu: "))

def frac_input(text,Condition=None):
    m=float(input(text))
    if m!=Condition:
        return m
    else:
        print("denominator cannot be zero.")
    return frac_input(text,Condition)

def main():
    print("fraction 1")
    frac_1=Fraction(frac_input("Enter numerator of fraction:"),frac_input("Enter denominator of fraction:",0))

    print("fraction 2")
    frac_2=Fraction(frac_input("Enter numerator of fraction:"),frac_input("Enter denominator of fraction:",0))

    while True:
        print("=============")
        choice=menu()
        print("=============")
        if choice == 1:
            print(f"{frac_1.__str__()} + {frac_2.__str__()} = ",end="")
            frac_1.add(frac_2).show()
        elif choice == 2:
            print(f"{frac_1.__str__()} - {frac_2.__str__()} = ",end="")
            frac_1.subtract(frac_2).show()
        elif choice == 3:
            print(f"{frac_1.__str__()} * {frac_2.__str__()} = ",end="")
            frac_1.multiply(frac_2).show()
        elif choice == 4:
            print(f"{frac_1.__str__()} / {frac_2.__str__()} = ",end="")
            frac_1.divide(frac_2).show()
        elif choice==5:
            break
        else:
            print("input invalid!")

if __name__ == "__main__":
    main()