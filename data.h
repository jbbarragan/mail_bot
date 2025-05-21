/*
*@file: data.h
*@brief: este es el archivo de definiciones de tipo para el sitema de manejo de datos de facturas pendientes
*@author: Joshua Barragán 
*@date: verano 2025 
*
**/ 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINEA 1024
#define MAX_ARTICULOS 200
#define MAX_CADENA 100

typedef struct def_elemento{
    char num_orden_com[MAX_CADENA];
    char fecha_emision[MAX_CADENA];
    char fecha_prometida[MAX_CADENA];
    char fecha_firma[MAX_CADENA];
    char cve_depto[MAX_CADENA];
    char nombre_depto[MAX_CADENA];
    char programa[MAX_CADENA];
    char fondo[MAX_CADENA];
    char subcuenta[MAX_CADENA];
    char anio[MAX_CADENA];
    char cve_servicio[MAX_CADENA];
    char folio_req[MAX_CADENA];
    char consec_req[MAX_CADENA];
    char cant_requerida[MAX_CADENA];
    char cant_surtida[MAX_CADENA];
    char cant_surtir[MAX_CADENA];
    char unidad_medida[MAX_CADENA];
    char cve_articulo[MAX_CADENA];
    char desc_articulo[MAX_CADENA];
    char lineaid[MAX_CADENA];
    char reasign_comp[MAX_CADENA];
    char comprador[MAX_CADENA];
    char costo_unitario[MAX_CADENA];
    char descuento[MAX_CADENA];
    char iva[MAX_CADENA];
    char total[MAX_CADENA];
    char cve_proveedor[MAX_CADENA];
    char nombre_proveedor[MAX_CADENA];
    char cve_cond_pago[MAX_CADENA];
    char desc_cond_pago[MAX_CADENA];
    char fecha_ejercido_min[MAX_CADENA];
    char fecha_ejercido_max[MAX_CADENA];
    char cve_moneda[MAX_CADENA];
    char tipo_cambio[MAX_CADENA];
    char estatus[MAX_CADENA];
    char usuario_recibe[MAX_CADENA];
    char importe_total[MAX_CADENA];
    char importe_surt[MAX_CADENA];
    char importe_no_surt[MAX_CADENA];
    char almacen[MAX_CADENA];
    char reabast[MAX_CADENA];
    char contacto[MAX_CADENA];
    char consecutivo[MAX_CADENA];
    char fecha_recepcion_min_ord[MAX_CADENA];
    char fecha_recepcion_max_ord[MAX_CADENA];
    char fecha_recepcion_max_art[MAX_CADENA];
} Articulo;

