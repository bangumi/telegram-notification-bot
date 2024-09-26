from datetime import datetime

import msgspec


class Source(msgspec.Struct):
    ts_ms: int

    def timestamp(self) -> datetime:
        return datetime.fromtimestamp(self.ts_ms / 1000).astimezone()


class ChiiNotify(msgspec.Struct):
    """table of chii_notify as json"""

    # nt_id: Any
    nt_uid: int
    nt_from_uid: int
    nt_status: int
    nt_type: int
    nt_mid: int  # ID of notify_field
    nt_related_id: int  # id of post
    timestamp: int = msgspec.field(name="nt_dateline")


class ChiiNotifyField(msgspec.Struct):
    """table of chii_notify_field as json"""

    ntf_id: int
    ntf_rid: int
    ntf_title: str
    ntf_hash: int


class NotifyValue(msgspec.Struct):
    after: ChiiNotify | None
    op: str  # 'r', 'c', 'd' ...


class ChiiMember(msgspec.Struct):
    """table of chii_members as json"""

    uid: int
    newpm: int


class MemberValue(msgspec.Struct):
    before: ChiiMember | None
    after: ChiiMember | None
    op: str  # 'r', 'c', 'd' ...
    source: Source
