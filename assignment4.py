# Write a program to withdraw Ksh.25000 if acc_bal is between Ksh.100000 and 200000 
# 30% if acc_bal is between 500000 and 1000000
# Above 1000000 deduct 15000

acc_bal =  int(input("Enter your acc_balance:"))

if (int(acc_bal) > 100000 and int(acc_bal) < 200000):
    acc_bal = acc_bal - 25000
    print("We have deducted Ksh.25000 from your account")
elif (int(acc_bal) > 500000 and int(acc_bal)< 1000000):
    acc_bal = acc_bal - (0.3*acc_bal)
    print("We have deducted 30 % from your account.")
elif (int(acc_bal) > 1000000):
    acc_bal = acc_bal - 15000
    print("We have deducted Ks.15000 from your account.")

