amount  = float(input("Whats The Total Bill Amount:  "))
tip = float(input("What Is The Tip Percentage You'd Like To Give :  "))
people = float(input("How Many People Are Splitting The Bill:  "))

print(f"Each Person Should Give -> {(amount + (amount*tip)/100)/people}")