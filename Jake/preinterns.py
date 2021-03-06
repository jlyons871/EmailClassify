#!/usr/local/bin/python

## first line allows you to double click the file and run as a script


import re 
import pprint 
import os

# fname_in = "testdata\\"
# my_range = 898
fname_out = "outdata\\"


# classified = {}


# f = open('cats.txt', 'r')
# for line in f:
    # path_cat = line.split()
    # label = path_cat[1]
    # subpaths = path_cat[0].split('\\')
    # file = subpaths[2]
    # file = file.replace('.cats','.txt')
    # classified[file] = label
    
# pprint.pprint(classified)


## check if file exists
def file_exists(filename):
    if os.path.isfile(filename):
        return True
    else:
        print "Error: The file '%s' does not exist." % filename
        return False

## return str w/ body of email for a file
def get_email_body(filename):
    if (not file_exists(filename)):
        pass
        
    f = open(filename, 'r')
    body_of_email = False   
    forward_info = False
    body_regex = r'X-FileName:'
    forward_regex = r'-------- Forwarded'
    endHeader_regex = r'Subject:'
    
    body_data = ""  
   
    for line in f: 
        ## set flag for start of forward header data
        if re.search(forward_regex, line) != None:
            forward_info = True  

        ## set 'body_of_email' true after header section
        if not body_of_email:
            if re.search(body_regex, line) != None:
                body_of_email = True  
                
        ## set flag for end of forward header data
        elif forward_info:
            if re.search(endHeader_regex, line) != None:
                forward_info = False            
                
        ## only copy body of email
        elif body_of_email and not forward_info:
            body_data += line

            
    f.close()
    return body_data

all_files = []    
    
# for dirname, dirnames, filenames in os.walk('.'):
    # if '.git' in dirnames:
        # dirnames.remove('.git')    
    
    # for filename in filenames:
        # if ('.py' not in filename) and ('.txt' not in filename):
            # all_files.append(os.path.join(dirname, filename))   

# count = 1    
# errors = []        
# for file in all_files:
    # try:
        # data = get_email_body(file)    
        # f_out = open(fname_out + str(count) + '.txt', 'w')
        # f_out.write('\n\nEmail Message:\n\n' + data + '\n\nFileName' + file)
        # f_out.close()
    # except Exception as error:
        # errors.append(file)
    # count += 1

    
    
    



    

