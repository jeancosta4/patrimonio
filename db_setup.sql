CREATE DATABASE patrimonio;

USE patrimonio;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE patrimonio (
    ref INT AUTO_INCREMENT PRIMARY KEY,
    numero_patrimonio int unique,
    descricao TEXT,
    local VARCHAR(100),
    condicao VARCHAR(50)
);
