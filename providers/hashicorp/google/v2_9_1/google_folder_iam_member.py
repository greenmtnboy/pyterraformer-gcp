
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleFolderIamMember(ResourceObject):
    """    
    Args:
        folder (str): 
        member (str): 
        role (str): 
    """
    _type = 'google_folder_iam_member'
    
    def __init__(self,
        tf_id: str,
        folder:str,
        member:str,
        role:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        ):
            kwargs = {}
            if folder is not None:
                kwargs['folder'] = folder
            if member is not None:
                kwargs['member'] = member
            if role is not None:
                kwargs['role'] = role
            if id is not None:
                kwargs['id'] = id
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
