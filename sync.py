import requests
import os
import json

USERNAME = "dhanashree_b"

url = f"https://www.codechef.com/recent/user?user_handle={USERNAME}"

response = requests.get(url)

try:
    data = response.json()
except:
    print("Could not parse JSON. Response:")
    print(response.text)
    exit(1)

if not isinstance(data, list):
    print("Unexpected data format")
    exit(1)

for item in data:
    try:
        status = item.get("status")
        if status == "Accepted":
            problem = item.get("problem_code")
            solution = item.get("solution")
            lang = item.get("language")

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
        print("Error processing item:", e)

print("Sync completed")
