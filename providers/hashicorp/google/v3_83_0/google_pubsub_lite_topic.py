
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class CapacityItem():
        publish_mib_per_sec:float
        subscribe_mib_per_sec:float
        # non-optional-blocks
        
# wrapper list class
class Capacity(BlockList):
        items: List[CapacityItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PartitionConfigItem():
        count:float
        # non-optional-blocks
        capacity: Optional[Capacity]=None,
        
# wrapper list class
class PartitionConfig(BlockList):
        items: List[PartitionConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RetentionConfigItem():
        per_partition_bytes:str
        # non-optional-blocks
        period: Optional[str] = None
        
# wrapper list class
class RetentionConfig(BlockList):
        items: List[RetentionConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GooglePubsubLiteTopic(ResourceObject):
    """    
    Args:
        name (str): Name of the topic.
    """
    _type = 'google_pubsub_lite_topic'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        zone: Optional[str] = None,
        capacity: Optional[Capacity]=None,
        partition_config: Optional[PartitionConfig]=None,
        retention_config: Optional[RetentionConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if zone is not None:
                kwargs['zone'] = zone
            if capacity is not None:
                kwargs['capacity'] = capacity
            if partition_config is not None:
                kwargs['partition_config'] = partition_config
            if retention_config is not None:
                kwargs['retention_config'] = retention_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
