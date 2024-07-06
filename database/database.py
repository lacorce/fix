import sqlite3 as sq

db = sq.connect('database/database.db')
cur = db.cursor()


def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS user_table('
                'tsekh TEXT,'
                'vacancy TEXT,'
                'questions TEXT)')

    cur.execute('CREATE TABLE IF NOT EXISTS admin('
            'id INTEGER PRIMARY KEY AUTOINCREMENT)')

async def add_tseh(tsekh, vacancy, questions):
    cur.execute('INSERT INTO user_table(tsekh, vacancy, questions) VALUES(?, ?, ?)', (tsekh, vacancy, questions))
    db.commit()