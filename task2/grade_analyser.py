import csv

def classify_grade(average):
    if average >= 70:
        return '1'
    elif average >= 60:
        return '2:1'
    elif average >= 50:
        return '2:2'
    elif average >= 40:
        return '3'
    else:
        return 'F'

def analyze_grades(filename):
    output_filename = f"{filename}_out.csv"

    with open(filename, mode='r') as infile, open(output_filename, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            student_id = row[0]
            grades = [int(grade) for grade in row[1:] if grade]  # Ignore empty cells
            
            if grades:  
                average_grade = sum(grades) / len(grades)
            else:
                average_grade = 0 
            
            classification = classify_grade(average_grade)

            writer.writerow([student_id, f"{average_grade:.2f}", classification])
    
    print(f"Data written to {output_filename}")

filename = input("Enter the filename of the student file: ")
analyze_grades(filename)