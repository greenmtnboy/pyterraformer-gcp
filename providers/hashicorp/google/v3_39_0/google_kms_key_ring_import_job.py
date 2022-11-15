
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




class GoogleKmsKeyRingImportJob(ResourceObject):
    """    
    Args:
        import_job_id (str): It must be unique within a KeyRing and match the regular expression [a-zA-Z0-9_-]{1,63}
        import_method (str): The wrapping method to be used for incoming key material. Possible values: ["RSA_OAEP_3072_SHA1_AES_256", "RSA_OAEP_4096_SHA1_AES_256"]
        key_ring (str): The KeyRing that this import job belongs to.
                    Format: ''projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}''.
        protection_level (str): The protection level of the ImportJob. This must match the protectionLevel of the
                    versionTemplate on the CryptoKey you attempt to import into. Possible values: ["SOFTWARE", "HSM", "EXTERNAL"]
    """
    _type = 'google_kms_key_ring_import_job'
    
    def __init__(self,
        tf_id: str,
        import_job_id:str,
        import_method:str,
        key_ring:str,
        protection_level:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if import_job_id is not None:
                kwargs['import_job_id'] = import_job_id
            if import_method is not None:
                kwargs['import_method'] = import_method
            if key_ring is not None:
                kwargs['key_ring'] = key_ring
            if protection_level is not None:
                kwargs['protection_level'] = protection_level
            if id is not None:
                kwargs['id'] = id
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
