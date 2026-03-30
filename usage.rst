Usage
=====

#####
basic
#####

first your are supposed to create a logger amnually or trough config
then you can reach it through index like dictionnaries and call a defined level

.. code-block::

 	test = Journal()
 	test.add_log("new")
	test["new"].info("this is a test ")