
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass




# this block can contain multiple items, items in a list are required
@dataclass 
class LabelsItem():
        key:str
        # non-optional-blocks
        description: Optional[str] = None
        value_type: Optional[str] = None
        
# wrapper list class
class Labels(BlockSet):
        items: Set[LabelsItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class MetadataItem():
        # non-optional-blocks
        ingest_delay: Optional[str] = None
        sample_period: Optional[str] = None
        
# wrapper list class
class Metadata(BlockList):
        items: List[MetadataItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleMonitoringMetricDescriptor(ResourceObject):
    """    
    Args:
        description (str): A detailed description of the metric, which can be used in documentation.
        display_name (str): A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example "Request count".
        metric_kind (str): Whether the metric records instantaneous values, changes to a value, etc. Some combinations of metricKind and valueType might not be supported. Possible values: ["METRIC_KIND_UNSPECIFIED", "GAUGE", "DELTA", "CUMULATIVE"]
        type (str): The metric type, including its DNS name prefix. The type is not URL-encoded. All service defined metrics must be prefixed with the service name, in the format of {service name}/{relative metric name}, such as cloudsql.googleapis.com/database/cpu/utilization. The relative metric name must have only upper and lower-case letters, digits, '/' and underscores '_' are allowed. Additionally, the maximum number of characters allowed for the relative_metric_name is 100. All user-defined metric types have the DNS name custom.googleapis.com, external.googleapis.com, or logging.googleapis.com/user/.
        value_type (str): Whether the measurement is an integer, a floating-point number, etc. Some combinations of metricKind and valueType might not be supported. Possible values: ["BOOL", "INT64", "DOUBLE", "STRING", "DISTRIBUTION"]
    """
    _type = 'google_monitoring_metric_descriptor'
    
    def __init__(self,
        tf_id: str,
        description:str,
        display_name:str,
        metric_kind:str,
        type:str,
        value_type:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        launch_stage: Optional[str] = None,
        project: Optional[str] = None,
        unit: Optional[str] = None,
        labels: Optional[Labels]=None,
        metadata: Optional[Metadata]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if description is not None:
                kwargs['description'] = description
            if display_name is not None:
                kwargs['display_name'] = display_name
            if metric_kind is not None:
                kwargs['metric_kind'] = metric_kind
            if type is not None:
                kwargs['type'] = type
            if value_type is not None:
                kwargs['value_type'] = value_type
            if id is not None:
                kwargs['id'] = id
            if launch_stage is not None:
                kwargs['launch_stage'] = launch_stage
            if project is not None:
                kwargs['project'] = project
            if unit is not None:
                kwargs['unit'] = unit
            if labels is not None:
                kwargs['labels'] = labels
            if metadata is not None:
                kwargs['metadata'] = metadata
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
