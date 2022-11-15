
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class HintItem():
        human_readable_name:str
        # non-optional-blocks
        
# wrapper list class
class Hint(BlockList):
        items: List[HintItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AttestationAuthorityItem():
        # non-optional-blocks
        hint: Optional[Hint]=None,
        
# wrapper list class
class AttestationAuthority(BlockList):
        items: List[AttestationAuthorityItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleContainerAnalysisNote(ResourceObject):
    """    
    Args:
        name (str): The name of the note.
    """
    _type = 'google_container_analysis_note'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        hint: Optional[Hint]=None,
        attestation_authority: Optional[AttestationAuthority]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if hint is not None:
                kwargs['hint'] = hint
            if attestation_authority is not None:
                kwargs['attestation_authority'] = attestation_authority
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
