
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
        is_ca:bool
        # non-optional-blocks
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
class SubjectItem():
        common_name:str
        organization:str
        # non-optional-blocks
        country_code: Optional[str] = None
        locality: Optional[str] = None
        organizational_unit: Optional[str] = None
        postal_code: Optional[str] = None
        province: Optional[str] = None
        street_address: Optional[str] = None
        
# wrapper list class
class Subject(BlockList):
        items: List[SubjectItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SubjectAltNameItem():
        # non-optional-blocks
        dns_names: Optional[List[str]] = None
        email_addresses: Optional[List[str]] = None
        ip_addresses: Optional[List[str]] = None
        uris: Optional[List[str]] = None
        
# wrapper list class
class SubjectAltName(BlockList):
        items: List[SubjectAltNameItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SubjectConfigItem():
        # non-optional-blocks
        subject: Optional[Subject]=None,
        subject_alt_name: Optional[SubjectAltName]=None,
        
# wrapper list class
class SubjectConfig(BlockList):
        items: List[SubjectConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class X509ConfigItem():
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
class X509Config(BlockList):
        items: List[X509ConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ConfigItem():
        # non-optional-blocks
        base_key_usage: Optional[BaseKeyUsage]=None,
        extended_key_usage: Optional[ExtendedKeyUsage]=None,
        unknown_extended_key_usages: Optional[UnknownExtendedKeyUsages]=None,
        object_id: Optional[ObjectId]=None,
        additional_extensions: Optional[AdditionalExtensions]=None,
        ca_options: Optional[CaOptions]=None,
        key_usage: Optional[KeyUsage]=None,
        policy_ids: Optional[PolicyIds]=None,
        subject: Optional[Subject]=None,
        subject_alt_name: Optional[SubjectAltName]=None,
        subject_config: Optional[SubjectConfig]=None,
        x509_config: Optional[X509Config]=None,
        
# wrapper list class
class Config(BlockList):
        items: List[ConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class KeySpecItem():
        # non-optional-blocks
        algorithm: Optional[str] = None
        cloud_kms_key_version: Optional[str] = None
        
# wrapper list class
class KeySpec(BlockList):
        items: List[KeySpecItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GooglePrivatecaCertificateAuthority(ResourceObject):
    """    
    Args:
        certificate_authority_id (str): The user provided Resource ID for this Certificate Authority.
        location (str): Location of the CertificateAuthority. A full list of valid locations can be found by
                    running 'gcloud privateca locations list'.
        pool (str): The name of the CaPool this Certificate Authority belongs to.
    """
    _type = 'google_privateca_certificate_authority'
    
    def __init__(self,
        tf_id: str,
        certificate_authority_id:str,
        location:str,
        pool:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        deletion_protection: Optional[bool] = None,
        desired_state: Optional[str] = None,
        gcs_bucket: Optional[str] = None,
        id: Optional[str] = None,
        ignore_active_certificates_on_deletion: Optional[bool] = None,
        labels: Optional[Dict[str, str]] = None,
        lifetime: Optional[str] = None,
        project: Optional[str] = None,
        type: Optional[str] = None,
        base_key_usage: Optional[BaseKeyUsage]=None,
        extended_key_usage: Optional[ExtendedKeyUsage]=None,
        unknown_extended_key_usages: Optional[UnknownExtendedKeyUsages]=None,
        object_id: Optional[ObjectId]=None,
        additional_extensions: Optional[AdditionalExtensions]=None,
        ca_options: Optional[CaOptions]=None,
        key_usage: Optional[KeyUsage]=None,
        policy_ids: Optional[PolicyIds]=None,
        subject: Optional[Subject]=None,
        subject_alt_name: Optional[SubjectAltName]=None,
        subject_config: Optional[SubjectConfig]=None,
        x509_config: Optional[X509Config]=None,
        config: Optional[Config]=None,
        key_spec: Optional[KeySpec]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if certificate_authority_id is not None:
                kwargs['certificate_authority_id'] = certificate_authority_id
            if location is not None:
                kwargs['location'] = location
            if pool is not None:
                kwargs['pool'] = pool
            if deletion_protection is not None:
                kwargs['deletion_protection'] = deletion_protection
            if desired_state is not None:
                kwargs['desired_state'] = desired_state
            if gcs_bucket is not None:
                kwargs['gcs_bucket'] = gcs_bucket
            if id is not None:
                kwargs['id'] = id
            if ignore_active_certificates_on_deletion is not None:
                kwargs['ignore_active_certificates_on_deletion'] = ignore_active_certificates_on_deletion
            if labels is not None:
                kwargs['labels'] = labels
            if lifetime is not None:
                kwargs['lifetime'] = lifetime
            if project is not None:
                kwargs['project'] = project
            if type is not None:
                kwargs['type'] = type
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
            if subject is not None:
                kwargs['subject'] = subject
            if subject_alt_name is not None:
                kwargs['subject_alt_name'] = subject_alt_name
            if subject_config is not None:
                kwargs['subject_config'] = subject_config
            if x509_config is not None:
                kwargs['x509_config'] = x509_config
            if config is not None:
                kwargs['config'] = config
            if key_spec is not None:
                kwargs['key_spec'] = key_spec
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
