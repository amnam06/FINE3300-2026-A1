#Import the csv file to read the exchange rate file
import csv

#Create a class called ExchangeRates
class ExchangeRates:
    #Constructor initializes the object with the exchange rate file
    def __init__(self, filename):
        self.__rate = 0
        #Open and read the csv file
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            #Loop through each row in the csv file
            for row in reader:
                #Store each USD/CAD rate from each row
                #The final value will be the lastest exchange rate
                self.__rate = float(row["FXAUSDCAD"])

    #Method to convert an amount between USD and CAD
    def convert(self, amount, from_currency, to_currency):
        #Convert USD to CAD by multiplying by the exchange rate
        if from_currency == "USD" and to_currency == "CAD":
            result = amount * self.__rate
        #Convert CAD to USD by dividing by the exchange rate
        elif from_currency == "CAD" and to_currency == "USD":
            result = amount / self.__rate 
        #If both currencies are the same, no conversion is needed
        elif from_currency == to_currency:
            result = amount
        #If another currency is entered, display error
        else:
            print ("Invaild currency")
            return None
        #Return the converted amount
        return result

#Main program
if __name__ == "__main__":
    #Welcome message
    print("Welcome to the USD/CAD exhange rate calculator!")
    #Create an ExchangeRates object using the csv file
    exchange = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")
    #Ask the user which amount they want to convert
    amount = float(input("Enter amount: "))
    #Ask the user which currency they are converting from
    from_currency = input("Enter the currency you are converting from: ").upper()
    #Ask the user which currency they are converting to
    to_currency = input("Enter the currency you are converting to: ").upper()
    #Convert the amount
    result = exchange.convert(amount, from_currency, to_currency)

    #Display the results
    if result is not None:
        print("${:.2f} {} = ${:.2f} {}".format(
            amount, from_currency, result, to_currency))
    else:
        print("Invaild currency entered")