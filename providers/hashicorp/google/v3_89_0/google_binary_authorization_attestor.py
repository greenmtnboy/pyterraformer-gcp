
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class PkixPublicKeyItem():
        # non-optional-blocks
        public_key_pem: Optional[str] = None
        signature_algorithm: Optional[str] = None
        
# wrapper list class
class PkixPublicKey(BlockList):
        items: List[PkixPublicKeyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PublicKeysItem():
        # non-optional-blocks
        ascii_armored_pgp_public_key: Optional[str] = None
        comment: Optional[str] = None
        id: Optional[str] = None
        pkix_public_key: Optional[PkixPublicKey]=None,
        
# wrapper list class
class PublicKeys(BlockList):
        items: List[PublicKeysItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AttestationAuthorityNoteItem():
        note_reference:str
        # non-optional-blocks
        pkix_public_key: Optional[PkixPublicKey]=None,
        public_keys: Optional[PublicKeys]=None,
        
# wrapper list class
class AttestationAuthorityNote(BlockList):
        items: List[AttestationAuthorityNoteItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleBinaryAuthorizationAttestor(ResourceObject):
    """    
    Args:
        name (str): The resource name.
    """
    _type = 'google_binary_authorization_attestor'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        pkix_public_key: Optional[PkixPublicKey]=None,
        public_keys: Optional[PublicKeys]=None,
        attestation_authority_note: Optional[AttestationAuthorityNote]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if pkix_public_key is not None:
                kwargs['pkix_public_key'] = pkix_public_key
            if public_keys is not None:
                kwargs['public_keys'] = public_keys
            if attestation_authority_note is not None:
                kwargs['attestation_authority_note'] = attestation_authority_note
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
