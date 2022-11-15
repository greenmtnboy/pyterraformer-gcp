
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



class GoogleRuntimeconfigVariable(ResourceObject):
    """    
    Args:
        name (str): The name of the variable to manage. Note that variable names can be hierarchical using slashes (e.g. "prod-variables/hostname").
        parent (str): The name of the RuntimeConfig resource containing this variable.
    """
    _type = 'google_runtimeconfig_variable'
    
    def __init__(self,
        tf_id: str,
        name:str,
        parent:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        text: Optional[str] = None,
        value: Optional[str] = None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if parent is not None:
                kwargs['parent'] = parent
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if text is not None:
                kwargs['text'] = text
            if value is not None:
                kwargs['value'] = value
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
