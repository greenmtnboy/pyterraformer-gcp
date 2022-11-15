
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class IdpCertificatesItem():
        # non-optional-blocks
        x509_certificate: Optional[str] = None
        
# wrapper list class
class IdpCertificates(BlockList):
        items: List[IdpCertificatesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class IdpConfigItem():
        idp_entity_id:str
        sso_url:str
        # non-optional-blocks
        sign_request: Optional[bool] = None
        idp_certificates: Optional[IdpCertificates]=None,
        
# wrapper list class
class IdpConfig(BlockList):
        items: List[IdpConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SpConfigItem():
        # non-optional-blocks
        callback_uri: Optional[str] = None
        sp_entity_id: Optional[str] = None
        
# wrapper list class
class SpConfig(BlockList):
        items: List[SpConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleIdentityPlatformInboundSamlConfig(ResourceObject):
    """    
    Args:
        display_name (str): Human friendly display name.
        name (str): The name of the InboundSamlConfig resource. Must start with 'saml.' and can only have alphanumeric characters,
                    hyphens, underscores or periods. The part after 'saml.' must also start with a lowercase letter, end with an
                    alphanumeric character, and have at least 2 characters.
    """
    _type = 'google_identity_platform_inbound_saml_config'
    
    def __init__(self,
        tf_id: str,
        display_name:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        enabled: Optional[bool] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        idp_certificates: Optional[IdpCertificates]=None,
        idp_config: Optional[IdpConfig]=None,
        sp_config: Optional[SpConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if display_name is not None:
                kwargs['display_name'] = display_name
            if name is not None:
                kwargs['name'] = name
            if enabled is not None:
                kwargs['enabled'] = enabled
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if idp_certificates is not None:
                kwargs['idp_certificates'] = idp_certificates
            if idp_config is not None:
                kwargs['idp_config'] = idp_config
            if sp_config is not None:
                kwargs['sp_config'] = sp_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
