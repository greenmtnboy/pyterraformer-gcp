
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class SchemaConfigItem():
        recursive_structure_depth:float
        # non-optional-blocks
        schema_type: Optional[str] = None
        
# wrapper list class
class SchemaConfig(BlockList):
        items: List[SchemaConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class BigqueryDestinationItem():
        dataset_uri:str
        # non-optional-blocks
        schema_config: Optional[SchemaConfig]=None,
        
# wrapper list class
class BigqueryDestination(BlockList):
        items: List[BigqueryDestinationItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class NotificationConfigItem():
        pubsub_topic:str
        # non-optional-blocks
        
# wrapper list class
class NotificationConfig(BlockList):
        items: List[NotificationConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class StreamConfigsItem():
        # non-optional-blocks
        resource_types: Optional[List[str]] = None
        schema_config: Optional[SchemaConfig]=None,
        bigquery_destination: Optional[BigqueryDestination]=None,
        
# wrapper list class
class StreamConfigs(BlockList):
        items: List[StreamConfigsItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleHealthcareFhirStore(ResourceObject):
    """    
    Args:
        dataset (str): Identifies the dataset addressed by this request. Must be in the format
                    'projects/{project}/locations/{location}/datasets/{dataset}'
        name (str): The resource name for the FhirStore.

                    ** Changing this property may recreate the FHIR store (removing all data) **
        version (str): The FHIR specification version. Possible values: ["DSTU2", "STU3", "R4"]
    """
    _type = 'google_healthcare_fhir_store'
    
    def __init__(self,
        tf_id: str,
        dataset:str,
        name:str,
        version:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        disable_referential_integrity: Optional[bool] = None,
        disable_resource_versioning: Optional[bool] = None,
        enable_history_import: Optional[bool] = None,
        enable_update_create: Optional[bool] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        schema_config: Optional[SchemaConfig]=None,
        bigquery_destination: Optional[BigqueryDestination]=None,
        notification_config: Optional[NotificationConfig]=None,
        stream_configs: Optional[StreamConfigs]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if dataset is not None:
                kwargs['dataset'] = dataset
            if name is not None:
                kwargs['name'] = name
            if version is not None:
                kwargs['version'] = version
            if disable_referential_integrity is not None:
                kwargs['disable_referential_integrity'] = disable_referential_integrity
            if disable_resource_versioning is not None:
                kwargs['disable_resource_versioning'] = disable_resource_versioning
            if enable_history_import is not None:
                kwargs['enable_history_import'] = enable_history_import
            if enable_update_create is not None:
                kwargs['enable_update_create'] = enable_update_create
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if schema_config is not None:
                kwargs['schema_config'] = schema_config
            if bigquery_destination is not None:
                kwargs['bigquery_destination'] = bigquery_destination
            if notification_config is not None:
                kwargs['notification_config'] = notification_config
            if stream_configs is not None:
                kwargs['stream_configs'] = stream_configs
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
