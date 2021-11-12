import sqlite3

database = input('Enter the name of the database file: ')
db = sqlite3.connect(database)
cursor = db.cursor()

rating = input('Enter the rating: ')
rank = input('Enter the earnings-rank cutoff: ')

filename = input('Enter the name of the results file: ')
f = open(filename, 'w')

# Execute the query.
command = '''SELECT earnings_rank, name, year
             FROM Movie
             WHERE rating = ?
               AND earnings_rank <= ?
             ORDER BY earnings_rank;'''
             
cursor.execute(command, [rating, rank])
print()

count = 0
for row in cursor:
    rate = str(row[0])
    movie = str(row[1])
    year = str(row[2])

    print(rate +','+ movie + ','+ year, file=f)
    count +=1
    
if (count == 0):
    print('There are no movies in the database that match your criteria.')
else:
    print('Wrote '+ str(count) + ' lines of results to the file.')
    
    
db.commit()
db.close()
f.close()
