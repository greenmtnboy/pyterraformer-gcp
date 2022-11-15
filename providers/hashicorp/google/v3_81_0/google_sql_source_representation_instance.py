
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleSqlSourceRepresentationInstance(ResourceObject):
    """    
    Args:
        database_version (str): The MySQL version running on your source database server. Possible values: ["MYSQL_5_5", "MYSQL_5_6", "MYSQL_5_7", "MYSQL_8_0"]
        host (str): The externally accessible IPv4 address for the source database server.
        name (str): The name of the source representation instance. Use any valid Cloud SQL instance name.
    """
    _type = 'google_sql_source_representation_instance'
    
    def __init__(self,
        tf_id: str,
        database_version:str,
        host:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        port: Optional[float] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if database_version is not None:
                kwargs['database_version'] = database_version
            if host is not None:
                kwargs['host'] = host
            if name is not None:
                kwargs['name'] = name
            if id is not None:
                kwargs['id'] = id
            if port is not None:
                kwargs['port'] = port
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
