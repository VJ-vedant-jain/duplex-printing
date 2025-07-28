from split import get_two_files

path = input("Enter path of pdf to print: ")

status = get_two_files(path)
print(status)

