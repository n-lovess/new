grades = [75, 88, 92, 67, 85]

average_grade = round(sum(grades) / len(grades), 2)
highest_grade = max(grades)
lowest_grade = min(grades)

with open("grades_output.txt", "w") as file:
    file.write(f"Average Grade: {average_grade:.2f}\n")
    file.write(f"Highest Grade: {highest_grade}\n")
    file.write(f"Lowest Grade: {lowest_grade}\n")