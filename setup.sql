DROP TABLE IF EXISTS products;

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    price REAL NOT NULL
);

INSERT INTO products (name, description, price) VALUES
('Laptop', 'Gaming laptop', 1200),
('Smartphone', 'Android phone', 500),
('Headphones', 'Noise-cancelling', 150),
('Keyboard', 'Mechanical keyboard', 80);
