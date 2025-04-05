#!/usr/bin/python3
import sys

party_items = [
    "Cake","Balloons","Music System","Lights","Catering Service",
    "DJ","Photo Booth","Tables","Chairs","Drinks","Party Hats",
    "Streamers","Invitation Cards","Party Games","Cleaning Service"
]
item_values = [20,21,10,5,8,3,15,7,12,6,9,18,4,2,11]

def calculate_party_code(selected):
    if not selected:
        return 0
    code = item_values[selected[0]]
    for i in selected[1:]:
        code &= item_values[i]
    return code

def modify_party_code(base_code):
    if base_code == 0:
        return base_code + 5, "Epic Party Incoming!"
    elif base_code > 5:
        return base_code - 2, "Let's keep it classy!"
    else:
        return base_code, "Chill vibes only!"

def display_result(selected):
    base_code = calculate_party_code(selected)
    final_code, message = modify_party_code(base_code)
    names = [party_items[i] for i in selected]
    return f"""
<html>
<body>
<h1>Selected Items: {', '.join(names)}</h1>
<p>Base Party Code: {base_code}</p>
<p>Adjusted Party Code: {final_code}</p>
<p>Final Party Code: {final_code}</p>
<p>Message: {message}</p>
</body>
</html>
"""

if __name__ == "__main__":
    if len(sys.argv) > 1:
        selected_indices = list(map(int, sys.argv[1:]))
    else:
        selected_indices = []
    print(display_result(selected_indices))
