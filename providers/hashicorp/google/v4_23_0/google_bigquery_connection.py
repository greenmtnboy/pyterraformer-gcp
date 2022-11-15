
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
class AccessRoleItem():
        iam_role_id:str
        # non-optional-blocks
        
# wrapper list class
class AccessRole(BlockList):
        items: List[AccessRoleItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AwsItem():
        # non-optional-blocks
        access_role: Optional[AccessRole]=None,
        
# wrapper list class
class Aws(BlockList):
        items: List[AwsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AzureItem():
        customer_tenant_id:str
        # non-optional-blocks
        
# wrapper list class
class Azure(BlockList):
        items: List[AzureItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CloudResourceItem():
        # non-optional-blocks
        
# wrapper list class
class CloudResource(BlockList):
        items: List[CloudResourceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CloudSpannerItem():
        database:str
        # non-optional-blocks
        use_parallelism: Optional[bool] = None
        
# wrapper list class
class CloudSpanner(BlockList):
        items: List[CloudSpannerItem]




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
        access_role: Optional[AccessRole]=None,
        aws: Optional[Aws]=None,
        azure: Optional[Azure]=None,
        cloud_resource: Optional[CloudResource]=None,
        cloud_spanner: Optional[CloudSpanner]=None,
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
            if access_role is not None:
                kwargs['access_role'] = access_role
            if aws is not None:
                kwargs['aws'] = aws
            if azure is not None:
                kwargs['azure'] = azure
            if cloud_resource is not None:
                kwargs['cloud_resource'] = cloud_resource
            if cloud_spanner is not None:
                kwargs['cloud_spanner'] = cloud_spanner
            if cloud_sql is not None:
                kwargs['cloud_sql'] = cloud_sql
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
