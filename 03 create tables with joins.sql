USE Test;
/* cada usuario tiene muchas direcciones*/
CREATE TABLE Usuario (
    id INTEGER NOT NULL IDENTITY,
    nombre VARCHAR(200) NOT NULL,
    apellido VARCHAR(200) NOT NULL,
    PRIMARY KEY (id)
)
CREATE TABLE Direccion (
    id INTEGER NOT NULL IDENTITY,
    direcccion VARCHAR(300) NOT NULL,
    PRIMARY KEY (id),
    user_id INTEGER NULL,
    FOREIGN KEY (user_id) REFERENCES Usuario(id),
)

