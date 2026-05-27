import ui_module

from settings import MYSQL_HOST

from sql_requests import get_all_films

from sql_requests import search_films, get_all_categories
#-----------------------------------------------------------------------------------------------------------------------

# print(get_all_films())
#print(MYSQL_HOST)

#-----------------------------------------------------------------------------------------------------------------------

def main():

    ui_module.show_welcome()

    while True:
        ui_module.show_menu()

        select_options()

#-----------------------------------------------------------------------------------------------------------------------

def select_options():

    choice = input("Choose an option: ")

    if choice == "1":
        keyword = input('Enter a film name: ')
        films = search_films(keyword)
        for i, row in enumerate(films, start=1):
            print(f'{i}. {row[0]}')

    elif choice == "2":
        categories = get_all_categories()
        print("\nAvailable categories:\n")
        for i, row in enumerate(categories, start=1):
            print(f'{i}. {row[0]}')

    elif choice == "3":
        choice_year = input("Enter a year or year range: ")

    elif choice == "4":
        pass

    elif choice == "5":
        print("Goodbye!")
        pass

#-----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------------------------------------------------------