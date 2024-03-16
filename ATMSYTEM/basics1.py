class AtmSytem:
    def atm(self):
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        from ATMSYTEM.Authentication import ATH
        card = ["Rupee Card", "Master Card", "Visa Card"]
        print("Please Select Card As Below [Select as numbers]:")
        for i in range(len(card)):
            print((i + 1), " ", card[i])
        s_card = input("Please Select The Card:")    
        if s_card == "1":
            user = input("Enter the username:")
            password = input("Enter the password:")
            a = ATH()
            r=a.auth(user, password,s_card)
            if r==1:
                o=AtmSytem
                o.atm(self)
        elif s_card == "2":      
            user = input("Enter the username:")
            password = input("Enter the password:")
            a = ATH()
            r=a.auth(user, password,s_card) 
            if r==1:
                o=AtmSytem
                o.atm(self) 
        elif s_card == "3":    
            user = input("Enter the username:")
            password = input("Enter the password:")
            a = ATH()
            r=a.auth(user, password,s_card)
            if r==1:
                o=AtmSytem
                o.atm(self)
        else:        
            print("Please Select Valid Card....")   


a = AtmSytem()
a.atm()