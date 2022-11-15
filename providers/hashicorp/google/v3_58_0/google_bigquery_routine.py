
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class ArgumentsItem():
        # non-optional-blocks
        argument_kind: Optional[str] = None
        data_type: Optional[str] = None
        mode: Optional[str] = None
        name: Optional[str] = None
        
# wrapper list class
class Arguments(BlockList):
        items: List[ArgumentsItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleBigqueryRoutine(ResourceObject):
    """    
    Args:
        dataset_id (str): The ID of the dataset containing this routine
        definition_body (str): The body of the routine. For functions, this is the expression in the AS clause.
                    If language=SQL, it is the substring inside (but excluding) the parentheses.
        routine_id (str): The ID of the the routine. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 256 characters.
    """
    _type = 'google_bigquery_routine'
    
    def __init__(self,
        tf_id: str,
        dataset_id:str,
        definition_body:str,
        routine_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        determinism_level: Optional[str] = None,
        id: Optional[str] = None,
        imported_libraries: Optional[List[str]] = None,
        language: Optional[str] = None,
        project: Optional[str] = None,
        return_type: Optional[str] = None,
        routine_type: Optional[str] = None,
        arguments: Optional[Arguments]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if dataset_id is not None:
                kwargs['dataset_id'] = dataset_id
            if definition_body is not None:
                kwargs['definition_body'] = definition_body
            if routine_id is not None:
                kwargs['routine_id'] = routine_id
            if description is not None:
                kwargs['description'] = description
            if determinism_level is not None:
                kwargs['determinism_level'] = determinism_level
            if id is not None:
                kwargs['id'] = id
            if imported_libraries is not None:
                kwargs['imported_libraries'] = imported_libraries
            if language is not None:
                kwargs['language'] = language
            if project is not None:
                kwargs['project'] = project
            if return_type is not None:
                kwargs['return_type'] = return_type
            if routine_type is not None:
                kwargs['routine_type'] = routine_type
            if arguments is not None:
                kwargs['arguments'] = arguments
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
