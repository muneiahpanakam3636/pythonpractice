#  craete file is running.

fp=open('Muni.txt','x')
fp.write('exclusive mode for write operation')

fp.close()

#  now it is creating new file which is not existing 'Muni.txt'