import sqlite3


def create_db():
    import sqlite3

    conn = sqlite3.connect('pets.db')
    c = conn.cursor()

    c.execute('''DROP TABLE IF EXISTS person''')
    c.execute('''CREATE TABLE person (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age INTEGER
        )''')

    c.execute('''DROP TABLE IF EXISTS pet''')
    c.execute('''CREATE TABLE pet (
        id INTEGER PRIMARY KEY,
        name TEXT,
        breed TEXT,
        age INTEGER,
        dead INTEGER
    )''')

    c.execute('''DROP TABLE IF EXISTS person_pet''')
    c.execute('''CREATE TABLE person_pet (
        person_id INTEGER,
        pet_id INTEGER
    )''')

    people = [
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23)
    ]

    pets = [(1, 'Rusty', 'Dalmation', 4, 1),
            (2, 'Bella', 'Alaskan Malamute', 3, 0),
            (3, 'Max', 'Cocker Spaniel', 1, 0),
            (4, 'Rocky', 'Beagle', 7, 0),
            (5, 'Rufus', 'Cocker Spaniel', 1, 0),
            (6, 'Spot', 'Bloodhound', 2, 1)]

    people_to_pets = [(1, 1),
                      (1, 2),
                      (2, 3),
                      (2, 4),
                      (3, 5),
                      (4, 6)]

    c.executemany('INSERT INTO person VALUES (?,?,?,?)', people)
    c.executemany('INSERT INTO pet VALUES (?,?,?,?,?)', pets)
    c.executemany('INSERT INTO person_pet VALUES (?,?)', people_to_pets)

    conn.commit()


if __name__ == '__main__':
    create_db()
    # creates connection to database
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()

    person_id = ''

    while person_id != '-1':

        person_id = raw_input('Please enter your ID number: To exit query, enter -1')
        query = '''
        SELECT *
        FROM person
        JOIN person_pet ON person.id = person_pet.person_id
        JOIN pet ON pet.id = person_pet.pet_id
        WHERE {} == person.id 
        '''.format(person_id)
        c.execute(query)
        result = c.fetchall()
        for row in result:
            print('{} {}, {} years old'.format(row[1], row[2], row[3]))
            print('{} {} owned {}, a {}, that was {} years old'.format(row[1], row[2], row[5], row[6], row[7]))
