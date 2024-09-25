def calculate_min_final_exam(mark_midterm_avg):
    # Calculate the minimum final exam mark needed to pass the course
    min_final_exam_mark = 50 - (mark_midterm_avg * 0.6) / 0.4
    
    # First condition check
    if min_final_exam_mark > 100:
        return 100
    
    # Second condition check
    if min_final_exam_mark < 50:
        # Check if the student can still pass with the current average
        if (min_final_exam_mark * 0.4 + mark_midterm_avg * 0.24) >= 32:
            return min_final_exam_mark
        else:
            # Calculate the minimum final exam mark needed to pass the test component
            min_final_exam_mark = (32 - (mark_midterm_avg * 0.24)) / 0.4
            return max(min_final_exam_mark, 50)  # Ensure at least 50%
    
    return min_final_exam_mark

def main():
    # Get user input for term average and midterm average
    term_avg = float(input("Enter your term average (0-100): "))
    midterm_avg = float(input("Enter your midterm test average (0-100): "))
    
    # Calculate the minimum final exam mark needed
    min_final_mark = calculate_min_final_exam(midterm_avg)
    
    # Display the result
    print(f"You need a minimum mark of {min_final_mark:.2f}% in the final exam to pass ENGI 1020.")

if __name__ == "__main__":
    main()
