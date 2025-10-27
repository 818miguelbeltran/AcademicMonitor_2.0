#Miguel Beltran
#Oct.26.25
# Miguel's Academic Monitor 2.0 (W3D5 Final Version)
# Meets W3D5 requirements: 4 functions, f-strings, error handling, complex feature (Loop/Condition/Return).

import sys

# --- FUNCTION 1: Help Menu ---
def show_help():
    """Prints usage instructions for the CLI tool."""
    print("=======================================================")
    print("             Miguel's Academic Monitor 2.0 HELP        ")
    print("=======================================================")
    print("Purpose: Compares current GPA to your target goal and provides")
    print("         targeted advice on your weakest assignment area.")
    print("\nHow to Use:")
    print("1. Enter your Target GPA (e.g., 4.0).")
    print("2. Enter the decimal weights (e.g., 0.20) for Quizzes, Exams, and Projects.")
    print("3. Enter your current overall GPA.")
    print("4. Enter scores for each assignment type.")
    print("\nTip: If you are behind your goal, the tool identifies the area (Quiz/Exam/Project)")
    print("     with the lowest score percentage to maximize your study focus.")
    print("=======================================================")

# --- FUNCTION 2: Initial Setup & Error Handling (Returns setup data) ---
def get_initial_setup():
    """Collects essential setup data (course name, GPA goal, weights)."""

    
    # Check if the user wants help before proceeding
    if input("Type 'help' for instructions or press Enter to continue: ").lower() == 'help':
        show_help()
        # Optionally exit after showing help, or let the user rerun the script.
        # For this version, we exit to keep the flow clean.
        sys.exit(0)

    try:
        print("--- Academic Monitor 2.0 Setup ---")

        # Add personalized course name input
        course_name = input("Enter Course Name (e.g., Intro to Sociology 01): ")

        required_gpa = float(input("Enter Your Target GPA Goal (e.g., 4.0): "))
        current_gpa = float(input("Enter Your Current Overall GPA (e.g., 3.6): "))

        print("\n--- Enter Course Weights (e.g., 0.20 for 20%) ---")

        quiz_weight = float(input("Quiz Weight: "))
        exam_weight = float(input("Exam Weight: "))
        project_weight = float(input("Project Weight: "))

        total_weight = quiz_weight + exam_weight + project_weight

        # Condition (Error Handling): Check if weights sum to 1.00
        if round(total_weight, 2) != 1.00:
            print("\nERROR: Weights must sum to 1.00 (100%). Please try again.")
            sys.exit(1)

        
        return required_gpa, current_gpa, quiz_weight, exam_weight, project_weight, course_name

    except ValueError:
        print("\nERROR: Please ensure all inputs are valid numbers (decimals for weights/GPA).")
        sys.exit(1)

# --- FUNCTION 3: Score Input with Loop/Condition (Returns score data) ---
def get_score_inputs():
    """Collects assignment scores using a loop and validation."""
    scores_data = {}
    print("\n--- Enter Assignment Scores ---")

    # Complex Feature: Loop + Condition + Return
    # We use a loop to ensure valid input is received
    assignment_types = ["Quiz", "Exam", "Project"]

    for type in assignment_types:
        while True:  # Loop
            try:
                score = int(input(f"{type} Points Earned: "))
                max_points = int(input(f"{type} Points Max: "))

                # Condition inside loop: Validate score against max points
                if score > max_points:
                    print(f"ERROR: Earned points ({score}) cannot exceed Max points ({max_points}). Try again.")
                    continue  # Loop: Ask for input again

                if max_points == 0:
                    percentage = 0.0
                else:
                    percentage = score / max_points

                scores_data[type] = percentage
                break # Exit the inner loop once valid data is entered
            except ValueError:
                print("ERROR: Please enter whole numbers for scores. Try again.")

    # Return values used in decision (used for calculations/advice)
    return scores_data

# --- FUNCTION 4: Main Logic and Reporting ---
def run_monitor():
    """Runs the full monitoring and reporting process."""

    # Get Setup Data
    required_gpa, current_gpa, quiz_weight, exam_weight, project_weight, course_name = get_initial_setup()

    # Get Score Data
    scores_data = get_score_inputs()

    # --- Calculation Phase ---

    quiz_pct = scores_data.get("Quiz", 0)
    exam_pct = scores_data.get("Exam", 0)
    project_pct = scores_data.get("Project", 0)

    # Calc 1: GPA Difference (Core logic for status)
    gpa_delta = current_gpa - required_gpa

    # Calc 2: Weighted Average Score (Correctly calculates final percentage)
    current_weighted_score = (
        quiz_pct * quiz_weight +
        exam_pct * exam_weight +
        project_pct * project_weight
    ) * 100 

    # Calc 3: Find Weakest Area for Targeted Advice
    scores_for_comparison = {
        "Quiz": quiz_pct,
        "Exam": exam_pct,
        "Project": project_pct
    }
    lowest_type = min(scores_for_comparison, key=scores_for_comparison.get)
    lowest_pct = scores_for_comparison[lowest_type]

    # Calc 4: Determine Status and Advice based on GPA Delta
    if gpa_delta >= 0.2:
        status = "**EXCELLENT**"
        advice = "Significantly above goal. Maintain this effort!"
    elif gpa_delta > 0:
        status = "**ON TRACK**"
        advice = "Meeting goal. Stay focused."
    elif gpa_delta >= -0.1:
        status = "**WARNING**"
        advice = "Close to your required GPA. Focus on the next assignment."
    else: # gpa_delta < -0.1 (REVIEW NEEDED)
        status = "**REVIEW NEEDED**"
        # Targeted advice with line break (\n)
        advice = (
            f"You are currently {abs(gpa_delta):.2f} points below your target. "
            f"Your weakest area is {lowest_type} with a {lowest_pct*100:.0f}% score. \n"
            f"Focus your study efforts on {lowest_type} for the biggest impact."
        )

    # --- Formatted Output (Final Report) ---
    print("\n==================================")
    print(f"   Academic Summary for {course_name}")
    print("==================================")
    print(f"Current GPA: {current_gpa}")
    print(f"Required GPA: {required_gpa}")
    print(f"GPA Difference: {gpa_delta:+.2f} points")
    print(f"Weighted Course Score: {current_weighted_score:.1f}%")
    print("\nSTATUS:", status)
    print("ADVICE:", advice)
    print("==================================")

if __name__ == "__main__":
    run_monitor()
