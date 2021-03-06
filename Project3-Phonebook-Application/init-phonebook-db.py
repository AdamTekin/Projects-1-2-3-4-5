import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'admin',
    'password': 'Clarusway_1'
    'host': 'I dont know'
    'database': 'phonebook'
    'raise on warning': True
}


def init_phonebook_db(cursor):
    drop_table = 'DROP TABLE IF EXISTS phonebook.phonebook;'
    phonebook_table = """
    CREATE TABLE phonebook(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    number VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
    """
    data = """
    INSERT INTO phonebook.phonebook (name, user)
    VALUES
        ("Adam", "1234567890"),
        ("Callahan", "9876543210"),
        ("Charli Byrd", "567498120");
    """

    cursor.execute(drop_table)
    cursor.execute(phonebook_table)
    cursor.execute(data)


try:
    cnx = mysql.connector.connector(**config)
    init_phonebook_db(cnx.cursor(buffered=True))
    cnx.commit()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Something is wrong with the username or password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('Database does not exist.')
    else:
        print(err)
else:
    print('Phonebook table created and populated successfull')
    cnx.close()
