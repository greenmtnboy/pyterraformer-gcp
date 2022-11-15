
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleKmsSecretCiphertext(ResourceObject):
    """    
    Args:
        crypto_key (str): The full name of the CryptoKey that will be used to encrypt the provided plaintext.
                    Format: ''projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}/cryptoKeys/{{cryptoKey}}''
        plaintext (str): The plaintext to be encrypted.
    """
    _type = 'google_kms_secret_ciphertext'
    
    def __init__(self,
        tf_id: str,
        crypto_key:str,
        plaintext:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        additional_authenticated_data: Optional[str] = None,
        id: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if crypto_key is not None:
                kwargs['crypto_key'] = crypto_key
            if plaintext is not None:
                kwargs['plaintext'] = plaintext
            if additional_authenticated_data is not None:
                kwargs['additional_authenticated_data'] = additional_authenticated_data
            if id is not None:
                kwargs['id'] = id
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
