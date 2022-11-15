
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class ContainerImageItem():
        repository:str
        # non-optional-blocks
        tag: Optional[str] = None
        
# wrapper list class
class ContainerImage(BlockList):
        items: List[ContainerImageItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




# this block can contain multiple items, items in a list are required
@dataclass 
class VmImageItem():
        project:str
        # non-optional-blocks
        image_family: Optional[str] = None
        image_name: Optional[str] = None
        
# wrapper list class
class VmImage(BlockList):
        items: List[VmImageItem]




class GoogleNotebooksEnvironment(ResourceObject):
    """    
    Args:
        location (str): A reference to the zone where the machine resides.
        name (str): The name specified for the Environment instance.
                    Format: projects/{project_id}/locations/{location}/environments/{environmentId}
    """
    _type = 'google_notebooks_environment'
    
    def __init__(self,
        tf_id: str,
        location:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        post_startup_script: Optional[str] = None,
        project: Optional[str] = None,
        container_image: Optional[ContainerImage]=None,
        timeouts: Optional[Timeouts]=None,
        vm_image: Optional[VmImage]=None,
        ):
            kwargs = {}
            if location is not None:
                kwargs['location'] = location
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if display_name is not None:
                kwargs['display_name'] = display_name
            if id is not None:
                kwargs['id'] = id
            if post_startup_script is not None:
                kwargs['post_startup_script'] = post_startup_script
            if project is not None:
                kwargs['project'] = project
            if container_image is not None:
                kwargs['container_image'] = container_image
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if vm_image is not None:
                kwargs['vm_image'] = vm_image
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
