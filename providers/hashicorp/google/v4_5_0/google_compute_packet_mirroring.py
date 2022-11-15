
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class InstancesItem():
        url:str
        # non-optional-blocks
        
# wrapper list class
class Instances(BlockList):
        items: List[InstancesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SubnetworksItem():
        url:str
        # non-optional-blocks
        
# wrapper list class
class Subnetworks(BlockList):
        items: List[SubnetworksItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CollectorIlbItem():
        url:str
        # non-optional-blocks
        
# wrapper list class
class CollectorIlb(BlockList):
        items: List[CollectorIlbItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class FilterItem():
        # non-optional-blocks
        cidr_ranges: Optional[List[str]] = None
        direction: Optional[str] = None
        ip_protocols: Optional[List[str]] = None
        
# wrapper list class
class Filter(BlockList):
        items: List[FilterItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MirroredResourcesItem():
        # non-optional-blocks
        tags: Optional[List[str]] = None
        instances: Optional[Instances]=None,
        subnetworks: Optional[Subnetworks]=None,
        
# wrapper list class
class MirroredResources(BlockList):
        items: List[MirroredResourcesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class NetworkItem():
        url:str
        # non-optional-blocks
        
# wrapper list class
class Network(BlockList):
        items: List[NetworkItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputePacketMirroring(ResourceObject):
    """    
    Args:
        name (str): The name of the packet mirroring rule
    """
    _type = 'google_compute_packet_mirroring'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        priority: Optional[float] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        instances: Optional[Instances]=None,
        subnetworks: Optional[Subnetworks]=None,
        collector_ilb: Optional[CollectorIlb]=None,
        filter: Optional[Filter]=None,
        mirrored_resources: Optional[MirroredResources]=None,
        network: Optional[Network]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if priority is not None:
                kwargs['priority'] = priority
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if instances is not None:
                kwargs['instances'] = instances
            if subnetworks is not None:
                kwargs['subnetworks'] = subnetworks
            if collector_ilb is not None:
                kwargs['collector_ilb'] = collector_ilb
            if filter is not None:
                kwargs['filter'] = filter
            if mirrored_resources is not None:
                kwargs['mirrored_resources'] = mirrored_resources
            if network is not None:
                kwargs['network'] = network
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
