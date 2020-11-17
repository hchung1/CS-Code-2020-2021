//Standard Libraries
#include <stdlib.h>
#include <stdio.h>

int transpose(size_t x, size_t y, int matrix[x][y]){
    
    //Memory
    int *matrix_t = malloc (sizeof (int) * y*x);
    
    //Transpose 2D
    for (int i = 0; i < x; i++){
        for (int j = 0; j < y; j++) {
            *(matrix_t+j*x+i) = matrix[i][j];
        }
    }
    for (int i = 0; i < y; i++){
        for (int j = 0; j < x; j++) {
            printf("%d  ", *(matrix_t+i*x+j));
            if (j == x - 1){printf("\n");}
        }
    }
}
int main(){
    // Data
    int a[1][4] = {{1,2,3,4}}; //1x4
    int b[4][4] = {{1,3,5,7},{2,4,6,8},{1,2,3,4},{5,6,7,8}}; //4x4

    //Find Size
    int x = sizeof(a)/sizeof(a[0]);
    int y = sizeof(a[0])/sizeof(a[0][0]);

    int x1 = sizeof(b)/sizeof(b[0]);
    int y1 = sizeof(b[0])/sizeof(b[0][0]);
    transpose(x,y,a);
    printf("\n\n");
    transpose(x1,y1,b);
    return 0;
}



