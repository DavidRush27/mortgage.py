home_value = 200000
down_payment = 80000
principal = 0
interest_rate = 0.05
time_in_years = 30
monthly_payment = 0
def calculate_principal(home_value, down_payment):
    principal = home_value - down_payment
    return principal

def calculate_mortgage_payment(principal, interest_rate, time_in_years):
    new_rate = interest_rate / 12
    months = time_in_years * 12
    monthly_payment = ((principal * new_rate) * (1 + new_rate)** months) / (((1+ new_rate)**months) - 1)
    return monthly_payment

monthly_payment = calculate_mortgage_payment(calculate_principal(home_value,down_payment),interest_rate,time_in_years)

print("What is the value of the home that you are looking at?")
home_value = int(input())
print("How much are you planning for the down payment?")
down_payment = int(input())
print("Next you need to enter in the interest rate as a decimal. For example a 5% interest rate is .o5")
interest_rate = float(input())
print("Lastly eneter the amount of time in years you like to pay the loan off")
time_in_years = int(input())

monthly_payment = calculate_mortgage_payment(calculate_principal(home_value,down_payment),interest_rate,time_in_years)

print("Based on the data that you provided your monthly pament will be $",round(monthly_payment),".")
