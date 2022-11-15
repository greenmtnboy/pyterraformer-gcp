
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class AzureCredentialsItem():
        sas_token:str
        # non-optional-blocks
        
# wrapper list class
class AzureCredentials(BlockList):
        items: List[AzureCredentialsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AwsAccessKeyItem():
        access_key_id:str
        secret_access_key:str
        # non-optional-blocks
        
# wrapper list class
class AwsAccessKey(BlockList):
        items: List[AwsAccessKeyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AwsS3DataSourceItem():
        bucket_name:str
        # non-optional-blocks
        aws_access_key: Optional[AwsAccessKey]=None,
        
# wrapper list class
class AwsS3DataSource(BlockList):
        items: List[AwsS3DataSourceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AzureBlobStorageDataSourceItem():
        container:str
        storage_account:str
        # non-optional-blocks
        path: Optional[str] = None
        azure_credentials: Optional[AzureCredentials]=None,
        
# wrapper list class
class AzureBlobStorageDataSource(BlockList):
        items: List[AzureBlobStorageDataSourceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GcsDataSinkItem():
        bucket_name:str
        # non-optional-blocks
        path: Optional[str] = None
        
# wrapper list class
class GcsDataSink(BlockList):
        items: List[GcsDataSinkItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GcsDataSourceItem():
        bucket_name:str
        # non-optional-blocks
        path: Optional[str] = None
        
# wrapper list class
class GcsDataSource(BlockList):
        items: List[GcsDataSourceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HttpDataSourceItem():
        list_url:str
        # non-optional-blocks
        
# wrapper list class
class HttpDataSource(BlockList):
        items: List[HttpDataSourceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ObjectConditionsItem():
        # non-optional-blocks
        exclude_prefixes: Optional[List[str]] = None
        include_prefixes: Optional[List[str]] = None
        max_time_elapsed_since_last_modification: Optional[str] = None
        min_time_elapsed_since_last_modification: Optional[str] = None
        
# wrapper list class
class ObjectConditions(BlockList):
        items: List[ObjectConditionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TransferOptionsItem():
        # non-optional-blocks
        delete_objects_from_source_after_transfer: Optional[bool] = None
        delete_objects_unique_in_sink: Optional[bool] = None
        overwrite_objects_already_existing_in_sink: Optional[bool] = None
        
# wrapper list class
class TransferOptions(BlockList):
        items: List[TransferOptionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ScheduleEndDateItem():
        day:float
        month:float
        year:float
        # non-optional-blocks
        
# wrapper list class
class ScheduleEndDate(BlockList):
        items: List[ScheduleEndDateItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ScheduleStartDateItem():
        day:float
        month:float
        year:float
        # non-optional-blocks
        
# wrapper list class
class ScheduleStartDate(BlockList):
        items: List[ScheduleStartDateItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class StartTimeOfDayItem():
        hours:float
        minutes:float
        nanos:float
        seconds:float
        # non-optional-blocks
        
# wrapper list class
class StartTimeOfDay(BlockList):
        items: List[StartTimeOfDayItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ScheduleItem():
        # non-optional-blocks
        schedule_end_date: Optional[ScheduleEndDate]=None,
        schedule_start_date: Optional[ScheduleStartDate]=None,
        start_time_of_day: Optional[StartTimeOfDay]=None,
        
# wrapper list class
class Schedule(BlockList):
        items: List[ScheduleItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TransferSpecItem():
        # non-optional-blocks
        azure_credentials: Optional[AzureCredentials]=None,
        aws_access_key: Optional[AwsAccessKey]=None,
        aws_s3_data_source: Optional[AwsS3DataSource]=None,
        azure_blob_storage_data_source: Optional[AzureBlobStorageDataSource]=None,
        gcs_data_sink: Optional[GcsDataSink]=None,
        gcs_data_source: Optional[GcsDataSource]=None,
        http_data_source: Optional[HttpDataSource]=None,
        object_conditions: Optional[ObjectConditions]=None,
        transfer_options: Optional[TransferOptions]=None,
        
# wrapper list class
class TransferSpec(BlockList):
        items: List[TransferSpecItem]




class GoogleStorageTransferJob(ResourceObject):
    """    
    Args:
        description (str): Unique description to identify the Transfer Job.
    """
    _type = 'google_storage_transfer_job'
    
    def __init__(self,
        tf_id: str,
        description:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        status: Optional[str] = None,
        azure_credentials: Optional[AzureCredentials]=None,
        aws_access_key: Optional[AwsAccessKey]=None,
        aws_s3_data_source: Optional[AwsS3DataSource]=None,
        azure_blob_storage_data_source: Optional[AzureBlobStorageDataSource]=None,
        gcs_data_sink: Optional[GcsDataSink]=None,
        gcs_data_source: Optional[GcsDataSource]=None,
        http_data_source: Optional[HttpDataSource]=None,
        object_conditions: Optional[ObjectConditions]=None,
        transfer_options: Optional[TransferOptions]=None,
        schedule_end_date: Optional[ScheduleEndDate]=None,
        schedule_start_date: Optional[ScheduleStartDate]=None,
        start_time_of_day: Optional[StartTimeOfDay]=None,
        schedule: Optional[Schedule]=None,
        transfer_spec: Optional[TransferSpec]=None,
        ):
            kwargs = {}
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if status is not None:
                kwargs['status'] = status
            if azure_credentials is not None:
                kwargs['azure_credentials'] = azure_credentials
            if aws_access_key is not None:
                kwargs['aws_access_key'] = aws_access_key
            if aws_s3_data_source is not None:
                kwargs['aws_s3_data_source'] = aws_s3_data_source
            if azure_blob_storage_data_source is not None:
                kwargs['azure_blob_storage_data_source'] = azure_blob_storage_data_source
            if gcs_data_sink is not None:
                kwargs['gcs_data_sink'] = gcs_data_sink
            if gcs_data_source is not None:
                kwargs['gcs_data_source'] = gcs_data_source
            if http_data_source is not None:
                kwargs['http_data_source'] = http_data_source
            if object_conditions is not None:
                kwargs['object_conditions'] = object_conditions
            if transfer_options is not None:
                kwargs['transfer_options'] = transfer_options
            if schedule_end_date is not None:
                kwargs['schedule_end_date'] = schedule_end_date
            if schedule_start_date is not None:
                kwargs['schedule_start_date'] = schedule_start_date
            if start_time_of_day is not None:
                kwargs['start_time_of_day'] = start_time_of_day
            if schedule is not None:
                kwargs['schedule'] = schedule
            if transfer_spec is not None:
                kwargs['transfer_spec'] = transfer_spec
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
