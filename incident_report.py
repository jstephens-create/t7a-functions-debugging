north_dc = [45, 30, 120, 15]
south_dc = [60, 10, 25]
def calculate_total(incidents):
    total_minutes = 0

    for minutes in incidents:
        total_minutes += minutes

    return total_minutes

print("North DC total downtime:", calculate_total(north_dc))
print("South DC total downtime:", calculate_total(south_dc))
print("Most recent North DC incident:", north_dc[-1])

raw = input("Enter new North DC downtime (minutes): ")

try:
    new_minutes = int(raw)
except ValueError:
    print("Please enter a whole number, like 30.")
else:
    north_dc.append(new_minutes)
    print("Updated North DC total:", calculate_total(north_dc))

def count_major_incidents(incidents):
    count = 0

    for minutes in incidents:
        if minutes >= 60:
            count += 1

    return count
print("Major incidents:", count_major_incidents(north_dc))