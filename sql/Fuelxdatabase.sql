DROP TABLE IF EXISTS user_credentials CASCADE;
DROP TABLE IF EXISTS client_information CASCADE;
DROP TABLE IF EXISTS fuel_quote CASCADE;

CREATE TABLE user_credentials (
    id int NOT NULL,
    email varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE client_information (
    id int NOT NULL,
    f_name varchar(255) NOT NULL,
    l_name varchar(255) NOT NULL,
    street_num int,
    street_name varchar NOT NULL,
    street_num2 int,
    street_name2 varchar,
    city varchar(50),
    state char(2) NOT NULL ,
    zip int NOT NULL,
    FOREIGN KEY (id) REFERENCES user_credentials(id)
);

CREATE TABLE fuel_quote (
    id int NOT NULL,
    date timestamptz NOT NULL,
    street_num int,
    street_name varchar,
    city varchar(50),
    state char(2),
    zip int NOT NULL,
    FOREIGN KEY (id) REFERENCES user_credentials(id)
);
