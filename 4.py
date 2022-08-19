id=int(input('Enter customer id: '))
if id >=101 and id<=1000:
    amt=int(input('Enter Ammount: '))
    if amt>=1000:
        amt=amt-amt*0.05
    elif amt>=500 and amt<1000:
        amt=amt-amt*0.02
    elif amt>0 and amt<500:
        amt=amt-amt*0.01
    print(amt,'is the discounted ammount')

else:
    print('Enter valid customer id ')