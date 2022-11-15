
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class FeaturesItem():
        type:str
        # non-optional-blocks
        
# wrapper list class
class Features(BlockList):
        items: List[FeaturesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GenericWebServiceItem():
        uri:str
        # non-optional-blocks
        password: Optional[str] = None
        request_headers: Optional[Dict[str, str]] = None
        username: Optional[str] = None
        
# wrapper list class
class GenericWebService(BlockList):
        items: List[GenericWebServiceItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleDialogflowFulfillment(ResourceObject):
    """    
    Args:
        display_name (str): The human-readable name of the fulfillment, unique within the agent.
    """
    _type = 'google_dialogflow_fulfillment'
    
    def __init__(self,
        tf_id: str,
        display_name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        enabled: Optional[bool] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        features: Optional[Features]=None,
        generic_web_service: Optional[GenericWebService]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if display_name is not None:
                kwargs['display_name'] = display_name
            if enabled is not None:
                kwargs['enabled'] = enabled
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if features is not None:
                kwargs['features'] = features
            if generic_web_service is not None:
                kwargs['generic_web_service'] = generic_web_service
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
