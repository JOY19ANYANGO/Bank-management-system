from view_records import  list_all_customers,list_transactions_for_customer,list_accounts_for_customer

def main():
    while True:
        print("Options:")
        print("1. Press 'S' to see records.")
        print("2. Press 'Q' to quit.")
        
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == 's':
            view_records_menu()
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def view_records_menu():
    while True:
        print("\nView Records Menu:")
        print("1. Press 'C' to see all customers.")
        print(". Press 'T' to see transaction records for a specific customer.")
        print("4. Press 'A' to see account records for a specific customer.")
        print("2. Press 'B' to go back to the main menu.")
        
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == 'c':
            list_all_customers()
        elif choice == 't':
            transaction_records() 
        elif choice == 'a':
            account_records()       
        elif choice == 'b':
            print("Returning to the main menu.")
            break
        else:
            print("Invalid choice. Please try again.")
def transaction_records():
    print("\nView transactions for a customer:")
    customer_id = input("Enter the ID of the customer: ").strip()

    if customer_id:
        try:
            customer_id = int(customer_id)
            list_transactions_for_customer(customer_id)
           
        except ValueError:
            print("Invalid customer ID. Please enter a valid id")
def account_records():
    print("\nView accounts for a customer:")
    customer_id = input("Enter the ID of the customer: ").strip()

    if customer_id:
        try:
            customer_id = int(customer_id)
            list_accounts_for_customer(customer_id)
           
        except ValueError:
            print("Invalid customer ID. Please enter a valid id")
            

if __name__ == "__main__":
    main()


