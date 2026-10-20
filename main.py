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

def view_entries():
    print("\n--- All Entries ---")
    if len(entries) == 0:
        print("No entries recorded yet.")
    else:
        for i, entry in enumerate(entries, 1):
            print(f"{i}. [{entry['type']}] {entry['title']} | Priority: {entry['priority']} | Status: {entry['status']}")

def display_summary():
    print("\n--- Summary Statistics ---")
    total = len(entries)
    bugs = sum(1 for e in entries if e['type'].lower() == 'bug')
    features = sum(1 for e in entries if e['type'].lower() == 'feature')
    open_entries = sum(1 for e in entries if e['status'].lower() == 'open')
    resolved_entries = sum(1 for e in entries if e['status'].lower() == 'resolved')
    
    print(f"Total entries: {total}")
    print(f"Bugs: {bugs}")
    print(f"Features: {features}")
    print(f"Open: {open_entries}")
    print(f"Resolved: {resolved_entries}")

def main():
    while True:
        print("\n=== Bug & Feature Tracker ===")
        print("1. Add an Entry")
        print("2. View All Entries")
        print("3. Display Summary Statistics")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            display_summary()
        elif choice == '4':
            print("Exiting tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()