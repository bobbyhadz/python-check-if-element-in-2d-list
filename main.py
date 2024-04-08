# Check if a Value exists in a Two-dimensional List in Python

my_2d_list = [['one', 'two'], ['three', 'four'], ['five', 'six']]


if any('three' in nested_list for nested_list in my_2d_list):
    # 👇️ This runs
    print('three is contained in the two-dimensional list')
else:
    print('three is NOT contained in the two-dimensional list')