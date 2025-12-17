import math

def currentr(current_assets,current_liability):
    ca=current_assets
    cl=current_liability

    a=math.gcd(ca,cl)

    numa=ca//a
    numb=cl//a

    return f"{numa}:{numb}"
def quickr(current_assets,current_liability,inventory_if_given=0,pre_paid_expenses_if_any=0):
    qa=int(current_assets-inventory_if_given-pre_paid_expenses_if_any)

    cl=current_liability

    a=math.gcd(qa,cl)

    numa=qa//a
    numb=cl//a

    return f"{numa}:{numb}"
    
def help():
    print("PyAccounting is developed and maintained by Navpreet Singh")
    print("-"*50)
    print("This python module help's to calculate accounting ratio's")
    print("currently there are two accounting ratio's supported")
    print("1. current ratio -> use currentr(current_assets,current_liability)")
    print("2. quick ratio -> use quickr(current_assets,current_liability,inventory_if_given=0,pre_paid_expenses_if_any=0)")
    
