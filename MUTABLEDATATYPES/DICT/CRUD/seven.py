

users = [{"eid":1,"ename":"Goldi","email":"gchance0@free.fr","gender":"Female"},
{"eid":2,"ename":"Sal","email":"sruf1@discuz.net","gender":"Male"},
{"eid":3,"ename":"Sid","email":"sdalgarnowch2@vimeo.com","gender":"Male"},
{"eid":4,"ename":"Doretta","email":"dfidler3@spiegel.de","gender":"Female"},
{"eid":5,"ename":"Berton","email":"bmycroft4@harvard.edu","gender":"Non-binary"},
{"eid":6,"ename":"Timoteo","email":"tjarmaine5@goo.ne.jp","gender":"Male"},
{"eid":7,"ename":"Tobye","email":"tcalltone6@techcrunch.com","gender":"Female"},
{"eid":8,"ename":"Laurie","email":"lsmeeton7@is.gd","gender":"Bigender"},
{"eid":9,"ename":"Crawford","email":"csutty8@redcross.org","gender":"Male"},
{"eid":10,"ename":"Sharline","email":"ssoloway9@lulu.com","gender":"Female"},
{"eid":11,"ename":"Armando","email":"aburndreda@hostgator.com","gender":"Male"},
{"eid":12,"ename":"Blake","email":"bturneauxb@hhs.gov","gender":"Female"},
{"eid":13,"ename":"Henderson","email":"hprettic@reuters.com","gender":"Male"},
{"eid":14,"ename":"Jacki","email":"jcolumbined@china.com.cn","gender":"Female"},
{"eid":15,"ename":"Marni","email":"mferriese@4shared.com","gender":"Genderqueer"},
{"eid":16,"ename":"Toinette","email":"trembrandtf@reverbnation.com","gender":"Female"},
{"eid":17,"ename":"Mendel","email":"mpoolmang@state.gov","gender":"Male"},
{"eid":18,"ename":"Nobie","email":"nblakelyh@elegantthemes.com","gender":"Male"},
{"eid":19,"ename":"Kelby","email":"kduffyni@netlog.com","gender":"Male"},
{"eid":20,"ename":"Caralie","email":"csimpsonj@lycos.com","gender":"Female"},
{"eid":21,"ename":"Randi","email":"rmcorkillk@who.int","gender":"Male"},
{"eid":22,"ename":"Sherwynd","email":"sbleythinl@bloomberg.com","gender":"Bigender"},
{"eid":23,"ename":"Earlie","email":"elobliem@answers.com","gender":"Male"},
{"eid":24,"ename":"Hew","email":"hkeyzorn@bizjournals.com","gender":"Male"},
{"eid":25,"ename":"Natty","email":"nellwello@gov.uk","gender":"Female"},
{"eid":26,"ename":"Ram","email":"rcalcottp@sun.com","gender":"Male"},
{"eid":27,"ename":"Vida","email":"vklicherq@ucoz.ru","gender":"Female"},
{"eid":28,"ename":"Gradey","email":"gcallicottr@zdnet.com","gender":"Male"},
{"eid":29,"ename":"Betsey","email":"bballances@odnoklassniki.ru","gender":"Female"},
{"eid":30,"ename":"Mac","email":"mveryant@free.fr","gender":"Male"},
{"eid":31,"ename":"Esdras","email":"eduetschensu@angelfire.com","gender":"Male"},
{"eid":32,"ename":"Cristabel","email":"cbergev@hp.com","gender":"Female"},
{"eid":33,"ename":"Marlene","email":"mbodycombw@buzzfeed.com","gender":"Female"},
{"eid":34,"ename":"Gretta","email":"gferraresex@miitbeian.gov.cn","gender":"Female"},
{"eid":35,"ename":"Ashlin","email":"aswyery@aboutads.info","gender":"Male"},
{"eid":36,"ename":"Lorri","email":"lserjeantsonz@zdnet.com","gender":"Genderqueer"},
{"eid":37,"ename":"Sherm","email":"sjedrzaszkiewicz10@wordpress.org","gender":"Male"},
{"eid":38,"ename":"Chariot","email":"callett11@hud.gov","gender":"Male"},
{"eid":39,"ename":"Car","email":"cfraulo12@nasa.gov","gender":"Male"},
{"eid":40,"ename":"Constanta","email":"ccastagna13@mashable.com","gender":"Female"},
{"eid":41,"ename":"Anders","email":"abyart14@weather.com","gender":"Male"},
{"eid":42,"ename":"Sissy","email":"ssimecek15@wikia.com","gender":"Female"},
{"eid":43,"ename":"Edd","email":"eearl16@nydailynews.com","gender":"Male"},
{"eid":44,"ename":"Jared","email":"jpaoletti17@netvibes.com","gender":"Male"},
{"eid":45,"ename":"Ricardo","email":"rlambirth18@feedburner.com","gender":"Male"},
{"eid":46,"ename":"Frayda","email":"fmulliss19@typepad.com","gender":"Female"},
{"eid":47,"ename":"Tripp","email":"tpaquet1a@nydailynews.com","gender":"Male"},
{"eid":48,"ename":"Lorant","email":"lwindeatt1b@timesonline.co.uk","gender":"Male"},
{"eid":49,"ename":"Christophorus","email":"cleidecker1c@digg.com","gender":"Male"},
{"eid":50,"ename":"Sampson","email":"smckag1d@smh.com.au","gender":"Male"}]

print(type(users))# list type


 
no_of_male_users=0
no_of_female_users =0

for user in users: 
    if user['gender']=='Male':
            no_of_male_users = no_of_male_users+1
           
    elif user['gender']=='Female':           
          no_of_females_users = no_of_female_users+1  
print("No of Male users:",no_of_male_users)  
print("No of FeMale users:", no_of_females_users )          


# No of Male users: 28
# No of FeMale users: 1

