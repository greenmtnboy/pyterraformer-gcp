
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class SchedulesItem():
        # non-optional-blocks
        cron_job_duration: Optional[str] = None
        cron_spec: Optional[str] = None
        end_time: Optional[str] = None
        start_time: Optional[str] = None
        
# wrapper list class
class Schedules(BlockList):
        items: List[SchedulesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SelectorsItem():
        # non-optional-blocks
        labels: Optional[Dict[str, str]] = None
        
# wrapper list class
class Selectors(BlockList):
        items: List[SelectorsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class FleetConfigsItem():
        fleet_spec:str
        # non-optional-blocks
        name: Optional[str] = None
        
# wrapper list class
class FleetConfigs(BlockList):
        items: List[FleetConfigsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ScalingConfigsItem():
        fleet_autoscaler_spec:str
        name:str
        # non-optional-blocks
        schedules: Optional[Schedules]=None,
        selectors: Optional[Selectors]=None,
        
# wrapper list class
class ScalingConfigs(BlockList):
        items: List[ScalingConfigsItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleGameServicesGameServerConfig(ResourceObject):
    """    
    Args:
        config_id (str): A unique id for the deployment config.
        deployment_id (str): A unique id for the deployment.
    """
    _type = 'google_game_services_game_server_config'
    
    def __init__(self,
        tf_id: str,
        config_id:str,
        deployment_id:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        location: Optional[str] = None,
        project: Optional[str] = None,
        schedules: Optional[Schedules]=None,
        selectors: Optional[Selectors]=None,
        fleet_configs: Optional[FleetConfigs]=None,
        scaling_configs: Optional[ScalingConfigs]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if config_id is not None:
                kwargs['config_id'] = config_id
            if deployment_id is not None:
                kwargs['deployment_id'] = deployment_id
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if location is not None:
                kwargs['location'] = location
            if project is not None:
                kwargs['project'] = project
            if schedules is not None:
                kwargs['schedules'] = schedules
            if selectors is not None:
                kwargs['selectors'] = selectors
            if fleet_configs is not None:
                kwargs['fleet_configs'] = fleet_configs
            if scaling_configs is not None:
                kwargs['scaling_configs'] = scaling_configs
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
