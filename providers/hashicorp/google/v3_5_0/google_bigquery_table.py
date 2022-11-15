
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class CsvOptionsItem():
        quote:str
        # non-optional-blocks
        allow_jagged_rows: Optional[bool] = None
        allow_quoted_newlines: Optional[bool] = None
        encoding: Optional[str] = None
        field_delimiter: Optional[str] = None
        skip_leading_rows: Optional[float] = None
        
# wrapper list class
class CsvOptions(BlockList):
        items: List[CsvOptionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GoogleSheetsOptionsItem():
        # non-optional-blocks
        range: Optional[str] = None
        skip_leading_rows: Optional[float] = None
        
# wrapper list class
class GoogleSheetsOptions(BlockList):
        items: List[GoogleSheetsOptionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class EncryptionConfigurationItem():
        kms_key_name:str
        # non-optional-blocks
        
# wrapper list class
class EncryptionConfiguration(BlockList):
        items: List[EncryptionConfigurationItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ExternalDataConfigurationItem():
        autodetect:bool
        source_format:str
        source_uris:List[str]
        # non-optional-blocks
        compression: Optional[str] = None
        ignore_unknown_values: Optional[bool] = None
        max_bad_records: Optional[float] = None
        csv_options: Optional[CsvOptions]=None,
        google_sheets_options: Optional[GoogleSheetsOptions]=None,
        
# wrapper list class
class ExternalDataConfiguration(BlockList):
        items: List[ExternalDataConfigurationItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TimePartitioningItem():
        type:str
        # non-optional-blocks
        expiration_ms: Optional[float] = None
        field: Optional[str] = None
        require_partition_filter: Optional[bool] = None
        
# wrapper list class
class TimePartitioning(BlockList):
        items: List[TimePartitioningItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ViewItem():
        query:str
        # non-optional-blocks
        use_legacy_sql: Optional[bool] = None
        
# wrapper list class
class View(BlockList):
        items: List[ViewItem]




class GoogleBigqueryTable(ResourceObject):
    """    
    Args:
        dataset_id (str): 
        table_id (str): 
    """
    _type = 'google_bigquery_table'
    
    def __init__(self,
        tf_id: str,
        dataset_id:str,
        table_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        clustering: Optional[List[str]] = None,
        description: Optional[str] = None,
        expiration_time: Optional[float] = None,
        friendly_name: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        schema: Optional[str] = None,
        csv_options: Optional[CsvOptions]=None,
        google_sheets_options: Optional[GoogleSheetsOptions]=None,
        encryption_configuration: Optional[EncryptionConfiguration]=None,
        external_data_configuration: Optional[ExternalDataConfiguration]=None,
        time_partitioning: Optional[TimePartitioning]=None,
        view: Optional[View]=None,
        ):
            kwargs = {}
            if dataset_id is not None:
                kwargs['dataset_id'] = dataset_id
            if table_id is not None:
                kwargs['table_id'] = table_id
            if clustering is not None:
                kwargs['clustering'] = clustering
            if description is not None:
                kwargs['description'] = description
            if expiration_time is not None:
                kwargs['expiration_time'] = expiration_time
            if friendly_name is not None:
                kwargs['friendly_name'] = friendly_name
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if schema is not None:
                kwargs['schema'] = schema
            if csv_options is not None:
                kwargs['csv_options'] = csv_options
            if google_sheets_options is not None:
                kwargs['google_sheets_options'] = google_sheets_options
            if encryption_configuration is not None:
                kwargs['encryption_configuration'] = encryption_configuration
            if external_data_configuration is not None:
                kwargs['external_data_configuration'] = external_data_configuration
            if time_partitioning is not None:
                kwargs['time_partitioning'] = time_partitioning
            if view is not None:
                kwargs['view'] = view
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
