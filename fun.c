/*
*@file: fun.c
*@brief: este es el archivo de dunciones para el manejo de datos de facturas pendientes
*@author: Joshua Barragán 
*@date: verano 2025 
*
**/ 
#include "data.h"

int leer_csv(const char *nombre_archivo, Articulo articulos[], int max_articulos) 
{
    FILE *archivo = fopen(nombre_archivo, "rt");
    if (archivo == NULL) 
    {
        perror("Error al abrir el archivo");
        return 0;
    }

    char linea[MAX_LINEA];
    int i = 0, linea_actual = 0;

    // Saltar primeras 5 líneas
    while (linea_actual < 5 && fgets(linea, sizeof(linea), archivo)) 
    {
        linea_actual++;
    }

    // Leer los artículos
    while (fgets(linea, sizeof(linea), archivo) && i < max_articulos) 
    {
        char *token = strtok(linea, ",");
        int j = 0;
        while (token != NULL && j < 46) 
        {
            switch (j) 
            {
                case 0: strcpy(articulos[i].num_orden_com, token); break;
                case 1: strcpy(articulos[i].fecha_emision, token); break;
                case 2: strcpy(articulos[i].fecha_prometida, token); break;
                case 3: strcpy(articulos[i].fecha_firma, token); break;
                case 4: strcpy(articulos[i].cve_depto, token); break;
                case 5: strcpy(articulos[i].nombre_depto, token); break;
                case 6: strcpy(articulos[i].programa, token); break;
                case 7: strcpy(articulos[i].fondo, token); break;
                case 8: strcpy(articulos[i].subcuenta, token); break;
                case 9: strcpy(articulos[i].anio, token); break;
                case 10: strcpy(articulos[i].cve_servicio, token); break;
                case 11: strcpy(articulos[i].folio_req, token); break;
                case 12: strcpy(articulos[i].consec_req, token); break;
                case 13: strcpy(articulos[i].cant_requerida, token); break;
                case 14: strcpy(articulos[i].cant_surtida, token); break;
                case 15: strcpy(articulos[i].cant_surtir, token); break;
                case 16: strcpy(articulos[i].unidad_medida, token); break;
                case 17: strcpy(articulos[i].cve_articulo, token); break;
                case 18: strcpy(articulos[i].desc_articulo, token); break;
                case 19: strcpy(articulos[i].lineaid, token); break;
                case 20: strcpy(articulos[i].reasign_comp, token); break;
                case 21: strcpy(articulos[i].comprador, token); break;
                case 22: strcpy(articulos[i].costo_unitario, token); break;
                case 23: strcpy(articulos[i].descuento, token); break;
                case 24: strcpy(articulos[i].iva, token); break;
                case 25: strcpy(articulos[i].total, token); break;
                case 26: strcpy(articulos[i].cve_proveedor, token); break;
                case 27: strcpy(articulos[i].nombre_proveedor, token); break;
                case 28: strcpy(articulos[i].cve_cond_pago, token); break;
                case 29: strcpy(articulos[i].desc_cond_pago, token); break;
                case 30: strcpy(articulos[i].fecha_ejercido_min, token); break;
                case 31: strcpy(articulos[i].fecha_ejercido_max, token); break;
                case 32: strcpy(articulos[i].cve_moneda, token); break;
                case 33: strcpy(articulos[i].tipo_cambio, token); break;
                case 34: strcpy(articulos[i].estatus, token); break;
                case 35: strcpy(articulos[i].usuario_recibe, token); break;
                case 36: strcpy(articulos[i].importe_total, token); break;
                case 37: strcpy(articulos[i].importe_surt, token); break;
                case 38: strcpy(articulos[i].importe_no_surt, token); break;
                case 39: strcpy(articulos[i].almacen, token); break;
                case 40: strcpy(articulos[i].reabast, token); break;
                case 41: strcpy(articulos[i].contacto, token); break;
                case 42: strcpy(articulos[i].consecutivo, token); break;
                case 43: strcpy(articulos[i].fecha_recepcion_min_ord, token); break;
                case 44: strcpy(articulos[i].fecha_recepcion_max_ord, token); break;
                case 45: strcpy(articulos[i].fecha_recepcion_max_art, token); break;
            }
            token = strtok(NULL, ",");
            j++;
        }
        i++;
    }

    fclose(archivo);
    return i;
}