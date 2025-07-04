CREATE TABLE sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    sale_date DATE NOT NULL
);

INSERT INTO sales (product_name, quantity, sale_date) VALUES
('Produto A', 10, '2025-06-05'),
('Produto B', 5, '2025-06-07'),
('Produto A', 7, '2025-06-08'),
('Produto C', 12, '2025-06-10'),
('Produto B', 9, '2025-06-15'),
('Produto A', 20, '2025-06-20'),
('Produto D', 15, '2025-06-21');
