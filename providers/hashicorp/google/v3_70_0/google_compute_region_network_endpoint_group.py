
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class AppEngineItem():
        # non-optional-blocks
        service: Optional[str] = None
        url_mask: Optional[str] = None
        version: Optional[str] = None
        
# wrapper list class
class AppEngine(BlockList):
        items: List[AppEngineItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CloudFunctionItem():
        # non-optional-blocks
        function: Optional[str] = None
        url_mask: Optional[str] = None
        
# wrapper list class
class CloudFunction(BlockList):
        items: List[CloudFunctionItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CloudRunItem():
        # non-optional-blocks
        service: Optional[str] = None
        tag: Optional[str] = None
        url_mask: Optional[str] = None
        
# wrapper list class
class CloudRun(BlockList):
        items: List[CloudRunItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleComputeRegionNetworkEndpointGroup(ResourceObject):
    """    
    Args:
        name (str): Name of the resource; provided by the client when the resource is
                    created. The name must be 1-63 characters long, and comply with
                    RFC1035. Specifically, the name must be 1-63 characters long and match
                    the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the
                    first character must be a lowercase letter, and all following
                    characters must be a dash, lowercase letter, or digit, except the last
                    character, which cannot be a dash.
        region (str): A reference to the region where the Serverless NEGs Reside.
    """
    _type = 'google_compute_region_network_endpoint_group'
    
    def __init__(self,
        tf_id: str,
        name:str,
        region:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        network_endpoint_type: Optional[str] = None,
        project: Optional[str] = None,
        app_engine: Optional[AppEngine]=None,
        cloud_function: Optional[CloudFunction]=None,
        cloud_run: Optional[CloudRun]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if region is not None:
                kwargs['region'] = region
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if network_endpoint_type is not None:
                kwargs['network_endpoint_type'] = network_endpoint_type
            if project is not None:
                kwargs['project'] = project
            if app_engine is not None:
                kwargs['app_engine'] = app_engine
            if cloud_function is not None:
                kwargs['cloud_function'] = cloud_function
            if cloud_run is not None:
                kwargs['cloud_run'] = cloud_run
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
