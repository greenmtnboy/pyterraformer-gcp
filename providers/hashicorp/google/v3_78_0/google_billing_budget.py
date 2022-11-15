
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class SpecifiedAmountItem():
        # non-optional-blocks
        currency_code: Optional[str] = None
        nanos: Optional[float] = None
        units: Optional[str] = None
        
# wrapper list class
class SpecifiedAmount(BlockList):
        items: List[SpecifiedAmountItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AllUpdatesRuleItem():
        # non-optional-blocks
        disable_default_iam_recipients: Optional[bool] = None
        monitoring_notification_channels: Optional[List[str]] = None
        pubsub_topic: Optional[str] = None
        schema_version: Optional[str] = None
        
# wrapper list class
class AllUpdatesRule(BlockList):
        items: List[AllUpdatesRuleItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AmountItem():
        # non-optional-blocks
        last_period_amount: Optional[bool] = None
        specified_amount: Optional[SpecifiedAmount]=None,
        
# wrapper list class
class Amount(BlockList):
        items: List[AmountItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class BudgetFilterItem():
        # non-optional-blocks
        credit_types: Optional[List[str]] = None
        credit_types_treatment: Optional[str] = None
        labels: Optional[Dict[str, str]] = None
        projects: Optional[Set[str]] = None
        services: Optional[List[str]] = None
        subaccounts: Optional[List[str]] = None
        
# wrapper list class
class BudgetFilter(BlockList):
        items: List[BudgetFilterItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ThresholdRulesItem():
        threshold_percent:float
        # non-optional-blocks
        spend_basis: Optional[str] = None
        
# wrapper list class
class ThresholdRules(BlockList):
        items: List[ThresholdRulesItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleBillingBudget(ResourceObject):
    """    
    Args:
        billing_account (str): ID of the billing account to set a budget on.
    """
    _type = 'google_billing_budget'
    
    def __init__(self,
        tf_id: str,
        billing_account:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        specified_amount: Optional[SpecifiedAmount]=None,
        all_updates_rule: Optional[AllUpdatesRule]=None,
        amount: Optional[Amount]=None,
        budget_filter: Optional[BudgetFilter]=None,
        threshold_rules: Optional[ThresholdRules]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if billing_account is not None:
                kwargs['billing_account'] = billing_account
            if display_name is not None:
                kwargs['display_name'] = display_name
            if id is not None:
                kwargs['id'] = id
            if specified_amount is not None:
                kwargs['specified_amount'] = specified_amount
            if all_updates_rule is not None:
                kwargs['all_updates_rule'] = all_updates_rule
            if amount is not None:
                kwargs['amount'] = amount
            if budget_filter is not None:
                kwargs['budget_filter'] = budget_filter
            if threshold_rules is not None:
                kwargs['threshold_rules'] = threshold_rules
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
