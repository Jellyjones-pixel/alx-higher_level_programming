#!/usr/bin/python3
'''Function that filters by user input'''
import MySQLdb
from sys import argv


def main(argv):

    if len(argv) != 4:
        print('Incorrect number of arguments')
        return

    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute('SELECT cities.id, cities.name, states.name \
    FROM cities \
    INNER JOIN states on states.id = cities.state_id ORDER BY cities.id ASC')

    for row in cur.fetchall():
        print(row)

    db.close()


if __name__ == '__main__':
    main(argv)
