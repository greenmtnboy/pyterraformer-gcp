
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class BigqueryOptionsItem():
        use_partitioned_tables:bool
        # non-optional-blocks
        
# wrapper list class
class BigqueryOptions(BlockList):
        items: List[BigqueryOptionsItem]




class GoogleLoggingOrganizationSink(ResourceObject):
    """    
    Args:
        destination (str): 
        name (str): 
        org_id (str): 
    """
    _type = 'google_logging_organization_sink'
    
    def __init__(self,
        tf_id: str,
        destination:str,
        name:str,
        org_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        filter: Optional[str] = None,
        id: Optional[str] = None,
        include_children: Optional[bool] = None,
        bigquery_options: Optional[BigqueryOptions]=None,
        ):
            kwargs = {}
            if destination is not None:
                kwargs['destination'] = destination
            if name is not None:
                kwargs['name'] = name
            if org_id is not None:
                kwargs['org_id'] = org_id
            if filter is not None:
                kwargs['filter'] = filter
            if id is not None:
                kwargs['id'] = id
            if include_children is not None:
                kwargs['include_children'] = include_children
            if bigquery_options is not None:
                kwargs['bigquery_options'] = bigquery_options
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
