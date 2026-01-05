import re
from collections import defaultdict

# ---------------- STUDENT CLASS ----------------
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.activities = []

    def add_activity(self, activity, date, time):
        self.activities.append((activity, date, time))

    def summary(self):
        logins = 0
        submissions = 0
        for activity, _, _ in self.activities:
            if activity == "LOGIN":
                logins += 1
            elif activity == "SUBMIT_ASSIGNMENT":
                submissions += 1
        return logins, submissions


# ---------------- REGEX PATTERNS ----------------
student_id_pattern = re.compile(r"^S\d+$")
activity_pattern = re.compile(r"^(LOGIN|LOGOUT|SUBMIT_ASSIGNMENT)$")
date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
time_pattern = re.compile(r"^\d{2}:\d{2}$")


# ---------------- GENERATOR FUNCTION ----------------
def read_logs(filename):
    with open(filename, "r") as file:
        for line in file:
            try:
                parts = [p.strip() for p in line.split("|")]

                if len(parts) != 5:
                    raise ValueError("Incorrect format")

                student_id, name, activity, date, time = parts

                if not student_id_pattern.match(student_id):
                    raise ValueError("Invalid Student ID")

                if not activity_pattern.match(activity):
                    raise ValueError("Invalid Activity")

                if not date_pattern.match(date) or not time_pattern.match(time):
                    raise ValueError("Invalid Date or Time")

                yield student_id, name, activity, date, time

            except Exception:
                print("Invalid entry skipped:", line.strip())


# ---------------- MAIN PROGRAM ----------------
students = {}
daily_stats = defaultdict(int)
login_tracker = defaultdict(int)

for student_id, name, activity, date, time in read_logs("student_log.txt"):

    if student_id not in students:
        students[student_id] = Student(student_id, name)

    students[student_id].add_activity(activity, date, time)

    daily_stats[(date, activity)] += 1

    if activity == "LOGIN":
        login_tracker[student_id] += 1
    elif activity == "LOGOUT":
        login_tracker[student_id] -= 1


# ---------------- REPORT ----------------
report = []
report.append("STUDENT ACTIVITY REPORT\n")

for student in students.values():
    logins, submissions = student.summary()
    report.append(
        f"{student.student_id} | {student.name} | Logins: {logins} | Submissions: {submissions}"
    )

report.append("\nABNORMAL BEHAVIOR:")
for sid, count in login_tracker.items():
    if count > 0:
        report.append(f"{sid} has multiple logins without logout")

report.append("\nDAILY ACTIVITY STATISTICS:")
for (date, activity), count in daily_stats.items():
    report.append(f"{date} | {activity} : {count}")


# ---------------- DISPLAY & SAVE ----------------
for line in report:
    print(line)

with open("final_report.txt", "w") as file:
    for line in report:
        file.write(line + "\n")
