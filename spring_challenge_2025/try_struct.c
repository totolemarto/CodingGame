#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdint.h>

#define SIZE 3

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

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

typedef struct to_analyze{
    point points[9];
    short size;
} to_analyze;

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
/* Second paramétre devient une copie du premier
*/
inline static void reboot_mat(short mat[SIZE][SIZE], short tmp[SIZE][SIZE]){
    memcpy(tmp, mat, sizeof(short) * SIZE * SIZE);
}

inline static short get_value_cell(short line, short col, short mat[SIZE][SIZE]){
    if (line < 0 || line >= SIZE || col < 0 || col >= SIZE || mat[line][col] == 0){
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
        if (value_top + value_right + value_bottom <= 6 ){
            result.to_remove[result.size] = TOP_RIGHT_BOTTOM;
            result.size++;
            if ( value_top + value_right + value_bottom + value_left <= 6 ){
                result.to_remove[result.size] = TOP_RIGHT_BOTTOM_LEFT;
                result.size++;
            }
        }
        if (value_top + value_right + value_left <= 6 ){
            result.to_remove[result.size] = TOP_RIGHT_LEFT;
            result.size++;
        }
    }
    if (value_top + value_bottom <= 6 ){
        result.to_remove[result.size] = TOP_BOTTOM;
        result.size++;
        if (value_top + value_bottom + value_left <= 6 ){
            result.to_remove[result.size] = TOP_BOTTOM_LEFT;
            result.size++;
        }
    }
    if (value_right + value_bottom <= 6 ){
        result.to_remove[result.size] = RIGHT_BOTTOM;
        result.size++;
        if (value_right + value_bottom + value_left <= 6 ){
            result.to_remove[result.size] = RIGHT_BOTTOM_LEFT;
            result.size++;
        }
    }
    if (value_top + value_left <= 6 ){
        result.to_remove[result.size] = TOP_LEFT;
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
    if (result.size == 0){
        result.to_remove[0] = NOTHING;
        result.size = 1;
    }
    return result;
} 

static inline void reboot_point(to_analyze *source, to_analyze *destination){
    memcpy(destination, source, sizeof(to_analyze));
}


static inline short modify_struct_point(short mat[SIZE][SIZE], to_analyze *all_points, to_analyze new_points){
    short result = 0;
    for (short i = 0; i < new_points.size; i++){
        result += mat[new_points.points[i].line][new_points.points[i].col];
        mat[new_points.points[i].line][new_points.points[i].col] = 0;
        all_points->points[all_points->size].line  = new_points.points[i].line;
        all_points->points[all_points->size].col =   new_points.points[i].col;
        all_points->size++;
    }
    return result;
}

void explore_all_possibility(short mat[SIZE][SIZE], uint32_t *total, int depth, to_analyze all_points){
    if (depth == 0 || all_points.size == 0){
        add_and_convert(get_hash(mat), total);
        return;
    }
    to_analyze tmp_analyze;
    reboot_point(&all_points, &tmp_analyze);
    short tmp[SIZE][SIZE];
    reboot_mat(mat, tmp);
    short pass_once = 0;

    for (short indice_point = 0; indice_point < all_points.size; indice_point++){
        point current = all_points.points[indice_point];
        point_to_remove todo = get_all_capture(mat, current);
        short i = current.line;
        short j = current.col;
        for (short indice = 0; indice < todo.size; indice++ ){
            short new_value = 0;
            to_analyze new_point;
            switch (todo.to_remove[indice]){
                case TOP_RIGHT:
                    new_value = mat[i-1][j];
                    all_points.points[indice_point].line = i - 1;
                    all_points.points[indice_point].col = j;
                    new_point.size = 1;
                    new_point.points[0].line = i;
                    new_point.points[0].col = j + 1;
                    new_value += modify_struct_point(mat, &all_points, new_point);
                    break;
                case TOP_BOTTOM:
                    new_value = mat[i-1][j];
                    all_points.points[indice_point].line = i - 1;
                    all_points.points[indice_point].col = j;
                    new_point.size = 1;
                    new_point.points[0].line = i + 1;
                    new_point.points[0].col = j;
                    new_value += modify_struct_point(mat, &all_points, new_point);
                    break;

                case TOP_LEFT:
                    new_value = mat[i-1][j];
                    all_points.points[indice_point].line = i - 1;
                    all_points.points[indice_point].col = j;
                    new_point.size = 1;
                    new_point.points[0].line = i;
                    new_point.points[0].col = j - 1;
                    new_value += modify_struct_point(mat, &all_points, new_point);
                    break;

                case RIGHT_BOTTOM:
                    new_value = mat[i][j + 1];
                    all_points.points[indice_point].line = i;
                    all_points.points[indice_point].col = j + 1;
                    new_point.size = 1;
                    new_point.points[0].line = i + 1;
                    new_point.points[0].col = j;
                    new_value += modify_struct_point(mat, &all_points, new_point);
                    break;

                case RIGHT_LEFT:
                    new_value = mat[i][j + 1];
                    all_points.points[indice_point].line = i;
                    all_points.points[indice_point].col = j + 1;
                    new_point.size = 1;
                    new_point.points[0].line = i;
                    new_point.points[0].col = j - 1;
                    new_value += modify_struct_point(mat, &all_points, new_point);
                    break;

                case BOTTOM_LEFT:
                    new_value = mat[i+1][j];
                    all_points.points[indice_point].line = i + 1;
                    all_points.points[indice_point].col = j;
                    new_point.size = 1;
                    new_point.points[0].line = i;
                    new_point.points[0].col = j - 1;
                    new_value += modify_struct_point(mat, &all_points, new_point);
                    break;

                case TOP_RIGHT_BOTTOM:
                    new_value = mat[i-1][j];
                    all_points.points[indice_point].line = i - 1;
                    all_points.points[indice_point].col = j;
                    new_point.size = 2;
                    new_point.points[0].line = i;
                    new_point.points[0].col = j + 1;
                    new_point.points[1].line = i + 1;
                    new_point.points[1].col = j;
                    new_value += modify_struct_point(mat, &all_points, new_point);
                    break;

                case TOP_RIGHT_LEFT:
                    new_value = mat[i-1][j];
                    all_points.points[indice_point].line = i - 1;
                    all_points.points[indice_point].col = j;
                    new_point.size = 2;
                    new_point.points[0].line = i;
                    new_point.points[0].col = j + 1;
                    new_point.points[1].line = i;
                    new_point.points[1].col = j - 1;
                    new_value += modify_struct_point(mat, &all_points, new_point);
                    break;

                case TOP_BOTTOM_LEFT:
                    new_value = mat[i-1][j];
                    all_points.points[indice_point].line = i - 1;
                    all_points.points[indice_point].col = j;
                    new_point.size = 2;
                    new_point.points[0].line = i + 1;
                    new_point.points[0].col = j;
                    new_point.points[1].line = i;
                    new_point.points[1].col = j - 1;
                    new_value += modify_struct_point(mat, &all_points, new_point);
                    break;

                case RIGHT_BOTTOM_LEFT:
                    new_value = mat[i][j + 1];
                    all_points.points[indice_point].line = i;
                    all_points.points[indice_point].col = j + 1;
                    new_point.size = 2;
                    new_point.points[0].line = i + 1;
                    new_point.points[0].col = j;
                    new_point.points[1].line = i;
                    new_point.points[1].col = j - 1;
                    new_value += modify_struct_point(mat, &all_points, new_point);
                    break;

                case TOP_RIGHT_BOTTOM_LEFT:
                    new_value = mat[i-1][j];
                    all_points.points[indice_point].line = i - 1;
                    all_points.points[indice_point].col = j;
                    new_point.size = 3;
                    new_point.points[0].line = i;
                    new_point.points[0].col = j + 1;
                    new_point.points[1].line = i + 1;
                    new_point.points[1].col = j;
                    new_point.points[1].line = i;
                    new_point.points[1].col = j - 1;
                    new_value += modify_struct_point(mat, &all_points, new_point);
                    break;

                case NOTHING:
                    new_value = 1;
                    all_points.points[indice_point] = all_points.points[all_points.size - 1];
                    all_points.size--;
                    break;
            }
            mat[i][j] = new_value;
            explore_all_possibility(mat, total, depth - 1, all_points);
            reboot_mat(tmp, mat);
            reboot_point( &tmp_analyze, &all_points);
        }
    }
    return;
}

int main()
{
    int depth;
    uint32_t total = 0;
    uint32_t result = 0;
    short mat[SIZE][SIZE];
    scanf("%d", &depth);
    fprintf(stderr,"profondeur : %d \n", depth);
    to_analyze zero_value;
    zero_value.size = 0;
    for (short i = 0; i < SIZE; i++) {
        for (short j = 0; j < SIZE; j++) {
            scanf("%hd", &(mat[i][j]));
            fprintf(stderr, "%hd ", mat[i][j]);
            if (mat[i][j] == 0){
                point cur = {i,j};
                zero_value.points[zero_value.size] = cur;
                zero_value.size++;
            }
        }
        fprintf(stderr,"\n");
    }
    
    explore_all_possibility(mat, &total, depth, zero_value);
    printf("%d\n", total);

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
