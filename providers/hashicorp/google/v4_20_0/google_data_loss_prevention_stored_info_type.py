
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class FieldItem():
        name:str
        # non-optional-blocks
        
# wrapper list class
class Field(BlockList):
        items: List[FieldItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TableItem():
        dataset_id:str
        project_id:str
        table_id:str
        # non-optional-blocks
        
# wrapper list class
class Table(BlockList):
        items: List[TableItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class BigQueryFieldItem():
        # non-optional-blocks
        field: Optional[Field]=None,
        table: Optional[Table]=None,
        
# wrapper list class
class BigQueryField(BlockList):
        items: List[BigQueryFieldItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CloudStorageFileSetItem():
        url:str
        # non-optional-blocks
        
# wrapper list class
class CloudStorageFileSet(BlockList):
        items: List[CloudStorageFileSetItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class OutputPathItem():
        path:str
        # non-optional-blocks
        
# wrapper list class
class OutputPath(BlockList):
        items: List[OutputPathItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CloudStoragePathItem():
        path:str
        # non-optional-blocks
        
# wrapper list class
class CloudStoragePath(BlockList):
        items: List[CloudStoragePathItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WordListItem():
        words:List[str]
        # non-optional-blocks
        
# wrapper list class
class WordList(BlockList):
        items: List[WordListItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DictionaryItem():
        # non-optional-blocks
        cloud_storage_path: Optional[CloudStoragePath]=None,
        word_list: Optional[WordList]=None,
        
# wrapper list class
class Dictionary(BlockList):
        items: List[DictionaryItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class LargeCustomDictionaryItem():
        # non-optional-blocks
        field: Optional[Field]=None,
        table: Optional[Table]=None,
        big_query_field: Optional[BigQueryField]=None,
        cloud_storage_file_set: Optional[CloudStorageFileSet]=None,
        output_path: Optional[OutputPath]=None,
        
# wrapper list class
class LargeCustomDictionary(BlockList):
        items: List[LargeCustomDictionaryItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RegexItem():
        pattern:str
        # non-optional-blocks
        group_indexes: Optional[List[float]] = None
        
# wrapper list class
class Regex(BlockList):
        items: List[RegexItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleDataLossPreventionStoredInfoType(ResourceObject):
    """    
    Args:
        parent (str): The parent of the info type in any of the following formats:

                    * 'projects/{{project}}'
                    * 'projects/{{project}}/locations/{{location}}'
                    * 'organizations/{{organization_id}}'
                    * 'organizations/{{organization_id}}/locations/{{location}}'
    """
    _type = 'google_data_loss_prevention_stored_info_type'
    
    def __init__(self,
        tf_id: str,
        parent:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        field: Optional[Field]=None,
        table: Optional[Table]=None,
        big_query_field: Optional[BigQueryField]=None,
        cloud_storage_file_set: Optional[CloudStorageFileSet]=None,
        output_path: Optional[OutputPath]=None,
        cloud_storage_path: Optional[CloudStoragePath]=None,
        word_list: Optional[WordList]=None,
        dictionary: Optional[Dictionary]=None,
        large_custom_dictionary: Optional[LargeCustomDictionary]=None,
        regex: Optional[Regex]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if parent is not None:
                kwargs['parent'] = parent
            if description is not None:
                kwargs['description'] = description
            if display_name is not None:
                kwargs['display_name'] = display_name
            if id is not None:
                kwargs['id'] = id
            if field is not None:
                kwargs['field'] = field
            if table is not None:
                kwargs['table'] = table
            if big_query_field is not None:
                kwargs['big_query_field'] = big_query_field
            if cloud_storage_file_set is not None:
                kwargs['cloud_storage_file_set'] = cloud_storage_file_set
            if output_path is not None:
                kwargs['output_path'] = output_path
            if cloud_storage_path is not None:
                kwargs['cloud_storage_path'] = cloud_storage_path
            if word_list is not None:
                kwargs['word_list'] = word_list
            if dictionary is not None:
                kwargs['dictionary'] = dictionary
            if large_custom_dictionary is not None:
                kwargs['large_custom_dictionary'] = large_custom_dictionary
            if regex is not None:
                kwargs['regex'] = regex
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
