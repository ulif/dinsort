dinsort
=======

Sort terms according to German DIN.

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


Install
-------

The latest release of `dinsort` can be installed via pip_::

  $ pip install dinsort

The exact way depends on your operating system.


Usage
-----

`dinsort` is a Python_ library.


.. _pip: https://pip.pypa.io/en/latest/
.. _Python: https://python.org/
