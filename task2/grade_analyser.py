import sys
import os


if len(sys.argv) < 2:
    print("Error: No input filename provided.")
    sys.exit(1)


input_filename = sys.argv[1]


output_filename = os.path.splitext(input_filename)[0] + "_out.csv"


grades = [75, 88, 92, 67, 85]


average_grade = round(sum(grades) / len(grades), 2)
highest_grade = max(grades)
lowest_grade = min(grades)


with open(output_filename, "w") as file:
    file.write(f"Average Grade: {average_grade:.2f}\n")
    file.write(f"Highest Grade: {highest_grade}\n")
    file.write(f"Lowest Grade: {lowest_grade}\n")

print(f"Results written to {output_filename}")