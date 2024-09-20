#data = open ('/Users/pd/Desktop/python/Headfirstpython/Chapter3/sketch.txt')
data = open('./Headfirstpython/Chapter3/sketch.txt')
# this code print first line
# print(data.readline(),end='')
# data.seek(0)
# this for loop prints each line in continous
for each_line in data:
    # print(each_line.split(":"))
    if not each_line.find(':')==-1: #to tackle pause issue
        try:
            (role, line_spoken)= each_line.split(':', 1) #number 1 is to tackle multiple : in the line
            print(role, end='')
            print(' said', end='')
            print(line_spoken, end='')
        except:
            pass
data.close()