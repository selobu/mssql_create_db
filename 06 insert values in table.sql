USE Test;
INSERT INTO [Usuario] ([nombre],[apellido])
VALUES
    ('Sebastian' , 'Lopez'),
    ('Beatriz', 'Lopez'),
    ('Yolanda', 'Buritica'),
    ('Manuel', 'Parga');
SELECT TOP 4 * FROM usuario
ORDER BY id DESC;
