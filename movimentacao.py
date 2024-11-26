import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
import time

class OrganizadorPorDataHandler(FileSystemEventHandler):
    def __init__(self, pasta_monitorada):
        self.pasta_monitorada = pasta_monitorada

    def on_created(self, event):
        if not event.is_directory:
            self.organizar_arquivo(event.src_path)

    def organizar_arquivo(self, caminho_arquivo):
        # Obter o nome do arquivo e sua data de modificação
        
        # Criar a pasta de destino com base na data
        
        # Mover o arquivo para a pasta de destino


    def obter_data_modificacao(self, caminho_arquivo):
        timestamp = os.path.getmtime(caminho_arquivo)
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

def organizar_arquivos_existentes(pasta):
    print("Organizando arquivos existentes...")

    print("Organização inicial concluída.")

def monitorar_pasta():
    pasta_monitorada = "entrada"
    os.makedirs(pasta_monitorada, exist_ok=True)
    
    # Organizar arquivos existentes antes de iniciar o monitoramento
    organizar_arquivos_existentes(pasta_monitorada)
    
    # Configurar e iniciar o monitoramento
    handler = OrganizadorPorDataHandler(pasta_monitorada)
    observer = Observer()
    observer.schedule(handler, path=pasta_monitorada, recursive=False)
    observer.start()
    
    try:
        print(f"Monitorando a pasta '{pasta_monitorada}'... Pressione Ctrl+C para encerrar.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nMonitoramento encerrado.")
    observer.join()

if __name__ == "__main__":
    monitorar_pasta()