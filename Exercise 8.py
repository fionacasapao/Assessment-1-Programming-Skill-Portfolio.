"""
Simple Search
"""

#Input
names=["Jake","Zac","Ian","Ron","Sam","Dave"]
search_name=input("Enter name you want to search for:")

if search_name in names:
    print(f"{search_name} found in the list!")
else:
    print(f"{search_name} not found in the list.")

    

