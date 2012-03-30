Introduction
============

Tired of copy&paste and find&replace for creating new OpenERP modules?

This module adds Paste_ templates for bootstrapping your modules.

Install
=======

As simple as::

	pip install openerp_pastertemplates

Issues and contribs
===================

https://github.com/simahawk/openerp_pastertemplates


Usage
=====

List templates::

    paster create --list-templates

You should see "openerp_newmodule" among the other templates.

To create your module run::

    paster create -t openerp_newmodule

and follow the instructions step by step.


.. _Paste: http://pythonpaste.org/script/
