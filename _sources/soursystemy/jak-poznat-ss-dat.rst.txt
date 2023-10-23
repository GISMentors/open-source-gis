Jak poznat v jakém souřadnicovém systému jsou data
==================================================

Pokud není souřadnicový systém uveden v `metadatech
<https://cs.wikipedia.org/wiki/Metadata>`_ datové sady, můžeme se
pokusit uhodnout souřadnicová systém čistě z hodnot souřadnic.
Omezíme se na Českou republiku, lze to ale vztáhnout na celý svět:

:doc:`mercatorovo-zobrazeni` - :epsg:`3857`

   kladné souřadnice s hodnotami :math:`x` mezi :math:`129 295` až
   :math:`1 817 312` a osy :math:`y` :math:`6 185 018` až :math:`6 709 371`

:doc:`wgs84` - :epsg:`4326`
      
  kladná čísla nabývající hodnot :math:`11` až :math:`20` ve směru
  osy :math:`x` a :math:`47` až :math:`52` ve směru osy :math:`y`

:doc:`sjtsk` - :epsg:`5514`
  
    souřadnice jsou záporné a nabývají hodnot :math:`-925 000` až
    :math:`-400 646` v ose :math:`x` a :math:`-1 444 353` až
    :math:`-920 000` v ose :math:`y`

.. figure:: ./images/map_projections.png
    :class: middle

    Řekni jaké zobrazení používáš a já ti povím, jaký jsi (zdroj:
    https://xkcd.com/977/)

.. tip:: Viz také část :doc:`../knihovny/index`.
