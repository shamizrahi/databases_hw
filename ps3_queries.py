#
# CS 105: Problem Set 3
#

#
# For each problem, use a text editor to add the appropriate SQL
# command between the triple quotes provided for that problem's variable.
#
# For example, here is how you would include a query that finds the
# names and years of all movies in the database with an R rating:
#
sample = """
    SELECT name, year
    FROM Movie
    WHERE rating = 'R';
"""

#
# Problem 1. Put your SQL command between the triple quotes found below.
# Follow the same format as the model query shown above.
#
problem1 = """
    SELECT M.name 
    FROM Movie M, Person P, Actor A
    WHERE P.name = 'Jason Alexander'
	AND P.id = A.actor_id
	AND M.id = A.movie_id;

"""

#
# Problem 2. Put your SQL command between the triple quotes found below.
#
problem2 = """
    SELECT SUM(earnings_rank)
    FROM Movie
    WHERE name like 'Avengers%';

"""

#
# Problem 3. Put your SQL command between the triple quotes found below.
#
problem3 = """
    SELECT COUNT(type)
    FROM Oscar O, Person P
    WHERE pob like 'New York, New York%'
    AND P.id = O.person_id;

"""

#
# Problem 4. Put your SQL command between the triple quotes found below.
#
problem4 = """
    SELECT P.name, COUNT(A.movie_id)
    FROM Person P, Actor A
    WHERE P.id = A.actor_id
    GROUP BY P.name
    HAVING COUNT(A.movie_id) >= 10;

"""

#
# Problem 5. Put your SQL command between the triple quotes found below.
#
problem5 = """
    SELECT  COUNT(*)
    FROM Movie
    WHERE year = 2020 OR year = 2021
    AND earnings_rank BETWEEN 1 AND 200;
    
"""

#
# Problem 6. Put your SQL command between the triple quotes found below.
#
problem6 = """
    SELECT  P.name
    FROM Person P
    WHERE pob like 'Boston, Mass%'
    AND P.id NOT IN (SELECT A.actor_id
                     FROM Actor A)

"""

#
# Problem 7. Put your SQL command between the triple quotes found below.
#
problem7 = """
    SELECT P.name, COUNT(O.type)
    FROM Person P LEFT OUTER JOIN Oscar O
		ON P.id = O.person_id
    WHERE P.pob like '%, Virginia, USA'
    GROUP BY P.name;

"""

#
# Problem 8. Put your SQL command between the triple quotes found below.
#
problem8 = """

    UPDATE Movie
    SET earnings_rank = 356
    WHERE name like 'Captain America: %'
    AND year = 2011;

"""
