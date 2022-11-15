
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




class GoogleComputeFirewallPolicyAssociation(ResourceObject):
    """    
    Args:
        attachment_target (str): The target that the firewall policy is attached to.
        firewall_policy (str): The firewall policy ID of the association.
        name (str): The name for an association.
    """
    _type = 'google_compute_firewall_policy_association'
    
    def __init__(self,
        tf_id: str,
        attachment_target:str,
        firewall_policy:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if attachment_target is not None:
                kwargs['attachment_target'] = attachment_target
            if firewall_policy is not None:
                kwargs['firewall_policy'] = firewall_policy
            if name is not None:
                kwargs['name'] = name
            if id is not None:
                kwargs['id'] = id
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
