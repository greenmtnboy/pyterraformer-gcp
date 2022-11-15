
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class CelExpressionItem():
        expression:str
        # non-optional-blocks
        description: Optional[str] = None
        location: Optional[str] = None
        title: Optional[str] = None
        
# wrapper list class
class CelExpression(BlockList):
        items: List[CelExpressionItem]




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
        critical:bool
        value:str
        # non-optional-blocks
        object_id: Optional[ObjectId]=None,
        
# wrapper list class
class AdditionalExtensions(BlockList):
        items: List[AdditionalExtensionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CaOptionsItem():
        # non-optional-blocks
        is_ca: Optional[bool] = None
        max_issuer_path_length: Optional[float] = None
        non_ca: Optional[bool] = None
        zero_max_issuer_path_length: Optional[bool] = None
        
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
class EllipticCurveItem():
        signature_algorithm:str
        # non-optional-blocks
        
# wrapper list class
class EllipticCurve(BlockList):
        items: List[EllipticCurveItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RsaItem():
        # non-optional-blocks
        max_modulus_size: Optional[str] = None
        min_modulus_size: Optional[str] = None
        
# wrapper list class
class Rsa(BlockList):
        items: List[RsaItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AllowedIssuanceModesItem():
        allow_config_based_issuance:bool
        allow_csr_based_issuance:bool
        # non-optional-blocks
        
# wrapper list class
class AllowedIssuanceModes(BlockList):
        items: List[AllowedIssuanceModesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AllowedKeyTypesItem():
        # non-optional-blocks
        elliptic_curve: Optional[EllipticCurve]=None,
        rsa: Optional[Rsa]=None,
        
# wrapper list class
class AllowedKeyTypes(BlockList):
        items: List[AllowedKeyTypesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class BaselineValuesItem():
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
class BaselineValues(BlockList):
        items: List[BaselineValuesItem]




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
class IssuancePolicyItem():
        # non-optional-blocks
        maximum_lifetime: Optional[str] = None
        cel_expression: Optional[CelExpression]=None,
        base_key_usage: Optional[BaseKeyUsage]=None,
        extended_key_usage: Optional[ExtendedKeyUsage]=None,
        unknown_extended_key_usages: Optional[UnknownExtendedKeyUsages]=None,
        object_id: Optional[ObjectId]=None,
        additional_extensions: Optional[AdditionalExtensions]=None,
        ca_options: Optional[CaOptions]=None,
        key_usage: Optional[KeyUsage]=None,
        policy_ids: Optional[PolicyIds]=None,
        elliptic_curve: Optional[EllipticCurve]=None,
        rsa: Optional[Rsa]=None,
        allowed_issuance_modes: Optional[AllowedIssuanceModes]=None,
        allowed_key_types: Optional[AllowedKeyTypes]=None,
        baseline_values: Optional[BaselineValues]=None,
        identity_constraints: Optional[IdentityConstraints]=None,
        
# wrapper list class
class IssuancePolicy(BlockList):
        items: List[IssuancePolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PublishingOptionsItem():
        publish_ca_cert:bool
        publish_crl:bool
        # non-optional-blocks
        
# wrapper list class
class PublishingOptions(BlockList):
        items: List[PublishingOptionsItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GooglePrivatecaCaPool(ResourceObject):
    """    
    Args:
        location (str): Location of the CaPool. A full list of valid locations can be found by
                    running 'gcloud privateca locations list'.
        name (str): The name for this CaPool.
        tier (str): The Tier of this CaPool. Possible values: ["ENTERPRISE", "DEVOPS"]
    """
    _type = 'google_privateca_ca_pool'
    
    def __init__(self,
        tf_id: str,
        location:str,
        name:str,
        tier:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        cel_expression: Optional[CelExpression]=None,
        base_key_usage: Optional[BaseKeyUsage]=None,
        extended_key_usage: Optional[ExtendedKeyUsage]=None,
        unknown_extended_key_usages: Optional[UnknownExtendedKeyUsages]=None,
        object_id: Optional[ObjectId]=None,
        additional_extensions: Optional[AdditionalExtensions]=None,
        ca_options: Optional[CaOptions]=None,
        key_usage: Optional[KeyUsage]=None,
        policy_ids: Optional[PolicyIds]=None,
        elliptic_curve: Optional[EllipticCurve]=None,
        rsa: Optional[Rsa]=None,
        allowed_issuance_modes: Optional[AllowedIssuanceModes]=None,
        allowed_key_types: Optional[AllowedKeyTypes]=None,
        baseline_values: Optional[BaselineValues]=None,
        identity_constraints: Optional[IdentityConstraints]=None,
        issuance_policy: Optional[IssuancePolicy]=None,
        publishing_options: Optional[PublishingOptions]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if location is not None:
                kwargs['location'] = location
            if name is not None:
                kwargs['name'] = name
            if tier is not None:
                kwargs['tier'] = tier
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if cel_expression is not None:
                kwargs['cel_expression'] = cel_expression
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
            if elliptic_curve is not None:
                kwargs['elliptic_curve'] = elliptic_curve
            if rsa is not None:
                kwargs['rsa'] = rsa
            if allowed_issuance_modes is not None:
                kwargs['allowed_issuance_modes'] = allowed_issuance_modes
            if allowed_key_types is not None:
                kwargs['allowed_key_types'] = allowed_key_types
            if baseline_values is not None:
                kwargs['baseline_values'] = baseline_values
            if identity_constraints is not None:
                kwargs['identity_constraints'] = identity_constraints
            if issuance_policy is not None:
                kwargs['issuance_policy'] = issuance_policy
            if publishing_options is not None:
                kwargs['publishing_options'] = publishing_options
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
