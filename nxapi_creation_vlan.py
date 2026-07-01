from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
import requests
import json
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def create_vlan_nxapi(task):
    url = f"http://{task.host.hostname}/ins"

    # 2. Construction du payload JSON-RPC pour envoyer les commandes
    payload = [
        {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {"cmd": "configure terminal", "version": 1},
            "id": 1
        },
        {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {"cmd": "vlan 10", "version": 1},
            "id": 2
        },
        {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {"cmd": "name VLAN_PRODUCTION_NXAPI", "version": 1},
            "id": 3
        },
        {
            "jsonrpc": "2.0",
            "method": "cli",
            "params" : {"cmd": "end", "version":1},
            "id":4
        },
        {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {"cmd": "show vlan brief", "version": 1},
            "id": 4
        }
    ]

    response = requests.post(
        url=url,
        headers={"content-type": "application/json-rpc"},
        data=json.dumps(payload),
        auth=(task.host.username, task.host.password),
        verify=False,
        timeout=10,
    )
    return response.json()

def main():
    nr = InitNornir(config_file="config.yaml")
    print("--- Configuration du VLAN via NX-API ---")
    
    # Exécution de notre fonction personnalisée
    resultats = nr.run(task=create_vlan_nxapi)
    print_result(resultats)

if __name__ == "__main__":
    main()
