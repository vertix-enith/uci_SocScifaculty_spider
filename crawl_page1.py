import requests
from bs4 import BeautifulSoup
import csv


url = "https://www.socsci.uci.edu/faculty-directory.php"


response = requests.get(url)
html = response.text


soup = BeautifulSoup(html, 'html.parser')


rows = soup.find_all('tr')[1:]


with open('faculty_page1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Title', 'Department', 'Email'])

    for row in rows:
        cols = row.find_all('td')
        if len(cols) < 5:
            continue

        name = cols[0].text.strip()
        title = cols[1].text.strip()
        department = cols[2].text.strip()
        email_icon = cols[4].find('a')
        email = email_icon['href'].replace('mailto:', '') if email_icon else 'N/A'

        writer.writerow([name, title, department, email])

print(" 第1页爬完了，结果保存在 faculty_page1.csv 文件里。")
