    def analyze_students(students):
        def validate_data():
            if not students: raise ValueError("Порожній словник")
            for v in students.values():
                if type(v) is not list or not v: raise ValueError("Некоректний список")
                if any(type(x) not in (int, float) or not 0 <= x <= 100 for x in v):
                    raise ValueError("Некоректна оцінка")

        def calculate_student_average():
            return {k: round(sum(v) / len(v), 1) for k, v in students.items()}

        def get_passed_students(avgs):
            return {k: "Pass" if v >= 60 else "Failed" for k, v in avgs.items()}

        def sort_student_by_marks(avgs):
            return dict(sorted(avgs.items(), key=lambda x: x[1], reverse=True))

        def get_failed_students(avgs):
            return [k for k, v in avgs.items() if v < 60]

        def get_top_students(avgs):
            m = max(avgs.values())
            return [k for k, v in avgs.items() if v == m]

        validate_data()
        avgs = calculate_student_average()

        return {
            "students average": avgs,
            "passed students": get_passed_students(avgs),
            "top students list": sort_student_by_marks(avgs),
            "failed_students": get_failed_students(avgs),
            "top_students": get_top_students(avgs)
        }


    students = {
        "Ivan": [78, 82, 90],
        "Olena": [45, 60, 55],
        "Petro": [100, 95, 98],
        "Anna": [50, 40, 30],
        "Maria": [70, 75, 80]
    }

    for k, v in analyze_students(students).items():
        print(f"{k}: {v}")