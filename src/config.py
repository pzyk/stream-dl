"""
Configuration handling
"""
import yaml


class Config:
    """
    Class for config handling
    """

    def __init__(self, config_path: str):
        """
        Init
        """
        self.services = self._read_config(config_path)

    @staticmethod
    def _read_config(config_path: str):
        """
        Reads channels YAML file
        Returns a dict of services and a dict of channels
        """
        # Open YAML file
        with open(config_path, encoding="utf-8") as file:
            content = yaml.safe_load(file)

        # Parse data from YAML file
        services = {}
        for service in content:
            url_main = content[service]["url"].strip()
            path_main = content[service]["path"].strip()
            interval_main = content[service]["interval"].strip()
            channels = content[service]["channels"]

            # Add trailing slash to main path if necessary
            if not path_main.endswith("/"):
                path_main += "/"

            # Create config dictionary
            config = {"url": url_main, "path": path_main, "interval": interval_main}

            services[service] = {"config": config, "channels": channels}

        return services
