students = {}

def show_menu():
    print("\n=== Grade Book ===")
    print("1. Add Student & Grades")
    print("2. Calculate Average Marks")
    print("0. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Enter student name: ")
            try:
                grades_input = input("Enter marks separated by spaces (e.g., 85 90 78): ")
                grades = [float(g) for g in grades_input.split()]
                students[name] = grades
                print(f"Grades added for {name}!")
            except ValueError:
                print("Invalid input! Please enter numbers for marks.")
                
        elif choice == "2":
            name = input("Enter student name to find average: ")
            if name in students:
                grades = students[name]
                if grades:
                    avg = sum(grades) / len(grades)
                    print(f"Average marks for {name}: {avg:.2f}")
                else:
                    print("No grades found for this student.")
            else:
                print("Student not found!")
                
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 0, 1, or 2.")

if __name__ == "__main__":
    main()