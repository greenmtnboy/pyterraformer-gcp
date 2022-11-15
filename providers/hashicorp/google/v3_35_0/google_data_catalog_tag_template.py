
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass




# this block can contain multiple items, items in a list are required
@dataclass 
class AllowedValuesItem():
        display_name:str
        # non-optional-blocks
        
# wrapper list class
class AllowedValues(BlockSet):
        items: Set[AllowedValuesItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class EnumTypeItem():
        # non-optional-blocks
        allowed_values: Optional[AllowedValues]=None,
        
# wrapper list class
class EnumType(BlockList):
        items: List[EnumTypeItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TypeItem():
        # non-optional-blocks
        primitive_type: Optional[str] = None
        allowed_values: Optional[AllowedValues]=None,
        enum_type: Optional[EnumType]=None,
        
# wrapper list class
class Type(BlockList):
        items: List[TypeItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class FieldsItem():
        field_id:str
        # non-optional-blocks
        display_name: Optional[str] = None
        is_required: Optional[bool] = None
        order: Optional[float] = None
        allowed_values: Optional[AllowedValues]=None,
        enum_type: Optional[EnumType]=None,
        type: Optional[Type]=None,
        
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




class GoogleDataCatalogTagTemplate(ResourceObject):
    """    
    Args:
        tag_template_id (str): The id of the tag template to create.
    """
    _type = 'google_data_catalog_tag_template'
    
    def __init__(self,
        tf_id: str,
        tag_template_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        display_name: Optional[str] = None,
        force_delete: Optional[bool] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        allowed_values: Optional[AllowedValues]=None,
        enum_type: Optional[EnumType]=None,
        type: Optional[Type]=None,
        fields: Optional[Fields]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if tag_template_id is not None:
                kwargs['tag_template_id'] = tag_template_id
            if display_name is not None:
                kwargs['display_name'] = display_name
            if force_delete is not None:
                kwargs['force_delete'] = force_delete
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if allowed_values is not None:
                kwargs['allowed_values'] = allowed_values
            if enum_type is not None:
                kwargs['enum_type'] = enum_type
            if type is not None:
                kwargs['type'] = type
            if fields is not None:
                kwargs['fields'] = fields
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
