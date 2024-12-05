Documento Funcional de Requerimientos (DFR)
Carrito de Compras
Introducción
Este documento describe las funcionalidades, requisitos y diseño del proyecto Carrito de Compras, desarrollado utilizando el framework Django en Python. El sistema tiene como objetivo proporcionar una solución básica pero efectiva para gestionar un catálogo de productos, permitir a los usuarios agregar productos a un carrito de compras y simular el proceso de compra.
El proyecto es modular y sigue la arquitectura Modelo-Vista-Controlador (MVC) que Django implementa a través de sus componentes Modelos, Vistas, y Plantillas (Templates). A lo largo de este documento, se detallarán las funcionalidades implementadas en cada módulo del sistema, junto con los requisitos funcionales y no funcionales, diagramas de diseño, y casos de uso.
Estructura del Documento
Composición del Proyecto: Descripción detallada de cada archivo del proyecto, explicando su propósito y funcionalidades implementadas.
Funcionalidades: Explicación de las características implementadas en el proyecto.
Casos de Uso: Escenarios de interacción entre el sistema y los usuarios.
Requisitos del Sistema: Requisitos funcionales y no funcionales.
Diagramas: Diagramas de Clases, y de Secuencia.


1 - Composición del proyecto:
1.1 - Modelo de Producto (models.py)
Descripción General
Este archivo contiene la definición del modelo Producto, que representa los productos gestionados por el sistema. Es parte de la capa de modelos de Django, encargada de definir la estructura y comportamiento de las entidades que se almacenan en la base de datos.
Detalles de la Funcionalidad
La clase Producto representa un producto con atributos específicos relacionados con sus características y disponibilidad. Se compone por los Atributos nombre (CharField que contiene el Nombre del producto), categoría (CharField que contiene la Categoría a la que pertenece el producto, precio (IntegerField que contiene el Precio del producto) y stock (IntegerField que contiene la Cantidad de unidades disponibles en inventario.
Incluye el Método __str__ el cual Representa el objeto como una cadena y muestra el nombre del producto junto con su precio. También gestiona la información clave de los productos, lo que es esencial para cualquier funcionalidad que implique mostrar, vender o actualizar productos en la aplicación.

1.2 - Controlador de Vistas (views.py)
Descripción General
Este archivo define las vistas que controlan la interacción del usuario con el sistema. Estas funciones manejan la lógica de negocio para mostrar productos, gestionar el carrito de compras, y procesar el flujo de pago. Cada vista está asociada a una URL específica y utiliza las plantillas correspondientes para generar las respuestas.
Detalles de la Funcionalidad
En este apartado, se describen las vistas definidas en el archivo, explicando su propósito, flujo de trabajo y cómo interactúan con otros componentes del sistema. Entre ellas se encuentran: 
Vista tienda: Cuyo propósito es mostrar todos los productos disponibles en la tienda, para ello Consulta todos los productos almacenados en la base de datos y Renderiza la plantilla tienda.html con los datos de los productos.
Vista agregar producto: Cuyo propósito es agregar un producto al carrito de compras. Para ello obtiene el producto por su id, si el mismo tiene unidades disponibles, lo agrega al carrito y reduce su stock en 1 y guarda los cambios.
Vista eliminar producto: Cuyo propósito es eliminar un producto del carrito de compras. Para ello, de igual manera que la vista anterior, obtiene el producto y lo elimina del carrito, incrementa el stock del producto eliminado y guarda los cambios.
Vista restar producto: Cuyo propósito es Restar una unidad de un producto en el carrito. Resta el producto del carrito utilizando la lógica implementada en la clase Carrito (la cual veremos en breve), incrementa el stock del producto en la base de datos y guarda los cambios.
Vista limpiar carrito: Cuyo propósito es vaciar completamente el carrito de compras. Para cada producto en el carrito, incrementa su stock según la cantidad que tenía en el carrito (digamos, los devuelve) y vacía el carrito.
Vista pantalla pago: Cuyo propósito es mostrar la pantalla de pago con el resumen del carrito. Para ello calcula el total del carrito sumando los valores acumulados de los productos y renderiza la plantilla pago.html con los datos del carrito y el total a pagar.
Vista confirmar pago: Cuyo propósito es procesar la simulación de confirmación del pago. Verifica que el método de pago haya sido enviado a través de un formulario POST. Limpia el carrito y redirige a la página de agradecimiento.
Vista gracias: Cuyo propósito es mostrar una página de agradecimiento tras completar la compra. Renderiza la plantilla gracias.html.
Relación con Otros Componentes
En esta sección se detalla cómo las vistas interactúan con otros módulos del sistema para cumplir con los objetivos del proyecto.
Se relaciona utilizando el modelo Producto para gestionar los datos almacenados. Interactúa con la clase personalizada Carrito para manejar la lógica del carrito de compras. Renderiza las plantillas tienda.html, pago.html y gracias.html para la interfaz de usuario.

1.3 - Configuración de URLs (urls.py)
Descripción General
Este archivo gestiona la configuración de las rutas (URLs) de la aplicación. En Django, las URLs determinan cómo las solicitudes HTTP se mapean a funciones específicas de vista. Este archivo conecta las vistas del proyecto con las rutas que los usuarios pueden visitar en su navegador.
Detalles de la Funcionalidad
A continuación, se describen las URL configuradas en el archivo, explicando el propósito de cada ruta y cómo se vinculan con las vistas correspondientes. 
Ruta '' (Raíz): Asociada a la vista Tienda, muestra la tienda principal donde los productos disponibles son listados.
Ruta 'agregar/<int:producto_id>/': Asociada a la vista agregar_producto, permite agregar un producto al carrito de compras, identificando el producto por su ID.
Ruta 'eliminar/<int:producto_id>/': Asociada a la vista eliminar_producto, elimina un producto del carrito de compras, identificando el producto por su ID.
Ruta 'restar/<int:producto_id>/': Asociada a la vista restar_producto, permite restar una unidad de un producto en el carrito, identificando el producto por su ID.
Ruta 'limpiar/': Asociada a la vista limpiar_carrito, limpia todo el carrito de compras, vaciando los productos agregados.
Ruta 'pago/': Asociada a la vista pantalla_pago,muestra la pantalla de pago, mostrando un resumen de los productos en el carrito y el total a pagar.
Ruta 'confirmar_pago/': Asociada a la vista confirmar_pago, procesa la confirmación del pago y limpia el carrito de compras después de completar la transacción.
Ruta 'gracias/': Asociada a la vista Gracias, muestra una página de agradecimiento tras completar la compra.
Relación con Otros Componentes
En esta sección se detalla cómo las rutas y vistas se relacionan con otros componentes del sistema:
Cada URL está vinculada a una vista específica que maneja la lógica de negocio y genera la respuesta adecuada. Las rutas se configuran utilizando la función path(), donde se especifica la URL, la vista asociada y un nombre para la ruta que facilita su referencia.

1.4 - Templates
1.4.1 - Tienda (tienda.html)
Descripción General
Esta plantilla es la que renderiza la página principal de la tienda. Muestra una lista de productos disponibles, incluyendo detalles como el nombre, categoría, precio y stock. Además, permite a los usuarios agregar productos al carrito si hay stock disponible.
Detalles de la Funcionalidad
Productos: Se recorren todos los productos disponibles (productos) y se muestran en tarjetas dentro de un layout de rejilla utilizando Bootstrap.
Stock: Si el producto tiene stock, se ofrece la opción de agregarlo al carrito mediante un enlace. Si no hay stock, el botón de agregar se desactiva.
Carrito: Se incluye el archivo carrito.html, que es responsable de mostrar el estado del carrito (productos agregados, cantidad y total).
Interactividad: Al hacer clic en los enlaces, se redirige al usuario a la vista agregar_producto, que agrega el producto al carrito.
1.4.2 - Carrito (carrito.html)
Descripción General
Esta plantilla muestra el estado actual del carrito de compras. Incluye una tabla con los productos agregados, su precio, cantidad, y la opción de aumentar o disminuir la cantidad de cada producto. También muestra el total del carrito.
Detalles de la Funcionalidad
Productos en el Carrito: Se recorren los productos del carrito usando la sesión de Django (request.session.carrito), mostrando su nombre, precio y cantidad.
Acciones: Los usuarios pueden incrementar o reducir la cantidad de cada producto usando los enlaces de los botones correspondientes.
Total: Se calcula el total del carrito sumando los precios de los productos multiplicados por su cantidad.
Acciones Disponibles: Los botones permiten limpiar el carrito o proceder al pago si el carrito contiene productos.
1.4.3 - Pago (pago.html)
Descripción General
Esta plantilla es responsable de mostrar la página de resumen del carrito, permitiendo al usuario revisar los productos en el carrito antes de proceder al pago. También incluye un formulario para que el usuario seleccione su método de pago.
Detalles de la Funcionalidad
Resumen del Carrito: Se muestra una tabla con los productos del carrito, sus precios y cantidades, junto con el total.
Método de Pago: El usuario puede elegir entre dos métodos de pago disponibles: Tarjeta de Crédito/Débito o MercadoPago, usando un select en el formulario.
Confirmación del Pago: Al enviar el formulario, se procesa el pago y se redirige al usuario a la página de confirmación del pago.
Acciones Disponibles: El formulario de pago solo está habilitado si el carrito contiene productos, y al confirmar el pago, se limpia el carrito.
1.4.4 - Gracias (gracias.html)
Descripción General
Esta plantilla se muestra al usuario después de completar el pago exitosamente. Agradece al usuario por su compra y le ofrece la opción de volver a la tienda.
Detalles de la Funcionalidad
Mensaje de Agradecimiento: Se muestra un mensaje de éxito indicando que el pago fue procesado correctamente y agradeciendo al usuario por su compra.
Volver a la Tienda: Se ofrece un botón para que el usuario pueda regresar a la página principal de la tienda, fomentando la interacción continua con el sitio.

1.5 - Procesadores de Contexto
1.5.1 - Total Carrito (context_processor.py)
Descripción General
Este archivo contiene un procesador de contexto que calcula el total acumulado de los productos en el carrito de compras.
Detalles de la Funcionalidad
Función total_carrito: Recorre los productos en el carrito y acumula el total de los productos basándose en su cantidad. Este valor es luego accesible en las plantillas bajo la variable total_carrito.

1.6 - Archivos de Administración
1.6.1 - Configuración de la Administración (apps.py y admin.py)
Descripción General
Estos archivos registran el modelo Producto para que sea administrable desde el panel de administración de Django.
Detalles de la Funcionalidad
apps.py: Registra el modelo Producto en el panel de administración para poder gestionarlo desde la interfaz administrativa de Django.
admin.py: Incluye el modelo Producto en el admin, lo que permite crear, editar y eliminar productos directamente desde el backend de Django.

1.7 - Configuración de Proyecto
1.7.1 - Ajustes del Proyecto (settings.py)
Descripción General
Este archivo contiene la configuración global de Django para el proyecto. Aquí se definen aspectos clave como la base de datos, aplicaciones instaladas, configuración de la plantilla, y el manejo de archivos estáticos.
Detalles de la Funcionalidad
Aplicaciones Instaladas: Se incluyen aplicaciones estándar de Django como django.contrib.admin, django.contrib.sessions, y la aplicación carrito.
Archivos Estáticos: Se configuran los archivos estáticos y se define el directorio donde se almacenan.
Context Processors: Se añade el procesador de contexto para total_carrito, permitiendo el cálculo del total en la vista de la tienda.


2. Funcionalidades del Sistema
2.1 - Gestión de Productos
La gestión de productos en la tienda es una de las funcionalidades más fundamentales del sistema. Permite a los usuarios ver productos disponibles, agregar productos al carrito, eliminar productos y ajustar la cantidad de productos en el carrito.
2.1.1 - Mostrar Productos (Vista: tienda)
Descripción: Esta funcionalidad permite a los usuarios ver todos los productos disponibles en la tienda, con su nombre, categoría, precio y stock.
Implementación: El archivo views.py define la vista tienda, que obtiene todos los productos desde la base de datos a través del modelo Producto. Los productos se muestran en una plantilla HTML (utilizando Bootstrap para el diseño), con un botón de "Agregar al carrito" visible si el producto tiene stock disponible.
2.1.2 - Agregar al Carrito (Vista: agregar_producto)
Descripción: Los usuarios pueden agregar productos al carrito de compras. Si un producto tiene stock disponible, se añade al carrito y se actualiza el inventario en la base de datos.
Implementación: En la vista agregar_producto, el carrito se gestiona a través de la clase Carrito, que está definida en un archivo separado. Cuando un usuario hace clic en "Agregar al carrito", el producto se añade a la sesión del carrito, y el stock se decrementa en la base de datos.
2.1.3 - Eliminar Producto del Carrito (Vista: eliminar_producto)
Descripción: Permite eliminar un producto del carrito. Al eliminarse un producto, el stock disponible en la tienda se incrementa de nuevo.
Implementación: En la vista eliminar_producto, se elimina un producto del carrito de la sesión y se actualiza el stock del producto en la base de datos.
2.1.4 - Restar Cantidad del Producto en el Carrito (Vista: restar_producto)
Descripción: Los usuarios pueden reducir la cantidad de un producto en su carrito. Si la cantidad es mayor que 1, la cantidad en el carrito disminuye y el stock aumenta.
Implementación: En la vista restar_producto, el carrito es modificado para reducir la cantidad del producto. A su vez, el stock del producto en la base de datos se actualiza.
2.1.5 - Limpiar el Carrito (Vista: limpiar_carrito)
Descripción: El usuario puede vaciar completamente el carrito. Cuando esto sucede, el sistema devuelve los productos a su estado original (incrementando el stock).
Implementación: En la vista limpiar_carrito, todos los productos en el carrito se eliminan y el stock de cada uno se restaura.
2.2 - Proceso de Pago
El proceso de pago permite a los usuarios revisar su carrito, elegir un método de pago y confirmar la compra.
2.2.1 - Ver Resumen del Carrito (Vista: pantalla_pago)
Descripción: Los usuarios pueden ver un resumen de su carrito antes de proceder al pago, incluyendo el nombre, precio y cantidad de los productos, así como el total de la compra.
Implementación: La vista pantalla_pago calcula el total del carrito y lo pasa a la plantilla pago.html. Además, muestra un formulario para que el usuario seleccione el método de pago.
2.2.2 - Confirmar Pago (Vista: confirmar_pago)
Descripción: Permite a los usuarios confirmar su compra y limpiar el carrito una vez el pago es procesado.
Implementación: En la vista confirmar_pago, el sistema procesa el pago, limpia el carrito y redirige al usuario a una página de agradecimiento.
2.2.3 - Página de Agradecimiento (Vista: gracias)
Descripción: Después de realizar el pago, el usuario es redirigido a una página de agradecimiento por la compra exitosa.
Implementación: La vista gracias renderiza una plantilla simple con un mensaje de agradecimiento al usuario.
2.3 - Funcionalidades Adicionales
2.3.1 - Módulo de Carrito
Descripción: El carrito se mantiene como una sesión en el servidor, y se utiliza para almacenar productos agregados por el usuario.
Implementación: El Carrito es una clase personalizada (ubicada en carrito/Carrito.py) que maneja los productos en el carrito, como agregar, restar y eliminar productos. Los productos en el carrito se almacenan como diccionario en la sesión de Django, lo que permite que los datos persistan entre las peticiones HTTP.
2.3.2 - Calcular Total del Carrito
Descripción: El sistema calcula automáticamente el total de la compra a medida que los productos se agregan, eliminan o modifican en el carrito.
Implementación: La función total_carrito en context_processor.py calcula el total acumulado de los productos en el carrito y lo hace disponible en las plantillas para su visualización.

3. Casos de Uso
3.1 - Caso de Uso 1: Ver Productos en la Tienda
Descripción: El usuario ingresa a la tienda y puede ver una lista de productos disponibles, con detalles como nombre, precio, categoría, y stock disponible. También puede ver la opción de agregar productos al carrito si están disponibles en stock.

Diagrama: //www.plantuml.com/plantuml/png/PP0zJyGm38Rt_8fNjnyIzx6WKtM8YO69ZzrAVIKYJP3jJ8Z_JbCY4M3pu_UntUQiHc9bZYxonM0P4gPNmnY4lOMS77dBWcSj9263T2bPMlSngF5CjLjBLsSeJP6nUM71k-InBAA24oBXAN0QQOCF1nHbJxg8zsaILX9GhzGxTzUTztjX4tQzS3i9J_GZWI8yYGJBJT_t-aDM4_g_y_3dQBW4lsXgsRyrvUWSrcV0TZkqxwp_t_3GOxLHdKQxbNQDzeskrZdSu7GAoSSoyZ2iqVuxElQHBjcdEtCQono_0000
Actores: Usuario (cliente) - Sistema
Precondiciones:
El usuario tiene acceso a la tienda a través del navegador.
El sistema tiene productos registrados y disponibles en la base de datos.
Flujo principal:
El usuario accede a la página principal de la tienda.
El sistema muestra una lista de productos disponibles.
Para cada producto, el sistema muestra el nombre, precio, categoría y stock disponible.
Si el producto tiene stock, el sistema ofrece un botón "Agregar al carrito".
El usuario puede ver la opción de agregar productos al carrito si tienen stock disponible.
Flujo alternativo:
Si un producto no tiene stock disponible, el botón "Agregar al carrito" se desactiva, mostrando un mensaje de "Sin stock".
Postcondiciones:
El usuario visualiza correctamente los productos disponibles en la tienda.
Si un producto tiene stock, el usuario puede agregarlo al carrito.
3.2 - Caso de Uso 2: Agregar Producto al Carrito
Descripción: El usuario agrega un producto al carrito de compras. Si el producto tiene stock disponible, se añade al carrito y se actualiza el inventario de la tienda.
Diagrama: //www.plantuml.com/plantuml/png/NO_1JiCm38RlUGghzo6nxeIcQcYymGHto_MAHPeWnpaXtfsapI7ivj__btpo9HcgvTKxptS3Yw2oV1hCeamcCJWaYmhlAQDA14nbP6tRcoJZ5UksZgw-mR1uXk5rKLvGuLlZd0iCwE6Agc9nW1y7a1CJfaBUs3DHKNNqi8ckppttmIfteK8bY_JLa6EFD6brKNFjrDXJRv9M2Ld-VtHo3hRRu72OchiUrUAnZvM6ohGqjlIqaV02vxC4yddcQTggSQzE3zMlkt2Oy-h_0000
Actores: Usuario (cliente) - Sistema
Precondiciones:
El usuario está autenticado o no requiere autenticación (depende de la configuración).
El producto a agregar tiene stock disponible.
El carrito de compras está vacío o contiene productos.
Flujo principal:
El usuario selecciona un producto para agregar al carrito.
El sistema verifica que el producto tiene stock disponible.
El sistema agrega el producto al carrito y actualiza la sesión del usuario.
El carrito se actualiza, mostrando el nuevo producto agregado.
El sistema disminuye el stock del producto en la base de datos.
Flujo alternativo:
Si el producto no tiene stock disponible, el sistema muestra un mensaje indicando que no se puede agregar el producto al carrito.
Postcondiciones:
El producto se agrega al carrito de compras.
El stock del producto en la tienda se reduce.
El carrito se actualiza para reflejar el nuevo producto.
3.3 - Caso de Uso 3: Ver Resumen del Carrito y Realizar Pago
Descripción: El usuario puede revisar los productos que ha agregado al carrito, ver el total de la compra y proceder con el pago seleccionando un método de pago.
Diagrama: //www.plantuml.com/plantuml/png/PO_1QiCm38RlVWhHUmTDiyieeT0NA2lRNTXgPf2jOCk7RUpTPsU6PUocNzzdoJfdnQGbi66wAwX0ylERWlE9h7g91grAWfTSC7a1pBMarBitdvK2jcuhJNk3SMQ2tJM9fIpW2Auuomu-3K39P35N-ap8_WDJPstgvR0LNYjtbR_3iWwg9J4il_QmjM_4PAsNMBL0AgxjtTh7hNsHUFSfLDTAM19sP_pZ8Dl2LL5Hv6uy6WFh-R3VJ_t7xUuUXsriDhJDFOrhElHqX1uVLXEUu7JoqN9nD4qh6d_Gy0-PBtEcw4hWRm00
Actores: Usuario (cliente) - Sistema
Precondiciones:
El usuario ha agregado al menos un producto al carrito.
El sistema ha calculado correctamente el total del carrito.
Flujo principal:
El usuario accede al carrito de compras.
El sistema muestra el resumen del carrito, incluyendo los productos, sus cantidades y precios.
El sistema calcula el total de la compra.
El usuario selecciona un método de pago (por ejemplo, tarjeta de crédito o MercadoPago).
El usuario confirma la compra y realiza el pago.
Flujo alternativo:
Si el carrito está vacío, el sistema muestra un mensaje indicando que no hay productos en el carrito y desactiva la opción de proceder al pago.
Si no hay un método de pago seleccionado, el sistema solicita al usuario que elija uno.
Postcondiciones:
El pago es procesado correctamente.
El carrito se limpia y los productos en él se eliminan.
El usuario es redirigido a la página de agradecimiento.
3.4 - Caso de Uso 4: Limpiar el Carrito
Descripción: El usuario puede eliminar todos los productos del carrito. El sistema vacía el carrito y restablece el stock de los productos.
Diagrama: //www.plantuml.com/plantuml/png/RP31IWGn38RlUOgmznNSkSaoZ7Zr9deFcJW6EwsawKNntKsbbq4BXO_qwz-VBjN9lEq9ahmwUa7JxSrnLHDsBHc0s8lXSsraMf1geDYOFcbrsIcc7G7w9SfR4ZmzwlwXPCXafbvE-0KOgrLXgl-Tz-I7swDqpzuewIV5KrxuVLYNe_L2_3Tf0lW6w5tnV9v_ewFYu0l4nfkE4zxXzQgPKrjbdY748KsmI5xZRtu0
Actores: Usuario (cliente) - Sistema
Precondiciones:
El usuario tiene productos en su carrito.
El carrito está activo y contiene productos.
Flujo principal:
El usuario selecciona la opción "Limpiar carrito".
El sistema elimina todos los productos del carrito.
El sistema actualiza el stock de los productos eliminados en la base de datos.
El carrito se vacía y el total se restablece a cero.
Flujo alternativo:
Si el carrito está vacío, el sistema muestra un mensaje indicando que no hay productos para eliminar.
Postcondiciones:
El carrito queda vacío.
El stock de los productos eliminados se actualiza.

4 - Requerimientos del sistema
4.1 - Requerimientos funcionales
Gestión de Productos:
El sistema debe permitir mostrar la lista de productos disponibles en la tienda.
Cada producto debe incluir su nombre, precio, categoría y stock disponible.
Carrito de Compras:
El sistema debe permitir agregar productos al carrito siempre que haya stock disponible.
El usuario debe poder visualizar un resumen detallado de los productos en el carrito.
El sistema debe permitir eliminar o restar la cantidad de un producto del carrito.
El usuario debe poder limpiar el carrito completo, restaurando el stock correspondiente.
Pago y Confirmación:
El sistema debe permitir que el usuario seleccione un método de pago al realizar el checkout.
El sistema debe procesar el pago y limpiar el carrito al finalizar la compra.
Debe mostrarse una página de agradecimiento al usuario tras confirmar el pago exitosamente.
Interacción con el Usuario:
El sistema debe actualizar dinámicamente el stock al agregar o eliminar productos.
El botón de agregar producto debe deshabilitarse automáticamente si no hay stock disponible.
4.2 - Requerimientos No Funcionales
Rendimiento:
El sistema debe cargar la página principal con la lista de productos en menos de 2 segundos.
La respuesta de cualquier acción del carrito (agregar, eliminar, limpiar) debe completarse en menos de 1 segundo.
Escalabilidad:
El sistema debe soportar un catálogo de hasta 1,000 productos sin degradación del rendimiento.
Interfaz de Usuario:
La interfaz debe ser intuitiva y responsiva, adaptándose correctamente a dispositivos móviles y de escritorio.
El diseño debe respetar un esquema visual limpio y profesional.
Seguridad:
El sistema debe proteger los datos de las transacciones mediante HTTPS.
Se debe implementar un sistema de protección contra CSRF en las acciones que modifiquen el carrito o procesen pagos.
Mantenibilidad:
El código del sistema debe estar documentado siguiendo estándares claros para facilitar futuras modificaciones.
La arquitectura debe respetar el modelo MVC de Django para mantener la separación de responsabilidades.
Compatibilidad:
El sistema debe ser compatible con navegadores modernos, incluyendo Chrome, Firefox, Edge y Safari.
El backend debe ejecutarse en entornos que soporten Python 3.9 o superior y Django 5.x.

5 - Diagrama de clases
El Diagrama de Clases representa la estructura estática del sistema, identificando las entidades principales y sus interacciones. Este modelo está diseñado para un sistema de carrito de compras en línea, donde los usuarios pueden navegar por productos, añadirlos al carrito, realizar pagos y finalizar sus compras.

Diagrama: //www.plantuml.com/plantuml/png/VLJ1ZjGm3BtdAwovx2we1wuve9LsXU2sMYIkbJVrHXPf4XoFX41y5P_0Zv7EPDhfbA4tFp-_FhzQlI-Aelin66KD18-CNd1460WU0XOgqC43Yh2c0vR6B5YCkO57UkN8Zl_yZbF77TbPE3hE6AYO2Ihm96dOkph-qq1zEk31mgUev4aQ4jFu8cJXizPftq27bPA4yGBFGewJXGyXeJQiQ79VrwfleU-BIj_Vtiq2lqppr3QQBGbzsrDH2nzLy_Enc6qSgBP6uxGfenVoABTthQR08ySpGEhyMLdRcSzgPOhKvnPCgVZYB4Mbxrf3SrHAacgnpIJ5q3StvnDVk2W-dM9V-4nnm0rntdozocncizEcqvRRuctBwnxHB-_D61L3m3wZNoHSYgyi8yeQzeAEiULq0yyKy7Xt55LEfsVcGzkzsy6RheDTtCrVsaxQXzpD2KgLiedRmbuvy0yq5xbstVlbb2sWSpGG_9Es2jh2G87yDMABPMQPrV14MeHI9a4ewKLeIxlk3Vt_XCmznM7w0Vm5

5 - Diagrama de secuencia
El Diagrama de Secuencia ilustra cómo los diferentes componentes del sistema interactúan en el tiempo para cumplir con las funcionalidades clave. Este tipo de diagrama se centra en mostrar el flujo de mensajes y las interacciones entre actores externos y las partes internas del sistema. En el contexto de nuestro carrito de compras, este diagrama describe las secuencias de acciones, como:
Agregar un producto al carrito: El usuario selecciona un producto y el sistema actualiza el carrito.
Diagrama: //www.plantuml.com/plantuml/png/LP2nJiD0343t-meh4mpz0GRKwbWO8Y9ekfkBYIpIS-Gu2x_59_1ZEEsbKPSeklVyB7a_6QhDvo5WCb5efncL1N22DeoEEF68sQ0wiQjmPCeTLWi_7U-5YAfiSc7n7jNIqI3Gg7HpAahTXD32xjaxy0GVD51AB1aLgaElrFiF3f1ADBZbRjsu-_Pfb4bXB3bu64NXzUKnEDwjnNLPcOp-LBhRuBOWn5l-dHoomcIIljVaCXubVx6UCV7VRmvnMtL8DkF0FrS27MrPvulMNhkit7iPmIvd37l_BhV_1m00
Realizar el pago: El usuario revisa los productos en el carrito, selecciona un método de pago, y el sistema procesa la transacción.
Diagrama: //www.plantuml.com/plantuml/png/NP0nRiCm34LtdOB8xWjqA88eOujwSNPMOWCMbcXGzD1pzGYzM1aB7kBDuFju3zQv6QgjPGwOJ1IcjgAo03QOmkA84ozO3KutzYcCU9VJWzx6PnnHbQsp-8mks0WomHLDsZQuN4EOO7Xr2xn0bFh5Mb1XSNlmcvFeuEFJg992akeVdCKjCwHU2X66tJ2gv3Mv7Nx0n73k4kzqcAZjTZyDnt3Ylz_gxcF_ZSl2g7jn8uucH-_IJ1qLgWs_jz_3ksAcn8Mf-lXCDJ_UzHy0
Vaciar el carrito: El usuario decide limpiar el carrito, y el sistema restaura los niveles de stock.
Diagrama: //www.plantuml.com/plantuml/png/RT2nJWCn383XtKzXTOAXBy20AjrSKO6kk_45oU8QHux3m3inyGXzCHm8WYAcayvV_bZPLIVpTbg1sDLmherC5AdY32L6mb8eEswE4XGdCXFNJGV7wLBydlqPxNL9g-B1T6ayoFu0CEFsDZfuWmzfJSoYcIpk8fRuyWX2Y72TtJrwoicmZ5B527z3w2owuUvJTMeMaUhAptXLzEVGDOJPZkAa-KdiH2pdznmr9FP6gxn-_UdDiUBbLfzBnMZ-hp4ClX2VtnHsAI_zZJy0
Mostrar la tienda: El sistema obtiene los productos y los presenta al usuario.
Diagrama: //www.plantuml.com/plantuml/png/LSyn2yCW40NWtL_no9u_qA6aTAsG8MO_r89WDPpdqb_VIsWXdR_ttkdKX5ZwAnloKXckTU9KGGtER4h9fusAO5YJHh6aM08Dkw_BVy3M47F5p3LqtJeoTZR6ORng61VSl8yXCWYP8CUIKL2si_AzbjQp46FxRZIZCFxgZ-C58PvuRoixLLkRyBcBMFOxgKZa9xtDfFVqeny0
Este modelo proporciona una visión clara y detallada del comportamiento dinámico del sistema, ayudando a identificar dependencias y optimizar el flujo de trabajo.





