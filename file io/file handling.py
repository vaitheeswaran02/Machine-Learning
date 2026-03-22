import re
from collections import defaultdict

# Student Class

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.activities = []  # list of (activity, date, time)

    def add_activity(self, activity, date, time):
        self.activities.append((activity, date, time))

    def activity_summary(self):
        logins = sum(1 for a in self.activities if a[0] == "LOGIN")
        submissions = sum(1 for a in self.activities if a[0] == "SUBMIT_ASSIGNMENT")
        return logins, submissions


# Parse and Validate Log Entry

def parse_log_entry(line):
    pattern = r'^(S\d+)\s*\|\s*(\w+)\s*\|\s*(LOGIN|LOGOUT|SUBMIT_ASSIGNMENT)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(\d{2}:\d{2})$'
    match = re.match(pattern, line)
    if not match:
        raise ValueError(f"Incorrect format: {line}")
    return match.groups()


# Generator to Read Log File

def read_log_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            try:
                yield parse_log_entry(line.strip())
            except ValueError as e:
                print("Invalid log entry:", e)


# Process Logs and Generate Report
def process_logs(input_file, output_file):
    students = {}
    daily_stats = defaultdict(int)
    abnormal_logins = defaultdict(int)

    # Read and process each log entry
    for student_id, name, activity, date, time in read_log_file(input_file):
        if student_id not in students:
            students[student_id] = Student(student_id, name)

        students[student_id].add_activity(activity, date, time)
        daily_stats[(date, activity)] += 1

        # Abnormal behavior detection
        if activity == "LOGIN":
            abnormal_logins[student_id] += 1
        elif activity == "LOGOUT":
            abnormal_logins[student_id] -= 1

    # Generate report
    with open(output_file, 'w') as out:
        print("\n STUDENT ACTIVITY REPORT\n")
        out.write("STUDENT ACTIVITY REPORT\n\n")

        for student in students.values():
            logins, submissions = student.activity_summary()
            report_line = f"{student.student_id} | {student.name} | Logins: {logins} | Submissions: {submissions}"
            print(report_line)
            out.write(report_line + "\n")

        print("\n Abnormal Behavior (Multiple logins without logout):")
        out.write("\nAbnormal Behavior:\n")
        for sid, count in abnormal_logins.items():
            if count > 0:
                alert = f"{sid} has {count} extra LOGIN(s)"
                print(alert)
                out.write(alert + "\n")

        print("\n Daily Activity Statistics:")
        out.write("\nDaily Activity Statistics:\n")
        for (date, activity), count in daily_stats.items():
            stat = f"{date} - {activity}: {count}"
            print(stat)
            out.write(stat + "\n")

# Main Program
if __name__ == "__main__":
    input_file = "student_logs.txt"
    output_file = "activity_report.txt"
    process_logs(input_file, output_file)
