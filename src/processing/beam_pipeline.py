import apache_beam as beam

def parse(line):
    return line.split(",")

with beam.Pipeline() as p:
    (
        p
        | "Leer CSV" >> beam.io.ReadFromText("data/processed/ventas_processed.csv", skip_header_lines=1)
        | "Parsear" >> beam.Map(parse)
        | "Filtrar completados" >> beam.Filter(lambda x: x[9] == "completado")
        | "Imprimir" >> beam.Map(print)
    )