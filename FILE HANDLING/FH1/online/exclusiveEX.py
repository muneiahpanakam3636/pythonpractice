#  craete error;-fileexisting error.

fp=open('tpt.txt','x')
fp.write('exclusive mode for write operation')

fp.close()


#FileExistsError: [Errno 17] File exists: 'tpt.txt'