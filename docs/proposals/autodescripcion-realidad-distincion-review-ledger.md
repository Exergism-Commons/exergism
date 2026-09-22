# Ledger de revisión — autodescripción, realidad y distinción

**PR:** #12 — *Derive regime-local semantic exhaustivity and isolate the Exists-R bridge*  
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
| REV-01 | BLOCKER | RESOLVED | **F1–F3 se exigían sin derivarse.** | Definición de F; teorema de clausura maximal. | Cerrado: desde la definición independiente de $\mathcal E_M$ se define $F_M$ como clausura reflexivo-transitiva de eventos emergentes; F1, F2 interna y F3 se derivan. Además F2 se elimina por redundante del teorema abstracto. El puente ontológico restante se registra aparte como REV-18. |
| REV-02 | BLOCKER | RESOLVED | **La inhibición contextual parecía refutar F2.** | Monotonía y cambio de contexto. | Cerrado por distinción de tipos: la inhibición compara operadores distintos $F_M$ y $F_N$, mientras F2 interna compara subconjuntos bajo un mismo $F_M$. Se construyó además un contraejemplo cross-system y una extensión conductualmente conservativa que preserva eventos. |
| REV-03 | BLOCKER | PARTIAL | **E es provisional y no independiente.** | [D4], programa [O5]. | Definir emergencia sin usar R, totalidad, Adm, ni «realmente posible porque pertenece a R»; comparar la definición con literatura de emergencia. |
| REV-04 | BLOCKER | RESOLVED | **F no discriminaba todavía:** faltaba un modelo explícito de punto fijo propio. | [I8]/puntos fijos propios. | Cerrado con el toy de cuatro componentes: para el operador $F_M$ inducido por el único evento emergente $p\leadsto c$, $S=\{p,c\}$ satisface $F_M(S)=S$ y $S\neq\Sigma_M$. |
| REV-05 | MAJOR | RESOLVED | **[I6] R = F(R) es analítico dado [D1] y un F que solo añade realidad.** | Retórica de «teorema/punto fijo». | Etiquetarlo como corolario analítico/condicional y separarlo del programa no circular de existencia. |
| REV-06 | MAJOR | RESOLVED | **Muchos [I] son consecuencias definicionales.** | [I1], [I2], [I2a], REC, [I10a], [I11a], etc. | Reclasificar cada resultado como definicional, lógico, matemático o sustantivo; eliminar retórica probatoria donde no corresponda. |
| REV-07 | BLOCKER | PARTIAL | **La directedness interna K3_i se deriva de StructAdm; permanece abierta la individuación filosófica del régimen mediante $\Lambda_*$.** | Criterio de pertenencia a $i$. | Para dominios del mismo régimen, la unión semántica positiva actual es admisible y proporciona cota común, por lo que K3_i queda demostrado. EEA también se deriva para footprints actuales. Falta justificar qué relaciones pertenecen a $\Lambda_*$, su invariancia representacional, que la taxonomía no colapse ni fragmente indebidamente regímenes y por qué `SameRegime` debe usar clausura por caminos finitos frente a posibles dependencias transfinitarias o de límite. |
| REV-08 | BLOCKER | RESOLVED | **Índices dirigidos maximales podían solaparse; VA(o) podía no ser única.** | [I13]–[I14a], Many-R. | Resuelto retirando la arquitectura que definía $i$ mediante maximales dirigidos y retirando definitivamente $\operatorname{VA}(o)=R_i$. La identidad de los regímenes ontológicos queda como obligación independiente de REV-07. |
| REV-09 | MAJOR | RESOLVED | **La inductividad K2 queda demostrada para cadenas set-indexed bajo admisibilidad estructural mínima.** | K2 / cotas de cadenas E-closed. | Uniones set-indexed de cadenas StructAdm siguen siendo StructAdm; el lema previo demuestra que `EClosed` también se preserva. Por tanto K2 vale en el alcance set-sized. La cuestión class-sized/aplicabilidad global queda exclusivamente en REV-22. |
| REV-10 | MAJOR | RESOLVED | **La ruta local hacia K2 usaba una hipótesis oculta de factorización/presentabilidad.** | Testigo acotado → algún estadio de una cadena. | Resuelto para el teorema vigente eliminando esa derivación: en la formulación procesual `EClosed`, el token de origen presente en la unión pertenece ya a algún estadio y el cierre de ese estadio arrastra evento y resultado. Reabrir solo si una futura noción de emergencia exige habilitación esencialmente infinitaria. |
| REV-11 | MAJOR | RESOLVED | **Carga asimétrica contra potencialismo/generalidad relativa.** | H12/O5c/generalidad absoluta. | Presentar absolutismo y expansionismo con cargas simétricas; integrar Rayo–Uzquiano, Fine, Glanzberg, Hellman, Parsons, Shapiro–Wright, Linnebo, Williamson, Studd y literatura relacionada. |
| REV-12 | MAJOR | RESOLVED | **H1 extrapola medio→emergencia sin criterio fuera de lo observado.** | Hipótesis de continuidad emergente. | Definir «medio» con contenido aplicable más allá del espacio-tiempo o degradar H1 a motivación heurística no usada por ningún teorema. |
| REV-13 | MAJOR | RESOLVED | **«Fractal» carece de criterio de verdad.** | Motivación multiescalar. | Definir patrón, escala y métrica de autosimilitud, o retirar «fractal» del argumento y conservarlo solo como metáfora/hipótesis futura. |
| REV-14 | BLOCKER doctrinal | RESOLVED | **«Verdad Absoluta indexada» relativizaba lo absoluto.** | [I13], [I13a], [I14a]. | Resuelto distinguiendo $\operatorname{Truth}_i$ —exhaustividad interna del régimen— de una hipotética $\operatorname{Truth}_{\mathrm{abs}}$, cuya existencia permanece abierta. La fórmula $\operatorname{VA}(o)=R_i$ queda SUPERSEDED y no se declara invariancia doctrinal ante Many-R. |
| REV-15 | MAJOR | OPEN | **Cero consecuencias metaontológicas discriminantes.** | §19.12, REC/Muro. | Separar función regulativa/metaontológica de afirmaciones empíricas; indicar qué podría discriminar teorías y qué queda por principio infra-determinado. |
| REV-16 | MINOR doctrinal | RESOLVED | **«Dios» no añade inferencia.** | D1/teología. | Moverlo a nomenclatura doctrinal y evitar usar el término como premisa o evidencia; mantener Total(R) ≠ Ground(R) explícito. |
| REV-17 | MAJOR fundacional | RESOLVED | **Zorn sobre clases propias requiere compromisos adicionales.** | [I6b]. | Limitar el teorema a posets set-sized o especificar teoría de clases/principio de elección global usado; documentar el compromiso. |
| REV-22 | BLOCKER fundacional | PARTIAL | **La aplicabilidad set-sized de Zorn se deriva condicionalmente de PON + las condiciones de smallness de REV-25.** | Tamaño del poset / fundamentos del teorema. | PON hace set-sized cada componente $[q]_{\sim}$; bajo $\mathrm{SigSmall}_i$ y $\mathrm{ActualSep}_i$, el universo de hechos y la colección de fragmentos StructAdm son sets. Así la ruta A de REV-22 queda demostrada condicionalmente. La ruta directa a $\operatorname{SemTotal}$ evita Zorn, pero no REV-24. Cerrar cuando REV-23 y REV-25 queden justificadas o se adopte otra base fundacional. |
| REV-23 | BLOCKER fundacional/metaontológico | OPEN | **PON no está justificada: un token podría tener proper-class many vecinos ontológicos inmediatos bajo $\bowtie$.** | Ruta directa a $\operatorname{SemTotal}$; smallness del régimen. | Justificar independientemente que $N(q)=\{r\mid q\bowtie r\}$ es set-sized para todo token actual, o sustituir PON por una condición más débil que siga haciendo set-sized cada componente finitamente conectado. No vale definir $\Lambda_*$ o «régimen» de forma que smallness resulte por estipulación. |
| REV-24 | BLOCKER doctrinal | OPEN | **Exhaustividad semántica no implica automáticamente totalidad ontológica.** | Conclusión del teorema directo / `ExistsR`. | El teorema construye un máximo de fragmentos semánticos positivos actuales y demuestra $\operatorname{SemTotal}_i(S_i^*)$. Para concluir $\operatorname{ExistsR}$ debe justificarse independientemente un puente $\mathrm{OTB}_i$ que explique cuándo esa exhaustividad representa el alcance ontológico exhaustivo del régimen. No vale definir `OntTotal` como mera maximalidad en el mismo poset ni resolver el paso por notación. |
| REV-25 | BLOCKER fundacional/semántico | OPEN | **La smallness de la firma y el paso por Separation son premisas independientes aún no justificadas.** | Construcción de $\Phi_i^{\mathrm{all}}$ y smallness del poset. | Justificar $\mathrm{SigSmall}_i$: firma set-sized y aridad set-sized para cada símbolo; la finitariedad es suficiente pero no necesaria. Además justificar $\mathrm{ActualSep}_i$: «actualmente verdadero» debe estar disponible como condición definible en la metateoría sobre el set de átomos candidatos, o sustituir Separation por una construcción equivalente explícita. |
| REV-18 | BLOCKER | RESOLVED | **El puente mínimo entre contenido emergente y dominio procesual queda tipado mediante fragmentos semánticos positivos actuales.** | Interpretación emergentista de $\mathfrak K$. | Se adopta $X=(T_X,\Phi_X)$ con $\operatorname{Adm}_i:=\operatorname{StructAdm}_i$; incidencia es pertenencia al carrier semántico y `EClosed_i` es una propiedad del contenido. El dominio no se reifica como entidad adicional. Este cierre es de tipos y no resuelve el paso de exhaustividad semántica a totalidad ontológica, registrado en REV-24. Reabrir REV-18 si se exige una noción de dominio más fuerte que fragmento positivo actual well-formed. |
| REV-19 | BLOCKER | RESOLVED | **El desajuste temporal y la ambigüedad del orden procesual quedan resueltos tipando el objeto como fragmento procesual semántico $X=(T_X,\Phi_X)$ y definiendo $\preceq_i^{\mathrm{proc}}$ por inclusión de contenido positivo actual.** | Tipo temporal y orden del dominio del teorema. | $\mathfrak P_i^{\mathrm{proc}}$ contiene fragmentos well-formed; $\mathfrak D_i^{\mathrm{proc}}$ se define aparte mediante $\operatorname{Adm}_i$. Incidencia se interpreta como pertenencia al carrier semántico; snapshots quedan como operación derivada opcional. K1/K2/admisibilidad no forman parte del cierre de este finding y permanecen en REV-20/09/18/07. |
| REV-20 | BLOCKER | PARTIAL | **K1 está matemáticamente caracterizada y deja de ser blocker independiente de la ruta directa.** | Existencia de extensiones cerradas / ruta Zorn. | Bajo StructAdm + COV, $K1_i\iff\mathrm{PSB}_i$; además PON implica PSB. Por tanto REV-20 queda subordinada a REV-23 en la ruta directa. Mantenerla PARTIAL para la arquitectura Zorn hasta cerrar la smallness local. |
| REV-21 | MAJOR formal | RESOLVED | **La no-degeneración de $F_i$ en sistemas ricos queda caracterizada exactamente por la estructura del grafo de eventos emergentes.** | Poder discriminante de $F_i$ más allá del toy. | Los puntos fijos son exactamente los subconjuntos forward-closed; el mínimo que contiene $s$ es $\operatorname{Reach}_i(s)$; existe punto fijo propio no vacío iff algún cono de alcanzabilidad es propio; el único punto fijo no vacío es $\Sigma_i$ iff el grafo es fuertemente conexo. Una función de progreso estricta sobre todos los eventos impide ciclos y, si $|\Sigma_i|>1$, garantiza un cierre propio. |
| FORM-01 | MAJOR | RESOLVED | **820 pares de sintaxis matemática inline no soportada tal como está escrita.** | Documento completo. | Convertir matemática inline a sintaxis GitHub soportada y comprobar renderizado. |
| FORM-02 | MAJOR | RESOLVED | **47 pares de bloques con delimitadores `$` aislados.** | Documento completo. | Convertir a `$$ ... $$` y comprobar renderizado. |
| FORM-03 | MAJOR | RESOLVED | **El comando MathJax inválido `Tau` con barra inversa aparecía 9 veces.** | Sección procesual. | Sustituir por símbolo/comando válido y comprobar renderizado. |
| FORM-04 | MAJOR | RESOLVED | **P3 tiene definiciones divergentes.** | PR body, programa, delta, H2a/O5e. | Una sola taxonomía canónica; cualquier taxonomía histórica debe marcarse como superada y fecharse. |
| FORM-05 | MAJOR | RESOLVED | **§16 e [I6d] enuncian teoremas distintos.** | Resúmenes. | Tener una única especificación normativa del teorema; los resúmenes deben referenciarla, no reescribirla. |
| FORM-06 | MAJOR | RESOLVED | **Etiquetas/taxonomía fuera de orden y semánticamente mezcladas.** | D/H/I/O/C. | Reemplazar por esquema estable: Definición, Axioma/Hipótesis, Lema/Teorema, Objeción, Resultado histórico superado. |
| DOC-01 | BLOCKER revisión | RESOLVED | **Tres resúmenes divergentes y crecimiento por acreción.** | PR body, §16, §20. | Una sola sección «Estado actual»; PR body enlaza, no duplica. |
| DOC-02 | BLOCKER revisión | RESOLVED | **Documento monolítico de ~5.8k líneas irrevisable.** | Documento completo. | Consolidar, archivar versión acumulativa y reducir el documento principal a una narración auditable; separar ledger y bibliografía. |
| DOC-03 | BLOCKER revisión | RESOLVED | **Contradicciones sin historia explícita.** | Documento completo. | Reescribir cronológicamente: hipótesis inicial → ataques → revisiones → resultados superados → estado actual; nada antiguo debe parecer simultáneamente vigente. |
| DOC-04 | MAJOR | PARTIAL | **Referencias insuficientes.** | Todos los bloques conceptuales. | Toda tesis que reutilice/debata literatura existente debe citar autores y obra; añadir mapa bibliográfico temático con relevancia exacta. |
| DOC-05 | MAJOR | RESOLVED | **88 puntos de investigación sin jerarquía.** | Programa de investigación. | Convertirlos en backlog vinculado a IDs del ledger; eliminar duplicados y priorizar bloqueadores/majors/minors. |

## Avance de REV-03

- **REV-03 permanece PARTIAL.** La candidata independiente se ha corregido para que la emergencia esté localizada al evento concreto: el estado resultante debe tener un comparador con el mismo perfil local y distinto valor macro, y debe habilitar al menos una traza de transición que el comparador no puede ejecutar.
- La macrovariable ya no es booleana por obligación: $P:\Sigma\to V_P$.
- La antigua separación `OrgDep` + `DynEff` se elimina por redundancia; con macro-invariancia y un testigo local con distinto valor de $P$, la organización distinta queda forzada.
- Se añade un modelo juguete explícito de cuatro componentes (camino → ciclo) donde la organización cíclica habilita `activate`.
- En este punto intermedio REV-04 seguía abierto; queda cerrado posteriormente al construirse $F_M$ y el punto fijo propio explícito $S=\{p,c\}$.

## Cierre formal de REV-01, REV-02 y REV-04

- **REV-01 RESOLVED:** fijado $M$, la relación de eventos induce un operador $F_M$ de alcanzabilidad emergente. Extensividad, monotonía interna e idempotencia se demuestran. La revisión del argumento de Zorn muestra además que F2 era redundante: F1 + F3 bastan para elevar cotas y para el paso de exhaustividad.
- **REV-02 RESOLVED:** el inhibidor no es un contraejemplo a F2 interna porque cambia el sistema y por tanto cambia el operador. Se conserva el contraejemplo cross-system y el lema de extensión conservativa como caracterización de cuándo los eventos sí se transportan.
- **REV-04 RESOLVED:** el toy produce el punto fijo propio $S=\{p,c\}$ con $F_M(S)=S\neq\Sigma_M$.
- **REV-18 PARTIAL:** ya existe un puente mínimo por incidencia y `EClosed`; sigue pendiente justificarlo ontológicamente y demostrar sus propiedades sobre dominios procesuales.
## Nuevos bloqueadores tras normalizar el teorema

- **REV-18 PARTIAL:** el puente mínimo se reduce a incidencia de configuraciones/eventos actuales en dominios y al predicado `EClosed`; ya no se exige un embedding fuerte en un powerset.
- **REV-19 RESOLVED:** el tipo y el orden procesual quedan fijados; las deudas restantes pertenecen a admisibilidad, K1/K2 y puente ontológico.
- **REV-20 OPEN:** K1/cofinalidad es una premisa sustantiva nueva de la forma operator-free; definir qué significa cerrado no demuestra que todo dominio tenga una extensión cerrada.
- **REV-09 PARTIAL** concentra la admisibilidad ontológica de la cota K2; **REV-10 RESOLVED** porque la ruta vigente ya no usa la factorización oculta; **REV-07** concentra K3/directedness.
## Avance de REV-20

- **REV-20 permanece OPEN.** K1 se caracteriza exactamente como cofinalidad de los dominios cerrados.
- Bajo elección, K1 equivale a la existencia de un selector extensivo e idempotente $F$ con $\operatorname{Fix}(F)=\mathfrak K$; no implica monotonía.
- Se demuestra independencia: en $\mathfrak D=\{0<1\}$ con $\mathfrak K=\{0\}$, K2 y K3 se cumplen pero K1 falla.
- El toy system-relative sí satisface K1 mediante $Y=F_M(X)$; la deuda restante es específicamente ontológica/procesual.
## Avance de K2 / REV-09–10

- **REV-09 pasa a PARTIAL.** Para cadenas de fragmentos procesuales compatibles, la unión formal de dominios E-closed sigue siendo E-closed: cualquier origen presente en la unión ya aparece en algún estadio, cuyo cierre contiene también evento y resultado.
- La deuda restante es ontológica: demostrar que la unión/direct limit formal pertenece realmente a $\mathfrak D_i^{\mathrm{proc}}$ o que existe otra cota procesual admisible.
- **REV-10 queda RESOLVED para la ruta vigente.** La inferencia oculta de presentabilidad/factorización de H8 ha sido eliminada; no se usa para probar preservación de cierre.
## Localidad ontológica de la emergencia

- La teoría de emergencia queda indexada por régimen: $\mathcal E_i$, $\mathfrak D_i^{\mathrm{proc}}$, $\mathfrak K_i$, $K1_i$–$K3_i$ y máximo semántico interno $S_i$.
- K1–K3 pueden establecer $\operatorname{SemTotal}_i(S_i)$; la promoción a un $R_i$ ontológico requiere REV-24/$\mathrm{OTB}_i$.
- Incluso suponiendo cerrados esos puentes para varios regímenes, no se infiere $\exists R_{\mathrm{abs}}$ de $\forall i\,\exists R_i$.
- La notación de una familia de $S_i$ es solo metalingüística; una familia de $R_i$ solo procede condicionalmente donde se haya satisfecho $\operatorname{OntTotal}_i$.
- One-R/Many-R queda desacoplado del teorema emergentista.
- REV-07 queda PARTIAL por la justificación de $\Lambda_*$ y de la clausura por caminos finitos; K3_i ya se deriva bajo StructAdm.
- REV-08 y REV-14 quedan RESOLVED en sus ataques originales al retirarse los maximales dirigidos como definición de índice y la noción de «Verdad Absoluta indexada».
## Avance de REV-07 — identidad de régimen

- Se introduce una familia $\Lambda$ de relaciones ontológicas **actualmente instanciadas** y una relación simétrica $q\bowtie r$ cuando alguna de esas relaciones enlaza los tokens.
- La clausura reflexivo-transitiva $\sim$ de $\bowtie$ es una equivalencia; sus clases son candidatos a regímenes ontológicos.
- Para dominios no vacíos, $\operatorname{Reg}(X)=i$ cuando todos los tokens incidentes en $X$ pertenecen a la misma clase $i$.
- La definición prohíbe usar K3, cotas comunes, $R_i$, `SameIndex`, `EClosed`, semejanza, isomorfismo, compartir leyes o mera posibilidad de interacción como criterio suficiente de enlace.
- Se demuestra independencia con un toy mínimo: dos dominios pueden ser `SameRegime` porque sus tokens están ontológicamente enlazados y, sin embargo, no existir en la familia de dominios ninguna cota común. Por tanto identidad de régimen no contiene K3.
- REV-07 permanece PARTIAL porque $\Lambda$ y su invariancia representacional requieren justificación, y $K3_i$ sigue necesitando una premisa adicional de admisibilidad de agregación.
## Avance de REV-07 — admisibilidad de $\Lambda_*$

- $\Lambda_*$ se define a nivel pre-régimen: no puede depender de $i$, $R_i$, K3, `SameRegime` ni `EClosed`.
- Toda instancia enlazante debe ser actual, ontológica, token-specific, desempeñar un rol integrador, poder evaluarse localmente sin totalización y ser invariante bajo representación fiel.
- Roles admitidos provisionalmente: proceso/incidencia, causalidad actual, constitución/parthood según la ontología concreta, dependencia ontológica token-specific y relación espaciotemporal cuando sea aplicable.
- Se bloquean explícitamente hubs abstractos: compartir universal, propiedad, tipo, ley, ecuación, isomorfismo o modelo no conecta regímenes.
- Correlación estadística y relaciones físicas no clásicas no entran automáticamente: necesitan una interpretación ontológica independiente que satisfaga los mismos criterios.
- REV-07 sigue PARTIAL porque la taxonomía de roles integradores todavía debe justificarse y K3_i sigue siendo una obligación separada.
## Avance de REV-07 — derivación local de K3_i

- **EEA:** si un dominio contiene un token $q$ y $q\bowtie r$, debe existir una extensión admisible que incorpore $r$.
- **OAM:** si dos dominios comparten un token actual, debe existir una extensión admisible común.
- Como `SameRegime` significa conectividad por caminos finitos de $\bowtie$, iterar EEA desde $X$ alcanza un token de $Y$; OAM produce entonces una cota común.
- Por tanto, para dominios no vacíos, $\mathrm{EEA}+\mathrm{OAM}\Rightarrow K3_i$.
- Si se permite un dominio vacío, basta además exigir que sea bottom.
- Esto reduce K3_i a dos principios locales que no usan `SameRegime` como sinónimo de amalgamabilidad. REV-07 sigue PARTIAL hasta justificar EEA/OAM y $\Lambda_*$.
## Cierre de REV-19 — orden procesual

- El dominio procesual semántico queda tipado como $X=(T_X,\Phi_X)$ con tokens y hechos actuales well-formed.
- $X\preceq_i^{\mathrm{proc}}Y$ significa $T_X\subseteq T_Y$ y $\Phi_X\subseteq\Phi_Y$: crecimiento de contenido positivo actual.
- Representaciones concretas se comparan solo a través del contenido que denotan; esto hace el orden invariante a recodificación.
- Incidencia se vuelve semánticamente precisa: $q\trianglelefteq_i X$ iff $q\in T_X$.
- La admisibilidad se separa como $\operatorname{Adm}_i(X)$; por tanto cerrar REV-19 no cierra REV-18, REV-20 ni REV-09.

## Cierre de REV-21 — estructura de puntos fijos

- $\operatorname{Fix}(F_i)$ coincide con los subconjuntos forward-closed del grafo emergente.
- Los puntos fijos corresponden a uniones forward-closed de SCCs en el grafo de condensación.
- El único punto fijo no vacío es $\Sigma_i$ exactamente cuando el grafo emergente es fuertemente conexo.
- Si existe una función de progreso estricta a lo largo de todas las aristas emergentes, el grafo es acíclico y no puede degenerar de ese modo cuando tiene más de un estado.
## Objetivo No-R y restricción del Muro

- El objetivo fuerte queda formulado como refutar $\operatorname{NoR}$ mostrando la existencia de al menos un máximo E-closed $R_i$ en algún régimen no vacío.
- K1 no puede justificarse por muestreo interno: el Muro impide convertir observación parcial del régimen en certificación universal.
- REV-20 exige por ello una derivación estructural/no enumerativa.
- REV-17 sigue RESOLVED respecto del teorema abstracto set-sized, pero aparece REV-22 como obligación de **aplicabilidad** al régimen ontológico real.
- Una ruta alternativa a hacer set-sized todo $\mathfrak D_i^{\mathrm{proc}}$ es exhibir un esqueleto cofinal set-sized $\mathfrak C_i$; Zorn sobre ese esqueleto basta para producir un máximo de todo el régimen si la cofinalidad y las propiedades K se preservan.
## Admisibilidad estructural y reducción de bloqueadores

- Se adopta normativamente $\operatorname{Adm}_i:=\operatorname{StructAdm}_i$: dominio = fragmento semántico positivo, actual y well-formed del régimen, no entidad ontológica adicional.
- **REV-18 RESOLVED:** incidencia y `EClosed_i` quedan tipados sobre ese contenido semántico.
- **REV-09 RESOLVED en alcance set-indexed:** uniones de cadenas preservan StructAdm y `EClosed`.
- **K3_i queda derivada:** la unión de dos dominios del mismo régimen es una cota común admisible; REV-07 queda reducido a la justificación de $\Lambda_*$.
- **REV-20 PARTIAL:** OEA/CUA se derivan; K1 sigue si además vale LSE_i (emergencia localmente set-like).
## Reducción final de REV-20

- PSB_i: para todo estado actual $s$, la colección $\operatorname{Out}_i(s)$ de eventos emergentes actuales con source $s$ es set-sized.
- PSB implica LSE para cualquier conjunto de sources mediante Replacement + Union.
- Con StructAdm, PSB implica SO y, mediante la construcción por rondas finitas, K1_i.
- La negación de PSB exige una ramificación local extrema: proper-class many eventos emergentes actuales desde un único estado.
- REV-20 permanece PARTIAL porque esa smallness puntual todavía debe justificarse; no se deriva de lógica pura.
## Ruta directa a SemTotal y blockers restantes

- Si PON vale, cada componente de conectividad finita $[q]_{\sim}$ es set-sized.
- Bajo $\mathrm{SigSmall}_i$ + $\mathrm{ActualSep}_i$ + StructAdm se construye directamente $S_i^*=([q]_{\sim},\Phi_i^{\mathrm{all}})$ y se demuestra $\operatorname{SemTotal}_i(S_i^*)$.
- La construcción no necesita K1/K2/K3 ni Zorn.
- PON implica PSB, así que REV-20 deja de ser blocker independiente de la construcción semántica.
- PON + REV-25 hace set-sized el poset de fragmentos, por lo que REV-22 queda resuelta condicionalmente en su ruta A una vez justificadas esas premisas.
- **REV-23 OPEN:** falta justificar PON sin construir smallness por definición.
- **REV-25 OPEN:** falta justificar la smallness/definibilidad necesaria para formar el universo de hechos actuales.
- **REV-24 OPEN:** incluso obteniendo $\operatorname{SemTotal}$, falta justificar el puente independiente a $\operatorname{OntTotal}$ y por tanto a $\operatorname{ExistsR}$.
## Alcance de algunos cierres
- **REV-01 está RESOLVED solo en alcance formal.** F1/F2-interna/F3 son propiedades de la clausura reflexivo-transitiva de cualquier relación binaria del tipo adecuado; no constituyen por sí mismas contenido emergentista. El contenido específico vive en $\mathcal E_M$ y por eso REV-03 sigue PARTIAL.
- **REV-04 está RESOLVED solo respecto de su criterio mínimo original:** existe un punto fijo propio explícito. No prueba no-degeneración en sistemas ricos; esa deuda queda separada como REV-21.
- **DOC-02/DOC-03 tuvieron una regresión por acreción durante esta tanda.** Se corrige extrayendo las antiguas secciones 3.1–3.7 a un documento técnico no normativo y marcando allí el diagnóstico erróneo sobre F2 como SUPERSEDED.

- **REV-05 y REV-06 están RESOLVED únicamente como problemas de presentación y clasificación.** Se corrigió la retórica: los resultados analíticos se etiquetan como analíticos/definicionales y se separan del programa sustantivo. Esto **no constituye avance ontológico** ni responde al hecho de que gran parte de lo actualmente demostrado siga siendo analítico.
- **REV-15 vuelve a OPEN.** Identificar la deuda —separar función regulativa de consecuencias empíricas— no satisface el criterio de cierre; falta producir consecuencias discriminantes o establecer explícitamente que la tesis carece de ellas y qué estatus filosófico tiene entonces.

## Regla de trazabilidad

Cada cambio que cierre o avance un finding debe añadir aquí: estado nuevo, evidencia, commit y nota de lo que siga abierto.

## Historial de resoluciones

| Fecha | ID | Cambio | Evidencia | Commit |
|---|---|---|---|---|
| 2026-09-22 | — | Ledger creado a partir de la revisión consolidada. | Este archivo. | 2070f899 |
| 2026-09-22 | DOC-02/DOC-03 | Documento acumulativo archivado y documento principal reescrito como crónica con un único estado normativo. | Documento principal + archivo histórico. | 70e561a, 9cfb857 |
| 2026-09-22 | FORM-01/02/03 | Documento vigente: 672 líneas,  aisladas, 0 usos del comando `Tau` con barra inversa. | Verificación sobre blob 321779c. | 9cfb857 |
| 2026-09-22 | DOC-01/FORM-04/FORM-05/FORM-06 | Descripción de PR reducida a índice; taxonomías/teoremas históricos viven solo en cronología/archivo. | PR #12 + Sección I del documento principal. | PR body actualizado tras 9cfb857 |
| 2026-09-22 | DOC-04 | Creado mapa bibliográfico temático; sigue PARTIAL hasta completar referencias primarias para cualquier concepto que vuelva al núcleo. | autodescripcion-realidad-distincion-references.md | e445175 |
| 2026-09-22 | REV-05/REV-06 | R=F(R) y consecuencias de totalidad reclasificadas como analíticas/condicionales; se separan del programa fuerte. | Sección I.2–I.4. | 9cfb857 |
| 2026-09-22 | REV-11 | Eliminada carga asimétrica: absolutismo y expansionismo quedan como posiciones abiertas con literatura explícita. | Sección I.6 + mapa bibliográfico. | 9cfb857, e445175 |
| 2026-09-22 | REV-12/REV-13 | H1/fractalidad retiradas del núcleo probatorio; branching no implica fractalidad. | Sección I.9 y Fase 7. | 9cfb857 |
| 2026-09-22 | REV-16 | “Dios” queda como nomenclatura doctrinal; Total(R) != Ground(R) permanece abierto. | Sección I.11. | 9cfb857 |
| 2026-09-22 | REV-17 | El lema de maximalidad vigente se restringe explícitamente a un poset set-sized. | Sección I.4 y Fase 5. | 9cfb857 |
| 2026-09-22 | REV-15 | Estado corregido de PARTIAL a OPEN: nombrar la deuda no la resuelve. | Ledger + sección normativa. | f0d36c5, 777c3fd |
| 2026-09-22 | REV-05/REV-06 | Se explicita que su cierre es editorial/clasificatorio, no avance sustantivo. | Sección “Alcance de algunos cierres”. | 777c3fd |
| 2026-09-22 | LEDGER-FIX | Eliminada la copia duplicada introducida por c014d98 y corregida la celda de evidencia con `$` cerrado. | Recuento de IDs + estructura del fichero. | 0c2266f |

| 2026-09-22 | REV-03 | Definida candidata independiente de emergencia organizacional dinámicamente efectiva; añadidos tests mínimos y literatura. Estado OPEN → PARTIAL. | Sección I.3.1 + mapa bibliográfico. | b3461d1, 2d62a69 |
| 2026-09-22 | REV-03 | Definición localizada al evento, macrovariable generalizada, capacidad por trazas y modelo juguete de cuatro componentes. | Sección I.3.1. | bd1ee6a |
| 2026-09-22 | REV-01/REV-02 | **SUPERSEDED:** se documentó erróneamente que el fallo de F2 rompía el paso de cota fija de Zorn. La corrección posterior demuestra $X\preceq U\preceq F(U)$ usando F1 + transitividad, sin F2. Se conserva esta fila solo como historia del error. | Documento técnico, pasaje marcado SUPERSEDED; corrección en §3.3/§4. | bd1ee6a → b4dcf23/e0e58ae |

| 2026-09-22 | REV-02 | Contraejemplo de inhibición + extensión conductualmente conservativa + lema de preservación de eventos. Estado OPEN → PARTIAL. | Sección I.3.2 + referencias de sistemas de transición. | 7bce3e0, 97b6967, b60b739 |
| 2026-09-22 | REV-01 | Construido $F_M$ como clausura emergente reflexivo-transitiva; derivadas F1/F2 interna/F3; F2 eliminada del teorema abstracto por redundante. | Sección I.3.3 + §4 revisado. | b4dcf23, 08127fc |
| 2026-09-22 | REV-02 | Distinguida monotonía interna de cambio cross-system; finding cerrado sin negar la inhibición contextual. | Secciones I.3.2–I.3.3. | b4dcf23 |
| 2026-09-22 | REV-04 | Toy explícito produce un punto fijo propio $S=F_M(S)\neq\Sigma_M$. | Sección I.3.3. | b4dcf23 |
| 2026-09-22 | REV-18 | Nuevo blocker: puente de tipos entre $F_M:\mathcal P(\Sigma_M)\to\mathcal P(\Sigma_M)$ y $F:\mathfrak D_i\to\mathfrak D_i$. | Sección I.3.3 + §4. | b4dcf23 |
| 2026-09-22 | REV-01/REV-18 | Reconciliadas las formas operator y operator-free: K1–K3 muestran la dependencia real de Zorn; F1+F3 inducen cofinalidad de Fix(F); F2 no es necesaria para elevar cotas. | §4 normalizado. | e0e58ae, f59a380 |
| 2026-09-22 | REFERENCES | Añadidas referencias explícitas a Tarski y familias de Moore para separar closure operators estándar del lema operator-free usado aquí. | Mapa bibliográfico. | 524cbca |
| 2026-09-22 | REV-18 | Puente simplificado a incidencia + `EClosed`; estado OPEN → PARTIAL. | Sección I.3.4. | d0f7fb2 |
| 2026-09-22 | REV-19 | Registrado desajuste diacrónico/sincrónico como blocker independiente. | Sección I.3.5. | d0f7fb2 |
| 2026-09-22 | REV-20 | Registrada cofinalidad K1 de dominios E-closed como obligación independiente. | §4 + ledger. | ab3c6be |
| 2026-09-22 | REV-19 | Elegida provisionalmente la ruta procesual para el teorema emergentista; definidos fragmentos procesuales mínimos y separación $T_{\mathrm{proc}}\neq T_{\mathrm{syn}}$. Estado OPEN → PARTIAL. | Sección I.3.5. | 0330795 |
| 2026-09-22 | REV-20 | K1 aislada como carga independiente; equivalencia con selector extensivo-idempotente bajo elección y contraejemplo K2+K3 sin K1. | Sección I.3.6. | 6e63ba3 |
| 2026-09-22 | REV-09 | Demostrada preservación formal de `EClosed` bajo uniones de cadenas procesuales compatibles; queda abierta la admisibilidad ontológica de la cota. Estado OPEN → PARTIAL. | Sección I.3.7. | 3eb89a4 |
| 2026-09-22 | REV-10 | Eliminada del teorema vigente la derivación que requería StageFactorization/presentabilidad; finding cerrado en su alcance original. | Sección I.3.7. | 3eb89a4 |
| 2026-09-22 | DOC-02/DOC-03 | Corregida regresión por acreción: 3.1–3.7 extraídas del estado normativo a un documento técnico; el principal vuelve a resumen de estado. | Documento principal + `work/autodescripcion-realidad-distincion-derivaciones-2026-09-22.md`. | c23223d, f2ff32e |
| 2026-09-22 | REV-07 | Criterio reforzado: K3 excluye Strong Many-R dentro del régimen y no puede usarse como argumento no circular a favor de One-R global. | Ledger + resumen normativo. | 605644a, d510e29 |
| 2026-09-22 | REV-21 | Registrada deuda de no-degeneración de $F_M$ en grafos de emergencia ricos; REV-04 permanece cerrado solo en su criterio mínimo. | Ledger + resumen normativo. | 605644a |
| 2026-09-22 | REV-07 | K3 queda indexada como $K3_i$; el teorema solo obtiene $R_i$ y deja de usarse como argumento para One-R global. Estado OPEN → PARTIAL; queda pendiente criterio independiente de identidad del régimen. | §§3.2 y 4. | a74e993, 7faeab8 |
| 2026-09-22 | REV-08 | Retirada la definición de índices mediante maximales dirigidos y retirada definitiva de $\operatorname{VA}(o)=R_i$. Finding cerrado sin probar partición global. | §7. | 7faeab8 |
| 2026-09-22 | REV-14 | Separadas exhaustividad interna $\operatorname{Truth}_i$ y absolutidad global $\operatorname{Truth}_{\mathrm{abs}}$; «Verdad Absoluta indexada» queda SUPERSEDED. | §§3.2 y 7. | a74e993, 7faeab8 |
| 2026-09-22 | REV-07 | Definido criterio candidato de régimen mediante enlace ontológico actual $\bowtie$ y componentes de $\sim$; demostrado con contraejemplo que `SameRegime` no implica K3. | §5 + documento técnico + mapa de referencias. | f282ed4, d7858f5, 3a43cf2 |
| 2026-09-22 | REV-07 | Restringida $\Lambda_*$ mediante seis criterios de admisibilidad y tests anti-colapso; universales/leyes/isomorfismo dejan de poder actuar como hubs de régimen. | §5 + documento técnico + referencias. | 02a8a4f, 3608b23, f4f7159 |
| 2026-09-22 | REV-07 | Derivado $K3_i$ desde Edge Extension Admissibility + Overlap Amalgamation para dominios no vacíos; caso vacío cubierto si existe bottom. | §5 + documento técnico. | 96a1461, 5db283e, 22d670e |
| 2026-09-22 | REV-19 | Fijado el tipo $X=(T_X,\Phi_X)$, el orden por inclusión de contenido positivo y la separación entre well-formedness y $\operatorname{Adm}_i$. Estado PARTIAL → RESOLVED. | §9 + documento técnico. | 447aaba, be0c606 |
| 2026-09-22 | REV-21 | Caracterizados exactamente los puntos fijos por forward-closure/SCCs; degeneración total iff fuerte conectividad. Estado OPEN → RESOLVED. | Documento técnico + resumen normativo. | f423b0a, be0c606 |
| 2026-09-22 | REV-08/REV-14 | Se registra como concesión doctrinal explícita que retirar $\operatorname{VA}(o)=R_i$ elimina el puente formal hacia una realidad/verdad absoluta; recuperarlo exigiría argumento metaontológico nuevo. | §7.3. | be0c606 |
| 2026-09-22 | REV-20 | Criterio de cierre endurecido por el Muro: K1 requiere justificación estructural/no enumerativa; muestreo interno no basta. | §§3.2 y 10. | 73185c4 |
| 2026-09-22 | REV-22 | Registrada la aplicabilidad fundacional del teorema; añadida ruta por esqueleto cofinal set-sized para no exigir que todo el régimen sea un conjunto. | Documento técnico + ledger. | 7c2bed7 |
| 2026-09-22 | REV-18/REV-09 | Adoptada admisibilidad estructural mínima; incidencia, OEA y uniones de cadenas quedan tipadas y preservan admisibilidad. REV-18 y REV-09 pasan a RESOLVED en su alcance actual. | §§3.3, 9 + documento técnico. | 9cd5a22, 3a85d03 |
| 2026-09-22 | REV-07 | Con StructAdm, la unión de dos dominios del mismo régimen es una cota común admisible; K3_i se deriva y REV-07 queda reducido a la justificación de $\Lambda_*$. | §5.5 + documento técnico. | 2b91afd |
| 2026-09-22 | REV-20 | K1 derivada desde StructAdm + LSE mediante construcción por rondas finitas; estado OPEN → PARTIAL hasta justificar LSE. | Documento técnico. | de880f1b, 833d60b |
| 2026-09-22 | REV-20 | LSE reducida a PSB por-token; StructAdm + PSB implica K1 mediante cierre por rondas finitas. REV-20 queda PARTIAL únicamente por la justificación de PSB. | §§3.4 + documento técnico. | 1a400fc, f360d50 |
| 2026-09-22 | REV-20 | Demostrada la equivalencia $K1_i\iff\mathrm{PSB}_i$ bajo StructAdm + COV + dominios set-sized; la deuda queda reducida exactamente a ramificación emergente local set-like. | §3.4 + documento técnico. | c0a5b6e, 23fd959 |
| 2026-09-22 | REV-23 | Introducida PON como la premisa explícita de smallness local de la construcción directa; tras REV-24 se precisa que PON conduce a $\operatorname{SemTotal}$, no por sí sola a Exists-R. | §4.0 + documento técnico. | af794e7, ba9af92, 836eeb9 |
| 2026-09-22 | REV-20/REV-22 | PON implica PSB/K1 y, junto con las premisas de firma, hace set-sized el régimen/poset; ambas deudas dejan de ser blockers independientes de la construcción semántica directa. | §4.0 + ledger. | af794e7, ba9af92 |
| 2026-09-22 | REV-24 | Reabierto explícitamente el problema histórico de §18.15: un máximo de fragmentos semánticos no equivale por sí solo a totalidad ontológica. La conclusión directa se rebaja a $\operatorname{SemTotal}$ y la cobertura se mantiene tipada semánticamente. | §§1.1, 3, 4.0 + ledger. | 836eeb9, c540e58 |
| 2026-09-22 | REV-25 | Separadas las premisas de smallness de firma y Separation. La aridad finita se reconoce como suficiente pero no necesaria; se introduce $\mathrm{ActualSep}_i$. | §4.0 + documento técnico + ledger. | 7f56973 |
| 2026-09-22 | REV-24 consistency / Codex P1 | Eliminada la segunda definición incompatible de `NoR` y toda inferencia normativa K1–K3 ⇒ `R_i`. K1–K3 producen `SemTotal_i(S_i)`; `ExistsR` requiere además `OTB_i`. La misma corrección se aplica al bloque REC/Muro, One-R/Many-R y al teorema abstracto del documento técnico. | §§3.2, 4, 7, 10 + documento técnico. | b25dd8a, cd34220 |

## Evidencia de consolidación documental

Tras el commit 9cfb857, el documento normativo principal funciona como crónica + estado actual. La versión antigua se conserva como evidencia histórica, pero sus contradicciones no se consideran tesis simultáneamente vigentes.

Estado sustantivo actual: REV-03 y REV-07 permanecen PARTIAL; REV-20 y REV-22 permanecen PARTIAL como rutas subordinadas/alternativas; REV-15, REV-23, REV-24 y REV-25 permanecen OPEN. La ruta directa demuestra condicionalmente $\operatorname{SemTotal}$, no todavía $\operatorname{ExistsR}$. Para llegar a Exists-R son sustantivos REV-07 (identidad y clausura finita de régimen), REV-23 (PON), REV-24 (puente semántica→ontología) y REV-25 (firma/Separation), además de la suficiencia doctrinal de REV-03 si se quiere que `EClosed` tenga contenido emergentista fuerte. REV-01, REV-02, REV-04, REV-08, REV-10, REV-14, REV-19 y REV-21 están RESOLVED en su alcance explícitamente acotado.
