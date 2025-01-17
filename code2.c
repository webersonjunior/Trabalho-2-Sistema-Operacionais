#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_PASSAGEIROS 100000
#define NUM_VOOS 200          
#define NUM_ITERACOES 10      

typedef struct {
    int id;
    int id_voo;
    int peso_bagagem;
} Passageiro;

typedef struct {
    int id;
    int num_passageiros;
    int peso_total_bagagens;
} Voo;

int main() {
    //INICIALIZAR SEMENTE RANDOM
    srand(11111);

    Passageiro *passageiros = (Passageiro *)malloc(NUM_PASSAGEIROS * sizeof(Passageiro));
    Voo *voos = (Voo *)malloc(NUM_VOOS * sizeof(Voo));

    if (!passageiros || !voos) {
        printf("erro na alocacao");
        return 1;
    }

    for (int i = 0; i < NUM_VOOS; i++) {
        voos[i].id = i;
        voos[i].num_passageiros = 0;
        voos[i].peso_total_bagagens = 0;
    }

    for (int i = 0; i < NUM_PASSAGEIROS; i++) {
        passageiros[i].id = i;
        passageiros[i].id_voo = rand() % NUM_VOOS;
        passageiros[i].peso_bagagem = rand() % 30 + 1; 
    }

    // Simular atividades do aeroporto
    for (int iteracao = 0; iteracao < NUM_ITERACOES; iteracao++) {
        for (int i = 0; i < NUM_PASSAGEIROS; i++) {
            int id_voo = passageiros[i].id_voo;
            voos[id_voo].num_passageiros++;
            voos[id_voo].peso_total_bagagens += passageiros[i].peso_bagagem;
        }

        if (iteracao == NUM_ITERACOES - 1) {
            for (int i = 0; i < 10; i++) {
                printf("voo %d: %d passageiros\n%d kg de bagagem\n\n\n", 
                    voos[i].id, 
                    voos[i].num_passageiros, 
                    voos[i].peso_total_bagagens);
            }
        }
    }

    return 0;
}
