Definitions
==========

#####
Levels
#####

Log levels are defined from 0 to 50 and are a way to tell loggers and handlers 
which message to catch 
    
.. note::
   *levels defined by default :*
	* INFO : 10
	* DEBUG : 20
	* WARNING : 30
	* CRITICAL : 40
	* ERROR : 50

#############
Format string
#############

Format strings are strings that contain specific attributes which can be processed by
handlers' formatters and allow to format output message at will

.. note::
	List of attribute can be found here
	https://docs.python.org/3/library/logging.html#logrecord-attributes


########
Handlers
########

A handler is an object linked to loggers which can each individually process messages that are sent through 
them : checking level and formating. 
After that they output it to their configured destination, which depends on the type
of handler (e.g. from file to web, ... )

.. note::
	List of handlers type can be found here
	https://docs.python.org/3/library/logging.handlers.html

#######
Loggers
#######

Loggers allow the developers to send message that will be caught depending on 
logger configured level and then sent to configured handlers
