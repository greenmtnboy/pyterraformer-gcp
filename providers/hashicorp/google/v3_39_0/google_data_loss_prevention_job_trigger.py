
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class ScheduleItem():
        # non-optional-blocks
        recurrence_period_duration: Optional[str] = None
        
# wrapper list class
class Schedule(BlockList):
        items: List[ScheduleItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TimestampFieldItem():
        name:str
        # non-optional-blocks
        
# wrapper list class
class TimestampField(BlockList):
        items: List[TimestampFieldItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class KindItem():
        name:str
        # non-optional-blocks
        
# wrapper list class
class Kind(BlockList):
        items: List[KindItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PartitionIdItem():
        project_id:str
        # non-optional-blocks
        namespace_id: Optional[str] = None
        
# wrapper list class
class PartitionId(BlockList):
        items: List[PartitionIdItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RegexFileSetItem():
        bucket_name:str
        # non-optional-blocks
        exclude_regex: Optional[List[str]] = None
        include_regex: Optional[List[str]] = None
        
# wrapper list class
class RegexFileSet(BlockList):
        items: List[RegexFileSetItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class FileSetItem():
        # non-optional-blocks
        url: Optional[str] = None
        regex_file_set: Optional[RegexFileSet]=None,
        
# wrapper list class
class FileSet(BlockList):
        items: List[FileSetItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TableReferenceItem():
        dataset_id:str
        project_id:str
        table_id:str
        # non-optional-blocks
        
# wrapper list class
class TableReference(BlockList):
        items: List[TableReferenceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class BigQueryOptionsItem():
        # non-optional-blocks
        table_reference: Optional[TableReference]=None,
        
# wrapper list class
class BigQueryOptions(BlockList):
        items: List[BigQueryOptionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CloudStorageOptionsItem():
        # non-optional-blocks
        bytes_limit_per_file: Optional[float] = None
        bytes_limit_per_file_percent: Optional[float] = None
        file_types: Optional[List[str]] = None
        files_limit_percent: Optional[float] = None
        sample_method: Optional[str] = None
        regex_file_set: Optional[RegexFileSet]=None,
        file_set: Optional[FileSet]=None,
        
# wrapper list class
class CloudStorageOptions(BlockList):
        items: List[CloudStorageOptionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DatastoreOptionsItem():
        # non-optional-blocks
        kind: Optional[Kind]=None,
        partition_id: Optional[PartitionId]=None,
        
# wrapper list class
class DatastoreOptions(BlockList):
        items: List[DatastoreOptionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TimespanConfigItem():
        # non-optional-blocks
        enable_auto_population_of_timespan_config: Optional[bool] = None
        end_time: Optional[str] = None
        start_time: Optional[str] = None
        timestamp_field: Optional[TimestampField]=None,
        
# wrapper list class
class TimespanConfig(BlockList):
        items: List[TimespanConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TableItem():
        dataset_id:str
        project_id:str
        # non-optional-blocks
        table_id: Optional[str] = None
        
# wrapper list class
class Table(BlockList):
        items: List[TableItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class OutputConfigItem():
        # non-optional-blocks
        output_schema: Optional[str] = None
        table: Optional[Table]=None,
        
# wrapper list class
class OutputConfig(BlockList):
        items: List[OutputConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SaveFindingsItem():
        # non-optional-blocks
        table: Optional[Table]=None,
        output_config: Optional[OutputConfig]=None,
        
# wrapper list class
class SaveFindings(BlockList):
        items: List[SaveFindingsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ActionsItem():
        # non-optional-blocks
        table: Optional[Table]=None,
        output_config: Optional[OutputConfig]=None,
        save_findings: Optional[SaveFindings]=None,
        
# wrapper list class
class Actions(BlockList):
        items: List[ActionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class StorageConfigItem():
        # non-optional-blocks
        timestamp_field: Optional[TimestampField]=None,
        kind: Optional[Kind]=None,
        partition_id: Optional[PartitionId]=None,
        regex_file_set: Optional[RegexFileSet]=None,
        file_set: Optional[FileSet]=None,
        table_reference: Optional[TableReference]=None,
        big_query_options: Optional[BigQueryOptions]=None,
        cloud_storage_options: Optional[CloudStorageOptions]=None,
        datastore_options: Optional[DatastoreOptions]=None,
        timespan_config: Optional[TimespanConfig]=None,
        
# wrapper list class
class StorageConfig(BlockList):
        items: List[StorageConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class InspectJobItem():
        inspect_template_name:str
        # non-optional-blocks
        timestamp_field: Optional[TimestampField]=None,
        kind: Optional[Kind]=None,
        partition_id: Optional[PartitionId]=None,
        regex_file_set: Optional[RegexFileSet]=None,
        file_set: Optional[FileSet]=None,
        table_reference: Optional[TableReference]=None,
        big_query_options: Optional[BigQueryOptions]=None,
        cloud_storage_options: Optional[CloudStorageOptions]=None,
        datastore_options: Optional[DatastoreOptions]=None,
        timespan_config: Optional[TimespanConfig]=None,
        table: Optional[Table]=None,
        output_config: Optional[OutputConfig]=None,
        save_findings: Optional[SaveFindings]=None,
        actions: Optional[Actions]=None,
        storage_config: Optional[StorageConfig]=None,
        
# wrapper list class
class InspectJob(BlockList):
        items: List[InspectJobItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




# this block can contain multiple items, items in a list are required
@dataclass 
class TriggersItem():
        # non-optional-blocks
        schedule: Optional[Schedule]=None,
        
# wrapper list class
class Triggers(BlockList):
        items: List[TriggersItem]




class GoogleDataLossPreventionJobTrigger(ResourceObject):
    """    
    Args:
        parent (str): The parent of the trigger, either in the format 'projects/{{project}}'
                    or 'projects/{{project}}/locations/{{location}}'
    """
    _type = 'google_data_loss_prevention_job_trigger'
    
    def __init__(self,
        tf_id: str,
        parent:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        status: Optional[str] = None,
        schedule: Optional[Schedule]=None,
        timestamp_field: Optional[TimestampField]=None,
        kind: Optional[Kind]=None,
        partition_id: Optional[PartitionId]=None,
        regex_file_set: Optional[RegexFileSet]=None,
        file_set: Optional[FileSet]=None,
        table_reference: Optional[TableReference]=None,
        big_query_options: Optional[BigQueryOptions]=None,
        cloud_storage_options: Optional[CloudStorageOptions]=None,
        datastore_options: Optional[DatastoreOptions]=None,
        timespan_config: Optional[TimespanConfig]=None,
        table: Optional[Table]=None,
        output_config: Optional[OutputConfig]=None,
        save_findings: Optional[SaveFindings]=None,
        actions: Optional[Actions]=None,
        storage_config: Optional[StorageConfig]=None,
        inspect_job: Optional[InspectJob]=None,
        timeouts: Optional[Timeouts]=None,
        triggers: Optional[Triggers]=None,
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
            if status is not None:
                kwargs['status'] = status
            if schedule is not None:
                kwargs['schedule'] = schedule
            if timestamp_field is not None:
                kwargs['timestamp_field'] = timestamp_field
            if kind is not None:
                kwargs['kind'] = kind
            if partition_id is not None:
                kwargs['partition_id'] = partition_id
            if regex_file_set is not None:
                kwargs['regex_file_set'] = regex_file_set
            if file_set is not None:
                kwargs['file_set'] = file_set
            if table_reference is not None:
                kwargs['table_reference'] = table_reference
            if big_query_options is not None:
                kwargs['big_query_options'] = big_query_options
            if cloud_storage_options is not None:
                kwargs['cloud_storage_options'] = cloud_storage_options
            if datastore_options is not None:
                kwargs['datastore_options'] = datastore_options
            if timespan_config is not None:
                kwargs['timespan_config'] = timespan_config
            if table is not None:
                kwargs['table'] = table
            if output_config is not None:
                kwargs['output_config'] = output_config
            if save_findings is not None:
                kwargs['save_findings'] = save_findings
            if actions is not None:
                kwargs['actions'] = actions
            if storage_config is not None:
                kwargs['storage_config'] = storage_config
            if inspect_job is not None:
                kwargs['inspect_job'] = inspect_job
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            if triggers is not None:
                kwargs['triggers'] = triggers
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
