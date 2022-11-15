
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class VolumesItem():
        name:str
        path:str
        # non-optional-blocks
        
# wrapper list class
class Volumes(BlockList):
        items: List[VolumesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class StepItem():
        name:str
        # non-optional-blocks
        args: Optional[List[str]] = None
        dir: Optional[str] = None
        entrypoint: Optional[str] = None
        env: Optional[List[str]] = None
        id: Optional[str] = None
        secret_env: Optional[List[str]] = None
        timeout: Optional[str] = None
        timing: Optional[str] = None
        wait_for: Optional[List[str]] = None
        volumes: Optional[Volumes]=None,
        
# wrapper list class
class Step(BlockList):
        items: List[StepItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class BuildItem():
        # non-optional-blocks
        images: Optional[List[str]] = None
        tags: Optional[List[str]] = None
        timeout: Optional[str] = None
        volumes: Optional[Volumes]=None,
        step: Optional[Step]=None,
        
# wrapper list class
class Build(BlockList):
        items: List[BuildItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




# this block can contain multiple items, items in a list are required
@dataclass 
class TriggerTemplateItem():
        # non-optional-blocks
        branch_name: Optional[str] = None
        commit_sha: Optional[str] = None
        dir: Optional[str] = None
        invert_regex: Optional[bool] = None
        project_id: Optional[str] = None
        repo_name: Optional[str] = None
        tag_name: Optional[str] = None
        
# wrapper list class
class TriggerTemplate(BlockList):
        items: List[TriggerTemplateItem]




class GoogleCloudbuildTrigger(ResourceObject):
    """    
    Args:
    """
    _type = 'google_cloudbuild_trigger'
    
    def __init__(self,
        tf_id: str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        disabled: Optional[bool] = None,
        filename: Optional[str] = None,
        id: Optional[str] = None,
        ignored_files: Optional[List[str]] = None,
        included_files: Optional[List[str]] = None,
        name: Optional[str] = None,
        project: Optional[str] = None,
        substitutions: Optional[Dict[str, str]] = None,
        volumes: Optional[Volumes]=None,
        step: Optional[Step]=None,
        build: Optional[Build]=None,
        timeouts: Optional[Timeouts]=None,
        trigger_template: Optional[TriggerTemplate]=None,
        ):
            kwargs = {}
            if description is not None:
                kwargs['description'] = description
            if disabled is not None:
                kwargs['disabled'] = disabled
            if filename is not None:
                kwargs['filename'] = filename
            if id is not None:
                kwargs['id'] = id
            if ignored_files is not None:
                kwargs['ignored_files'] = ignored_files
            if included_files is not None:
                kwargs['included_files'] = included_files
            if name is not None:
                kwargs['name'] = name
            if project is not None:
                kwargs['project'] = project
            if substitutions is not None:
                kwargs['substitutions'] = substitutions
            if volumes is not None:
                kwargs['volumes'] = volumes
            if step is not None:
                kwargs['step'] = step
            if build is not None:
                kwargs['build'] = build
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if trigger_template is not None:
                kwargs['trigger_template'] = trigger_template
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
