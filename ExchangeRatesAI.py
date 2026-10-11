import pandas as pd

class ExchangeRates:
    def __init__(self, filename):
        # Read exchange rate file
        df = pd.read_csv(filename)

        # Get the latest row
        latest_row = df.iloc[-1]

        # Get latest USD/CAD exchange rate
        self.usd_cad_rate = float(latest_row["FXAUSDCAD"])

    def convert(self, amount, from_currency, to_currency):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency == to_currency:
            return amount

        # USD -> CAD
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.usd_cad_rate

        # CAD -> USD
        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.usd_cad_rate

        else:
            raise ValueError("Currency must be USD or CAD.")


def format_currency(amount, currency):
    symbol = "$"
    return f"{symbol}{amount:,.2f} {currency}"


# Main Program
if __name__ == "__main__":

    rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

    amount = float(input("Enter amount: "))
    from_currency = input("Convert FROM (USD/CAD): ")
    to_currency = input("Convert TO (USD/CAD): ")

    converted_amount = rates.convert(amount, from_currency, to_currency)

    print("\nConversion Result")
    print(f"{format_currency(amount, from_currency.upper())} = "
          f"{format_currency(converted_amount, to_currency.upper())}")