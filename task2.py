import matplotlib.pyplot as plt
import pandas as pd

# Mock Data simulating an API response
student_data = [
    {"name": "Amit", "score": 78},
    {"name": "Priya", "score": 92},
    {"name": "Rahul", "score": 88},
    {"name": "Neha", "score": 65},
    {"name": "Karan", "score": 74}
]

def analyze_scores():
    # Load data into a DataFrame (Standard tabular format)
    df = pd.DataFrame(student_data)
    
    # Calculate Average
    average_score = df["score"].mean()
    print(f"The average score is: {average_score}")
    
    # Create the Bar Chart
    plt.figure(figsize=(8, 5))
    plt.bar(df["name"], df["score"], color="skyblue")
    
    # Add a line for the average
    plt.axhline(y=average_score, color='red', linestyle='--', label=f"Avg: {average_score}")
    
    plt.title("Student Test Scores")
    plt.xlabel("Student Name")
    plt.ylabel("Marks")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    analyze_scores()