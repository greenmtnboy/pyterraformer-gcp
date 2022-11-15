
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class RealmsSelectorItem():
        # non-optional-blocks
        realms: Optional[List[str]] = None
        
# wrapper list class
class RealmsSelector(BlockList):
        items: List[RealmsSelectorItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GameServerConfigOverridesItem():
        # non-optional-blocks
        config_version: Optional[str] = None
        realms_selector: Optional[RealmsSelector]=None,
        
# wrapper list class
class GameServerConfigOverrides(BlockList):
        items: List[GameServerConfigOverridesItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleGameServicesGameServerDeploymentRollout(ResourceObject):
    """    
    Args:
        default_game_server_config (str): This field points to the game server config that is
                    applied by default to all realms and clusters. For example,

                    'projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config'.
        deployment_id (str): The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.
    """
    _type = 'google_game_services_game_server_deployment_rollout'
    
    def __init__(self,
        tf_id: str,
        default_game_server_config:str,
        deployment_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        project: Optional[str] = None,
        realms_selector: Optional[RealmsSelector]=None,
        game_server_config_overrides: Optional[GameServerConfigOverrides]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if default_game_server_config is not None:
                kwargs['default_game_server_config'] = default_game_server_config
            if deployment_id is not None:
                kwargs['deployment_id'] = deployment_id
            if id is not None:
                kwargs['id'] = id
            if project is not None:
                kwargs['project'] = project
            if realms_selector is not None:
                kwargs['realms_selector'] = realms_selector
            if game_server_config_overrides is not None:
                kwargs['game_server_config_overrides'] = game_server_config_overrides
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
