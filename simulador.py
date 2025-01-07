from collections import deque

def simular_tlb_fifo(arquivo_trace, tamanho_tlb):
    tlb_instrucoes = deque(maxlen=tamanho_tlb)  
    tlb_dados = deque(maxlen=tamanho_tlb)       
    falhas_instrucoes, falhas_dados = 0, 0
    total_instrucoes, total_dados = 0, 0
    with open(arquivo_trace, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha: 
                continue

            partes = linha.split()
            if len(partes) < 2: 
                continue

            try:
                operacao, endereco = partes[0], partes[1].split(',')[0]
                pagina = endereco[:-3] 
            except IndexError:
                continue  

            if operacao == "I":  
                total_instrucoes += 1
                if pagina not in tlb_instrucoes:
                    falhas_instrucoes += 1  
                    tlb_instrucoes.append(pagina) 

            elif operacao in ("L", "S"):  
                total_dados += 1
                if pagina not in tlb_dados:
                    falhas_dados += 1  
                    tlb_dados.append(pagina) 

    taxa_falhas_instrucoes = (falhas_instrucoes / total_instrucoes) * 100 if total_instrucoes else 0
    taxa_falhas_dados = (falhas_dados / total_dados) * 100 if total_dados else 0
    return taxa_falhas_instrucoes, taxa_falhas_dados

arquivo_trace = input("Digite o nome do arquivo de trace: ")
for tamanho in [4, 8, 16, 32, 64, 128]: 
    taxa_instrucoes, taxa_dados = simular_tlb_fifo(arquivo_trace, tamanho_tlb=tamanho)
    print(f"Tamanho da TLB: {tamanho}, Taxa de Falhas (Instruções): {taxa_instrucoes:.2f}%, Taxa de Falhas (Dados): {taxa_dados:.2f}%")

