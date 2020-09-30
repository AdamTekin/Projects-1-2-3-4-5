CREATE TABLE phonebook_db.phonebook(
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(100) NOT NULL,
    number VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utff8mb4 COLLATE=utff8mb4_unicode_ci;

INSERT INTO phonebook_db.phonebook (name, number)
    VALUES
        ("Callahan", "123456789"),
        ("Sergio Taco", "87654321"),
        ("Vincenzo Altobelli", "9836457283");

        
