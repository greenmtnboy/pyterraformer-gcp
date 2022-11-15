
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




class GoogleWorkflowsWorkflow(ResourceObject):
    """    
    Args:
    """
    _type = 'google_workflows_workflow'
    
    def __init__(self,
        tf_id: str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        name: Optional[str] = None,
        name_prefix: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        service_account: Optional[str] = None,
        source_contents: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if name is not None:
                kwargs['name'] = name
            if name_prefix is not None:
                kwargs['name_prefix'] = name_prefix
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if service_account is not None:
                kwargs['service_account'] = service_account
            if source_contents is not None:
                kwargs['source_contents'] = source_contents
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
