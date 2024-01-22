# Input: Get hours worked and hourly pay rate from user
hours_worked = float(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter your hourly pay rate: "))

# Calculations: Calculate gross pay
gross_pay = hours_worked * hourly_rate

# Output: Display the gross pay
print(f"The gross pay is: ${gross_pay:.2f}")