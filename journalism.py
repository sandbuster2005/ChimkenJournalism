"""a journal module to handle complex log system """
import logging
import datetime



# conf exemple
# you always need a default config with all the field
conf = {
    "default" :
        {
        "level": 0,
        "format": "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
        "loggers": ["main" ,"sub" ],
        "handlers":
          [
            {
            "name" : "main.log",
            "type" : "file",
            "level": 0
            },
            
            {
            "name" : "warning.log",
            "type" : "file",
            "level": 30
            }         
          ]
        },
    
    "backup" :
        {
        "loggers" : ["backup"],
        "handlers":
          [
            {
            "name" : "backup.log",
            "type" : "file",
            "level" : 0
            }
          ]
        }      
       }





def gen_config(name ,level= None ,format_string = None ,loggers = None ,handlers = None ):
    """
    allows you to generate a single config
    
    :param str name: the name of the config
    :param int level: the level above which the loggers will catch the messages
    :param str format_string: allow to format what will be log in the file
    :param list loggers: the list of the names of the loggers to be created using this config
    :param list handlers: where should the catched messages be written
    :**Warning**: for individual handlers reffer to *gen_handler*
    """
    result = {}
    
    if format_string:
        result["format"] = format_string
    
    if level:
        result["level"] = level
        
    if loggers:
        result["loggers"] = loggers
        
    if handlers:
        result["handlers"] = handlers
    
    return { name : result }



def gen_handler(name , handler_type , level):
    """
    allow you to generate singular handlers
    
    :param str name: of the handler ( the name of the file if this is for a file handler )
    :param str handler_type: the type of handler ( file , console , WEB ... )
    :param int level: the level above which message should be written by the handler
    :**Warning**: currently only basic file handlers are implemented
    """
    return { "name" : name  ,"type" : handler_type ,"level" : level }



class Journal:
    """
    The main class
    
    :param config: dict containing a journal config
    """
    def __init__(self, cfg = None ):
        
        logging.getLogger().setLevel(0)
        
        self._levels = { 10 : "DEBUG" ,20 : "INFO"  ,30: "WARNING" ,40: "ERROR" ,50 : "CRITICAL" }
        self._logger = {}
        self._handlers = []
        self._configs = cfg
        print(self._configs)
        
        self.add_log("_JOURNAL_")
        
        for config in self._configs.keys():
            if "loggers" in self._configs[config].keys():
                for logger in self._configs[config]["loggers"]:
                    self.add_log( logger , config )
        
        
        
        
        
    def __getitem__(self, index):
        
        if index in self._logger.keys():
            return self._logger[index]
        
        else:
            self.add_log( index )
            self._logger["_JOURNAL_"].warning(f"{index} log do not exist and should be manually created before next time")
            
            return self._logger[index]
        
        
        
            
    
    def __repr__(self):
        
        return self.loggers()
    
    
    
    
    
    def _create_file_handler( self, filehandler , template ):
        
        handler = logging.FileHandler( filehandler["name"] )
        handler.setLevel( filehandler["level"] )
        handler.setFormatter ( template ) 
        self._handlers.append( handler )
        
        return handler
    
    
    
    
    
    def _create_log_formatter(self , config = "defaut" ):
        
        if "format" in self._configs[config].keys():
            return logging.Formatter(fmt = self._configs[config]["format"] )
        
        else:
            return logging.Formatter(fmt = self._configs["default"]["format"] )
        
        
        
        
    
    def add_log(self, name , config= "default" ):
        """
        allow you to create a new logger instance
        
        
        :param str name: the name of the new logger you want to create
        :param str config: the name of a config you loaded before
        """
        self._logger[ name ] = logging.getLogger( name )
        
    
        if "level" in self._configs[config].keys():
            self._logger[ name ].setLevel( self._configs[config]["level"] )
            
        else:
            self._logger[ name ].setLevel( self._configs["default"]["level"] )
        
        
        template = self._create_log_formatter( config )  
        
        if "handlers" in self._configs[config].keys() :
            handlers = self._configs[config]["handlers"]
        
        else:
            handlers = self._configs["default"]["handlers"]
       
        for handler in handlers:
            if handler["type"] == "file":
                 self._logger[ name ].addHandler( self._create_file_handler( handler , template ) )
        
        
        self._logger[ name ].propagate = False
    
    
    
    
    
    def add_level(self, level_name, level_num, erase = False ):
        """
        allow you to add a new level to loggers ,
        each level need a name and a value between 0 and 50
        
        :param str level_name: the name you want to give it
        :param int level_num: the level you want to give it
        :param bool erase: allow to replace level if value already exist
        
        """
        if level_num in self.levels_values() and not erase:
            raise Exception("log level already exist")
        
        if level_name in self.levels_names():
            raise Exception("log name already exist")
        
        
        method_name = level_name.lower()
        level_name = level_name.upper()

        def logForLevel(self, message, *args, **kwargs):
            if self.isEnabledFor(level_num):
                self._log(level_num, message, args, **kwargs)

        def logToRoot(message, *args, **kwargs):
            logging.log(level_num, message, *args, **kwargs)
        
        self._levels[level_num] = level_name
        
        logging.addLevelName(level_num, level_name)

        setattr(logging, level_name, level_num)
        setattr(logging.getLoggerClass(), method_name, logForLevel)
        setattr(logging, method_name, logToRoot)
        
        
        
        
    def add_config(self,config):
        """
        allow you to load new config into the journal
        """
        for old in self._configs.keys():
            for new in config.keys():
                if old == new:
                    raise Exception("{new} config already exist")
          
        self._configs = { **self._configs , **config }
        
        for cfg in configs.keys():
            if "loggers" in config[cfg].keys():
                for logger in configs[cfg]["loggers"]:
                    self.add_log( logger , cfg )
    
    
    
    
    
    def load_logs(self, config):
        pass
                
        
        
    
    
    
    
    
    def loggers(self):
        """

        return the list of configured loggers
        """
        return  "loggers : " + " ,".join( [ x for x in self._logger.keys() ] )
    
    
    
    
    
    def levels(self):
        """
        returned the list of configured levels
        """
        return "\n".join( [ f"{ self._levels[x] } : {x} " for x in sorted(self._levels) ] ) 
    
    
    
    
    
    def handlers(self):
        """
        return the list of configured handlers
        """    
        return self._handlers
    
    
    
    
    
    def levels_names(self):
        return [ self._levels[x] for x in self._levels.keys() ]
    
    
    
    
    
    def levels_values(self):
        return self._levels.keys()
    
if __name__ == "__main__":   
    journal = Journal( conf )
    journal.add_level("test",15)
    journal["test"].test("this is a teste")
    journal.add_log("screen" ,"backup")
    journal["screen"].test("its working")
    journal["main"].warning("this is normal")
    print(journal.loggers() )
    print( journal.levels() )
    print( journal._logger["screen"].handlers)
    print(journal)
