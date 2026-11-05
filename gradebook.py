students = {}

# standardizes the inputted marks for straight-forward operations
def normalize_marks(marks):
    if marks is None:
        return []
    if isinstance(marks, (int, float)):
        return [float(marks)]
    if isinstance(marks, str):
        text = marks.strip()
        if not text:
            return []
        return [float(value) for value in text.split()]
    if isinstance(marks, (list, tuple, set)):
        flat_marks = []
        for item in marks:
            flat_marks.extend(normalize_marks(item))
        return flat_marks
    return []


def calculate_class_average(student_data=None):
    #if no inputted student_data used saved students data
    data = students if student_data is None else student_data
    if not data:
        return 0.0

    all_marks = []
    for marks in data.values():
        all_marks.extend(normalize_marks(marks))

    if not all_marks:
        return 0.0

    return sum(all_marks) / len(all_marks)

#calculating the avg
def calculate_average(student_data=None):
    return calculate_class_average(student_data)


def add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("Student name cannot be empty.")
        return

    marks_input = input("Enter marks separated by spaces (leave blank if none): ").strip()
    marks = normalize_marks(marks_input)
    students[name] = marks
    print(f"Added {name} with marks: {marks if marks else 'no marks'}")


def show_menu():
    print("\n=== Grade Book ===")
    print("1. Add student")
    print("2. Calculate class average")
    print("3. View all students")
    print("0. Exit")


def display_class_average():
    if not students:
        print("No students have been added yet.")
        return

    avg = calculate_class_average()
    print(f"Average marks of the entire class: {avg:.2f}")


def display_students():
    if not students:
        print("No students have been added yet.")
        return

    for name, marks in students.items():
        print(f"{name}: {marks}")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_class_average()
        elif choice == "3":
            display_students()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()