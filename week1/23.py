# some programs using day 1 concepts
#Write a program that takes a price and discount percentage,then prints the final price using an f-string. Example: "Final price: ₹450.00"
price = float(input("Enter price "))

discount = float(input("Enter discount in % "))

discount_amount = price * discount/ 100
final_price = price - discount_amount

print(f'Your final price is: {final_price} ')