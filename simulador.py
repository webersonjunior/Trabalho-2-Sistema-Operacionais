from collections import deque

def simular_tlb_fifo(arquivo_trace, tamanho_tlb):
    # Estruturas para TLB separadas de instruções e dados
    tlb_instrucoes = deque(maxlen=tamanho_tlb)  # TLB para instruções
    tlb_dados = deque(maxlen=tamanho_tlb)       # TLB para dados

    # Contadores de acessos e falhas
    falhas_instrucoes, falhas_dados = 0, 0
    total_instrucoes, total_dados = 0, 0

    # Leitura do arquivo de trace
    with open(arquivo_trace, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()  # Remove espaços em branco no início e fim
            if not linha:  # Ignorar linhas vazias
                continue

            partes = linha.split()
            if len(partes) < 2:  # Ignorar linhas mal formatadas
                continue

            try:
                operacao, endereco = partes[0], partes[1].split(',')[0]
                pagina = endereco[:-3]  # Remove os 12 bits de deslocamento (tamanho da página)
            except IndexError:
                continue  # Ignorar caso falte algum campo necessário

            if operacao == "I":  # Acesso a instrução
                total_instrucoes += 1
                if pagina not in tlb_instrucoes:
                    falhas_instrucoes += 1  # Falha na TLB
                    tlb_instrucoes.append(pagina)  # Adicionar a nova página na TLB

            elif operacao in ("L", "S"):  # Acesso a dados (load ou store)
                total_dados += 1
                if pagina not in tlb_dados:
                    falhas_dados += 1  # Falha na TLB
                    tlb_dados.append(pagina)  # Adicionar a nova página na TLB

    # Cálculo da taxa de falhas
    taxa_falhas_instrucoes = (falhas_instrucoes / total_instrucoes) * 100 if total_instrucoes else 0
    taxa_falhas_dados = (falhas_dados / total_dados) * 100 if total_dados else 0

    return taxa_falhas_instrucoes, taxa_falhas_dados

# Entrada dinâmica para o usuário
arquivo_trace = input("Digite o nome do arquivo de trace: ")
for tamanho in [4, 8, 16, 32, 64, 128]:  # Diferentes tamanhos de TLB
    taxa_instrucoes, taxa_dados = simular_tlb_fifo(arquivo_trace, tamanho_tlb=tamanho)
    print(f"Tamanho da TLB: {tamanho}, Taxa de Falhas (Instruções): {taxa_instrucoes:.2f}%, Taxa de Falhas (Dados): {taxa_dados:.2f}%")

