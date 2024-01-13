#assign no 06 question no 01
def calculate_ticket_price(age,day,is_group=False,is_family=False):
    based_price=0
    #assign based price on age
    if age=="adult":
        based_price=10
    elif age=="child":
        based_price=5
    elif age=="senier":
        based_price=8
    else:
        return "invild age"

    #discount based on day
    if day=="weekday":
        based_price-=2
    elif day=="weekend":
        based_price+=3
    else:
        return "invalid day"
    #discount based on group or family_group
    if is_group:
        based_price*=0.9
    elif is_family:
        based_price*=0.8
    else:
        "invalid group"
age=input("enter age categry(adult,child,senior)")
day=input("enter day catrgry(weekday,weekend)")
group_discount=input("enter group_discount categry)")
ticket_price=calculate_ticket_price(age,day,is_group=False,is_family=False)
print("ticket_price",ticket_price)

#Question 02
def caculate_total_bill(items,dis_per=0,tax_per=0,num_frd=1):
    total_amount=0
    for item in items:
        quantity=item["quantity"]
        price=item["ptice"]
        total_amount+=quantity*price
    #apply disount
    total_amount-=(dis_per/100)*total_amount
    #apply tax
    total_amount+=(tax_per/100)*total_amount
    #bill among friend
    if num_frd>1:
        total_amount/=num_frd
        return "total_bill"
quantity=[2,3,1]
price=[5,7,9]
total_amount=caculate_total_bill(item=3,quantity=3,dis_per=0.1,tax_per=0.4,num_frd=1)
print("total_bill")


#QUESTION NO 04
def estimate_travel_cost(destination,transport_cost,accommodation_cost,activities_cost,budget_style='standard',duration=7):
    style_multipilar={'budget':0.8,'standard':1.0,'luxury':1.5}
    #calculate total cost
    total_cost=(transport_cost+accommodation_cost+activities_cost)*style_multipilar.get(budget_style,1.0)
    #total cost based on duration
    total_cost*=duration/7  #with respect to week
    return total_cost
destination='pairs'
transport_cost=500
accommodation_cost=800
activities_cost=300
budget_style='standard'
duration=10
estimated_cost=estimate_travel_cost(destination, transport_cost, accommodation_cost, activities_cost, budget_style, duration)
print(f"Estimated Travel Cost for {duration} week in {destination}({budget_style} style): ${estimated_cost: 2f}")

