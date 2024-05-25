-- Este script crea una base de datos llamada 'proyecto' y una tabla llamada 'Membresia'.
CREATE DATABASE proyecto1;
USE proyecto1;

-- La tabla 'Membresia' almacena información sobre membresías.
CREATE TABLE Membresia (
    IDMembresia CHAR(9) NOT NULL, -- Identificador único de la membresía.
    tipo VARCHAR(20) NOT NULL, -- Tipo de membresía (por ejemplo, 'Premium', 'Básica', etc.).
    costo DECIMAL(9, 2) NOT NULL, -- Costo de la membresía.
    estado CHAR(3) NOT NULL, -- Estado de la membresía: pendiente (P), activo (A) o no activo (NA).
    PRIMARY KEY (IDMembresia) -- Clave primaria que garantiza la unicidad de IDMembresia.
    -- Si la llave primaria fuera compuesta, se indicaría así: PRIMARY KEY (atributo1, atributo2).
);


-- Agrega una restricción de verificación para el campo 'estado' asegurando que solo pueda tener valores 'P', 'A' o 'NA'.
ALTER TABLE Membresia
ADD CONSTRAINT estado_check CHECK (estado = 'P' OR estado = 'A' OR estado = 'NA');
-- Inserta datos en la tabla 'Membresia'.
INSERT INTO Membresia (IDMembresia, tipo, costo, estado)
VALUES 
('M001', 'básica', 50.00, 'P'), -- Membresía básica pendiente.
('M002', 'estándar', 75.00, 'A'), -- Membresía estándar activa.
('M003', 'premium', 100.00, 'P'), -- Membresía premium pendiente.
('M004', 'VIP', 150.00, 'A'), -- Membresía VIP activa.
('M005', 'corporativa', 200.00, 'P'), -- Membresía corporativa pendiente.
('M006', 'familiar', 250.00, 'A'); -- Membresía familiar activa.

-- Crea la tabla 'Cliente' para almacenar información de clientes.
CREATE TABLE Cliente (
    IDCliente CHAR(11) NOT NULL, -- Identificador único del cliente.
    IDMembresia CHAR(9) NOT NULL, -- Identificador de la membresía del cliente.
    nombre VARCHAR(50) NOT NULL, -- Nombre del cliente.
    apellidol VARCHAR(50) NOT NULL, -- Primer apellido del cliente.
    apellido2 VARCHAR(50) NOT NULL, -- Segundo apellido del cliente.
    correoElectronico VARCHAR(100) NOT NULL, -- Correo electrónico del cliente.
    NumeroTelefono CHAR(9) NULL, -- Número de teléfono del cliente (opcional).
    PRIMARY KEY (IDCliente), -- Clave primaria que garantiza la unicidad de IDCliente.
    FOREIGN KEY (IDMembresia) REFERENCES Membresia(IDMembresia) -- Clave foránea que establece una relación con la tabla 'Membresia'.
    -- Si la llave primaria fuera compuesta, se indicaría así: PRIMARY KEY (atributo1, atributo2).
);

ALTER TABLE Cliente MODIFY COLUMN IDMembresia CHAR(9) NULL;


-- Inserta datos en la tabla 'Cliente'
INSERT INTO Cliente (IDCliente, IDMembresia, nombre, apellidol, apellido2, correoElectronico, NumeroTelefono) 
VALUES 
('CL001', 'M001', 'Juan', 'García', 'López', 'juan@example.com', '123456789'),
('CL002', 'M002', 'María', 'Martínez', 'Rodríguez', 'maria@example.com', '987654321'),
('CL003', 'M003', 'Pedro', 'Díaz', 'Pérez', 'pedro@example.com', NULL),
('CL004', 'M004', 'Ana', 'González', 'Sánchez', 'ana@example.com', '654987321'),
('CL005', 'M005', 'Carlos', 'Fernández', 'Gómez', 'carlos@example.com', '321654987'),
('CL006', 'M006', 'Laura', 'López', 'Martínez', 'laura@example.com', '789456123'),
('CL007', 'M001', 'Sofía', 'Hernández', 'Ruiz', 'sofia@example.com', '456123789'),
('CL008', 'M002', 'David', 'Torres', 'Gutiérrez', 'david@example.com', '987123456'),
('CL009', 'M003', 'Elena', 'Vázquez', 'Jiménez', 'elena@example.com', '321789654'),
('CL010', 'M004', 'Francisco', 'Sánchez', 'Molina', 'francisco@example.com', '654321789'),
('CL011', 'M005', 'Lucía', 'Morales', 'Ortega', 'lucia@example.com', '987654123'),
('CL012', 'M006', 'Marcos', 'Gómez', 'Navarro', 'marcos@example.com', '321456987'),
('CL013', 'M001', 'Isabel', 'Ortega', 'Fernández', 'isabel@example.com', '789654321'),
('CL014', 'M002', 'Antonio', 'Jiménez', 'Ruiz', 'antonio@example.com', '456987123'),
('CL015', 'M003', 'Carmen', 'Pérez', 'García', 'carmen@example.com', '123789654'),
('CL016', 'M004', 'Ana', 'García', 'Sánchez', 'ana_g@example.com', '654123789'),
('CL017', 'M005', 'Javier', 'Martínez', 'López', 'javier@example.com', '789654123'),
('CL018', 'M006', 'Marta', 'Fernández', 'Díaz', 'marta@example.com', '123456987'),
('CL019', 'M001', 'Pablo', 'Rodríguez', 'Hernández', 'pablo@example.com', '456789123'),
('CL020', 'M002', 'Laura', 'López', 'González', 'laura_l@example.com', '987321654'),
('CL021', 'M003', 'Diego', 'Sánchez', 'Martínez', 'diego@example.com', '321789456'),
('CL022', 'M004', 'Sara', 'Martínez', 'Sanz', 'sara@example.com', '654987321'),
('CL023', 'M005', 'Adrián', 'Sanz', 'Pérez', 'adrian@example.com', '789321654'),
('CL024', 'M006', 'Eva', 'Fernández', 'López', 'eva@example.com', '321456789'),
('CL025', 'M001', 'José', 'García', 'Díaz', 'jose@example.com', '456987321'),
('CL026', 'M002', 'Cristina', 'Jiménez', 'Gómez', 'cristina@example.com', '987321456'),
('CL027', 'M003', 'Manuel', 'Rodríguez', 'Hernández', 'manuel@example.com', '321654987'),
('CL028', 'M004', 'Natalia', 'Martínez', 'Fernández', 'natalia@example.com', '654321789'),
('CL029', 'M005', 'Raúl', 'López', 'García', 'raul@example.com', '789654321'),
('CL030', 'M006', 'Silvia', 'García', 'Jiménez', 'silvia@example.com', '321789654');
-- Crea la tabla 'PuestoFuncionario' para almacenar información sobre los puestos de los funcionarios.
CREATE TABLE PuestoFuncionario (
    IDPuesto CHAR(9) NOT NULL, -- Identificador único del puesto.
    puesto VARCHAR(30) NOT NULL, -- Nombre del puesto.
    PRIMARY KEY (IDPuesto) -- Clave primaria que garantiza la unicidad de IDPuesto.
);

-- Inserta datos en la tabla 'PuestoFuncionario'.
INSERT INTO PuestoFuncionario (IDPuesto, puesto) 
VALUES 
('PF001', 'Gerente'), -- Puesto de Gerente.
('PF002', 'Entrenador'), -- Puesto de Entrenador.
('PF003', 'Analista de Datos'), -- Puesto de Analista de Datos.
('PF004', 'Desarrollador de Software'), -- Puesto de Desarrollador de Software.
('PF005', 'Especialista en Marketing'), -- Puesto de Especialista en Marketing.
('PF006', 'Asistente Administrativo'); -- Puesto de Asistente Administrativo.

-- Crea la tabla 'Funcionario' para almacenar información sobre los funcionarios.
CREATE TABLE Funcionario (
    IDFuncionario CHAR(11) NOT NULL, -- Identificador único del funcionario.
    puesto CHAR(9) NOT NULL, -- Identificador del puesto del funcionario.
    nombre VARCHAR(50) NOT NULL, -- Nombre del funcionario.
    apellidol VARCHAR(50) NOT NULL, -- Primer apellido del funcionario.
    apellido2 VARCHAR(50) NOT NULL, -- Segundo apellido del funcionario.
    NumeroTelefono CHAR(9) NULL, -- Número de teléfono del funcionario (opcional).
    PRIMARY KEY (IDFuncionario), -- Clave primaria que garantiza la unicidad de IDFuncionario.
    FOREIGN KEY (puesto) REFERENCES PuestoFuncionario(IDPuesto) -- Clave foránea que establece una relación con la tabla 'PuestoFuncionario'.
);
alter table Funcionario modify column puesto char(9);

-- Inserta datos en la tabla 'Funcionario'.
INSERT INTO Funcionario (IDFuncionario, puesto, nombre, apellidol, apellido2, NumeroTelefono) 
VALUES 
('F001', 'PF001', 'Juan', 'García', 'López', '123456789'), -- Funcionario Juan, Gerente.
('F002', 'PF002', 'María', 'Martínez', 'Rodríguez', '987654321'), -- Funcionario María, Entrenador.
('F003', 'PF002', 'Pedro', 'Díaz', 'Pérez', NULL), -- Funcionario Pedro, Entrenador sin número de teléfono.
('F004', 'PF003', 'Ana', 'González', 'Sánchez', '654987321'), -- Funcionario Ana, Analista de Datos.
('F005', 'PF004', 'Carlos', 'Fernández', 'Gómez', '321654987'), -- Funcionario Carlos, Desarrollador de Software.
('F006', 'PF006', 'Laura', 'López', 'Martínez', '789456123'); -- Funcionario Laura, Asistente Administrativo.

-- Crea la tabla 'Ciudad' para almacenar información sobre las ciudades.
CREATE TABLE Ciudad (
    IDCiudad CHAR(9) NOT NULL, -- Identificador único de la ciudad.
    nombre VARCHAR(50) NOT NULL, -- Nombre de la ciudad.
    PRIMARY KEY (IDCiudad) -- Clave primaria que garantiza la unicidad de IDCiudad.
);
-- Insertar datos en la tabla Ciudad
INSERT INTO Ciudad (IDCiudad, nombre) 
VALUES 
('CR001', 'San José'),
('CR002', 'Liberia'),
('CR003', 'Alajuela'),
('CR004', 'Heredia'),
('CR005', 'Puntarenas'),
('CR006', 'Limón');
-- Crea la tabla 'Gimnasio' para almacenar información sobre los gimnasios.
CREATE TABLE Gimnasio (
    IDGimnasio CHAR(9) NOT NULL, -- Identificador único del gimnasio.
    IDCiudad CHAR(9) NOT NULL, -- Identificador de la ciudad donde se encuentra el gimnasio.
    nombre VARCHAR(50) NOT NULL, -- Nombre del gimnasio.
    direccionExacta VARCHAR(200) NOT NULL, -- Dirección exacta del gimnasio.
    NumeroTelefono CHAR(9) NULL, -- Número de teléfono del gimnasio (opcional).
    PRIMARY KEY (IDGimnasio), -- Clave primaria que garantiza la unicidad de IDGimnasio.
    FOREIGN KEY (IDCiudad) REFERENCES Ciudad(IDCiudad) -- Clave foránea que establece una relación con la tabla 'Ciudad'.
);

alter table gimnasio modify column IDCiudad char(9);

-- Inserta datos en la tabla 'Gimnasio'.
INSERT INTO Gimnasio (IDGimnasio, IDCiudad, nombre, direccionExacta, NumeroTelefono) 
VALUES 
('G001', 'CR001', 'Gimnasio Fitness San José', 'Avenida 10, San José, Costa Rica', '22223333'), -- Gimnasio en San José.
('G002', 'CR002', 'Gimnasio Power Liberia', 'Calle 6, Liberia, Costa Rica', '26664444'), -- Gimnasio en Liberia.
('G003', 'CR003', 'Gimnasio Wellness Alajuela', 'Avenida Central, Alajuela, Costa Rica', '24445555'), -- Gimnasio en Alajuela.
('G004', 'CR004', 'Gimnasio Energy Heredia', 'Avenida 2, Heredia, Costa Rica', '28886666'), -- Gimnasio en Heredia.
('G005', 'CR005', 'Gimnasio Fit Puntarenas', 'Calle 7, Puntarenas, Costa Rica', '27779999'), -- Gimnasio en Puntarenas.
('G006', 'CR006', 'Gimnasio Vital Limón', 'Calle 5, Limón, Costa Rica', '29998888'); -- Gimnasio en Limón.

-- Crea la tabla 'Trabaja' para almacenar la relación entre gimnasios y funcionarios.
CREATE TABLE Trabaja (
   IDGimnasio CHAR(9) NOT NULL, -- Identificador del gimnasio.
   IDFuncionario CHAR(11) NOT NULL, -- Identificador del funcionario.
   PRIMARY KEY (IDGimnasio, IDFuncionario), -- Clave primaria compuesta por IDGimnasio e IDFuncionario.
   FOREIGN KEY (IDGimnasio) REFERENCES Gimnasio(IDGimnasio), -- Clave foránea que establece una relación con la tabla 'Gimnasio'.
   FOREIGN KEY (IDFuncionario) REFERENCES Funcionario(IDFuncionario) -- Clave foránea que establece una relación con la tabla 'Funcionario'.
);
alter table trabaja modify column IDGimnasio char(9);
alter table trabaja modify column IDFuncionario char(11);


-- Inserta datos en la tabla 'Trabaja'.
INSERT INTO Trabaja (IDGimnasio, IDFuncionario)
VALUES 
('G001', 'F001'), -- Asigna el gerente Juan al Gimnasio Fitness San José.
('G002', 'F002'), -- Asigna el entrenador María al Gimnasio Power Liberia.
('G003', 'F003'), -- Asigna el entrenador Pedro al Gimnasio Wellness Alajuela.
('G004', 'F004'), -- Asigna el analista Ana al Gimnasio Energy Heredia.
('G005', 'F005'), -- Asigna el desarrollador Carlos al Gimnasio Fit Puntarenas.
('G006', 'F006'); -- Asigna el asistente administrativo Laura al Gimnasio Vital Limón.

-- Crea la tabla 'Equipo' para almacenar información sobre el equipo del gimnasio.
CREATE TABLE Equipo (
  CodigoEquipo CHAR(9) NOT NULL, -- Código único del equipo.
  CodigoGimnasio CHAR(9) NOT NULL, -- Código del gimnasio al que pertenece el equipo.
  nombre VARCHAR(50) NOT NULL, -- Nombre del equipo.
  estado CHAR(3) NOT NULL, -- Estado del equipo (Disponible (D), en Mantenimiento (M), Fuera de Servicio (FS)).
  fechaAdquisicion DATE NOT NULL, -- Fecha de adquisición del equipo.
  PRIMARY KEY (CodigoEquipo), -- Clave primaria que garantiza la unicidad de CodigoEquipo.
  FOREIGN KEY (CodigoGimnasio) REFERENCES Gimnasio(IDGimnasio) -- Clave foránea que establece una relación con la tabla 'Gimnasio'.
);

-- Agrega una restricción de verificación para el campo 'estado' en la tabla 'Equipo'.
ALTER TABLE Equipo
ADD CONSTRAINT check_estado CHECK (estado = 'D' OR estado = 'M' OR estado = 'FS');

-- Inserta datos en la tabla 'Equipo'.
INSERT INTO Equipo (CodigoEquipo, CodigoGimnasio, nombre, estado, fechaAdquisicion)
VALUES 
('EQP001', 'G001', 'Máquina de correr', 'D', '2023-01-15'), -- Equipo disponible.
('EQP002', 'G001', 'Bicicleta estática', 'M', '2022-12-20'), -- Equipo en mantenimiento.
('EQP003', 'G001', 'Mancuernas ajustables', 'D', '2023-02-10'), -- Equipo disponible.
('EQP004', 'G001', 'Máquina de remo', 'FS', '2023-03-05'), -- Equipo fuera de servicio.
('EQP005', 'G001', 'Banco de pesas', 'M', '2023-04-08'), -- Equipo en mantenimiento.
('EQP006', 'G001', 'Elíptica', 'D', '2022-11-25'), -- Equipo disponible.
('EQP007', 'G001', 'Máquina de prensa de piernas', 'D', '2023-05-12'), -- Equipo disponible.
('EQP008', 'G001', 'Cinta de estiramiento', 'M', '2023-06-18'), -- Equipo en mantenimiento.
('EQP009', 'G001', 'Barra olímpica', 'D', '2023-07-21'), -- Equipo disponible.
('EQP010', 'G001', 'Balón de yoga', 'M', '2022-10-30'); -- Equipo en mantenimiento.

-- Crea la tabla 'Clase' para almacenar información sobre las clases en el gimnasio.
CREATE TABLE Clase (
   IDClase CHAR(9) NOT NULL, -- Identificador único de la clase.
   IDFuncionario CHAR(11) NOT NULL, -- Identificador del funcionario que imparte la clase.
   nombre VARCHAR(50) NOT NULL, -- Nombre de la clase.
   capacidadMaxima INT NOT NULL, -- Capacidad máxima de la clase.
   PRIMARY KEY (IDClase), -- Clave primaria que garantiza la unicidad de IDClase.
   FOREIGN KEY (IDFuncionario) REFERENCES Funcionario(IDFuncionario) -- Clave foránea que establece una relación con la tabla 'Funcionario'.
);

-- Inserta datos en la tabla 'Clase'.
INSERT INTO Clase (IDClase, IDFuncionario, nombre, capacidadMaxima) 
VALUES 
('C001', 'F002', 'Yoga', 20), -- Clase de Yoga.
('C002', 'F002', 'Pilates', 18), -- Clase de Pilates.
('C003', 'F003', 'Spinning', 25), -- Clase de Spinning.
('C004', 'F003', 'Zumba', 22), -- Clase de Zumba.
('C005', 'F002', 'Entrenamiento Funcional', 15), -- Clase de Entrenamiento Funcional.
('C006', 'F003', 'Aeróbicos', 30); -- Clase de Aeróbicos.

-- Crea la tabla 'Inscribirse' para almacenar la relación entre clases y clientes.
CREATE TABLE Inscribirse (
   codigoInscripcion INT AUTO_INCREMENT, -- Campo de incremento automático para la clave primaria.
   IDClase CHAR(9) NOT NULL, -- Identificador de la clase.
   IDCliente CHAR(11) NOT NULL, -- Identificador del cliente.
   PRIMARY KEY (codigoInscripcion), -- Define la clave primaria de la tabla.
   FOREIGN KEY (IDClase) REFERENCES Clase(IDClase), -- Clave foránea que establece una relación con la tabla 'Clase'.
   FOREIGN KEY (IDCliente) REFERENCES Cliente(IDCliente) -- Clave foránea que establece una relación con la tabla 'Cliente'.
);




-- Inserta datos en la tabla 'Inscribirse'. (Los valores de inserción están pendientes.)

INSERT INTO Inscribirse (IDClase, IDCliente) 
VALUES 
('C003', 'CL003'),
('C004', 'CL004'),
('C005', 'CL005'),
('C006', 'CL006'),
('C001', 'CL007'),
('C002', 'CL008'),
('C003', 'CL009'),
('C004', 'CL010'),
('C005', 'CL011'),
('C006', 'CL012'),
('C001', 'CL013'),
('C002', 'CL014'),
('C003', 'CL015'),
('C004', 'CL016'),
('C005', 'CL017'),
('C006', 'CL018'),
('C001', 'CL019'),
('C002', 'CL020'),
('C003', 'CL021'),
('C004', 'CL022'),
('C005', 'CL023'),
('C006', 'CL024'),
('C001', 'CL025'),
('C002', 'CL026'),
('C003', 'CL027'),
('C004', 'CL028'),
('C005', 'CL029'),
('C006', 'CL030');
-- Crea la tabla 'Producto' para almacenar información sobre los productos disponibles.
CREATE TABLE Producto (
   IDProducto CHAR(9) NOT NULL, -- Identificador único del producto.
   nombre VARCHAR(50) NOT NULL, -- Nombre del producto.
   descripcion VARCHAR(200) NOT NULL, -- Descripción del producto.
   costo DECIMAL(9, 2) NOT NULL, -- Costo del producto.
   PRIMARY KEY (IDProducto) -- Clave primaria que garantiza la unicidad de IDProducto.
);

-- Inserta datos en la tabla 'Producto'.
INSERT INTO Producto (IDProducto, nombre, descripcion, costo) 
VALUES 
('PROD001', 'Botella de agua', 'Botella de agua reutilizable de 500ml', 2.50), -- Producto: Botella de agua.
('PROD002', 'Toalla de microfibra', 'Toalla absorbente de secado rápido', 15.99), -- Producto: Toalla de microfibra.
('PROD003', 'Shaker', 'Botella mezcladora para preparar batidos de proteínas', 9.99), -- Producto: Shaker.
('PROD004', 'Guantes para levantar pesas', 'Guantes acolchados para proteger las manos durante el levantamiento de pesas', 12.50), -- Producto: Guantes para levantar pesas.
('PROD005', 'Banda elástica de resistencia', 'Banda de resistencia para ejercicios de fortalecimiento y estiramiento', 7.99), -- Producto: Banda elástica de resistencia.
('PROD006', 'Barra de proteína', 'Barra energética con alto contenido de proteínas para la recuperación muscular', 3.99), -- Producto: Barra de proteína.
('PROD007', 'Cuerda para saltar', 'Cuerda de saltar ajustable para ejercicios cardiovasculares', 5.99), -- Producto: Cuerda para saltar.
('PROD008', 'Gel de ducha deportivo', 'Gel de ducha especialmente formulado para deportistas', 8.50), -- Producto: Gel de ducha deportivo.
('PROD009', 'Calcetines deportivos', 'Calcetines transpirables y acolchados para actividades deportivas', 6.99), -- Producto: Calcetines deportivos.
('PROD010', 'Bolso deportivo', 'Bolso resistente al agua con compartimentos para llevar equipo de entrenamiento', 29.99); -- Producto: Bolso deportivo.

-- Crea la tabla 'Venta' para almacenar información sobre las ventas de productos.
CREATE TABLE Venta (
   NumeroTransaccion INT NOT NULL, -- Número único de la transacción.
   IDCliente CHAR(11) NOT NULL, -- Identificador del cliente que realizó la compra.
   IDProducto CHAR(9) NOT NULL, -- Identificador del producto vendido.
   fechaAdquisicion DATE NOT NULL, -- Fecha de adquisición del producto.
   monto DECIMAL(9, 2) NOT NULL, -- Monto total de la transacción.
   cantidad INT NOT NULL, -- Cantidad de productos vendidos.
   PRIMARY KEY (NumeroTransaccion), -- Clave primaria que garantiza la unicidad de NumeroTransaccion.
   FOREIGN KEY (IDCliente) REFERENCES Cliente(IDCliente), -- Clave foránea que establece una relación con la tabla 'Cliente'.
   FOREIGN KEY (IDProducto) REFERENCES Producto(IDProducto) -- Clave foránea que establece una relación con la tabla 'Producto'.
);
alter table venta modify column IDCliente char(11);

-- Inserta datos en la tabla 'Venta'.
INSERT INTO Venta (NumeroTransaccion, IDCliente, IDProducto, fechaAdquisicion, monto, cantidad) 
VALUES 
(1001, 'CL001', 'PROD001', '2024-04-01', 2.50, 1), -- Venta: Botella de agua.
(1002, 'CL002', 'PROD002', '2024-04-02', 15.99, 1), -- Venta: Toalla de microfibra.
(1003, 'CL003', 'PROD003', '2024-04-03', 9.99, 1), -- Venta: Shaker.
(1004, 'CL004', 'PROD004', '2024-04-04', 12.50, 1), -- Venta: Guantes para levantar pesas.
(1005, 'CL005', 'PROD005', '2024-04-05', 7.99, 1), -- Venta: Banda elástica de resistencia.
(1006, 'CL006', 'PROD006', '2024-04-06', 3.99, 1); -- Venta: Barra de proteína.

-- Esta consulta selecciona el nombre, apellido y tipo de membresía de los clientes, junto con el costo de la membresía, ordenados por apellido.
SELECT cliente.nombre, cliente.apellidol, cliente.apellido2,
cliente.IDMembresia, membresia.costo
FROM cliente 
INNER JOIN membresia ON cliente.IDMembresia = membresia.IDMembresia
ORDER BY cliente.apellidol;

-- Esta consulta selecciona el número de transacción, ID del cliente, nombre del cliente, apellido del cliente, ID del producto y nombre del producto de cada venta.
SELECT venta.NumeroTransaccion, venta.IDCliente, cliente.nombre, cliente.apellidol, 
cliente.apellido2, venta.IDProducto, producto.nombre
FROM venta 
INNER JOIN cliente ON venta.IDCliente = cliente.IDCliente
INNER JOIN producto ON producto.IDProducto = venta.IDProducto;

-- Esta consulta selecciona el nombre del gimnasio, su número de teléfono y el nombre de la ciudad a la que pertenece.
SELECT gimnasio.nombre, gimnasio.NumeroTelefono, ciudad.nombre
FROM gimnasio 
LEFT JOIN ciudad ON gimnasio.IDCiudad = ciudad.IDCiudad;

-- Esta consulta cuenta el número de clientes inscritos por cada funcionario en cada clase en cada gimnasio.
SELECT funcionario.nombre, funcionario.apellidol, puestoFuncionario.puesto, clase.nombre,
gimnasio.nombre, COUNT(cliente.IDCliente) AS clientesInscritos
FROM clase
INNER JOIN funcionario ON clase.IDFuncionario = funcionario.IDFuncionario
INNER JOIN puestoFuncionario ON funcionario.puesto = puestoFuncionario.IDPuesto
INNER JOIN inscribirse ON clase.IDClase = inscribirse.IDClase
INNER JOIN cliente ON inscribirse.IDCliente = cliente.IDCliente
INNER JOIN trabaja ON funcionario.IDFuncionario = trabaja.IDFuncionario 
INNER JOIN gimnasio ON trabaja.IDGimnasio = gimnasio.IDGimnasio
GROUP BY funcionario.nombre, funcionario.apellidol, puestoFuncionario.puesto, clase.nombre, gimnasio.nombre;

-- Esta consulta selecciona el código de equipo, nombre del equipo y nombre del gimnasio al que pertenece cada equipo.
SELECT equipo.CodigoEquipo, equipo.nombre, gimnasio.nombre 
FROM equipo 
INNER JOIN gimnasio ON equipo.CodigoGimnasio = gimnasio.IDGimnasio;


-- ////////////////////////////////////////////FUNCIONES DEL PROYECTO////////////////////////////////////////////

-- ////////////////////////////////////////////FUNCIONES DEL PROYECTO////////////////////////////////////////////
--  Membresía función para actualizar datos
-- Función para actualizar un nuevo registro en la tabla Membresia
DELIMITER //
CREATE procedure verMembresias (

)
BEGIN
select distinct * from membresia;
END //		
DELIMITER ; 
call verMembresias();

-- 1 Membresía procedimiento para insertar datos
-- Procedimiento para insertar un nuevo registro en la tabla Membresia
DELIMITER //
CREATE procedure InsertarMembresia (
    IN IDMembresiaParam CHAR(9),
    IN tipoParam VARCHAR(20),
    IN costoParam DECIMAL(9, 2),
    IN estadoParam CHAR(3)
)
BEGIN
INSERT INTO membresia (IDMembresia, tipo, costo, estado)
VALUES (IDMembresiaParam, tipoParam, costoParam, estadoParam);
END //		
DELIMITER ; 

-- ////////////////////////////////////////////FUNCIONES DEL PROYECTO////////////////////////////////////////////
--  Membresía función para actualizar datos
-- Función para actualizar un nuevo registro en la tabla Membresia
DELIMITER //

CREATE PROCEDURE ActualizarMembresia (
    IN IDMembresiaParam CHAR(9),
    IN tipoParam VARCHAR(20),
    IN costoParam DECIMAL(9, 2),
    IN estadoParam CHAR(3)
)
BEGIN
    IF EXISTS (SELECT 1 FROM Membresia WHERE IDMembresia = IDMembresiaParam) THEN
        UPDATE Membresia
        SET tipo = tipoParam,
            costo = costoParam,
            estado = estadoParam
        WHERE IDMembresia = IDMembresiaParam;
    END IF;
END //

DELIMITER ;



-- ////////////////////////////////////////////FUNCIONES DEL PROYECTO////////////////////////////////////////////
--  Membresía función para eliminar registro


DELIMITER //

CREATE PROCEDURE EliminarMembresia (
    IN IDMembresiaParam CHAR(9)
)
BEGIN
    IF EXISTS (SELECT 1 FROM Membresia WHERE IDMembresia = IDMembresiaParam) THEN
        UPDATE Cliente SET IDMembresia = NULL WHERE IDMembresia = IDMembresiaParam;
        DELETE FROM Membresia WHERE IDMembresia = IDMembresiaParam;
    END IF;
END //

DELIMITER ;




-- ////////////////////////////////////////////FUNCIONES DE LAS CLASES////////////////////////////////////////////
--  Cliente función para Insertar datos
-- Función para insertar un nuevo registro en la tabla Clase

DELIMITER //

CREATE PROCEDURE verClases (

)
BEGIN
	select distinct * from clase;
END //

-- Reset the delimiter back to the semicolon
DELIMITER ;

call verClases();

DELIMITER //

CREATE PROCEDURE InsertarClase (
    IN IDClaseP CHAR(9),
    IN IDFuncionarioP CHAR(11),
    IN nombreP VARCHAR(50),
    IN capacidadMaximaP INT
)
BEGIN
    INSERT INTO clase (IDClase, IDFuncionario, nombre, capacidadMaxima)
    VALUES (IDClaseP, IDFuncionarioP, nombreP, capacidadMaximaP);
END //

-- Reset the delimiter back to the semicolon
DELIMITER ;




DELIMITER //

CREATE PROCEDURE ActualizarClase (
    IN IDClaseP CHAR(9),
    IN IDFuncionarioP CHAR(11),
    IN nombreP VARCHAR(50),
    IN capacidadMaximaP INT
)
BEGIN
    IF EXISTS (SELECT 1 FROM Clase WHERE IDClase = IDClaseP) THEN
        UPDATE Clase
        SET IDFuncionario = IDFuncionarioP,
            nombre = nombreP,
            capacidadMaxima = capacidadMaximaP
        WHERE IDClase = IDClaseP;
    END IF;
END //

DELIMITER ;


DELIMITER //

CREATE PROCEDURE EliminarClase (
    IN IDClaseP CHAR(9)
)
BEGIN
    IF EXISTS (SELECT 1 FROM Clase WHERE IDClase = IDClaseP) THEN
        DELETE FROM Clase WHERE IDClase = IDClaseP;
    END IF;
END //

DELIMITER ;




-- ////////////////////////////////////////////FUNCIONES DE LOS CLIENTES////////////////////////////////////////////

DELIMITER //

CREATE PROCEDURE verClientes (

)
BEGIN
	select distinct * from cliente;
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;

call verClientes();

DELIMITER //

CREATE PROCEDURE InsertarCliente (
    IN IDClienteP CHAR(11),
    IN IDMembresiaP CHAR(9),
    IN nombreP VARCHAR(50),
    IN apellido1P VARCHAR(50),
    IN apellido2P VARCHAR(50),
    IN correoElectronicoP VARCHAR(100),
    IN NumeroTelefonoP CHAR(9)
)
BEGIN
    INSERT INTO cliente (IDCliente, IDMembresia, nombre, apellidol, apellido2, correoElectronico, NumeroTelefono)
    VALUES (IDClienteP, IDMembresiaP, nombreP, apellido1P, apellido2P, correoElectronicoP, NumeroTelefonoP);
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;

DELIMITER //

CREATE PROCEDURE ActualizarCliente (
    IN IDClienteP CHAR(11),
    IN IDMembresiaP CHAR(9),
    IN nombreP VARCHAR(50),
    IN apellido1P VARCHAR(50),
    IN apellido2P VARCHAR(50),
    IN correoElectronicoP VARCHAR(100),
    IN NumeroTelefonoP CHAR(9)
)
BEGIN
    IF EXISTS (SELECT 1 FROM Cliente WHERE IDCliente = IDClienteP) THEN
        UPDATE Cliente
        SET IDCliente = IDClienteP,
            IDMembresia = IDMembresiaP,
            nombre = nombreP,
            apellidol  = apellido1P,
            apellido2 = apellido2P,
            correoElectronico = correoElectronicoP,
            NumeroTelefono = NumeroTelefonoP
        WHERE IDCliente = IDClienteP;
    END IF;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE EliminarCliente (
    IN IDClienteP CHAR(11)
)
BEGIN
    DECLARE cliente_existente INT;
    SELECT COUNT(*) INTO cliente_existente FROM Cliente WHERE IDCliente = IDClienteP;

    IF cliente_existente > 0 THEN
        UPDATE venta SET IDCliente = null WHERE IDCliente = IDClienteP;
        DELETE FROM inscribirse WHERE IDCliente = IDClienteP;
        DELETE FROM Cliente WHERE IDCliente = IDClienteP;
    END IF;
END //

DELIMITER ;

-- ////////////////////////////////////////////FUNCIONES DE Puesto Funcionario////////////////////////////////////////////

DELIMITER //

CREATE PROCEDURE verPuestosFuncionario (

)
BEGIN
	select distinct * from puestoFuncionario;
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;

call verPuestosFuncionario();

DELIMITER //

CREATE PROCEDURE InsertarPuestoFuncionario (
    IN IDPuestoP CHAR(11),
    IN puestoP varchar(30)
)
BEGIN
    INSERT INTO puestoFuncionario (IDPuesto, puesto)
    VALUES (IDPuestoP, puestoP);
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;
drop procedure InsertarPuestoFuncionario;
select * from puestofuncionario p ;
call insertarPuestoFuncionario('PF011', 'Entrenador');


DELIMITER //

CREATE PROCEDURE ActualizarPuestoFuncionario (
    IN IDPuestoP CHAR(11),
    IN puestoP varchar(30)
)
BEGIN
    IF EXISTS (SELECT 1 FROM puestoFuncionario WHERE IDPuesto = IDPuestoP) THEN
        UPDATE puestofuncionario 
        SET IDPuesto = IDPuestoP,
        	puesto = puestoP      
        WHERE IDPuesto = IDPuestoP;
    END IF;
END //

DELIMITER ;


DELIMITER //

CREATE PROCEDURE EliminarPuestoFuncionario (
    IN IDPuestoP CHAR(9)
)
BEGIN
    IF EXISTS (SELECT 1 FROM puestoFuncionario WHERE IDPuesto = IDPuestoP) then
        UPDATE funcionario  SET puesto = null WHERE puesto = IDPuestoP;
        DELETE FROM puestoFuncionario WHERE IDPuesto = IDPuestoP;
    END IF;
END //

DELIMITER ;


-- ////////////////////////////////////////////FUNCIONES DE Funcionarios////////////////////////////////////////////
DELIMITER //

CREATE PROCEDURE verFuncionarios (

)
BEGIN
	select distinct * from funcionario;
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;




DELIMITER //

CREATE PROCEDURE InsertarFuncionario (
	in IDFuncionarioP char(11),
	in puestoP char(9),
	in nombreP varchar(50),
	in apellido1P varchar(50),
	in apellido2P varchar(50),
	in NumeroTelefonoP char(9)
)
BEGIN
    INSERT INTO Funcionario (IDFuncionario,
puesto ,
nombre ,
apellidol ,
apellido2 ,
NumeroTelefono)
    VALUES (IDFuncionarioP,
puestoP ,
nombreP ,
apellido1P ,
apellido2P ,
NumeroTelefonoP);
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;


DELIMITER //

CREATE PROCEDURE ActualizarFuncionario (
	in IDFuncionarioP char(11),
	in puestoP char(9),
	in nombreP varchar(50),
	in apellido1P varchar(50),
	in apellido2P varchar(50),
	in NumeroTelefonoP char(9)
)
BEGIN
    IF EXISTS (SELECT 1 FROM funcionario WHERE IDFuncionario = IDFuncionarioP) THEN
        UPDATE funcionario 
        SET IDFuncionario = IDFuncionarioP,
			puesto = puestoP ,
			nombre = nombreP ,
			apellidol = apellido1P ,
			apellido2 = apellido2P ,
			NumeroTelefono = NumeroTelefonoP   
        WHERE IDFuncionario = IDFuncionarioP;
    END IF;
END //

DELIMITER ;


DELIMITER //

CREATE PROCEDURE EliminarFuncionario (
    IN IDFuncionarioP CHAR(9)
)
BEGIN
    IF EXISTS (SELECT 1 from funcionario WHERE IDFuncionario = IDFuncionarioP) then
        DELETE FROM funcionario WHERE IDFuncionario = IDFuncionarioP;
    END IF;
END //

DELIMITER ;


-- ////////////////////////////////////////////FUNCIONES DE Ciudad////////////////////////////////////////////
DELIMITER //

CREATE PROCEDURE verCiudades (

)
BEGIN
	select distinct * from ciudad;
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;

DELIMITER //

CREATE PROCEDURE InsertarCiudad (
    IN IDCiudadP CHAR(9),
    IN nombreP varchar(50)
)
BEGIN
    INSERT INTO Ciudad (IDCiudad, nombre)
    VALUES (IDCiudadP, nombreP);
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;


DELIMITER //

CREATE PROCEDURE InsertarCiudad (
    IN IDCiudadP CHAR(9),
    IN nombreP varchar(50)
)
BEGIN
    INSERT INTO Ciudad (IDCiudad, nombre)
    VALUES (IDCiudadP, nombreP);
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;


Delimiter // 

CREATE PROCEDURE ActualizarCiudad (
    IN IDCiudadP CHAR(9),
    IN nombreP varchar(50)
)
BEGIN
    IF EXISTS (SELECT 1 FROM Ciudad WHERE IDCiudad = IDCiudadP) THEN
        UPDATE Ciudad 
        SET IDCiudad = IDCiudadP,
        	nombre = nombreP
        WHERE IDCiudad = IDCiudadP;
    END IF;
END //

DELIMITER ;
);

DELIMITER //

CREATE PROCEDURE EliminarCiudad (
    IN IDCiudadP CHAR(9)
)
BEGIN
    IF EXISTS (SELECT 1 from ciudad WHERE IDCiudad = IDCiudadP) then
        UPDATE gimnasio SET IDCiudad = null WHERE IDCiudad = IDCiudadP;
        DELETE FROM ciudad WHERE IDCiudad = IDCiudadP;
    END IF;
END //

DELIMITER ;

-- ////////////////////////////////////////////FUNCIONES DE Gimnasio////////////////////////////////////////////

DELIMITER //

CREATE PROCEDURE verGimnasios (
 
)
BEGIN
	select distinct * from gimnasio;
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;

DELIMITER //

CREATE PROCEDURE InsertarGimnasio (
	in IDGimnasioP char(9),
	in IDCiudadP char(9),
	in nombreP varchar(50),	
	in direccionExactaP varchar(200),
	in NumeroTelefonoP char(9)
)
BEGIN
    INSERT INTO gimnasio (IDGimnasio, IDCiudad, nombre, direccionExacta, NumeroTelefono)
    VALUES (IDGimnasioP, IDCiudadP, nombreP, direccionExactaP, NumeroTelefonoP);
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;


Delimiter // 

CREATE PROCEDURE ActualizarGimnasio (
	in IDGimnasioP char(9),
	in IDCiudadP char(9),
	in nombreP varchar(50),	
	in direccionExactaP varchar(200),
	in NumeroTelefonoP char(9)
)
BEGIN
    IF EXISTS (SELECT 1 FROM gimnasio WHERE IDGimnasio = IDGimnasioP) THEN
        UPDATE gimnasio  
        SET IDGimnasio = IDGimnasioP,
        	IDCiudad = IDCiudadP,
        	nombre = nombreP,
        	direccionExacta = direccionExactaP,
        	NumeroTelefono = NumeroTelefonoP
        WHERE IDGimnasio = IDGimnasioP;
    END IF;
END //

DELIMITER ;


DELIMITER //

CREATE PROCEDURE EliminarGimnasio(
    IN IDGimnasioP CHAR(9)
)
BEGIN
    IF EXISTS (SELECT 1 from gimnasio WHERE IDGimnasio = IDGimnasioP) then
        DELETE FROM gimnasio WHERE IDGimnasio = IDGimnasioP;
    END IF;
END //

DELIMITER ;

-- ////////////////////////////////////////////FUNCIONES DE Trabaja////////////////////////////////////////////
DELIMITER //

CREATE PROCEDURE verTrabajos (

)
BEGIN
	select distinct * from trabaja;
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;


DELIMITER //

CREATE PROCEDURE InsertarTrabaja (
	in IDGimnasioP char(9),
	in IDFuncionarioP char(11)
)
BEGIN
    INSERT INTO Trabaja (IDGimnasio, IDFuncionario)
    VALUES (IDGimnasioP,IDFuncionarioP);
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;


Delimiter // 

CREATE PROCEDURE ActualizarTrabaja (
	in IDGimnasioP char(9),
	in IDFuncionarioP char(11)
)
BEGIN
    IF EXISTS (SELECT 1 FROM trabaja WHERE IDGimnasio = IDGimnasioP and IDFuncionario = IDFuncionarioP) THEN
        UPDATE trabaja 
        SET IDGimnasio = IDGimnasioP
        WHERE IDGimnasio = IDGimnasioP and IDFuncionario = IDFuncionarioP;
    END IF;
END //
DELIMITER ;


DELIMITER //

CREATE PROCEDURE EliminarTrabaja(
    IN IDFuncionarioP CHAR(9),
    in IDGimnasioP char(11)
)
BEGIN
    IF EXISTS (SELECT 1 from Trabaja WHERE IDGimnasio = IDGimnasioP and IDFuncionario = IDFuncionarioP) then
        DELETE FROM Trabaja WHERE IDGimnasio = IDGimnasioP and IDFuncionario = IDFuncionarioP;
    END IF;
END //

DELIMITER ;


-- ////////////////////////////////////////////FUNCIONES DE Equipo////////////////////////////////////////////

DELIMITER //

CREATE PROCEDURE verEquipos (

)
BEGIN
	select distinct * from equipo;
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;

DELIMITER //

CREATE PROCEDURE InsertarEquipo (
	in CodigoEquipoP char(9),
	in CodigoGimnasioP char(9),
	in nombreP varchar(50),
	in estadoP char(3),
	in fechaAdquisicionP date
)
BEGIN
    INSERT INTO equipo (CodigoEquipo, CodigoGimnasio, nombre, estado, fechaAdquisicion)
    VALUES (CodigoEquipoP, CodigoGimnasioP, nombreP, estadoP, fechaAdquisicionP);
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;


Delimiter // 

CREATE PROCEDURE ActualizarEquipo (
	in CodigoEquipoP char(9),
	in CodigoGimnasioP char(9),
	in nombreP varchar(50),
	in estadoP char(3),
	in fechaAdquisicionP date
)
BEGIN
    IF EXISTS (SELECT 1 FROM Equipo WHERE CodigoEquipo = CodigoEquipoP) THEN
        UPDATE equipo  
        SET CodigoEquipo = CodigoEquipoP,
        	CodigoGimnasio = CodigoGimnasioP,
        	nombre = nombreP,
        	estado = estadoP,
        	fechaAdquisicion = fechaAdquisicionP
        WHERE CodigoEquipo = CodigoEquipoP;
    END IF;
END //
DELIMITER ;


DELIMITER //

CREATE PROCEDURE EliminarEquipo(
	in CodigoEquipoP char(9)
)
BEGIN
    IF EXISTS (SELECT 1 from equipo WHERE CodigoEquipo = CodigoEquipoP ) then
        DELETE FROM equipo WHERE CodigoEquipo = CodigoEquipoP;
    END IF;
END //

DELIMITER ;


-- ////////////////////////////////////////////FUNCIONES DE Trabaja////////////////////////////////////////////

DELIMITER //

CREATE PROCEDURE verProductos (

)
BEGIN
	select distinct * from producto;
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;

DELIMITER //

CREATE PROCEDURE InsertarProducto (
	in IDProductoP char(9),
	in nombreP varchar(50),
	in descripcionP varchar(200),
	in costoP decimal(9,2)
)
BEGIN
    INSERT INTO producto (IDProducto, nombre, descripcion, costo)
    VALUES (IDProductoP, nombreP, descripcionP, costoP);
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;


DELIMITER //

CREATE PROCEDURE ActualizarProducto (
	in IDProductoP char(9),
	in nombreP varchar(50),
	in descripcionP varchar(200),
	in costoP decimal(9,2)
)
BEGIN
    IF EXISTS (SELECT 1 FROM producto WHERE IDProducto = IDProductoP) THEN
        UPDATE producto  
        SET nombre = nombreP,
        	descripcion = descripcionP,
        	costo = costoP
        WHERE IDProducto = IDProductoP;
    END IF;
END //
DELIMITER ;


DELIMITER //

CREATE PROCEDURE EliminarProducto(
	in IDProductoP char(9)
)
BEGIN
    IF EXISTS (SELECT 1 from producto WHERE IDProducto = IDProductoP ) then
        DELETE FROM producto WHERE IDProducto = IDProductoP;
    END IF;
END //

DELIMITER ;


-- ////////////////////////////////////////////FUNCIONES DE VENTA////////////////////////////////////////////

DELIMITER //

CREATE PROCEDURE verVentas (

)
BEGIN
	select distinct * from venta;
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;

DELIMITER //

CREATE PROCEDURE InsertarVenta (
	in NumeroTransaccionP int,
	in IDClienteP char(11),
	in IDProductoP char(9),
	in fechaAdquisicionP date,
	in montoP decimal(9,2),
	in cantidadP int
)
BEGIN
    INSERT INTO venta (NumeroTransaccion, IDCliente, IDProducto, fechaAdquisicion, monto, cantidad)
    VALUES (NumeroTransaccionP, IDClienteP, IDProductoP, fechaAdquisicionP, montoP, cantidadP);
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;

DELIMITER //

CREATE PROCEDURE ActualizarVenta (
	in NumeroTransaccionP int,
	in IDClienteP char(11),
	in IDProductoP char(9),
	in fechaAdquisicionP date,
	in montoP decimal(9,2),
	in cantidadP int
)
BEGIN
    IF EXISTS (SELECT 1 FROM venta WHERE NumeroTransaccion = NumeroTransaccionP) THEN
        UPDATE venta  
        SET NumeroTransaccion = NumeroTransaccionP,
        	IDCliente = IDClienteP,
        	IDProducto = IDProductoP,
        	fechaAdquisicion = fechaAdquisicionP,
        	monto = montoP,
        	cantidad = cantidadP
        WHERE NumeroTransaccion = NumeroTransaccionP;
    END IF;
END //
DELIMITER ;


DELIMITER //

CREATE PROCEDURE EliminarVenta(
	in NumeroTransaccionP int
)
BEGIN
    IF EXISTS (SELECT 1 from venta WHERE NumeroTransaccion = NumeroTransaccionP ) then
        DELETE FROM venta WHERE NumeroTransaccion = NumeroTransaccionP;
    END IF;
END //

DELIMITER ;


-- ////////////////////////////////////////////FUNCIONES DE VENTA////////////////////////////////////////////
DELIMITER //
CREATE PROCEDURE verInscripciones (

)
BEGIN
	select distinct * from inscribirse;
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;


DELIMITER //
CREATE PROCEDURE InsertarInscribirse (
	in IDClaseP char(9),
	in IDClienteP char(11)
)
BEGIN
    INSERT INTO inscribirse (IDClase, IDCliente)
    VALUES (IDClaseP, IDClienteP);
END //
-- Reset the delimiter back to the semicolon
DELIMITER ;


DELIMITER //

CREATE PROCEDURE ActualizarInscripcion (
	in codigoInscripcionP int,
	in IDClaseP char(9),
	in IDClienteP char(11)
)
BEGIN
    IF EXISTS (SELECT 1 FROM inscribirse WHERE codigoInscripcion = codigoInscripcionP) THEN
        UPDATE inscribirse  
        SET IDCliente = IDClienteP,
        	IDClase = IDClaseP
        WHERE codigoInscripcion = codigoInscripcionP;
    END IF;
END //
DELIMITER ;


DELIMITER //

CREATE PROCEDURE EliminarInscripcion(
	in codigoInscripcionP int
)
BEGIN
    IF EXISTS (SELECT 1 from inscribirse WHERE codigoInscripcion = codigoInscripcionP ) then
        DELETE FROM inscribirse WHERE codigoInscripcion = codigoInscripcionP;
    END IF;
END //

DELIMITER ;

-- //////////////////////////////////////////////////////////////////////////////////////////
ALTER TABLE producto ADD stock int NULL;
UPDATE Producto set stock = 30;

-- INDICES NO CLÚSTER 

CREATE INDEX idx_NumeroTelefono ON cliente(NumeroTelefono);
create index idx_Producto on producto(nombre);
create index idx_VentaFecha on venta(fechaAdquisicion);
create index idx_ClaseNombre on clase(nombre);
create index idx_direccionGimnasio on gimnasio(direccionExacta);


SELECT * FROM mysql.user;

create user 'superUsuarioProyecto2'@localhost2 identified by '123';
create user 'normalUsuarioProyecto2'@localhost2 identified by '124';
create user 'respaldoUsuarioProyecto2'@localhost2 identified by '125';


GRANT ALL PRIVILEGES ON proyecto1.* TO 'superUsuarioProyecto2'@'localhost2' WITH GRANT OPTION;
GRANT SELECT, INSERT, UPDATE, DELETE ON proyecto1.* TO 'normalUsuarioProyecto2'@'localhost2';
GRANT SELECT, SHOW VIEW, LOCK TABLES ON proyecto1.* TO 'respaldoUsuarioProyecto2'@'localhost2';
FLUSH PRIVILEGES;


