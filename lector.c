#include "data.h"

extern int leer_csv(const char *nombre_archivo, Articulo articulos[], int max_articulos);

int main(void) 
{
    Articulo articulos[MAX_ARTICULOS];
    int cantidad = leer_csv("datos.csv", articulos, MAX_ARTICULOS);

    printf("Se leyeron %d artículos del archivo.\n", cantidad);

    // Mostrar los primeros 3 artículos como ejemplo
    for (int i = 0; i < cantidad && i < 3; i++) 
    {
        printf("Artículo #%d: %s - %s - %s\n", i + 1, articulos[i].num_orden_com, articulos[i].desc_articulo, articulos[i].total);
    }

    return 0;
}
