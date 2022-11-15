
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class FileSharesItem():
        capacity_gb:float
        name:str
        # non-optional-blocks
        
# wrapper list class
class FileShares(BlockList):
        items: List[FileSharesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class NetworksItem():
        modes:List[str]
        network:str
        # non-optional-blocks
        reserved_ip_range: Optional[str] = None
        
# wrapper list class
class Networks(BlockList):
        items: List[NetworksItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleFilestoreInstance(ResourceObject):
    """    
    Args:
        name (str): The resource name of the instance.
        tier (str): The service tier of the instance.
                    Possible values include: STANDARD, PREMIUM, BASIC_HDD, BASIC_SSD, HIGH_SCALE_SSD and ENTERPRISE (beta only)
    """
    _type = 'google_filestore_instance'
    
    def __init__(self,
        tf_id: str,
        name:str,
        tier:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        location: Optional[str] = None,
        project: Optional[str] = None,
        zone: Optional[str] = None,
        file_shares: Optional[FileShares]=None,
        networks: Optional[Networks]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if tier is not None:
                kwargs['tier'] = tier
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if location is not None:
                kwargs['location'] = location
            if project is not None:
                kwargs['project'] = project
            if zone is not None:
                kwargs['zone'] = zone
            if file_shares is not None:
                kwargs['file_shares'] = file_shares
            if networks is not None:
                kwargs['networks'] = networks
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
