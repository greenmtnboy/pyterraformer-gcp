
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class DestinationItem():
        # non-optional-blocks
        instance: Optional[str] = None
        ip_address: Optional[str] = None
        network: Optional[str] = None
        port: Optional[float] = None
        project_id: Optional[str] = None
        
# wrapper list class
class Destination(BlockList):
        items: List[DestinationItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SourceItem():
        # non-optional-blocks
        instance: Optional[str] = None
        ip_address: Optional[str] = None
        network: Optional[str] = None
        network_type: Optional[str] = None
        port: Optional[float] = None
        project_id: Optional[str] = None
        
# wrapper list class
class Source(BlockList):
        items: List[SourceItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleNetworkManagementConnectivityTest(ResourceObject):
    """    
    Args:
        name (str): Unique name for the connectivity test.
    """
    _type = 'google_network_management_connectivity_test'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        protocol: Optional[str] = None,
        related_projects: Optional[List[str]] = None,
        destination: Optional[Destination]=None,
        source: Optional[Source]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if protocol is not None:
                kwargs['protocol'] = protocol
            if related_projects is not None:
                kwargs['related_projects'] = related_projects
            if destination is not None:
                kwargs['destination'] = destination
            if source is not None:
                kwargs['source'] = source
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
