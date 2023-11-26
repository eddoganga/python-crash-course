# with open('text_files\pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)


filename = 'text_files\pi_digits.txt'
with open(filename) as file_objects:
    for line in file_objects:
        print(line.rstrip())