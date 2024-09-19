Employees =[
{"eid":1,"ename":"Goldi","email":"gchance0@free.fr","gender":"Female","range":"MUNI"},
{"eid":2,"ename":"Sal","email":"sruf1@discuz.net","gender":"Male","range":"UMA"},
{"eid":3,"ename":"Sid","email":"sdalgarnowch2@vimeo.com","gender":"Male","range":"MUNI"},
{"eid":4,"ename":"Doretta","email":"dfidler3@spiegel.de","gender":"Female","range":"UMA"},
{"eid":5,"ename":"Berton","email":"bmycroft4@harvard.edu","gender":"Non-binary","range":"UMA"},
{"eid":6,"ename":"Timoteo","email":"tjarmaine5@goo.ne.jp","gender":"Male","range":"UMA"},
{"eid":7,"ename":"Tobye","email":"tcalltone6@techcrunch.com","gender":"Female","range":"MUNI"},
{"eid":8,"ename":"Laurie","email":"lsmeeton7@is.gd","gender":"Bigender","range":"UMA"},
{"eid":9,"ename":"Crawford","email":"csutty8@redcross.org","gender":"Male","range":"MUNI"}

]


MUNI_Employees = []
UMA_Employees =[]

for emp in Employees:
    if emp["range"] == "MUNI":
        MUNI_Employees.append(emp)
    else:
        UMA_Employees.append(emp)    
print(MUNI_Employees)
print(UMA_Employees)