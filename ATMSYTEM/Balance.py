class Bal:
    def __init__(self):
        self.balance=50000.0
        self.statement=[]
    def display(self,c):
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print(f'Balance :{self.balance} Rupees')

    def cash_withdrawal(self, card):
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print("******CASH WITHDRAWAL PAGE******")
        amount = float(input("Please Enter The Amount:")) 
        if card == "1":
            if self.balance >= amount and amount <= 2000:
                self.balance = self.balance - amount
                self.statement.append(-(amount))
                print("Successfully Dedited!")
                self.display(self) 
            else:
                print("****Insufficient Funds Or Cash Limit Exceed!****")
        elif card == "2":
            if self.balance >= amount and amount <= 8499:
                self.balance = self.balance - amount
                self.statement.append(-(amount))
                print("Successfully Dedited!")
                self.display(self) 
            else:
                print("****Insufficient Funds Or Cash Limit Exceed!****")
        elif card == "3":
            if self.balance >= amount and amount <= 5000:
                self.balance = self.balance - amount
                self.statement.append(-(amount))
                print("Successfully Dedited!")
                self.display(self) 
            else:
                print("****Insufficient Funds Or Cash Limit Exceed!****")                


    def Cash_Deposit(self,c):
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print("******CASH DEPOSIT PAGE******")
        cash=float(input("Enter The Amount:"))  
        self.balance=self.balance+cash
        self.statement.append(cash)
        print("Successfully Deposited!")
        self.display(self)   
     



    def mini_Statement(self,c):
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print("******MINI STATEMENT PAGE******")
        
        if self.statement ==[]:
            print("Withdrawal:0\nCash Deposit:0") 
            self.display(self)
        else:
            print("Withdraw:",end=" ")
            for i in self.statement:
                if i<0:
                    print(i," ",end=" ")
            print()        
            print("Cash Deposit:",end=" ")                
            for i in self.statement:
                if i>0:
                    print(i," ",end=" ")   
            print()   
            self.display(self)               
                                   

# o=Bal()

# o.mini_Statement("1")