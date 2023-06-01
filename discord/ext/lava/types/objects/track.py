from typing import Any, TypeAlias, TypedDict


class TrackInfoData(TypedDict):
    identifier: str
    isSeekable: bool
    author: str
    length: int
    isStream: bool
    position: int
    title: str
    uri: str | None
    artworkUrl: str | None
    isrc: str | None
    sourceName: str


TrackPluginInfoData: TypeAlias = dict[str, Any]


class TrackData(TypedDict):
    info: TrackInfoData
    pluginInfo: TrackPluginInfoData
    encoded: str