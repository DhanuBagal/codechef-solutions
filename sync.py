import requests
import os

USERNAME = "dhanashree_b"

url = f"https://www.codechef.com/recent/user?user_handle={USERNAME}"
response = requests.get(url)
data = response.json()

for item in data:
    if item['status'] == 'Accepted':
        problem = item['problem_code']
        solution = item['solution']
        lang = item['language']

        ext = "txt"
        if "C++" in lang:
            ext = "cpp"
        elif "Python" in lang:
            ext = "py"
        elif "Java" in lang:
            ext = "java"

        filename = f"{problem}.{ext}"

        if not os.path.exists(filename):
            with open(filename, "w") as f:
                f.write(solution)

print("Sync done")