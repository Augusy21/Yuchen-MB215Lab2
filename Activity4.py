def format_title(title, width=20): # Function to format each column title to a fixed width
    return title.ljust(width)

column_One = input("Enter title for column 1: ")# Asking the user for column One
column_Two = input("Enter title for column 2: ")# Asking the user for column Two
column_Three = input("Enter title for column 3: ")# Asking the user for column Three

formatted_column_One = format_title(column_One)# Formatting the column One
formatted_column_Two = format_title(column_Two)# Formatting the column Two
formatted_column_Three = format_title(column_Three)# Formatting the column Three

print(formatted_column_One + formatted_column_Two + formatted_column_Three)
