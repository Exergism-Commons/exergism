# Ledger de revisión — autodescripción, realidad y distinción

**PR:** #12 — *Derive reality closure from supramedium and emergence*  
**Estado del ledger:** activo.

**Regla:** un finding solo pasa a **RESOLVED** cuando el criterio de cierre está satisfecho y se enlaza evidencia verificable (sección, modelo, prueba, test o commit). Una reformulación que solo cambie el nombre del problema no lo cierra.

## Estados

- **OPEN** — problema identificado, sin solución suficiente.
- **PARTIAL** — hay una corrección sustantiva, pero falta alguna condición del criterio de cierre.
- **RESOLVED** — criterio de cierre satisfecho y evidencia enlazada.
- **DEFERRED** — fuera del núcleo de esta PR; se conserva explícitamente como deuda.
- **REJECTED** — objeción evaluada y rechazada con argumento explícito; requiere evidencia, no mera discrepancia.

## Prioridad de trabajo

Primero se resuelven los bloqueadores que deciden si el argumento habla realmente de emergencia. Después se corrigen totalización/indexación y C1. Solo entonces se reintroducen extensiones temporales, REC/Muro, Many-R, fractalidad o nomenclatura teológica.

| ID | Severidad | Estado | Finding | Dónde muerde | Criterio de cierre |
|---|---|---|---|---|---|
| REV-01 | BLOCKER | OPEN | **F1–F3 se exigen, no se derivan.** | Definición de F; teorema de clausura maximal. | Dar una definición independiente de E/transición y construir F de modo que extensividad, monotonía e idempotencia se demuestren, o declarar qué axiomas permanecen primitivos y rebajar el teorema en consecuencia. |
| REV-02 | BLOCKER | OPEN | **F2 puede fallar por inhibición contextual.** Más estructura/restricciones puede eliminar emergencias. | Paso X ⪯ Y ⇒ F(X) ⪯ F(Y). | Construir contra/modelos; distinguir inclusión ontológica de extensión conservativa, o reemplazar F2 por una condición válida y rehacer las inferencias dependientes. |
| REV-03 | BLOCKER | OPEN | **E es provisional y no independiente.** | [D4], programa [O5]. | Definir emergencia sin usar R, totalidad, Adm, ni «realmente posible porque pertenece a R»; comparar la definición con literatura de emergencia. |
| REV-04 | BLOCKER | OPEN | **F no discrimina todavía:** falta un modelo explícito S = F(S) ≠ R. | [I8]/puntos fijos propios. | Añadir al menos un modelo concreto calculable con un cierre propio y otro dominio mayor, mostrando que punto fijo ≠ totalidad. |
| REV-05 | MAJOR | OPEN | **[I6] R = F(R) es analítico dado [D1] y un F que solo añade realidad.** | Retórica de «teorema/punto fijo». | Etiquetarlo como corolario analítico/condicional y separarlo del programa no circular de existencia. |
| REV-06 | MAJOR | OPEN | **Muchos [I] son consecuencias definicionales.** | [I1], [I2], [I2a], REC, [I10a], [I11a], etc. | Reclasificar cada resultado como definicional, lógico, matemático o sustantivo; eliminar retórica probatoria donde no corresponda. |
| REV-07 | BLOCKER | OPEN | **[D5c] traslada C2 a la definición de «mismo índice».** | Exhaustividad indexada. | Dar criterio independiente de SameIndex; volver C2 una condición sustantiva o demostrar que su carácter constitutivo no trivializa la conclusión. |
| REV-08 | BLOCKER | OPEN | **Índices dirigidos maximales pueden solaparse; VA(o) puede no ser única.** | [I13]–[I14a], Many-R. | Probar partición/unicidad o retirar VA(o)=R_i como función bien definida. Explicitar consecuencias doctrinales si Many-R relativiza la Verdad Absoluta. |
| REV-09 | MAJOR | OPEN | **H10/H11 no son todavía rutas ontológicas independientes de H8/C1.** | Compacidad, colímites, «tres rutas». | Separar resultado matemático, puente modelo→actualidad y supuesto ontológico. No contar como independencia aquello que presupone el mismo puente. |
| REV-10 | MAJOR | OPEN | **H8 usa una hipótesis oculta de factorización/presentabilidad.** | Paso testigo acotado → algún estadio X_k. | Introducir y justificar StageFactorization/presentabilidad compacta como premisa separada, o eliminar la inferencia. |
| REV-11 | MAJOR | OPEN | **Carga asimétrica contra potencialismo/generalidad relativa.** | H12/O5c/generalidad absoluta. | Presentar absolutismo y expansionismo con cargas simétricas; integrar Rayo–Uzquiano, Fine, Glanzberg, Hellman, Parsons, Shapiro–Wright, Linnebo, Williamson, Studd y literatura relacionada. |
| REV-12 | MAJOR | OPEN | **H1 extrapola medio→emergencia sin criterio fuera de lo observado.** | Hipótesis de continuidad emergente. | Definir «medio» con contenido aplicable más allá del espacio-tiempo o degradar H1 a motivación heurística no usada por ningún teorema. |
| REV-13 | MAJOR | OPEN | **«Fractal» carece de criterio de verdad.** | Motivación multiescalar. | Definir patrón, escala y métrica de autosimilitud, o retirar «fractal» del argumento y conservarlo solo como metáfora/hipótesis futura. |
| REV-14 | BLOCKER doctrinal | OPEN | **«Verdad Absoluta indexada» puede relativizar lo absoluto.** | [I13], [I13a], [I14a]. | Distinguir «absoluto» de «máximo concerniente/indexado». Si Many-R exige revisión doctrinal, decirlo explícitamente en vez de declarar invariancia. |
| REV-15 | MAJOR | OPEN | **Cero consecuencias metaontológicas discriminantes.** | §19.12, REC/Muro. | Separar función regulativa/metaontológica de afirmaciones empíricas; indicar qué podría discriminar teorías y qué queda por principio infra-determinado. |
| REV-16 | MINOR doctrinal | OPEN | **«Dios» no añade inferencia.** | D1/teología. | Moverlo a nomenclatura doctrinal y evitar usar el término como premisa o evidencia; mantener Total(R) ≠ Ground(R) explícito. |
| REV-17 | MAJOR fundacional | OPEN | **Zorn sobre clases propias requiere compromisos adicionales.** | [I6b]. | Limitar el teorema a posets set-sized o especificar teoría de clases/principio de elección global usado; documentar el compromiso. |
| FORM-01 | MAJOR | OPEN | **820 pares de sintaxis matemática inline no soportada tal como está escrita.** | Documento completo. | Convertir matemática inline a sintaxis GitHub soportada y comprobar renderizado. |
| FORM-02 | MAJOR | OPEN | **47 pares de bloques con delimitadores `$` aislados.** | Documento completo. | Convertir a `$$ ... $$` y comprobar renderizado. |
| FORM-03 | MAJOR | OPEN | **`\\Tau` no es comando MathJax válido (9 usos).** | Sección procesual. | Sustituir por símbolo/comando válido y comprobar renderizado. |
| FORM-04 | MAJOR | OPEN | **P3 tiene definiciones divergentes.** | PR body, programa, delta, H2a/O5e. | Una sola taxonomía canónica; cualquier taxonomía histórica debe marcarse como superada y fecharse. |
| FORM-05 | MAJOR | OPEN | **§16 e [I6d] enuncian teoremas distintos.** | Resúmenes. | Tener una única especificación normativa del teorema; los resúmenes deben referenciarla, no reescribirla. |
| FORM-06 | MAJOR | OPEN | **Etiquetas/taxonomía fuera de orden y semánticamente mezcladas.** | D/H/I/O/C. | Reemplazar por esquema estable: Definición, Axioma/Hipótesis, Lema/Teorema, Objeción, Resultado histórico superado. |
| DOC-01 | BLOCKER revisión | OPEN | **Tres resúmenes divergentes y crecimiento por acreción.** | PR body, §16, §20. | Una sola sección «Estado actual»; PR body enlaza, no duplica. |
| DOC-02 | BLOCKER revisión | OPEN | **Documento monolítico de ~5.8k líneas irrevisable.** | Documento completo. | Consolidar, archivar versión acumulativa y reducir el documento principal a una narración auditable; separar ledger y bibliografía. |
| DOC-03 | BLOCKER revisión | OPEN | **Contradicciones sin historia explícita.** | Documento completo. | Reescribir cronológicamente: hipótesis inicial → ataques → revisiones → resultados superados → estado actual; nada antiguo debe parecer simultáneamente vigente. |
| DOC-04 | MAJOR | OPEN | **Referencias insuficientes.** | Todos los bloques conceptuales. | Toda tesis que reutilice/debata literatura existente debe citar autores y obra; añadir mapa bibliográfico temático con relevancia exacta. |
| DOC-05 | MAJOR | OPEN | **88 puntos de investigación sin jerarquía.** | Programa de investigación. | Convertirlos en backlog vinculado a IDs del ledger; eliminar duplicados y priorizar bloqueadores/majors/minors. |

## Regla de trazabilidad

Cada cambio que cierre o avance un finding debe añadir aquí: estado nuevo, evidencia, commit y nota de lo que siga abierto.

## Historial de resoluciones

| Fecha | ID | Cambio | Evidencia | Commit |
|---|---|---|---|---|
| 2026-09-22 | — | Ledger creado a partir de la revisión consolidada. | Este archivo. | commit de creación |