from quark.plugin_manager import factory

from quark_plugin_tsp.classical_tsp_solver import ClassicalTspSolver
from quark_plugin_tsp.tsp_graph_provider import TspGraphProvider


def register() -> None:
    factory.register("tsp_graph_provider", TspGraphProvider)
    factory.register("classical_tsp_solver", ClassicalTspSolver)
