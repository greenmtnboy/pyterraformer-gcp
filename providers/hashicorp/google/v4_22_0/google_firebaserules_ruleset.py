
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class FilesItem():
        content:str
        name:str
        # non-optional-blocks
        fingerprint: Optional[str] = None
        
# wrapper list class
class Files(BlockList):
        items: List[FilesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SourceItem():
        # non-optional-blocks
        language: Optional[str] = None
        files: Optional[Files]=None,
        
# wrapper list class
class Source(BlockList):
        items: List[SourceItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleFirebaserulesRuleset(ResourceObject):
    """    
    Args:
    """
    _type = 'google_firebaserules_ruleset'
    
    def __init__(self,
        tf_id: str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        files: Optional[Files]=None,
        source: Optional[Source]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if files is not None:
                kwargs['files'] = files
            if source is not None:
                kwargs['source'] = source
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
