import sqlite3
from random import randint
# cursor.execute("INSERT INTO movie (title,year,path) VALUES('The Shining',1980,'pictures\\The-Shining.ppm')")
# cursor.execute("INSERT INTO movie (title,year,path)"
#                " VALUES('The Lord of the Rings The Return of the King',2003,'pictures\\The Lord of the Rings The Return of the King.ppm')")
#
# cursor.execute("INSERT INTO movie (title,year,path)"
#                " VALUES('The Lord of the Rings The Two Towers',2002,'pictures\\The-Lord-of-the-Rings-The-Two-Towers.ppm')")
#
# cursor.execute("INSERT INTO movie (title,year,path)"
#                " VALUES('The Matrix',1999,'pictures\\The-Matrix.ppm')")
#
# cursor.execute("INSERT INTO movie (title,year,path)"
#                " VALUES('The Pianist',2002,'pictures\\The-Pianist.ppm')")
#
# cursor.execute("INSERT INTO movie (title,year,path)"
#                " VALUES('The Prestige',2006,'pictures\\The-Prestige.ppm')")
#
# cursor.execute("INSERT INTO movie (title,year,path)"
#                " VALUES('The Shawshank Redemption',1994,'pictures\\The-Shawshank-Redemption.ppm')")

class DataBaseService:

    def __init__(self):
        self.connection = sqlite3.connect('movie_db.db')
        self.cursor = self.connection.cursor()
        self.rowcount = self.get_all()

    def __del__(self):
        self.connection.close()

    def get_random_movie(self):
        self.get_all()
        rnd = randint(1,self.rowcount)
        rnd_movie = self.cursor.execute('SELECT * FROM movie WHERE id={}'.format(rnd)).fetchone()

        return rnd_movie

    def get_variants(self):
        variants = set()

        while len(variants) != 3:
            rnd = randint(1, self.rowcount)
            rnd_movie = self.cursor.execute('SELECT * FROM movie WHERE id={}'.format(rnd)).fetchone()
            variants.add(rnd_movie)

        return variants

    def get_all(self):
        self.cursor.execute('SELECT COUNT() FROM movie')

        return self.cursor.fetchone()[0]

# db = DataBaseService()
# print(db.get_all())
# connection = sqlite3.connect('movie_db.db')
# cursor = connection.cursor()
# cursor.execute("INSERT INTO movie (title,year,path)"
#                " VALUES('The Lord of the Rings The Return of the King',2003,'pictures\\The Lord of the Rings The Return of the King.ppm')")
#
# cursor.execute("INSERT INTO movie (title,year,path)"
#                " VALUES('The Lord of the Rings The Two Towers',2002,'pictures\\The-Lord-of-the-Rings-The-Two-Towers.ppm')")
#
# cursor.execute("INSERT INTO movie (title,year,path)"
#                " VALUES('The Matrix',1999,'pictures\\The-Matrix.ppm')")
#
# cursor.execute("INSERT INTO movie (title,year,path)"
#                " VALUES('The Pianist',2002,'pictures\\The-Pianist.ppm')")
#
# cursor.execute("INSERT INTO movie (title,year,path)"
#                " VALUES('The Prestige',2006,'pictures\\The-Prestige.ppm')")
#
# cursor.execute("INSERT INTO movie (title,year,path)"
#                " VALUES('The Shawshank Redemption',1994,'pictures\\The-Shawshank-Redemption.ppm')")
# cursor.execute('SELECT * FROM movie')
#
# for row in cursor.fetchall():
#     print(row)
# connection.commit()
# connection.close()
# cursor.execute('SELECT COUNT() FROM movie')
# print(cursor.fetchone()[0])