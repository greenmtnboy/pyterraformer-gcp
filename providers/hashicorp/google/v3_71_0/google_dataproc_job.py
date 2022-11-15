
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class LoggingConfigItem():
        driver_log_levels:Dict[str, str]
        # non-optional-blocks
        
# wrapper list class
class LoggingConfig(BlockList):
        items: List[LoggingConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HadoopConfigItem():
        # non-optional-blocks
        archive_uris: Optional[List[str]] = None
        args: Optional[List[str]] = None
        file_uris: Optional[List[str]] = None
        jar_file_uris: Optional[List[str]] = None
        main_class: Optional[str] = None
        main_jar_file_uri: Optional[str] = None
        properties: Optional[Dict[str, str]] = None
        logging_config: Optional[LoggingConfig]=None,
        
# wrapper list class
class HadoopConfig(BlockList):
        items: List[HadoopConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HiveConfigItem():
        # non-optional-blocks
        continue_on_failure: Optional[bool] = None
        jar_file_uris: Optional[List[str]] = None
        properties: Optional[Dict[str, str]] = None
        query_file_uri: Optional[str] = None
        query_list: Optional[List[str]] = None
        script_variables: Optional[Dict[str, str]] = None
        
# wrapper list class
class HiveConfig(BlockList):
        items: List[HiveConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PigConfigItem():
        # non-optional-blocks
        continue_on_failure: Optional[bool] = None
        jar_file_uris: Optional[List[str]] = None
        properties: Optional[Dict[str, str]] = None
        query_file_uri: Optional[str] = None
        query_list: Optional[List[str]] = None
        script_variables: Optional[Dict[str, str]] = None
        logging_config: Optional[LoggingConfig]=None,
        
# wrapper list class
class PigConfig(BlockList):
        items: List[PigConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PlacementItem():
        cluster_name:str
        # non-optional-blocks
        
# wrapper list class
class Placement(BlockList):
        items: List[PlacementItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PysparkConfigItem():
        main_python_file_uri:str
        # non-optional-blocks
        archive_uris: Optional[List[str]] = None
        args: Optional[List[str]] = None
        file_uris: Optional[List[str]] = None
        jar_file_uris: Optional[List[str]] = None
        properties: Optional[Dict[str, str]] = None
        python_file_uris: Optional[List[str]] = None
        logging_config: Optional[LoggingConfig]=None,
        
# wrapper list class
class PysparkConfig(BlockList):
        items: List[PysparkConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ReferenceItem():
        # non-optional-blocks
        job_id: Optional[str] = None
        
# wrapper list class
class Reference(BlockList):
        items: List[ReferenceItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SchedulingItem():
        max_failures_per_hour:float
        max_failures_total:float
        # non-optional-blocks
        
# wrapper list class
class Scheduling(BlockList):
        items: List[SchedulingItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SparkConfigItem():
        # non-optional-blocks
        archive_uris: Optional[List[str]] = None
        args: Optional[List[str]] = None
        file_uris: Optional[List[str]] = None
        jar_file_uris: Optional[List[str]] = None
        main_class: Optional[str] = None
        main_jar_file_uri: Optional[str] = None
        properties: Optional[Dict[str, str]] = None
        logging_config: Optional[LoggingConfig]=None,
        
# wrapper list class
class SparkConfig(BlockList):
        items: List[SparkConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SparksqlConfigItem():
        # non-optional-blocks
        jar_file_uris: Optional[List[str]] = None
        properties: Optional[Dict[str, str]] = None
        query_file_uri: Optional[str] = None
        query_list: Optional[List[str]] = None
        script_variables: Optional[Dict[str, str]] = None
        logging_config: Optional[LoggingConfig]=None,
        
# wrapper list class
class SparksqlConfig(BlockList):
        items: List[SparksqlConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleDataprocJob(ResourceObject):
    """    
    Args:
    """
    _type = 'google_dataproc_job'
    
    def __init__(self,
        tf_id: str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        force_delete: Optional[bool] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        region: Optional[str] = None,
        logging_config: Optional[LoggingConfig]=None,
        hadoop_config: Optional[HadoopConfig]=None,
        hive_config: Optional[HiveConfig]=None,
        pig_config: Optional[PigConfig]=None,
        placement: Optional[Placement]=None,
        pyspark_config: Optional[PysparkConfig]=None,
        reference: Optional[Reference]=None,
        scheduling: Optional[Scheduling]=None,
        spark_config: Optional[SparkConfig]=None,
        sparksql_config: Optional[SparksqlConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if force_delete is not None:
                kwargs['force_delete'] = force_delete
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if region is not None:
                kwargs['region'] = region
            if logging_config is not None:
                kwargs['logging_config'] = logging_config
            if hadoop_config is not None:
                kwargs['hadoop_config'] = hadoop_config
            if hive_config is not None:
                kwargs['hive_config'] = hive_config
            if pig_config is not None:
                kwargs['pig_config'] = pig_config
            if placement is not None:
                kwargs['placement'] = placement
            if pyspark_config is not None:
                kwargs['pyspark_config'] = pyspark_config
            if reference is not None:
                kwargs['reference'] = reference
            if scheduling is not None:
                kwargs['scheduling'] = scheduling
            if spark_config is not None:
                kwargs['spark_config'] = spark_config
            if sparksql_config is not None:
                kwargs['sparksql_config'] = sparksql_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
