
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class BaseKeyUsageItem():
        # non-optional-blocks
        cert_sign: Optional[bool] = None
        content_commitment: Optional[bool] = None
        crl_sign: Optional[bool] = None
        data_encipherment: Optional[bool] = None
        decipher_only: Optional[bool] = None
        digital_signature: Optional[bool] = None
        encipher_only: Optional[bool] = None
        key_agreement: Optional[bool] = None
        key_encipherment: Optional[bool] = None
        
# wrapper list class
class BaseKeyUsage(BlockList):
        items: List[BaseKeyUsageItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ExtendedKeyUsageItem():
        # non-optional-blocks
        client_auth: Optional[bool] = None
        code_signing: Optional[bool] = None
        email_protection: Optional[bool] = None
        ocsp_signing: Optional[bool] = None
        server_auth: Optional[bool] = None
        time_stamping: Optional[bool] = None
        
# wrapper list class
class ExtendedKeyUsage(BlockList):
        items: List[ExtendedKeyUsageItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class UnknownExtendedKeyUsagesItem():
        object_id_path:List[float]
        # non-optional-blocks
        
# wrapper list class
class UnknownExtendedKeyUsages(BlockList):
        items: List[UnknownExtendedKeyUsagesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ObjectIdItem():
        object_id_path:List[float]
        # non-optional-blocks
        
# wrapper list class
class ObjectId(BlockList):
        items: List[ObjectIdItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AdditionalExtensionsItem():
        object_id_path:List[float]
        # non-optional-blocks
        
# wrapper list class
class AdditionalExtensions(BlockList):
        items: List[AdditionalExtensionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CaOptionsItem():
        # non-optional-blocks
        is_ca: Optional[bool] = None
        max_issuer_path_length: Optional[float] = None
        
# wrapper list class
class CaOptions(BlockList):
        items: List[CaOptionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class KeyUsageItem():
        # non-optional-blocks
        base_key_usage: Optional[BaseKeyUsage]=None,
        extended_key_usage: Optional[ExtendedKeyUsage]=None,
        unknown_extended_key_usages: Optional[UnknownExtendedKeyUsages]=None,
        
# wrapper list class
class KeyUsage(BlockList):
        items: List[KeyUsageItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PolicyIdsItem():
        object_id_path:List[float]
        # non-optional-blocks
        
# wrapper list class
class PolicyIds(BlockList):
        items: List[PolicyIdsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CelExpressionItem():
        # non-optional-blocks
        description: Optional[str] = None
        expression: Optional[str] = None
        location: Optional[str] = None
        title: Optional[str] = None
        
# wrapper list class
class CelExpression(BlockList):
        items: List[CelExpressionItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class IdentityConstraintsItem():
        allow_subject_alt_names_passthrough:bool
        allow_subject_passthrough:bool
        # non-optional-blocks
        cel_expression: Optional[CelExpression]=None,
        
# wrapper list class
class IdentityConstraints(BlockList):
        items: List[IdentityConstraintsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PassthroughExtensionsItem():
        # non-optional-blocks
        known_extensions: Optional[List[str]] = None
        additional_extensions: Optional[AdditionalExtensions]=None,
        
# wrapper list class
class PassthroughExtensions(BlockList):
        items: List[PassthroughExtensionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PredefinedValuesItem():
        # non-optional-blocks
        aia_ocsp_servers: Optional[List[str]] = None
        base_key_usage: Optional[BaseKeyUsage]=None,
        extended_key_usage: Optional[ExtendedKeyUsage]=None,
        unknown_extended_key_usages: Optional[UnknownExtendedKeyUsages]=None,
        object_id: Optional[ObjectId]=None,
        additional_extensions: Optional[AdditionalExtensions]=None,
        ca_options: Optional[CaOptions]=None,
        key_usage: Optional[KeyUsage]=None,
        policy_ids: Optional[PolicyIds]=None,
        
# wrapper list class
class PredefinedValues(BlockList):
        items: List[PredefinedValuesItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GooglePrivatecaCertificateTemplate(ResourceObject):
    """    
    Args:
        location (str): The location for the resource
        name (str): The resource name for this CertificateTemplate in the format `projects/*/locations/*/certificateTemplates/*`.
    """
    _type = 'google_privateca_certificate_template'
    
    def __init__(self,
        tf_id: str,
        location:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        base_key_usage: Optional[BaseKeyUsage]=None,
        extended_key_usage: Optional[ExtendedKeyUsage]=None,
        unknown_extended_key_usages: Optional[UnknownExtendedKeyUsages]=None,
        object_id: Optional[ObjectId]=None,
        additional_extensions: Optional[AdditionalExtensions]=None,
        ca_options: Optional[CaOptions]=None,
        key_usage: Optional[KeyUsage]=None,
        policy_ids: Optional[PolicyIds]=None,
        cel_expression: Optional[CelExpression]=None,
        identity_constraints: Optional[IdentityConstraints]=None,
        passthrough_extensions: Optional[PassthroughExtensions]=None,
        predefined_values: Optional[PredefinedValues]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if location is not None:
                kwargs['location'] = location
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if base_key_usage is not None:
                kwargs['base_key_usage'] = base_key_usage
            if extended_key_usage is not None:
                kwargs['extended_key_usage'] = extended_key_usage
            if unknown_extended_key_usages is not None:
                kwargs['unknown_extended_key_usages'] = unknown_extended_key_usages
            if object_id is not None:
                kwargs['object_id'] = object_id
            if additional_extensions is not None:
                kwargs['additional_extensions'] = additional_extensions
            if ca_options is not None:
                kwargs['ca_options'] = ca_options
            if key_usage is not None:
                kwargs['key_usage'] = key_usage
            if policy_ids is not None:
                kwargs['policy_ids'] = policy_ids
            if cel_expression is not None:
                kwargs['cel_expression'] = cel_expression
            if identity_constraints is not None:
                kwargs['identity_constraints'] = identity_constraints
            if passthrough_extensions is not None:
                kwargs['passthrough_extensions'] = passthrough_extensions
            if predefined_values is not None:
                kwargs['predefined_values'] = predefined_values
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
