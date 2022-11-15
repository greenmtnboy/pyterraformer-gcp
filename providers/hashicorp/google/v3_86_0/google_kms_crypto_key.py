
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




# this block can contain multiple items, items in a list are required
@dataclass 
class VersionTemplateItem():
        algorithm:str
        # non-optional-blocks
        protection_level: Optional[str] = None
        
# wrapper list class
class VersionTemplate(BlockList):
        items: List[VersionTemplateItem]




class GoogleKmsCryptoKey(ResourceObject):
    """    
    Args:
        key_ring (str): The KeyRing that this key belongs to.
                    Format: ''projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}''.
        name (str): The resource name for the CryptoKey.
    """
    _type = 'google_kms_crypto_key'
    
    def __init__(self,
        tf_id: str,
        key_ring:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        destroy_scheduled_duration: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        purpose: Optional[str] = None,
        rotation_period: Optional[str] = None,
        skip_initial_version_creation: Optional[bool] = None,
        timeouts: Optional[Timeouts]=None,
        version_template: Optional[VersionTemplate]=None,
        ):
            kwargs = {}
            if key_ring is not None:
                kwargs['key_ring'] = key_ring
            if name is not None:
                kwargs['name'] = name
            if destroy_scheduled_duration is not None:
                kwargs['destroy_scheduled_duration'] = destroy_scheduled_duration
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if purpose is not None:
                kwargs['purpose'] = purpose
            if rotation_period is not None:
                kwargs['rotation_period'] = rotation_period
            if skip_initial_version_creation is not None:
                kwargs['skip_initial_version_creation'] = skip_initial_version_creation
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if version_template is not None:
                kwargs['version_template'] = version_template
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
