# Bug & Feature Tracker

entries = []

def add_entry():
    print("\n--- Add New Entry ---")
    
    while True:
        title = input("Enter title/description: ").strip()
        if title:
            break
        print("Title cannot be empty. Please try again.")
        
    while True:
        entry_type = input("Type (Bug/Feature): ").strip().capitalize()
        if entry_type in ['Bug', 'Feature']:
            break
        print("Invalid type. Please enter 'Bug' or 'Feature'.")
        
    while True:
        priority = input("Priority (Low/Medium/High): ").strip().capitalize()
        if priority in ['Low', 'Medium', 'High']:
            break
        print("Invalid priority. Please enter 'Low', 'Medium', or 'High'.")
        
    while True:
        status = input("Status (Open/Resolved): ").strip().capitalize()
        if status in ['Open', 'Resolved']:
            break
        print("Invalid status. Please enter 'Open' or 'Resolved'.")
    
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
        
        choice = input("Select an option (1-4): ").strip()
        
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