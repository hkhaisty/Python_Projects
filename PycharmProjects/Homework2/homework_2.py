#Name: Harriet Haisty
#Instructor: Ji Li
#Class: Internet Programming

with open('in.txt', 'r') as my_file:
    data = my_file.read().replace('\n', '')

text_file = open('out.txt', 'w')
text_file.write(data.upper())
text_file.close()
