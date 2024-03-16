
class ATH: 
        def opt(self, c):
            from ATMSYTEM.Balance import Bal
            bal_instance = Bal()
            while True:
                print("----------------------------------------------------------------------------------------------------------------------------------------")
                options = ["Check Balance", "Cash Withdrawal", "Cash Deposit", "Mini Statement", "Exit"]
                print("Please Select Options As Below [Select as numbers]")
                for i in range(len(options)):
                    print((i+1), " ", options[i])
                choice_option = input("Please Select An Option: ")    
                if choice_option == "1":
                    bal_instance.display(c)  # Pass 'c' to display method
                elif choice_option == "2":
                    bal_instance.cash_withdrawal(c)  # Pass 'c' to cash_withdrawal method
                elif choice_option == "3":
                    bal_instance.Cash_Deposit(c)  # Pass 'c' to display method
                elif choice_option == "4":
                    bal_instance.mini_Statement(c)  # Pass 'c' to display method
                elif choice_option == "5":
                    import basics1
                    break
                else:
                    print("******PLEASE ENTER VALID OPTION******")



        def auth(self,u,p,card):
            print("----------------------------------------------------------------------------------------------------------------------------------------")
            self.u=u
            self.p=p
            user="abc"
            password="1234"
            if user==self.u and password==self.p:
                print("****Authentication Successful!****")
                op=ATH()
                op.opt(card)
            else:    
                print("Please Enter Valid UserName or Password!")  
                return 1              

















