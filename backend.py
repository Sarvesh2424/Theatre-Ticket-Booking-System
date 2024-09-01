# importing necessary module(s)
import csv

movie_Data = open("data.csv", "w", newline="")
wtr = csv.writer(movie_Data)
wtr.writerow(["Name", "Age", "Number of seats",  "Premium"])
movie_Data.close()

user_Data = open("user_data.csv", "w", newline="")
wtr = csv.writer(user_Data)
wtr.writerow(["Gmail", "Password"])
user_Data.close()


def input_data(name, age, seat_nos, premium):

    movie_Data = open("data.csv", "a", newline ="")
    wtr = csv.writer(movie_Data)
    wtr.writerow([name, age, seat_nos, premium])
    movie_Data.close()


def input_userData(gmail, password):
    user_Data = open("user_data.csv", "a", newline="")
    wtr = csv.writer(user_Data)
    wtr.writerow([gmail, password])


def write_newData(movie, genre, movie_lang, cast):
    old_Data = open("data.csv", 'r')
    rdr = csv.reader(old_Data)

    data = []

    for column in rdr:
        column.extend(['Movie', 'Genre', 'Movie Language', 'Cast'])
        data.append(column)
        break

    for column in rdr:
        column.extend([movie, genre, movie_lang, cast])
        data.append(column)

    old_Data.close()

    new_Data = open("data.csv", 'w', newline="")
    wtr = csv.writer(new_Data)
    wtr.writerows(data)
    new_Data.close()

def write_seatData(seats):
    old_Data = open("data.csv", 'r')
    rdr = csv.reader(old_Data)

    data = []

    for column in rdr:
        column.extend(["Selected Seats"])
        data.append(column)
        break

    for column in rdr:
        column.extend([seats])
        data.append(column)

    old_Data.close()

    new_Data = open("data.csv", 'w', newline="")
    wtr = csv.writer(new_Data)
    wtr.writerows(data)
    new_Data.close()


    
