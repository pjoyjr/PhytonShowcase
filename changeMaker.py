#Asks user for which items they would like to buy and ask for their amount paid and figure out
#how much change is required for each bill and coin.
import math ##allows math.ceil to be called

print("Hello, welcome to the vending machine") #greet user
options = ["0. Gum: $.98 ","1. Poptart: $1.99","2. Munchos: $.99","3. M&M's: $.89 ","4. Water: $.99","5. Coca Cola: $1.99","6. Gatorade: $2.00"] ## vending options
optionsAmount = [.98,1.99,.99,.89,.99,1.99,2.00]
a=0 #for loop below
price = 0
while a < 7: ##print options
    print(options[a]) #prints options[a]
    a=a+1 #increment
itemPrice = input("What would you like to buy?(Enter number):") #what item they want
price = optionsAmount[int(itemPrice)] #add item to price
tax = price * .07
print("Your sub total is $" + str(price) + " + a tax of $" + str("%.2f" % tax))
price = price + tax
print("Bringing your grand total to $"+ str("%.2f" % price)) 
paid = float(input("Cash tendered: $")) #ask user for tendered amount and store as float
change = paid - price #find change in float
while change < 0.00: #if underpaid
    addChange = float(input("A balance of $" +"%.2f" % abs(change) + " is remaining. Please tender more money. Money tendered: $")) #ask for more money
    change = addChange + change #add payment to old
print("Change (in dollars):" +"%.2f" % change) #display change and formats float to two decimals
remain = int(change*100) #dollars to cents and int
print("Change (in cents): " + str(remain) +"\n") ##test print

changeTypes = ["Twenties: ","Tens: ","Fives: ","Singles: ","Quarters: ","Dimes: ","Nickels: ","Pennies: "] #declare coins and bills
stack = [] #placeholder for change back
changeMulti = [1,5,10,25,100,500,1000,2000] #values of each type in cents in int

x=0 #for loop, initialize counter
while x < 8: ## loop for amount of values in changeValues
    cMulti = changeMulti.pop()#saves last int in changeMulti to cMulti
    ##print("cMulti is : " + str(cMulti)) ##tests cMulti and works
    z=(remain//cMulti) ##finds how many can be spared
    ##print("z is: " + str(z)) ##test z and works
    stack.append(z) #add amount spared to stack
    remain = remain-(z*cMulti) ##figures out remaining change after deductions from above
    print("Amount of " + str(changeTypes[x]) + " " + str(stack.pop())) ##test print
    x=x+1
    ##print("Remaining: " + str("%.2f" % float(remain))) ##test remain and works!

##print("Change remaining: $" + str("%.2f" % remain))##test print
print("Thank you, come again!") ##say goodbye

