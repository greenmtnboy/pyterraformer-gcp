
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass




# this block can contain multiple items, items in a list are required
@dataclass 
class FieldsItem():
        field_name:str
        # non-optional-blocks
        bool_value: Optional[bool] = None
        double_value: Optional[float] = None
        enum_value: Optional[str] = None
        string_value: Optional[str] = None
        timestamp_value: Optional[str] = None
        
# wrapper list class
class Fields(BlockSet):
        items: Set[FieldsItem]



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleDataCatalogTag(ResourceObject):
    """    
    Args:
        template (str): The resource name of the tag template that this tag uses. Example:
                    projects/{project_id}/locations/{location}/tagTemplates/{tagTemplateId}
                    This field cannot be modified after creation.
    """
    _type = 'google_data_catalog_tag'
    
    def __init__(self,
        tf_id: str,
        template:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        column: Optional[str] = None,
        id: Optional[str] = None,
        parent: Optional[str] = None,
        fields: Optional[Fields]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if template is not None:
                kwargs['template'] = template
            if column is not None:
                kwargs['column'] = column
            if id is not None:
                kwargs['id'] = id
            if parent is not None:
                kwargs['parent'] = parent
            if fields is not None:
                kwargs['fields'] = fields
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
