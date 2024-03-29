def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

def main():
    try:
        original_price = float(input("500: $"))
        discount_percent = float(input("30: "))
        
        final_price = calculate_discount(original_price, discount_percent)
        
        if final_price == original_price:
            print(f"No discount applied. Final price: ${final_price:.2f}")
        else:
            print(f"Discount applied. Final price after discount: ${final_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
