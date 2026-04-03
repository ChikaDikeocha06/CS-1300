#Write a program that calculates the price of a movie ticket based 
#on the viewer's age and whether they areseeing a matinee (before 5 PM) showing.
age_group= ["Child (under 13),Teen (13 to 17),Adult (18 to 64),Senior (65+)"]
matinee_price= ["$6.00", "$7.00", "$8.00", "$6.00"]
regular_price= ["$8.00", "$10.00", "$13.00", "$7.00"]
# Ask the user for their age (integer)
user_age = int(input("Please enter your age: "))
#  Ask the user if the showing is a matinee (yes/no)
is_matinee = True if input("Is this a matinee showing? (yes/no): ").lower() in ["yes", "y"] else False
#Use nested if statements: the outer level should determine the age group, and the inner level should determine matinee vs. regular pricing.
age_descriptions=[]
ticket_prices=[]
while True:
    if user_age < 0:
        print("Invalid age. Please enter a valid age.")
        input("Please enter your age: ")
    if user_age < 13:
        age_group = "Child (under 13)"
        price = matinee_price[0] if is_matinee else regular_price[0]
        break
    elif 13 <= user_age <= 17:
        age_group = "Teen (13 to 17)"
        price = matinee_price[1] if is_matinee else regular_price[1]
        break
    elif 18 <= user_age <= 64:
        age_group = "Adult (18 to 64)"
        price = matinee_price[2] if is_matinee else regular_price[2]
        break
    elif user_age >= 65:
        age_group = "Senior (65+)"
        price = matinee_price[3] if is_matinee else regular_price[3]
        break
    else:
        print("Invalid age. Please enter a valid age.")
        user_age = int(input("Please enter your age: "))    
age_descriptions.append(age_group)
ticket_prices.append(price)
#Print the ticket price to the user.
print(f"Age group: {age_group}\nTicket price: {price}")
