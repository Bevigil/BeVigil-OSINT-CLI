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
  Enumerate assets using BeVigil OSINT API

Options:
  -h, --help  Show this message and exit.

Commands:
  hosts       Request hosts present in an android package
  packages    Request packages associated associated with a domain/subdomain
  params      Request params associated with an android package
  s3          Request S3 buckets associated with a package or a keyword
  subdomains  Request subdomains associated with a domain
  urls        Request URLs associated with a domain
  wordlist    Request a wordlist for a package
```

Examples
------------

* To request a wordlist crafted from an android pacakge:
```bash

```
