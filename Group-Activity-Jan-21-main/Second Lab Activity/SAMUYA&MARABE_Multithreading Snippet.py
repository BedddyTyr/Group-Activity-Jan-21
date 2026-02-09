import threading
import time

def compute_grade(subject, grade, grades):
    print(f"[Thread-{subject}] Processing grade...")
    time.sleep(0.5)  # simulate work
    grades.append(grade)
    print(f"[Thread-{subject}] Grade recorded: {grade}")

grades = []
threads = []

n = int(input("Enter number of subjects: "))

start_time = time.time()

for i in range(n):
    grade = float(input(f"Enter grade for subject {i + 1}: "))
    t = threading.Thread(
        target=compute_grade,
        args=(i + 1, grade, grades)
    )
    threads.append(t)
    t.start()

for t in threads:
    t.join()

gwa = sum(grades) / len(grades)
end_time = time.time()

print("\nFinal GWA:", round(gwa, 2))
print("Execution Time:", round(end_time - start_time, 4), "seconds")
