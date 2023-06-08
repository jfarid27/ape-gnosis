from ape import plugins
from ape.api import NetworkAPI, create_network_type
from ape.api.networks import LOCAL_NETWORK_NAME
from ape_geth import GethProvider
from ape_test import LocalProvider

from .ecosystem import NETWORKS, Gnosis, GnosisConfig


@plugins.register(plugins.Config)
def config_class():
    return GnosisConfig


@plugins.register(plugins.EcosystemPlugin)
def ecosystems():
    yield Gnosis


@plugins.register(plugins.NetworkPlugin)
def networks():
    for network_name, network_params in NETWORKS.items():
        yield "gnosis", network_name, create_network_type(*network_params)
        yield "gnosis", f"{network_name}-fork", NetworkAPI

    # NOTE: This works for development providers, as they get chain_id from themselves
    yield "gnosis", LOCAL_NETWORK_NAME, NetworkAPI


@plugins.register(plugins.ProviderPlugin)
def providers():
    for network_name in NETWORKS:
        yield "gnosis", network_name, GethProvider

    yield "gnosis", LOCAL_NETWORK_NAME, LocalProvider
