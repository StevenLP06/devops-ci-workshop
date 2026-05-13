**Integrantes:**
- Juan Sebastian Zapata
- Steven Lopez Parra

## Error 1
-**Archivo:** pytest.py
-**Problema:** El test test_home() esperaba data["status"] == "running", pero app.py retornaba "status": "ok"
-**Solución:** Cambiar el test para que espere "status": "ok" y agregar assert data["service"] == "devops-api"

## Error 2
-**Archivo:** pytest.py
-**Problema:** El test test_health() esperaba "uptime_seconds" en la respuesta, pero app.py retornaba "cpu_percent" y "memory_percent"
-**Solución:**  Cambiar el test para que verifique "cpu_percent" y "memory_percent" en lugar de "uptime_seconds"

## Error 3
-**Archivo:** pytest.py
-**Problema:** El test test_metrics() buscaba el endpoint /metrics, pero app.py tenía el endpoint /metric (sin la letra 's')
-**Solución:** Cambiar el nombre de la función a test_metric() y la URL a /metric

## Error 4
-**Archivo:** app.py
-**Problema:** La aplicación estaba configurada en el puerto 5001, pero algunos entornos esperan el puerto 5000 por defecto
-**Solución:** Cambiar app.run(host='0.0.0.0', port=5001) a app.run(host='0.0.0.0', port=5000)

## Error 5
-**Archivo:** requirements.txt
-**Problema:** El pipeline intenta ejecutar test en Pytest sin haberlo instalado anteriormente, lo cual produce un error.
-**Solución:** Agregar en requirements.txt pytest==9.0.1 (en este caso en específico).

ola
