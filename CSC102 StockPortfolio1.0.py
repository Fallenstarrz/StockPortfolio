#####################################################################################################################################################################################
#                                                                                                                                                                                   #
# In this assignment you will build the first part of a stock portfolio manager.                                                                                                    #
# The manager program will consist of the following dictionaries:                                                                                                                   #
#    1. The first dictionary, called Names, maps the stock symbol to the company name (example: "GM" maps to "General Motors").                                                     #
#    2. The second dictionary, called Prices, maps the stock symbol to a list of 2 floating point numbers corresponding to the buy price (the price the user paid for the stock)    #
#       and the current market price (the price the user could sell the stock for today).                                                                                           #
#    3. The third dictionary, called Exposure, maps the stock symbol to a list of 2 floating point numbers, corresponding to the number of shares purchased,                        #
#       and the risk associated with holding onto the stock (i.e. How likely the stock is to gain value in the future).                                                             #
#       The risk associated with holding onto the stock should be a percentage                                                                                                      #
#       (the stock is high risk so the exposure value would be .5 or the stock is low risk so the exposure value would be .05)                                                      #
#                                                                                                                                                                                   #
# Your program should have the following functions:                                                                                                                                 #
#    1. addName - Asks the user for a Stock Symbol and Name pairing then adds it to the Names dictionary.                                                                           #
#    2. addPrices - Takes a Stock Symbol as an input parameter, then asks the user for the Buy price and the Current price of the corresponding stock,                              #
#                   adding them to the Prices dictionary.                                                                                                                           #
#    3. addExposure - Takes a Stock Symbol as an input parameter, then asks the user for the Risk and Shares of the corresponding stock,                                            #
#                    adding them to the Exposure dictionary.                                                                                                                        #
#    4. addStock - Calls addName, addPrices, and addExposure to add a new stock to the portfolio.                                                                                   #
#    5. main – This should have no parameters but should create 2 stocks which means 2 entries in each dictionary with the key in each dictionary being the stock symbol.           #
#              Then, the program should display all the information for each stock.                                                                                                 #
#                                                                                                                                                                                   #
#    Be sure to use comments for both structure of the program and documentation of the code.                                                                                       #
#    All code must completely be your own individual work product.                                                                                                                  #
#                                                                                                                                                                                   #
#####################################################################################################################################################################################

NAMES = {} 
PRICES = {}
EXPOSURE = {}

def validMenu(y):                                                                                                       # This checks to see that the menu option is valid
    while True:                                                                                                         
        if (str.isdigit(y)):                                                                                            
            y = int(y)                                                                                                  
            if y >= 1 and y <= 5:
                return (y)                                                                                              
            else:
                y = input('Please select a valid option\n')
        else:                                                                                                           
            y = input('Please select a valid option\n')                                                                 
    
def validInput(x):                                                                                                      # Checks to see that the input is a number and turns it into an int                                                        
    while True:                                                                                                         
        if (str.isdigit(x)):                                                                                            
            x = int(x)                                                                                                 
            return (x)                                                                                              
        else:                                                                                                       
            x = input('Please select a valid integer\n')                                                                
      
def validFInput(z):                                                                                                     # This checks to see that the float is valid
    while True:     
        if(z.replace('.', '', 1).isdecimal()):
            z = float(z)
            return(z)
        else:
            z = input('Please select a valid floating point value')

def makeMoney(b):                                                                                                       # Make and format an input into American currency
    b = '${:,.2f}'.format(b)
    return(b)

def makePercent(a):                                                                                                     # Make and format an input into a percentage
    a = '{:,.0%}'.format(a)
    return(a)

def mainMenu(x):                                                                                                        # This is the main menu
    print()
    print('Stock Portfolio')
    print('---------------')
    print('1. Search Stocks')
    print('2. Create New Stock')
    print('3. Edit Stock in Portfolio')
    print('4. Recommend Sale in Portfolio')
    print('5. Close Program')
    print()

    x = input('What would you like to do? ')
    x = validMenu(x)
    return(x)

def editMenu(x):                                                                                                        # This is the edit menu
    print()
    print('Stock Portfolio')
    print('---------------')
    print('1. Return to previous menu')
    print('2. Edit Company Name or Company Symbol')
    print('3. Edit Buy and Sell Price')
    print('4. Edit Risk or Number of shares owned')
    print()

    x = input ('')
    x = validMenu(x)
    if x > 5:
        x = input('Please Select a valid option')
    return(x)

def searchMenu(NAMES):                                                                                                  # This is the search menu. This will generate a menu
    num = 1                                                                                                             # that will grow as you add more companies to your dictionary
    print()
    print('Stock Portfolio')
    print('---------------')
    print('0. Previous Menu')
    for i in NAMES:
        print(num,'. ', i, sep='')
        num += 1   
    x = input ('Which Stock would you like to explore? ')
    x = validInput(x)
    while ((x > num) or (x < 0)):
        x = input('Please select a valid company in your portfolio.')
        x = validInput(x)
    return(x)

def addName(NAMES):                                                                                                     # Adds Names to your dictionary list
    stockSymbol = input('Please input the company symbol. ')
    stockName = input('Please input the company name. ')
    NAMES[stockSymbol] = [stockName]
    PRICES[stockSymbol] = None
    EXPOSURE[stockSymbol] = None
    return(NAMES)
    
def addPrices(PRICES):                                                                                                  # Adds prices to stock symbols
    while True:
        stockSymbol = input('Please input the company symbol. ')
        if stockSymbol in PRICES:
            buyPrice = input('How much does this stock cost to purchase? ')
            buyPrice = validFInput(buyPrice)
            buyPrice = makeMoney(buyPrice)
            sellPrice = input('How much does this stock sell for? ')
            sellPrice = validFInput(sellPrice)
            sellPrice = makeMoney(sellPrice)
            PRICES[stockSymbol] = [buyPrice, sellPrice]
            return (PRICES)
        else:
            print('This symbol does not exist.')

def addExposure(EXPOSURE):                                                                                              # Adds risk and shared owned to stock symbols
    while True:
        stockSymbol = input('Plese input the company symbol. ')
        if stockSymbol in EXPOSURE:
            ownedShares = input('How many shares do you own? ')
            ownedShares = validFInput(ownedShares)
            risk = input('What is the risk of owning this share? ')
            risk = validFInput(risk)
            risk = makePercent(risk)
            EXPOSURE[stockSymbol] = [ownedShares, risk]
            return(EXPOSURE)
        else:
            print('This symbol does not exist.')

def addStock(NAMES, PRICES, EXPOSURE):                                                                                  # Calls the three add functions to create a stock in your stock portfolio
    NAMES = (addName(NAMES))
    PRICES = (addPrices(PRICES))
    EXPOSURE = (addExposure(EXPOSURE))
    print('Successfully Placed Stock in Portfolio')
    return(NAMES, PRICES, EXPOSURE)

def searchPortfolio(NAMES, PRICES, EXPOSURE):                                                                           # This Searches through the company symbol keys and will return all of
    while True:                                                                                                         # elements belonging to that stock symbol
        explore = searchMenu(NAMES)
        search = list(NAMES.keys())
        search.insert(0, 'Previous Menu')
        if explore == 0:
            return()
        else:
            print(NAMES.get(search[explore]))
            print(PRICES.get(search[explore]))
            print(EXPOSURE.get(search[explore]))

def editPortfolio(NAMES, PRICES, EXPOSURE):                                                                             # This will let you hop into a stock symbol and the values of it's elements
    previous = 1
    editNames = 2
    editPrices = 3
    editRisk = 4
    
    decision = 0
    
    while decision != previous:
        decision = editMenu(decision)
        if decision == previous:
            return()
        elif decision == editNames:
            addStock(NAMES, PRICES, EXPOSURE)
        elif decision == editPrices:
            addPrices(PRICES)
        elif decision == editRisk:
            addExposure(EXPOSURE)
    return(NAMES, PRICES, EXPOSURE)

def getSale():                                                                                                          # This is the assignment for next week
    print ('\nTo be implemented in StockPortfolio2.0')
    return()

def main():                                                                                                             # This is the main program/Loop
    searchStocks = 1
    newStock = 2
    editStock = 3
    recommendSale = 4
    leaveProgram = 5 

    choice = 0
    
    while choice != leaveProgram:                                                                                       
        choice = mainMenu(choice)                                                                                       # Calls the main menu
        if choice == searchStocks:
            searchPortfolio(NAMES, PRICES, EXPOSURE)                                                                    # Calls searchPortfolio function to search for items in your portfolio
        elif choice == newStock:
            addStock(NAMES, PRICES, EXPOSURE)                                                                           # calls addStock function to add new stocks to your portfolio
        elif choice == editStock:
            editPortfolio(NAMES, PRICES, EXPOSURE)                                                                      # calls the editPortfolio function to edit stocks in your portfolio
        elif choice == recommendSale:
            getSale()                                                                                                   # This is not yet implemented
    input('Press ENTER to Close Portfolio')

main()
