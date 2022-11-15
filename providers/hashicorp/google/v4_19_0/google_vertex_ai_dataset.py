
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class EncryptionSpecItem():
        # non-optional-blocks
        kms_key_name: Optional[str] = None
        
# wrapper list class
class EncryptionSpec(BlockList):
        items: List[EncryptionSpecItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleVertexAiDataset(ResourceObject):
    """    
    Args:
        display_name (str): The user-defined name of the Dataset. The name can be up to 128 characters long and can be consist of any UTF-8 characters.
        metadata_schema_uri (str): Points to a YAML file stored on Google Cloud Storage describing additional information about the Dataset. The schema is defined as an OpenAPI 3.0.2 Schema Object. The schema files that can be used here are found in gs://google-cloud-aiplatform/schema/dataset/metadata/.
    """
    _type = 'google_vertex_ai_dataset'
    
    def __init__(self,
        tf_id: str,
        display_name:str,
        metadata_schema_uri:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        encryption_spec: Optional[EncryptionSpec]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if display_name is not None:
                kwargs['display_name'] = display_name
            if metadata_schema_uri is not None:
                kwargs['metadata_schema_uri'] = metadata_schema_uri
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if encryption_spec is not None:
                kwargs['encryption_spec'] = encryption_spec
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
