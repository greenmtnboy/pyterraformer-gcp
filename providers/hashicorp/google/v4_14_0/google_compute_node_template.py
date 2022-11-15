
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class NodeTypeFlexibilityItem():
        # non-optional-blocks
        cpus: Optional[str] = None
        memory: Optional[str] = None
        
# wrapper list class
class NodeTypeFlexibility(BlockList):
        items: List[NodeTypeFlexibilityItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ServerBindingItem():
        type:str
        # non-optional-blocks
        
# wrapper list class
class ServerBinding(BlockList):
        items: List[ServerBindingItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleComputeNodeTemplate(ResourceObject):
    """    
    Args:
    """
    _type = 'google_compute_node_template'
    
    def __init__(self,
        tf_id: str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        cpu_overcommit_type: Optional[str] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        node_affinity_labels: Optional[Dict[str, str]] = None,
        node_type: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        node_type_flexibility: Optional[NodeTypeFlexibility]=None,
        server_binding: Optional[ServerBinding]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if cpu_overcommit_type is not None:
                kwargs['cpu_overcommit_type'] = cpu_overcommit_type
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if name is not None:
                kwargs['name'] = name
            if node_affinity_labels is not None:
                kwargs['node_affinity_labels'] = node_affinity_labels
            if node_type is not None:
                kwargs['node_type'] = node_type
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if node_type_flexibility is not None:
                kwargs['node_type_flexibility'] = node_type_flexibility
            if server_binding is not None:
                kwargs['server_binding'] = server_binding
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
