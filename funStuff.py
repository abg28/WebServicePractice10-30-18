import requests

r = requests.post("http://bme590.suyash.io/student",
                  json={"first_name": "Alex", "last_name": "Guevara", "netid": "abg28", "github_username": "abg28"})
print(r.json())

r2 = requests.get("http://bme590.suyash.io/list")

print(r2.json())
