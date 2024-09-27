import os

# Respostas esperadas para clima
resps_clima = {
    "ensolarado": "Seco",
    "chuvoso": "Molhado",
    "nublado": "Intermediário"
}

# Função para recomendar pneus com base nas condições do clima
def recomenda_pneus(clima):
    if clima == 'ensolarado':
        return 'Pneus slick'
    elif clima == 'chuvoso':
        return 'Pneus de chuva'
    else:
        return 'Pneus intermediários'

# Função para configurar piloto
def escolha_do_piloto():
    pilotos = ['Nyck de Vries', 'Edoardo Mortara']
    while True:
        print("Escolha o piloto:")
        for i, piloto in enumerate(pilotos, start=1):
            print(f"{i}: {piloto}")
        
        escolha = int(input("Digite o número do piloto desejado: "))
        if 1 <= escolha <= len(pilotos):
            return pilotos[escolha - 1]
        else:
            print("Escolha inválida. Tente novamente.")

# Função para escolher pista
def escolha_da_pista():
    pistas = ['Mônaco', 'Interlagos', 'Detroit']
    while True:
        print("Escolha a pista:")
        for i, pista in enumerate(pistas, start=1):
            print(f"{i}: {pista}")
        
        escolha = int(input("Digite o número da pista desejada: "))
        if 1 <= escolha <= len(pistas):
            return pistas[escolha - 1]
        else:
            print("Escolha inválida. Tente novamente.")

# Função para ajustar o desempenho do piloto baseado na pista
def desempenho_do_piloto(piloto, pista):
    desempenho = {
        'Nyck de Vries': {
            'Mônaco': 'Excelente',
            'Interlagos': 'Bom',
            'Detroit': 'Regular',
        },
        'Edoardo Mortara': {
            'Mônaco': 'Bom',
            'Interlagos': 'Excelente',
            'Detroit': 'Regular',
        }
    }
    return desempenho[piloto][pista]

# Função principal do simulador
def simulador():
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("Bem-vindo ao Simulador de Configuração de Corrida da Mahindra Formula E!")

        # Previsão do tempo
        clima = ''
        while clima not in ['ensolarado', 'chuvoso', 'nublado']:
            clima = input("Qual é a previsão do tempo (ensolarado/chuvoso/nublado)? ").lower()
            if clima not in ['ensolarado', 'chuvoso', 'nublado']:
                print("Entrada inválida. Tente novamente.")
        
        # Escolha do piloto
        piloto = escolha_do_piloto()

        # Escolha da pista
        pista = escolha_da_pista()

        # Recomendação de pneus
        pneus_recomendados = recomenda_pneus(clima)
        
        # Ajuste de desempenho do piloto baseado na pista
        desempenho = desempenho_do_piloto(piloto, pista)
        
        # Condições do clima esperadas
        condicao_clima = resps_clima[clima]

        # Resultados finais bonitinhos
        print("\n" + "="*40)
        print("         Configurações da Corrida")
        print("="*40)
        print(f"Pista:                    {pista}")
        print(f"Piloto escolhido:         {piloto}")
        print(f"Previsão do tempo:        {clima.capitalize()}")
        print(f"Condição de pista esperada: {condicao_clima}")
        print(f"Pneus recomendados:       {pneus_recomendados}")
        print(f"Provavel desempenho:     {desempenho}")
        print("="*40)

        # Detalhar o tipo de pneus utilizados
        print("\nDetalhes dos pneus utilizados baseados no clima:")
        print("  - Ensolarado:            Pneus slick")
        print("  - Chuvoso:               Pneus de chuva")
        print("  - Nublado:               Pneus intermediários")
        print("="*40)

        # Perguntar ao usuário se deseja configurar outra corrida
        cont = input("\nDeseja configurar outra corrida? Digite 'sim' para continuar ou 'não' para concluir: ").lower()
        if cont == 'não':
            break

# Executar o simulador
if __name__ == "__main__":
    simulador()