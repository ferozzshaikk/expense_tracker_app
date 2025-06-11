from user_data import UserData
from datetime import datetime

# option 1
def get_user_info():
    print("Getting User Data")
    while True:
        name = input("Enter Type (Income/Expense): ").lower().strip()
        if name in ["income", "expense"]:
            break
        print("Invalid Type!")

    category = input("Enter category (e.g: salary, business, etc...):") if name== "income" else input("Enter category (e.g: food, rent, travel, etc...):")

    amount= float(input("Enter amount: "))

    while True:
        get_date = input("Enter date (DD/MM/YYYY): ").strip()
        try:
            datetime.strptime(get_date,"%d/%m/%Y")
            break
        except ValueError:
            print("Invalid date!")

    print(f"You've entered {category} worth ₹{amount}/- in your {name}")

    return UserData(get_date, name, category, amount)

# option 2
def summary():
    print("\nMonthly Summary:\n")
    try:
        monthly_data = {}

        with open("user_data.csv", "r") as file:
            for line in file:
                date, name, category, amount = line.strip().split(", ")
                
                key = datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m")

                if key not in monthly_data:
                    monthly_data[key] = {"income": 0.0, "expense": 0.0}

                if name == "expense":
                    monthly_data[key]["expense"] += float(amount)
                else:
                    monthly_data[key]["income"] += float(amount)


        # Print the summary
        for month, data in monthly_data.items():
            savings = data["income"] - data["expense"]
            print(f"{month}: Income = ₹{data['income']:.2f}, Expense = ₹{data['expense']:.2f}, Savings = ₹{savings:.2f}")

    except FileNotFoundError:
        print("File Not Found!")

# option 3
def save_userdate(data: UserData, data_file_path):
   print(f"\nsaving user data: {data} to {data_file_path}")

   with open(data_file_path, "a")as f:
       f.write(f"{data.date}, {data.name}, {data.category}, {data.amount}\n")
    
# option 4
def load_file_data():
    file_path = input("Enter the file name to load data (.csv): ").strip()
    try:
        with open(file_path, "r") as source_file, open("user_data.csv", "a") as target_file:
            lines = source_file.readlines()
            for line in lines:
                target_file.write(line)
        print("Data loaded successfully from the file.")
    except FileNotFoundError:
        print("File Not Found! Failed to load the data")

def main():
    data_file_path = "user_data.csv"

    print("\n Expense Tracker\n")
    while True:
        print("\n 1.Add Income/Expenses\n 2.View Monthly Summary\n 3.Save Data\n 4.Load Data From a File\n 5.Exit")

        option = input("choose an option: ")
        if option=="1":
            data = get_user_info()
        elif option == "2":
            summary()
        elif option == "3":
            save_userdate(data, data_file_path)
        elif option =="4":
            load_file_data()
        else:
            print("Thank you! Have a nice day.")
            break

if __name__ == "__main__":
    main()