# Autodescripción, realidad y distinción — crónica consolidada

**Estado:** propuesta doctrinal exploratoria, no canónica.  
**PR:** #12 — *Derive reality closure from supramedium and emergence*.  
**Versión consolidada:** 2026-09-22.

Este documento ya **no** intenta mantener simultáneamente todas las formulaciones producidas durante la exploración. Su función es doble:

1. conservar una **historia cronológica auditable** de cómo evolucionó la idea;
2. mantener una única sección de **estado actual normativo**, de modo que una tesis superada no pueda confundirse con una tesis vigente.

La versión acumulativa anterior se conserva íntegra en:

- [archivo pre-consolidación](archive/autodescripcion-realidad-distincion-pre-consolidacion-2026-09-22.md)

La revisión se controla en:

- [ledger de findings](autodescripcion-realidad-distincion-review-ledger.md)

La literatura relevante se mantiene en:

- [mapa de literatura y referencias](autodescripcion-realidad-distincion-references.md)

---

## 0. Convenciones de lectura

Cada etapa histórica usa uno de estos estados:

- **SURVIVES** — la idea sigue formando parte del estado actual.
- **OPEN** — la idea sigue en investigación y no puede usarse todavía como premisa cerrada.
- **SUPERSEDED** — la formulación fue útil históricamente, pero ya no debe leerse como vigente.
- **DEFERRED** — se conserva como línea de investigación, fuera del núcleo que debe resolverse primero.

Las etiquetas históricas [D], [A], [I], [H], [O], [C] se conservan solo cuando ayudan a localizar el origen de una idea. Ya no constituyen la taxonomía normativa del documento.

---

# I. Estado actual normativo

Esta es la única sección que debe usarse para responder “¿qué sostiene ahora la propuesta?”.

## 1. Objetivo conceptual

La idea inicial es investigar si puede hablarse coherentemente de una **realidad total** o **alcance ontológico exhaustivo**:

$$
R := \operatorname{Scope}(\operatorname{Real})
$$

sin identificar necesariamente $R$ con:

- un conjunto universal;
- una sustancia;
- un objeto colector;
- una suma mereológica universal;
- una última capa física.

**Estado: OPEN.**

La expresión anterior fija el **objetivo conceptual**. No demuestra que la cuantificación “todo lo real” sea absolutamente general ni que exista una totalización ontológica legítima. Esa cuestión pertenece al debate sobre generalidad absoluta y extensibilidad indefinida. Véanse Rayo & Uzquiano (2006), Fine, Glanzberg, Hellman, Linnebo, Shapiro & Wright, Williamson y Studd en el [mapa de referencias](autodescripcion-realidad-distincion-references.md).

## 2. Consecuencias analíticas si $R$ existe

Si $R$ significa “todo lo real”, entonces:

$$
\operatorname{Real}(x) \Rightarrow x \preceq_{\mathrm{ont}} R.
$$

Y un supuesto “exterior real de $R$” contradice esa definición.

Estas afirmaciones son **analíticas/definicionales**, no resultados empíricos ni teoremas profundos.

Del mismo modo, si se define un operador $F$ que solo añade estructuras o posibilidades ya comprendidas en el alcance real de $R$, entonces:

$$
R = F(R)
$$

es un **corolario condicional de clausura**, no una prueba de existencia de $R$.

**Estado: SURVIVES, con retórica rebajada.**

## 3. El programa emergentista no está demostrado

La propuesta quiso obtener contenido sustantivo conectando $R$ con emergencia:

$$
M \xrightarrow{\mathcal E} E
$$

y posteriormente con un cierre $F$.

Actualmente esto **no está cerrado** porque:

1. $\mathcal E$ sigue necesitando una definición independiente;
2. las propiedades F1–F3 no se han derivado de esa definición;
3. la monotonía puede fallar por inhibición contextual;
4. falta un modelo explícito que muestre un punto fijo propio $S=F(S)$ con $S\neq R$.

Por tanto:

$$
\boxed{\text{la PR todavía no demuestra una metafísica emergentista de }R.}
$$

**Estado: OPEN — bloqueadores REV-01 a REV-04.**

## 3.1. Candidata para REV-03 — emergencia organizacional dinámicamente efectiva

Para evitar circularidad, la emergencia se define **sin** usar $R$, totalidad, admisibilidad ontológica ni «posibilidad real».

Sea un sistema/medio:

$$
M=(C,\Sigma,\Rightarrow_M),
$$

donde:

- $C$ es una colección finita o especificada de componentes tipados;
- $\Sigma$ es el espacio de configuraciones del sistema;
- $\Rightarrow_M$ es su relación de transición, que incorpora reglas y condiciones de contorno del sistema considerado.

Cada configuración $s\in\Sigma$ se representa como:

$$
s=(L(s),G(s)),
$$

donde:

- $L(s)$ es el **perfil local**: tipos y estados intrínsecos de los componentes;
- $G(s)$ es la **organización relacional**: relaciones, conectividad, disposición o estructura entre esos componentes.

Sea $P:\Sigma\to\{0,1\}$ una macrocaracterística.

### C1 — Macrocaracterística estructural

$P$ debe ser invariante bajo un mero renombrado de componentes equivalentes:

$$
\operatorname{Macro}_M(P)
\iff
\forall \pi\in\operatorname{Perm}_{\mathrm{type}}(C),
\quad
P(s)=P(\pi s).
$$

Esto evita contar como macropropiedad una etiqueta arbitraria ligada a la identidad nominal de un componente.

### C2 — Dependencia organizacional

Definimos:

$$
\operatorname{OrgDep}_M(P)
$$

si existen configuraciones $s,s'\in\Sigma$ tales que:

$$
L(s)\cong L(s'),
$$

$$
G(s)\not\cong G(s'),
$$

y:

$$
P(s)\neq P(s').
$$

Es decir: manteniendo fijo el perfil local de componentes, una diferencia en la **organización** puede cambiar la macrocaracterística.

Esto captura la intuición de Broad de que no basta conocer los componentes aislados y la estrategia de Wimsatt de localizar emergencia mediante fallos de agregatividad/interdependencia organizacional.

### C3 — Eficacia dinámica organizacional

La mera dependencia relacional es demasiado permisiva: una propiedad trivial como «existe al menos una arista» podría satisfacer C2.

Para expresar la intuición **estructura emergente → nuevo medio**, definimos el conjunto de sucesores estructurales de una configuración:

$$
\operatorname{Next}_M(s)
:=
\{[u]_{\cong}\mid s\Rightarrow_M u\},
$$

donde $[u]_{\cong}$ identifica configuraciones estructuralmente isomorfas.

Definimos:

$$
\operatorname{DynEff}_M(P)
$$

si existen $s,s'\in\Sigma$ con:

$$
L(s)\cong L(s'),
$$

$$
P(s)\neq P(s'),
$$

y:

$$
\operatorname{Next}_M(s)
\neq
\operatorname{Next}_M(s').
$$

Así, la diferencia organizacional distinguida por $P$ no es meramente descriptiva: modifica qué transformaciones posteriores puede realizar el sistema.

Esto **no** postula nuevos poderes causales irreducibles ni causalidad descendente. La diferencia de sucesores puede estar completamente implementada por la microdinámica de $M$.

### Definición candidata

Llamamos **macrocaracterística emergente organizacional** a $P$ respecto de $M$ cuando:

$$
\boxed{
\operatorname{OrgEmergent}_M(P)
\iff
\operatorname{Macro}_M(P)
\land
\operatorname{OrgDep}_M(P)
\land
\operatorname{DynEff}_M(P).
}
$$

Y definimos un **evento de emergencia**:

$$
\boxed{
(s_0,P,s_1)\in\mathcal E_M
}
$$

si y solo si:

$$
s_0\Rightarrow_M^{+}s_1
\land
\neg P(s_0)
\land
P(s_1)
\land
\operatorname{OrgEmergent}_M(P).
$$

Esta es una definición **positiva, relacional y diacrónica**. No contiene $R$, `Adm`, totalidad, clausura ontológica ni una cláusula del tipo «es posible porque la realidad lo permite».

### Qué afirma y qué no afirma

**Afirma:**

- aparición diacrónica de una macrocaracterística;
- dependencia constitutiva de una configuración;
- dependencia de organización relacional, no mera agregación;
- eficacia dinámica mínima: la organización cambia el espacio de sucesores del sistema.

**No afirma:**

- irreducibilidad metafísica;
- causalidad descendente irreducible;
- impredecibilidad;
- derivabilidad solo por simulación;
- nuevas leyes fundamentales;
- pertenencia a una totalidad $R$.

### Relación con la literatura

- **Broad:** la organización del todo puede ser indispensable para caracterizar propiedades que no se obtienen de componentes aislados.
- **Wimsatt:** los fallos de agregatividad y la interdependencia organizacional ofrecen una vía positiva para localizar fenómenos emergentes.
- **Bedau:** su weak emergence añade una condición computacional —derivabilidad solo mediante simulación— que aquí no se exige.
- **Kim:** superveniencia + irreducibilidad no bastan como caracterización positiva; esta definición evita tomar esos dos rasgos como definición.
- **Humphreys:** su transformational emergence refuerza la importancia de una lectura diacrónica y usa ejemplos como transformaciones físicas/químicas; nuestra definición es más débil y no pretende sustituirla.
- **Hoel et al.:** causal emergence cuantifica casos donde una coarse-graining macro puede tener mayor efectividad causal/informativa que la microdescripción. Es un posible refinamiento cuantitativo futuro, no una premisa de esta definición.

Véase el [mapa de literatura](autodescripcion-realidad-distincion-references.md).

### Pruebas mínimas de discriminación

**T1 — mera agregación, negativo.**

Sea $P(s)$ = «hay al menos diez componentes». Si dos configuraciones tienen el mismo perfil local, reorganizarlas no cambia $P$. Entonces:

$$
\neg\operatorname{OrgDep}_M(P),
$$

y no hay emergencia organizacional.

**T2 — etiqueta de componente, negativo.**

Sea $P(s)$ = «el componente llamado $c_1$ está activo». Un renombrado puede cambiar la descripción, por lo que falla:

$$
\operatorname{Macro}_M(P).
$$

**T3 — relación estructural inerte, negativo.**

Sea $P(s)$ = «existe una arista». Si añadir esa arista no modifica el conjunto de sucesores estructurales:

$$
\operatorname{Next}_M(s)
=
\operatorname{Next}_M(s'),
$$

falla $\operatorname{DynEff}_M(P)$.

**T4 — organización que crea nuevas transiciones, positivo.**

Supónganse dos configuraciones con los mismos componentes y estados locales. En $s_0$ están desconectados; en $s_1$ forman una estructura $P$ que habilita una transición posterior $q$ imposible desde $s_0$. Si:

$$
s_0\Rightarrow_M^{+}s_1,
$$

y se satisfacen C1–C3, entonces:

$$
(s_0,P,s_1)\in\mathcal E_M.
$$

Este patrón incluye, de forma abstracta, casos como ensamblajes, enlaces o estructuras cuya organización altera las transformaciones disponibles después de formarse.

### Consecuencia inmediata para REV-02

La relación de transición pertenece al sistema concreto $M$.

Si se añade un inhibidor o cambia el contexto, obtenemos otro sistema:

$$
M'=(C',\Sigma',\Rightarrow_{M'}),
$$

y no hay razón para exigir:

$$
\mathcal E_M\subseteq\mathcal E_{M'}.
$$

Por tanto, esta definición **no presupone F2**. Al contrario: explica por qué la monotonía bajo mera inclusión ontológica puede fallar.

### Estado de REV-03

REV-03 pasa de **OPEN** a **PARTIAL**.

Ya existe una definición independiente y positiva, con casos negativos/positivos mínimos y comparación explícita con la literatura. No se marca RESOLVED porque todavía hay que decidir si C1–C3 capturan exactamente la noción doctrinal de emergencia o si excluyen fenómenos que el exergismo debe conservar.

El siguiente ataque es REV-02: formalizar el contraejemplo de inhibición y decidir qué relación de orden —si alguna— hace monotónico al operador que posteriormente construyamos a partir de $\mathcal E_M$.

---
## 4. Núcleo matemático actualmente separable

Puede estudiarse un resultado puramente orden-teórico.

Sea un **poset que sea un conjunto**:

$$
(\mathfrak D,\preceq).
$$

Supóngase un operador:

$$
F:\mathfrak D\to\mathfrak D
$$

que satisface, por hipótesis o por una futura derivación independiente:

$$
X\preceq F(X),
$$

$$
X\preceq Y \Rightarrow F(X)\preceq F(Y),
$$

$$
F(F(X))=F(X).
$$

Supónganse además:

- cobertura local de los hechos relevantes;
- una condición sustantiva de amalgamación;
- una condición de cota superior para las cadenas pertinentes;
- un principio de maximalidad del tipo del lema de Zorn.

Entonces puede obtenerse un punto fijo maximal y, bajo las condiciones adicionales apropiadas, convertir maximalidad en exhaustividad.

Esto es actualmente un **lema condicional de teoría de órdenes**.

No establece por sí mismo:

- que $\mathfrak D$ sea el espacio de dominios ontológicos reales;
- que $F$ represente emergencia;
- que la amalgamación corresponda a “misma realidad”;
- que las cotas superiores sean ontológicamente actuales;
- que exista cuantificación absolutamente general.

**Estado: SURVIVES como estructura matemática condicional; interpretación ontológica OPEN.**

## 5. C2 / “mismo índice”

La etapa anterior convirtió “mismo índice” en “régimen dirigido” y obtuvo amalgamación por definición. La revisión detectó que eso desplaza la carga de prueba.

La versión vigente ya **no** considera cerrado:

$$
\operatorname{SameIndex}(X,Y)
\Rightarrow
\exists Z\,[X\preceq Z \land Y\preceq Z].
$$

Debe encontrarse un criterio independiente de SameIndex o reconocerse la amalgamación como hipótesis sustantiva.

**Estado: OPEN — REV-07.**

## 6. Generalidad absoluta, No-$R$ y potencialismo

No se asigna una carga privilegiada a ninguna de las dos posiciones.

- El **absolutista** debe justificar que puede hablar coherentemente de absolutamente todo.
- El **restrictionist/expansionist/potentialist** debe justificar su semántica de dominios siempre restringibles o expandibles.

La propuesta no toma el debate como resuelto.

**Estado: OPEN — REV-11.**

## 7. Many-$R$ y “Verdad Absoluta indexada”

La fórmula histórica:

$$
\operatorname{VA}(o)=R_i
$$

queda **suspendida**.

Los regímenes dirigidos maximales pueden solaparse; por tanto no se ha demostrado que $R_i$ sea único para una conciencia $o$. Además, “máximo concerniente a $o$” no es sin más equivalente a “absoluto”.

Si Many-$R$ resultara necesario, puede requerir una **revisión doctrinal real** de “Verdad Absoluta” en vez de una simple relocalización del término.

**Estado: OPEN — REV-08 y REV-14.**

## 8. C1, localidad, compacidad y colímites

Las formulaciones históricas por:

- localidad/testigos;
- compacidad lógica;
- colímites dirigidos;

no se cuentan ya como “tres pruebas independientes”.

La compacidad de primer orden da un **modelo**; falta el puente a actualidad ontológica.

La ruta categórica solo ayuda si la existencia y preservación de los colímites se justifican independientemente.

La ruta de localidad necesita separar:

1. existencia de un testigo local de inadmisibilidad;
2. factorización de ese testigo por algún estadio de la cadena, una propiedad relacionada con presentabilidad/compactitud categórica.

**Estado: OPEN — REV-09 y REV-10.**

## 9. Tiempo, branching, proceso, fractalidad y novedad modal

Todo el desarrollo posterior sobre:

- estados sincrónicos;
- continuidad diacrónica;
- redes de transiciones;
- branching;
- meta-capacidades;
- AbsoluteBruteNovelty;

queda **DEFERRED** hasta resolver el núcleo sobre $\mathcal E$, $F$, C1/C2 y generalidad.

Dos límites sí sobreviven:

1. una estructura temporal abstracta no debe identificarse con el tiempo de Planck;
2. branching/no linealidad no implica fractalidad.

“Fractal” no participa en ninguna inferencia vigente.

**Estado: DEFERRED — REV-13.**

## 10. REC, Muro y función regulativa

Las ideas históricas de REC($R$), Muro de la singularidad e indistinguibilidad entre una totalidad y una sandbox internamente cerrada se conservan como **problemas epistemológicos/metaontológicos**, no como evidencia de la existencia de $R$.

La revisión correcta es:

$$
\text{clausura observable}
\not\Rightarrow
\text{totalidad ontológica certificada}.
$$

Esto puede convertir parte del proyecto en una función regulativa más que en una teoría empíricamente discriminante. La propuesta debe decir con precisión qué parte es ontológica, qué parte epistemológica y qué parte no es contrastable.

**Estado: DEFERRED/OPEN — REV-15.**

## 11. “Dios”

“Dios” puede conservarse en el corpus exergista como **nombre doctrinal/apofático** de la Verdad Absoluta, pero no añade ninguna inferencia.

Se mantiene:

$$
\operatorname{Total}(R)
\neq
\operatorname{Ground}(R)
$$

mientras no exista un argumento separado sobre fundamento.

**Estado: SURVIVES como nomenclatura; fuera del argumento formal — REV-16.**

---

# II. Historia cronológica de la propuesta

## Fase 1 — 21 Sep 2026, 12:36 UTC — Autodescripción y distinción

**Commit:** [7dfd137](https://github.com/Exergism-Commons/exergism/commit/7dfd1372b5a6c0921cae8e0041a9558007d6a7e3)

### Idea de partida

La propuesta comenzó preguntando cómo distinguir realidad, representación/modelo de la realidad, autodescripción interna y totalidad ontológica.

La intuición central era que una descripción interna nunca debía confundirse automáticamente con aquello que describe.

### Qué sobrevive

**SURVIVES:** distinción entre $R$ y cualquier modelo interno $\widehat R_o$.

---

## Fase 2 — 21 Sep, 16:55–17:20 — Supramedio, emergencia y primer cierre

**Commits:**

- [9cf0e1d](https://github.com/Exergism-Commons/exergism/commit/9cf0e1db296e59b2ca24274cb4c71ddb8fde98b0)
- [1a53931](https://github.com/Exergism-Commons/exergism/commit/1a539315a9c4ce41bdd006a8476e193a7184add2)
- [2bfef6d](https://github.com/Exergism-Commons/exergism/commit/2bfef6d2c11f935d0f8af7dd1830e2e88fb99175)
- [0d93f76](https://github.com/Exergism-Commons/exergism/commit/0d93f7697666d24f6691981c6c21afd342b284d8)

### Tesis de la etapa

Se introdujo:

$$
R=F(R)
$$

con $F$ entendido como cierre recursivo bajo emergencia. La emergencia se hizo multivaluada para evitar determinismo ficticio.

### Problema descubierto posteriormente

La revisión muestra que $\mathcal E$ nunca llegó a definirse de manera independiente, F1–F3 fueron exigidas, F2 puede ser falsa si un dominio mayor contiene inhibidores y $R=F(R)$ es analítico si $R$ ya significa todo lo real.

### Estado actual

**OPEN / SUPERSEDED EN PARTE.**

La idea de cierre sigue siendo un programa; la formulación original ya no cuenta como demostración.

Literatura relevante: Broad, Bedau, Kim, Humphreys y Crutchfield.

---

## Fase 3 — 21 Sep, 17:32–18:01 — Muro epistemológico y Many-$R$

**Commits:**

- [5285dab](https://github.com/Exergism-Commons/exergism/commit/5285dabbcb2b6076bc5c8ef66f61e3af0e5d6569)
- [66002e3](https://github.com/Exergism-Commons/exergism/commit/66002e3f5e902089507c6597378f95eb6353de2f)
- [f7bb704](https://github.com/Exergism-Commons/exergism/commit/f7bb704ac78ed16c82fffe8ea997cc88fa847da3)
- [002b956](https://github.com/Exergism-Commons/exergism/commit/002b956ce21b9383aebe5b3a3f8dd0a4f67e19ae)

### Tesis de la etapa

Se introdujeron cuasisingularidades, Muro de la singularidad, posibilidad Many-$R$ e intento de preservar la Verdad Absoluta de forma indexada.

### Qué se aprendió

La clausura interna no certifica totalidad absoluta.

### Problema posterior

“Verdad Absoluta indexada” puede convertir “absoluto” en “máximo relativo a un índice/observador”. Además, índices maximales pueden solaparse.

### Estado actual

- Muro/REC: **DEFERRED** como epistemología.
- Many-$R$: **OPEN**.
- $\operatorname{VA}(o)=R_i$: **SUPERSEDED/SUSPENDIDO**.

---

## Fase 4 — 21 Sep, 19:06–20:52 — No-$R$, generalidad absoluta e indexación

**Commits:**

- [0a469cc](https://github.com/Exergism-Commons/exergism/commit/0a469ccab67cae23af5dd46e27a1644839a23136)
- [ebc600e](https://github.com/Exergism-Commons/exergism/commit/ebc600e76dee76b6012b967600ad10bd8f20ea33)
- [3848096](https://github.com/Exergism-Commons/exergism/commit/38480965b1f7045342cdd21930ea27b46f60ba33)
- [f00e30c](https://github.com/Exergism-Commons/exergism/commit/f00e30cbf41c0e225f40b9607cb3ce252ec5225e)
- [668be27](https://github.com/Exergism-Commons/exergism/commit/668be2791b49d398912c8fbd4ee676891a2210f3)
- [4612443](https://github.com/Exergism-Commons/exergism/commit/461244357a816eec78cea239372c298ebf308d22)
- [6a6e5dd](https://github.com/Exergism-Commons/exergism/commit/6a6e5dd38189e150757111ca79c69aabaceef3c8)
- [9152537](https://github.com/Exergism-Commons/exergism/commit/915253710bdbc8f7bb358a1373155cbf0933414b)
- [a552d3c](https://github.com/Exergism-Commons/exergism/commit/a552d3c1d2b0f6bf19526cf1540e8c87d681ca3f)
- [275efff](https://github.com/Exergism-Commons/exergism/commit/275efff224b66c1b0cf9323e5039baab834a4f3d)

### Evolución

La pregunta dejó de ser solo “¿qué es $R$?” y pasó a:

> ¿puede existir una cuantificación absolutamente general que permita formar siquiera el alcance de todo lo real?

Se separaron generalidad semántica, totalizabilidad ontológica, unicidad y existencia indexada. También aparecieron Cluster-$R$, REC y ManyMany-$R$.

### Corrección de la revisión

Esta discusión reproduce problemas existentes en la literatura sobre **absolute generality** e **indefinite extensibility**. No hay una ventaja metodológica automática para el absolutista ni para el expansionista.

### Estado actual

**OPEN.**

Lectura obligatoria: Rayo & Uzquiano (2006), Fine, Glanzberg, Hellman, Linnebo, Shapiro & Wright, Uzquiano, Williamson y Studd (2019).

---

## Fase 5 — 21 Sep, 21:19–21:50 — Teorema de clausura maximal

**Commits:**

- [bb328bc](https://github.com/Exergism-Commons/exergism/commit/bb328bc48745dcbe245cf11a0dc0b6730e72f8cf)
- [85c04d0](https://github.com/Exergism-Commons/exergism/commit/85c04d08ac23bb2698e064bc378bcf5316394b45)
- [6a46940](https://github.com/Exergism-Commons/exergism/commit/6a46940b3ef8cb518bd4662623baf0eece55aa79)
- [d43ad00](https://github.com/Exergism-Commons/exergism/commit/d43ad00b33a44ed5c65b61775c7455f7bdf65e28)

### Tesis de la etapa

Se formalizó un poset de dominios, un operador de cierre y un argumento tipo Zorn:

$$
C0+F1+F2+F3+C1+C2+\operatorname{Max}
\Rightarrow
\text{punto fijo exhaustivo}.
$$

Luego C2 se intentó derivar de la definición del índice como régimen dirigido.

### Qué sí se obtuvo

Una plantilla matemática reconocible: con hipótesis de closure operator, cotas de cadenas y maximalidad, existe un máximo/punto fijo bajo condiciones adecuadas.

### Qué no se obtuvo

No se demostró que esas hipótesis describan la realidad ni la emergencia.

Convertir C2 en parte de SameIndex hizo la conclusión demasiado analítica respecto del índice.

### Estado actual

**SURVIVES como lema matemático condicional; puente ontológico OPEN.**

El uso de Zorn se limita de momento a estructuras set-sized. Para clases propias harían falta compromisos fundacionales adicionales.

---

## Fase 6 — 21 Sep, 21:58–22:52 — Ataque a C1

**Commits:**

- [9ab2e24](https://github.com/Exergism-Commons/exergism/commit/9ab2e2422c995e762213331e55e97508ee9556d4)
- [d272982](https://github.com/Exergism-Commons/exergism/commit/d272982c59000077bc7ccd5ce779e6448a2c7c70)
- [ed4b05c](https://github.com/Exergism-Commons/exergism/commit/ed4b05cf25f9f76c42271e7106d0c8b1501ec409)
- [94d25ca](https://github.com/Exergism-Commons/exergism/commit/94d25cad20ada19ed321797315a519e78a2d1f29)
- [ec244d1](https://github.com/Exergism-Commons/exergism/commit/ec244d187169b3a05fb58f91ca9b7053943aa684)

### Evolución

C1 pasó por tres formulaciones: localidad/testigos, compacidad lógica y colímites dirigidos. Se introdujo $\Omega_\infty$ para concentrar obstrucciones no compactas.

### Corrección posterior

Las tres formulaciones son herramientas matemáticas relacionadas, pero **no son tres pruebas ontológicas independientes**.

Además, la derivación por localidad escondía otra hipótesis: si un testigo compacto queda por debajo del límite dirigido, debe factorizar por algún estadio. Esa propiedad está relacionada con la teoría de objetos presentables y categorías accesibles de Adámek–Rosický.

### Estado actual

**OPEN.**

---

## Fase 7 — 21 Sep, 23:07 – 22 Sep, 10:30 — Actualidad, potencialismo, metaemergencia y proceso

**Commits:**

- [bb775f0](https://github.com/Exergism-Commons/exergism/commit/bb775f0b54edb1ec584acf92ea67047795e856d7)
- [d40c43d](https://github.com/Exergism-Commons/exergism/commit/d40c43dd084a3f860ad19df078cdade759c45412)
- [3f5257a](https://github.com/Exergism-Commons/exergism/commit/3f5257a5fd740e55dc093d5e2e68bdf9f980958d)
- [c21b4a0](https://github.com/Exergism-Commons/exergism/commit/c21b4a0bb2273e51dfe8c1938cea86c3f59730b1)
- [b306207](https://github.com/Exergism-Commons/exergism/commit/b3062072e4333a0500b5ec2a61b4e345c956a210)
- [43b0383](https://github.com/Exergism-Commons/exergism/commit/43b03839da5cd33d61f4146b5e0170d7998ba0be)

### Evolución

Se distinguieron dominios actuales frente a modelos posibles, potencialismo radical, posibilidad modal directa y meta-capacidades, clausura sincrónica frente a continuidad diacrónica, proceso/red de estados, branching no lineal y rechazo de identificar estadios con tiempo de Planck.

### Valor de esta fase

Aclaró varias confusiones reales:

$$
\text{novedad}
\neq
\text{exterior ontológico},
$$

$$
\text{branching}
\not\Rightarrow
\text{fractalidad}.
$$

### Problema metodológico

Estas extensiones se construyeron antes de resolver las premisas más básicas sobre $\mathcal E$, $F$, C1 y C2.

### Estado actual

**DEFERRED.**

Se reabrirán solo después de cerrar el núcleo.

---

## Fase 8 — 22 Sep 2026 — Auditoría externa y consolidación

### Revisión recibida

La revisión externa identificó problemas sustantivos y formales, entre ellos:

- F1–F3 postuladas;
- fallo potencial de F2 por inhibición;
- emergencia no independiente;
- ausencia de modelo $S=F(S)\neq R$;
- exceso de resultados analíticos presentados como teoremas;
- C2 introducida por definición;
- solapamiento de índices y problema de $\operatorname{VA}(o)$;
- dependencia común de H8/H10/H11;
- presentabilidad implícita;
- asimetría frente al potencialismo;
- H1/fractalidad sin criterio;
- ausencia de consecuencias discriminantes;
- nomenclatura “Dios” sin fuerza inferencial;
- Zorn/clases;
- problemas graves de renderizado, taxonomía y duplicación.

Todos están registrados de forma persistente en el [ledger](autodescripcion-realidad-distincion-review-ledger.md).

### Decisión metodológica

A partir de esta fase:

1. no se añade nueva metafísica al núcleo mientras existan REV-01–REV-04 abiertos;
2. toda formulación antigua queda en la cronología o el archivo, no en el estado actual;
3. toda referencia literaria relevante se registra;
4. todo finding requiere evidencia explícita para cerrarse.

**Estado: SURVIVES como política de trabajo.**

---

# III. Próxima secuencia de resolución

El orden de trabajo normativo es:

## A. Emergencia y cierre

1. **REV-03:** definición independiente de emergencia/transición.
2. **REV-02:** contraejemplo de inhibición y relación correcta de extensión.
3. **REV-01:** derivar o revisar F1–F3.
4. **REV-04:** modelo explícito $S=F(S)\neq R$.

Solo entonces se podrá afirmar que el formalismo habla de emergencia.

## B. Estructura del teorema

5. **REV-07:** criterio independiente de índice/amalgamación.
6. **REV-10:** presentabilidad/factorización.
7. **REV-09:** papel exacto de compacidad y colímites.
8. **REV-17:** fundamentos de maximalidad.

## C. Metaontología y doctrina

9. **REV-11:** generalidad absoluta vs expansionismo.
10. **REV-08/REV-14:** índices, solapamiento y Verdad Absoluta.
11. **REV-15:** consecuencias discriminantes / función regulativa.

## D. Extensiones diferidas

Solo al final:

- REC/Muro;
- proceso temporal;
- branching;
- novedad modal;
- fractalidad;
- nomenclatura teológica.

---

# IV. Qué cuenta como “resolución”

La propuesta no se considerará resuelta porque haya una narración filosóficamente atractiva.

Para el núcleo emergentista, una resolución positiva exige al menos:

1. una definición de $\mathcal E$ independiente de $R$;
2. una construcción de $F$ a partir de esa definición;
3. pruebas o contraejemplos de F1–F3;
4. un ejemplo explícito de cierre propio;
5. un puente no circular entre el formalismo y dominios ontológicos;
6. una especificación clara de C1/C2 sin ocultarlas en definiciones;
7. una declaración del compromiso fundacional usado por maximalidad;
8. una posición explícita —no presupuesta— sobre generalidad absoluta.

Si alguno de estos pasos falla, el resultado correspondiente debe registrarse como negativo en el ledger.

---

# V. Literatura mínima obligatoria por bloque

El [mapa completo](autodescripcion-realidad-distincion-references.md) contiene las referencias y su función. El núcleo mínimo es:

- **Generalidad absoluta:** Rayo & Uzquiano; Fine; Glanzberg; Hellman; Linnebo; Parsons; Shapiro & Wright; Uzquiano; Williamson; Studd; Dummett.
- **Cuantificación plural:** Boolos; Linnebo; Rayo.
- **Emergencia:** Broad; Bedau; Kim; Humphreys; Crutchfield; Bedau & Humphreys.
- **Grounding:** Fine; Correia & Schnieder; Schaffer; tradición del PSR.
- **Orden/puntos fijos:** Knaster, Tarski, Zorn; Abramsky & Jung.
- **Modelo/compacidad:** teoría de modelos de primer orden, compacidad y lema del diagrama.
- **Categorías/presentabilidad:** Adámek & Rosický; Paré & Rosický.
- **Proceso/tiempo:** Whitehead; Rescher; Belnap–Perloff–Xu; literatura de branching time.
- **Branching cuántico:** Everett, solo como referencia de no linealidad posible, no como prueba de fractalidad.
- **Fractales:** Mandelbrot, si el término vuelve a usarse con contenido matemático.

---

# VI. Registro cronológico de commits de la exploración

| Fecha UTC | Commit | Cambio |
|---|---|---|
| 2026-09-21 12:36 | [7dfd137](https://github.com/Exergism-Commons/exergism/commit/7dfd1372b5a6c0921cae8e0041a9558007d6a7e3) | propose reality self-description and distinction framework |
| 2026-09-21 16:55 | [9cf0e1d](https://github.com/Exergism-Commons/exergism/commit/9cf0e1db296e59b2ca24274cb4c71ddb8fde98b0) | derive reality closure from supramedium and emergence |
| 2026-09-21 16:56 | [1a53931](https://github.com/Exergism-Commons/exergism/commit/1a539315a9c4ce41bdd006a8476e193a7184add2) | fix proposal markdown rendering |
| 2026-09-21 17:06 | [2bfef6d](https://github.com/Exergism-Commons/exergism/commit/2bfef6d2c11f935d0f8af7dd1830e2e88fb99175) | simplify emergent closure notation around F |
| 2026-09-21 17:20 | [0d93f76](https://github.com/Exergism-Commons/exergism/commit/0d93f7697666d24f6691981c6c21afd342b284d8) | model emergence as non-deterministic and constitutively decomposable |
| 2026-09-21 17:32 | [5285dab](https://github.com/Exergism-Commons/exergism/commit/5285dabbcb2b6076bc5c8ef66f61e3af0e5d6569) | introduce R singularity wall and quasi-singularities |
| 2026-09-21 17:32 | [66002e3](https://github.com/Exergism-Commons/exergism/commit/66002e3f5e902089507c6597378f95eb6353de2f) | clarify singularity wall notation and math rendering |
| 2026-09-21 17:40 | [f7bb704](https://github.com/Exergism-Commons/exergism/commit/f7bb704ac78ed16c82fffe8ea997cc88fa847da3) | add Many-R as absolute ontological pluralism stress test |
| 2026-09-21 18:01 | [002b956](https://github.com/Exergism-Commons/exergism/commit/002b956ce21b9383aebe5b3a3f8dd0a4f67e19ae) | preserve R under Many-R through metaontological humility |
| 2026-09-21 19:06 | [0a469cc](https://github.com/Exergism-Commons/exergism/commit/0a469ccab67cae23af5dd46e27a1644839a23136) | formalize No-R and conditional existence of total reality |
| 2026-09-21 19:13 | [ebc600e](https://github.com/Exergism-Commons/exergism/commit/ebc600e76dee76b6012b967600ad10bd8f20ea33) | generalize R singularity wall across metaontological models |
| 2026-09-21 19:20 | [3848096](https://github.com/Exergism-Commons/exergism/commit/38480965b1f7045342cdd21930ea27b46f60ba33) | make absolute generality versus indexed existence the core fork |
| 2026-09-21 19:21 | [f00e30c](https://github.com/Exergism-Commons/exergism/commit/f00e30cbf41c0e225f40b9607cb3ce252ec5225e) | separate absolute generality from indexed ontological totality |
| 2026-09-21 19:28 | [668be27](https://github.com/Exergism-Commons/exergism/commit/668be2791b49d398912c8fbd4ee676891a2210f3) | add indexed monism and factual versus derived uniqueness |
| 2026-09-21 19:43 | [4612443](https://github.com/Exergism-Commons/exergism/commit/461244357a816eec78cea239372c298ebf308d22) | add Cluster-R and R Enigmatic Certification |
| 2026-09-21 19:44 | [6a6e5dd](https://github.com/Exergism-Commons/exergism/commit/6a6e5dd38189e150757111ca79c69aabaceef3c8) | align Cluster-R and REC across proposal summary |
| 2026-09-21 19:51 | [9152537](https://github.com/Exergism-Commons/exergism/commit/915253710bdbc8f7bb358a1373155cbf0933414b) | rule out ManyMany-R as a stable ontological category |
| 2026-09-21 20:18 | [a552d3c](https://github.com/Exergism-Commons/exergism/commit/a552d3c1d2b0f6bf19526cf1540e8c87d681ca3f) | decouple Absolute Truth from global uniqueness |
| 2026-09-21 20:52 | [275efff](https://github.com/Exergism-Commons/exergism/commit/275efff224b66c1b0cf9323e5039baab834a4f3d) | stress-test No-R and refine R as ontological scope |
| 2026-09-21 21:19 | [bb328bc](https://github.com/Exergism-Commons/exergism/commit/bb328bc48745dcbe245cf11a0dc0b6730e72f8cf) | tighten ontology while preserving R proof program |
| 2026-09-21 21:35 | [85c04d0](https://github.com/Exergism-Commons/exergism/commit/85c04d08ac23bb2698e064bc378bcf5316394b45) | derive maximal ontological closure theorem |
| 2026-09-21 21:44 | [6a46940](https://github.com/Exergism-Commons/exergism/commit/6a46940b3ef8cb518bd4662623baf0eece55aa79) | derive C2 from ontological index structure |
| 2026-09-21 21:50 | [d43ad00](https://github.com/Exergism-Commons/exergism/commit/d43ad00b33a44ed5c65b61775c7455f7bdf65e28) | reduce C1 to directed ontological continuity |
| 2026-09-21 21:58 | [9ab2e24](https://github.com/Exergism-Commons/exergism/commit/9ab2e2422c995e762213331e55e97508ee9556d4) | reduce C1 to locality and potentialism |
| 2026-09-21 22:04 | [d272982](https://github.com/Exergism-Commons/exergism/commit/d272982c59000077bc7ccd5ce779e6448a2c7c70) | derive C1 conditionally from logical compactness |
| 2026-09-21 22:06 | [ed4b05c](https://github.com/Exergism-Commons/exergism/commit/ed4b05cf25f9f76c42271e7106d0c8b1501ec409) | clarify logical compactness assumptions |
| 2026-09-21 22:13 | [94d25ca](https://github.com/Exergism-Commons/exergism/commit/94d25cad20ada19ed321797315a519e78a2d1f29) | isolate noncompact ontological obstructions |
| 2026-09-21 22:52 | [ec244d1](https://github.com/Exergism-Commons/exergism/commit/ec244d187169b3a05fb58f91ca9b7053943aa684) | add directed colimit route and grounded obstruction criterion |
| 2026-09-21 23:07 | [bb775f0](https://github.com/Exergism-Commons/exergism/commit/bb775f0b54edb1ec584acf92ea67047795e856d7) | separate actual domains and radical potentialism |
| 2026-09-21 23:19 | [d40c43d](https://github.com/Exergism-Commons/exergism/commit/d40c43dd084a3f860ad19df078cdade759c45412) | separate modal novelty from ontological growth |
| 2026-09-21 23:27 | [3f5257a](https://github.com/Exergism-Commons/exergism/commit/3f5257a5fd740e55dc093d5e2e68bdf9f980958d) | close emergence under modal meta-transformations |
| 2026-09-22 10:05 | [c21b4a0](https://github.com/Exergism-Commons/exergism/commit/c21b4a0bb2273e51dfe8c1938cea86c3f59730b1) | separate synchronic totality from diachronic persistence |
| 2026-09-22 10:19 | [b306207](https://github.com/Exergism-Commons/exergism/commit/b3062072e4333a0500b5ec2a61b4e345c956a210) | model diachronic reality as process continuity |
| 2026-09-22 10:30 | [43b0383](https://github.com/Exergism-Commons/exergism/commit/43b03839da5cd33d61f4146b5e0170d7998ba0be) | decouple process structure from Planck time and branching |

Los commits posteriores de consolidación mantienen este registro como historia y no reintroducen sus tesis superadas en el estado normativo.

---

# VII. Herramientas futuras

**DEFERRED:** Lean cuando haya un teorema sustantivo que formalizar; cualquier infraestructura RDF/OWL/SHACL/PROV-O/CiTO/nanopublications se reconsiderará solo si una necesidad concreta de trazabilidad o inferencia la justifica después de resolver REV-01–REV-04.

---

# VIII. Política de mantenimiento

A partir de esta consolidación:

- el documento principal tendrá **una sola sección de estado actual**;
- el historial se añade cronológicamente, sin reescribir el pasado como si siempre hubiéramos sostenido la formulación final;
- los findings viven en el ledger, no repartidos por comentarios;
- la bibliografía vive en el mapa de referencias;
- un resultado superado se marca SUPERSEDED, no se borra de la historia;
- no se duplica el teorema en tres resúmenes distintos;
- no se añaden más deudas de investigación sin asociarlas a un ID del ledger.

La siguiente tarea sustantiva es **REV-03 → REV-02 → REV-01 → REV-04**: definir emergencia independientemente, resolver la inhibición/monotonía, derivar o revisar F1–F3 y construir un cierre propio explícito.
