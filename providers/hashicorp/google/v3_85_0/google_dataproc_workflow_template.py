
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class AcceleratorsItem():
        # non-optional-blocks
        accelerator_count: Optional[float] = None
        accelerator_type: Optional[str] = None
        
# wrapper list class
class Accelerators(BlockList):
        items: List[AcceleratorsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class DiskConfigItem():
        # non-optional-blocks
        boot_disk_size_gb: Optional[float] = None
        boot_disk_type: Optional[str] = None
        num_local_ssds: Optional[float] = None
        
# wrapper list class
class DiskConfig(BlockList):
        items: List[DiskConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class KerberosConfigItem():
        # non-optional-blocks
        cross_realm_trust_admin_server: Optional[str] = None
        cross_realm_trust_kdc: Optional[str] = None
        cross_realm_trust_realm: Optional[str] = None
        cross_realm_trust_shared_password: Optional[str] = None
        enable_kerberos: Optional[bool] = None
        kdc_db_key: Optional[str] = None
        key_password: Optional[str] = None
        keystore: Optional[str] = None
        keystore_password: Optional[str] = None
        kms_key: Optional[str] = None
        realm: Optional[str] = None
        root_principal_password: Optional[str] = None
        tgt_lifetime_hours: Optional[float] = None
        truststore: Optional[str] = None
        truststore_password: Optional[str] = None
        
# wrapper list class
class KerberosConfig(BlockList):
        items: List[KerberosConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class NodeGroupAffinityItem():
        node_group:str
        # non-optional-blocks
        
# wrapper list class
class NodeGroupAffinity(BlockList):
        items: List[NodeGroupAffinityItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ReservationAffinityItem():
        # non-optional-blocks
        consume_reservation_type: Optional[str] = None
        key: Optional[str] = None
        values: Optional[List[str]] = None
        
# wrapper list class
class ReservationAffinity(BlockList):
        items: List[ReservationAffinityItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class AutoscalingConfigItem():
        # non-optional-blocks
        policy: Optional[str] = None
        
# wrapper list class
class AutoscalingConfig(BlockList):
        items: List[AutoscalingConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class EncryptionConfigItem():
        # non-optional-blocks
        gce_pd_kms_key_name: Optional[str] = None
        
# wrapper list class
class EncryptionConfig(BlockList):
        items: List[EncryptionConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class EndpointConfigItem():
        # non-optional-blocks
        enable_http_port_access: Optional[bool] = None
        
# wrapper list class
class EndpointConfig(BlockList):
        items: List[EndpointConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class GceClusterConfigItem():
        # non-optional-blocks
        internal_ip_only: Optional[bool] = None
        metadata: Optional[Dict[str, str]] = None
        network: Optional[str] = None
        private_ipv6_google_access: Optional[str] = None
        service_account: Optional[str] = None
        service_account_scopes: Optional[List[str]] = None
        subnetwork: Optional[str] = None
        tags: Optional[Set[str]] = None
        zone: Optional[str] = None
        node_group_affinity: Optional[NodeGroupAffinity]=None,
        reservation_affinity: Optional[ReservationAffinity]=None,
        
# wrapper list class
class GceClusterConfig(BlockList):
        items: List[GceClusterConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class InitializationActionsItem():
        # non-optional-blocks
        executable_file: Optional[str] = None
        execution_timeout: Optional[str] = None
        
# wrapper list class
class InitializationActions(BlockList):
        items: List[InitializationActionsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class LifecycleConfigItem():
        # non-optional-blocks
        auto_delete_time: Optional[str] = None
        auto_delete_ttl: Optional[str] = None
        idle_delete_ttl: Optional[str] = None
        
# wrapper list class
class LifecycleConfig(BlockList):
        items: List[LifecycleConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MasterConfigItem():
        # non-optional-blocks
        image: Optional[str] = None
        machine_type: Optional[str] = None
        min_cpu_platform: Optional[str] = None
        num_instances: Optional[float] = None
        preemptibility: Optional[str] = None
        accelerators: Optional[Accelerators]=None,
        disk_config: Optional[DiskConfig]=None,
        
# wrapper list class
class MasterConfig(BlockList):
        items: List[MasterConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SecondaryWorkerConfigItem():
        # non-optional-blocks
        image: Optional[str] = None
        machine_type: Optional[str] = None
        min_cpu_platform: Optional[str] = None
        num_instances: Optional[float] = None
        preemptibility: Optional[str] = None
        accelerators: Optional[Accelerators]=None,
        disk_config: Optional[DiskConfig]=None,
        
# wrapper list class
class SecondaryWorkerConfig(BlockList):
        items: List[SecondaryWorkerConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SecurityConfigItem():
        # non-optional-blocks
        kerberos_config: Optional[KerberosConfig]=None,
        
# wrapper list class
class SecurityConfig(BlockList):
        items: List[SecurityConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SoftwareConfigItem():
        # non-optional-blocks
        image_version: Optional[str] = None
        properties: Optional[Dict[str, str]] = None
        
# wrapper list class
class SoftwareConfig(BlockList):
        items: List[SoftwareConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class WorkerConfigItem():
        # non-optional-blocks
        image: Optional[str] = None
        machine_type: Optional[str] = None
        min_cpu_platform: Optional[str] = None
        num_instances: Optional[float] = None
        preemptibility: Optional[str] = None
        accelerators: Optional[Accelerators]=None,
        disk_config: Optional[DiskConfig]=None,
        
# wrapper list class
class WorkerConfig(BlockList):
        items: List[WorkerConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ConfigItem():
        # non-optional-blocks
        staging_bucket: Optional[str] = None
        temp_bucket: Optional[str] = None
        accelerators: Optional[Accelerators]=None,
        disk_config: Optional[DiskConfig]=None,
        kerberos_config: Optional[KerberosConfig]=None,
        node_group_affinity: Optional[NodeGroupAffinity]=None,
        reservation_affinity: Optional[ReservationAffinity]=None,
        autoscaling_config: Optional[AutoscalingConfig]=None,
        encryption_config: Optional[EncryptionConfig]=None,
        endpoint_config: Optional[EndpointConfig]=None,
        gce_cluster_config: Optional[GceClusterConfig]=None,
        initialization_actions: Optional[InitializationActions]=None,
        lifecycle_config: Optional[LifecycleConfig]=None,
        master_config: Optional[MasterConfig]=None,
        secondary_worker_config: Optional[SecondaryWorkerConfig]=None,
        security_config: Optional[SecurityConfig]=None,
        software_config: Optional[SoftwareConfig]=None,
        worker_config: Optional[WorkerConfig]=None,
        
# wrapper list class
class Config(BlockList):
        items: List[ConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ClusterSelectorItem():
        cluster_labels:Dict[str, str]
        # non-optional-blocks
        zone: Optional[str] = None
        
# wrapper list class
class ClusterSelector(BlockList):
        items: List[ClusterSelectorItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ManagedClusterItem():
        cluster_name:str
        # non-optional-blocks
        labels: Optional[Dict[str, str]] = None
        accelerators: Optional[Accelerators]=None,
        disk_config: Optional[DiskConfig]=None,
        kerberos_config: Optional[KerberosConfig]=None,
        node_group_affinity: Optional[NodeGroupAffinity]=None,
        reservation_affinity: Optional[ReservationAffinity]=None,
        autoscaling_config: Optional[AutoscalingConfig]=None,
        encryption_config: Optional[EncryptionConfig]=None,
        endpoint_config: Optional[EndpointConfig]=None,
        gce_cluster_config: Optional[GceClusterConfig]=None,
        initialization_actions: Optional[InitializationActions]=None,
        lifecycle_config: Optional[LifecycleConfig]=None,
        master_config: Optional[MasterConfig]=None,
        secondary_worker_config: Optional[SecondaryWorkerConfig]=None,
        security_config: Optional[SecurityConfig]=None,
        software_config: Optional[SoftwareConfig]=None,
        worker_config: Optional[WorkerConfig]=None,
        config: Optional[Config]=None,
        
# wrapper list class
class ManagedCluster(BlockList):
        items: List[ManagedClusterItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RegexItem():
        regexes:List[str]
        # non-optional-blocks
        
# wrapper list class
class Regex(BlockList):
        items: List[RegexItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ValuesItem():
        values:List[str]
        # non-optional-blocks
        
# wrapper list class
class Values(BlockList):
        items: List[ValuesItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ValidationItem():
        # non-optional-blocks
        regex: Optional[Regex]=None,
        values: Optional[Values]=None,
        
# wrapper list class
class Validation(BlockList):
        items: List[ValidationItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class LoggingConfigItem():
        # non-optional-blocks
        driver_log_levels: Optional[Dict[str, str]] = None
        
# wrapper list class
class LoggingConfig(BlockList):
        items: List[LoggingConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class QueryListItem():
        queries:List[str]
        # non-optional-blocks
        
# wrapper list class
class QueryList(BlockList):
        items: List[QueryListItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HadoopJobItem():
        # non-optional-blocks
        archive_uris: Optional[List[str]] = None
        args: Optional[List[str]] = None
        file_uris: Optional[List[str]] = None
        jar_file_uris: Optional[List[str]] = None
        main_class: Optional[str] = None
        main_jar_file_uri: Optional[str] = None
        properties: Optional[Dict[str, str]] = None
        logging_config: Optional[LoggingConfig]=None,
        
# wrapper list class
class HadoopJob(BlockList):
        items: List[HadoopJobItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HiveJobItem():
        # non-optional-blocks
        continue_on_failure: Optional[bool] = None
        jar_file_uris: Optional[List[str]] = None
        properties: Optional[Dict[str, str]] = None
        query_file_uri: Optional[str] = None
        script_variables: Optional[Dict[str, str]] = None
        query_list: Optional[QueryList]=None,
        
# wrapper list class
class HiveJob(BlockList):
        items: List[HiveJobItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PigJobItem():
        # non-optional-blocks
        continue_on_failure: Optional[bool] = None
        jar_file_uris: Optional[List[str]] = None
        properties: Optional[Dict[str, str]] = None
        query_file_uri: Optional[str] = None
        script_variables: Optional[Dict[str, str]] = None
        logging_config: Optional[LoggingConfig]=None,
        query_list: Optional[QueryList]=None,
        
# wrapper list class
class PigJob(BlockList):
        items: List[PigJobItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PrestoJobItem():
        # non-optional-blocks
        client_tags: Optional[List[str]] = None
        continue_on_failure: Optional[bool] = None
        output_format: Optional[str] = None
        properties: Optional[Dict[str, str]] = None
        query_file_uri: Optional[str] = None
        logging_config: Optional[LoggingConfig]=None,
        query_list: Optional[QueryList]=None,
        
# wrapper list class
class PrestoJob(BlockList):
        items: List[PrestoJobItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PysparkJobItem():
        main_python_file_uri:str
        # non-optional-blocks
        archive_uris: Optional[List[str]] = None
        args: Optional[List[str]] = None
        file_uris: Optional[List[str]] = None
        jar_file_uris: Optional[List[str]] = None
        properties: Optional[Dict[str, str]] = None
        python_file_uris: Optional[List[str]] = None
        logging_config: Optional[LoggingConfig]=None,
        
# wrapper list class
class PysparkJob(BlockList):
        items: List[PysparkJobItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SchedulingItem():
        # non-optional-blocks
        max_failures_per_hour: Optional[float] = None
        max_failures_total: Optional[float] = None
        
# wrapper list class
class Scheduling(BlockList):
        items: List[SchedulingItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SparkJobItem():
        # non-optional-blocks
        archive_uris: Optional[List[str]] = None
        args: Optional[List[str]] = None
        file_uris: Optional[List[str]] = None
        jar_file_uris: Optional[List[str]] = None
        main_class: Optional[str] = None
        main_jar_file_uri: Optional[str] = None
        properties: Optional[Dict[str, str]] = None
        logging_config: Optional[LoggingConfig]=None,
        
# wrapper list class
class SparkJob(BlockList):
        items: List[SparkJobItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SparkRJobItem():
        main_r_file_uri:str
        # non-optional-blocks
        archive_uris: Optional[List[str]] = None
        args: Optional[List[str]] = None
        file_uris: Optional[List[str]] = None
        properties: Optional[Dict[str, str]] = None
        logging_config: Optional[LoggingConfig]=None,
        
# wrapper list class
class SparkRJob(BlockList):
        items: List[SparkRJobItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SparkSqlJobItem():
        # non-optional-blocks
        jar_file_uris: Optional[List[str]] = None
        properties: Optional[Dict[str, str]] = None
        query_file_uri: Optional[str] = None
        script_variables: Optional[Dict[str, str]] = None
        logging_config: Optional[LoggingConfig]=None,
        query_list: Optional[QueryList]=None,
        
# wrapper list class
class SparkSqlJob(BlockList):
        items: List[SparkSqlJobItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class JobsItem():
        step_id:str
        # non-optional-blocks
        labels: Optional[Dict[str, str]] = None
        prerequisite_step_ids: Optional[List[str]] = None
        logging_config: Optional[LoggingConfig]=None,
        query_list: Optional[QueryList]=None,
        hadoop_job: Optional[HadoopJob]=None,
        hive_job: Optional[HiveJob]=None,
        pig_job: Optional[PigJob]=None,
        presto_job: Optional[PrestoJob]=None,
        pyspark_job: Optional[PysparkJob]=None,
        scheduling: Optional[Scheduling]=None,
        spark_job: Optional[SparkJob]=None,
        spark_r_job: Optional[SparkRJob]=None,
        spark_sql_job: Optional[SparkSqlJob]=None,
        
# wrapper list class
class Jobs(BlockList):
        items: List[JobsItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ParametersItem():
        fields:List[str]
        name:str
        # non-optional-blocks
        description: Optional[str] = None
        regex: Optional[Regex]=None,
        values: Optional[Values]=None,
        validation: Optional[Validation]=None,
        
# wrapper list class
class Parameters(BlockList):
        items: List[ParametersItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PlacementItem():
        # non-optional-blocks
        accelerators: Optional[Accelerators]=None,
        disk_config: Optional[DiskConfig]=None,
        kerberos_config: Optional[KerberosConfig]=None,
        node_group_affinity: Optional[NodeGroupAffinity]=None,
        reservation_affinity: Optional[ReservationAffinity]=None,
        autoscaling_config: Optional[AutoscalingConfig]=None,
        encryption_config: Optional[EncryptionConfig]=None,
        endpoint_config: Optional[EndpointConfig]=None,
        gce_cluster_config: Optional[GceClusterConfig]=None,
        initialization_actions: Optional[InitializationActions]=None,
        lifecycle_config: Optional[LifecycleConfig]=None,
        master_config: Optional[MasterConfig]=None,
        secondary_worker_config: Optional[SecondaryWorkerConfig]=None,
        security_config: Optional[SecurityConfig]=None,
        software_config: Optional[SoftwareConfig]=None,
        worker_config: Optional[WorkerConfig]=None,
        config: Optional[Config]=None,
        cluster_selector: Optional[ClusterSelector]=None,
        managed_cluster: Optional[ManagedCluster]=None,
        
# wrapper list class
class Placement(BlockList):
        items: List[PlacementItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None




class GoogleDataprocWorkflowTemplate(ResourceObject):
    """    
    Args:
        location (str): The location for the resource
        name (str): Output only. The resource name of the workflow template, as described in https://cloud.google.com/apis/design/resource_names. * For `projects.regions.workflowTemplates`, the resource name of the template has the following format: `projects/{project_id}/regions/{region}/workflowTemplates/{template_id}` * For `projects.locations.workflowTemplates`, the resource name of the template has the following format: `projects/{project_id}/locations/{location}/workflowTemplates/{template_id}`
    """
    _type = 'google_dataproc_workflow_template'
    
    def __init__(self,
        tf_id: str,
        location:str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        version: Optional[float] = None,
        accelerators: Optional[Accelerators]=None,
        disk_config: Optional[DiskConfig]=None,
        kerberos_config: Optional[KerberosConfig]=None,
        node_group_affinity: Optional[NodeGroupAffinity]=None,
        reservation_affinity: Optional[ReservationAffinity]=None,
        autoscaling_config: Optional[AutoscalingConfig]=None,
        encryption_config: Optional[EncryptionConfig]=None,
        endpoint_config: Optional[EndpointConfig]=None,
        gce_cluster_config: Optional[GceClusterConfig]=None,
        initialization_actions: Optional[InitializationActions]=None,
        lifecycle_config: Optional[LifecycleConfig]=None,
        master_config: Optional[MasterConfig]=None,
        secondary_worker_config: Optional[SecondaryWorkerConfig]=None,
        security_config: Optional[SecurityConfig]=None,
        software_config: Optional[SoftwareConfig]=None,
        worker_config: Optional[WorkerConfig]=None,
        config: Optional[Config]=None,
        cluster_selector: Optional[ClusterSelector]=None,
        managed_cluster: Optional[ManagedCluster]=None,
        regex: Optional[Regex]=None,
        values: Optional[Values]=None,
        validation: Optional[Validation]=None,
        logging_config: Optional[LoggingConfig]=None,
        query_list: Optional[QueryList]=None,
        hadoop_job: Optional[HadoopJob]=None,
        hive_job: Optional[HiveJob]=None,
        pig_job: Optional[PigJob]=None,
        presto_job: Optional[PrestoJob]=None,
        pyspark_job: Optional[PysparkJob]=None,
        scheduling: Optional[Scheduling]=None,
        spark_job: Optional[SparkJob]=None,
        spark_r_job: Optional[SparkRJob]=None,
        spark_sql_job: Optional[SparkSqlJob]=None,
        jobs: Optional[Jobs]=None,
        parameters: Optional[Parameters]=None,
        placement: Optional[Placement]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if location is not None:
                kwargs['location'] = location
            if name is not None:
                kwargs['name'] = name
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if version is not None:
                kwargs['version'] = version
            if accelerators is not None:
                kwargs['accelerators'] = accelerators
            if disk_config is not None:
                kwargs['disk_config'] = disk_config
            if kerberos_config is not None:
                kwargs['kerberos_config'] = kerberos_config
            if node_group_affinity is not None:
                kwargs['node_group_affinity'] = node_group_affinity
            if reservation_affinity is not None:
                kwargs['reservation_affinity'] = reservation_affinity
            if autoscaling_config is not None:
                kwargs['autoscaling_config'] = autoscaling_config
            if encryption_config is not None:
                kwargs['encryption_config'] = encryption_config
            if endpoint_config is not None:
                kwargs['endpoint_config'] = endpoint_config
            if gce_cluster_config is not None:
                kwargs['gce_cluster_config'] = gce_cluster_config
            if initialization_actions is not None:
                kwargs['initialization_actions'] = initialization_actions
            if lifecycle_config is not None:
                kwargs['lifecycle_config'] = lifecycle_config
            if master_config is not None:
                kwargs['master_config'] = master_config
            if secondary_worker_config is not None:
                kwargs['secondary_worker_config'] = secondary_worker_config
            if security_config is not None:
                kwargs['security_config'] = security_config
            if software_config is not None:
                kwargs['software_config'] = software_config
            if worker_config is not None:
                kwargs['worker_config'] = worker_config
            if config is not None:
                kwargs['config'] = config
            if cluster_selector is not None:
                kwargs['cluster_selector'] = cluster_selector
            if managed_cluster is not None:
                kwargs['managed_cluster'] = managed_cluster
            if regex is not None:
                kwargs['regex'] = regex
            if values is not None:
                kwargs['values'] = values
            if validation is not None:
                kwargs['validation'] = validation
            if logging_config is not None:
                kwargs['logging_config'] = logging_config
            if query_list is not None:
                kwargs['query_list'] = query_list
            if hadoop_job is not None:
                kwargs['hadoop_job'] = hadoop_job
            if hive_job is not None:
                kwargs['hive_job'] = hive_job
            if pig_job is not None:
                kwargs['pig_job'] = pig_job
            if presto_job is not None:
                kwargs['presto_job'] = presto_job
            if pyspark_job is not None:
                kwargs['pyspark_job'] = pyspark_job
            if scheduling is not None:
                kwargs['scheduling'] = scheduling
            if spark_job is not None:
                kwargs['spark_job'] = spark_job
            if spark_r_job is not None:
                kwargs['spark_r_job'] = spark_r_job
            if spark_sql_job is not None:
                kwargs['spark_sql_job'] = spark_sql_job
            if jobs is not None:
                kwargs['jobs'] = jobs
            if parameters is not None:
                kwargs['parameters'] = parameters
            if placement is not None:
                kwargs['placement'] = placement
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
