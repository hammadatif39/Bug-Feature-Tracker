# Bug & Feature Tracker

entries = []

def add_entry():
    print("\n--- Add New Entry ---")
    title = input("Enter title/description: ")
    entry_type = input("Type (Bug/Feature): ")
    priority = input("Priority (Low/Medium/High): ")
    status = input("Status (Open/Resolved): ")
    
    entry = {
        "title": title,
        "type": entry_type,
        "priority": priority,
        "status": status
    }
    entries.append(entry)
    print("Entry added successfully!")

def main():
    while True:
        print("\n=== Bug & Feature Tracker ===")
        print("1. Add an Entry")
        print("2. Exit")
        
        choice = input("Select an option (1-2): ")
        
        if choice == '1':
            add_entry()
        elif choice == '2':
            print("Exiting tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()