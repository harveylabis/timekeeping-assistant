from bs4 import BeautifulSoup

with open("my_timesheet.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

# print(soup.prettify())
dates = {}

for i in soup.find_all("timecard-cell"):
    try:
        id = i.find("span", {"name": "content"}).get("id")
        data = i.find("span", {"name": "data"}).get_text(strip=True) 
        dates[id] = data
    except:
        continue

for id in dates:
    print(id, dates[id])