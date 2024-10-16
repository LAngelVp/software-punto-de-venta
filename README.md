# Sistema de Punto de Venta (POS) Genérico

Este repositorio contiene un Sistema de Punto de Venta (POS) genérico desarrollado en Python con PyQt6 para el entorno de escritorio y utilizando PostgreSQL como base de datos. El POS está diseñado para ser flexible y adaptable a diferentes tipos de negocios, proporcionando funcionalidades básicas para la gestión de ventas, inventario y generación de informes.

## Características Principales

- Gestión de productos: Agregar, eliminar, actualizar y buscar productos en el inventario.
- Procesamiento de ventas: Realizar ventas, calcular el total y generar recibos.
- Gestión de clientes: Registrar y mantener información de clientes.
- Informes de ventas: Generar informes sobre ventas, productos más vendidos, etc.

## Tecnologías Utilizadas

- **Python**: Utilizado para la lógica de negocio y la implementación del POS.
- **PyQt6**: Biblioteca de Python para crear aplicaciones de escritorio.
- **PostgreSQL**: Base de datos relacional utilizada para almacenar datos de forma persistente.

## Configuración del Entorno

Para ejecutar este POS en tu máquina local, sigue estos pasos:

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener instalado Python (versión X.X) y PyQt6 en tu sistema.
3. Instala las dependencias de Python ejecutando el siguiente comando:
    ```bash
    pip install -r requirements.txt
    ```
4. Configura la conexión a la base de datos PostgreSQL en el archivo `config.py`.
5. Ejecuta PostgreSQL en un contenedor Docker asignándole el puerto 5432 del host al contenedor utilizando el siguiente comando:
    ```bash
    docker container run \
    --name postgres-alpha \
    -e POSTGRES_USER=DevelopmentTeam \
    -e POSTGRES_PASSWORD=DevelopmentTeam \
    -dp 5432:5432 \
    postgres:12.19-alpine3
    ```
6. Inicia la aplicación de escritorio ejecutando el siguiente comando:
    ```bash
    python Login.py
    ```

## Contribución

¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una rama con una descripción clara de tu función o corrección.
3. Realiza tus cambios y asegúrate de seguir las guías de estilo del proyecto.
4. Realiza un pull request a la rama principal de este repositorio.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto con nosotros a través de los issues de GitLab o por correo electrónico.
#   s o f t w a r e - p u n t o - d e - v e n t a  
 