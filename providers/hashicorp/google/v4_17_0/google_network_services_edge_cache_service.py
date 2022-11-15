
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class CacheKeyPolicyItem():
        # non-optional-blocks
        exclude_host: Optional[bool] = None
        exclude_query_string: Optional[bool] = None
        excluded_query_parameters: Optional[List[str]] = None
        include_protocol: Optional[bool] = None
        included_cookie_names: Optional[List[str]] = None
        included_header_names: Optional[List[str]] = None
        included_query_parameters: Optional[List[str]] = None
        
# wrapper list class
class CacheKeyPolicy(BlockList):
        items: List[CacheKeyPolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CdnPolicyItem():
        # non-optional-blocks
        cache_mode: Optional[str] = None
        client_ttl: Optional[str] = None
        default_ttl: Optional[str] = None
        max_ttl: Optional[str] = None
        negative_caching: Optional[bool] = None
        negative_caching_policy: Optional[Dict[str, str]] = None
        signed_request_keyset: Optional[str] = None
        signed_request_mode: Optional[str] = None
        cache_key_policy: Optional[CacheKeyPolicy]=None,
        
# wrapper list class
class CdnPolicy(BlockList):
        items: List[CdnPolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class CorsPolicyItem():
        max_age:str
        # non-optional-blocks
        allow_credentials: Optional[bool] = None
        allow_headers: Optional[List[str]] = None
        allow_methods: Optional[List[str]] = None
        allow_origins: Optional[List[str]] = None
        disabled: Optional[bool] = None
        expose_headers: Optional[List[str]] = None
        
# wrapper list class
class CorsPolicy(BlockList):
        items: List[CorsPolicyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class UrlRewriteItem():
        # non-optional-blocks
        host_rewrite: Optional[str] = None
        path_prefix_rewrite: Optional[str] = None
        path_template_rewrite: Optional[str] = None
        
# wrapper list class
class UrlRewrite(BlockList):
        items: List[UrlRewriteItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HeaderMatchItem():
        header_name:str
        # non-optional-blocks
        exact_match: Optional[str] = None
        invert_match: Optional[bool] = None
        prefix_match: Optional[str] = None
        present_match: Optional[bool] = None
        suffix_match: Optional[str] = None
        
# wrapper list class
class HeaderMatch(BlockList):
        items: List[HeaderMatchItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class QueryParameterMatchItem():
        name:str
        # non-optional-blocks
        exact_match: Optional[str] = None
        present_match: Optional[bool] = None
        
# wrapper list class
class QueryParameterMatch(BlockList):
        items: List[QueryParameterMatchItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RequestHeaderToAddItem():
        header_name:str
        header_value:str
        # non-optional-blocks
        replace: Optional[bool] = None
        
# wrapper list class
class RequestHeaderToAdd(BlockList):
        items: List[RequestHeaderToAddItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RequestHeaderToRemoveItem():
        header_name:str
        # non-optional-blocks
        
# wrapper list class
class RequestHeaderToRemove(BlockList):
        items: List[RequestHeaderToRemoveItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ResponseHeaderToAddItem():
        header_name:str
        header_value:str
        # non-optional-blocks
        replace: Optional[bool] = None
        
# wrapper list class
class ResponseHeaderToAdd(BlockList):
        items: List[ResponseHeaderToAddItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class ResponseHeaderToRemoveItem():
        header_name:str
        # non-optional-blocks
        
# wrapper list class
class ResponseHeaderToRemove(BlockList):
        items: List[ResponseHeaderToRemoveItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HeaderActionItem():
        # non-optional-blocks
        request_header_to_add: Optional[RequestHeaderToAdd]=None,
        request_header_to_remove: Optional[RequestHeaderToRemove]=None,
        response_header_to_add: Optional[ResponseHeaderToAdd]=None,
        response_header_to_remove: Optional[ResponseHeaderToRemove]=None,
        
# wrapper list class
class HeaderAction(BlockList):
        items: List[HeaderActionItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class MatchRuleItem():
        # non-optional-blocks
        full_path_match: Optional[str] = None
        ignore_case: Optional[bool] = None
        path_template_match: Optional[str] = None
        prefix_match: Optional[str] = None
        header_match: Optional[HeaderMatch]=None,
        query_parameter_match: Optional[QueryParameterMatch]=None,
        
# wrapper list class
class MatchRule(BlockList):
        items: List[MatchRuleItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RouteActionItem():
        # non-optional-blocks
        cache_key_policy: Optional[CacheKeyPolicy]=None,
        cdn_policy: Optional[CdnPolicy]=None,
        cors_policy: Optional[CorsPolicy]=None,
        url_rewrite: Optional[UrlRewrite]=None,
        
# wrapper list class
class RouteAction(BlockList):
        items: List[RouteActionItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class UrlRedirectItem():
        # non-optional-blocks
        host_redirect: Optional[str] = None
        https_redirect: Optional[bool] = None
        path_redirect: Optional[str] = None
        prefix_redirect: Optional[str] = None
        redirect_response_code: Optional[str] = None
        strip_query: Optional[bool] = None
        
# wrapper list class
class UrlRedirect(BlockList):
        items: List[UrlRedirectItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RouteRuleItem():
        priority:str
        # non-optional-blocks
        description: Optional[str] = None
        origin: Optional[str] = None
        cache_key_policy: Optional[CacheKeyPolicy]=None,
        cdn_policy: Optional[CdnPolicy]=None,
        cors_policy: Optional[CorsPolicy]=None,
        url_rewrite: Optional[UrlRewrite]=None,
        header_match: Optional[HeaderMatch]=None,
        query_parameter_match: Optional[QueryParameterMatch]=None,
        request_header_to_add: Optional[RequestHeaderToAdd]=None,
        request_header_to_remove: Optional[RequestHeaderToRemove]=None,
        response_header_to_add: Optional[ResponseHeaderToAdd]=None,
        response_header_to_remove: Optional[ResponseHeaderToRemove]=None,
        header_action: Optional[HeaderAction]=None,
        match_rule: Optional[MatchRule]=None,
        route_action: Optional[RouteAction]=None,
        url_redirect: Optional[UrlRedirect]=None,
        
# wrapper list class
class RouteRule(BlockList):
        items: List[RouteRuleItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class HostRuleItem():
        hosts:List[str]
        path_matcher:str
        # non-optional-blocks
        description: Optional[str] = None
        
# wrapper list class
class HostRule(BlockList):
        items: List[HostRuleItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class PathMatcherItem():
        name:str
        # non-optional-blocks
        description: Optional[str] = None
        cache_key_policy: Optional[CacheKeyPolicy]=None,
        cdn_policy: Optional[CdnPolicy]=None,
        cors_policy: Optional[CorsPolicy]=None,
        url_rewrite: Optional[UrlRewrite]=None,
        header_match: Optional[HeaderMatch]=None,
        query_parameter_match: Optional[QueryParameterMatch]=None,
        request_header_to_add: Optional[RequestHeaderToAdd]=None,
        request_header_to_remove: Optional[RequestHeaderToRemove]=None,
        response_header_to_add: Optional[ResponseHeaderToAdd]=None,
        response_header_to_remove: Optional[ResponseHeaderToRemove]=None,
        header_action: Optional[HeaderAction]=None,
        match_rule: Optional[MatchRule]=None,
        route_action: Optional[RouteAction]=None,
        url_redirect: Optional[UrlRedirect]=None,
        route_rule: Optional[RouteRule]=None,
        
# wrapper list class
class PathMatcher(BlockList):
        items: List[PathMatcherItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class LogConfigItem():
        # non-optional-blocks
        enable: Optional[bool] = None
        sample_rate: Optional[float] = None
        
# wrapper list class
class LogConfig(BlockList):
        items: List[LogConfigItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class RoutingItem():
        # non-optional-blocks
        cache_key_policy: Optional[CacheKeyPolicy]=None,
        cdn_policy: Optional[CdnPolicy]=None,
        cors_policy: Optional[CorsPolicy]=None,
        url_rewrite: Optional[UrlRewrite]=None,
        header_match: Optional[HeaderMatch]=None,
        query_parameter_match: Optional[QueryParameterMatch]=None,
        request_header_to_add: Optional[RequestHeaderToAdd]=None,
        request_header_to_remove: Optional[RequestHeaderToRemove]=None,
        response_header_to_add: Optional[ResponseHeaderToAdd]=None,
        response_header_to_remove: Optional[ResponseHeaderToRemove]=None,
        header_action: Optional[HeaderAction]=None,
        match_rule: Optional[MatchRule]=None,
        route_action: Optional[RouteAction]=None,
        url_redirect: Optional[UrlRedirect]=None,
        route_rule: Optional[RouteRule]=None,
        host_rule: Optional[HostRule]=None,
        path_matcher: Optional[PathMatcher]=None,
        
# wrapper list class
class Routing(BlockList):
        items: List[RoutingItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleNetworkServicesEdgeCacheService(ResourceObject):
    """    
    Args:
        name (str): Name of the resource; provided by the client when the resource is created.
                    The name must be 1-64 characters long, and match the regular expression [a-zA-Z][a-zA-Z0-9_-]* which means the first character must be a letter,
                    and all following characters must be a dash, underscore, letter or digit.
    """
    _type = 'google_network_services_edge_cache_service'
    
    def __init__(self,
        tf_id: str,
        name:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        disable_http2: Optional[bool] = None,
        disable_quic: Optional[bool] = None,
        edge_security_policy: Optional[str] = None,
        edge_ssl_certificates: Optional[List[str]] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        require_tls: Optional[bool] = None,
        ssl_policy: Optional[str] = None,
        cache_key_policy: Optional[CacheKeyPolicy]=None,
        cdn_policy: Optional[CdnPolicy]=None,
        cors_policy: Optional[CorsPolicy]=None,
        url_rewrite: Optional[UrlRewrite]=None,
        header_match: Optional[HeaderMatch]=None,
        query_parameter_match: Optional[QueryParameterMatch]=None,
        request_header_to_add: Optional[RequestHeaderToAdd]=None,
        request_header_to_remove: Optional[RequestHeaderToRemove]=None,
        response_header_to_add: Optional[ResponseHeaderToAdd]=None,
        response_header_to_remove: Optional[ResponseHeaderToRemove]=None,
        header_action: Optional[HeaderAction]=None,
        match_rule: Optional[MatchRule]=None,
        route_action: Optional[RouteAction]=None,
        url_redirect: Optional[UrlRedirect]=None,
        route_rule: Optional[RouteRule]=None,
        host_rule: Optional[HostRule]=None,
        path_matcher: Optional[PathMatcher]=None,
        log_config: Optional[LogConfig]=None,
        routing: Optional[Routing]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if description is not None:
                kwargs['description'] = description
            if disable_http2 is not None:
                kwargs['disable_http2'] = disable_http2
            if disable_quic is not None:
                kwargs['disable_quic'] = disable_quic
            if edge_security_policy is not None:
                kwargs['edge_security_policy'] = edge_security_policy
            if edge_ssl_certificates is not None:
                kwargs['edge_ssl_certificates'] = edge_ssl_certificates
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if require_tls is not None:
                kwargs['require_tls'] = require_tls
            if ssl_policy is not None:
                kwargs['ssl_policy'] = ssl_policy
            if cache_key_policy is not None:
                kwargs['cache_key_policy'] = cache_key_policy
            if cdn_policy is not None:
                kwargs['cdn_policy'] = cdn_policy
            if cors_policy is not None:
                kwargs['cors_policy'] = cors_policy
            if url_rewrite is not None:
                kwargs['url_rewrite'] = url_rewrite
            if header_match is not None:
                kwargs['header_match'] = header_match
            if query_parameter_match is not None:
                kwargs['query_parameter_match'] = query_parameter_match
            if request_header_to_add is not None:
                kwargs['request_header_to_add'] = request_header_to_add
            if request_header_to_remove is not None:
                kwargs['request_header_to_remove'] = request_header_to_remove
            if response_header_to_add is not None:
                kwargs['response_header_to_add'] = response_header_to_add
            if response_header_to_remove is not None:
                kwargs['response_header_to_remove'] = response_header_to_remove
            if header_action is not None:
                kwargs['header_action'] = header_action
            if match_rule is not None:
                kwargs['match_rule'] = match_rule
            if route_action is not None:
                kwargs['route_action'] = route_action
            if url_redirect is not None:
                kwargs['url_redirect'] = url_redirect
            if route_rule is not None:
                kwargs['route_rule'] = route_rule
            if host_rule is not None:
                kwargs['host_rule'] = host_rule
            if path_matcher is not None:
                kwargs['path_matcher'] = path_matcher
            if log_config is not None:
                kwargs['log_config'] = log_config
            if routing is not None:
                kwargs['routing'] = routing
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        
