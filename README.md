# Documentación de Infraestructura - Proyecto InnovaTech

## Introducción
Este proyecto presenta una solución integral de contenedorización para la plataforma InnovaTech. Se ha diseñado una arquitectura basada en microservicios que prioriza la seguridad, la persistencia de los datos y la automatización mediante procesos de CI/CD. La solución está preparada para ser desplegada en entornos de nube como AWS EC2, garantizando alta disponibilidad y aislamiento de recursos.

## Decisiones de Arquitectura

### Configuración de Contenedores y Optimización
Se ha optado por el uso de Dockerfiles con construcción de múltiples etapas (Multi-stage builds). Esta técnica permite separar el entorno de compilación del entorno de ejecución, resultando en imágenes significativamente más ligeras y seguras al no contener dependencias de desarrollo en el artefacto final.

### Seguridad y Segmentación de Redes
Se implementó un esquema de aislamiento mediante redes virtuales de Docker:
- **web_net:** Utilizada para la exposición controlada de los servicios hacia el exterior.
- **db_net:** Una red privada interna que restringe la comunicación de la base de datos únicamente al backend, eliminando cualquier vector de ataque externo hacia la capa de datos.

### Persistencia y Gestión de Volúmenes
Para la base de datos PostgreSQL, se definieron Volúmenes Nombrados (Named Volumes). Esta decisión asegura que la información crítica no dependa del ciclo de vida del contenedor, permitiendo actualizaciones de software o reinicios del sistema sin riesgo de pérdida de datos.

### Automatización CI/CD
El flujo de trabajo se integra con GitHub Actions, utilizando Secretos de GitHub para el almacenamiento seguro de credenciales. Esto permite que el proceso de construcción y publicación de imágenes sea automático, confiable y cumpla con las normativas de seguridad de no exponer claves en texto plano.

## Instrucciones para Ejecución Local

Para levantar el entorno completo en una estación de trabajo local, siga estos pasos:

1. Asegúrese de tener instalado Docker y Docker Compose.
2. Verifique la existencia del archivo de configuración de variables de entorno `.env` en la raíz del proyecto.
3. Ejecute el siguiente comando en la terminal:

```bash
docker-compose up -d