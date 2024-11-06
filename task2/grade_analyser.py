import sys
import os


if len(sys.argv) < 2:
    print("Error: No input filename provided.")
    sys.exit(1)


input_filename = sys.argv[1]


output_filename = os.path.splitext(input_filename)[0] + "_out.csv"

try:

    with open(input_filename, "r") as file:
        grades = [float(line.strip()) for line in file if line.strip().isdigit()]


    if not grades:
        raise ValueError("No valid grades found in the file.")


    average_grade = round(sum(grades) / len(grades), 2)
    highest_grade = max(grades)
    lowest_grade = min(grades)


    with open(output_filename, "w") as file:
        file.write(f"Average Grade: {average_grade:.2f}\n")
        file.write(f"Highest Grade: {highest_grade}\n")
        file.write(f"Lowest Grade: {lowest_grade}\n")

    print(f"Results written to {output_filename}")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found.")
    sys.exit(1)

except ValueError as ve:
    print(f"Error: {ve}")
    with open(output_filename, "w") as file:
        file.write("No valid grades found.\n")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)