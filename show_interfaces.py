from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

def get_interfaces_status(task):
    # On envoie la commande de vérification
    output = task.run(
        task=netmiko_send_command,
        command_string="show ip interface brief"
    )

def main():
    # Initialisation de Nornir avec ton fichier de configuration
    nr = InitNornir(config_file="config.yaml")
    
    print("--- Récupération de l'état des interfaces ---")
    
    # On filtre sur ton switch 3850 (ou par plateforme)
    target_switch = nr.filter(platform="cisco_ios")
    
    # Exécution de la tâche
    resultats = target_switch.run(task=get_interfaces_status)
    
    # Affichage propre du résultat dans la console
    print_result(resultats)

if __name__ == "__main__":
    main()
