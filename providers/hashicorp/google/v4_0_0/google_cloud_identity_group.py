
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class GroupKeyItem():
        id:str
        # non-optional-blocks
        namespace: Optional[str] = None
        
# wrapper list class
class GroupKey(BlockList):
        items: List[GroupKeyItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleCloudIdentityGroup(ResourceObject):
    """    
    Args:
        labels (Dict[str, str]): The labels that apply to the Group.

                    Must not contain more than one entry. Must contain the entry
                    'cloudidentity.googleapis.com/groups.discussion_forum': '' if the Group is a Google Group or
                    'system/groups/external': '' if the Group is an external-identity-mapped group.
        parent (str): The resource name of the entity under which this Group resides in the
                    Cloud Identity resource hierarchy.

                    Must be of the form identitysources/{identity_source_id} for external-identity-mapped
                    groups or customers/{customer_id} for Google Groups.
    """
    _type = 'google_cloud_identity_group'
    
    def __init__(self,
        tf_id: str,
        labels:Dict[str, str],
        parent:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        initial_group_config: Optional[str] = None,
        group_key: Optional[GroupKey]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if labels is not None:
                kwargs['labels'] = labels
            if parent is not None:
                kwargs['parent'] = parent
            if description is not None:
                kwargs['description'] = description
            if display_name is not None:
                kwargs['display_name'] = display_name
            if id is not None:
                kwargs['id'] = id
            if initial_group_config is not None:
                kwargs['initial_group_config'] = initial_group_config
            if group_key is not None:
                kwargs['group_key'] = group_key
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
