
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass




# this block can contain multiple items, items in a list are required
@dataclass 
class SignaturesItem():
        public_key_id:str
        # non-optional-blocks
        signature: Optional[str] = None
        
# wrapper list class
class Signatures(BlockSet):
        items: Set[SignaturesItem]



# this block can contain multiple items, items in a list are required
@dataclass 
class AttestationItem():
        serialized_payload:str
        # non-optional-blocks
        signatures: Optional[Signatures]=None,
        
# wrapper list class
class Attestation(BlockList):
        items: List[AttestationItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleContainerAnalysisOccurrence(ResourceObject):
    """    
    Args:
        note_name (str): The analysis note associated with this occurrence, in the form of
                    projects/[PROJECT]/notes/[NOTE_ID]. This field can be used as a
                    filter in list requests.
        resource_uri (str): Required. Immutable. A URI that represents the resource for which
                    the occurrence applies. For example,
                    https://gcr.io/project/image@sha256:123abc for a Docker image.
    """
    _type = 'google_container_analysis_occurrence'
    
    def __init__(self,
        tf_id: str,
        note_name:str,
        resource_uri:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        remediation: Optional[str] = None,
        signatures: Optional[Signatures]=None,
        attestation: Optional[Attestation]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if note_name is not None:
                kwargs['note_name'] = note_name
            if resource_uri is not None:
                kwargs['resource_uri'] = resource_uri
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if remediation is not None:
                kwargs['remediation'] = remediation
            if signatures is not None:
                kwargs['signatures'] = signatures
            if attestation is not None:
                kwargs['attestation'] = attestation
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
