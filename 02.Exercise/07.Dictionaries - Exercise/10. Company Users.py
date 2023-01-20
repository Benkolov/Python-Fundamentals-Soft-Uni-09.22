final_data = {}

while True:
    data = input()
    if data == "End":
        break
    company, id = data.split(" -> ")
    if company not in final_data:
        final_data[company] = []
        final_data[company].append(id)
    else:
        if id in final_data[company]:
            pass
        else:
            final_data[company].append(id)

for company_name, employees in final_data.items():
    print(company_name)
    for employees_id in employees:
        print(f"-- {employees_id}")