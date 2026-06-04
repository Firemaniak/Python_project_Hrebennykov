# Queries Stored in Variables

GET_ALL_FILMS = """
    SELECT film_id, title
    FROM film
"""

SEARCH_FILMS = """
    SELECT title
    FROM film
    WHERE title LIKE %s
    LIMIT 10
"""

GET_ALL_CATEGORIES = """
    SELECT category_id, name
    FROM category
    ORDER BY name
"""

SELECT_CATEGORY = """
    SELECT f.title
    FROM film AS f
    JOIN film_category AS fc
        ON f.film_id = fc.film_id
    WHERE fc.category_id = %s
    ORDER BY f.title
    LIMIT %s OFFSET %s
"""

SEARCH_BY_YEAR_RANGE = """
    SELECT title, release_year
    FROM film
    WHERE release_year BETWEEN %s AND %s
    ORDER BY release_year, title
    LIMIT %s OFFSET %s
"""

GET_YEAR_RANGE = """
    SELECT MIN(release_year), MAX(release_year)
    FROM film
"""