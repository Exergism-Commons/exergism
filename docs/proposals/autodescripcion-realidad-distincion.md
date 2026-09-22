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

## 3. Estado actual del programa emergentista

La propuesta ya dispone de una definición independiente y event-local de emergencia, un operador system-relative construido desde ella, pruebas de F1–F3 dentro de ese tipo y un punto fijo propio explícito.

Por tanto, REV-01, REV-02 y REV-04 están cerrados en sus criterios originales, mientras REV-03 permanece PARTIAL por alcance doctrinal.

Esto **todavía no demuestra una metafísica emergentista de $R$** porque falta conectar el formalismo event-level con el tipo correcto de dominio ontológico y decidir si el teorema debe ser sincrónico o procesual.

Los bloqueadores activos relevantes pasan a ser:

- **REV-18:** puente entre eventos/configuraciones actualizadas y dominios ontológicos cerrados;
- **REV-19:** desajuste temporal entre emergencia diacrónica y el antiguo objetivo sincrónico;
- **REV-07:** amalgamación/directedness no circular;
- **REV-09/REV-10:** inductividad/cotas de cadenas;
- **REV-14/REV-15:** consecuencias doctrinales y discriminantes aún abiertas.

## 3.1. Candidata para REV-03 — emergencia organizacional localizada al evento

Para evitar circularidad, la emergencia se define **sin** usar $R$, totalidad, admisibilidad ontológica ni «posibilidad real».

### Sistema de transición

Sea un sistema/medio etiquetado:

$$
M=(C,\Sigma,A,\xrightarrow{}_M,\xrightarrow{}_{M,\mathrm{act}}),
$$

donde:

- $C$ es una colección finita o especificada de componentes tipados;
- $\Sigma$ es el espacio de configuraciones;
- $A$ es un conjunto de tipos de transición/acciones;
- $s\xrightarrow{a}_M u$ indica que la transición de tipo $a$ está **dinámicamente disponible** desde $s$;
- $s\xrightarrow{a}_{M,\mathrm{act}}u$ indica que esa transición fue **efectivamente realizada**;
- se exige:
$$
\xrightarrow{}_{M,\mathrm{act}}
\;\subseteq\;
\xrightarrow{}_M.
$$

Así se separa capacidad dinámica de actualización: una posibilidad de transición puede ser relevante para caracterizar qué habilita una organización sin convertirse por ello en un hecho actual.

Cada configuración se representa como:

$$
s=(L(s),G(s)),
$$

donde:

- $L(s)$ es el **perfil local**: tipos y estados intrínsecos de los componentes;
- $G(s)$ es la **organización relacional** entre esos componentes.

Una macrocaracterística ya no tiene por qué ser booleana:

$$
P:\Sigma\to V_P,
$$

donde $V_P$ puede ser binario, ordinal, cuantitativo o estructurado de otro modo.

### C1 — Macro-invariancia

$P$ debe ser invariante bajo renombrados type-preserving de componentes equivalentes:

$$
\operatorname{Macro}_M(P)
\iff
\forall s\in\Sigma\;
\forall \pi\in\operatorname{Perm}_{\mathrm{type}}(C),
\quad
P(s)=P(\pi s).
$$

Esto impide contar como macrocaracterística una etiqueta dependiente del nombre de un componente.

### Capacidad dinámica observable

Para no identificar «dinámica distinta» con «sucesores distintos» —condición casi trivial en cualquier dinámica no degenerada— definimos la capacidad conductual de una configuración mediante las secuencias de tipos de transición que puede ejecutar.

Sea:

$$
\operatorname{Traces}_M(s)
:=
\{
a_1\cdots a_n
\mid
\exists s_1,\ldots,s_n:
s\xrightarrow{a_1}_M s_1
\xrightarrow{a_2}_M\cdots
\xrightarrow{a_n}_M s_n
\}.
$$

Dos configuraciones pueden ser diferentes y, sin embargo, ofrecer exactamente las mismas capacidades de transición. Lo relevante aquí es que una organización **habilite una capacidad** que una organización alternativa, con el mismo perfil local, no posee.

Definimos:

$$
\operatorname{Enables}_M(s,w)
\iff
\operatorname{Traces}_M(s)
\setminus
\operatorname{Traces}_M(w)
\neq
\varnothing.
$$

Equivalente: existe al menos una transición o secuencia de transiciones ejecutable desde $s$ que no puede ejecutarse desde $w$.

### Testigo organizacional local al evento

La condición de emergencia debe ser satisfecha por el **estado resultante concreto**, no por algún par exótico situado en otra región de $\Sigma$.

Definimos:

$$
\operatorname{OrgWitness}_M(P,s_1)
$$

si existe $w\in\Sigma$ tal que:

$$
L(w)\cong L(s_1),
$$

$$
P(w)\neq P(s_1),
$$

y:

$$
\operatorname{Enables}_M(s_1,w).
$$

No es necesario añadir separadamente $G(w)\not\cong G(s_1)$. Si los perfiles locales son isomorfos y la organización también lo fuese mediante una permutación type-preserving, C1 obligaría a $P(w)=P(s_1)$, contradiciendo la segunda condición. Por tanto, la antigua condición global de dependencia organizacional era redundante una vez localizada la eficacia dinámica en el testigo concreto.

### Definición candidata de evento emergente

Un evento:

$$
e=(s_0,P,s_1)
$$

pertenece a $\mathcal E_M$ si y solo si:

$$
\boxed{
s_0\xrightarrow{+}_{M,\mathrm{act}} s_1
\land
P(s_0)\neq P(s_1)
\land
\operatorname{Macro}_M(P)
\land
\operatorname{OrgWitness}_M(P,s_1).
}
$$

Aquí $s_0\xrightarrow{+}_{M,\mathrm{act}} s_1$ significa que existe una trayectoria no vacía de **transiciones efectivamente realizadas** desde $s_0$ hasta $s_1$. Las trazas usadas por $\operatorname{OrgWitness}$ siguen calculándose sobre $\xrightarrow{}_M$, es decir, sobre capacidades disponibles.

La emergencia queda así **localizada al evento**: el propio $s_1$ debe exhibir una macrocaracterística cuyo valor depende de su organización y cuya organización habilita capacidades dinámicas ausentes en un comparador estructural $w$ con el mismo perfil local.

No basta ya con que $P$ sea «emergente en algún lugar» del espacio de estados.

### Qué afirma y qué no afirma

**Afirma:**

- novedad macroestructural diacrónica;
- no dependencia de nombres de componentes;
- dependencia de organización con perfil local controlado;
- aparición de al menos una capacidad de transición atribuible a esa diferencia organizacional.

**No afirma:**

- irreducibilidad metafísica;
- causalidad descendente irreducible;
- impredecibilidad;
- derivabilidad solo por simulación;
- nuevas leyes fundamentales;
- pertenencia a una totalidad $R$.

La microdinámica de $M$ puede implementar completamente la capacidad habilitada.

### Relación con la literatura

- **Broad:** la organización del todo puede ser indispensable para propiedades que no se determinan por componentes considerados aisladamente.
- **Wimsatt:** los fallos de agregatividad y la interdependencia organizacional proporcionan un criterio positivo para buscar emergencia.
- **Bedau:** weak emergence añade una exigencia computacional de derivación solo por simulación, aquí no adoptada.
- **Kim:** superveniencia + irreducibilidad no constituyen por sí solas una caracterización positiva suficiente.
- **Humphreys:** transformational emergence motiva tratar seriamente la generación diacrónica; nuestra definición es más débil.
- **Hoel et al.:** causal emergence ofrece un posible refinamiento cuantitativo de eficacia causal macro, no una premisa de este criterio mínimo.

La comparación de capacidades mediante trazas usa una herramienta estándar de semántica de sistemas de transición; no presupone que la realidad física sea literalmente una máquina de estados.

### Tests de discriminación

**T1 — mera agregación, negativo.**

Sea $P(s)$ = número de componentes. Reorganizar un sistema con el mismo perfil local no cambia $P$. No existe testigo $w$ con:

$$
L(w)\cong L(s_1)
\quad\text{y}\quad
P(w)\neq P(s_1).
$$

Por tanto el evento no pertenece a $\mathcal E_M$.

**T2 — etiqueta nominal, negativo.**

Sea $P(s)$ = «el componente llamado $c_1$ está activo». Falla C1 porque un renombrado type-preserving puede cambiar el valor descrito.

**T3 — estructura descriptiva pero dinámicamente inerte, negativo.**

Supónganse $s_1$ y $w$ con el mismo perfil local y distinto valor de una descripción estructural $P$, pero:

$$
\operatorname{Traces}_M(s_1)
=
\operatorname{Traces}_M(w).
$$

Entonces:

$$
\neg\operatorname{Enables}_M(s_1,w),
$$

y la diferencia estructural no cuenta como emergencia en esta noción.

**T4 — organización que habilita una capacidad, positivo.**

Si:

$$
L(w)\cong L(s_1),
$$

$$
P(w)\neq P(s_1),
$$

y existe una traza $\alpha$ tal que:

$$
\alpha\in\operatorname{Traces}_M(s_1)
\setminus
\operatorname{Traces}_M(w),
$$

entonces $s_1$ posee una capacidad habilitada por su organización que el comparador $w$ no posee.

### Modelo juguete explícito: cuatro componentes

Sea:

$$
C=\{1,2,3,4\},
$$

con los cuatro componentes del mismo tipo y en el mismo estado local `ready`.

Consideremos cuatro configuraciones:

- $p$: grafo camino $1-2-3-4$;
- $c$: grafo ciclo $1-2-3-4-1$;
- $a$: misma organización cíclica tras una activación colectiva;
- $i$: configuración inerte auxiliar.

$p$ y $c$ tienen el mismo perfil local:

$$
L(p)\cong L(c).
$$

Sea la macrocaracterística:

$$
P(s)=\beta_1(G(s)),
$$

el número ciclomático del grafo de organización. Entonces:

$$
P(p)=0,
\qquad
P(c)=1.
$$

$P$ es invariante bajo renombrado de vértices.

Definimos las capacidades dinámicas mínimas:

| Estado | Acción disponible | Destino |
|---|---|---|
| $p$ | `close` | $c$ |
| $p$ | `idle` | $p$ |
| $c$ | `activate` | $a$ |
| $c$ | `idle` | $c$ |
| $a$ | `idle` | $a$ |
| $i$ | `idle` | $i$ |

Para el episodio actual considerado fijamos además:

$$
p\xrightarrow{\texttt{close}}_{M,\mathrm{act}}c.
$$

No exigimos que `activate` se haya realizado: basta que esté disponible desde $c$ y no desde $p$ para funcionar como testigo de capacidad organizacional.

Por tanto:

$$
\texttt{activate}
\in
\operatorname{Traces}_M(c),
$$

pero:

$$
\texttt{activate}
\notin
\operatorname{Traces}_M(p).
$$

El evento:

$$
e=(p,P,c)
$$

satisface:

$$
p\xrightarrow{\texttt{close}}_{M,\mathrm{act}} c,
$$

$$
P(p)\neq P(c),
$$

y el propio $p$ sirve como testigo organizacional de $c$:

$$
L(p)\cong L(c),
$$

$$
P(p)\neq P(c),
$$

$$
\operatorname{Enables}_M(c,p).
$$

Luego:

$$
\boxed{
(p,P,c)\in\mathcal E_M.
}
$$

El ejemplo es deliberadamente pequeño y no pretende modelar vida, conciencia ni química real. Su función es demostrar que la definición es **calculable y discriminante**.

### Consecuencia para REV-02 y REV-01

Si al sistema anterior se añade un inhibidor que bloquea `close` o `activate`, se obtiene otro sistema de transición:

$$
M'=(C',\Sigma',A',\xrightarrow{}_{M'}),
$$

aunque intuitivamente contenga «más cosas».

No hay razón para esperar:

$$
\mathcal E_M\subseteq\mathcal E_{M'}.
$$

Esto convierte REV-02 en un diagnóstico formal: **la inclusión ontológica ordinaria no es una relación respecto de la cual la emergencia tenga por qué ser monótona**.

La consecuencia para REV-01 es más grave que una mera dificultad de derivación. En la ruta archivada hacia maximalidad, F2 era necesaria para convertir una cota superior $U$ de una cadena de puntos fijos en una cota superior **dentro de** $\operatorname{Fix}(F)$:

$$
X=F(X),
\quad
X\preceq U,
$$

y por F2:

$$
F(X)\preceq F(U),
$$

de donde:

$$
X\preceq F(U).
$$

Como además F3 daba:

$$
F(F(U))=F(U),
$$

$F(U)$ funcionaba como punto fijo que acotaba la cadena.

Sin monotonía, el paso:

$$
X\preceq U
\not\Rightarrow
X\preceq F(U)
$$

queda sin justificar. Por tanto, la ruta actual de Zorn **no arranca** simplemente con C1.

Así, REV-01 ya no debe formularse como «derivar F1–F3» sin más. Las opciones abiertas son:

1. encontrar una relación de **extensión conservativa** $\hookrightarrow_{\mathrm{cons}}$ respecto de la cual el operador sea monótono y reconstruir el teorema con esa relación;
2. demostrar directamente que las cadenas de $\operatorname{Fix}(F)$ poseen cotas superiores fijas por otro mecanismo, sin usar F2;
3. abandonar esa ruta de maximalidad si ninguna de las dos opciones puede justificarse.

### Estado de REV-03

REV-03 permanece **PARTIAL**.

La candidata ahora:

- es independiente de $R$;
- está localizada al evento concreto;
- admite macrovariables no booleanas;
- elimina la redundancia entre dependencia organizacional y eficacia dinámica;
- exige capacidad habilitada, no mera desigualdad entre sucesores;
- posee un modelo juguete explícito calculable.

No se marca RESOLVED hasta probarla contra una muestra más amplia de casos positivos y negativos y decidir si esta noción mínima es doctrinalmente suficiente.

En este punto de la derivación REV-04 seguía abierto; queda resuelto posteriormente en §3.3 al construirse el operador system-relative $F_M$ y el punto fijo propio explícito $S=\{p,c\}$.

---
## 3.2. REV-02 — inhibición, extensión estructural y extensión conservativa

REV-02 pregunta si el crecimiento de un sistema preserva sus emergencias. La respuesta depende de qué signifique exactamente «extender» un sistema.

### Extensión estructural bruta

Sean:

$$
M=(C,\Sigma,A,\xrightarrow{}_M)
$$

y:

$$
N=(C',\Sigma',A',\xrightarrow{}_N).
$$

Escribimos provisionalmente:

$$
M\hookrightarrow_{\mathrm{str}}N
$$

si existen inyecciones de componentes, configuraciones y etiquetas que permiten identificar dentro de $N$ una copia estructural de las descripciones de $M$, pero **sin exigir preservación de la relación de transición**.

Esta noción solo expresa algo parecido a «$N$ contiene los componentes/estructura de $M$ y además más contexto». No expresa conservación de comportamiento.

### Contraejemplo explícito por inhibición

Partimos del sistema juguete de REV-03. En $M$:

$$
p\xrightarrow{\texttt{close}}_M c
$$

y:

$$
c\xrightarrow{\texttt{activate}}_M a.
$$

El evento:

$$
(p,P,c)\in\mathcal E_M
$$

porque la organización cíclica de $c$ habilita `activate`, capacidad ausente en $p$.

Construimos ahora un sistema con inhibidor:

$$
M^{I}=(C\cup\{h\},\Sigma^{I},A,\xrightarrow{}_{I},\xrightarrow{}_{I,\mathrm{act}}),
$$

donde $h$ está en estado local `on` y bloquea `close` y `activate` en las configuraciones embebidas.

Sea:

$$
\iota(p)=p^{I},
\qquad
\iota(c)=c^{I},
\qquad
\iota(a)=a^{I}.
$$

Las transiciones relevantes son:

| Estado | Acción disponible | Destino |
|---|---|---|
| $p^I$ | `idle` | $p^I$ |
| $c^I$ | `idle` | $c^I$ |
| $a^I$ | `idle` | $a^I$ |

Aunque:

$$
M\hookrightarrow_{\mathrm{str}}M^I,
$$

ya no existe:

$$
p^I\xrightarrow{+}_{I,\mathrm{act}}c^I.
$$

Por tanto el transporte del antiguo evento falla:

$$
(p,P,c)\in\mathcal E_M
$$

pero:

$$
(p^I,P^I,c^I)\notin\mathcal E_{M^I}.
$$

Así se obtiene un contraejemplo concreto:

$$
\boxed{
M\hookrightarrow_{\mathrm{str}}N
\not\Rightarrow
\mathcal E_M\hookrightarrow\mathcal E_N.
}
$$

Esto formaliza la intuición del revisor: **añadir ontológicamente/contextualmente algo puede retirar capacidades**.

### Por qué preservar solo transiciones antiguas tampoco basta

Una noción débil de extensión podría exigir simplemente que toda transición de $M$ siga existiendo entre las imágenes de sus estados.

Eso todavía no preserva necesariamente un evento emergente. Si $w$ era el comparador que carecía de una capacidad $\alpha$, el sistema extendido podría añadir a $\iota(w)$ una ruta nueva etiquetada por $\alpha$. Entonces desaparecería la diferencia conductual que hacía de $w$ un testigo.

Por tanto hace falta no solo **preservar** capacidades antiguas, sino también **reflejar** las capacidades antiguas respecto del alfabeto original.

### Extensión conservativa de comportamiento

Sean $M$ y $N$ como antes. Escribimos:

$$
M\hookrightarrow_{\mathrm{cons}}N
$$

si existen una inyección de configuraciones:

$$
\iota:\Sigma_M\to\Sigma_N
$$

y una inyección de etiquetas:

$$
j:A_M\to A_N
$$

que satisfacen las condiciones siguientes.

**CE1 — fidelidad del perfil local.** Para cualesquiera $s,t\in\Sigma_M$:

$$
L_M(s)\cong L_M(t)
\iff
L_N(\iota(s))\cong L_N(\iota(t)).
$$

El contexto añadido no puede romper ni crear artificialmente equivalencias de perfil local entre estados embebidos.

**CE2 — preservación de actualizaciones con extremo.** Si:

$$
s\xrightarrow{\alpha,+}_{M,\mathrm{act}} t,
$$

entonces:

$$
\iota(s)\xrightarrow{j(\alpha),+}_{N,\mathrm{act}}\iota(t).
$$

Es decir, un episodio efectivamente realizado se conserva como episodio realizado y termina en la imagen del mismo estado.

**CE3 — preservación y reflexión de trazas antiguas.** Para todo $s\in\Sigma_M$:

$$
j(\operatorname{Traces}_M(s))
=
\operatorname{Traces}_N(\iota(s))
\cap
j(A_M^*).
$$

N puede introducir etiquetas y capacidades nuevas, pero sobre el alfabeto antiguo no puede borrar ni inventar trazas para los estados embebidos.

Esta condición es deliberadamente fuerte. Es una forma de **conservatividad conductual** y no debe confundirse con mera inclusión de componentes.

### Extensión compatible de una macrocaracterística

Para transportar un evento también necesitamos una macrocaracterística $P_N$ que extienda a $P_M$:

$$
P_N(\iota(s))=P_M(s)
$$

para todo $s\in\Sigma_M$, y que siga satisfaciendo:

$$
\operatorname{Macro}_N(P_N).
$$

Llamaremos a esto una extensión $P$-compatible.

### Lema REV-02.1 — preservación de eventos bajo extensión conservativa

Si:

$$
M\hookrightarrow_{\mathrm{cons}}N,
$$

$P_N$ es una extensión $P$-compatible de $P_M$, y:

$$
(s_0,P_M,s_1)\in\mathcal E_M,
$$

entonces:

$$
\boxed{
(\iota(s_0),P_N,\iota(s_1))\in\mathcal E_N.
}
$$

**Demostración.**

Del evento en $M$ existe un camino no vacío:

$$
s_0\xrightarrow{+}_{M,\mathrm{act}} s_1.
$$

Por CE2:

$$
\iota(s_0)\xrightarrow{+}_{N,\mathrm{act}}\iota(s_1).
$$

Como $P_N$ extiende a $P_M$:

$$
P_N(\iota(s_0))
\neq
P_N(\iota(s_1)).
$$

Sea $w$ un testigo de $\operatorname{OrgWitness}_M(P_M,s_1)$. Por CE1:

$$
L_N(\iota(w))
\cong
L_N(\iota(s_1)).
$$

Por compatibilidad de $P$:

$$
P_N(\iota(w))
\neq
P_N(\iota(s_1)).
$$

Además existe alguna traza antigua $\alpha$ con:

$$
\alpha\in\operatorname{Traces}_M(s_1)
\setminus
\operatorname{Traces}_M(w).
$$

Por CE3:

$$
j(\alpha)
\in
\operatorname{Traces}_N(\iota(s_1))
\setminus
\operatorname{Traces}_N(\iota(w)).
$$

Así $\iota(w)$ es un testigo organizacional para $\iota(s_1)$. Junto con $\operatorname{Macro}_N(P_N)$ se satisfacen todas las condiciones de $\mathcal E_N$. $\square$

### Qué se ha demostrado y qué no

Se han obtenido dos resultados distintos:

$$
\boxed{
\text{extensión estructural bruta}
\not\Rightarrow
\text{preservación de emergencia}
}
$$

y:

$$
\boxed{
\text{extensión conductualmente conservativa}
+
\text{compatibilidad de }P
\Rightarrow
\text{preservación de eventos emergentes}.
}
$$

Pero el contraejemplo por inhibición **no refuta la monotonía interna de un único operador**. Compara dos sistemas diferentes, y por tanto dos relaciones de emergencia diferentes:

$$
\mathcal E_M
\quad\text{frente a}\quad
\mathcal E_N.
$$

Esta distinción corrige la interpretación anterior de REV-02.

---

## 3.3. REV-01 — clausura emergente system-relative y eliminación de F2 del teorema

### Relación binaria inducida por eventos emergentes

Fijado un sistema $M$, donde $\mathcal E_M$ contiene solo **eventos emergentes efectivamente realizados**, definimos:

$$
s\leadsto_{\mathcal E_M}t
\iff
\exists P:\;
(s,P,t)\in\mathcal E_M.
$$

Sea $\leadsto_{\mathcal E_M}^{*}$ la clausura reflexivo-transitiva de esa relación.

Para cualquier conjunto de configuraciones:

$$
X\subseteq\Sigma_M,
$$

definimos el **cierre emergente system-relative**:

$$
\boxed{
F_M(X)
:=
\{
t\in\Sigma_M
\mid
\exists s\in X:\;
s\leadsto_{\mathcal E_M}^{*}t
\}.
}
$$

Esta definición se construye directamente desde la $\mathcal E_M$ independiente de REV-03.

### F1 se deriva — extensividad

Por reflexividad:

$$
s\leadsto_{\mathcal E_M}^{*}s.
$$

Por tanto:

$$
\boxed{
X\subseteq F_M(X).
}
$$

### F2 interna se deriva — monotonía con $M$ fijo

Si:

$$
X\subseteq Y,
$$

todo punto alcanzable por una cadena emergente desde algún $x\in X$ también es alcanzable desde un elemento de $Y$. Luego:

$$
\boxed{
X\subseteq Y
\Rightarrow
F_M(X)\subseteq F_M(Y).
}
$$

Esto no contradice REV-02. El inhibidor cambia $M$ y, con él, cambia el propio operador:

$$
F_M
\neq
F_{M^I}.
$$

F2 es una afirmación sobre **un mismo** $F_M$; la inhibición es una comparación **entre operadores distintos**.

### F3 se deriva — idempotencia

Sea:

$$
t\in F_M(F_M(X)).
$$

Entonces existe $u\in F_M(X)$ tal que:

$$
u\leadsto_{\mathcal E_M}^{*}t.
$$

Y existe $s\in X$ con:

$$
s\leadsto_{\mathcal E_M}^{*}u.
$$

Por transitividad de la clausura:

$$
s\leadsto_{\mathcal E_M}^{*}t.
$$

por lo que:

$$
t\in F_M(X).
$$

Junto con F1 aplicada a $F_M(X)$:

$$
F_M(X)\subseteq F_M(F_M(X)),
$$

obtenemos:

$$
\boxed{
F_M(F_M(X))=F_M(X).
}
$$

Así F1–F3 **ya no son axiomas gratuitos** para este operador concreto: son consecuencias de la clausura reflexivo-transitiva de la relación de eventos emergentes.

### Corrección del teorema: F2 nunca fue necesaria

La prueba archivada usaba F2 para mostrar que, dada una cadena:

$$
\mathcal C\subseteq\operatorname{Fix}(F),
$$

y una cota:

$$
\forall X\in\mathcal C:\;X\preceq U,
$$

$F(U)$ era una cota superior fija.

Pero basta F1.

Para cada $X\in\mathcal C$:

$$
X\preceq U
$$

y por F1:

$$
U\preceq F(U).
$$

Por transitividad:

$$
\boxed{
X\preceq F(U).
}
$$

Por F3:

$$
F(F(U))=F(U),
$$

de modo que:

$$
F(U)\in\operatorname{Fix}(F).
$$

Por tanto, para levantar una cota arbitraria de una cadena de puntos fijos a una cota **fija**, solo hacen falta:

$$
\boxed{F1+F3.}
$$

F2 era una premisa redundante.

### Exhaustividad tampoco usa F2

Sea $M_*$ un punto fijo maximal y supóngase un hecho $x$ no cubierto por $M_*$.

Por cobertura existe $X_x$ con:

$$
x\preceq X_x.
$$

Si la amalgamación proporciona $Y$ tal que:

$$
M_*\preceq Y
\quad\text{y}\quad
X_x\preceq Y,
$$

F1 da:

$$
Y\preceq F(Y),
$$

y F3:

$$
F(Y)\in\operatorname{Fix}(F).
$$

Entonces:

$$
M_*\preceq F(Y)
$$

y:

$$
x\preceq F(Y).
$$

Como $x\not\preceq M_*$, $F(Y)$ es una extensión fija estricta de $M_*$, contradiciendo maximalidad.

De nuevo, F2 no aparece.

### Teorema abstracto revisado

Sea $(\mathfrak D,\preceq)$ un poset set-sized y:

$$
F:\mathfrak D\to\mathfrak D
$$

un operador que satisface únicamente:

$$
\text{F1: }X\preceq F(X),
$$

$$
\text{F3: }F(F(X))=F(X).
$$

Supóngase además:

1. cobertura local C0;
2. toda cadena de $\operatorname{Fix}(F)$ tiene una cota superior en $\mathfrak D$;
3. un principio de maximalidad tipo Zorn aplicable;
4. amalgamación sustantiva entre el punto fijo maximal y cualquier dominio que cubra un hecho del mismo régimen.

Entonces existe un punto fijo maximal y todo punto fijo maximal es exhaustivo respecto de los hechos cubiertos por ese régimen.

Esquemáticamente:

$$
\boxed{
C0+F1+F3+C1_{\operatorname{Fix}}+C2+\operatorname{Max}
\Rightarrow
\exists R_i[
F(R_i)=R_i
\land
\operatorname{Exhaustive}_i(R_i)
].
}
$$

Esta corrección **reduce**, no aumenta, las premisas matemáticas del teorema.

### REV-04 — punto fijo propio explícito

El toy de cuatro componentes permite ya demostrar que punto fijo no implica totalidad del sistema.

Sea:

$$
\Sigma_M=\{p,c,a,i\}
$$

y supóngase que el único evento emergente del juguete es:

$$
p\leadsto_{\mathcal E_M}c.
$$

La transición `activate` de $c$ a $a$ es una transición ordinaria del sistema, no un segundo evento emergente en este toy.

Tomemos:

$$
S=\{p,c\}.
$$

Entonces:

$$
F_M(S)=\{p,c\}=S.
$$

Pero:

$$
S\neq\Sigma_M.
$$

Por tanto:

$$
\boxed{
S=F_M(S)
\land
S\neq\Sigma_M.
}
$$

Existe así un **punto fijo propio explícito y calculable**. El operador no colapsa semánticamente en «la unión de todo».

Esto satisface el criterio formal de REV-04.

### Nuevo problema revelado: puente de tipos

El avance anterior introduce una obligación que antes estaba oculta.

$F_M$ está bien definido sobre:

$$
\mathcal P(\Sigma_M),
$$

mientras el teorema ontológico pretende operar sobre:

$$
(\mathfrak D_i,\preceq_{\mathrm{ont}}).
$$

No se ha demostrado que un dominio ontológico sea un conjunto de configuraciones, ni que:

$$
\subseteq
$$

represente:

$$
\preceq_{\mathrm{ont}}.
$$

Por tanto aparece un nuevo blocker independiente:

$$
\boxed{
\text{puente entre clausura emergente system-relative y dominio ontológico}.
}
$$

Esta obligación se registra como REV-18 y evita declarar una victoria ontológica a partir de un operador formal bien construido.

### Estados después de la corrección

- **REV-01:** RESOLVED en su ataque original: existe una definición independiente de $\mathcal E_M$ y F1–F3 se derivan para el operador concreto $F_M$; además F2 no es necesaria para el teorema abstracto.
- **REV-02:** RESOLVED: la inhibición es no-monotonía **entre sistemas/operadores**, no contraejemplo a la monotonía interna de $F_M$; la extensión conservativa caracteriza cuándo sí puede transportarse un evento.
- **REV-04:** RESOLVED: existe un punto fijo propio explícito en el toy.
- **REV-18:** OPEN: falta el puente formal y ontológico entre $F_M$ sobre estados y $F$ sobre dominios.

---
## 3.4. REV-18 — puente mínimo desde eventos emergentes a dominios cerrados

El teorema operator-free de §4 ya no necesita transportar $F_M$ entero al nivel ontológico. El puente mínimo puede ser más austero.

Sea:

$$
(\mathfrak D_i^{A},\preceq_{\mathrm{ont}})
$$

el poset candidato de dominios ontológicos actuales del régimen $i$.

Introducimos una relación de incidencia:

$$
s\trianglelefteq_i X,
$$

que se lee:

> la configuración/event-token actual $s$ forma parte del contenido ontológico representado por el dominio $X$.

Esta relación no es pertenencia conjuntista y no identifica $X$ con un conjunto de estados.

### I1 — monotonicidad de incidencia

Si:

$$
s\trianglelefteq_i X
\quad\text{y}\quad
X\preceq_{\mathrm{ont}}Y,
$$

debe cumplirse:

$$
\boxed{
s\trianglelefteq_i Y.
}
$$

Es la condición mínima para que «más contenido ontológico» no pierda un hecho ya representado.

### Predicado de cierre emergente

Sea $\mathcal E_i^{\mathrm{act}}$ la relación de eventos emergentes **efectivamente actualizados** del régimen, definida localmente mediante los criterios de REV-03.

Definimos:

$$
\boxed{
\operatorname{EClosed}_i(X)
\iff
\forall(s_0,P,s_1)\in\mathcal E_i^{\mathrm{act}},
\;
s_0\trianglelefteq_i X
\Rightarrow
s_1\trianglelefteq_i X.
}
$$

Y:

$$
\boxed{
\mathfrak K_i
:=
\{
X\in\mathfrak D_i^{A}
\mid
\operatorname{EClosed}_i(X)
\}.
}
$$

Así, la familia $\mathfrak K$ del teorema de §4 recibe por fin una candidata de interpretación emergentista **sin** exigir un isomorfismo:

$$
\mathfrak D_i^{A}
\cong
\mathcal P(\Sigma_M).
$$

### Qué evita esta formulación

- no identifica dominios ontológicos con conjuntos de configuraciones;
- no identifica $\preceq_{\mathrm{ont}}$ con $\subseteq$;
- no exige un único sistema global $M_i$ que enumere todos los estados posibles;
- no necesita una función de cierre ontológica única;
- no convierte capacidades posibles en hechos actuales: $\mathcal E_i^{\mathrm{act}}$ solo contiene eventos realizados.

### Qué sigue sin demostrarse

Esta definición solo da significado a «cerrado». No demuestra las hipótesis K del teorema.

En particular queda abierto:

**K1 / cofinalidad:**

$$
\forall X\in\mathfrak D_i^{A}
\;\exists Y\in\mathfrak K_i:
X\preceq_{\mathrm{ont}}Y.
$$

Es decir: ¿todo fragmento actual admite alguna extensión ontológica que no omita ningún resultado emergente actual relevante?

**K2 / inductividad:** toda cadena de dominios E-closed debe admitir una cota E-closed. Esta carga conecta directamente con REV-09/REV-10.

**K3 / amalgamación:** sigue siendo REV-07 y no se deriva de $\operatorname{EClosed}$.

### Totalización semántica evitada, cuantificación no resuelta

El predicado anterior no requiere que todos los eventos formen un **objeto ontológico colector**. Puede leerse metalingüísticamente como cuantificación sobre cualquier evento actual pertinente.

Pero esto no resuelve por sí solo el debate de generalidad absoluta: si ni siquiera esa cuantificación global fuese legítima, la definición tendría que relativizarse a familias locales.

### Estado de REV-18

REV-18 permanece **PARTIAL**.

Se ha reducido el puente a una relación de incidencia y un predicado $\operatorname{EClosed}$, eliminando la necesidad del embedding fuerte $J_i$.

Para cerrarlo todavía hay que justificar ontológicamente la relación $\trianglelefteq_i$ y demostrar que $\operatorname{EClosed}$ es la noción de cierre adecuada para el tipo de dominio elegido.

---

## 3.5. REV-19 — desajuste sincrónico/diacrónico

La emergencia de REV-03 es explícitamente diacrónica:

$$
s_0\xrightarrow{+}_{M,\mathrm{act}}s_1.
$$

Por tanto, $\operatorname{EClosed}(X)$ exige que un dominio que contiene el origen de un evento contenga también su resultado posterior.

Eso es natural si $X$ es un **fragmento de proceso o historia**.

Pero el teorema anterior se presentó históricamente sobre dominios sincrónicos:

$$
R_i^{A}(t).
$$

Una instantánea en $t$ no tiene por qué contener un estado que solo se actualiza en $t'>t$.

Por tanto:

$$
\boxed{
\text{cierre bajo eventos actualizados}
\not\equiv
\text{cierre sincrónico}.
}
$$

Hay dos rutas legítimas y todavía no se elige entre ellas:

1. **Ruta procesual:** reinterpretar $\mathfrak D_i$ como dominios/procesos diacrónicos y aplicar $\operatorname{EClosed}$ literalmente.
2. **Ruta sincrónica:** conservar $\mathfrak D_i^{A}(t)$ y definir una noción diferente de cierre estructural/constitutivo que no obligue a incluir futuros resultados actualizados.

Elegir una ruta no es una cuestión de notación: cambia el objeto del teorema.

### Estado de REV-19

**OPEN.** Debe fijarse el tipo temporal del dominio antes de afirmar que la emergencia independiente alimenta la prueba de totalidad.

---
## 4. Núcleo matemático normalizado — qué necesita realmente Zorn

Las secciones anteriores producen dos niveles distintos que no deben confundirse:

1. **nivel system-relative:** para un sistema fijo $M$, la emergencia independiente $\mathcal E_M$ induce un operador concreto $F_M$ sobre $\mathcal P(\Sigma_M)$, y F1–F3 se derivan;
2. **nivel ontológico:** el teorema pretende hablar de dominios $(\mathfrak D,\preceq_{\mathrm{ont}})$, tipo para el que todavía falta REV-18.

La forma operator-free del argumento permite ver exactamente qué parte de la estructura de $F$ es necesaria.

### 4.1. Forma operator-free

Sea:

$$
(\mathfrak D,\preceq)
$$

un poset **set-sized** no vacío y sea:

$$
\mathfrak K\subseteq\mathfrak D
$$

una familia de dominios que llamaremos **cerrados**.

Supongamos:

**K1 — cofinalidad**

$$
\forall X\in\mathfrak D\;
\exists Y\in\mathfrak K:
X\preceq Y.
$$

**K2 — inductividad de los cerrados**

Para toda cadena $\mathcal C\subseteq\mathfrak K$ existe $U\in\mathfrak K$ tal que:

$$
\forall X\in\mathcal C,\quad X\preceq U.
$$

**K3 — directedness/amalgamación**

$$
\forall X,Y\in\mathfrak D\;
\exists Z\in\mathfrak D:
X\preceq Z
\land
Y\preceq Z.
$$

### 4.2. Teorema de máximo cerrado cofinal

**Teorema.** Bajo K1–K3 existe:

$$
R\in\mathfrak K
$$

tal que:

$$
\boxed{
\forall X\in\mathfrak D,\quad X\preceq R.
}
$$

**Demostración.**

K1 y la no-vacuidad de $\mathfrak D$ implican $\mathfrak K\neq\varnothing$.

Por K2, toda cadena en $\mathfrak K$ tiene una cota superior en $\mathfrak K$. Por Zorn existe un $R\in\mathfrak K$ maximal.

Sea $X\in\mathfrak D$. Por K3 existe $Y\in\mathfrak D$ con:

$$
R\preceq Y
\land
X\preceq Y.
$$

Por K1 existe $Z\in\mathfrak K$ con:

$$
Y\preceq Z.
$$

Luego $R\preceq Z$. Como ambos pertenecen a $\mathfrak K$ y $R$ es maximal:

$$
Z=R.
$$

Por tanto:

$$
X\preceq Y\preceq R.
$$

Como $X$ era arbitrario, $R$ es un **máximo de todo $\mathfrak D$**, no solo un maximal de $\mathfrak K$. $\square$

### 4.3. Cobertura de lo real

Si además:

$$
\operatorname{Real}(x)
\Rightarrow
\exists X\in\mathfrak D:
x\preceq X,
$$

entonces:

$$
\operatorname{Real}(x)
\Rightarrow
x\preceq R.
$$

La inferencia es simplemente:

$$
x\preceq X\preceq R.
$$

### 4.4. Cómo se recupera esta forma desde un operador

Sea ahora:

$$
F:\mathfrak D\to\mathfrak D
$$

con solo:

$$
\text{F1: }X\preceq F(X),
$$

y:

$$
\text{F3: }F(F(X))=F(X).
$$

Definamos:

$$
\mathfrak K:=\operatorname{Fix}(F).
$$

Entonces F1 + F3 implican automáticamente K1:

para cualquier $X\in\mathfrak D$,

$$
X\preceq F(X)
$$

y:

$$
F(F(X))=F(X),
$$

por lo que:

$$
F(X)\in\mathfrak K.
$$

Además, si una cadena $\mathcal C\subseteq\operatorname{Fix}(F)$ tiene una cota $U\in\mathfrak D$, F1 da:

$$
U\preceq F(U).
$$

Así, para cada $X\in\mathcal C$:

$$
X\preceq U\preceq F(U).
$$

Y F3 da:

$$
F(U)\in\operatorname{Fix}(F).
$$

Por tanto la cota fija se obtiene con:

$$
\boxed{F1+F3,}
$$

sin usar F2.

Esta es la corrección exacta al argumento archivado: **la monotonía F2 era redundante para la ruta de Zorn**.

### 4.5. Papel de $F_M$

El operador system-relative construido en REV-01:

$$
F_M:\mathcal P(\Sigma_M)\to\mathcal P(\Sigma_M)
$$

sigue siendo útil y no queda superseded.

Para $F_M$:

- F1 se deriva por reflexividad;
- F2 interna se deriva por inclusión de conjuntos bajo un mismo sistema $M$;
- F3 se deriva por transitividad del cierre emergente.

El contraejemplo del inhibidor de REV-02 compara:

$$
F_M
\quad\text{con}\quad
F_N,
$$

no dos entradas del mismo operador. Por tanto no refuta la monotonía interna de $F_M$.

La extensión conductualmente conservativa de REV-02 sigue siendo útil para saber cuándo un evento puede transportarse entre sistemas, pero:

$$
\boxed{
\hookrightarrow_{\mathrm{cons}}
\text{ no es el orden ontológico } \preceq_{\mathrm{ont}}.
}
$$

Una incorporación real puede cambiar capacidades previas sin dejar de ser ontológicamente real.

### 4.6. Qué queda demostrado y qué no

**Demostrado matemáticamente:**

1. F2 no es necesaria para el teorema abstracto de maximalidad/exhaustividad;
2. F1 + F3 convierten cotas arbitrarias de cadenas de puntos fijos en cotas fijas;
3. la forma operator-free K1–K3 basta para obtener un máximo de $\mathfrak D$;
4. el $F_M$ concreto de REV-01 satisface F1–F3 dentro de su propio tipo.

**No demostrado ontológicamente:**

1. que un dominio ontológico $X\in\mathfrak D$ sea representable por un subconjunto de $\Sigma_M$;
2. que $\subseteq$ represente $\preceq_{\mathrm{ont}}$;
3. que la noción de cierre inducida por $F_M$ produzca una familia $\mathfrak K$ ontológicamente cofinal;
4. que las cadenas ontológicas relevantes tengan las cotas requeridas;
5. que K3/directedness sea legítima independientemente de “mismo índice”.

Estas cargas se concentran ahora en REV-18, REV-09/REV-10 y REV-07.

### 4.7. Relación con teoría estándar de puntos fijos

El teorema clásico de Tarski afirma que los puntos fijos de una función monótona sobre un retículo completo forman un retículo completo. Los closure operators estándar son extensivos, monótonos e idempotentes.

Nuestra observación es más modesta: **para esta ruta concreta de Zorn, una vez que existe un operador extensivo e idempotente y las cadenas de puntos fijos tienen cotas en el poset ambiente, la monotonía no es necesaria para levantar esas cotas a puntos fijos**.

La versión operator-free de K1–K3 hace transparente esa dependencia.

### 4.8. Estado normativo

- **REV-01:** RESOLVED en su ataque original. F1–F3 se derivan para $F_M$, y F2 resulta además redundante para el teorema abstracto.
- **REV-02:** RESOLVED en el sentido tipado correcto: la inhibición muestra no-monotonía entre sistemas/operadores, no dentro de un único $F_M$.
- **REV-04:** RESOLVED mediante el punto fijo propio explícito del toy.
- **REV-18:** OPEN y ahora es el blocker principal del enlace entre la teoría de emergencia y la ontología global.

---

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
