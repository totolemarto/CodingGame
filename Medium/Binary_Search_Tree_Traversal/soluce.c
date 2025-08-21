#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
struct tree{
    struct tree * gauche;
    struct tree * droite;
    int valeur;
};
typedef struct tree * noeud;
typedef noeud * arbre;

noeud creer_noeud(int valeur){
    noeud mon_arbre =  malloc(sizeof(struct tree));
    mon_arbre->gauche = NULL;
    mon_arbre->droite = NULL;
    mon_arbre->valeur = valeur;
    return (mon_arbre);
}

void rajouter_noeud(arbre mon_arbre, int valeur){
    if (!(*mon_arbre)){
        (*mon_arbre) = creer_noeud(valeur);
        return;
    }
    if ((*mon_arbre) ->valeur > valeur && !(*mon_arbre)->gauche ){
        (*mon_arbre)->gauche = creer_noeud(valeur);
        return;
    }
    if ((*mon_arbre) ->valeur < valeur && !(*mon_arbre)->droite ){
        (*mon_arbre)->droite = creer_noeud(valeur);
        return;
    }
     if ((*mon_arbre) ->valeur > valeur){
        rajouter_noeud(&(*mon_arbre)->gauche, valeur);
        return;
     }
     if ((*mon_arbre) ->valeur < valeur){
        rajouter_noeud(&(*mon_arbre)->droite, valeur);
        return;
     }
}

void parcours_arbre_prefixe(arbre mon_arbre, int * i){
    if (!(*mon_arbre)){
        return;
    }
    if (*i == 0){
        printf("%d", (*mon_arbre)->valeur);
        *i = 2;
    }else
        printf(" %d", (*mon_arbre)->valeur);
    parcours_arbre_prefixe(&(*mon_arbre)->gauche, i);
    parcours_arbre_prefixe(&(*mon_arbre)->droite, i);
}

void parcours_arbre_infixe(arbre mon_arbre, int * i){
    if (!(*mon_arbre)){
        return;
    }
    parcours_arbre_infixe(&(*mon_arbre)->gauche, i);
    if (*i == 0){
        printf("%d", (*mon_arbre)->valeur);
        *i = 2;
    }else
        printf(" %d", (*mon_arbre)->valeur);
    parcours_arbre_infixe(&(*mon_arbre)->droite, i);
}

void parcours_arbre_sufixe(arbre mon_arbre, int * i){
    if (!(*mon_arbre)){
        return;
    }
    parcours_arbre_sufixe(&(*mon_arbre)->gauche, i);
    parcours_arbre_sufixe(&(*mon_arbre)->droite, i);
    if (*i == 0){
        printf("%d", (*mon_arbre)->valeur);
        *i = 2;
    }else
        printf(" %d", (*mon_arbre)->valeur);
}

void parcours_largeur(arbre mon_arbre){
    noeud *file = calloc(100, sizeof(noeud)) ;
    file[0] = *mon_arbre;
    int pos_actu = 0;
    int to_add = 1;
    while (file[pos_actu]){
        if (file[pos_actu]->gauche){
            file[to_add] = file[pos_actu]->gauche;
            to_add ++;
        }
        if (file[pos_actu]->droite){
            file[to_add] = file[pos_actu]->droite;
            to_add ++;
        } 
        if (pos_actu == 0){
            printf("%d", file[pos_actu]->valeur);
        } else{
            printf(" %d", file[pos_actu]->valeur);
        }
        pos_actu += 1;
    }
    return;
}

int main()
{
    arbre mon_arbre = malloc(sizeof(noeud));
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int vi;
        scanf("%d", &vi);
        if (i != 0){
            rajouter_noeud(mon_arbre, vi);
        } else{
            *mon_arbre = creer_noeud(vi);
        }
    }
    int i = 0;
    parcours_arbre_prefixe(mon_arbre, &i);
    printf("\n");
    i = 0;
    parcours_arbre_infixe(mon_arbre, &i);
    printf("\n");
    i = 0;
    
    parcours_arbre_sufixe(mon_arbre, &i);
    printf("\n");
    i = 0;
    parcours_largeur(mon_arbre);

    return 0;
}
