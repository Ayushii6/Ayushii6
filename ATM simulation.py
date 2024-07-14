name=input("Enter your name:")
print("hello",name)
message="""
How may i help you 


please select any of them,option,
type 1 >>>> CHECK BALANCE.
type 2 >>>> DEPOSIT.
type 3 >>> WITHDRAWL."""
print(message)
task=int(input("plz enter your option"))
available_amount =5000
if task>=1 and task<=3:
    print("welcome to our virtual bank")
    #check balance
    if task==1:
        print("your available blance is :",available_amount)
# deposit
    elif task==2:
      deposit_amount=  int(input("please enter your deposit amount:"))
      available_amount+=deposit_amount
      print("you have deposit successfully:",deposit_amount)
      print("your bank balance is:",available_amount)

      if deposit_amount>500:
          pass
      else :
          print("amount is not depositable")
#withdrawl
    else:
        withdrawl_amount=int(input("enter withdrawl amount"))
        if withdrawl_amount>available_amount:
            print("sorry your available balnce is less")
        else:
             available_amount -= withdrawl_amount
            print("now your available balance is",available_amount)
else:
    print("select in between 1 to 3" )
