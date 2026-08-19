print(format("-----------------------------Personal Expense Tracker---------------------------",'>80'))
print("Option 1 for 'Add Expenses'")
print("Option 2 for 'View All Expenses'")
print("Option 3 for ' Total Expenses'")
print("Option 4 for 'Highest expenses'")
print("Option 5 for 'search items'")
print("Option 6 for 'Search items'")
print("Option 7 for 'Exit'")
Expenses=[]
def add_expenses():
    Amount=int(input("Enter amount : "))
    Catagory=input("Enter category : ")
    Description=input("Enter description : ")
    if Amount>0:
        item_details={"Amount":Amount,"Category":Catagory,"Description":Description}
        Expenses.append(item_details)
        print(item_details)
        print(format("----------------------------Expenses are sucessfully added------------------------------",'>80'))
    else:
        print("Invalid Amount")
    return ""
def view():
    print(format('-------------------------All Expenses------------------------','>80'))
    for items in Expenses:
        print(f"{items["Amount"]}| {items["Category"]} | {items["Description"]}")
    return " "
def total_amount():
    sum=0
    for i in Expenses:
        sum=sum+i["Amount"]
    print(f"Total Spending : {sum}")
    return ""
def highest_expenses():
    amount=[]
    for i in Expenses:
        amount.append(i["Amount"])
    print(amount)
    max_amount=amount[0]
    min_amount=amount[0]
    for i in amount:
        if max_amount<=i:
            max_amount=i
    for j in amount:
        if min_amount>=i:
            min_amount=i
    for m in Expenses:
        if max_amount== m["Amount"]:
            print(f"Higeshest expenses {m}")
        if min_amount==m["Amount"]:
            print(print(f"Min expenses {m}"))
    return " "
def search_item():
    item_name=input("enter the item name : ")
    for i in Expenses:
        if item_name in i["Category"]:
            print(i)
            print(format("--------------------------Items sucessfully found!!---------------------------"),'>80')
        else:
            print(format("----------------------------Item is not found-----------------------"),">80")
    return""
def categories_summary():
    # def category_summary():
    category_data = {}

    for expense in Expenses:
        category = expense["Category"]
        amount = expense["Amount"]

        if category in category_data:
            category_data[category] += amount
        else:
            category_data[category] = amount

    print(format("==========Category Summary==========", ">80"))
    for category in category_data:
        print(f"{category} : {category_data[category]}")

    return

while True:
    option=int(input("Enter a Option : "))
    if option==1:
        add_expenses()
    elif option==2:
        view()
    elif option==3:
        total_amount()
    elif option==4:
        highest_expenses()
    elif option==5:
        search_item()
    elif option==6:
        print("categories summary")
        categories_summary()
    elif option==7:
        print(format("----------------------------------EXIT-----------------------------------"),'>80')
        break