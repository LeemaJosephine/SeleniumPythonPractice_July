import csv

data =[
    ["standard_user", "secret_sauce", "PASS"],
    ["problem_user", "secret_sauce", "PASS"]
]

with open("TestData/result.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([  # Write a single row
        "Useraname",
        "Password",
        "Result"
    ])

    writer.writerows(data)  # write multiple rows