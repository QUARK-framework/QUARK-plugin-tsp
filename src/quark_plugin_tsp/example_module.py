from dataclasses import dataclass
from typing import override

from quark.protocols import Core

@dataclass
class ExampleModule(Core):
    """
    This is an example module following the recommended structure for a quark module.

    Each module must have a preprocess and postprocess method, as required by the Core protocol.
    The types those methods take and return define the modules interface, dictating which other modules it can be connected to.
    Types defining interfaces should be chosen form QUARKs predefined set of types to ensure compatibility with other modules. TODO: insert link
    """

    @override
    def preprocess(self, data: None) -> None:
        pass

    @override
    def postprocess(self, data: None) -> None:
        pass
