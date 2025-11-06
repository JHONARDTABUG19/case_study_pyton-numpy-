# ------------------------------------------------------------
# reports.py — Reporting Module (Summary Only)
# ------------------------------------------------------------
# Feature:
#   ✅ Print summary of all student grades
#   ✅ Compute final grade from components (weighted)
#   ✅ Show basic stats
#
# Author: Jhonard Tabug
# ------------------------------------------------------------

import csv
import os
import statistics

FILENAME = "ano.csv"  # your CSV file name

def summary_report(filename=FILENAME):
    """Compute and print summary of all student final grades."""
    if not os.path.exists(filename):
        print("⚠️ File not found.")
        return

    with open(filename, "r", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))

    if not reader:
        print("⚠️ No data in CSV.")
        return

    print("\n=== SUMMARY REPORT ===")
    print("{:<12} {:<15} {:<15} {:<10} {:>10}".format(
        "student_id", "last_name", "first_name", "section", "final_grade"
    ))
    print("-" * 65)

    grades = []
    for r in reader:
        try:
            # Compute weighted grade (you can adjust weights if needed)
            quizzes = [
                float(r.get("quiz1", 0) or 0),
                float(r.get("quiz2", 0) or 0),
                float(r.get("quiz3", 0) or 0),
                float(r.get("quiz4", 0) or 0),
                float(r.get("quiz5", 0) or 0),
            ]
            midterm = float(r.get("midterm", 0) or 0)
            final = float(r.get("final", 0) or 0)
            attendance = float(r.get("attendance_percent", 0) or 0)

            # Example weighted formula (you can tweak these)
            quiz_avg = sum(quizzes) / len(quizzes)
            final_grade = (quiz_avg * 0.3) + (midterm * 0.3) + (final * 0.3) + (attendance * 0.1)

            grades.append(final_grade)

            print("{:<12} {:<15} {:<15} {:<10} {:>10.2f}".format(
                r.get("student_id", ""),
                r.get("last_name", ""),
                r.get("first_name", ""),
                r.get("section", ""),
                final_grade
            ))

        except ValueError:
            continue

    if not grades:
        print("\n⚠️ No valid grade data available.")
        return

    print("\n--- SUMMARY STATISTICS ---")
    print(f"Total Students: {len(grades)}")
    print(f"Average Grade: {statistics.mean(grades):.2f}")
    print(f"Highest Grade: {max(grades):.2f}")
    print(f"Lowest Grade:  {min(grades):.2f}")
