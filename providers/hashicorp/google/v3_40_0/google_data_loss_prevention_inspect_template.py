
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class HotwordRegexItem():
        pattern:str
        # non-optional-blocks
        group_indexes: Optional[List[float]] = None
        
# wrapper list class
class HotwordRegex(BlockList):
        items: List[HotwordRegexItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class LikelihoodAdjustmentItem():
        # non-optional-blocks
        fixed_likelihood: Optional[str] = None
        relative_likelihood: Optional[float] = None
        
# wrapper list class
class LikelihoodAdjustment(BlockList):
        items: List[LikelihoodAdjustmentItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ProximityItem():
        # non-optional-blocks
        window_after: Optional[float] = None
        window_before: Optional[float] = None
        
# wrapper list class
class Proximity(BlockList):
        items: List[ProximityItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class InfoTypesItem():
        name:str
        # non-optional-blocks
        
# wrapper list class
class InfoTypes(BlockList):
        items: List[InfoTypesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CloudStoragePathItem():
        path:str
        # non-optional-blocks
        
# wrapper list class
class CloudStoragePath(BlockList):
        items: List[CloudStoragePathItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WordListItem():
        words:List[str]
        # non-optional-blocks
        
# wrapper list class
class WordList(BlockList):
        items: List[WordListItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DictionaryItem():
        # non-optional-blocks
        cloud_storage_path: Optional[CloudStoragePath]=None,
        word_list: Optional[WordList]=None,
        
# wrapper list class
class Dictionary(BlockList):
        items: List[DictionaryItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ExcludeInfoTypesItem():
        # non-optional-blocks
        info_types: Optional[InfoTypes]=None,
        
# wrapper list class
class ExcludeInfoTypes(BlockList):
        items: List[ExcludeInfoTypesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RegexItem():
        pattern:str
        # non-optional-blocks
        group_indexes: Optional[List[float]] = None
        
# wrapper list class
class Regex(BlockList):
        items: List[RegexItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ExclusionRuleItem():
        matching_type:str
        # non-optional-blocks
        info_types: Optional[InfoTypes]=None,
        cloud_storage_path: Optional[CloudStoragePath]=None,
        word_list: Optional[WordList]=None,
        dictionary: Optional[Dictionary]=None,
        exclude_info_types: Optional[ExcludeInfoTypes]=None,
        regex: Optional[Regex]=None,
        
# wrapper list class
class ExclusionRule(BlockList):
        items: List[ExclusionRuleItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HotwordRuleItem():
        # non-optional-blocks
        hotword_regex: Optional[HotwordRegex]=None,
        likelihood_adjustment: Optional[LikelihoodAdjustment]=None,
        proximity: Optional[Proximity]=None,
        
# wrapper list class
class HotwordRule(BlockList):
        items: List[HotwordRuleItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RulesItem():
        # non-optional-blocks
        hotword_regex: Optional[HotwordRegex]=None,
        likelihood_adjustment: Optional[LikelihoodAdjustment]=None,
        proximity: Optional[Proximity]=None,
        info_types: Optional[InfoTypes]=None,
        cloud_storage_path: Optional[CloudStoragePath]=None,
        word_list: Optional[WordList]=None,
        dictionary: Optional[Dictionary]=None,
        exclude_info_types: Optional[ExcludeInfoTypes]=None,
        regex: Optional[Regex]=None,
        exclusion_rule: Optional[ExclusionRule]=None,
        hotword_rule: Optional[HotwordRule]=None,
        
# wrapper list class
class Rules(BlockList):
        items: List[RulesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class InfoTypeItem():
        name:str
        # non-optional-blocks
        
# wrapper list class
class InfoType(BlockList):
        items: List[InfoTypeItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MaxFindingsPerInfoTypeItem():
        max_findings:float
        # non-optional-blocks
        info_type: Optional[InfoType]=None,
        
# wrapper list class
class MaxFindingsPerInfoType(BlockList):
        items: List[MaxFindingsPerInfoTypeItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class LimitsItem():
        max_findings_per_item:float
        max_findings_per_request:float
        # non-optional-blocks
        info_type: Optional[InfoType]=None,
        max_findings_per_info_type: Optional[MaxFindingsPerInfoType]=None,
        
# wrapper list class
class Limits(BlockList):
        items: List[LimitsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RuleSetItem():
        # non-optional-blocks
        hotword_regex: Optional[HotwordRegex]=None,
        likelihood_adjustment: Optional[LikelihoodAdjustment]=None,
        proximity: Optional[Proximity]=None,
        info_types: Optional[InfoTypes]=None,
        cloud_storage_path: Optional[CloudStoragePath]=None,
        word_list: Optional[WordList]=None,
        dictionary: Optional[Dictionary]=None,
        exclude_info_types: Optional[ExcludeInfoTypes]=None,
        regex: Optional[Regex]=None,
        exclusion_rule: Optional[ExclusionRule]=None,
        hotword_rule: Optional[HotwordRule]=None,
        rules: Optional[Rules]=None,
        
# wrapper list class
class RuleSet(BlockList):
        items: List[RuleSetItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class InspectConfigItem():
        # non-optional-blocks
        content_options: Optional[List[str]] = None
        exclude_info_types: Optional[bool] = None
        include_quote: Optional[bool] = None
        min_likelihood: Optional[str] = None
        hotword_regex: Optional[HotwordRegex]=None,
        likelihood_adjustment: Optional[LikelihoodAdjustment]=None,
        proximity: Optional[Proximity]=None,
        info_types: Optional[InfoTypes]=None,
        cloud_storage_path: Optional[CloudStoragePath]=None,
        word_list: Optional[WordList]=None,
        dictionary: Optional[Dictionary]=None,
        exclude_info_types: Optional[ExcludeInfoTypes]=None,
        regex: Optional[Regex]=None,
        exclusion_rule: Optional[ExclusionRule]=None,
        hotword_rule: Optional[HotwordRule]=None,
        rules: Optional[Rules]=None,
        info_type: Optional[InfoType]=None,
        max_findings_per_info_type: Optional[MaxFindingsPerInfoType]=None,
        limits: Optional[Limits]=None,
        rule_set: Optional[RuleSet]=None,
        
# wrapper list class
class InspectConfig(BlockList):
        items: List[InspectConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleDataLossPreventionInspectTemplate(ResourceObject):
    """    
    Args:
        parent (str): The parent of the inspect template in any of the following formats:

                    * 'projects/{{project}}'
                    * 'projects/{{project}}/locations/{{location}}'
                    * 'organizations/{{organization_id}}'
                    * 'organizations/{{organization_id}}/locations/{{location}}'
    """
    _type = 'google_data_loss_prevention_inspect_template'
    
    def __init__(self,
        tf_id: str,
        parent:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        hotword_regex: Optional[HotwordRegex]=None,
        likelihood_adjustment: Optional[LikelihoodAdjustment]=None,
        proximity: Optional[Proximity]=None,
        info_types: Optional[InfoTypes]=None,
        cloud_storage_path: Optional[CloudStoragePath]=None,
        word_list: Optional[WordList]=None,
        dictionary: Optional[Dictionary]=None,
        exclude_info_types: Optional[ExcludeInfoTypes]=None,
        regex: Optional[Regex]=None,
        exclusion_rule: Optional[ExclusionRule]=None,
        hotword_rule: Optional[HotwordRule]=None,
        rules: Optional[Rules]=None,
        info_type: Optional[InfoType]=None,
        max_findings_per_info_type: Optional[MaxFindingsPerInfoType]=None,
        limits: Optional[Limits]=None,
        rule_set: Optional[RuleSet]=None,
        inspect_config: Optional[InspectConfig]=None,
        timeouts: Optional[Timeouts]=None,
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
            if hotword_regex is not None:
                kwargs['hotword_regex'] = hotword_regex
            if likelihood_adjustment is not None:
                kwargs['likelihood_adjustment'] = likelihood_adjustment
            if proximity is not None:
                kwargs['proximity'] = proximity
            if info_types is not None:
                kwargs['info_types'] = info_types
            if cloud_storage_path is not None:
                kwargs['cloud_storage_path'] = cloud_storage_path
            if word_list is not None:
                kwargs['word_list'] = word_list
            if dictionary is not None:
                kwargs['dictionary'] = dictionary
            if exclude_info_types is not None:
                kwargs['exclude_info_types'] = exclude_info_types
            if regex is not None:
                kwargs['regex'] = regex
            if exclusion_rule is not None:
                kwargs['exclusion_rule'] = exclusion_rule
            if hotword_rule is not None:
                kwargs['hotword_rule'] = hotword_rule
            if rules is not None:
                kwargs['rules'] = rules
            if info_type is not None:
                kwargs['info_type'] = info_type
            if max_findings_per_info_type is not None:
                kwargs['max_findings_per_info_type'] = max_findings_per_info_type
            if limits is not None:
                kwargs['limits'] = limits
            if rule_set is not None:
                kwargs['rule_set'] = rule_set
            if inspect_config is not None:
                kwargs['inspect_config'] = inspect_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
