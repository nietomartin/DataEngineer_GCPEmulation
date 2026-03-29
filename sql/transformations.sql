SELECT
  ciudad,
  categoria,
  SUM(total) AS total_ventas
FROM ventas
WHERE estado = 'completado'
GROUP BY ciudad, categoria;
