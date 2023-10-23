.. index:: NoSQL
           
Prostorové NoSQL databáze
-------------------------

NoSQL poskytuje nové technologie pro správu dat, jejichž cílem je
uspokojit rostoucí objem, rychlost a množství dat.  Segment NoSQL
databází v současnosti významně roste a prospívá především v oblasti
*big data* a *real-time webu*. Popularizace NoSQL v některých lidech
vzbuzuje odpor, v jiných zase nekritické naděje. Často umožňují dotazy
i v SQL (či podobném) jazyce.

.. figure:: images/nosql.png
   :class: middle  

   Zdroj: `What is NoSQL?
   <http://i2.wp.com/jennyxiaozhang.com/wp-content/uploads/2014/08/nosql-logos.png?w=400>`_.

.. index:: CouchDB
              
CouchDB
^^^^^^^

`CouchDB <http://couchdb.apache.org/>`_ je dokumentově orientovaná
databáze, vyvíjená pod křídly :wikipedia:`Apache Software Foundation`
a nabízí některé zajímavé možnosti.  Kromě obvyklých NoSQL
vymožeností, jako například snadná replikovatelnost a vysoká rychlost
operací, ji můžeme využít, ve spojení s frameworkem CouchApp, i pro
běh webových aplikací přímo v ní samotné.  Apache CouchDB je jeden z
nových databázových systémů. Představuje hodně odlišný způsob ukládání
dat. Způsob, který není výrazně lepší nebo horší než ty, co tu už byly
– je to prostě jen jiný nástroj, jiný způsob přemýšlení o věcech.

.. figure:: images/couchdb_logo.png
   :width: 150px    

   Logo CouchDB (zdroj: `wikimedia
   <https://upload.wikimedia.org/wikipedia/en/thumb/f/f8/CouchDB.svg/964px-CouchDB.svg.png>`__).

.. tip:: Viz. online překlad kompletního průvodce CouchDB od Martina
   Malého, `Kompletní průvodce po CouchDB
   <https://www.zdrojak.cz/serialy/kompletni-pruvodce-po-couchdb/>`_.

.. index:: Cassandra
              
Cassandra
^^^^^^^^^

Návrh :wikipedia:`Apache Cassandra` se zaměřuje na snadné a spolehlivé
propojování velkého množství počítačů, které vytvoří jednu
distribuovanou vysoce výkonnou dobře horizontálně škálovatelnou
databázi. Projekt zařadil :wikipedia:`Apache Software Foundation` mezi
své top-level projekty.  Cassandra je napsána v Javě. Její principy se
neslučují s principy klasických SQL databází.

.. figure:: images/cassandra_logo.png
   :width: 150px    

   Logo Cassandra (zdroj: `wikimedia
   <https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Cassandra_logo.svg/500px-Cassandra_logo.svg.png>`__).

.. tip:: Viz. online `dokumentaci
   <http://docs.datastax.com/en/archived/cassandra/0.6/docs/>`_,
   uveřejněnou společností Riptano, která nabízí komerční podporu pro
   NoSQL databázi Cassandra nebo `seriál o NoSQL databázi Cassandra
   <http://www.linuxsoft.cz/user_page.php?user_id=16648&part=article>`_
   od Františka Bártíka v českém jazyku.

.. index:: MongoDB

MongoDB
^^^^^^^

`MongoDB <https://www.mongodb.com>`__ pracuje s daty ve formátu
:ref:`JSON <json>`. Data jsou členěna do databází a databáze dále do
collections.

.. figure:: images/mongo_logo.png
   :width: 250px    

   Logo MongoDB (zdroj: `wikimedia
   <https://en.wikipedia.org/wiki/MongoDB#/media/File:MongoDB-Logo.svg>`__).

.. tip:: Blog GISMentors: `Mongo a prostorová data
         <http://www.gismentors.cz/blog/mongo-a-prostorova-data>`__
              
