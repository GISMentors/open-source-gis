Instalace
---------

Ze zdrojových kódů
""""""""""""""""""

Pycsw obsahuje rychlý návod na instalaci, který lze  zvládnout za pár minut.::

        # Nastavit virtualní prostředí pro Python
        $ virtualenv pycsw && cd pycsw && . bin/activate
        
        # Stánout zdrojové kódy, nainstalovat závislosti
        $ git clone https://github.com/geopython/pycsw.git && cd pycsw
        $ pip install -e . && pip install -r requirements-standalone.txt
        
        # Vytvoření konfiguračního souboru a jeho nastavení
        $ cp default-sample.cfg default.cfg
        $ $EDITOR default.cfg

        # nastvit cesty v 
        # - server.home
        # - repository.database
        # nastavit server.url na http://localhost:8000/
        
        # inicializovat databázi
        $ pycsw-admin.py -c setup_db -f default.cfg
        
        # Načíst metadatové záznamy ('recordy') z připravených souborů XML v
        # daném adresáři
        $ pycsw-admin.py -c load_records -f default.cfg -p /path/to/xml/
        
        # Spuštění serveru
        $ python ./pycsw/wsgi.py
        
        # Testování serveru serveru
        $ curl http://localhost:8000/?service=CSW&version=2.0.2&request=GetCapabilities

Linux z balíčků
"""""""""""""""

Pro distribuci Ubuntu existují balíčky::

    $ sudo apt-get install pycsw

Windows and PIP
"""""""""""""""

Pro Windows buď použijte instalaci ze zdrojových kódů nebo prostřednictvím
balíčkovače PIP::

    # pip install pycsw

