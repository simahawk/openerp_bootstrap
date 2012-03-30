Introduction
============

Tired of copy&paste and find&replace for creating new OpenERP modules?

This module adds Paster templates for bootstrapping your modules.

Install
=======

No release available yet so you must install it 'manually'.

Clone this repo, cd into it and launch::

    python setup.py install


Usage
=====

List templates::

    paster create --list-templates

You should see "openerp_newmodule" among the other templates.

To create your module run::

    paster create -t openerp_newmodule

and follow the instrunctions step by step.
