
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass




# this block can contain multiple items, items in a list are required
@dataclass 
class AuditLogConfigItem():
        log_type:str
        # non-optional-blocks
        exempted_members: Optional[Set[str]] = None
        
# wrapper list class
class AuditLogConfig(BlockSet):
        items: Set[AuditLogConfigItem]



class GoogleProjectIamAuditConfig(ResourceObject):
    """    
    Args:
        service (str): 
    """
    _type = 'google_project_iam_audit_config'
    
    def __init__(self,
        tf_id: str,
        service:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        audit_log_config: Optional[AuditLogConfig]=None,
        ):
            kwargs = {}
            if service is not None:
                kwargs['service'] = service
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if audit_log_config is not None:
                kwargs['audit_log_config'] = audit_log_config
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
