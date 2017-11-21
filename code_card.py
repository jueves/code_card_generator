import random
import webbrowser
import os

#Set personal parameters
names_dic = {'dropbox' : 'blue', 'facebook' : 'purple', 'lastpass' : 'darkred',
             'todoist' : 'red', 'evernote' : 'green', 'gmail' : 'black'}
pre_char_length = 4
post_char_length = 0

#This function generates pseudo random strings
def my_random_strings():
    pre_char = ''
    for char in range(pre_char_length):
        pre_char = pre_char + str(random.randint(0,9))
    post_char = ''
    for char in range(post_char_length):
        post_char = post_char + str(random.randint(0,9))
    return [pre_char, post_char]

#Open files
files_dic = {}
for name in names_dic:
    files_dic[name] = open('services/' + name + '.txt', 'r')

#Arrange passwords in lists.
passwords_dic = {}
for file in files_dic:
    password = files_dic[file].readline().strip('\n')
    passwords_dic[file] = []
    while password != '':
        passwords_dic[file].append(password)
        password = files_dic[file].readline().strip('\n')

#Add extra text
for service in passwords_dic:
    count = 0
    for password in passwords_dic[service]:
        random_str_list = my_random_strings() #Generate pseudo random characters
        html_str_list = ["<p class=\"" + service + "\">", "</p>"] #list of html strings
        ext_pwd = random_str_list[0] + password + random_str_list[1] #Extended password
        passwords_dic[service][count] = html_str_list[0] + ext_pwd + html_str_list[1]
        count = count + 1

#Unify strings
unified_list = []
for service in passwords_dic:
    #This sorts the new function in random order
    for password in passwords_dic[service]:
        unified_list.append(password)

#Shufle
final_list = []
for i in range(len(unified_list)):
    string = random.choice(unified_list)
    unified_list.remove(string)
    final_list.append(string)

#Create html file
pre_text_file = open('pre_text.txt', 'r')
pre_text = pre_text_file.read()
post_text_file = open('post_text.txt', 'r')
post_text = post_text_file.read()

final_file = open('code_card.html', 'w')
final_file.write(pre_text)
for password in final_list:
    final_file.write(password + '\n')
final_file.write(post_text)
final_file.close()

#Edit CSS
css_file = open('style.css', 'w')
pre_css_file = open('pre_css.txt', 'r')
css_file.write(pre_css_file.read() + '\n')
for service in names_dic:
    css_file.write('.' + service + ' {\n color: ' + names_dic[service] + ';\n }\n\n')
css_file.close()

#Launch browser
webbrowser.open(os.path.realpath('code_card.html'))
