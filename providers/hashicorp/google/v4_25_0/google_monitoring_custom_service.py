
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class TelemetryItem():
        # non-optional-blocks
        resource_name: Optional[str] = None
        
# wrapper list class
class Telemetry(BlockList):
        items: List[TelemetryItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleMonitoringCustomService(ResourceObject):
    """    
    Args:
    """
    _type = 'google_monitoring_custom_service'
    
    def __init__(self,
        tf_id: str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        service_id: Optional[str] = None,
        user_labels: Optional[Dict[str, str]] = None,
        telemetry: Optional[Telemetry]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if display_name is not None:
                kwargs['display_name'] = display_name
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if service_id is not None:
                kwargs['service_id'] = service_id
            if user_labels is not None:
                kwargs['user_labels'] = user_labels
            if telemetry is not None:
                kwargs['telemetry'] = telemetry
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
