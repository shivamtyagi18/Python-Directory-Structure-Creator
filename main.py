#to create a directory
import os
Counties=["ContraCosta",
         "Imperial",
         "SanDiego",
         "Riverside"
        ]

years=["2007-08",
"2008-09",
"2009-10",
"2010-11",
"2011-12",
"2012-13",
"2013-14",
"2014-15",
"2015-16",
"2016-17",
"2017-18" ]

Cities={
    
    "ContraCosta" : [
                    "Antioch",
                    "Brentwood",
                    "Clayton",
                    "Concord",
                    "Town of Danville",
                    "El Cerrito",
                    "Hercules",
                    "Lafayette",
                    "Martinez",
                    "Town of Moraga",
                    "Oakley",
                    "Orinda",
                    "Pinole",
                    "Pittsburg",
                    "Pleasant Hill",
                    "Richmond",
                    "San Pablo",
                    "San Ramon",
                    "Walnut Creek"], #3
    "Imperial": [
                    "Brawley",
                    "Calexico",
                    "Calipatria",
                    "El Centro",
                    "Holtville",
                    "Imperial",
                    "Westmorland"], #4
    "SanDiego" : [
                    "Carlsbad",
                    "Chula Vista",
                    "Coronado",
                    "Del Mar",
                    "El Cajon",
                    "Encinitas",
                    "Escondido",
                    "Imperial Beach",
                    "La Mesa",
                    "Lemon Grove",
                    "National City",
                    "Oceanside",
                    "Poway",
                    "San Diego",
                    "San Marcos",
                    "Santee",
                    "Solana Beach",
                    "Vista"
                    ], #5
    "Riverside" : [
                    "Blythe",
                    "Calimesa",
                    "Canyon Lake",
                    "Cathedral City",
                    "Coachella",
                    "Corona",
                    "Desert Hot Springs",
                    "Eastvale",
                    "Hemet",
                    "Indian Wells",
                    "Indio",
                    "Jurupa Valley",
                    "La Quinta",
                    "Lake Elsinore",
                    "Menifee",
                    "Moreno Valley",
                    "Murrieta",
                    "Norco",
                    "Palm Desert",
                    "Palm Springs",
                    "Perris",
                    "Rancho Mirage",
                    "Riverside",
                    "San Jacinto",
                    "Temecula",
                    "Wildomar"
                    ],
    
}

print("Select 1 for Contra Costa\nSelect 2 forImperial\nSelect 3 for San Diego\nSelect 4 for Riverside")

t = int(input())-1 

for j in years:
    county=Counties[t] 
    path = "/Users/"+county+"/Local Return Spending/City Documents/"+j+"/"
    access_rights = 0o755
#     try:  
#         os.mkdir(path, access_rights)
#     except OSError:  
#         print ("Creation of the directory %s failed" % path)
#     else:  
#         print ("Successfully created the directory %s" % path)
    for i in Cities[county]:
        path1 = path+i+"/"

# define the access rights
        access_rights = 0o755
        try:  
            os.makedirs(path1, access_rights)
            #os.rmdir(path)
        except OSError:  
            print ("Creation of the directory %s failed" % path1)
        else:  
            print ("Successfully created the directory %s" % path1)
