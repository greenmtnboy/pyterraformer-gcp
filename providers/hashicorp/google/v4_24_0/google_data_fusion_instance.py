
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class NetworkConfigItem():
        ip_allocation:str
        network:str
        # non-optional-blocks
        
# wrapper list class
class NetworkConfig(BlockList):
        items: List[NetworkConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleDataFusionInstance(ResourceObject):
    """    
    Args:
        name (str): The ID of the instance or a fully qualified identifier for the instance.
        type (str): Represents the type of Data Fusion instance. Each type is configured with
                    the default settings for processing and memory.
                    - BASIC: Basic Data Fusion instance. In Basic type, the user will be able to create data pipelines
                    using point and click UI. However, there are certain limitations, such as fewer number
                    of concurrent pipelines, no support for streaming pipelines, etc.
                    - ENTERPRISE: Enterprise Data Fusion instance. In Enterprise type, the user will have more features
                    available, such as support for streaming pipelines, higher number of concurrent pipelines, etc.
                    - DEVELOPER: Developer Data Fusion instance. In Developer type, the user will have all features available but
                    with restrictive capabilities. This is to help enterprises design and develop their data ingestion and integration 
                    pipelines at low cost. Possible values: ["BASIC", "ENTERPRISE", "DEVELOPER"]
    """
    _type = 'google_data_fusion_instance'
    
    def __init__(self,
        tf_id: str,
        name:str,
        type:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        dataproc_service_account: Optional[str] = None,
        description: Optional[str] = None,
        enable_stackdriver_logging: Optional[bool] = None,
        enable_stackdriver_monitoring: Optional[bool] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        options: Optional[Dict[str, str]] = None,
        private_instance: Optional[bool] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        version: Optional[str] = None,
        network_config: Optional[NetworkConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if type is not None:
                kwargs['type'] = type
            if dataproc_service_account is not None:
                kwargs['dataproc_service_account'] = dataproc_service_account
            if description is not None:
                kwargs['description'] = description
            if enable_stackdriver_logging is not None:
                kwargs['enable_stackdriver_logging'] = enable_stackdriver_logging
            if enable_stackdriver_monitoring is not None:
                kwargs['enable_stackdriver_monitoring'] = enable_stackdriver_monitoring
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if options is not None:
                kwargs['options'] = options
            if private_instance is not None:
                kwargs['private_instance'] = private_instance
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if version is not None:
                kwargs['version'] = version
            if network_config is not None:
                kwargs['network_config'] = network_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
