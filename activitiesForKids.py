# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take a child's name as an argument. Each function should print that the child performed the activity.
def run(firstName):
    return {f'{firstName} runs fast'}

def swing(firstName):
    return {f'{firstName} swings high'}

def slide(firstName):
    return {f'{firstName} slides bravely'}

def hide_and_seek(firstName):
    return {f'{firstName} plays hide and seek'}

# The following lists of children should be iterated, and the names sent to the appropriate functions.

running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

for kid in running_kids:
    print(run(kid))
    
for kid in swinging_kids:
    print(swing(kid))
    
for kid in sliding_kids:
    print(slide(kid))
    
for kid in hiding_kids:
    print(hide_and_seek(kid))