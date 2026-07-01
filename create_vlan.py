from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result


def main():
    nr = InitNornir(config_file="config.yaml")
    print("--- Configuration du VLAN sur le switch ---")
    commandes_vlan = [
    "vlan 10",
    "name vlan_production"
    ]
    resultats = nr.run(
        task=netmiko_send_config,
        config_commands=commandes_vlan
    )

    print_result(resultats)

if __name__ == "__main__":
    main()
