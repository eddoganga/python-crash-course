# filename = 'text_files\programming.txt'

# # with open(filename, 'w') as file_object:
# #     file_object.write('I love programming!\n')
# #     file_object.write('I love solving complex problems.\n')

# #appending to a file
# with open(filename, 'a') as file_object:
#     file_object.write('I also love to find meaning in large datasets.\n')
#     file_object.write('I love creating apps that run in a browser.\n')


filename = 'text_files\guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(input('Enter your name: '))