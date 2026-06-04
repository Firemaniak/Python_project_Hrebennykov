# Movie Search Application

## Description

Movie Search Application is a console-based Python application that allows users to search movies 
using the MySQL Sakila database.

The application supports searching movies by title, category, and year range. It also stores search statistics 
in MongoDB Atlas and displays the most popular movie searches.

---

## Features

* Search movies by title
* Search movies by category
* Search movies by year range
* Popular search statistics
* Pagination (15 movies per page)
* Input validation
* MySQL integration
* MongoDB Atlas integration

---

## Technologies

* Python 3
* MySQL (Sakila Database)
* MongoDB Atlas
* PyMySQL
* PyMongo
* python-dotenv

---

## Project Structure

```text
main.py

select_options.py
ui_module.py

sql_queries.py
sql_requests.py
my_sql_client.py
db_decorators.py

mongo_client.py
logger.py

settings.py

requirements.txt
README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Firemaniak/Python_project_Hrebennykov
cd Python_project_Hrebennykov
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file and add the following variables:

```env
MYSQL_HOST=your_host
MYSQL_USER=your_user
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=your_database
MYSQL_PORT=3306

MONGO_URI=your_mongodb_connection_string
```

---

## Run Application

```bash
python main.py
```

---

## Screenshots

### Main Menu

![Main Menu](screenshots/001_main_menu.png)

### Search by Title

![Search by Title](screenshots/002_search_title.png)

### Search by Category

![Category Search](screenshots/003_category_search.png)

### Search by Year Range

![Search by Year Range](screenshots/004_year_search.png)

### Popular Searches

![Popular Searches](screenshots/005_popular_searches.png)

---

## Database Design

### MySQL

MySQL (Sakila database) is used to store movie information and perform movie searches.

### MongoDB Atlas

MongoDB Atlas is used to store and analyze movie search statistics.

---

## Author

Oleksii Hrebennykov / 121225-ptm

---

## Future Improvements

* Export search results to file
* Advanced movie filters
* User authentication
* Web interface
* Docker support
