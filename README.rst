===========
 arXiv-CLI
===========

.. image:: https://travis-ci.org/jacquerie/arxiv-cli.svg?branch=master
    :target: https://travis-ci.org/jacquerie/arxiv-cli

.. image:: https://coveralls.io/repos/github/jacquerie/arxiv-cli/badge.svg?branch=master
    :target: https://coveralls.io/github/jacquerie/arxiv-cli?branch=master


About
=====

A Python wrapper for the arXiv API.


Install
=======

.. code-block:: console

    $ pip install arxiv-cli


Usage
=====

You can use ``arXiv-CLI`` as a CLI to navigate arXiv or as a library to query
its API.

CLI
---

Currently ``arXiv-CLI`` implements three subcommands:

.. code-block:: console

    $ arxiv download [-t/--timeout seconds] IDS
    $ arxiv fetch [-t/--timeout seconds] IDS
    $ arxiv find [-i/--ids, -t/--timeout seconds] QUERY

The first two commands accept a list of arXiv ids and, respectively, download
the corresponding PDFs or display their metadata in JSON format.

The third command runs a query against arXiv and prints the metadata in JSON
format of the records that match. Adding the ``-i/--ids`` flag will return only
their ids.

Adding the ``-t/--timeout seconds`` option will sleep for that amount of
seconds between successive requests to the arXiv API.

Note that the previous commands can be chained, therefore running

.. code-block:: console

    $ arxiv download $(arxiv find --ids QUERY)

will download all papers that match ``QUERY``, while

.. code-block:: console

    $ arxiv fetch $(arxiv find --ids QUERY)

will fetch all their metadata.

API
---

The previous CLI is built on top of a Python library that can be used on its
own to query arXiv's API. For example:

.. code-block:: python

    >>> from arxiv_cli import Client
    >>> client = Client()
    >>> client.download([IDS])

will achieve the same effect as

.. code-block:: console

    $ arxiv download IDS


Author
======

Jacopo Notarstefano (`@Jaconotar`_)


License
=======

MIT


.. _`@Jaconotar`: https://twitter.com/Jaconotar
