import csv

KEYWORDS = ['lab', 'center', 'institute', 'research group', 'project', 'initiative']
TARGET_DEPTS = ['cognitive', 'psychology', 'anthropology', 'sociology', 'political']
TARGET_TITLES = ['assistant professor', 'associate professor', 'director''Co-Director']

with open("ra_candidates.csv", newline='') as infile, open("target_labs.csv", "w", newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)
    writer.writerow(header)

    count = 0
    for row in reader:
        name, title, dept, email = row
        title_lower = title.lower()
        dept_lower = dept.lower()

        if any(k in title_lower + dept_lower for k in KEYWORDS) and \
           any(d in dept_lower for d in TARGET_DEPTS) and \
           any(t in title_lower for t in TARGET_TITLES):
            writer.writerow(row)
            count += 1

print(f"筛选出 {count} 个目标 lab 导师，保存为 target_labs.csv")
