from abc import ABC, abstractmethod


# abstrakte Basisklasse für Cloud-Instanzen
class CloudInstance(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def get_status(self):
        pass


# konkrete Instanzen
class AWSInstance(CloudInstance):

    def __init__(self, config):
        if "name" not in config:
            raise ValueError("Ungültige AWS-Konfiguration")
        self.name = config["name"]
        self.status = "gestoppt"

    def start(self):
        self.status = "läuft"
        print("AWS-Instanz", self.name, "wird gestartet.")

    def stop(self):
        self.status = "gestoppt"
        print("AWS-Instanz", self.name, "wird gestoppt.")

    def get_status(self):
        print("AWS-Instanz", self.name, "Status:", self.status)


class AzureInstance(CloudInstance):

    def __init__(self, config):
        if "name" not in config:
            raise ValueError("Ungültige Azure-Konfiguration")
        self.name = config["name"]
        self.status = "gestoppt"

    def start(self):
        self.status = "läuft"
        print("Azure-Instanz", self.name, "wird gestartet.")

    def stop(self):
        self.status = "gestoppt"
        print("Azure-Instanz", self.name, "wird gestoppt.")

    def get_status(self):
        print("Azure-Instanz", self.name, "Status:", self.status)


class GCPInstance(CloudInstance):

    def __init__(self, config):
        if "name" not in config:
            raise ValueError("Ungültige GCP-Konfiguration")
        self.name = config["name"]
        self.status = "gestoppt"

    def start(self):
        self.status = "läuft"
        print("GCP-Instanz", self.name, "wird gestartet.")

    def stop(self):
        self.status = "gestoppt"
        print("GCP-Instanz", self.name, "wird gestoppt.")

    def get_status(self):
        print("GCP-Instanz", self.name, "Status:", self.status)


# abstrakter Creator
class CloudProvider(ABC):

    @abstractmethod
    def create_instance(self, config):
        pass


# konkrete Creator / Factory-Klassen
class AWSProvider(CloudProvider):

    def create_instance(self, config):
        return AWSInstance(config)


class AzureProvider(CloudProvider):

    def create_instance(self, config):
        return AzureInstance(config)


class GCPProvider(CloudProvider):

    def create_instance(self, config):
        return GCPInstance(config)


# Client-Logik
def bereitstellen_und_starten(provider, config):
    instance = provider.create_instance(config)
    instance.get_status()
    instance.start()
    instance.get_status()
    return instance


# Testcode
if __name__ == "__main__":

    print("AWS Beispiel:")
    aws_provider = AWSProvider()
    aws_instance = bereitstellen_und_starten(aws_provider, {"name": "aws-server-1"})
    aws_instance.stop()
    aws_instance.get_status()

    print()

    print("Azure Beispiel:")
    azure_provider = AzureProvider()
    azure_instance = bereitstellen_und_starten(azure_provider, {"name": "azure-server-1"})
    azure_instance.stop()
    azure_instance.get_status()

    print()

    print("GCP Beispiel:")
    gcp_provider = GCPProvider()
    gcp_instance = bereitstellen_und_starten(gcp_provider, {"name": "gcp-server-1"})
    gcp_instance.stop()
    gcp_instance.get_status()

    print()

    # einfache Fehlerbehandlung
    print("Fehlerbehandlung:")
    try:
        falscher_provider = AWSProvider()
        falsche_instanz = bereitstellen_und_starten(falscher_provider, {})
    except ValueError as e:
        print("Fehler:", e)