# generated by datamodel-codegen:
#   filename:  swagger.json
#   timestamp: 2022-03-30T02:38:35+00:00

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, Field

from ...apimachinery.pkg.apis.meta import v1
from ...apimachinery.pkg.util import intstr


class Eviction(BaseModel):
    class Config:
        allow_population_by_field_name = True

    api_version: Optional[str] = Field(
        None,
        alias='apiVersion',
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    delete_options: Optional[v1.DeleteOptions] = Field(
        None, alias='deleteOptions', description='DeleteOptions may be provided'
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = Field(None, description='ObjectMeta describes the pod that is being evicted.')


class PodDisruptionBudgetSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True

    max_unavailable: Optional[intstr.IntOrString] = Field(
        None,
        alias='maxUnavailable',
        description='An eviction is allowed if at most "maxUnavailable" pods selected by "selector" are unavailable after the eviction, i.e. even in absence of the evicted pod. For example, one can prevent all voluntary evictions by specifying 0. This is a mutually exclusive setting with "minAvailable".',
    )
    min_available: Optional[intstr.IntOrString] = Field(
        None,
        alias='minAvailable',
        description='An eviction is allowed if at least "minAvailable" pods selected by "selector" will still be available after the eviction, i.e. even in the absence of the evicted pod.  So for example you can prevent all voluntary evictions by specifying "100%".',
    )
    selector: Optional[v1.LabelSelector] = Field(
        None,
        description='Label query over pods whose evictions are managed by the disruption budget. A null selector will match no pods, while an empty ({}) selector will select all pods within the namespace.',
    )


class PodDisruptionBudgetStatus(BaseModel):
    class Config:
        allow_population_by_field_name = True

    conditions: Optional[List[v1.Condition]] = Field(
        None,
        description="Conditions contain conditions for PDB. The disruption controller sets the DisruptionAllowed condition. The following are known values for the reason field (additional reasons could be added in the future): - SyncFailed: The controller encountered an error and wasn't able to compute\n              the number of allowed disruptions. Therefore no disruptions are\n              allowed and the status of the condition will be False.\n- InsufficientPods: The number of pods are either at or below the number\n                    required by the PodDisruptionBudget. No disruptions are\n                    allowed and the status of the condition will be False.\n- SufficientPods: There are more pods than required by the PodDisruptionBudget.\n                  The condition will be True, and the number of allowed\n                  disruptions are provided by the disruptionsAllowed property.",
    )
    current_healthy: int = Field(..., alias='currentHealthy', description='current number of healthy pods')
    desired_healthy: int = Field(..., alias='desiredHealthy', description='minimum desired number of healthy pods')
    disrupted_pods: Optional[Dict[str, v1.Time]] = Field(
        None,
        alias='disruptedPods',
        description="DisruptedPods contains information about pods whose eviction was processed by the API server eviction subresource handler but has not yet been observed by the PodDisruptionBudget controller. A pod will be in this map from the time when the API server processed the eviction request to the time when the pod is seen by PDB controller as having been marked for deletion (or after a timeout). The key in the map is the name of the pod and the value is the time when the API server processed the eviction request. If the deletion didn't occur and a pod is still there it will be removed from the list automatically by PodDisruptionBudget controller after some time. If everything goes smooth this map should be empty for the most of the time. Large number of entries in the map may indicate problems with pod deletions.",
    )
    disruptions_allowed: int = Field(
        ..., alias='disruptionsAllowed', description='Number of pod disruptions that are currently allowed.'
    )
    expected_pods: int = Field(
        ..., alias='expectedPods', description='total number of pods counted by this disruption budget'
    )
    observed_generation: Optional[int] = Field(
        None,
        alias='observedGeneration',
        description="Most recent generation observed when updating this PDB status. DisruptionsAllowed and other status information is valid only if observedGeneration equals to PDB's object generation.",
    )


class PodDisruptionBudget(BaseModel):
    class Config:
        allow_population_by_field_name = True

    api_version: Optional[str] = Field(
        None,
        alias='apiVersion',
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[PodDisruptionBudgetSpec] = Field(
        None, description='Specification of the desired behavior of the PodDisruptionBudget.'
    )
    status: Optional[PodDisruptionBudgetStatus] = Field(
        None, description='Most recently observed status of the PodDisruptionBudget.'
    )


class PodDisruptionBudgetList(BaseModel):
    class Config:
        allow_population_by_field_name = True

    api_version: Optional[str] = Field(
        None,
        alias='apiVersion',
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[PodDisruptionBudget] = Field(..., description='Items is a list of PodDisruptionBudgets')
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
