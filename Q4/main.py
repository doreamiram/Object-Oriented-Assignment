# שאלה 4
# פונקציה נפרדת לבדיקה האם מספר אחד הוא מכפלה של השני (סעיף א)
def is_multiple(n1, n2):
    # בדיקה ששני המספרים אינם אפס כדי למנוע שגיאת חילוק ב-0
    if n1 == 0 or n2 == 0:
        return n1 == n2
    return n1 % n2 == 0 or n2 % n1 == 0

def main():
    print("Welcome to the Multiple Checker. Enter -1 at any time to exit.")
    
    while True:
        try:
            # קליטת המספר הראשון
            num1 = int(input("Enter first number: "))
            if num1 == -1: # תנאי יציאה (סעיף ב)
                break
            
            # קליטת המספר השני
            num2 = int(input("Enter second number: "))
            if num2 == -1: # תנאי יציאה (סעיף ב)
                break
            
            # קריאה לפונקציה והצגת התוצאה
            if is_multiple(num1, num2):
                print(f"Yes! One of the numbers is a multiple of the other.")
            else:
                print(f"No, neither number is a multiple of the other.")
                
        except ValueError:
            print("Please enter valid integers only.")

    print("Process finished.")

if __name__ == "__main__":

    main()
