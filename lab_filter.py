import csv

KEYWORDS = ['center', 'lab', 'institute', 'director', 'program', 'initiative', 'project', 'research group']

with open("ra_candidates.csv", newline='') as infile, open("ra_with_lab.csv", "w", newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)
    writer.writerow(header)

    count = 0
    for row in reader:
        title = row[1].lower()
        dept = row[2].lower()
        if any(keyword in title or keyword in dept for keyword in KEYWORDS):
            writer.writerow(row)
            count += 1

print(f"✅ 共筛出 {count} 位可能拥有 lab/project 的教授，保存为 ra_with_lab.csv")

