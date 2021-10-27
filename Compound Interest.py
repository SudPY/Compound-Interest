p = float(input("Enter the Principle : "))
t = float(input("Enter the Time period : "))
r = float(input("Enter the Rate of interest : "))

def compound_interest(p, t, r):
    amount = p * (pow((1 + r / 100), t))
    CI = amount - p
    print("The interest is : ", CI)

compound_interest(p, t, r)
