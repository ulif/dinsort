dinsort
*******

Sort terms according to German DIN 5007.

|bdg-build|  | `sources <https://github.com/ulif/dinsort>`_ | `issues <https://github.com/ulif/dinsort/issues>`_

.. |bdg-build| image:: https://travis-ci.org/ulif/dinsort.png?branch=master
    :target: https://travis-ci.org/ulif/dinsort
    :alt: Build Status


Little Python library to support sorting of terms according to DIN
(German Standards Institute) standard 5007.

This standard describes how to sort german terms alphabtically. It
provides two variants:

* Variant 1:

   - ``'ä'`` equals ``'a'``
   - ``'ß'`` equals ``'ss'``
   - ...

* Variant 2:

   - ``'ä'`` equals ``'ae'``
   - ``'ß'`` equals ``'ss'``
   - ...

In both variants other diacritics are removed. So ``'é'`` and ``'ç'``
become ``'e'`` and ``'c'`` respecively.


Usage
=====

`dinsort` is a Python_ library.


Normalizing Terms
-----------------

Main function is `dinsort.normalize`. It generates a normalized form
of any string term given::

   >>> from dinsort import normalize
   >>> normalize("Löblich")
   'loblich'

Variants are defined as constants::

   >>> from dinsort import VARIANT1, VARIANT2
   >>> normalize("Müßig", variant=VARIANT1)
   'mussig'

   >>> normalize("Müßig", variant=VARIANT2)
   'muessig'

Terms are normalized to lower-case by default. You can request
case-sensitiveness::

   >>> normalize("Maße", case_sensitive=True)
   'Masse'


Sorting
-------

Normalized terms can easily be used for sorting lists of terms::

   >>> sorted(["fas", "fair", "fär"], key=lambda x: normalize(x))
   ['fair', 'fär', 'fas']

We provide a shortcut to avoid (sometimes not easy to read) `lambda`
statements with `normalize` in your code. Use `sort_func` for that::

   >>> from dinsort import sort_func
   >>> sorted(["fas", "fair", "fär"], key=sort_func())
   ['fair', 'fär', 'fas']

The `sort_func` accepts the keywords of `normalize`::

   >>> sorted(["Muße", "muß"], key=sort_func())
   ['muß', 'Muße']

   >>> sorted(["Muße", "muß"], key=sort_func(case_sensitive=True))
   ['Muße', 'muß']

   >>> sorted(["far", "fähre"], key=sort_func())
   ['fähre', 'far']

   >>> sorted(["far", "färe", "fast"], key=sort_func())
   ['far', 'färe', 'fast']

   >>> sorted(["far", "färe", "fast"], key=sort_func(variant=VARIANT2))
   ['färe', 'far', 'fast']


Install
=======

User Install
------------

The latest release of `dinsort` can be installed via pip_::

  $ pip install dinsort

The exact way depends on your operating system.


Developer Install
-----------------

Developers clone the sources from github::

  $ git clone https://github.com/ulif/dinsort.git

Create a virtual env (Python versions >= 2.6 supported)::

  $ cd dinsort
  $ virtualenv py27
  $ source py27/bin/activate

and install dependencies::

  (py27) python setup py dev

You can run tests with `py.test`::

  (py27) py.test

or with `tox`::

  (py27) pip install tox
  (py27) tox



.. _pip: https://pip.pypa.io/en/latest/
.. _Python: https://python.org/
