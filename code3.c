#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUMERO_MAQUINAS 5
#define OPERACOES_POR_MAQUINA 50000

typedef struct {
    int id_maquina;
    int pecas_produzidas;
    int iteracoes;
} Maquina;

void operar_maquina(Maquina *maquina) {
    for (int i = 0; i < OPERACOES_POR_MAQUINA; i++) {
        maquina->pecas_produzidas += rand() % 10;
        maquina->iteracoes += rand() % 5;
        
        if (maquina->pecas_produzidas % 100 == 0) {
            maquina->iteracoes += 1;
        }
    }
}

int main() {
    srand(11111); 

    Maquina maquinas[NUMERO_MAQUINAS];

    for (int i = 0; i < NUMERO_MAQUINAS; i++) {
        maquinas[i].id_maquina = i + 1;
        maquinas[i].pecas_produzidas = 0;
        maquinas[i].iteracoes = 0;
    }

    for (int i = 0; i < NUMERO_MAQUINAS; i++) {
        printf("iniciando maquina %d\n", maquinas[i].id_maquina);
        operar_maquina(&maquinas[i]);
        printf("maquina %d finalizou \npecas produzidas: %d\ntempo de operacao: %d\n\n\n",
               maquinas[i].id_maquina, maquinas[i].pecas_produzidas, maquinas[i].iteracoes);
    }

    return 0;
}