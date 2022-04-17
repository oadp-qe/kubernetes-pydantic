# generated by datamodel-codegen:
#   filename:  swagger.json
#   timestamp: 2022-03-30T02:38:35+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class IntOrString(BaseModel):
    class Config:
        allow_population_by_field_name = True

    __root__: str = Field(
        ...,
        description='IntOrString is a type that can hold an int32 or a string.  When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type.  This allows you to have, for example, a JSON field that can accept a name or number.',
    )
