
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class AdmissionWhitelistPatternsItem():
        # non-optional-blocks
        name_pattern: Optional[str] = None
        
# wrapper list class
class AdmissionWhitelistPatterns(BlockList):
        items: List[AdmissionWhitelistPatternsItem]





# this block can contain multiple items, items in a list are required
@dataclass 
class ClusterAdmissionRulesItem():
        cluster:str
        # non-optional-blocks
        enforcement_mode: Optional[str] = None
        evaluation_mode: Optional[str] = None
        require_attestations_by: Optional[Set[str]] = None
        
# wrapper list class
class ClusterAdmissionRules(BlockSet):
        items: Set[ClusterAdmissionRulesItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class DefaultAdmissionRuleItem():
        enforcement_mode:str
        evaluation_mode:str
        # non-optional-blocks
        require_attestations_by: Optional[Set[str]] = None
        
# wrapper list class
class DefaultAdmissionRule(BlockList):
        items: List[DefaultAdmissionRuleItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleBinaryAuthorizationPolicy(ResourceObject):
    """    
    Args:
    """
    _type = 'google_binary_authorization_policy'
    
    def __init__(self,
        tf_id: str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        global_policy_evaluation_mode: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        admission_whitelist_patterns: Optional[AdmissionWhitelistPatterns]=None,
        cluster_admission_rules: Optional[ClusterAdmissionRules]=None,
        default_admission_rule: Optional[DefaultAdmissionRule]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if description is not None:
                kwargs['description'] = description
            if global_policy_evaluation_mode is not None:
                kwargs['global_policy_evaluation_mode'] = global_policy_evaluation_mode
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if admission_whitelist_patterns is not None:
                kwargs['admission_whitelist_patterns'] = admission_whitelist_patterns
            if cluster_admission_rules is not None:
                kwargs['cluster_admission_rules'] = cluster_admission_rules
            if default_admission_rule is not None:
                kwargs['default_admission_rule'] = default_admission_rule
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
