#  Readme
Many online services offer the posibility to setup two step authentication with your phone. They also provide a set of one use passwords in case you lost the device.  
This code creates printable card for the passwords, adding extra digits at the beggining and the end, and assigning a certain color to each service.  
This is an example:  
![card example](card_example.png)  
Although the original pin passwords had just 8 digits, 4 pseudo random digits have been added to the beggining of each password.
### Adding your passwords
This repository includes some examples of lists of passwords which can be used both for reference and as random data to fill the card.  
Each list is a text file with the name of the service followed by `.txt`. The contents of the file are the passwords, one per line.
### Setting up the parameters
At the beggining of the python file `code_card.py` there is a python dictionary structure with the names of the services and their colors. You can change both service names and colors, and add as many services as you want, although the final result may not have a card shape.  
You can choose how many pseudo random digits you want at the beggining and at the end of each password setting the values of the parameters `pre_char_len` and `post_char_len`.
