from dataclasses import field, dataclass
from typing import List


@dataclass
class Currency:
    """
    class for validation data that was collected from daily quotes endpoint
    may and must be validated via XmlParser of Xsdata
    """
    id: str = field(metadata=dict(type="Attribute", name="ID"))
    num_code: int = field(metadata=dict(name="NumCode"))
    char_code: str = field(metadata=dict(name="CharCode"))
    nominal: int = field(metadata=dict(name="Nominal"))
    name: str = field(metadata=dict(name="Name"))
    value: str = field(metadata=dict(name="Value"))


@dataclass
class Currencies:
    class Meta:
        name = "ValCurs"

    date: str = field(metadata=dict(type="Attribute", name="Date"))
    name: str = field(metadata=dict(type="Attribute"))
    values: List[Currency] = field(default_factory=list, metadata=dict(name="Valute"))



