#day 2 concepts
"""A shop gives discounts based on membership and purchase amount:
Gold members get 20% off any purchase. Silver members get 10% off purchases above ₹500.
Others get 5% off purchases above ₹1000. Print the final price.
"""
price = int(input("Enter price: "))
gold_member = False
silver_member = True

if gold_member:
    dis_amt = price * 20/100
    final_price = price - dis_amt
    
elif silver_member and price>500:
    dis_amt = price * 10/100
    final_price = price - dis_amt
    
elif gold_member == False and silver_member == False and price>1000:
    dis_amt = price * 5/100
    final_price = price - dis_amt
    
else:
    print("Final price: ", price)   
print("final price:",final_price)         
