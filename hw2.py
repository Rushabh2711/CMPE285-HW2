#Python Stock Profit Calculator - Individual Homework 
 
def Proceeds(finalSharePrice, allotment):
    #Proceeds = Final Share Price * Allotment
    return finalSharePrice * allotment

def PurchasePrice(initialSharePrice, allotment):
    #Purchase Price = initialSharePrice * allotment
    return initialSharePrice * allotment

def RawProfit(initialSharePrice, finalSharePrice, allotment, buyCommission, sellCommission):
    #Raw Profit = (Final Share Price - Initial Share Price) * Allotment - Buy Commission - Sell Commission
    return (finalSharePrice - initialSharePrice) * allotment  - buyCommission - sellCommission

def Tax(rawProfit, taxPercentage):
    #Tax = Raw Profit * Tax Rate%
    return rawProfit * taxPercentage / 100

def BreakEvenPrice(initialSharePrice, allotment, buyCommission, sellCommission):
    #ToBreakEvenPrice = (Buy Commission + Sell Commission) / Allotment +  Initial Share Price
    return (buyCommission + sellCommission) / allotment + initialSharePrice

def TwoDecimal(floatNum):
    #String of floating number with only two decimals
    return "%.2f" % floatNum

CURR = "$"


#Input from User
print ("**********************************")
print ("WELCOME TO STOCK PROFIT CALCULATOR")
print ("**********************************\n")
print ("Compute Your Profit \n")

Symbol = input("Please enter Ticker Symbol:\n")
allotment = int(input("\nAllotment?\n"))
finalSharePrice = float(input("\nFinal Share Price?\n"))
sellCommission = float(input("\nSell Commission?\n"))
initialSharePrice = float(input("\nInitial Share Price?\n"))
buyCommission = float(input("\nBuy Commission?\n"))
taxPercentage = float(input("\nCapital Gain Tax Rate?\n"))


# Computing values for user
pp = PurchasePrice(initialSharePrice, allotment)
rawProfit = RawProfit(initialSharePrice, finalSharePrice, allotment, buyCommission, sellCommission)
tax = Tax(rawProfit, taxPercentage)
cost = pp + buyCommission + sellCommission + tax
netP = rawProfit - tax

#Showing result to user
print("")
print ("YOUR PROFIT REPORT:")
print ("----------------------------------\n")
print ("Proceeds")
print (CURR + TwoDecimal(Proceeds(finalSharePrice, allotment)) + "\n")
print ("Cost")
print (CURR + str(cost) + "\n")
print ("Cost details:")
print ("Total Purchase Price:")
print (str(allotment) + " x " + CURR + str(initialSharePrice) + " = " + str(pp))
print ("Buy Commission = " + TwoDecimal(buyCommission))
print ("Sell Commission = " + TwoDecimal(sellCommission))
print ("Net Profit:")
print (CURR + TwoDecimal(netP) + "\n")
print ("Return on Investment:")
print (TwoDecimal(100 + (netP - cost) / cost * 100) + "%" + "\n")
print ("To break even, you should have a final share price of ")
print (CURR + TwoDecimal(BreakEvenPrice(initialSharePrice, allotment, buyCommission, sellCommission)))