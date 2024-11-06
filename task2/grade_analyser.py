import sys
import os

# Ensure the input filename is passed as a command-line argument
if len(sys.argv) < 2:
    print("Error: No input filename provided.")
    sys.exit(1)

# Capture the input filename from the arguments
input_filename = sys.argv[1]
output_filename = os.path.splitext(input_filename)[0] + "_out.csv"

try:
    # Read grades from the input file, processing only valid numbers
    grades = []
    with open(input_filename, "r") as file:
        for line in file:
            try:
                grade = float(line.strip())
                grades.append(grade)
            except ValueError:
                pass  # Ignore non-numeric entries

    # Prepare the output content based on the grades available
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

    # Write the output content to the output file
    with open(output_filename, "w") as file:
        file.write(output_content)

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found.")
    sys.exit(1)

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)