
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




class GoogleComputeSslPolicy(ResourceObject):
    """    
    Args:
        name (str): Name of the resource. Provided by the client when the resource is
                    created. The name must be 1-63 characters long, and comply with
                    RFC1035. Specifically, the name must be 1-63 characters long and match
                    the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the
                    first character must be a lowercase letter, and all following
                    characters must be a dash, lowercase letter, or digit, except the last
                    character, which cannot be a dash.
    """
    _type = 'google_compute_ssl_policy'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        custom_features: Optional[Set[str]] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        min_tls_version: Optional[str] = None,
        profile: Optional[str] = None,
        project: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if custom_features is not None:
                kwargs['custom_features'] = custom_features
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if min_tls_version is not None:
                kwargs['min_tls_version'] = min_tls_version
            if profile is not None:
                kwargs['profile'] = profile
            if project is not None:
                kwargs['project'] = project
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
