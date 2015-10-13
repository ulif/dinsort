# -*- coding: utf-8 -*-
#
#  dinsort -- Sort terms according to German DIN
#
#  Copyright (C) 2015  Uli Fouquet
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import unicode_literals
import unicodedata


#: The lexicographic variant
VARIANT1 = 'variant1'

#: The namelist variant.
VARIANT2 = 'variant2'


def normalize(text, variant=VARIANT1, case_sensitive=False):
    """Create a normalized version of `text`.

    With `variant` set to ``VARIANT1`` (default), german umlauts are
    transformed to plain chars: ``ä`` -> ``a``, ``ö`` -> ``o``, ...::

      >>> print(normalize("mäßig"))
      massig

    With `variant` set to ``VARIANT2``, german umlauts are transformed
    ``ä`` -> ``ae``, etc.::

      >>> print(normalize("mäßig", variant=VARIANT2))
      maessig

    All words are turned to lower-case.::

      >>> print(normalize("Maße"))
      masse

    except if `case_sensitive` is set to `True`::

      >>> print(normalize("Maße", case_sensitive=True))
      Masse

    Other chars with diacritics will be returned with the diacritics
    stripped off::

      >>> print(normalize("Česká"))
      ceska


    """
    text = text.replace("ß", "ss")
    if not case_sensitive:
        text = text.lower()
    if variant == VARIANT2:
        for char, repl in (
                ('ä', 'ae'), ('ö', 'oe'), ('ü', 'ue'),
                ('Ä', 'AE'), ('Ö', 'OE'), ('Ü', 'UE')):
            text = text.replace(char, repl)
    text = unicodedata.normalize("NFKD", text).encode("ASCII", "ignore")
    return text.decode()


def sort_func(variant=VARIANT1):
    return lambda x: normalize(x, variant=variant)
