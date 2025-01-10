#include <stdio.h>

int main() {
    int tempoAnos = 100;
    double vInicial = 1000.0; 
    double taxaJuros = 0.05;  
    long double acumulado = 0.0;      
    double rendimento = 0.0;    
    long double totalRendimento = 0.0;  

    for (int ano = 1; ano <= tempoAnos; ano++) {
        rendimento = vInicial * taxaJuros;  
        acumulado += rendimento;              
        vInicial += rendimento;              
        totalRendimento += rendimento;       

        if (ano % 10 == 0) {
            taxaJuros += 0.001; 
        }
    }

    printf("Montante final: %.3Lf\n", acumulado);
    printf("Total de rendimentos: %.3Lf\n", totalRendimento);
    printf("Taxa de juros final: %.3f\n", taxaJuros);

    return 0;
}


