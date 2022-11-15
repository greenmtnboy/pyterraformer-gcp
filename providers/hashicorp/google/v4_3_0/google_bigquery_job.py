
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class DefaultDatasetItem():
        dataset_id:str
        # non-optional-blocks
        project_id: Optional[str] = None
        
# wrapper list class
class DefaultDataset(BlockList):
        items: List[DefaultDatasetItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DestinationEncryptionConfigurationItem():
        kms_key_name:str
        # non-optional-blocks
        
# wrapper list class
class DestinationEncryptionConfiguration(BlockList):
        items: List[DestinationEncryptionConfigurationItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DestinationTableItem():
        table_id:str
        # non-optional-blocks
        dataset_id: Optional[str] = None
        project_id: Optional[str] = None
        
# wrapper list class
class DestinationTable(BlockList):
        items: List[DestinationTableItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ScriptOptionsItem():
        # non-optional-blocks
        key_result_statement: Optional[str] = None
        statement_byte_budget: Optional[str] = None
        statement_timeout_ms: Optional[str] = None
        
# wrapper list class
class ScriptOptions(BlockList):
        items: List[ScriptOptionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class UserDefinedFunctionResourcesItem():
        # non-optional-blocks
        inline_code: Optional[str] = None
        resource_uri: Optional[str] = None
        
# wrapper list class
class UserDefinedFunctionResources(BlockList):
        items: List[UserDefinedFunctionResourcesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TimePartitioningItem():
        type:str
        # non-optional-blocks
        expiration_ms: Optional[str] = None
        field: Optional[str] = None
        
# wrapper list class
class TimePartitioning(BlockList):
        items: List[TimePartitioningItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SourceModelItem():
        dataset_id:str
        model_id:str
        project_id:str
        # non-optional-blocks
        
# wrapper list class
class SourceModel(BlockList):
        items: List[SourceModelItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SourceTableItem():
        table_id:str
        # non-optional-blocks
        dataset_id: Optional[str] = None
        project_id: Optional[str] = None
        
# wrapper list class
class SourceTable(BlockList):
        items: List[SourceTableItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SourceTablesItem():
        table_id:str
        # non-optional-blocks
        dataset_id: Optional[str] = None
        project_id: Optional[str] = None
        
# wrapper list class
class SourceTables(BlockList):
        items: List[SourceTablesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CopyItem():
        # non-optional-blocks
        create_disposition: Optional[str] = None
        write_disposition: Optional[str] = None
        destination_encryption_configuration: Optional[DestinationEncryptionConfiguration]=None,
        destination_table: Optional[DestinationTable]=None,
        source_tables: Optional[SourceTables]=None,
        
# wrapper list class
class Copy(BlockList):
        items: List[CopyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ExtractItem():
        destination_uris:List[str]
        # non-optional-blocks
        compression: Optional[str] = None
        destination_format: Optional[str] = None
        field_delimiter: Optional[str] = None
        print_header: Optional[bool] = None
        use_avro_logical_types: Optional[bool] = None
        source_model: Optional[SourceModel]=None,
        source_table: Optional[SourceTable]=None,
        
# wrapper list class
class Extract(BlockList):
        items: List[ExtractItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class LoadItem():
        source_uris:List[str]
        # non-optional-blocks
        allow_jagged_rows: Optional[bool] = None
        allow_quoted_newlines: Optional[bool] = None
        autodetect: Optional[bool] = None
        create_disposition: Optional[str] = None
        encoding: Optional[str] = None
        field_delimiter: Optional[str] = None
        ignore_unknown_values: Optional[bool] = None
        max_bad_records: Optional[float] = None
        null_marker: Optional[str] = None
        projection_fields: Optional[List[str]] = None
        quote: Optional[str] = None
        schema_update_options: Optional[List[str]] = None
        skip_leading_rows: Optional[float] = None
        source_format: Optional[str] = None
        write_disposition: Optional[str] = None
        destination_encryption_configuration: Optional[DestinationEncryptionConfiguration]=None,
        destination_table: Optional[DestinationTable]=None,
        time_partitioning: Optional[TimePartitioning]=None,
        
# wrapper list class
class Load(BlockList):
        items: List[LoadItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class QueryItem():
        query:str
        # non-optional-blocks
        allow_large_results: Optional[bool] = None
        create_disposition: Optional[str] = None
        flatten_results: Optional[bool] = None
        maximum_billing_tier: Optional[float] = None
        maximum_bytes_billed: Optional[str] = None
        parameter_mode: Optional[str] = None
        priority: Optional[str] = None
        schema_update_options: Optional[List[str]] = None
        use_legacy_sql: Optional[bool] = None
        use_query_cache: Optional[bool] = None
        write_disposition: Optional[str] = None
        default_dataset: Optional[DefaultDataset]=None,
        destination_encryption_configuration: Optional[DestinationEncryptionConfiguration]=None,
        destination_table: Optional[DestinationTable]=None,
        script_options: Optional[ScriptOptions]=None,
        user_defined_function_resources: Optional[UserDefinedFunctionResources]=None,
        
# wrapper list class
class Query(BlockList):
        items: List[QueryItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleBigqueryJob(ResourceObject):
    """    
    Args:
        job_id (str): The ID of the job. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). The maximum length is 1,024 characters.
    """
    _type = 'google_bigquery_job'
    
    def __init__(self,
        tf_id: str,
        job_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        job_timeout_ms: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        location: Optional[str] = None,
        project: Optional[str] = None,
        default_dataset: Optional[DefaultDataset]=None,
        destination_encryption_configuration: Optional[DestinationEncryptionConfiguration]=None,
        destination_table: Optional[DestinationTable]=None,
        script_options: Optional[ScriptOptions]=None,
        user_defined_function_resources: Optional[UserDefinedFunctionResources]=None,
        time_partitioning: Optional[TimePartitioning]=None,
        source_model: Optional[SourceModel]=None,
        source_table: Optional[SourceTable]=None,
        source_tables: Optional[SourceTables]=None,
        copy: Optional[Copy]=None,
        extract: Optional[Extract]=None,
        load: Optional[Load]=None,
        query: Optional[Query]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if job_id is not None:
                kwargs['job_id'] = job_id
            if id is not None:
                kwargs['id'] = id
            if job_timeout_ms is not None:
                kwargs['job_timeout_ms'] = job_timeout_ms
            if labels is not None:
                kwargs['labels'] = labels
            if location is not None:
                kwargs['location'] = location
            if project is not None:
                kwargs['project'] = project
            if default_dataset is not None:
                kwargs['default_dataset'] = default_dataset
            if destination_encryption_configuration is not None:
                kwargs['destination_encryption_configuration'] = destination_encryption_configuration
            if destination_table is not None:
                kwargs['destination_table'] = destination_table
            if script_options is not None:
                kwargs['script_options'] = script_options
            if user_defined_function_resources is not None:
                kwargs['user_defined_function_resources'] = user_defined_function_resources
            if time_partitioning is not None:
                kwargs['time_partitioning'] = time_partitioning
            if source_model is not None:
                kwargs['source_model'] = source_model
            if source_table is not None:
                kwargs['source_table'] = source_table
            if source_tables is not None:
                kwargs['source_tables'] = source_tables
            if copy is not None:
                kwargs['copy'] = copy
            if extract is not None:
                kwargs['extract'] = extract
            if load is not None:
                kwargs['load'] = load
            if query is not None:
                kwargs['query'] = query
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
