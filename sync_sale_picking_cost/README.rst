.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
	:target: http://www.gnu.org/licenses/agpl
	:alt: License: AGPL-3

================
Carier Follow Up
================

This module allows to follow the status of shipments. It provides a base so be used for different carriers to automatically
update the shipments status. I also creates a timesheet line when an outgoing picking is 'in preparation'.


Installation
============

To install this module, you need to:

#. Only install

NOTE. There is a soft dependency on stock_valuation_fifo_lot module, as Odoo uses a financial FIFO valuation, not a real FIFO valuation, which is solved by the stock_valuation_fifo_lot module.


Configuration
=============

To configure this module, you need to:

#. Go to the stock picking types and select an account in the field 'Preparation Timesheet Account' on those that will create a timesheet
line when the 'In preparation' field in the picking is set to True.
#. Check the 'Provides Follow Up Information' checkbox in those carriers that automatically provide shipping information. The methods have
to be developed in modules that depend on this one.
#. Activate the 'Update Shipments Status' crone if shipments status have to be checked automatically.


Usage
=====

To use this module, you need to:

#. Outgoing pickings cannot be validated unless they are 'In preparation'. Press on the 'In preparation' button to be able to validate the picking.
This action will automatically create a timesheet line related to the picking and assigned to the picking resposnsible or the current user.


ROADMAP
=======

[ Enumerate known caveats and future potential improvements.
  It is mostly intended for end-users, and can also help
  potential new contributors discovering new features to implement. ]

* ...


Bug Tracker
===========

Bugs and errors are managed in `issues of GitHub <https://github.com/sygel/REPOSITORY/issues>`_.
In case of problems, please check if your problem has already been
reported. If you are the first to discover it, help us solving it by indicating
a detailed description `here <https://github.com/sygel/REPOSITORY/issues/new>`_.

Do not contact contributors directly about support or help with technical issues.


Credits
=======

Authors
~~~~~~~

* Sygel, Odoo Community Association (OCA)


Contributors
~~~~~~~~~~~~

* Manuel Regidor <manuel.regidor@sygel.es>


Maintainer
~~~~~~~~~~

This module is maintained by Sygel.

.. image:: https://pbs.twimg.com/profile_images/702799639855157248/ujffk9GL_200x200.png
   :alt: Sygel
   :target: https://www.sygel.es

This module is part of the `Sygel/REPOSITORY <https://github.com/sygel/repository>`_.

To contribute to this module, please visit https://github.com/sygel.
