
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class CredentialItem():
        password:str
        username:str
        # non-optional-blocks
        
# wrapper list class
class Credential(BlockList):
        items: List[CredentialItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CloudResourceItem():
        # non-optional-blocks
        
# wrapper list class
class CloudResource(BlockList):
        items: List[CloudResourceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CloudSqlItem():
        database:str
        instance_id:str
        type:str
        # non-optional-blocks
        credential: Optional[Credential]=None,
        
# wrapper list class
class CloudSql(BlockList):
        items: List[CloudSqlItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleBigqueryConnection(ResourceObject):
    """    
    Args:
    """
    _type = 'google_bigquery_connection'
    
    def __init__(self,
        tf_id: str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        connection_id: Optional[str] = None,
        description: Optional[str] = None,
        friendly_name: Optional[str] = None,
        id: Optional[str] = None,
        location: Optional[str] = None,
        project: Optional[str] = None,
        credential: Optional[Credential]=None,
        cloud_resource: Optional[CloudResource]=None,
        cloud_sql: Optional[CloudSql]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if connection_id is not None:
                kwargs['connection_id'] = connection_id
            if description is not None:
                kwargs['description'] = description
            if friendly_name is not None:
                kwargs['friendly_name'] = friendly_name
            if id is not None:
                kwargs['id'] = id
            if location is not None:
                kwargs['location'] = location
            if project is not None:
                kwargs['project'] = project
            if credential is not None:
                kwargs['credential'] = credential
            if cloud_resource is not None:
                kwargs['cloud_resource'] = cloud_resource
            if cloud_sql is not None:
                kwargs['cloud_sql'] = cloud_sql
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
