import json
from collections import defaultdict


def find_top_department(filepath="employees.json"):
    with open(filepath, encoding="utf-8") as f:
        employees = json.load(f)

    totals = defaultdict(int)
    for emp in employees:
        totals[emp["department"]] += emp["salary"]

    top_dept = max(totals, key=totals.get)

    print(f"Отдел с наибольшей суммарной зарплатой: {top_dept} ({totals[top_dept]:,})")
    print("\nСотрудники:")
    for emp in employees:
        if emp["department"] == top_dept:
            print(f"  {emp['name']} — {emp['salary']:,}")


if __name__ == "__main__":
    find_top_department()
