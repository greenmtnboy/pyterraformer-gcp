
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class SplitItem():
        allocations:Dict[str, str]
        # non-optional-blocks
        shard_by: Optional[str] = None
        
# wrapper list class
class Split(BlockList):
        items: List[SplitItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleAppEngineServiceSplitTraffic(ResourceObject):
    """    
    Args:
        service (str): The name of the service these settings apply to.
    """
    _type = 'google_app_engine_service_split_traffic'
    
    def __init__(self,
        tf_id: str,
        service:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        migrate_traffic: Optional[bool] = None,
        project: Optional[str] = None,
        split: Optional[Split]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if service is not None:
                kwargs['service'] = service
            if id is not None:
                kwargs['id'] = id
            if migrate_traffic is not None:
                kwargs['migrate_traffic'] = migrate_traffic
            if project is not None:
                kwargs['project'] = project
            if split is not None:
                kwargs['split'] = split
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
