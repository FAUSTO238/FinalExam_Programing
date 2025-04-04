
party_items = [
    "Cake", "Balloons", "Music System", "Lights", "Catering Service", "DJ",
    "Photo Booth", "Tables", "Chairs", "Drinks", "Party Hats", "Streamers",
    "Invitation Cards", "Party Games", "Cleaning Service"
]

# Display available items
print("Available Party Items:")
for idx, item in enumerate(party_items):
    print(f"{idx}: {item}")

# Allow user to select items
user_input = input("Enter item indices separated by commas (e.g., 0, 1): ")
selected_indices = list(map(int, user_input.split(",")))
selected_items = [party_items[i] for i in selected_indices]
print(f"Selected Items: {', '.join(selected_items)}")

# Assign values to party items
item_values = [20, 21, 10, 5, 8, 3, 15, 7, 12, 6, 9, 18, 4, 2, 11]
values = [item_values[i] for i in selected_indices]

# Perform bitwise AND operation
base_code = values[0]
for value in values[1:]:
    base_code &= value

print(f"Base Party Code: {' & '.join(map(str, values))} = {base_code}")

# Modify base code
if base_code == 0:
    base_code += 5
    message = "Epic Party Incoming!"
elif base_code > 5:
    base_code -= 2
    message = "Let's keep it classy!"
else:
    message = "Chill vibes only!"

print(f"Adjusted Party Code: {base_code}")
print(f"Final Party Code: {base_code}")
print(f"Message: {message}")

# Output in HTML format
html_output = f"""
<html>
    <head><title>Party Planner</title></head>
    <body>
        <h2>Selected Items</h2>
        <p>{', '.join(selected_items)}</p>
        <h3>Final Party Code: {base_code}</h3>
        <p>{message}</p>
    </body>
</html>
"""

print(html_output)
