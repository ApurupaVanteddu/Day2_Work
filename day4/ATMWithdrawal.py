bal=5000
amt=int(input("Enter withdrawal amount: "))

if amt<=bal and amt %100==0:
    bal=bal-amt
    print("Please collect your cash")
    print("Available balance is:",bal)
else:
    print("Invalid amount or insufficient balance")

