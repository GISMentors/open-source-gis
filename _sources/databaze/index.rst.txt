.. _prostorovedatabaze:

*******************
Prostorové databáze
*******************

Prostorové databáze jsou databáze, v nichž jsou uložena i prostorové
data, resp. informace o objektech reálného světa reprezentované
prostorovými daty.  Jak bylo již zmíněno v části :ref:`geodata,
geoprvky <geodata-geoprvky>`, prostorová data obsahují formální
polohovou referenci a zpravidla bývají vyjádřené i pomocí geometrické,
topologické a popisné složky popisu.

Výhodou prostorových databází je, že spolu s prostorovými daty v nich
mohou být uložena a spravována i atributové, textové, obrazové a další
podobné informace. Už :ref:`víme <proc-gis>`, že pokud jsou prostorová
data vztažená k povrchu Země, označují se jako geografická data nebo
geodata. Prostorové databáze se pak označují jako *geografické
databáze* nebo geodatabáze. Někdy se výraz geografické databáze
používá jako synonym pojmu prostorové databáze, ale není to správné,
protože pojem prostorové databáze má obecnější význam (*Ďuračiová,
2014*).  Tabulka s prostorovým atributem (atribut obsahující
geometrické data) se nazývá *prostorová tabulka*.

.. figure:: images/db_table.png
   :class: middle
    
   Atributy prostorových dat (Zdroj: `www.indiana.edu
   <http://www.indiana.edu/~gisci/courses/g338/images/chapter2figs/fig2-2.gif>`_).

Protože prostorové tabulky reprezentují jak ​​metrické, tak i
topologické vztahy příslušných objektů, jejichž struktura je podstatně
složitější než struktura klasických vazeb v relačních databázích, mají
i jiné specifické vlastnosti než konvenční atributové
tabulky. Požadavek na jejich zajištění nedovoluje běžným způsobem
využívat klasické relační databázové systémy, které jsou pro ostatní
(neprostorové) datové typy a databáze nejpoužívanější.  Mezi specifika
patří i implementace speciálních prostorových indexů (kromě indexů i
složitější struktura prostorových dat a nutnost rozšíření standardního
dotazovacího jazyka v příslušných databázích o možnost práce s
prostorovými daty).

.. index:: Prostorový index, R-stromy, Quadtree
           
Prostorové indexy
-----------------

Indexy jsou v databázových systémech důležitou součástí. Kromě podpory
prostorových datových typů a funkcí hraje podpora speciálních
indexových struktur pro prostorové data významnou roli. Indexové
struktury pro prostorová data se liší od konvenčního způsobu vytváření
indexů (:wikipedia:`B-stromy <B-strom>`, :wikipedia:`B+ stromy
<B+ strom>`, :wikipedia-en:`lineární hašování <Linearhashing>`,
atd).  Prostorová data vyžadují použití specifických postupů
indexování, které nejsou běžně implementovány přímo v relačních
databázových systémech. Indexy obecně urychlují vyhledávání dat a také
provádění různých prostorových poptávek.  Mezi indexové struktury pro
prostorové data patří tzv. :wikipedia:`stromy <Strom_(datová
struktura)>`, například (a) :wikipedia-en:`KD-stromy <K-d_tree>`
určené k ukládání bodů (uzlů), (b) :wikipedia-en:`BSP-stromy <Binary space partitioning>` založené na rekurzivní dělení prostoru na dva poloprostory, 
(c) :wikipedia-en:`R-stromy <R-tree>` založené na dekompozici prostoru
formou minimálních ohraničujících obdélníků, přičemž jednotlivé
obdélníky se mohou i vzájemně překrývat, nebo (d)
:wikipedia-en:`kvadrátové stromy <Quadtree>` založené na postupném
dělení prostoru na kvadranty.

.. figure:: images/stromy.png
   :class: middle
    
   Indexové struktury pro prostorová data (*Ďuračiová, 2014*).

**Další témata**
    
.. toctree::
   :maxdepth: 2

   sql
   nosql
