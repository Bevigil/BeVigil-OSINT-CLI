bevigil-osint-cli
=================

This package provides a unified command line interface to BeVigil OSINT.

Getting Started
---------------

This README is for the BeVigil OSINT CLI version 1.

Requirements
------------

The BeVigil-osint-cli package works on Python versions:

-  3.6.x and greater
-  3.7.x and greater
-  3.8.x and greater
-  3.9.x and greater
-  3.10.x and greater

Installation
------------
Installation of the BeVigil OSINT CLI and its dependencies use a range of packaging
features provided by ``pip`` and ``setuptools``. To ensure smooth installation,
it's recommended to use:

- ``pip``: 9.0.2 or greater
- ``setuptools``: 36.2.0 or greater

The safest way to install the BeVigil OSINT CLI is to use [pip](https://pip.pypa.io/en/stable/) in a ``virtualenv``:



```bash
   $ python -m pip install bevigil-cli
```

or, if you are not installing in a ``virtualenv``, to install globally:

```bash
   $ sudo python -m pip install bevigil-cli
```

or for your user:

```bash
   $ python -m pip install --user bevigil-cli
```

If you have the bevigil-cli package installed and want to upgrade to the
latest version, you can run:

```bash
   $ python -m pip install --upgrade bevigil-cli
```

This will install the bevigil-cli package as well as all dependencies.

Configuration
------------

Before using the BeVigil OSINT CLI, you need to configure your api key.
You can do this using the ``bevigil-cli init`` command:

```bash
   $ bevigil-cli init --api-key <API_KEY>
```
