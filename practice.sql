Find all the information about each film
/Solution
SELECT title, year FROM movies; 

Find the first 5 Pixar movies and their release year
/Solution 
SELECT title, year FROM movies
WHERE year < 2000 

Find all the WALL-* movies
/Solution
SELECT title, director FROM movies 
WHERE director != "John Lasseter";

List the next five Pixar movies sorted alphabetically 
/Solution
SELECT title FROM movies
ORDER BY title ASC
LIMIT 5 OFFSET 5;

List the third and fourth largest cities (by population) in the United States and their population
/Solution
SELECT city, population FROM north_american_cities
WHERE country LIKE "United States"
ORDER BY population DESC
LIMIT 2 OFFSET 2;

List all the movies by their ratings in descending order
/Solution
SELECT title, rating
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id
ORDER BY rating DESC;

List all buildings and the distinct employee roles in each building (including empty buildings)
/   Solution
SELECT DISTINCT building_name, role 
FROM buildings 
  LEFT JOIN employees
    ON building_name = building;

Find the names of the buildings that hold no employees 
/Solution
SELECT DISTINCT building_name
FROM buildings 
  LEFT JOIN employees
    ON building_name = building
WHERE role IS NULL;

List all movies and their combined sales in millions of dollars
/Solution
SELECT title, (domestic_sales + international_sales) / 1000000 AS gross_sales_millions
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
