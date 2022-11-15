
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass




# this block can contain multiple items, items in a list are required
@dataclass 
class PubsubConfigsItem():
        message_format:str
        topic:str
        # non-optional-blocks
        service_account_email: Optional[str] = None
        
# wrapper list class
class PubsubConfigs(BlockSet):
        items: Set[PubsubConfigsItem]



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleSourcerepoRepository(ResourceObject):
    """    
    Args:
        name (str): Resource name of the repository, of the form '{{repo}}'.
                    The repo name may contain slashes. eg, 'name/with/slash'
    """
    _type = 'google_sourcerepo_repository'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        pubsub_configs: Optional[PubsubConfigs]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if pubsub_configs is not None:
                kwargs['pubsub_configs'] = pubsub_configs
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
