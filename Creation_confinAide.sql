CREATE DATABASE confinAide;
USE confinAide;

CREATE TABLE client(
id_client bigint NOT NULL,
password varchar(20) NOT NULL,
mail varchar(50) NOT NULL,
nom varchar(20),
tel varchar(20),
adresse varchar(20),
PRIMARY KEY(id_client));

CREATE TABLE produit(
id_produit bigint NOT NULL,
nom_produit varchar(20) NOT NULL,
type varchar(20),
PRIMARY KEY(id_produit));


CREATE TABLE commandeProduit(
id_commande_produit bigint NOT NULL,
id_produit bigint NOT NULL,
id_client bigint NOT NULL,
confirm Bool,
description varchar(200),
PRIMARY KEY(id_commande_produit),
CONSTRAINT fk_id_client FOREIGN KEY (id_client)
REFERENCES client(id_client)
ON DELETE CASCADE,
CONSTRAINT fk_id_produit FOREIGN KEY (id_produit)
REFERENCES produit(id_produit)
ON DELETE CASCADE);


INSERT INTO client(id_client,password,mail,nom,tel,adresse) VALUES (1,'mama','mama@gmail.com','Le Goff', '0789985746','Paris');
INSERT INTO client(id_client,password,mail,nom,tel,adresse) VALUES (2,'alex','alex@gmail.com','Jean', '0847564739','Lille');
INSERT INTO client(id_client,password,mail,nom,tel,adresse) VALUES (3,'jerem','jerem@gmail.com','Pierre', '0758475676','Grenoble');

INSERT INTO produit(id_produit,nom_produit,type) VALUES (1,'Pates',NULL);
INSERT INTO produit(id_produit,nom_produit,type) VALUES (2,'Eau',NULL);
INSERT INTO produit(id_produit,nom_produit,type) VALUES (3,'Grenadine',NULL);
