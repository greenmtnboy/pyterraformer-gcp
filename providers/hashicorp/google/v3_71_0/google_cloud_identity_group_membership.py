
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class PreferredMemberKeyItem():
        id:str
        # non-optional-blocks
        namespace: Optional[str] = None
        
# wrapper list class
class PreferredMemberKey(BlockList):
        items: List[PreferredMemberKeyItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class RolesItem():
        name:str
        # non-optional-blocks
        
# wrapper list class
class Roles(BlockSet):
        items: Set[RolesItem]



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleCloudIdentityGroupMembership(ResourceObject):
    """    
    Args:
        group (str): The name of the Group to create this membership in.
    """
    _type = 'google_cloud_identity_group_membership'
    
    def __init__(self,
        tf_id: str,
        group:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        preferred_member_key: Optional[PreferredMemberKey]=None,
        roles: Optional[Roles]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if group is not None:
                kwargs['group'] = group
            if id is not None:
                kwargs['id'] = id
            if preferred_member_key is not None:
                kwargs['preferred_member_key'] = preferred_member_key
            if roles is not None:
                kwargs['roles'] = roles
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
