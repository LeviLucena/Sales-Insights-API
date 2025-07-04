DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    category TEXT,
    price REAL
);

CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    customer_id INTEGER,
    quantity INTEGER NOT NULL,
    total_amount REAL NOT NULL,
    sale_date TEXT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

-- Inserir produtos
INSERT INTO products (sku, name, category, price) VALUES ('SKU001', 'Product A', 'Category 1', 10.99);
INSERT INTO products (sku, name, category, price) VALUES ('SKU002', 'Product B', 'Category 1', 20.50);
INSERT INTO products (sku, name, category, price) VALUES ('SKU003', 'Product C', 'Category 2', 15.75);
INSERT INTO products (sku, name, category, price) VALUES ('SKU004', 'Product D', 'Category 3', 30.00);
INSERT INTO products (sku, name, category, price) VALUES ('SKU005', 'Product E', 'Category 4', 25.00);

-- Inserir clientes
INSERT INTO customers (name, email) VALUES ('John Doe', 'john@example.com');
INSERT INTO customers (name, email) VALUES ('Jane Smith', 'jane@example.com');
INSERT INTO customers (name, email) VALUES ('Bob Johnson', 'bob@example.com');
INSERT INTO customers (name, email) VALUES ('Alice Brown', 'alice@example.com');
INSERT INTO customers (name, email) VALUES ('Charlie Davis', 'charlie@example.com');

-- Inserir vendas
INSERT INTO sales (product_id, customer_id, quantity, total_amount, sale_date) VALUES (1, 1, 2, 21.98, '2025-06-01');
INSERT INTO sales (product_id, customer_id, quantity, total_amount, sale_date) VALUES (2, 2, 1, 20.50, '2025-06-02');
INSERT INTO sales (product_id, customer_id, quantity, total_amount, sale_date) VALUES (3, 3, 5, 78.75, '2025-06-03');
INSERT INTO sales (product_id, customer_id, quantity, total_amount, sale_date) VALUES (4, 4, 3, 90.00, '2025-06-04');
INSERT INTO sales (product_id, customer_id, quantity, total_amount, sale_date) VALUES (5, 5, 4, 100.00, '2025-06-05');
