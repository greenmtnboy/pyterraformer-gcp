
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class AggregationsItem():
        # non-optional-blocks
        alignment_period: Optional[str] = None
        cross_series_reducer: Optional[str] = None
        group_by_fields: Optional[List[str]] = None
        per_series_aligner: Optional[str] = None
        
# wrapper list class
class Aggregations(BlockList):
        items: List[AggregationsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DenominatorAggregationsItem():
        # non-optional-blocks
        alignment_period: Optional[str] = None
        cross_series_reducer: Optional[str] = None
        group_by_fields: Optional[List[str]] = None
        per_series_aligner: Optional[str] = None
        
# wrapper list class
class DenominatorAggregations(BlockList):
        items: List[DenominatorAggregationsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TriggerItem():
        # non-optional-blocks
        count: Optional[float] = None
        percent: Optional[float] = None
        
# wrapper list class
class Trigger(BlockList):
        items: List[TriggerItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ConditionAbsentItem():
        duration:str
        # non-optional-blocks
        filter: Optional[str] = None
        aggregations: Optional[Aggregations]=None,
        trigger: Optional[Trigger]=None,
        
# wrapper list class
class ConditionAbsent(BlockList):
        items: List[ConditionAbsentItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ConditionThresholdItem():
        comparison:str
        duration:str
        # non-optional-blocks
        denominator_filter: Optional[str] = None
        filter: Optional[str] = None
        threshold_value: Optional[float] = None
        aggregations: Optional[Aggregations]=None,
        denominator_aggregations: Optional[DenominatorAggregations]=None,
        trigger: Optional[Trigger]=None,
        
# wrapper list class
class ConditionThreshold(BlockList):
        items: List[ConditionThresholdItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ConditionsItem():
        display_name:str
        # non-optional-blocks
        aggregations: Optional[Aggregations]=None,
        denominator_aggregations: Optional[DenominatorAggregations]=None,
        trigger: Optional[Trigger]=None,
        condition_absent: Optional[ConditionAbsent]=None,
        condition_threshold: Optional[ConditionThreshold]=None,
        
# wrapper list class
class Conditions(BlockList):
        items: List[ConditionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DocumentationItem():
        # non-optional-blocks
        content: Optional[str] = None
        mime_type: Optional[str] = None
        
# wrapper list class
class Documentation(BlockList):
        items: List[DocumentationItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleMonitoringAlertPolicy(ResourceObject):
    """    
    Args:
        combiner (str): 
        display_name (str): 
    """
    _type = 'google_monitoring_alert_policy'
    
    def __init__(self,
        tf_id: str,
        combiner:str,
        display_name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        enabled: Optional[bool] = None,
        id: Optional[str] = None,
        labels: Optional[List[str]] = None,
        notification_channels: Optional[List[str]] = None,
        project: Optional[str] = None,
        aggregations: Optional[Aggregations]=None,
        denominator_aggregations: Optional[DenominatorAggregations]=None,
        trigger: Optional[Trigger]=None,
        condition_absent: Optional[ConditionAbsent]=None,
        condition_threshold: Optional[ConditionThreshold]=None,
        conditions: Optional[Conditions]=None,
        documentation: Optional[Documentation]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if combiner is not None:
                kwargs['combiner'] = combiner
            if display_name is not None:
                kwargs['display_name'] = display_name
            if enabled is not None:
                kwargs['enabled'] = enabled
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if notification_channels is not None:
                kwargs['notification_channels'] = notification_channels
            if project is not None:
                kwargs['project'] = project
            if aggregations is not None:
                kwargs['aggregations'] = aggregations
            if denominator_aggregations is not None:
                kwargs['denominator_aggregations'] = denominator_aggregations
            if trigger is not None:
                kwargs['trigger'] = trigger
            if condition_absent is not None:
                kwargs['condition_absent'] = condition_absent
            if condition_threshold is not None:
                kwargs['condition_threshold'] = condition_threshold
            if conditions is not None:
                kwargs['conditions'] = conditions
            if documentation is not None:
                kwargs['documentation'] = documentation
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
