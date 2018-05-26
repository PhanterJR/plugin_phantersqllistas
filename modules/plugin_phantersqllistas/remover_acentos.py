#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' 
Devolve cópia de uma str substituindo os caracteres 
acentuados pelos seus equivalentes não acentuados.
    
ATENÇÃO: carateres gráficos não ASCII e não alfa-numéricos,
tais como bullets, travessões, aspas assimétricas, etc. 
são simplesmente removidos!
    
    >>> remover_acentos('[ACENTUAÇÃO] ç: áàãâä! éèêë? íì&#297;îï, óòõôö; úù&#361;ûü.')
    '[ACENTUACAO] c: aaaaa! eeee? iiiii, ooooo; uuuuu.'
    
'''

from unicodedata import normalize

def remover_acentos(txt, codif='utf-8', maiusculo=True):
    if maiusculo:
        return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore').upper()
    else:
        return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore')
    
if __name__ == '__main__':
    from doctest import testmod
    testmod()
