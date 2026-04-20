Usage
=====

######
Basics
######

First, you need to create a logger manually or through a config. 
You can then reach it through indexes, just like dictionnaries, and call a defined level.

.. code-block::

 	test = Journal()
 	test.add_log(name = "new")
	test["new"].info("this is a test ")


######
Levels
######

They can be created before or after loggers and can be called like all other levels.

.. warning::
	When creating new level, make sure neither the name or the value is already used
	or else unpredictable behavior can occur. 


.. code-block::
	
	test.add_level("Mylevel", 29)
	test["new"].Mylevel( "this is an important message" ) 


######
Config
######

To add configs, it is recommanded to use the :py:func:`gen_config<journalism.gen_config>` and :py:func:`gen_handler <journalism.gen_handler>`

.. code-block::

	handler = gen_handler( "logs/cat_traceback.log" , "file" , 18 )
        config = gen_config( "cat" , level = 10 , loggers = [ "black" , "white" ] , handlers = handler) 
        #since no format was indicated , it will use the defaut's config one
        test.add_config( config )
        test["black"].Mylevel(" this is using logger generated through config ")


########
Handlers
########

Handlers are created via :py:func:`add_log <journalism.Journal.add_log>`. You can define which config to use, otherwise it will use the
default one.

.. code-block::

	test.add_log( name = "mixed" , config = "cat")
	test["mixed"].warning("this cat is strange")


        
