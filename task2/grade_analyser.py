import sys
import os


print(f"sys.argv: {sys.argv}") 


if len(sys.argv) < 2:
    print("Error: No input filename provided.")
    print("Usage: python script_name.py <input_filename>")
    sys.exit(1)


input_filename = sys.argv[1]


if not os.path.isfile(input_filename):
    print(f"Error: The file '{input_filename}' does not exist.")
    sys.exit(1)


output_filename = os.path.splitext(input_filename)[0] + "_out.csv"

try:

    grades = []
    with open(input_filename, "r") as file:
        for line in file:
            try:
                grade = float(line.strip())
                grades.append(grade)
            except ValueError:
                pass 

    print(f"Grades: {grades}")


    if not grades:
        output_content = "No valid grades found.\n"
    else:
        average_grade = round(sum(grades) / len(grades), 2)
        highest_grade = max(grades)
        lowest_grade = min(grades)
        output_content = (
            f"Average Grade: {average_grade:.2f}\n"
            f"Highest Grade: {highest_grade}\n"
            f"Lowest Grade: {lowest_grade}\n"
        )


    print(f"Output Content: {output_content}")


    with open(output_filename, "w") as file:
        file.write(output_content)

    print(f"Processing complete. Results saved to '{output_filename}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found.")
    sys.exit(1)

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)
