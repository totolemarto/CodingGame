#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdint.h>

#define SIZE 3
#define MAX_MEMO 40000000 


typedef struct configuration{
    uint32_t hash;
    uint32_t depth; // 0 <= depth <= 40
    uint32_t result;
} config;
   


typedef struct point{
    short line;
    short col;
} point;


typedef enum case_capture{
    TOP_RIGHT,
    TOP_BOTTOM,
    TOP_LEFT,
    RIGHT_BOTTOM,
    RIGHT_LEFT,
    BOTTOM_LEFT,
    TOP_RIGHT_BOTTOM,
    TOP_RIGHT_LEFT,
    TOP_BOTTOM_LEFT,
    RIGHT_BOTTOM_LEFT,
    TOP_RIGHT_BOTTOM_LEFT,
    NOTHING,
} capture;

typedef struct point_to_remove{
    capture to_remove[16];
    short size;
} point_to_remove;

inline static void add_and_convert(uint32_t current, uint32_t *total){
    *total = ( current + *total ) & 0x3FFFFFFF;
}


inline static uint32_t get_hash(short mat[SIZE][SIZE]){
    uint32_t result = 0;
    for (short i = 0; i < SIZE; i++){
        for (short j = 0; j < SIZE; j++){
            result = result * 10 + mat[i][j];
        }            
    }
    return result;
}

inline static void get_mat(uint32_t hash, short mat[SIZE][SIZE]){
    for (short i = 0; i < SIZE; i++){
        for (short j = 0; j < SIZE; j++){
            mat[i][j] = hash % 10;
            hash = hash / 10;
        }            
    }
    return;
}
/* Second paramétre devient une copie du premier
*/
inline static void reboot_mat(short mat[SIZE][SIZE], short tmp[SIZE][SIZE]){
    memcpy(tmp, mat, sizeof(short) * SIZE * SIZE);
}

inline static short get_value_cell(short line, short col, short mat[SIZE][SIZE]){
    if (line < 0 || line >= SIZE || col < 0 || col >= SIZE){
        return 10;
    }
    if (mat[line][col] == 0){
        return 10;
    }
    return mat[line][col];
}



point_to_remove get_all_capture(short mat[SIZE][SIZE], point begin){
    
    point_to_remove result;
    result.size = 0;
    short value_top = get_value_cell(begin.line -1, begin.col,  mat);// on est sur qu'au moins c'est faux
    short value_bottom = get_value_cell(begin.line + 1, begin.col,  mat);
    short value_right = get_value_cell(begin.line , begin.col + 1,  mat);
    short value_left = get_value_cell(begin.line , begin.col - 1,  mat);

    if (value_top + value_right <= 6 ){
        result.to_remove[result.size] = TOP_RIGHT;
        result.size++;
    }
    if (value_top + value_bottom <= 6 ){
        result.to_remove[result.size] = TOP_BOTTOM;
        result.size++;
    }
    if (value_top + value_left <= 6 ){
        result.to_remove[result.size] = TOP_LEFT;
        result.size++;
    }
    if (value_right + value_bottom <= 6 ){
        result.to_remove[result.size] = RIGHT_BOTTOM;
        result.size++;
    }
    if (value_right + value_left <= 6 ){
        result.to_remove[result.size] = RIGHT_LEFT;
        result.size++;
    }
    if (value_bottom + value_left <= 6 ){
        result.to_remove[result.size] = BOTTOM_LEFT;
        result.size++;
    }
    if (value_top + value_right + value_bottom <= 6 ){
        result.to_remove[result.size] = TOP_RIGHT_BOTTOM;
        result.size++;
    }
    if (value_top + value_right + value_left <= 6 ){
        result.to_remove[result.size] = TOP_RIGHT_LEFT;
        result.size++;
    }
    if (value_top + value_bottom + value_left <= 6 ){
        result.to_remove[result.size] = TOP_BOTTOM_LEFT;
        result.size++;
    }
    if (value_right + value_bottom + value_left <= 6 ){
        result.to_remove[result.size] = RIGHT_BOTTOM_LEFT;
        result.size++;
    }
    if ( value_top + value_right + value_bottom + value_left <= 6 ){
        result.to_remove[result.size] = TOP_RIGHT_BOTTOM_LEFT;
        result.size++;
    }
    if (result.size == 0){
        result.to_remove[0] = NOTHING;
        result.size = 1;
    }
    return result;
} 

void explore_all_possibility(short mat[SIZE][SIZE], uint32_t *total, int depth){
//    uint32_t le_hash = get_hash(mat);
  //  uint64_t le_hash_memo = le_hash * 100 + depth;
/*
    if ( memoisation[le_hash_memo] != 0 ){
        add_and_convert(memoisation[le_hash_memo], total);
        return le_hash;
    }
*/
    if (depth == 0){
        add_and_convert(get_hash(mat), total);
 //       memoisation[le_hash_memo] = le_hash;
        return; //le_hash;
    }
    uint32_t total_fun = 0;
    short to_call[81][SIZE][SIZE];
    short pass_once = 0;
    for (short i = 0; i < SIZE; i++){
        for (short j = 0; j < SIZE; j++){
            if (mat[i][j] == 0){
                point current ={i,j};
                point_to_remove todo = get_all_capture(mat, current);
                for (short indice = 0; indice < todo.size; indice++ ){
                    short new_value = 0;
                    reboot_mat(mat, to_call[pass_once]);
                    switch (todo.to_remove[indice]){
                        case TOP_RIGHT:
                            new_value = to_call[pass_once][i-1][j] + to_call[pass_once][i][j+1];
                            to_call[pass_once][i-1][j] = 0;
                            to_call[pass_once][i][j+1] = 0;
                            break;
                        case TOP_BOTTOM:
                            new_value = to_call[pass_once][i-1][j] + to_call[pass_once][i + 1][j];
                            to_call[pass_once][i-1][j] = 0;
                            to_call[pass_once][i + 1][j] = 0;
                            break;

                        case TOP_LEFT:
                            new_value = to_call[pass_once][i-1][j] + to_call[pass_once][i][j - 1];
                            to_call[pass_once][i-1][j] = 0;
                            to_call[pass_once][i][j - 1] = 0;
                            break;

                        case RIGHT_BOTTOM:
                            new_value = to_call[pass_once][i][j + 1] + to_call[pass_once][i + 1][j];
                            to_call[pass_once][i][j + 1] = 0;
                            to_call[pass_once][i + 1][j] = 0;
                            break;

                        case RIGHT_LEFT:
                            new_value = to_call[pass_once][i][j + 1] + to_call[pass_once][i][j - 1];
                            to_call[pass_once][i][j + 1] = 0;
                            to_call[pass_once][i][j - 1] = 0;
                            break;

                        case BOTTOM_LEFT:

                            new_value = to_call[pass_once][i + 1][j] + to_call[pass_once][i][j - 1];
                            to_call[pass_once][i + 1][j] = 0;
                            to_call[pass_once][i][j - 1] = 0;
                            break;
                        case TOP_RIGHT_BOTTOM:
                            new_value = to_call[pass_once][i-1][j] + to_call[pass_once][i][j+1] + to_call[pass_once][i + 1][j];
                            to_call[pass_once][i - 1][j] = 0;
                            to_call[pass_once][i][j + 1] = 0;
                            to_call[pass_once][i + 1][j] = 0;
                            break;

                        case TOP_RIGHT_LEFT:
                            new_value = to_call[pass_once][i-1][j] + to_call[pass_once][i][j+1] + to_call[pass_once][i][j - 1];
                            to_call[pass_once][i - 1][j] = 0;
                            to_call[pass_once][i][j + 1] = 0;
                            to_call[pass_once][i][j - 1] = 0;
                            break;

                        case TOP_BOTTOM_LEFT:
                            new_value = to_call[pass_once][i-1][j] + to_call[pass_once][i + 1][j] + to_call[pass_once][i][j - 1];
                            to_call[pass_once][i - 1][j] = 0;
                            to_call[pass_once][i + 1][j] = 0;
                            to_call[pass_once][i][j - 1] = 0;
                            break;

                        case RIGHT_BOTTOM_LEFT:
                            new_value = to_call[pass_once][i][j + 1] + to_call[pass_once][i + 1][j] + to_call[pass_once][i][j - 1];
                            to_call[pass_once][i][j + 1] = 0;
                            to_call[pass_once][i + 1][j] = 0;
                            to_call[pass_once][i][j - 1] = 0;
                            break;

                        case TOP_RIGHT_BOTTOM_LEFT:
                            new_value = to_call[pass_once][i-1][j] + to_call[pass_once][i + 1][j] + to_call[pass_once][i][j - 1] + to_call[pass_once][i][j + 1];
                            to_call[pass_once][i - 1][j] = 0;
                            to_call[pass_once][i + 1][j] = 0;
                            to_call[pass_once][i][j - 1] = 0;
                            to_call[pass_once][i][j + 1] = 0;
                            break;

                        case NOTHING:
                            new_value = 1;
                            break;
                    }
                    to_call[pass_once][i][j] = new_value;
                    //add_and_convert(explore_all_possibility(mat, total, depth - 1), &total_fun);
                    pass_once += 1;
                }
            }
        }            
    }
    if (pass_once == 0){
        //total_fun = le_hash;
        add_and_convert(get_hash(mat), total);
    } else{
        for (short i = 0; i < pass_once; i++){
            explore_all_possibility(to_call[i], total, depth - 1);
        }

    }
    //memoisation[le_hash_memo] = total_fun;
    return; //total_fun;
}

int main(int arc, char ** argv)
{
    int depth;
    uint32_t total = 0;
    uint32_t result = 0;
    //memoisation = calloc (sizeof(uint64_t),  MAX_MEMO); 
    short mat[SIZE][SIZE];
    FILE * f = fopen(argv[1], "r");
    fscanf(f, "%d", &depth);
    fprintf(stderr,"profondeur : %d \n", depth);

    for (short i = 0; i < SIZE; i++) {
        for (short j = 0; j < SIZE; j++) {
            fscanf(f, "%hd", &(mat[i][j]));
            fprintf(stderr, "%hd ", mat[i][j]);
        }
        fprintf(stderr,"\n");
    }
    
    explore_all_possibility(mat, &total, depth);
    printf("%d\n", total);
    fclose(f);
    /*
    mat[0][0] = 1;
    mat[0][2] = 1;

    get_hash(mat, &result);
    add_and_convert(result, &total);
    add_and_convert(result, &total);

    fprintf(stderr,"%d\n", result);
    */

    // Write an action using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");


    return 0;
}
