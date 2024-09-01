# This program is to manage the data from the server side, 
# although it is in the same directory as the client program.
# Here only csv file handling will be used to manage the data from
# "data.csv", into which we are inserting the data using frontend and backend

import csv

print("1. Delete record")
print("2. Sort based on language and update data")
print("3. Sort based on cast and update data")
print("4. Sort based on genre and update data")
print("5. Update record")

ch = int(input("Enter your choice: "))

def del_rec():

    f = open("data.csv","r", newline="")
    n = input("Enter the name whose record has to be deleted: ")
    l = []
    csv_reader = csv.reader(f)
    next(csv_reader)

    for i in csv_reader:
        if i[0] != n:
            l.append(i)

    f.close()

    g = open("data.csv","w",newline="")
    csv_writer = csv.writer(g)
    csv_writer.writerow(["Name","Age","Number of seats","Premium",
    "Movie","Genre","Movie Language","Cast"])
    csv_writer.writerows(l)
    
    g.close()


def update_rec():
    
    f = open("data.csv","r", newline="")
    n = input("Enter the name whose record has to be updated: ")
    b = input("Enter the field that has to be updated: ")
    c = input("Enter the new data: ")
    l = []
    csv_reader = csv.reader(f)
    next(csv_reader)

    for i in csv_reader:
        if i[0] == n:
            if b == "Name":
                i[0] = c
            elif b == "Age":
                i[1] = c
            elif b == "Number of seats":
                i[2] = c
            elif b == "Premium":
                i[3] = c
        l.append(i)

    f.close()

    g = open("data.csv","w",newline="")
    csv_writer = csv.writer(g)
    csv_writer.writerow(["Name","Age","Number of seats","Premium",
                         "Movie","Genre","Movie Language","Cast"])
    csv_writer.writerows(l)
    
    g.close()

def sort_lang():

    f = open("data.csv","r", newline="")
    csv_reader = csv.reader(f)
    next(csv_reader)
    l = []
    lang = []
    y = True
    for i in csv_reader:
        if i[6] not in lang:
            lang.append(i[6])
        l.append(i)
    sl=[]
    while y == True:
        for j in lang:
            for i in l:
                if i[6] == j:
                    sl.append(i)
                    l.remove(i)
        if len(l)==0:
            y = False
    
    f.close()

    g = open("data.csv","w",newline="")
    csv_writer = csv.writer(g)
    csv_writer.writerow(["Name","Age","Number of seats","Premium",
                         "Movie","Genre","Movie Language","Cast"])
    csv_writer.writerows(sl)

    g.close()

def sort_genre():

    f = open("data.csv","r", newline="")
    csv_reader = csv.reader(f)
    next(csv_reader)
    g = []
    genre = []
    y = True
    for i in csv_reader:
        if i[5] not in genre:
            genre.append(i[5])
        g.append(i)
    sg = []
    while y == True:
        for j in genre:
            for i in g:
                if i[5] == j:
                    sg.append(i)
                    g.remove(i)
        if len(g) == 0:
            y = False
    
    f.close()

    h = open("data.csv","w",newline="")
    csv_writer = csv.writer(h)
    csv_writer.writerow(["Name","Age","Number of seats","Premium",
                         "Movie","Genre","Movie Language","Cast"])
    csv_writer.writerows(sg)

    h.close()

def sort_cast():

    f = open("data.csv","r", newline="")
    csv_reader = csv.reader(f)
    next(csv_reader)
    c = []
    cast = []
    y = True
    for i in csv_reader:
        if i[7][0] not in cast:
            cast.append(i[7][0])
        c.append(i)
    sc=[]
    while y == True:
        for j in cast:
            for i in c:
                if i[7][0] == j:
                    sc.append(i)
                    c.remove(i)
        if len(c)==0:
            y = False
    
    f.close()

    h = open("data.csv","w",newline="")
    csv_writer = csv.writer(h)
    csv_writer.writerow(["Name","Age","Number of seats","Premium",
                         "Movie","Genre","Movie Language","Cast"])
    csv_writer.writerows(sc)

    h.close()

if ch == 1:
    del_rec()
if ch == 2:
    sort_lang()
if  ch == 3:
    sort_cast()
if ch == 4:
    sort_genre()
if ch == 5:
    update_rec()



    
