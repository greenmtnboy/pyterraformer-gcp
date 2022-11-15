
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class EmailPreferencesItem():
        enable_failure_email:bool
        # non-optional-blocks
        
# wrapper list class
class EmailPreferences(BlockList):
        items: List[EmailPreferencesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ScheduleOptionsItem():
        # non-optional-blocks
        disable_auto_scheduling: Optional[bool] = None
        end_time: Optional[str] = None
        start_time: Optional[str] = None
        
# wrapper list class
class ScheduleOptions(BlockList):
        items: List[ScheduleOptionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SensitiveParamsItem():
        secret_access_key:str
        # non-optional-blocks
        
# wrapper list class
class SensitiveParams(BlockList):
        items: List[SensitiveParamsItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleBigqueryDataTransferConfig(ResourceObject):
    """    
    Args:
        data_source_id (str): The data source id. Cannot be changed once the transfer config is created.
        display_name (str): The user specified display name for the transfer config.
        params (Dict[str, str]): Parameters specific to each data source. For more information see the bq tab in the 'Setting up a data transfer'
                    section for each data source. For example the parameters for Cloud Storage transfers are listed here:
                    https://cloud.google.com/bigquery-transfer/docs/cloud-storage-transfer#bq
    """
    _type = 'google_bigquery_data_transfer_config'
    
    def __init__(self,
        tf_id: str,
        data_source_id:str,
        display_name:str,
        params:Dict[str, str],
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        data_refresh_window_days: Optional[float] = None,
        destination_dataset_id: Optional[str] = None,
        disabled: Optional[bool] = None,
        id: Optional[str] = None,
        location: Optional[str] = None,
        notification_pubsub_topic: Optional[str] = None,
        project: Optional[str] = None,
        schedule: Optional[str] = None,
        service_account_name: Optional[str] = None,
        email_preferences: Optional[EmailPreferences]=None,
        schedule_options: Optional[ScheduleOptions]=None,
        sensitive_params: Optional[SensitiveParams]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if data_source_id is not None:
                kwargs['data_source_id'] = data_source_id
            if display_name is not None:
                kwargs['display_name'] = display_name
            if params is not None:
                kwargs['params'] = params
            if data_refresh_window_days is not None:
                kwargs['data_refresh_window_days'] = data_refresh_window_days
            if destination_dataset_id is not None:
                kwargs['destination_dataset_id'] = destination_dataset_id
            if disabled is not None:
                kwargs['disabled'] = disabled
            if id is not None:
                kwargs['id'] = id
            if location is not None:
                kwargs['location'] = location
            if notification_pubsub_topic is not None:
                kwargs['notification_pubsub_topic'] = notification_pubsub_topic
            if project is not None:
                kwargs['project'] = project
            if schedule is not None:
                kwargs['schedule'] = schedule
            if service_account_name is not None:
                kwargs['service_account_name'] = service_account_name
            if email_preferences is not None:
                kwargs['email_preferences'] = email_preferences
            if schedule_options is not None:
                kwargs['schedule_options'] = schedule_options
            if sensitive_params is not None:
                kwargs['sensitive_params'] = sensitive_params
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
