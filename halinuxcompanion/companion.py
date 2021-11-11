import platform

CONFIG_KEYS = [("ha_url", True), ("ha_token", True), ("device_id", True),
               ("device_name", False), ("manufacturer", False),
               ("model", False), ("computer_ip", True),
               ("computer_port", True), ("refresh_interval", False)]


class Companion:
    """Class encolsing a companion instance
    https://developers.home-assistant.io/docs/api/native-app-integration/setup
    """
    def __init__(self, config: dict):
        # Load only allowed values
        for key, req in CONFIG_KEYS:
            value = config.get(key, None)
            if value is None and req:
                raise ValueError(f"Missing required config key: {key}")
            else:
                if value != "":
                    setattr(self, key, value)

    def registration_payload(self) -> dict:
        return {
            "device_id": self.device_id,
            "app_id": self.app_id,
            "app_name": self.app_name,
            "app_version": self.app_version,
            "device_name": self.device_name,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "os_name": self.os_name,
            "os_version": self.os_version,
            "supports_encryption": self.supports_encryption,
            # TODO: implement
            "app_data": self.app_data,
        }

    device_id: str = platform.node()
    # TODO: Get the default values from something that helps sets releases.
    app_name: str = "Linux Companion"
    app_version: str = "0.0.1"
    app_id: str = app_name.replace(" ", "_") + app_version
    device_name: str = platform.node()
    manufacturer: str = platform.system()
    model: str = "Computer"
    os_name: str = platform.system()
    os_version: str = platform.release()
    # TODO: Encryption requires https://github.com/jedisct1/libsodium
    supports_encryption: bool = False
    app_data: dict = {}
    refresh_interval: int = 15
    ip: str = ""
    port: int = 8400
    ha_url: str = "http://localhost:8123"
    ha_token: str
