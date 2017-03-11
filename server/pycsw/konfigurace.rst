Konfigurace
-----------

Konfigurace se provádí prostřednictvím konfiguračního souboru `default.cfg`,
PyCSW se distribuuje s jeho šablonou s názvem `default-sample.cfg`. Jedná se o
textový soubor se sekcemi (viz `dokumentace <http://docs.pycsw.org/en/2.0.2/configuration.html>`_):

[server]
    Kde se konfigurují vlastnosti serveru jako takového, cesty, logování, jazyk
    atd.

[manager]
    Kde se konfigurují možné transakce, povolené IP adresy

[metadata:main]
    Základní metadata služby, zejména kontaktu

[repository]
    Konfigurace databáze na pozadí pycsw

Cestu k souboru s konfigurací můžeme nastavit přímo v souboru `csw.py`. Další
možností je nastavení proměnné prostředí `PYCSW_CONFIG` (v konfiguraci webového
serveru nebo pomocí wrapper skriptu::

    #!/bin/sh

    export PYCSW_CONFIG=/var/www/pycsw/csw-foo.cfg
    /var/www/pycsw/csw.py

Administrace
------------

Pro `administraci <http://docs.pycsw.org/en/2.0.2/administration.html>`_ 
serveru slouží skript `pycsw-admin.py`, který by měl být
dostupný jako spustitelný soubor.
