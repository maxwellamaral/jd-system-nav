import argparse
import os
import subprocess
import yaml

def load_config(config_file):
    with open(config_file, "r") as stream:
        try:
            config = yaml.safe_load(stream)
            return config
        except yaml.YAMLError as exc:
            print(exc)
            return None

def search_folder(folder_prefix, path):
    for root, dirs, files in os.walk(path):
        for dir_name in dirs:
            if dir_name.startswith(folder_prefix):
                return os.path.join(root, dir_name)
    return None

def open_with_explorer(folder_path):
    subprocess.run(["explorer", folder_path])

def open_with_vscode(folder_path, vscode_path):    
    subprocess.run([vscode_path, folder_path])

def main():
    parser = argparse.ArgumentParser(description="Search for folders based on a search term.")
    parser.add_argument("search_term", metavar="search_term", type=str, help="Search term for folders")
    parser.add_argument("-f", "--file", metavar="file", type=str, default="config.yaml", help="YAML config file (default: config.yaml)")
    parser.add_argument("-o", "--open", metavar="open", choices=["explorer", "code"], default="explorer", help="Specify 'explorer' to open with Windows Explorer or 'code' to open with VSCode (default: explorer)")
    args = parser.parse_args()

    search_term = args.search_term

    # Obtém o diretório do script atual
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Constrói o caminho completo para o arquivo config.yaml
    config_file = os.path.join(script_dir, args.file)

    config = load_config(config_file)
    if config and "path" in config:
        path = config["path"]
    else:
        print(
            f"Erro: Não foi possível carregar o arquivo {config_file} ou a chave 'path' não está definida."
        )
        return

    folder_path = search_folder(search_term, path)
    if folder_path:
        print("Pasta encontrada:", folder_path)
        # Abre o Windows Explorer ou o VSCode baseado no argumento -o
        if args.open == "code" and "vscode_path" in config:
            vscode_path = config['vscode_path']
            open_with_vscode(folder_path, vscode_path)
        else:
            open_with_explorer(folder_path)
    else:
        print("Pasta não encontrada")

if __name__ == "__main__":
    main()
