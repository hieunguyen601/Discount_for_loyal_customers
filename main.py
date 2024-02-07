# Discount for loyal customers
Loyal_customers = ["Hieu", "Harry", "Yone", "Riven"]
drinks = {"Coffee": 5.25, "Milk tea": 5.75, "Tea": 4.75}
discount = 20


def find_loyal_customers(coupon):
    customers = input("Enter your name: ")
    if customers in Loyal_customers:
        print("Your name is on the list", customers)
        return True
    else:
        print("There is no your name is the list")
        return False


def order_drinks():
    print("Available drinks:")
    for drink, price in drinks.items():
        print(drink, "-", price)

    drink_choice = input("Enter your drink choice: ")
    if drink_choice in drinks:
        return drink_choice
    else:
        print("Invalid choice. Please select a drink from the menu.")
        return order_drinks()


def calculate_total(drink, is_loyal_customer):
    price = drinks[drink]
    if is_loyal_customer:
        price *= (100 - discount) / 100
    return price


if __name__ == "__main__":
    is_loyal = find_loyal_customers(Loyal_customers)
    chosen_drink = order_drinks()
    total_cost = calculate_total(chosen_drink, is_loyal)
    print(f"Your total cost for {chosen_drink} is: ${total_cost:.2f}")
