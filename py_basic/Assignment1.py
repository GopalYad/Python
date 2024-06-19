import pandas as pd
import os

# 1. Write a program to print Twinkle twinkle little star poem in python.
print(
    """
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.
"""
)
# 2. Use REPL and print the table of 5 using it.
# 5 * 1, 5 * 2, 5 * 3, 5 * 4, 5 * 5, 5 * 6, 5 * 7, 5 * 8, 5 * 9, 5 * 10
# (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)


# 3. Install an external module and use it to perform an operation of your interest.
# pip install pandas
# Create a simple DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [24, 27, 22, 32, 29],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
}
df = pd.DataFrame(data)

# Perform basic operations
# 1. Display the DataFrame
print("Original DataFrame:")
print(df)


# 4.Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that
# def print_directory_contents(path):
#     try:
#         # Get the list of all files and directories
#         dir_contents = os.listdir(path)
#         print(f"Contents of the directory '{path}':")
#         for item in dir_contents:
#             print(item)
#     except FileNotFoundError:
#         print(f"The directory '{path}' does not exist.")
#     except NotADirectoryError:
#         print(f"The path '{path}' is not a directory.")
#     except PermissionError:
#         print(f"Permission denied to access the directory '{path}'.")


# # Specify the directory path
# directory_path = "."  # Current directory

# # Call the function to print directory contents
# print_directory_contents(directory_path)




# 5. Label the program written in problem 4 with comments. 
