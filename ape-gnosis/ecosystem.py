from ape.api.config import PluginConfig
from ape.api.networks import LOCAL_NETWORK_NAME
from ape_ethereum.ecosystem import Ethereum, NetworkConfig

NETWORKS = {
    # chain_id, network_id
    "mainnet": (100, 100),
    "optimism": (300, 300),
}


class GnosisConfig(PluginConfig):
    mainnet: NetworkConfig = NetworkConfig(required_confirmations=1, block_time=2)  # type: ignore
    optimism: NetworkConfig = NetworkConfig(required_confirmations=1, block_time=2)  # type: ignore
    local: NetworkConfig = NetworkConfig(default_provider="test")  # type: ignore
    default_network: str = LOCAL_NETWORK_NAME


class Gnosis(Ethereum):
    @property
    def config(self) -> GnosisConfig:  # type: ignore
        return self.config_manager.get_config("gnosis")  # type: ignore