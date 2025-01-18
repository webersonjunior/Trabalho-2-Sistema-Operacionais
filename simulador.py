from collections import deque


class tlb_fifo:
    def __init__(self, max_tamanho):
        self.max_tamanho = max_tamanho
        self.fila = []

    def add(self, item):
        if len(self.fila) >= self.max_tamanho:
            self.fila.pop(0)  # Remove o mais antigo
        self.fila.append(item)

    def __contains__(self, item):
        return item in self.fila  # Verifica se o item está na fila



def simular_tlb_fifo(arquivo_trace, tamanho_tlb):
    tlb_instrucoes = tlb_fifo(tamanho_tlb)  
    tlb_dados = tlb_fifo(tamanho_tlb)       
    falhas_instrucoes, falhas_dados = 0, 0
    total_instrucoes, total_dados = 0, 0
    with open(arquivo_trace, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            
            if linha.startswith("=="):
                continue
            
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
                    tlb_instrucoes.add(pagina) 

            elif operacao in ("L", "S", "M"):  
                total_dados += 1  

                if operacao == "M":
                    total_dados += 1  

                if pagina not in tlb_dados:
                    falhas_dados += 1  
                    tlb_dados.add(pagina) 


    taxa_falhas_instrucoes = (falhas_instrucoes / total_instrucoes) * 100 if total_instrucoes else 0
    taxa_falhas_dados = (falhas_dados / total_dados) * 100 if total_dados else 0
    return taxa_falhas_instrucoes, taxa_falhas_dados

arquivo_trace = input("Digite o nome do arquivo de trace: ")
for tamanho in [4, 8, 16, 32, 64, 128]: 
    taxa_instrucoes, taxa_dados = simular_tlb_fifo(arquivo_trace, tamanho_tlb=tamanho)
    print(f"Tamanho da TLB: {tamanho}, Taxa de Falhas (Instruções): {taxa_instrucoes:.5f}%, Taxa de Falhas (Dados): {taxa_dados:.5f}%")

