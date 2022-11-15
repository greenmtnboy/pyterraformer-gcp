
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



class GoogleOrganizationIamAuditConfig(ResourceObject):
    """    
    Args:
        org_id (str): The numeric ID of the organization in which you want to manage the audit logging config.
        service (str): Service which will be enabled for audit logging. The special value allServices covers all services.
    """
    _type = 'google_organization_iam_audit_config'
    
    def __init__(self,
        tf_id: str,
        org_id:str,
        service:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        audit_log_config: Optional[AuditLogConfig]=None,
        ):
            kwargs = {}
            if org_id is not None:
                kwargs['org_id'] = org_id
            if service is not None:
                kwargs['service'] = service
            if id is not None:
                kwargs['id'] = id
            if audit_log_config is not None:
                kwargs['audit_log_config'] = audit_log_config
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
