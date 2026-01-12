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
    print("--- Security Management System ---")
    
    # 1. הזנה והרצה עבור מניה (Stock)
    print("\n[ Stock Entry ]")
    s_sym = input("Enter Stock Symbol: ")
    s_price = float(input("Enter Price: "))
    s_div = float(input("Enter Dividend Yield (%): "))
    my_stock = Stock(s_sym, "Tech Corp", s_price, s_div)
    print(my_stock.get_details()) # פונקציה מהאבא
    print(f"Dividend: {my_stock.calculate_dividend()}") # פונקציה מהבן

    # 2. הזנה והרצה עבור אג"ח (Bond)
    print("\n[ Bond Entry ]")
    b_sym = input("Enter Bond Symbol: ")
    b_price = float(input("Enter Price: "))
    b_int = float(input("Enter Interest Rate (%): "))
    my_bond = Bond(b_sym, "Gov Bank", b_price, b_int)
    print(my_bond.get_details()) # פונקציה מהאבא
    print(my_bond.get_bond_info()) # פונקציה מהבן

    # 3. הזנה והרצה עבור אופציה (Option)
    print("\n[ Option Entry ]")
    o_sym = input("Enter Option Symbol: ")
    o_price = float(input("Enter Current Price: "))
    o_strike = float(input("Enter Strike Price: "))
    my_option = Option(o_sym, "Trading House", o_price, o_strike)
    print(my_option.get_details()) # פונקציה מהאבא
    print(f"Status: {my_option.check_profitability()}") # פונקציה מהבן

# ד. תשובה עיונית: מהי מטרת ההורשה ומהי תוצאתה
"""
* תשובה כתובה באופן מסודר בקובץ נפרד בגיט
מטרה: לאפשר שימוש חוזר בקוד  על ידי הגדרת תכונות ומתודות משותפות 
במחלקה אחת ומניעת כפילויות בקוד.
תוצאה: יצירת היררכיה של מחלקות שבה מחלקות הבן מקבלות את כל יכולות האב 
ויכולות להוסיף עליהן התנהגות ייחודית משלהן.
"""