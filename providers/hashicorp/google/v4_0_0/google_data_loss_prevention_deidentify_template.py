
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class DateValueItem():
        # non-optional-blocks
        day: Optional[float] = None
        month: Optional[float] = None
        year: Optional[float] = None
        
# wrapper list class
class DateValue(BlockList):
        items: List[DateValueItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TimeValueItem():
        # non-optional-blocks
        hours: Optional[float] = None
        minutes: Optional[float] = None
        nanos: Optional[float] = None
        seconds: Optional[float] = None
        
# wrapper list class
class TimeValue(BlockList):
        items: List[TimeValueItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class NewValueItem():
        # non-optional-blocks
        boolean_value: Optional[bool] = None
        day_of_week_value: Optional[str] = None
        float_value: Optional[float] = None
        integer_value: Optional[float] = None
        string_value: Optional[str] = None
        timestamp_value: Optional[str] = None
        date_value: Optional[DateValue]=None,
        time_value: Optional[TimeValue]=None,
        
# wrapper list class
class NewValue(BlockList):
        items: List[NewValueItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class KmsWrappedItem():
        crypto_key_name:str
        wrapped_key:str
        # non-optional-blocks
        
# wrapper list class
class KmsWrapped(BlockList):
        items: List[KmsWrappedItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TransientItem():
        name:str
        # non-optional-blocks
        
# wrapper list class
class Transient(BlockList):
        items: List[TransientItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class UnwrappedItem():
        key:str
        # non-optional-blocks
        
# wrapper list class
class Unwrapped(BlockList):
        items: List[UnwrappedItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ContextItem():
        # non-optional-blocks
        name: Optional[str] = None
        
# wrapper list class
class Context(BlockList):
        items: List[ContextItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CryptoKeyItem():
        # non-optional-blocks
        kms_wrapped: Optional[KmsWrapped]=None,
        transient: Optional[Transient]=None,
        unwrapped: Optional[Unwrapped]=None,
        
# wrapper list class
class CryptoKey(BlockList):
        items: List[CryptoKeyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SurrogateInfoTypeItem():
        # non-optional-blocks
        name: Optional[str] = None
        
# wrapper list class
class SurrogateInfoType(BlockList):
        items: List[SurrogateInfoTypeItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CharactersToIgnoreItem():
        # non-optional-blocks
        character_to_skip: Optional[str] = None
        common_characters_to_ignore: Optional[str] = None
        
# wrapper list class
class CharactersToIgnore(BlockList):
        items: List[CharactersToIgnoreItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CharacterMaskConfigItem():
        # non-optional-blocks
        masking_character: Optional[str] = None
        number_to_mask: Optional[float] = None
        reverse_order: Optional[bool] = None
        characters_to_ignore: Optional[CharactersToIgnore]=None,
        
# wrapper list class
class CharacterMaskConfig(BlockList):
        items: List[CharacterMaskConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CryptoDeterministicConfigItem():
        # non-optional-blocks
        kms_wrapped: Optional[KmsWrapped]=None,
        transient: Optional[Transient]=None,
        unwrapped: Optional[Unwrapped]=None,
        context: Optional[Context]=None,
        crypto_key: Optional[CryptoKey]=None,
        surrogate_info_type: Optional[SurrogateInfoType]=None,
        
# wrapper list class
class CryptoDeterministicConfig(BlockList):
        items: List[CryptoDeterministicConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CryptoReplaceFfxFpeConfigItem():
        # non-optional-blocks
        common_alphabet: Optional[str] = None
        custom_alphabet: Optional[str] = None
        radix: Optional[float] = None
        kms_wrapped: Optional[KmsWrapped]=None,
        transient: Optional[Transient]=None,
        unwrapped: Optional[Unwrapped]=None,
        context: Optional[Context]=None,
        crypto_key: Optional[CryptoKey]=None,
        surrogate_info_type: Optional[SurrogateInfoType]=None,
        
# wrapper list class
class CryptoReplaceFfxFpeConfig(BlockList):
        items: List[CryptoReplaceFfxFpeConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ReplaceConfigItem():
        # non-optional-blocks
        date_value: Optional[DateValue]=None,
        time_value: Optional[TimeValue]=None,
        new_value: Optional[NewValue]=None,
        
# wrapper list class
class ReplaceConfig(BlockList):
        items: List[ReplaceConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class InfoTypesItem():
        name:str
        # non-optional-blocks
        
# wrapper list class
class InfoTypes(BlockList):
        items: List[InfoTypesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PrimitiveTransformationItem():
        # non-optional-blocks
        replace_with_info_type_config: Optional[bool] = None
        date_value: Optional[DateValue]=None,
        time_value: Optional[TimeValue]=None,
        new_value: Optional[NewValue]=None,
        kms_wrapped: Optional[KmsWrapped]=None,
        transient: Optional[Transient]=None,
        unwrapped: Optional[Unwrapped]=None,
        context: Optional[Context]=None,
        crypto_key: Optional[CryptoKey]=None,
        surrogate_info_type: Optional[SurrogateInfoType]=None,
        characters_to_ignore: Optional[CharactersToIgnore]=None,
        character_mask_config: Optional[CharacterMaskConfig]=None,
        crypto_deterministic_config: Optional[CryptoDeterministicConfig]=None,
        crypto_replace_ffx_fpe_config: Optional[CryptoReplaceFfxFpeConfig]=None,
        replace_config: Optional[ReplaceConfig]=None,
        
# wrapper list class
class PrimitiveTransformation(BlockList):
        items: List[PrimitiveTransformationItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class TransformationsItem():
        # non-optional-blocks
        date_value: Optional[DateValue]=None,
        time_value: Optional[TimeValue]=None,
        new_value: Optional[NewValue]=None,
        kms_wrapped: Optional[KmsWrapped]=None,
        transient: Optional[Transient]=None,
        unwrapped: Optional[Unwrapped]=None,
        context: Optional[Context]=None,
        crypto_key: Optional[CryptoKey]=None,
        surrogate_info_type: Optional[SurrogateInfoType]=None,
        characters_to_ignore: Optional[CharactersToIgnore]=None,
        character_mask_config: Optional[CharacterMaskConfig]=None,
        crypto_deterministic_config: Optional[CryptoDeterministicConfig]=None,
        crypto_replace_ffx_fpe_config: Optional[CryptoReplaceFfxFpeConfig]=None,
        replace_config: Optional[ReplaceConfig]=None,
        info_types: Optional[InfoTypes]=None,
        primitive_transformation: Optional[PrimitiveTransformation]=None,
        
# wrapper list class
class Transformations(BlockList):
        items: List[TransformationsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class InfoTypeTransformationsItem():
        # non-optional-blocks
        date_value: Optional[DateValue]=None,
        time_value: Optional[TimeValue]=None,
        new_value: Optional[NewValue]=None,
        kms_wrapped: Optional[KmsWrapped]=None,
        transient: Optional[Transient]=None,
        unwrapped: Optional[Unwrapped]=None,
        context: Optional[Context]=None,
        crypto_key: Optional[CryptoKey]=None,
        surrogate_info_type: Optional[SurrogateInfoType]=None,
        characters_to_ignore: Optional[CharactersToIgnore]=None,
        character_mask_config: Optional[CharacterMaskConfig]=None,
        crypto_deterministic_config: Optional[CryptoDeterministicConfig]=None,
        crypto_replace_ffx_fpe_config: Optional[CryptoReplaceFfxFpeConfig]=None,
        replace_config: Optional[ReplaceConfig]=None,
        info_types: Optional[InfoTypes]=None,
        primitive_transformation: Optional[PrimitiveTransformation]=None,
        transformations: Optional[Transformations]=None,
        
# wrapper list class
class InfoTypeTransformations(BlockList):
        items: List[InfoTypeTransformationsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DeidentifyConfigItem():
        # non-optional-blocks
        date_value: Optional[DateValue]=None,
        time_value: Optional[TimeValue]=None,
        new_value: Optional[NewValue]=None,
        kms_wrapped: Optional[KmsWrapped]=None,
        transient: Optional[Transient]=None,
        unwrapped: Optional[Unwrapped]=None,
        context: Optional[Context]=None,
        crypto_key: Optional[CryptoKey]=None,
        surrogate_info_type: Optional[SurrogateInfoType]=None,
        characters_to_ignore: Optional[CharactersToIgnore]=None,
        character_mask_config: Optional[CharacterMaskConfig]=None,
        crypto_deterministic_config: Optional[CryptoDeterministicConfig]=None,
        crypto_replace_ffx_fpe_config: Optional[CryptoReplaceFfxFpeConfig]=None,
        replace_config: Optional[ReplaceConfig]=None,
        info_types: Optional[InfoTypes]=None,
        primitive_transformation: Optional[PrimitiveTransformation]=None,
        transformations: Optional[Transformations]=None,
        info_type_transformations: Optional[InfoTypeTransformations]=None,
        
# wrapper list class
class DeidentifyConfig(BlockList):
        items: List[DeidentifyConfigItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleDataLossPreventionDeidentifyTemplate(ResourceObject):
    """    
    Args:
        parent (str): The parent of the template in any of the following formats:

                    * 'projects/{{project}}'
                    * 'projects/{{project}}/locations/{{location}}'
                    * 'organizations/{{organization_id}}'
                    * 'organizations/{{organization_id}}/locations/{{location}}'
    """
    _type = 'google_data_loss_prevention_deidentify_template'
    
    def __init__(self,
        tf_id: str,
        parent:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        id: Optional[str] = None,
        date_value: Optional[DateValue]=None,
        time_value: Optional[TimeValue]=None,
        new_value: Optional[NewValue]=None,
        kms_wrapped: Optional[KmsWrapped]=None,
        transient: Optional[Transient]=None,
        unwrapped: Optional[Unwrapped]=None,
        context: Optional[Context]=None,
        crypto_key: Optional[CryptoKey]=None,
        surrogate_info_type: Optional[SurrogateInfoType]=None,
        characters_to_ignore: Optional[CharactersToIgnore]=None,
        character_mask_config: Optional[CharacterMaskConfig]=None,
        crypto_deterministic_config: Optional[CryptoDeterministicConfig]=None,
        crypto_replace_ffx_fpe_config: Optional[CryptoReplaceFfxFpeConfig]=None,
        replace_config: Optional[ReplaceConfig]=None,
        info_types: Optional[InfoTypes]=None,
        primitive_transformation: Optional[PrimitiveTransformation]=None,
        transformations: Optional[Transformations]=None,
        info_type_transformations: Optional[InfoTypeTransformations]=None,
        deidentify_config: Optional[DeidentifyConfig]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if parent is not None:
                kwargs['parent'] = parent
            if description is not None:
                kwargs['description'] = description
            if display_name is not None:
                kwargs['display_name'] = display_name
            if id is not None:
                kwargs['id'] = id
            if date_value is not None:
                kwargs['date_value'] = date_value
            if time_value is not None:
                kwargs['time_value'] = time_value
            if new_value is not None:
                kwargs['new_value'] = new_value
            if kms_wrapped is not None:
                kwargs['kms_wrapped'] = kms_wrapped
            if transient is not None:
                kwargs['transient'] = transient
            if unwrapped is not None:
                kwargs['unwrapped'] = unwrapped
            if context is not None:
                kwargs['context'] = context
            if crypto_key is not None:
                kwargs['crypto_key'] = crypto_key
            if surrogate_info_type is not None:
                kwargs['surrogate_info_type'] = surrogate_info_type
            if characters_to_ignore is not None:
                kwargs['characters_to_ignore'] = characters_to_ignore
            if character_mask_config is not None:
                kwargs['character_mask_config'] = character_mask_config
            if crypto_deterministic_config is not None:
                kwargs['crypto_deterministic_config'] = crypto_deterministic_config
            if crypto_replace_ffx_fpe_config is not None:
                kwargs['crypto_replace_ffx_fpe_config'] = crypto_replace_ffx_fpe_config
            if replace_config is not None:
                kwargs['replace_config'] = replace_config
            if info_types is not None:
                kwargs['info_types'] = info_types
            if primitive_transformation is not None:
                kwargs['primitive_transformation'] = primitive_transformation
            if transformations is not None:
                kwargs['transformations'] = transformations
            if info_type_transformations is not None:
                kwargs['info_type_transformations'] = info_type_transformations
            if deidentify_config is not None:
                kwargs['deidentify_config'] = deidentify_config
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
