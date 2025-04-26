import csv

with open("faculty_page1.csv", "r") as f:
    reader = csv.DictReader(f)
    filtered = []

    for row in reader:
        title = row["Title"].lower()
        dept = row["Department"].lower()
        email = row["Email"].strip()

        if email == "N/A":
            continue  # 没邮箱就跳过

        # 看起来是招人的信号
        if any(keyword in dept for keyword in ["lab", "center", "institute", "research"]):
            if any(keyword in title for keyword in ["assistant", "associate", "professor", "director"]):
                filtered.append(row)

with open("ra_candidates.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Title", "Department", "Email"])
    writer.writeheader()
    writer.writerows(filtered)

print(f" 共筛出 {len(filtered)} 位有潜力的 RA 导师，保存为 ra_candidates.csv")
