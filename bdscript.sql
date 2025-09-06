-- Crear la base de datos y tabla
CREATE DATABASE IF NOT EXISTS tienda;
USE tienda;

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    valor DECIMAL(10,2) NOT NULL
);


INSERT INTO productos (id, nombre, categoria, valor) VALUES
('1', 'iPhone 15 Pro', 'Smartphones', 1350),
('2', 'Samsung Galaxy S24 Ultra', 'Smartphones', 1450),
('3', 'Google Pixel 8 Pro', 'Smartphones', 1200),
('4', 'Samsung Galaxy Tab S9', 'Tablets', 950),
('5', 'iPad Pro 12.9"', 'Tablets', 1300),
('6', 'Amazon Fire HD 10', 'Tablets', 250),
('7', 'Monitor LG UltraWide 34”', 'Monitores', 600),
('8', 'Monitor Dell UltraSharp 27”', 'Monitores', 750),
('9', 'Monitor Samsung Odyssey G9', 'Monitores', 1600),
('10', 'Teclado Mecánico Logitech G Pro', 'Accesorios', 180),
('11', 'Mouse Gamer Razer DeathAdder', 'Accesorios', 90),
('12', 'Base Dock USB-C Anker', 'Accesorios', 65),
('13', 'Auriculares Sony WH-1000XM5', 'Audio', 400),
('14', 'Bose QuietComfort 45', 'Audio', 350),
('15', 'Parlante JBL Charge 5', 'Audio', 220),
('16', 'Reloj Inteligente Apple Watch 9', 'Wearables', 520),
('17', 'Samsung Galaxy Watch 6', 'Wearables', 480),
('18', 'Xiaomi Mi Band 8', 'Wearables', 70),
('19', 'Impresora HP LaserJet Pro', 'Impresoras', 280),
('20', 'Impresora Epson EcoTank L3250', 'Impresoras', 300),
('21', 'Impresora Canon Pixma G6010', 'Impresoras', 330),
('22', 'Router WiFi 6 TP-Link AX6000', 'Redes', 320),
('23', 'Router ASUS ROG Rapture GT-AX11000', 'Redes', 500),
('24', 'Router Netgear Nighthawk AX12', 'Redes', 450),
('25', 'Cámara Canon EOS R7', 'Cámaras', 1500),
('26', 'Sony Alpha A7 IV', 'Cámaras', 2300),
('27', 'Nikon Z6 II', 'Cámaras', 2000),
('28', 'Laptop Dell XPS 15', 'Laptops', 2100),
('29', 'MacBook Pro 14” M3', 'Laptops', 2400),
('30', 'Lenovo ThinkPad X1 Carbon', 'Laptops', 1900);
