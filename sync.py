import requests
import os

USERNAME = "dhanashree_b"

url = f"https://www.codechef.com/recent/user?user_handle={USERNAME}"

response = requests.get(url)

if response.status_code != 200:
    print("Failed to fetch data")
    exit(1)

data = response.json()

for item in data:
    try:
        if item.get('status') == 'Accepted':
            problem = item.get('problem_code')
            solution = item.get('solution')
            lang = item.get('language')

            if not solution:
                continue

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

                print(f"Saved {filename}")

    except Exception as e:
        print("Error:", e)

print("Sync completed")
