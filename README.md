bevigil-cli
=================

This package provides a unified command line interface and python library for using BeVigil OSINT API.

Getting Started
---------------

Installation
------------

The safest way to install the BeVigil OSINT CLI is to use [pip](https://pip.pypa.io/en/stable/):

```bash
   $ pip3 install bevigil-cli
```

If you already have the bevigil-cli package installed and want to upgrade to the
latest version, you can run:

```bash
   $ pip3 install --upgrade bevigil-cli
```

This will install the bevigil-cli package as well as all dependencies.


Usage
------------

Initialization
------------

Before using the bevigil-cli to extract assets, you need to configure your api key.
You can do this using the ``init`` command:

```bash
   $ bevigil-cli init --api-key <API_KEY>
```

To get an API key, you can register at [BeVigil's website](https://bevigil.com/osint-api)


Enumeration
------------

Once the API key is configured, you can request BeVigil's OSINT API for different types of assets. The ``enum`` command consists of subcommands to enumerate different assets collected by BeVigil OSINT API. Following are all the supported subcommands under ``enum`` group including their options.

```

```
