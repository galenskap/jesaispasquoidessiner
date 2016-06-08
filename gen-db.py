#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
con = sqlite3.connect('generateur.db') # Warning: This file is created in the current directory

## OBJETS
con.execute("CREATE TABLE objets (id INTEGER PRIMARY KEY, texte char(100) NOT NULL, status bool NOT NULL)")

# singulier masc
con.execute("INSERT INTO objets (texte,status) VALUES ('un éléphant',1)")
con.execute("INSERT INTO objets (texte,status) VALUES ('ton voisin',1)")
con.execute("INSERT INTO objets (texte,status) VALUES ('Dr Who',1)")
con.execute("INSERT INTO objets (texte,status) VALUES ('un orang-outan',1)")
con.execute("INSERT INTO objets (texte,status) VALUES ('Victor Hugo',1)")
con.execute("INSERT INTO objets (texte,status) VALUES ('un chef cuisto',1)")
con.execute("INSERT INTO objets (texte,status) VALUES ('un personnage de Star Wars',1)")
con.execute("INSERT INTO objets (texte,status) VALUES ('un virus dangereux',1)")
con.execute("INSERT INTO objets (texte,status) VALUES ('le doyen de l`humanité',1)")
# singulier fem
con.execute("INSERT INTO objets (texte,status) VALUES ('la mère Michelle',1)")
con.execute("INSERT INTO objets (texte,status) VALUES ('une bucheronne canadienne',1)")
con.execute("INSERT INTO objets (texte,status) VALUES ('une ado geek',1)")
# pluriel masc
con.execute("INSERT INTO objets (texte,status) VALUES ('des pirates',1)")
con.execute("INSERT INTO objets (texte,status) VALUES ('des champignons',1)")
con.execute("INSERT INTO objets (texte,status) VALUES ('un régiment d`escargots',1)")
# pluriel fem
con.execute("INSERT INTO objets (texte,status) VALUES ('les pyramides d`Égypte',1)")
con.execute("INSERT INTO objets (texte,status) VALUES ('un bol de mignonnes petites cacahuètes',1)")


## SITUATIONS
con.execute("CREATE TABLE situations (id INTEGER PRIMARY KEY, texte char(100) NOT NULL, status bool NOT NULL)")

# neutre
con.execute("INSERT INTO situations (texte,status) VALUES ('vs un smartphone',1)")
con.execute("INSERT INTO situations (texte,status) VALUES ('un lundi matin',1)")
con.execute("INSERT INTO situations (texte,status) VALUES ('au secours d`un-e prince-sse',1)")
con.execute("INSERT INTO situations (texte,status) VALUES ('au Moyen-Âge, dans un donjon assiégé',1)")
con.execute("INSERT INTO situations (texte,status) VALUES ('au musée du Louvre',1)")
con.execute("INSERT INTO situations (texte,status) VALUES ('dans une forêt magique',1)")
con.execute("INSERT INTO situations (texte,status) VALUES ('dans une montgolfière',1)")
con.execute("INSERT INTO situations (texte,status) VALUES ('dans un asile de fous',1)")
con.execute("INSERT INTO situations (texte,status) VALUES ('apprenant à voler',1)")
con.execute("INSERT INTO situations (texte,status) VALUES ('aux sports d`hiver',1)")
con.execute("INSERT INTO situations (texte,status) VALUES ('à l`aquagym',1)")
con.execute("INSERT INTO situations (texte,status) VALUES ('au concert de Louane',1)")
con.execute("INSERT INTO situations (texte,status) VALUES (', frappé(e) d`une mort inattendue',1)")
# singulier
con.execute("INSERT INTO situations (texte,status) VALUES ('avec ses pokémons',1)")
con.execute("INSERT INTO situations (texte,status) VALUES ('qui fait du patin à glace',1)")
con.execute("INSERT INTO situations (texte,status) VALUES (', son ange gardien et son petit diabe intérieur',1)")
con.execute("INSERT INTO situations (texte,status) VALUES ('qui apprend à voler',1)")
con.execute("INSERT INTO situations (texte,status) VALUES ('qui fait une crise d`agoraphobie',1)")
# pluriel
con.execute("INSERT INTO situations (texte,status) VALUES ('qui font une manif',1)")

con.commit()
