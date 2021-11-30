#this is my Theatre 

# This program stores the name and year release of movies
# This is now an updated version of the movie list program
import csv
import sys
FILENAME = "movies.csv"

#creating a csv file and adding movies to the file
def write_movies(Movies_list):
    try:

        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(Movies_list)
    except Exception as e:
        print(type(e), e)


# reading data from a csv file and adding them to a list
def read_movies():
    try:

        Movies_list = []
        with open(FILENAME, newline="")as file:
            reader = csv.reader(file)
            for row in reader:  # going by each line in the file
                Movies_list.append(row) #each line will be assigned as an item in the list. once completed it will return the list
            return Movies_list
    except FileNotFoundError:
        print("Could  not find " + FILENAME + " file.")
    except Exception as e:
        print(type(e), e)



def Display_menu():
    print("DISPLAY MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("delete - Delete a movie")
    print("find - Find a movie by the year")
    print("exit - Exit program")
    print()
    print("PSA.......We will be adding more features as we figure out customer needs")
    print("Patch 1.2")


def List(Movies_list):
    if len(Movies_list) == 0: 
        print("There are no movies in the list. \n")
        return
    else:
        print("List of movies and their year")
        i = 1
        for i, movie in enumerate(Movies_list, start=1):
            print(f"{i}. {movie[0]} ({movie[1]})")
            i += 1
        print()
def add(Movies_list):

    name = input("Name of movie: ")
    year = input("Year: ")
    movie = []
    movie.append(name)
    movie.append(year)
    movie.append(year)
    Movies_list.append(movie)
    write_movies(Movies_list)
    print(movie[0] + " was added. \n") 

def find(Movies_list):
    year = int(input("Year of the movie: "))
    for movie in Movies_list:
        if movie[1] == year:
            print(f"{movie[0]} was released in {year}")
        print()

def delete(Movies_list):
    while True:
        try:
            number = int(input("Enter the number for the movie: "))
        except ValueError:
            print("Invalid. That is not an integer. PLease try again")
            continue
        if number < 1 and number > len(Movies_list):
            print("Invalid movie number. returning to main menu \n")
        else:
            movie = Movies_list.pop(number -1)
            write_movies(Movies_list)
            print(movie[0] + " was deleted \n")
def main():
    Display_menu()

    Movies_list = read_movies()

    while True:
        command = str(input("Command:"))
        if command.lower() == "list":
            List(Movies_list)
        elif command.lower() == "add":
            add(Movies_list)
        elif command.lower() == "delete":
            delete(Movies_list)
        elif command.lower() == "find":
            find(Movies_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid selection my friend. Please try again. \n")
    print("Bye")

if __name__ == "__main__":
    main()

