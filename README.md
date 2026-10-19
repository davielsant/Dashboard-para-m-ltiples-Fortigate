# 🛡️ FortiGate: Informe Completo de Seguridad Gestionada

Un dashboard profesional e integral para **Grafana** diseñado para visualizar telemetría, tráfico, eventos del sistema y amenazas de seguridad de múltiples firewalls **FortiGate**, actuando como un sustituto directo del reporte gestionado de **FortiAnalyzer**.

---

## 📋 Descripción General

Este dashboard permite monitorear y auditar de forma centralizada la infraestructura FortiGate. Procesa eventos y logs en formato **syslog** recolectados por **Wazuh** y almacenados en un backend **OpenSearch / Elasticsearch**.

### 🛠️ Características Clave
* **Sustituto de FortiAnalyzer:** Mapea las métricas principales de los informes ejecutivos y técnicos de FortiAnalyzer.
* **Integración con Wazuh & OpenSearch:** Consultas optimizadas en Lucene para decodificadores y reglas de FortiGate (`rule.groups: fortigate`, `rule.id: 81600 TO 81646`, etc.).
* **Soporte Multidispositivo / Multi-VDOM:** Filtrado dinámico por agente de Wazuh, nombre de equipo (`devname`), número de serie (`devid`), VDOM (`vd`) e interfaces de red.
* **Feed Forense en Tiempo Real:** Visor de logs en streaming para auditoría y respuesta a incidentes en vivo.

---

## 📊 Estructura del Dashboard

El dashboard se organiza modularmente en **8 secciones principales**:

### 1. 📌 Estado e Inventario del Equipo (Device Inventory)
* **Datos de Inventario:** Nombre del equipo, modelo de hardware, IP de monitoreo, versión de FortiOS y número de serie (`devid`).
* **Estado Operativo:** Conteo de equipos FortiGate activos transmitiendo telemetría.
* **Políticas Activas:** Top de políticas de firewall más utilizadas.

### 2. 📊 Estadísticas Generales de Tráfico (Traffic & Protocols)
* **Métricas Principales:** Total de sesiones/flujos procesados, volumen de eventos de tráfico, usuarios/IPs únicas conectadas, aplicaciones únicas y destinos remotos alcanzados.
* **Rendimiento Temporal:** Gráfico de evolución temporal de flujos salientes (Tx) y entrantes (Rx).
* **Distribución:** Ranking de protocolos/servicios más usados y desglose por interfaces origen (`srcintf`) y destino (`dstintf`).

### 3. 🚀 Navegación y Control de Aplicaciones (Application Visibility)
* **Categorías de Aplicaciones:** Distribución del ancho de banda por categorías de aplicaciones (Social Media, Collaboration, Network.Service, etc.).
* **Ranking de Aplicaciones:** Matriz con Nivel de Riesgo (Risk Level), Categoría, Usuarios y Sesiones.
* **Top Consumo por Usuario:** Desglose de aplicaciones utilizadas por cliente/IP interna.

### 4. 🌐 Filtrado Web y Navegación (Web Filtering)
* **Uso por Categoría Web:** Distribución de peticiones según categorías FortiGuard (IT, Search Engines, Social, etc.).
* **Tráfico por Sitio/Dominio:** Desglose de consumo de ancho de banda y peticiones por dominio (`hostname`).
* **Usuarios más Activos:** Ranking de clientes internos con mayor volumen de navegación HTTP/HTTPS.

### 5. 🔐 Seguridad del Sistema y Auditoría (System Security)
* **Eventos por Severidad:** Gráficos de distribución y evolución temporal por niveles (Critical, Error, Warning, Notice, Info).
* **Auditoría de Administración:** 
  * Inicios de sesión de administradores exitosos (`Admin Logins`) por usuario e IP.
  * Intentos fallidos de autenticación en la gestión (`Failed Logins`).
  * Auditoría de cambios de configuración (`Config Changes Audit`) sobre objetos o políticas (`cfgpath`, `action`).

### 6. 🛡️ Aplicaciones y Categorías Bloqueadas / Alto Riesgo
* **Aplicaciones Prohibidas:** Registro de bloqueos por la política de *Application Control*.
* **Aplicaciones de Alto Riesgo:** Detección de aplicaciones con riesgo *High* o *Critical* (P2P, Proxies, VPNs no autorizadas) y los usuarios asociados.
* **Web Filtering Bloqueado:** Categorías y sitios web bloqueados por políticas de seguridad web.
* **Detección de Phishing:** Peticiones registradas hacia URLs catalogadas como Phishing, Spam o Maliciosas.

### 7. 🛡️ Accesos y Conexiones VPN (SSL-VPN e IPsec)
* **Monitoreo de Teletrabajadores:** Matriz de usuarios VPN activos e históricos, IP remota pública, tipo de túnel (SSL/IPsec) y duración promedio de sesión.
* **Auditoría de Fallas:** Total y detalle de intentos fallidos de conexión VPN (usuarios y top IPs atacantes).
* **Túneles Site-to-Site:** Estado de gateways e interfaces IPsec inter-sucursal.
* **Geolocalización:** Mapa mundial de conexiones VPN por país de destino (`dstcountry`).
* **Ancho de Banda VPN:** Evolución del tráfico transferido/recibido en túneles.

### 8. 🚨 Amenazas Detectadas (IPS, Malware & DoS)
* **Indicadores de Intrusion (IPS):**
  * Total de ataques IPS bloqueados (`dropped`) vs. solo detectados (`detected/pass`).
  * Total de incidentes catalogados con severidad *Critical*.
  * Top 10 de firmas de ataque y exploits más recurrentes.
  * Análisis de vectores de ataque (dirección `incoming` / `outgoing`).
  * Top de IPs atacantes (origen) y víctimas (destino).
* **Motor Antivirus:** Detección de malware, virus identificados, archivos involucrados y hosts internos infectados (`srcip`).
* **Anomalías de Red:** Inundaciones DoS (SYN/ICMP Flood) y encabezados anómalos.

---

## ⚙️ Requisitos e Instalación

### Requisitos Previos
1. **Grafana** (v10.x / v11.x o superior).
2. **Fuente de Datos:** Plugin de data source **OpenSearch / Elasticsearch** configurado en Grafana apuntando a tu clúster de Wazuh (nombre por defecto sugerido: `Wazuh-CGMA`).
3. **Agente Wazuh / Syslog:** FortiGate enviando logs syslog a Wazuh con los decodificadores estándar habilitados.

### Pasos de Importación
1. Descarga el archivo JSON del panel: `FORTIGATE_ Informe Completo de Seguridad Gestionada (FortiAnalyzer).json`.
2. En Grafana, ve a **Dashboards** ➔ **New** ➔ **Import**.
3. Sube el archivo JSON o pega su contenido.
4. Selecciona tu DataSource de **OpenSearch/Wazuh** cuando se te solicite.
5. Haz clic en **Import**.

---

## 🔧 Selectores del Dashboard (Dashboard Variables)

El panel cuenta únicamente con **dos selectores principales** en la barra superior para filtrar todas las métricas y paneles de forma dinámica:
* **`$agent_group` (Grupo de Agentes):** Permite filtrar los datos para todos los grupos o para un grupo de agentes Wazuh específico (`agent.labels.group`).
* **`$agent_name` (Agente Wazuh):** Permite mostrar los datos de todos los agentes o de un agente específico (`agent.name`).

### 📌 ¿Cómo reconoce Wazuh los Grupos en los Logs?
Por diseño, la interfaz de Wazuh muestra la columna *groups* porque consulta directamente la base de datos interna de la API de Wazuh Manager (`GET /agents`). Sin embargo, en **Discover** (índice `wazuh-alerts-*`), los eventos individuales no traen un parámetro `group` por defecto.

Para que los logs en OpenSearch/Grafana contengan el grupo del agente, se utiliza el mecanismo nativo de Wazuh: **Etiquetas de Agente (Agent Labels)**:
1. En el Wazuh Manager, edita la configuración centralizada del grupo (en `/var/ossec/etc/shared/<nombre_grupo>/agent.conf` o desde la GUI en **Management > Groups > [Tu Grupo] > Edit group configuration**).
2. Añade el bloque `<labels>` con la clave `group`:
   ```xml
   <agent_config>
     <labels>
       <label key="group">nombre_de_tu_grupo</label>
     </labels>
   </agent_config>
   ```
3. A partir de ese momento, cada alerta generada por los agentes de ese grupo incluirá automáticamente el campo `agent.labels.group: "nombre_de_tu_grupo"`, permitiendo que el selector de Grafana filtre inmediatamente los paneles.
4. En caso de ver la nota *No cached mapping for this field. Refresh field list from the Dashboards Management > Index Patterns page* en los eventos de Wazuh, el procedimiento correcto es: Menu de la interfaz Web de Wazuh / Dashboard Management / Index Patterns / Default Pattern / Refresh field list(flecha circular en la parte superior derecha).