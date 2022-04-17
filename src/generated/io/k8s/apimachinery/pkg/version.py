# generated by datamodel-codegen:
#   filename:  swagger.json
#   timestamp: 2022-03-30T02:38:35+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class Info(BaseModel):
    class Config:
        allow_population_by_field_name = True

    build_date: str = Field(..., alias='buildDate')
    compiler: str
    git_commit: str = Field(..., alias='gitCommit')
    git_tree_state: str = Field(..., alias='gitTreeState')
    git_version: str = Field(..., alias='gitVersion')
    go_version: str = Field(..., alias='goVersion')
    major: str
    minor: str
    platform: str
