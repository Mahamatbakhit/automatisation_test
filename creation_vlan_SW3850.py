from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

def main():
    nr = InitNornir(config_file="config.yaml")
    print("--- Configuration du VLAN sur le switch Catalyst ---")
    
    # 1. ON FILTRE ICI : On ne garde que les équipements IOS
    switchs_catalyst = nr.filter(platform="cisco_ios")
    
    commandes_vlan = [
        "vlan 10",
        "name vlan_production"
    ]
    
    # 2. ON CORRIGE L'APPEL : On lance .run() sur notre filtre, pas sur "nr" global
    resultats = switchs_catalyst.run(
        task=netmiko_send_config,
        config_commands=commandes_vlan
    )

    print_result(resultats)

if __name__ == "__main__":
    main()
