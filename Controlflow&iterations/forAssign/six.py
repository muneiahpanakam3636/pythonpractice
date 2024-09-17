##  print 1 2 3 4 6 7 8 9 10

#  important keywords i.e,  break;loops
#                           continue
#                           pass-Empty block

#continue : to skip current iteration and ;ang execute next iteration.
#example

i =1

for i in range(1,11):

    if i==5:
        continue
    print(i)
    i=i+1
