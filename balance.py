# abdullahi, 10, kenya

def withdraw(current_bank, amouth):
    current_bank = current_bank
    if current_bank >= amouth:
        
        print("your' withdraw", amouth)
        current_bank =current_bank - amouth
        return current_bank
    else:
        print("insufficient balance, please rechange your acount")

print(withdraw(600, 300))