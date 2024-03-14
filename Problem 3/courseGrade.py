def calculate_letter_grade(score):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

def courseGrade():
    input_files = ["StudentInfo.tsv", "StudentInfo1.tsv", "StudentInfo2.tsv"]
    
    # Get user input for selecting file
    user_input = input("Enter the file name: ")
    if user_input in input_files:
        input_file = user_input
        output_file = f"report{input_files.index(input_file) + 1}.txt"
    else:
        print("File not found in the list.")
        return

    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

            total_students = len(lines)
            total_midterm1 = 0
            total_midterm2 = 0
            total_final = 0

            with open(output_file, 'w') as output_file:
                for line in lines:
                    parts = line.strip().split('\t')
                    last_name, first_name, midterm1, midterm2, final = parts
                    midterm1 = int(midterm1)
                    midterm2 = int(midterm2)
                    final = int(final)

                    total_midterm1 += midterm1
                    total_midterm2 += midterm2
                    total_final += final

                    average_score = (midterm1 + midterm2 + final) / 3
                    letter_grade = calculate_letter_grade(average_score)

                    output_file.write(f"{last_name}\t{first_name}\t{midterm1}\t{midterm2}\t{final}\t{letter_grade}\n")

                average_midterm1 = total_midterm1 / total_students
                average_midterm2 = total_midterm2 / total_students
                average_final = total_final / total_students

                output_file.write(f"\nAverages: midterm1 {average_midterm1:.2f}, midterm2 {average_midterm2:.2f}, final {average_final:.2f}")

        print(f"Report generated successfully for {input_file}.")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    courseGrade()