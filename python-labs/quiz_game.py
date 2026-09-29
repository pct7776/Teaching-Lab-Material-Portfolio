import sys

def run_quiz():
    # 1. Define the quiz database using a nested dictionary structure
    quiz_bank = {
        "Which of the following is an open-source operating system?": {
            "options": ["A. Windows", "B. macOS", "C. Linux", "D. iOS"],
            "correct_option": "C"
        },
        "What does HTML stand for?": {
            "options": [
                "A. Hyper Text Markup Language", 
                "B. High Text Machine Language", 
                "C. Hyper Transfer Multi Language", 
                "D. Home Tool Markup Language"
            ],
            "correct_option": "A"
        },
        "Which programming language is widely known for its simple readability and dynamic typing?": {
            "options": ["A. C++", "B. Python", "C. Java", "D. Assembly"],
            "correct_option": "B"
        },
        "In a relational database tracking systems, what does 'DBMS' stand for?": {
            "options": [
                "A. Data Base Management System", 
                "B. Digital Binary Machine Structure", 
                "C. Data Backup Main Server", 
                "D. Distributed Business Memory Storage"
            ],
            "correct_option": "A"
        }
    }

    score = 0
    total_questions = len(quiz_bank)

    print("==================================================")
    print("      Welcome to the Terminal Quiz Challenge      ")
    print("==================================================\n")

    # 2. Iterate through the dictionary items to serve questions
    for index, (question, data) in enumerate(quiz_bank.items(), 1):
        print(f"Question {index}: {question}")
        
        # Display the corresponding array list options
        for option in data["options"]:
            print(f"  {option}")
        
        # 3. Capture input safely and format to uppercase
        user_choice = input("\nYour Answer (A, B, C, or D): ").strip().upper()

        # 4. Input validation loop
        while user_choice not in ["A", "B", "C", "D"]:
            print("Invalid choice! Please enter only the letters A, B, C, or D.")
            user_choice = input("Your Answer (A, B, C, or D): ").strip().upper()

        # 5. Evaluate answer logic and provide feedback
        if user_choice == data["correct_option"]:
            print("🎉 Correct! Great job.\n")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was option '{data['correct_option']}'.\n")
            
        print("-" * 50)

    # 6. Process and display final stats calculation
    percentage = (score / total_questions) * 100
    print("\n==================================================")
    print("                   QUIZ OVER!                     ")
    print("==================================================")
    print(f"Final Score: {score} out of {total_questions}")
    print(f"Success Rate: {percentage:.2f}%")
    print("==================================================")

if __name__ == "__main__":
    run_quiz()
