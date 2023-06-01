from dataclasses import field, dataclass
from typing import List

@dataclass
class AllCurrencies:
    """
     class for validation compare data that was collected from currency codes reference endpoint
     may and must be validated via XmlParser of Xsdata
     """

    id: str = field(metadata=dict(type="Attribute", name="ID"))
    name: str = field(metadata=dict(name="Name"))
    eng_name: str = field(metadata=dict(name="EngName"))
    nominal: int = field(metadata=dict(name="Nominal"))
    parent_code: str = field(metadata=dict(name="ParentCode"))
    num_code: str = field(metadata=dict(name="ISO_Num_Code"))
    char_code: str = field(metadata=dict(name="ISO_Char_Code"))

@dataclass
class CurrenciesLib:
    class Meta:
        name = "Valuta"

    name: str = field(metadata=dict(type="Attribute"))
    values: List[AllCurrencies] = field(default_factory=list, metadata=dict(name="Item"))


