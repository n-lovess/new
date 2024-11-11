import csv

# Define function to classify average grades
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

# Main function to process the student data
def analyze_grades(filename):
    output_filename = f"{filename}_out.csv"
    
    # Open the input and output CSV files
    with open(filename, mode='r') as infile, open(output_filename, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Process each row in the input file
        for row in reader:
            # Extract student ID and grades
            student_id = row[0]
            grades = [int(grade) for grade in row[1:] if grade]  # Ignore empty cells
            
            # Calculate average grade
            if grades:  # Avoid division by zero if no grades are found
                average_grade = sum(grades) / len(grades)
            else:
                average_grade = 0  # Default to 0 if no grades are provided
            
            # Determine classification
            classification = classify_grade(average_grade)
            
            # Write result to output file with average grade rounded to 2 decimal places
            writer.writerow([student_id, f"{average_grade:.2f}", classification])
    
    print(f"Data written to {output_filename}")

# Request filename input from user and analyze grades
filename = input("Enter the filename of the student file: ")
analyze_grades(filename)