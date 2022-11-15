
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





# this block can contain multiple items, items in a list are required
@dataclass 
class RelatedUrlItem():
        url:str
        # non-optional-blocks
        label: Optional[str] = None
        
# wrapper list class
class RelatedUrl(BlockSet):
        items: Set[RelatedUrlItem]



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
        expiration_time: Optional[str] = None,
        id: Optional[str] = None,
        long_description: Optional[str] = None,
        project: Optional[str] = None,
        related_note_names: Optional[Set[str]] = None,
        short_description: Optional[str] = None,
        hint: Optional[Hint]=None,
        attestation_authority: Optional[AttestationAuthority]=None,
        related_url: Optional[RelatedUrl]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if expiration_time is not None:
                kwargs['expiration_time'] = expiration_time
            if id is not None:
                kwargs['id'] = id
            if long_description is not None:
                kwargs['long_description'] = long_description
            if project is not None:
                kwargs['project'] = project
            if related_note_names is not None:
                kwargs['related_note_names'] = related_note_names
            if short_description is not None:
                kwargs['short_description'] = short_description
            if hint is not None:
                kwargs['hint'] = hint
            if attestation_authority is not None:
                kwargs['attestation_authority'] = attestation_authority
            if related_url is not None:
                kwargs['related_url'] = related_url
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
