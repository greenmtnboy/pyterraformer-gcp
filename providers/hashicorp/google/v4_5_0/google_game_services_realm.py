
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleGameServicesRealm(ResourceObject):
    """    
    Args:
        realm_id (str): GCP region of the Realm.
        time_zone (str): Required. Time zone where all realm-specific policies are evaluated. The value of
                    this field must be from the IANA time zone database:
                    https://www.iana.org/time-zones.
    """
    _type = 'google_game_services_realm'
    
    def __init__(self,
        tf_id: str,
        realm_id:str,
        time_zone:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        location: Optional[str] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if realm_id is not None:
                kwargs['realm_id'] = realm_id
            if time_zone is not None:
                kwargs['time_zone'] = time_zone
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
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
