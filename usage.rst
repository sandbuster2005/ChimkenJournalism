Usage
=====

#####
basic
#####

first your are supposed to create a logger amnually or trough config
then you can reach it through index like dictionnaries and call a defined level

.. code-block::

 	test = Journal()
 	test.add_log(name = "new")
	test["new"].info("this is a test ")


######
levels
######

they can be created before or after loggers , it doesn't matter ,
then it can be called like all other levels 

.. warning::
	when creating new level make sure neither name or value is already used
	or else unpredictible behavior can be seen 


.. code-block::
	
	test.add_level("Mylevel", 29)
	test["new"].Mylevel( "this is an important message" ) 


######
config
######

to add configs its recommanded to use gen_config and gen_handler

.. code-block::

	handler = gen_handler( "logs/cat_traceback.log" , "file" , 18 )
        config = gen_config( "cat" , level = 10 , loggers = [ "black" , "white" ] , handlers = handler) 
        #since no format was indicated , it will use the defaut's config one
        test.add_config( config )
        test["black"].Mylevel(" this is using logger generated through config ")


########
handlers
########

they are created via add_log , you can add the a config to be used, else it will use the
default one 

.. code-block::

	test.add_log( name = "mixed" , config = "cat")
	test["mixed"].warning("this cat is strange")


        