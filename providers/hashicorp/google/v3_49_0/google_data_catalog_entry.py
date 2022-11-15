
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class GcsFilesetSpecItem():
        file_patterns:List[str]
        # non-optional-blocks
        
# wrapper list class
class GcsFilesetSpec(BlockList):
        items: List[GcsFilesetSpecItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleDataCatalogEntry(ResourceObject):
    """    
    Args:
        entry_group (str): The name of the entry group this entry is in.
        entry_id (str): The id of the entry to create.
    """
    _type = 'google_data_catalog_entry'
    
    def __init__(self,
        tf_id: str,
        entry_group:str,
        entry_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        linked_resource: Optional[str] = None,
        schema: Optional[str] = None,
        type: Optional[str] = None,
        user_specified_system: Optional[str] = None,
        user_specified_type: Optional[str] = None,
        gcs_fileset_spec: Optional[GcsFilesetSpec]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if entry_group is not None:
                kwargs['entry_group'] = entry_group
            if entry_id is not None:
                kwargs['entry_id'] = entry_id
            if description is not None:
                kwargs['description'] = description
            if display_name is not None:
                kwargs['display_name'] = display_name
            if id is not None:
                kwargs['id'] = id
            if linked_resource is not None:
                kwargs['linked_resource'] = linked_resource
            if schema is not None:
                kwargs['schema'] = schema
            if type is not None:
                kwargs['type'] = type
            if user_specified_system is not None:
                kwargs['user_specified_system'] = user_specified_system
            if user_specified_type is not None:
                kwargs['user_specified_type'] = user_specified_type
            if gcs_fileset_spec is not None:
                kwargs['gcs_fileset_spec'] = gcs_fileset_spec
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
