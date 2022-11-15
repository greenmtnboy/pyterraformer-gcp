
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
class Labels(BlockList):
        items: List[LabelsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ExplicitItem():
        # non-optional-blocks
        bounds: Optional[List[str]] = None
        
# wrapper list class
class Explicit(BlockList):
        items: List[ExplicitItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ExponentialBucketsItem():
        # non-optional-blocks
        growth_factor: Optional[float] = None
        num_finite_buckets: Optional[float] = None
        scale: Optional[float] = None
        
# wrapper list class
class ExponentialBuckets(BlockList):
        items: List[ExponentialBucketsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class LinearBucketsItem():
        # non-optional-blocks
        num_finite_buckets: Optional[float] = None
        offset: Optional[float] = None
        width: Optional[float] = None
        
# wrapper list class
class LinearBuckets(BlockList):
        items: List[LinearBucketsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class BucketOptionsItem():
        # non-optional-blocks
        explicit: Optional[Explicit]=None,
        exponential_buckets: Optional[ExponentialBuckets]=None,
        linear_buckets: Optional[LinearBuckets]=None,
        
# wrapper list class
class BucketOptions(BlockList):
        items: List[BucketOptionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MetricDescriptorItem():
        metric_kind:str
        value_type:str
        # non-optional-blocks
        labels: Optional[Labels]=None,
        
# wrapper list class
class MetricDescriptor(BlockList):
        items: List[MetricDescriptorItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleLoggingMetric(ResourceObject):
    """    
    Args:
        filter (str): 
        name (str): 
    """
    _type = 'google_logging_metric'
    
    def __init__(self,
        tf_id: str,
        filter:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        label_extractors: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        value_extractor: Optional[str] = None,
        labels: Optional[Labels]=None,
        explicit: Optional[Explicit]=None,
        exponential_buckets: Optional[ExponentialBuckets]=None,
        linear_buckets: Optional[LinearBuckets]=None,
        bucket_options: Optional[BucketOptions]=None,
        metric_descriptor: Optional[MetricDescriptor]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if filter is not None:
                kwargs['filter'] = filter
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if label_extractors is not None:
                kwargs['label_extractors'] = label_extractors
            if project is not None:
                kwargs['project'] = project
            if value_extractor is not None:
                kwargs['value_extractor'] = value_extractor
            if labels is not None:
                kwargs['labels'] = labels
            if explicit is not None:
                kwargs['explicit'] = explicit
            if exponential_buckets is not None:
                kwargs['exponential_buckets'] = exponential_buckets
            if linear_buckets is not None:
                kwargs['linear_buckets'] = linear_buckets
            if bucket_options is not None:
                kwargs['bucket_options'] = bucket_options
            if metric_descriptor is not None:
                kwargs['metric_descriptor'] = metric_descriptor
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
