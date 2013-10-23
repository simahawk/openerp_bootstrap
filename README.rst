Introduction
============

Tired of copy&paste and find&replace for creating new OpenERP modules?

This module adds Paste_ templates for bootstrapping your modules.

Install
=======

As simple as::

	pip install openerp_bootstrap

Issues and contribs
===================

https://github.com/simahawk/openerp_bootstrap


Usage
=====

.. warning:: Starting from version 1.0b2 the template "openerp_theme" has been renamed to "openerp_webmodule".


List templates::

    paster create --list-templates

You should see "openerp_newmodule", "openerp_webmodule" among the other templates.

To create a simple module run::

    paster create -t openerp_newmodule

to create a basic web package run::

    paster create -t openerp_webmodule

and follow the instructions step by step.


.. _Paste: http://pythonpaste.org/script/
