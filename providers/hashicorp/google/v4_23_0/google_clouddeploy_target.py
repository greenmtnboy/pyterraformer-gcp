
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class AnthosClusterItem():
        # non-optional-blocks
        membership: Optional[str] = None
        
# wrapper list class
class AnthosCluster(BlockList):
        items: List[AnthosClusterItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ExecutionConfigsItem():
        usages:List[str]
        # non-optional-blocks
        artifact_storage: Optional[str] = None
        service_account: Optional[str] = None
        worker_pool: Optional[str] = None
        
# wrapper list class
class ExecutionConfigs(BlockList):
        items: List[ExecutionConfigsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GkeItem():
        # non-optional-blocks
        cluster: Optional[str] = None
        internal_ip: Optional[bool] = None
        
# wrapper list class
class Gke(BlockList):
        items: List[GkeItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleClouddeployTarget(ResourceObject):
    """    
    Args:
        location (str): The location for the resource
        name (str): Name of the `Target`. Format is [a-z][a-z0-9\-]{0,62}.
    """
    _type = 'google_clouddeploy_target'
    
    def __init__(self,
        tf_id: str,
        location:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        annotations: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        require_approval: Optional[bool] = None,
        anthos_cluster: Optional[AnthosCluster]=None,
        execution_configs: Optional[ExecutionConfigs]=None,
        gke: Optional[Gke]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if location is not None:
                kwargs['location'] = location
            if name is not None:
                kwargs['name'] = name
            if annotations is not None:
                kwargs['annotations'] = annotations
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if require_approval is not None:
                kwargs['require_approval'] = require_approval
            if anthos_cluster is not None:
                kwargs['anthos_cluster'] = anthos_cluster
            if execution_configs is not None:
                kwargs['execution_configs'] = execution_configs
            if gke is not None:
                kwargs['gke'] = gke
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
