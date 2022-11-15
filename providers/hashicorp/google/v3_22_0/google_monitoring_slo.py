
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class RangeItem():
        # non-optional-blocks
        max: Optional[float] = None
        min: Optional[float] = None
        
# wrapper list class
class Range(BlockList):
        items: List[RangeItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DistributionCutItem():
        distribution_filter:str
        # non-optional-blocks
        range: Optional[Range]=None,
        
# wrapper list class
class DistributionCut(BlockList):
        items: List[DistributionCutItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GoodTotalRatioItem():
        # non-optional-blocks
        bad_service_filter: Optional[str] = None
        good_service_filter: Optional[str] = None
        total_service_filter: Optional[str] = None
        
# wrapper list class
class GoodTotalRatio(BlockList):
        items: List[GoodTotalRatioItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class LatencyItem():
        threshold:str
        # non-optional-blocks
        
# wrapper list class
class Latency(BlockList):
        items: List[LatencyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class BasicSliItem():
        # non-optional-blocks
        location: Optional[Set[str]] = None
        method: Optional[Set[str]] = None
        version: Optional[Set[str]] = None
        latency: Optional[Latency]=None,
        
# wrapper list class
class BasicSli(BlockList):
        items: List[BasicSliItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RequestBasedSliItem():
        # non-optional-blocks
        range: Optional[Range]=None,
        distribution_cut: Optional[DistributionCut]=None,
        good_total_ratio: Optional[GoodTotalRatio]=None,
        
# wrapper list class
class RequestBasedSli(BlockList):
        items: List[RequestBasedSliItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleMonitoringSlo(ResourceObject):
    """    
    Args:
        goal (float): The fraction of service that must be good in order for this objective
                    to be met. 0 < goal <= 0.999
        service (str): ID of the service to which this SLO belongs.
    """
    _type = 'google_monitoring_slo'
    
    def __init__(self,
        tf_id: str,
        goal:float,
        service:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        calendar_period: Optional[str] = None,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        rolling_period_days: Optional[float] = None,
        slo_id: Optional[str] = None,
        range: Optional[Range]=None,
        distribution_cut: Optional[DistributionCut]=None,
        good_total_ratio: Optional[GoodTotalRatio]=None,
        latency: Optional[Latency]=None,
        basic_sli: Optional[BasicSli]=None,
        request_based_sli: Optional[RequestBasedSli]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if goal is not None:
                kwargs['goal'] = goal
            if service is not None:
                kwargs['service'] = service
            if calendar_period is not None:
                kwargs['calendar_period'] = calendar_period
            if display_name is not None:
                kwargs['display_name'] = display_name
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if rolling_period_days is not None:
                kwargs['rolling_period_days'] = rolling_period_days
            if slo_id is not None:
                kwargs['slo_id'] = slo_id
            if range is not None:
                kwargs['range'] = range
            if distribution_cut is not None:
                kwargs['distribution_cut'] = distribution_cut
            if good_total_ratio is not None:
                kwargs['good_total_ratio'] = good_total_ratio
            if latency is not None:
                kwargs['latency'] = latency
            if basic_sli is not None:
                kwargs['basic_sli'] = basic_sli
            if request_based_sli is not None:
                kwargs['request_based_sli'] = request_based_sli
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
