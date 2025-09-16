def convert(dollar_amount):
    rupee_rate = 88.03
    pound_rate = 0.738
    yuan_rate = 7.12

    rupee = dollar_amount * rupee_rate
    pound = dollar_amount * pound_rate
    yuan = dollar_amount * yuan_rate

    print(f"{dollar_amount:.2f}\t\t{rupee:.2f}\t\t{pound:.2f}\t\t{yuan:.2f}")
    # print(f"{dollar_amount} - {rupee:.2f} - {pound:.2f} - {yuan:.2f}")

print("Currency Converter")
print("Enter dollar amounts separated by '@'. Type '*' to exit.")

while True:
    amount = input("Enter Dollar ($): ")
    if amount == "*":
        print("Closing....")
        break

    print("\nDollar ($)  Indian Rupee (₹) British Pound (£)  Chinese Yuan (¥)")
    
    dollar_values = amount.split("@")
    for value in dollar_values:
        if value.replace('.', '', 1).isdigit():
            dollar = (value)
            convert(dollar)
        else:
            print(f"Invalid input: {value}")
