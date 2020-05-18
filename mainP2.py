import subprocess

if __name__ == '__main__':
    print("Introduceti comanda:\n")
    command = input("")
    print("Se executa comanda...")
    subprocess.run(command, shell=True, stderr=subprocess.STDOUT)
    # ip a | grep inet | wc -l
    print("Se creeaza un pipeline...\n")
    lista_comenzi=command.split("|")
    vector_procese=[0]*len(lista_comenzi)
    print("Comenzile sunt:\n",lista_comenzi)
    vector_procese[0]=subprocess.Popen(lista_comenzi[0], shell=True, stdout=subprocess.PIPE)
    for i in range(1, len(lista_comenzi)-1):
        vector_procese[i]=subprocess.Popen(lista_comenzi[i], shell=True, stdin=vector_procese[i-1].stdout,
                                           stdout=subprocess.PIPE)
    vector_procese[len(lista_comenzi)-1]=subprocess.Popen(lista_comenzi[len(lista_comenzi)-1], shell=True,
                                                          stdin=vector_procese[len(lista_comenzi)-2].stdout)
    print("Rezultatul este: ")