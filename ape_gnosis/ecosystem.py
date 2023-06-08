from typing import Optional
from ape.api.config import PluginConfig
from ape.api.networks import LOCAL_NETWORK_NAME
from ape_ethereum.ecosystem import Ethereum, NetworkConfig

NETWORKS = {
    # chain_id, network_id
    "mainnet": (100, 100),
    "chiado": (10200, 10200),  # testnet
}


def _create_network_config(
    required_confirmations: int = 1, block_time: int = 2, **kwargs
) -> NetworkConfig:
    return NetworkConfig(
        required_confirmations=required_confirmations, block_time=block_time, **kwargs
    )


def _create_local_config(default_provider: Optional[str] = None) -> NetworkConfig:
    return _create_network_config(
        required_confirmations=0, block_time=0, default_provider=default_provider
    )


class GnosisConfig(PluginConfig):
    mainnet: NetworkConfig = _create_network_config()
    mainnet_fork: NetworkConfig = _create_local_config()
    mumbai: NetworkConfig = _create_network_config()
    mumbai_fork: NetworkConfig = _create_local_config()
    local: NetworkConfig = NetworkConfig(default_provider="test")
    default_network: str = LOCAL_NETWORK_NAME


class Gnosis(Ethereum):
    @property
    def config(self) -> GnosisConfig:  # type: ignore
        return self.config_manager.get_config("gnosis")  # type: ignore
