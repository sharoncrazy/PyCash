from datetime import datetime
date_format = "%d-%m-%Y"
CATEGORIES = {"I" : "income", "E":"expense"}

def get_date(prompt,allow_default = False):
    Date_str = input(prompt)
    if allow_default and not Date_str:
        return datetime.today().strptime(date_format)
    
    try :
        valid_date = datetime.strptime(Date_str,date_format)
        return valid_date.strftime(date_format)
    except ValueError :
        print(f"Invalid Date Format , Enter date in {d-m-y} format ")
        return get_date(prompt,allow_default)

def get_amount():
    try :
        amount = float(input("Enter the Amount: "))
        if amount <= 0 :
            raise ValueError("Amount cannot be 0 or Below")
        return amount 
    except ValueError as e :
        print(e)
        return get_amount()

def get_catrgory():
    category  = input("Enter The Category 'I' for Income and 'E' For Expense").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    else :
        print("invalid Category, Please either 'E' or 'I' ")


def get_description():
    return input("Enter a Description")