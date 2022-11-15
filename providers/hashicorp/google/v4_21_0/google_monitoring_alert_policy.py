
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
class ConditionMatchedLogItem():
        filter:str
        # non-optional-blocks
        label_extractors: Optional[Dict[str, str]] = None
        
# wrapper list class
class ConditionMatchedLog(BlockList):
        items: List[ConditionMatchedLogItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ConditionMonitoringQueryLanguageItem():
        duration:str
        query:str
        # non-optional-blocks
        trigger: Optional[Trigger]=None,
        
# wrapper list class
class ConditionMonitoringQueryLanguage(BlockList):
        items: List[ConditionMonitoringQueryLanguageItem]




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
class NotificationRateLimitItem():
        # non-optional-blocks
        period: Optional[str] = None
        
# wrapper list class
class NotificationRateLimit(BlockList):
        items: List[NotificationRateLimitItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AlertStrategyItem():
        # non-optional-blocks
        auto_close: Optional[str] = None
        notification_rate_limit: Optional[NotificationRateLimit]=None,
        
# wrapper list class
class AlertStrategy(BlockList):
        items: List[AlertStrategyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ConditionsItem():
        display_name:str
        # non-optional-blocks
        aggregations: Optional[Aggregations]=None,
        denominator_aggregations: Optional[DenominatorAggregations]=None,
        trigger: Optional[Trigger]=None,
        condition_absent: Optional[ConditionAbsent]=None,
        condition_matched_log: Optional[ConditionMatchedLog]=None,
        condition_monitoring_query_language: Optional[ConditionMonitoringQueryLanguage]=None,
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
        combiner (str): How to combine the results of multiple conditions to
                    determine if an incident should be opened. Possible values: ["AND", "OR", "AND_WITH_MATCHING_RESOURCE"]
        display_name (str): A short name or phrase used to identify the policy in
                    dashboards, notifications, and incidents. To avoid confusion, don't use
                    the same display name for multiple policies in the same project. The
                    name is limited to 512 Unicode characters.
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
        notification_channels: Optional[List[str]] = None,
        project: Optional[str] = None,
        user_labels: Optional[Dict[str, str]] = None,
        aggregations: Optional[Aggregations]=None,
        denominator_aggregations: Optional[DenominatorAggregations]=None,
        trigger: Optional[Trigger]=None,
        condition_absent: Optional[ConditionAbsent]=None,
        condition_matched_log: Optional[ConditionMatchedLog]=None,
        condition_monitoring_query_language: Optional[ConditionMonitoringQueryLanguage]=None,
        condition_threshold: Optional[ConditionThreshold]=None,
        notification_rate_limit: Optional[NotificationRateLimit]=None,
        alert_strategy: Optional[AlertStrategy]=None,
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
            if notification_channels is not None:
                kwargs['notification_channels'] = notification_channels
            if project is not None:
                kwargs['project'] = project
            if user_labels is not None:
                kwargs['user_labels'] = user_labels
            if aggregations is not None:
                kwargs['aggregations'] = aggregations
            if denominator_aggregations is not None:
                kwargs['denominator_aggregations'] = denominator_aggregations
            if trigger is not None:
                kwargs['trigger'] = trigger
            if condition_absent is not None:
                kwargs['condition_absent'] = condition_absent
            if condition_matched_log is not None:
                kwargs['condition_matched_log'] = condition_matched_log
            if condition_monitoring_query_language is not None:
                kwargs['condition_monitoring_query_language'] = condition_monitoring_query_language
            if condition_threshold is not None:
                kwargs['condition_threshold'] = condition_threshold
            if notification_rate_limit is not None:
                kwargs['notification_rate_limit'] = notification_rate_limit
            if alert_strategy is not None:
                kwargs['alert_strategy'] = alert_strategy
            if conditions is not None:
                kwargs['conditions'] = conditions
            if documentation is not None:
                kwargs['documentation'] = documentation
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
