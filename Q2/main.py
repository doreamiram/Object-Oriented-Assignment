#שאלה 2
# סעיף 2: הורשה
#א. הגדרת מחלקת אב מסוג נייר ערך הכוללת לפחות 3 תכונות ופונקציה אחת
class Security:
    def __init__(self, symbol, issuer, current_price):
        self.symbol = symbol          # תכונה 1
        self.issuer = issuer          # תכונה 2
        self.current_price = current_price  # תכונה 3

    def get_details(self): # פונקציה במחלקת האב
        return f"Symbol: {self.symbol}, Issuer: {self.issuer}, Price: {self.current_price}"

# ב. ביצוע הורשה לשלושה סוגי ניירות: מניה, אג"ח ואופציה 
# הוספת לפחות תכונה אחת ומתודה אחת לכל אחד מהם 

class Stock(Security): # מניה
    def __init__(self, symbol, issuer, current_price, dividend_yield):
        super().__init__(symbol, issuer, current_price)
        self.dividend_yield = dividend_yield # תכונה נוספת

    def calculate_dividend(self): # מתודה נוספת
        return self.current_price * (self.dividend_yield / 100)

class Bond(Security): # אג"ח
    def __init__(self, symbol, issuer, current_price, interest_rate):
        super().__init__(symbol, issuer, current_price)
        self.interest_rate = interest_rate # תכונה נוספת

    def get_bond_info(self): # מתודה נוספת
        return f"Annual Interest: {self.interest_rate}%"

class Option(Security): # אופציה
    def __init__(self, symbol, issuer, current_price, strike_price):
        super().__init__(symbol, issuer, current_price)
        self.strike_price = strike_price # תכונה נוספת

    def check_profitability(self): # מתודה נוספת
        if self.current_price > self.strike_price:
            return "In the Money"
        return "Out of the Money"

# ג. קליטת ערכים, יצירת מופעים וקריאה למתודות 
if __name__ == "__main__":
    print("--- Security System Setup ---")
    
    # קלט לדוגמה עבור מניה
    sym = input("Enter Security Symbol: ")
    price = float(input("Enter Current Price: "))
    div = float(input("Enter Dividend (%): "))
    
    # יצירת מופע של מניה
    my_stock = Stock(sym, "Financial Corp", price, div)
    
    # קריאה למתודות (גם של האב וגם של הבן)
    print("\n--- Output ---")
    print(my_stock.get_details())
    print(f"Dividend Payment: {my_stock.calculate_dividend()}")

    # יצירת מופע של אג"ח להדגמה
    my_bond = Bond("GOV_IL", "Israel Gov", 100, 2.5)
    print(my_bond.get_bond_info())

# ד. תשובה עיונית: מהי מטרת ההורשה ומהי תוצאתה
"""
מטרה: לאפשר שימוש חוזר בקוד  על ידי הגדרת תכונות ומתודות משותפות 
במחלקה אחת ומניעת כפילויות בקוד.
תוצאה: יצירת היררכיה של מחלקות שבה מחלקות הבן מקבלות את כל יכולות האב 
ויכולות להוסיף עליהן התנהגות ייחודית משלהן.

"""
