# generated by datamodel-codegen:
#   filename:  swagger.json
#   timestamp: 2022-03-30T02:38:35+00:00

from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field

from ...apimachinery.pkg.apis.meta import v1 as v1_1
from ..core import v1


class EndpointConditions(BaseModel):
    class Config:
        allow_population_by_field_name = True

    ready: Optional[bool] = Field(
        None,
        description='ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready. For compatibility reasons, ready should never be "true" for terminating endpoints.',
    )
    serving: Optional[bool] = Field(
        None,
        description='serving is identical to ready except that it is set regardless of the terminating state of endpoints. This condition should be set to true for a ready endpoint that is terminating. If nil, consumers should defer to the ready condition. This field can be enabled with the EndpointSliceTerminatingCondition feature gate.',
    )
    terminating: Optional[bool] = Field(
        None,
        description='terminating indicates that this endpoint is terminating. A nil value indicates an unknown state. Consumers should interpret this unknown state to mean that the endpoint is not terminating. This field can be enabled with the EndpointSliceTerminatingCondition feature gate.',
    )


class EndpointPort(BaseModel):
    class Config:
        allow_population_by_field_name = True

    app_protocol: Optional[str] = Field(
        None,
        alias='appProtocol',
        description='The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol.',
    )
    name: Optional[str] = Field(
        None,
        description="The name of this port. All ports in an EndpointSlice must have a unique name. If the EndpointSlice is dervied from a Kubernetes service, this corresponds to the Service.ports[].name. Name must either be an empty string or pass DNS_LABEL validation: * must be no more than 63 characters long. * must consist of lower case alphanumeric characters or '-'. * must start and end with an alphanumeric character. Default is empty string.",
    )
    port: Optional[int] = Field(
        None,
        description='The port number of the endpoint. If this is not specified, ports are not restricted and must be interpreted in the context of the specific consumer.',
    )
    protocol: Optional[str] = Field(
        None, description='The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.'
    )


class AddressType(Enum):
    fqdn = 'FQDN'
    i_pv4 = 'IPv4'
    i_pv6 = 'IPv6'


class ForZone(BaseModel):
    class Config:
        allow_population_by_field_name = True

    name: str = Field(..., description='name represents the name of the zone.')


class EndpointHints(BaseModel):
    class Config:
        allow_population_by_field_name = True

    for_zones: Optional[List[ForZone]] = Field(
        None,
        alias='forZones',
        description='forZones indicates the zone(s) this endpoint should be consumed by to enable topology aware routing.',
    )


class Endpoint(BaseModel):
    class Config:
        allow_population_by_field_name = True

    addresses: List[str] = Field(
        ...,
        description='addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different generated of addresses in the context of their own capabilities. This must contain at least one address but no more than 100. These are all assumed to be fungible and clients may choose to only use the first element. Refer to: https://issue.k8s.io/106267',
    )
    conditions: Optional[EndpointConditions] = Field(
        None, description='conditions contains information about the current status of the endpoint.'
    )
    deprecated_topology: Optional[Dict[str, str]] = Field(
        None,
        alias='deprecatedTopology',
        description='deprecatedTopology contains topology information part of the v1beta1 API. This field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and any attempts to write to it will be silently ignored. Topology information can be found in the zone and nodeName fields instead.',
    )
    hints: Optional[EndpointHints] = Field(
        None, description='hints contains information associated with how an endpoint should be consumed.'
    )
    hostname: Optional[str] = Field(
        None,
        description='hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation.',
    )
    node_name: Optional[str] = Field(
        None,
        alias='nodeName',
        description='nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node. This field can be enabled with the EndpointSliceNodeName feature gate.',
    )
    target_ref: Optional[v1.ObjectReference] = Field(
        None,
        alias='targetRef',
        description='targetRef is a reference to a Kubernetes object that represents this endpoint.',
    )
    zone: Optional[str] = Field(None, description='zone is the name of the Zone this endpoint exists in.')


class EndpointSlice(BaseModel):
    class Config:
        allow_population_by_field_name = True

    address_type: AddressType = Field(
        ...,
        alias='addressType',
        description='addressType specifies the type of address carried by this EndpointSlice. All addresses in this slice must be the same type. This field is immutable after creation. The following address generated are currently supported: * IPv4: Represents an IPv4 Address. * IPv6: Represents an IPv6 Address. * FQDN: Represents a Fully Qualified Domain Name.\n\nPossible enum values:\n - `"FQDN"` represents a FQDN.\n - `"IPv4"` represents an IPv4 Address.\n - `"IPv6"` represents an IPv6 Address.',
    )
    api_version: Optional[str] = Field(
        None,
        alias='apiVersion',
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    endpoints: List[Endpoint] = Field(
        ...,
        description='endpoints is a list of unique endpoints in this slice. Each slice may include a maximum of 1000 endpoints.',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1_1.ObjectMeta] = Field(None, description="Standard object's metadata.")
    ports: Optional[List[EndpointPort]] = Field(
        None,
        description='ports specifies the list of network ports exposed by each endpoint in this slice. Each port must have a unique name. When ports is empty, it indicates that there are no defined ports. When a port is defined with a nil port value, it indicates "all ports". Each slice may include a maximum of 100 ports.',
    )


class EndpointSliceList(BaseModel):
    class Config:
        allow_population_by_field_name = True

    api_version: Optional[str] = Field(
        None,
        alias='apiVersion',
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[EndpointSlice] = Field(..., description='List of endpoint slices')
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1_1.ListMeta] = Field(None, description='Standard list metadata.')
