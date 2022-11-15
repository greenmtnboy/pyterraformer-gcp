
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleComputeGlobalForwardingRule(ResourceObject):
    """    
    Args:
        name (str): 
        target (str): 
    """
    _type = 'google_compute_global_forwarding_rule'
    
    def __init__(self,
        tf_id: str,
        name:str,
        target:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        ip_address: Optional[str] = None,
        ip_protocol: Optional[str] = None,
        ip_version: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        port_range: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if target is not None:
                kwargs['target'] = target
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if ip_address is not None:
                kwargs['ip_address'] = ip_address
            if ip_protocol is not None:
                kwargs['ip_protocol'] = ip_protocol
            if ip_version is not None:
                kwargs['ip_version'] = ip_version
            if labels is not None:
                kwargs['labels'] = labels
            if port_range is not None:
                kwargs['port_range'] = port_range
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
