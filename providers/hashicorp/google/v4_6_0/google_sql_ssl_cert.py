
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




class GoogleSqlSslCert(ResourceObject):
    """    
    Args:
        common_name (str): The common name to be used in the certificate to identify the client. Constrained to [a-zA-Z.-_ ]+. Changing this forces a new resource to be created.
        instance (str): The name of the Cloud SQL instance. Changing this forces a new resource to be created.
    """
    _type = 'google_sql_ssl_cert'
    
    def __init__(self,
        tf_id: str,
        common_name:str,
        instance:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if common_name is not None:
                kwargs['common_name'] = common_name
            if instance is not None:
                kwargs['instance'] = instance
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
