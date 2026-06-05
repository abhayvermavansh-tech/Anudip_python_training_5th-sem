deeposit = 0
withdrawal = 0
count_d = 0
count_w = 0
balance = 0
deposit =[]
withdraw =[]
tran = [5000,-2000,3000,-1000,-500,7000]
for i in tran:
    if(i>0):
        deposit.append(i)
        deeposit = deeposit + i
        count_d = count_d +1
    else:
        withdraw.append(i)
        withdrawal  = withdrawal +1
        count_w = count_w +1
balance =   deeposit - withdrawal
print("Current Balance: ₹",balance) 
print("Deposits:",deposit)
print("Withdrawals:",withdraw)
deposit.sort()
withdraw.sort()
print("Largest Deposit:",deposit.pop())
print("Largest Withdrawal:",withdraw.pop(0))
