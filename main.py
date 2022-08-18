from machine_data import profit,bank,choice,machine_on,MENU,resources,change
import os

def coffee_menu(menu):
    '''Show the coffee menu available for the customer'''
    espresso_cost = menu['espresso']['cost']
    capuccino_cost = menu['cappuccino']['cost']
    latte_cost = menu['latte']['cost']
    
    
    print(f"\nWhat would you like?\n\nespresso: ${espresso_cost}\ncappuccino: ${capuccino_cost}\nlatte: ${latte_cost}")
    
def report(machine_resources,net_profit):
    '''Report of the coffee machine resources'''
    print(f"\nWater: {machine_resources['water']}ml\nMilk: {machine_resources['milk']}ml\nCoffee: {machine_resources['coffee']}g\nMoney: ${net_profit}")

def product_check(user_choice,menu,machine_resources):
    '''Check product resources'''
    for ingredient in menu[user_choice]['ingredients']:
        
        coffee_ingredient = menu[user_choice]['ingredients'].get(ingredient)
        machine_resource = machine_resources.get(ingredient)
        
        if coffee_ingredient <= machine_resource:
            return True
        else:
            
            #! The output is printing more than one. Need to resolve this issue.
            #! Issue Priority Level: NORMAL
            
            print(f"Sorry there is not enough {ingredient}.")
            return False
            
def process_coin():
    '''Insert coins and return the monetary value'''
    
    quarter_value = 0.25
    dime_value = 0.10
    nickle_value = 0.05
    pennie_value = 0.01
    
    quarter = int(input("\nHow many quarters? "))
    dime = int(input("\nHow many dimes? "))
    nickle = int(input("\nHow many nickles? "))
    pennie = int(input("\nHow many pennies? "))
    
    total = quarter_value*quarter + dime_value*dime + nickle_value*nickle + pennie_value*pennie
    
    return total

def transaction(inserted_money,net_profit,machine_bank,coffee_cost,money_change):
    '''Transaction payment'''
    
    if(inserted_money == coffee_cost):
        
       
        
        return True
    
    elif(inserted_money > coffee_cost):
        
        money_change = round(inserted_money - coffee_cost,2)
        machine_bank -= money_change
        
        
        
        print(f"\nHere is ${money_change} dollars in change.")
        
        return True
    
    else:
        
        print("\nSorry that's not enough money. Money refunded")
        
        return False
        
def make_coffee(user_choice,menu,machine_resources):
    '''Prepare the coffee selected'''
    
    for ingredient in menu[user_choice]['ingredients']:
        
        machine_resources[ingredient] = machine_resources.get(ingredient) - menu[user_choice]['ingredients'].get(ingredient)
        
  
while(machine_on == True):
    
    coffee_menu(MENU)
    
    choice = input("\nEnter: ").lower()
    
    if(choice == 'espresso' or choice == 'cappuccino' or choice == 'latte'):
        
        #// TODO -> Check resources
        #! Issue Level: Normal
        product_check(choice,MENU,resources)
        
        if product_check(choice,MENU,resources) == True:
            #// TODO -> Transation Payment  
           money_inserted = process_coin() # Money inserted for the purchase
           product_cost = MENU[choice]['cost'] # Price of the product selected
           
           payment = transaction(money_inserted,profit,bank,product_cost,change) 
           
           if(payment == True):
               
               # TODO -> Prepare the product
               
               profit += round(product_cost,2)
               
               make_coffee(choice,MENU,resources)
               
               print(f"\nHere's your {choice}. Enjoy!")
               
           else:
               machine_on = True
               
          
    elif(choice == 'report'):
        
        #// TODO -> Report of the machine resources (including profits)
        
        report(resources,profit)
        
    elif(choice == 'off'):
        
        machine_on = False
        
    else:
        os.system('cls')
        machine_on = True