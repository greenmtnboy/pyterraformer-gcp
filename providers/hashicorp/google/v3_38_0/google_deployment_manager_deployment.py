
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class ConfigItem():
        content:str
        # non-optional-blocks
        
# wrapper list class
class Config(BlockList):
        items: List[ConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ImportsItem():
        # non-optional-blocks
        content: Optional[str] = None
        name: Optional[str] = None
        
# wrapper list class
class Imports(BlockList):
        items: List[ImportsItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class LabelsItem():
        # non-optional-blocks
        key: Optional[str] = None
        value: Optional[str] = None
        
# wrapper list class
class Labels(BlockSet):
        items: Set[LabelsItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class TargetItem():
        # non-optional-blocks
        config: Optional[Config]=None,
        imports: Optional[Imports]=None,
        
# wrapper list class
class Target(BlockList):
        items: List[TargetItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleDeploymentManagerDeployment(ResourceObject):
    """    
    Args:
        name (str): Unique name for the deployment
    """
    _type = 'google_deployment_manager_deployment'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        create_policy: Optional[str] = None,
        delete_policy: Optional[str] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        preview: Optional[bool] = None,
        project: Optional[str] = None,
        config: Optional[Config]=None,
        imports: Optional[Imports]=None,
        labels: Optional[Labels]=None,
        target: Optional[Target]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if create_policy is not None:
                kwargs['create_policy'] = create_policy
            if delete_policy is not None:
                kwargs['delete_policy'] = delete_policy
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if preview is not None:
                kwargs['preview'] = preview
            if project is not None:
                kwargs['project'] = project
            if config is not None:
                kwargs['config'] = config
            if imports is not None:
                kwargs['imports'] = imports
            if labels is not None:
                kwargs['labels'] = labels
            if target is not None:
                kwargs['target'] = target
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
