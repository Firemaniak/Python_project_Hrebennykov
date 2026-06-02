#Модуль для работы с интерфейсом пользователя

#-----------------------------------------------------------------------------------------------------------------------

def show_welcome():
    # print(f'Welcome to Kozak_production \n{50 * "-"}')
    print("""
                Welcome to Kozak_production!

In this console application, you can find the perfect movie for any mood or taste.

You can search for movies in two ways:
1. By keyword search (search by part of the movie title).
2. By genre and release year range.
   Before searching, you will see:
   - a list of all available genres
   - the minimum and maximum release years in the database

You can also stay on trend and discover what other users are searching 
for with our most popular search statistics.

--- Enter 1 to search by keyword
--- Enter 2 to view all genres
--- Enter 3 to search by release year range
--- Enter 4 to show favorite movies
--- Enter 0 to exit the program

"""
)

#-----------------------------------------------------------------------------------------------------------------------

def show_menu():
    print("""
        ==============================
               MOVIE SEARCH APP
        ==============================

        1. Search movies by keyword
        2. View all genres
        3. Search by genre and year range
        4. View popular searches
        0. Exit
    """)

#-----------------------------------------------------------------------------------------------------------------------
