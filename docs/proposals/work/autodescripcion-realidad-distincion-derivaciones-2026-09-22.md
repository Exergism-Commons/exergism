# Derivaciones técnicas — autodescripción, realidad y distinción

**Estado:** documento de trabajo técnico, no normativo.
**Origen:** contenido extraído de las antiguas secciones 3.1–3.7 del documento principal el 2026-09-22.

Este archivo conserva pruebas, contraejemplos, toys y derivaciones detalladas. El estado vigente de la propuesta está en `autodescripcion-realidad-distincion.md`; si hay conflicto, prevalece el documento principal y el ledger.

Las formulaciones superadas se conservan solo cuando ayudan a reconstruir la historia del razonamiento y deben llevar una marca `SUPERSEDED` visible.

---

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

> **SUPERSEDED — diagnóstico de revisión externa posteriormente corregido.**
> Este pasaje se conserva únicamente como historia del razonamiento. La afirmación de que F2 era necesaria para elevar una cota de cadena es falsa: de $X\preceq U$ y F1, $U\preceq F(U)$, se obtiene por transitividad $X\preceq F(U)$ sin usar F2. La corrección se formaliza después en §3.3 y en el teorema normalizado del documento principal.

### [SUPERSEDED] Diagnóstico histórico sobre F2

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

> **Fin del pasaje SUPERSEDED. No usar como estado vigente.**

### Estado de REV-03

REV-03 permanece **PARTIAL** respecto de la suficiencia doctrinal general de la noción mínima. **Reutilización posterior:** §§0.11.69j–0.11.69o conectan esta misma definición event-local con TR-M/IA0 mediante EpsilonAlignment y la ruta restringida \(\varepsilon\)RSP; no se redefine la emergencia para conseguir ese resultado.

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

Esquemáticamente, y manteniendo separado el nivel semántico del ontológico:

$$
\boxed{
C0+F1+F3+C1_{\operatorname{Fix}}+C2+\operatorname{Max}
\Rightarrow
\exists S_i[
F(S_i)=S_i
\land
\operatorname{SemExhaustive}_i(S_i)
].
}
$$

Aquí $\operatorname{SemExhaustive}_i$ expresa exhaustividad dentro del tipo formal cubierto por $\mathfrak D_i$; no implica por sí sola la existencia de un $R_i$ ontológicamente total presentado por ese máximo. Justificar esa relación de presentación requiere REV-24/$\mathrm{OTB}_i$.

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

### Estado histórico de REV-18

**HISTORICAL — SUPERSEDED STATUS.** En este punto REV-18 permanecía PARTIAL. La formulación normativa posterior lo cierra en tipado mediante fragmentos semánticos positivos actuales (X=(T_X,\Phi_X)), incidencia como pertenencia al carrier y `EClosed_i` como propiedad del contenido. Conservar lo que sigue como deuda histórica que condujo a esa solución, no como status vigente.

Se ha reducido el puente a una relación de incidencia y un predicado $\operatorname{EClosed}$, eliminando la necesidad del embedding fuerte $J_i$.

Para cerrarlo todavía hay que justificar ontológicamente la relación $\trianglelefteq_i$ y demostrar que $\operatorname{EClosed}$ es la noción de cierre adecuada para el tipo de dominio elegido.

---

## 3.5. REV-19 — tipado temporal: el teorema emergentista debe ser procesual

La emergencia de REV-03 es explícitamente diacrónica:

$$
s_0\xrightarrow{+}_{M,\mathrm{act}}s_1.
$$

Por tanto, $\operatorname{EClosed}(X)$ exige que un dominio capaz de representar el origen de un evento pueda representar también su resultado.

Eso no está bien tipado si $X$ significa exclusivamente una instantánea:

$$
S_i^{A}(t),
$$

porque un estado que se actualiza en $t'>t$ no pertenece, en general, al contenido sincrónico de $t$.

Así:

$$
\boxed{
\text{cierre bajo eventos actualizados}
\not\equiv
\text{cierre sincrónico}.
}
$$

### 3.5.1. Decisión de arquitectura

Si la emergencia ha de hacer trabajo formal en la prueba, el target primario se redefine provisionalmente como un **dominio procesual actual**:

$$
X\in\mathfrak D_i^{\mathrm{proc}},
$$

no como una instantánea aislada.

Esto no implica:

- eternalismo;
- existencia actual de todos los futuros;
- un tiempo discreto;
- linealidad temporal;
- Many-Worlds;
- un conjunto ontológico de “todos los tiempos”.

Solo exige que un dominio pueda representar una porción de realidad extendida a través de ocurrencias relacionadas.

La literatura de process philosophy trata precisamente la dinámica, el cambio y la ocurrencia como categorías ontológicas centrales; las event structures de Winskel proporcionan un antecedente formal útil para representar procesos mediante ocurrencias y dependencias causales sin imponer un orden temporal total.

### 3.5.2. Fragmento procesual mínimo

Como tipo formal candidato, un fragmento procesual puede representarse por:

$$
H=
(S_H,E_H,\operatorname{src}_H,\operatorname{tgt}_H,\prec_H),
$$

donde:

- $S_H$ contiene tokens de configuraciones/estados efectivamente actualizados;
- $E_H$ contiene tokens de eventos efectivamente actualizados;
- $\operatorname{src}_H,\operatorname{tgt}_H:E_H\to S_H$ asignan origen y resultado;
- $\prec_H$ es una relación acíclica de precedencia/dependencia entre eventos.

No se exige que $\prec_H$ sea total. Por tanto se permiten concurrencia y branching.

Para todo $e\in E_H$:

$$
\operatorname{src}_H(e)\in S_H
$$

y:

$$
\operatorname{tgt}_H(e)\in S_H.
$$

Un evento emergente es un subtipo distinguido de evento actual, no el único tipo de transición que puede contener $H$.

### 3.5.3. Incidencia ontológica procesual

La relación de REV-18:

$$
s\trianglelefteq_i X
$$

se generaliza a estados y eventos:

$$
s\trianglelefteq_i X,
\qquad
e\trianglelefteq_i X.
$$

Su lectura sigue siendo ontológica, no conjuntista:

> el token de estado/evento está representado en el contenido del dominio procesual $X$.

Monotonicidad de incidencia:

$$
q\trianglelefteq_i X
\land
X\preceq_{\mathrm{proc}}Y
\Rightarrow
q\trianglelefteq_i Y,
$$

donde $q$ puede ser un estado o un evento.

### 3.5.4. Cierre emergente procesual

Sea $e$ un evento emergente actual con:

$$
\operatorname{src}(e)=s_0,
\qquad
\operatorname{tgt}(e)=s_1.
$$

Definimos:

$$
\boxed{
\operatorname{EClosed}^{\mathrm{proc}}_i(X)
}
$$

si, para todo evento emergente actual $e$ del régimen:

$$
s_0\trianglelefteq_i X
\Rightarrow
e\trianglelefteq_i X
\land
s_1\trianglelefteq_i X.
$$

Así el cierre ya no exige meter un futuro en una instantánea: exige completar un **fragmento de proceso** respecto de los eventos emergentes que parten de contenido ya representado.

La familia candidata del teorema pasa a ser:

$$
\mathfrak K_i^{\mathrm{proc}}
:=
\{
X\in\mathfrak D_i^{\mathrm{proc}}
\mid
\operatorname{EClosed}^{\mathrm{proc}}_i(X)
\}.
$$

### 3.5.5. Orden procesual

El orden:

$$
X\preceq_{\mathrm{proc}}Y
$$

debe significar que $Y$ conserva el contenido procesual actual representado por $X$ y añade contenido ontológico.

Todavía no se fija si la implementación formal será:

- inclusión literal de tokens identificados;
- subestructura;
- embedding preservador de fuentes, destinos y precedencia;
- clases de isomorfismo de alguna de las anteriores.

Elegirlo prematuramente podría volver a esconder el problema de REV-18. Lo único exigido ahora es que sea un orden ontológico, no una equivalencia conductual como $\hookrightarrow_{\mathrm{cons}}$.

### 3.5.6. Separación del teorema sincrónico

Quedan dos preguntas distintas:

**Teorema emergentista procesual**

$$
\text{¿existe un máximo semántico }S_i^{\mathrm{proc}}
\text{ entre los dominios procesuales actuales?}
$$

Aquí $\mathcal E_M$ y $\operatorname{EClosed}^{\mathrm{proc}}$ sí son pertinentes. Obtener un alcance ontológico $R_i$ presentado por $S_i^{\mathrm{proc}}$ requeriría REV-24/$\mathrm{OTB}_i$; los dos objetos no se identifican.

**Teorema sincrónico**

$$
\text{¿existe un dominio semánticamente exhaustivo }S_i^{A}(t)
\text{ para una sección actual dada?}
$$

Este segundo problema no se deriva automáticamente de la emergencia diacrónica. Necesitaría una noción sincrónica independiente de cobertura/cierre o una operación de sección sobre un proceso ya construido.

Por tanto:

$$
\boxed{
T_{\mathrm{proc}}
\neq
T_{\mathrm{syn}}.
}
$$

La propuesta deja de intentar que una sola prueba haga ambos trabajos.

### 3.5.7. Qué no se presupone

La formulación procesual no presupone una totalidad histórica acabada.

Un dominio puede ser un fragmento abierto:

$$
H_0\preceq_{\mathrm{proc}}H_1\preceq_{\mathrm{proc}}\cdots
$$

y la cuestión de si cadenas así poseen una cota sigue siendo exactamente la obligación de REV-09/REV-10.

Tampoco se presupone una estructura global de todos los eventos. La cuantificación sobre “todo evento emergente actual pertinente” puede mantenerse metalingüística mientras REV-11/generalidad siga abierta.

### 3.5.8. Estado histórico de REV-19

**HISTORICAL — SUPERSEDED STATUS.** Aquí REV-19 pasó de OPEN a PARTIAL. La arquitectura procesual posterior cerró el problema de tipado/orden: el status vigente es RESOLVED en ese alcance. Las obligaciones ontológicas que sobrevivieron fueron reasignadas a REV-18/20/09/07 en vez de mantener REV-19 artificialmente abierto.

Se ha resuelto el error de tipos más inmediato:

$$
\boxed{
\text{la clausura emergentista se aplica a procesos, no a snapshots.}
}
$$

No se marca RESOLVED porque todavía falta:

1. fijar rigurosamente el orden $\preceq_{\mathrm{proc}}$;
2. demostrar que la incidencia de REV-18 tiene interpretación ontológica independiente;
3. demostrar K1/K2 para $\mathfrak K_i^{\mathrm{proc}}$;
4. establecer, si se desea, cómo se recuperan dominios sincrónicos $S_i^{A}(t)$ desde un dominio procesual sin asumir una teoría temporal concreta.

---

## 3.6. REV-20 — qué significa realmente la cofinalidad K1

La forma operator-free del teorema exige:

$$
\text{K1:}\qquad
\forall X\in\mathfrak D\;
\exists Y\in\mathfrak K:
X\preceq Y.
$$

K1 no es una consecuencia lógica de llamar “cerrados” a los elementos de $\mathfrak K$.

### 3.6.1. K1 y operadores extensivos-idempotentes

Sea $(\mathfrak D,\preceq)$ un poset set-sized y $\mathfrak K\subseteq\mathfrak D$.

**Proposición.**

Si existe:

$$
F:\mathfrak D\to\mathfrak D
$$

tal que:

$$
X\preceq F(X),
$$

$$
F(F(X))=F(X),
$$

y:

$$
\operatorname{Fix}(F)=\mathfrak K,
$$

entonces K1 se cumple.

**Prueba.** Para todo $X$:

$$
X\preceq F(X),
$$

y por idempotencia:

$$
F(X)\in\operatorname{Fix}(F)=\mathfrak K.
$$

Luego $F(X)$ es una extensión cerrada de $X$. $\square$

La conversa también vale bajo una elección de extensiones cerradas.

Si K1 se cumple, para cada $X\in\mathfrak D$ sea:

$$
U_X=
\{
Y\in\mathfrak K
\mid
X\preceq Y
\}.
$$

K1 asegura:

$$
U_X\neq\varnothing.
$$

Elegimos:

$$
F(X)\in U_X,
$$

imponiendo además:

$$
X\in\mathfrak K
\Rightarrow
F(X)=X.
$$

Entonces:

$$
X\preceq F(X),
$$

y como $F(X)\in\mathfrak K$:

$$
F(F(X))=F(X).
$$

Además:

$$
\operatorname{Fix}(F)=\mathfrak K.
$$

Por tanto, bajo la elección requerida:

$$
\boxed{
\text{K1}
\Longleftrightarrow
\text{existencia de un selector extensivo e idempotente sobre }\mathfrak K.
}
$$

No se obtiene monotonía:

$$
X\preceq Y
\not\Rightarrow
F(X)\preceq F(Y).
$$

Así, K1 representa exactamente la **existencia de alguna extensión cerrada**, no un closure operator estándar.

### 3.6.2. K1 es independiente de K2 y K3

Consideremos:

$$
\mathfrak D=\{0,1\},
\qquad
0\prec 1,
$$

y:

$$
\mathfrak K=\{0\}.
$$

K3 se cumple porque $\mathfrak D$ es dirigido: $1$ es cota común de cualquier par.

K2 también se cumple: toda cadena contenida en $\mathfrak K$ tiene como cota cerrada a $0$.

Pero K1 falla para $1$:

$$
\nexists Y\in\mathfrak K:
1\preceq Y.
$$

Luego:

$$
\boxed{
K2+K3
\not\Rightarrow
K1.
}
$$

La cofinalidad es una carga independiente.

### 3.6.3. Dónde sí se satisface formalmente

En el toy system-relative:

$$
\mathfrak D_{\mathrm{toy}}
=
\mathcal P(\Sigma_M),
$$

y:

$$
\mathfrak K_{\mathrm{toy}}
=
\operatorname{Fix}(F_M).
$$

Como $F_M$ satisface F1 y F3:

$$
X\subseteq F_M(X)
$$

y:

$$
F_M(F_M(X))=F_M(X),
$$

K1 sí se satisface formalmente:

$$
\forall X\subseteq\Sigma_M,\;
\exists Y\in\mathfrak K_{\mathrm{toy}}:
X\subseteq Y.
$$

Podemos tomar simplemente:

$$
Y=F_M(X).
$$

Esto demuestra que REV-20 **no es un problema del formalismo system-relative**.

Es un problema del salto ontológico:

> ¿por qué todo dominio procesual ontológico actual debería admitir una extensión ontológica E-closed?

### 3.6.4. Relación con REV-18

Si REV-18 consiguiera construir sobre $\mathfrak D_i^{\mathrm{proc}}$ un operador:

$$
F_i^{\mathrm{proc}}
$$

que preservase las dos propiedades mínimas:

$$
X\preceq_{\mathrm{proc}}F_i^{\mathrm{proc}}(X)
$$

y:

$$
F_i^{\mathrm{proc}}(F_i^{\mathrm{proc}}(X))
=
F_i^{\mathrm{proc}}(X),
$$

entonces K1 quedaría derivada inmediatamente.

Pero la formulación austera por incidencia de REV-18 todavía solo define:

$$
\operatorname{EClosed}^{\mathrm{proc}}_i(X).
$$

De un predicado de cierre no se sigue que exista un dominio cerrado por encima de cada $X$.

Por tanto REV-20 permanece independiente mientras no se construya esa extensión o se demuestre su existencia por otra vía.

### 3.6.5. Estado de REV-20

**OPEN.**

Se ha demostrado:

- qué contenido matemático exacto tiene K1;
- que es independiente de K2/K3;
- que equivale, bajo elección, a disponer de un selector extensivo-idempotente hacia los dominios cerrados;
- que el toy formal sí satisface K1.

No se ha demostrado la afirmación ontológica requerida:

$$
\forall X\in\mathfrak D_i^{\mathrm{proc}}\;
\exists Y\in\mathfrak K_i^{\mathrm{proc}}:
X\preceq_{\mathrm{proc}}Y.
$$

---

## 3.7. REV-09/REV-10 — preservación de EClosed bajo cadenas procesuales

La carga K2 dice que una cadena de dominios cerrados debe tener una cota que siga siendo cerrada.

La formulación procesual permite separar dos cuestiones:

1. si el **predicado de cierre** se preserva al tomar el límite/unión de una cadena;
2. si ese límite formal corresponde a un **dominio ontológico admisible**.

### 3.7.1. Lema de preservación por unión

Consideremos una cadena de fragmentos procesuales compatibles:

$$
H_0\preceq_{\mathrm{proc}}
H_1\preceq_{\mathrm{proc}}
H_2\preceq_{\mathrm{proc}}
\cdots
$$

y, para el lema formal, elijamos representantes coherentes donde la extensión se realiza por subestructura/inclusión.

Sea:

$$
H_\infty
:=
\bigcup_{\alpha}H_\alpha
$$

componente a componente:

$$
S_\infty
=
\bigcup_\alpha S_\alpha,
$$

$$
E_\infty
=
\bigcup_\alpha E_\alpha,
$$

con fuentes, destinos y precedencia heredados de la cadena compatible.

Supongamos:

$$
\forall\alpha,\quad
\operatorname{EClosed}^{\mathrm{proc}}_i(H_\alpha).
$$

Entonces:

$$
\boxed{
\operatorname{EClosed}^{\mathrm{proc}}_i(H_\infty).
}
$$

**Demostración.**

Sea $e$ un evento emergente actual con:

$$
\operatorname{src}(e)=s_0
$$

y supongamos:

$$
s_0\trianglelefteq_i H_\infty.
$$

Como $H_\infty$ es la unión de la cadena, existe algún $\alpha$ tal que:

$$
s_0\trianglelefteq_i H_\alpha.
$$

Como $H_\alpha$ es E-closed:

$$
e\trianglelefteq_i H_\alpha
$$

y:

$$
\operatorname{tgt}(e)\trianglelefteq_i H_\alpha.
$$

Por inclusión:

$$
e\trianglelefteq_i H_\infty
$$

y:

$$
\operatorname{tgt}(e)\trianglelefteq_i H_\infty.
$$

Luego $H_\infty$ es E-closed. $\square$

### 3.7.2. Qué demuestra este lema

La clausura emergente actual es **local respecto del origen del evento**.

Por eso no necesitamos, para esta inferencia, el antiguo argumento:

> si el límite falla, debe existir un testigo finito que factorice por algún estadio.

El propio token de origen ya aparece en algún estadio de la cadena.

Esto elimina el uso de la inferencia oculta criticada en REV-10 **para esta ruta concreta**.

### 3.7.3. Qué no demuestra

El lema no prueba que:

$$
H_\infty\in\mathfrak D_i^{\mathrm{proc}}.
$$

Es decir, una unión formal de estructuras compatibles no se convierte automáticamente en un dominio ontológico actual/admisible.

La obligación ontológica restante es:

$$
\boxed{
\operatorname{ChainAdmissible}_i:
\quad
\{H_\alpha\}_\alpha
\subseteq
\mathfrak D_i^{\mathrm{proc}}
\Rightarrow
\bigcup_\alpha H_\alpha
\in
\mathfrak D_i^{\mathrm{proc}}
}
$$

para las cadenas pertinentes, o una condición más débil que garantice alguna cota procesual admisible equivalente.

Así, K2 se descompone en:

$$
\boxed{
\text{preservación formal de EClosed}
+
\text{admisibilidad ontológica de la cota}.
}
$$

La primera parte está demostrada; la segunda no.

### 3.7.4. Embeddings en lugar de inclusión

Si $\preceq_{\mathrm{proc}}$ se formaliza mediante embeddings en lugar de inclusiones literales, la unión anterior debe sustituirse por una construcción de límite/direct limit compatible.

No se introduce todavía maquinaria categórica adicional. El contenido esencial que tendría que preservarse es el mismo:

> todo token/evento presente en un estadio debe conservar una imagen coherente en la cota.

La existencia ontológica de esa cota sigue siendo la cuestión sustantiva.

### 3.7.5. Consecuencia para REV-10

REV-10 criticaba que la antigua ruta H8 usaba sin declarar una hipótesis de presentabilidad/factorización para hacer bajar un testigo del límite a algún estadio.

La ruta procesual actual ya no utiliza esa inferencia.

Por tanto:

**REV-10 queda RESOLVED respecto del teorema vigente** eliminando la derivación que requería StageFactorization.

Esto no afirma que toda noción futura de emergencia sea finitaria. Si se introdujeran eventos con condiciones de habilitación esencialmente infinitarias que no pudieran empaquetarse en un estado/origen representado, habría que reabrir una obligación de compactitud apropiada.

### 3.7.6. Estado histórico de REV-09

**HISTORICAL — SUPERSEDED STATUS.** Aquí REV-09 pasó de OPEN a PARTIAL. Posteriormente, con `Adm_i := StructAdm_i`, las uniones de cadenas set-indexed preservan admisibilidad y `EClosed`; el status vigente es RESOLVED para el alcance set-indexed. La cuestión class-sized/smallness quedó trasladada a REV-22/23/25.

Se ha demostrado que EClosed se preserva formalmente bajo uniones de cadenas compatibles.

Falta demostrar la parte ontológica:

$$
\text{la cota formal es un dominio procesual admisible/actual}.
$$

Esa es ahora la forma precisa de K2.

---

---

## REV-07 — origen unificado, generación hiperaridad y reconstrucción

**CURRENT TARGET.** Para un parámetro de contexto fijo $i$, la realidad no se individua por conectividad semántica sino por una configuración-originaria unificada y su least generative closure.

### 0.1. Configuración-originaria

El símbolo:

$$
\mathcal O_i
$$

denota una configuración-token ontológicamente instanciada dentro del contexto $i$, no una colección que el metalenguaje pueda formar libremente.

Sea:

$$
B_i(\mathcal O_i)
:=
\operatorname{Seed}_i(\mathcal O_i)
$$

su contenido inicial.

La unidad no se define a partir del candidato $\mathcal O_i$. Introducimos hechos de integración independientes:

$$
\operatorname{UnitFact}_i(f_i,U_i),
$$

donde $U_i$ es la familia de relata del hecho/proceso/constraint integrativo. UnitFact conserva UF1–UF5: instancia actual, contenido integrativo, independencia del contenedor y del target, e invariancia bajo recodificación fiel.

El predicado binario previo $\operatorname{OriginConstitutive}_i(f_i,U_i)$ queda **SUPERSEDED**: ser constitutivo no es una propiedad suficientemente informativa del hecho aislado, sino de cómo su dependencia cruza una separación concreta.

La dependencia constitutiva no queda como un primitivo opaco. Separamos dos relaciones independientes de la genealogía:

$$
\operatorname{IdDep}_i(x_i;f_i\mid Y_i)
$$

significa que la identidad ontológica relevante de $x_i$ incluye esencialmente la instancia $f_i$ con soporte en $Y_i$; y

$$
\operatorname{ConstExistDep}_i(x_i;f_i\mid Y_i)
$$

significa que la existencia actual de $x_i$, en sentido constitutivo y no meramente causal, requiere la instancia $f_i$ con soporte en $Y_i$.

Ambas relaciones deben justificarse mediante la semántica propia del modo ontológico concreto. No pueden mencionar $\mathcal O_i$, Seed, OriginUnity, $R_i$, CoReal, Generated$^*$, SameRegime, equivalencia de índice, CommonGround ni CGP. En particular, necesidad causal, dependencia contrafáctica dinámica o ser efecto de $f_i$ no bastan para ConstExistDep.

Definimos entonces:

$$
\boxed{
\operatorname{EssConDep}_i(x_i;f_i,U_i\mid Y_i)
:\Longleftrightarrow
\operatorname{UnitFact}_i(f_i,U_i)
\land
\bigl(
\operatorname{IdDep}_i(x_i;f_i\mid Y_i)
\lor
\operatorname{ConstExistDep}_i(x_i;f_i\mid Y_i)
\bigr).
}
$$

Así EssConDep no certifica nada por etiqueta: exige una dependencia de identidad o de existencia constitutiva independientemente justificada. Que $a_i,b_i$ sean inputs de un evento que produce $c_i$ puede hacer depender causalmente $c_i$ del evento, pero no produce IdDep/ConstExistDep hacia $a_i$ o $b_i$ y no los vuelve retroactivamente constituidos por la convergencia.

Definimos además el footprint semántico:

$$
U_i\cup\{f_i\}
\preceq
\operatorname{UnitFoot}_i(f_i,U_i),
$$

determinado por el hecho y su soporte ontológico necesario, no por el candidato.

Para pluralidades disjuntas no vacías $A_i,B_i$ definimos:

$$
\boxed{
\begin{aligned}
\operatorname{ConstitutiveBridge}_i(f_i,U_i;A_i,B_i)
:\Longleftrightarrow\;&
\operatorname{UnitFact}_i(f_i,U_i)\\
&\land\exists a_i[
a_i\preceq A_i\cap\operatorname{UnitFoot}_i(f_i,U_i)
\land
\operatorname{EssConDep}_i(a_i;f_i,U_i\mid B_i)
]\\
&\land\exists b_i[
b_i\preceq B_i\cap\operatorname{UnitFoot}_i(f_i,U_i)
\land
\operatorname{EssConDep}_i(b_i;f_i,U_i\mid A_i)
].
\end{aligned}
}
$$

La exigencia es deliberadamente bilateral. Si una base contiene $a_i$ y algo derivado unilateralmente de $a_i$, el contenido derivado debe pertenecer normalmente a la clausura generada, no inflar artificialmente el origen. En cambio, mutual grounding, constitución holística o soporte mutuo pueden satisfacer el puente cuando la ontología concreta justifique EssConDep en ambas direcciones.

OriginUnity queda entonces:

$$
\boxed{
\operatorname{OriginUnity}_i(\mathcal O_i)
:\Longleftrightarrow
\forall A_i,B_i[
\operatorname{Partition}_i(\operatorname{Seed}_i(\mathcal O_i);A_i,B_i)
\Rightarrow
\exists f_i,U_i[
\operatorname{ConstitutiveBridge}_i(f_i,U_i;A_i,B_i)
\land
\operatorname{UnitFoot}_i(f_i,U_i)\preceq\operatorname{Seed}_i(\mathcal O_i)
]
].
}
$$

Así la prueba de unidad no pregunta si el hecho «pertenece al origen»: pregunta, de forma local y anterior al candidato, si hay dependencia constitutiva esencial cruzada hacia ambos lados. La inclusión de UnitFoot solo verifica después que el testigo completo esté contenido en la configuración candidata.

### 0.2. Lema anti-agregación

Definimos la ausencia objetiva de puente constitutivo entre dos contenidos no vacíos:

$$
\mathrm{NoConstitutiveBridge}_i(A_i,B_i)
:\Longleftrightarrow
\neg\exists f_i,U_i[
\operatorname{ConstitutiveBridge}_i(f_i,U_i;A_i,B_i)
\land
\operatorname{UnitFoot}_i(f_i,U_i)\preceq A_i\cup B_i
].
$$

Para toda configuración candidata $\mathcal O_i$:

$$
\boxed{
\operatorname{Seed}_i(\mathcal O_i)=A_i\cup B_i
\land
\mathrm{NoConstitutiveBridge}_i(A_i,B_i)
\Rightarrow
\neg\operatorname{OriginUnity}_i(\mathcal O_i).
}
$$

La prueba es inmediata por la partición $A_i\mid B_i$. La unión metalingüística de dos raíces no crea EssConDep y una interacción posterior no la hace retroactiva.

#### 0.2.1. Modelos de control para REV-07a

**M1 — átomo fundamental.** Si $\operatorname{Seed}_i(\mathcal O_i)=\{a_i\}$, no existe partición no trivial. OriginUnity vale vacuamente; la carga restante recae en OriginConfig, RootClosed e Irredundant.

**M2 — soporte mutuo/ciclo fundamental.** Para $a_i,b_i$ y un hecho estructural $f_i$:

$$
\operatorname{EssConDep}_i(a_i;f_i,U_i\mid\{b_i\})
\land
\operatorname{EssConDep}_i(b_i;f_i,U_i\mid\{a_i\})
$$

produce un ConstitutiveBridge para la partición $\{a_i\}\mid\{b_i\}$. La bilateralidad admite cofundamentación sin exigir prioridad temporal.

**M3 — constitución holística.** Si la identidad/actualidad constitutiva de relata situados a ambos lados depende esencialmente de una misma estructura $f_i$, el puente puede satisfacer OriginUnity aunque ninguna dirección sea causal-temporal.

**M4 — suma independiente.** Si $A_i$ y $B_i$ son internamente completos pero no existe EssConDep cruzada, entonces NoConstitutiveBridge y la unión falla OriginUnity.

**M5 — convergencia tardía.** Supóngase:

$$
\operatorname{OntProd}_i(e_i,\{a_i,b_i\},c_i).
$$

Aunque $c_i$ dependa de $e_i$, de $a_i$ y de $b_i$, no se sigue:

$$
\operatorname{EssConDep}_i(a_i;e_i,\{a_i,b_i\}\mid\{b_i,c_i,e_i\})
$$

ni su análogo para $b_i$. Por tanto incluir retrospectivamente $e_i,c_i$ en el seed no proporciona un ConstitutiveBridge para una partición que aísle una de las ramas ancestrales. La convergencia sigue siendo JointRealizable, no co-origen.

**M6 — grounding unilateral.** Si $a_i$ fundamenta unilateralmente $b_i$, pero $a_i$ no depende constitutivamente de la estructura que fundamenta $b_i$, entonces $\{a_i,b_i\}$ no es una base cofundamental unificada. El comportamiento esperado es que $a_i$ pueda pertenecer al origen y $b_i$ aparezca en la clausura generada.

Estos modelos convierten REV-07a en un criterio refutable. La taxonomía MOD/RLC/HC/PC y el contrato ECD1–ECD7 fijan después qué formas de testigo son admisibles; la existencia de una instancia concreta no se presupone y pertenece a la obligación de testigo de OntOrigin/ExistsR.

#### 0.2.2. Contrato de admisibilidad de EssConDep

Una familia ontológica concreta solo puede instanciar $\operatorname{EssConDep}$ si satisface conjuntamente:

- **ECD1 / actuality:** existe una instancia actual del modo, no mera posibilidad, ley general o semejanza;
- **ECD2 / directed essentiality:** la semántica del modo implica dependencia de la actualidad/identidad constitutiva de $x_i$ respecto de la instancia $f_i$ y del soporte cruzado indicado por $Y_i$;
- **ECD3 / no input inversion:** ser input, causa, enabling condition o mero antecedente de $f_i$ no basta para concluir que el input depende de $f_i$;
- **ECD4 / locality:** la justificación usa solo la semántica del modo y sus tokens/relata/soporte, no una totalidad final ni el candidato;
- **ECD5 / target independence:** no menciona $R_i$, Generated$^*$, CoReal, SameRegime, equivalencia de índices, CommonGround ni CGP;
- **ECD6 / recoding invariance:** una recodificación fiel que preserve la estructura ontológica relevante preserva el juicio de dependencia;
- **ECD7 / auditability:** debe poder indicarse qué token de un lado depende constitutivamente de qué soporte cruzado y mediante qué modo ontológico.

Familias candidatas que **pueden** satisfacer el contrato si se justifican independientemente: mutual ontological dependence token-specific, identidad constitutiva relacional, estructuras holísticas en las que los relata dependen esencialmente del patrón total y co-constitución procesual genuina.

No satisfacen el contrato por sí solas: causalidad ordinaria, colisión/interacción, proximidad espacio-temporal, semejanza, obediencia a una misma ley, representación conjunta, compartir un descendiente ni pertenecer a la misma clausura candidata.

Por tanto REV-07a no se cerrará enumerando etiquetas metafísicas: cada modo admitido debe proporcionar una regla ECD1–ECD7 y pasar M1–M6.

#### 0.2.3. Taxonomía núcleo de modos EssConDep

Fijamos cuatro **esquemas de modo** actualmente admitidos: $\mathsf{MOD}_i$, $\mathsf{RLC}_i$, $\mathsf{HC}_i$ y $\mathsf{PC}_i$, sin convertirlos en objetos de un dominio ni afirmar que toda ontología concreta deba instanciarlos todos. Un juicio $\operatorname{EssConDep}_i$ solo puede derivarse de una instancia explícita de uno de estos esquemas —o de una futura extensión que satisfaga ECD1–ECD7 y M1–M6.

Los nombres de modo **no certifican** dependencia. Primero debe demostrarse IdDep o ConstExistDep; el esquema solo clasifica la forma del testigo.

**MOD — mutual ontological dependence / co-dependencia fundamental.**

Para un lado del puente:

$$
\mathsf{MOD}_i(f_i;x_i,Y_i)
\Rightarrow
\bigl(
\operatorname{IdDep}_i(x_i;f_i\mid Y_i)
\lor
\operatorname{ConstExistDep}_i(x_i;f_i\mid Y_i)
\bigr).
$$

Para un ConstitutiveBridge debe existir además un juicio MOD recíproco desde el otro lado respecto de la misma instancia integrativa. MOD permite soporte mutuo o dependencia ontológica cíclica si una teoría independiente los admite; no afirma que la relación estándar de grounding sea necesariamente cíclica.

**RLC — constitución relacional esencial.**

$$
\boxed{
\mathsf{RLC}_i(f_i;x_i,Y_i)
\Rightarrow
\operatorname{IdDep}_i(x_i;f_i\mid Y_i).
}
$$

RLC se reserva al caso en que $x_i$ no sería el mismo token o no instanciaría el mismo tipo ontológicamente relevante sin la relación actual $f_i$ con soporte en $Y_i$. Influencia causal o propiedades accidentales no bastan.

**HC — constitución holística/estructural.**

Sea $f_i$ una estructura actual con footprint $H_i$. Para $x_i\preceq H_i$:

$$
\mathsf{HC}_i(f_i;x_i,H_i\setminus\{x_i\})
\Rightarrow
\left[
\operatorname{IdDep}_i(x_i;f_i\mid H_i\setminus\{x_i\})
\lor
\operatorname{ConstExistDep}_i(x_i;f_i\mid H_i\setminus\{x_i\})
\right].
$$

HC exige que el patrón estructural sea constitutivo; pertenecer a una colección, estar correlacionado con el resto o formar parte de un agregado mereológico no lo demuestra.

**PC — co-constitución procesual.**

$$
\mathsf{PC}_i(f_i;x_i,Y_i)
\Rightarrow
\left[
\operatorname{IdDep}_i(x_i;f_i\mid Y_i)
\lor
\operatorname{ConstExistDep}_i(x_i;f_i\mid Y_i)
\right].
$$

PC se limita a estadios, roles, fases o participantes cuya identidad/existencia constitutiva depende del proceso actual $f_i$ y del soporte cruzado. Ser simplemente causa, input, output o participante contingente no satisface PC.

Por definición de EssConDep, cualquiera de estas derivaciones produce EssConDep **solo además de** un UnitFact actual con el mismo $f_i,U_i$. La auditabilidad ECD7 exige exponer: modo, instancia, dependiente, soporte cruzado y si la ruta concreta fue IdDep o ConstExistDep.

#### 0.2.4. Exclusiones y frontera con OntProd

La taxonomía de EssConDep es **más estrecha** que la futura taxonomía de OntProd: toda EssConDep debe ser relevante para la futura clasificación generativa, pero no toda producción/dependencia que entre en OntProd será constitutiva de una base cofundamental. No se introduce aquí un predicado intermedio nuevo.

Quedan excluidos de EssConDep salvo que una teoría adicional demuestre uno de los modos anteriores:

- causalidad eficiente ordinaria;
- producción temporal;
- enabling;
- input/output;
- interacción o colisión;
- dependencia contrafáctica meramente causal;
- parthood no esencial;
- co-localización;
- misma ley;
- misma clase/tipo;
- mismo descendiente;
- mismo proceso si la participación es contingente;
- misma clausura generativa;
- compatibilidad o JointRealizable.

Esto impide que REV-07b trivialice REV-07a: que una relación entre en OntProd no la convierte automáticamente en EssConDep.

#### 0.2.5. Matriz de pruebas de la taxonomía

| Modelo | MOD | RLC | HC | PC | Resultado esperado |
|---|---:|---:|---:|---:|---|
| M1 átomo fundamental | n/a | n/a | n/a | n/a | OriginUnity vacua |
| M2 soporte mutuo/ciclo | posible | posible | posible | posible | puede pasar |
| M3 constitución holística | no requerido | posible | sí | posible | puede pasar |
| M4 suma independiente | no | no | no | no | falla |
| M5 convergencia tardía | no por el mero evento | no | no | no por mera participación | falla |
| M6 grounding unilateral | unilateral solamente | posible unilateral | no bilateral | no | falla como base cofundamental |

La tabla no prueba que una instancia concreta satisfaga un modo; fija qué **tipo de justificación** tendría que aportar. En particular, M5 sigue fallando aunque $e_i$ y $c_i$ se añadan retrospectivamente al seed.

#### 0.2.6. Regla de extensión

Un nuevo esquema de modo $\mathsf X_i$ puede añadirse a la taxonomía únicamente si:

$$
\mathrm{ECD1{-}7}(\mathsf X_i)
\land
\mathrm{PassesM1{-}M6}(\mathsf X_i)
$$

y existe una regla local explícita:

$$
\mathsf X_i(f_i;x_i,Y_i)
\Rightarrow
\operatorname{EssConDep}_i(x_i;f_i,U_i\mid Y_i)
$$

que no use OntOrigin, Seed, OriginUnity, GeneTotal, $R_i$, CoReal, Generated$^*$, SameRegime, CommonGround, CGP ni equivalencia de índices.

Con esto REV-07a deja de tener una variable semántica completamente libre. Permanece pendiente decidir qué esquemas acepta finalmente la ontología y justificar cada uno en términos independientes; cualquier ampliación futura queda sujeta al mismo filtro anti-circular.

#### 0.2.7. Lema de independencia del candidato

Supóngase que UnitFact, IdDep, ConstExistDep y UnitFoot satisfacen las prohibiciones de ECD4–ECD7. Entonces, para pluralidades fijas $A_i,B_i$ y tokens fijos $f_i,U_i$, el valor de:

$$
\operatorname{ConstitutiveBridge}_i(f_i,U_i;A_i,B_i)
$$

no cambia al insertar esos mismos tokens en una configuración candidata distinta, porque su definición no contiene $\mathcal O_i$, Seed, OriginUnity, OntOrigin, GeneTotal, $R_i$, CoReal, Generated$^*$, CommonGround, CGP ni equivalencia de índices.

Por tanto:

$$
\boxed{
\operatorname{ConstitutiveBridge}_i
\text{ es candidate-independent.}
}
$$

OriginUnity sí consulta $\operatorname{Seed}_i(\mathcal O_i)$ para enumerar particiones y verificar que el footprint completo del testigo es interno, pero **no obtiene** la verdad del bridge de esa pertenencia.

#### 0.2.8. Lema de no-retroactividad de convergencia

Sea un evento integrador:

$$
\operatorname{OntProd}_i(e_i,A_i\cup B_i,c_i)
$$

y sea $D_i$ cualquier contenido añadido retrospectivamente junto con $e_i,c_i$. Si para algún lado, por ejemplo $A_i$, no existe token $a_i\preceq A_i$ tal que:

$$
\operatorname{IdDep}_i(a_i;e_i\mid B_i\cup D_i)
\lor
\operatorname{ConstExistDep}_i(a_i;e_i\mid B_i\cup D_i),
$$

entonces, para cualquier $U_i$:

$$
\boxed{
\neg\operatorname{ConstitutiveBridge}_i(
e_i,U_i;
A_i,
B_i\cup D_i
).
}
$$

**Demostración.** ConstitutiveBridge exige EssConDep hacia ambos lados. Por definición de EssConDep, el lado $A_i$ requeriría precisamente IdDep o ConstExistDep respecto de la instancia $e_i$ y del soporte cruzado. La negación anterior bloquea ese conjuncto. Añadir $e_i,c_i,D_i$ al seed no altera IdDep ni ConstExistDep por candidate-independence. $\square$

El lema es deliberadamente modesto: no prueba que nunca pueda existir un bridge distinto entre los linajes. Prueba exactamente lo necesario contra seed-stuffing: **el hecho de converger no se convierte a sí mismo en fundamento común**. Si existe otro bridge, debe venir acompañado por un testigo independiente.

#### 0.2.9. Cierre de REV-07a

REV-07a pedía evitar tres trivializaciones:

1. definir la unidad por pertenencia al candidato;
2. definirla por la realidad/clausura que se intenta obtener;
3. reciclar una convergencia posterior como unidad originaria.

La arquitectura actual bloquea las tres:

- Candidate Independence Lemma bloquea (1);
- ECD4–ECD7 + la definición de IdDep/ConstExistDep bloquean (2);
- No-Retroactivity Lemma bloquea (3).

Por ello REV-07a queda **RESOLVED como criterio de OriginUnity**. Esto **no demuestra** que exista una configuración concreta con suficientes ConstitutiveBridge. Tal existencia es una obligación de instancia de OriginCandidate/OntOrigin y, en última instancia, de ExistsR; no debe mantenerse artificialmente REV-07a abierto por no haber demostrado todavía ExistsR.

Los esquemas MOD/RLC/HC/PC son rutas admitidas para clasificar testigos, no axiomas de que tales testigos existan. Una ontología concreta puede usar un subconjunto, ninguno, o futuras extensiones que pasen ECD1–ECD7 y M1–M6.


### 0.3. Root-closure sin primera causa temporal

**Aclaración de tipo.** OntOrigin no significa comienzo temporal, espacial ni primera causa cronológica. OntProd es una relación objetivo de producción/dependencia ontológica cuyos modos concretos pueden ser causales, constitutivos, de grounding o de continuidad procesual. Por tanto:

$$
\text{no first temporal event}
\not\Rightarrow
\neg\operatorname{OntOrigin}_i.
$$

REV-07d solo muerde si la estructura carece de **toda base ontológica mínima admisible** bajo la dependencia relevante, no simplemente si presenta un regreso temporal infinito. Un fundamento puede ser atemporal, estructural, cíclico o de soporte mutuo sin ser un miembro cronológicamente anterior de la genealogía.

Definimos:

$$
\mathrm{RootClosed}_i(\mathcal O_i)
$$

mediante:

$$
b_i\in\operatorname{Seed}_i(\mathcal O_i)
\land
\operatorname{OntProd}_i(e_i,A_i,b_i)
\Rightarrow
\operatorname{GenFoot}_i(e_i,A_i,b_i)
\preceq
\operatorname{Seed}_i(\mathcal O_i).
$$

Definimos el footprint mínimo de una producción de modo que:

$$
A_i\cup\{e_i,b_i\}
\preceq
\operatorname{GenFoot}_i(e_i,A_i,b_i).
$$

Así RootClosed exige que no solo los antecedentes, sino también el propio evento productor y cualquier token ontológico estructural obligatorio, pertenezcan al seed.

Esto no exige que los constituyentes del origen sean incausados individualmente. Permite ciclos fundamentales, soporte mutuo o una configuración estacionaria siempre que no exista antecedente generativo externo al seed.

Ejemplo permitido:

$$
a_i\leadsto b_i,
\qquad
b_i\leadsto a_i,
\qquad
a_i,b_i\in\operatorname{Seed}_i(\mathcal O_i).
$$

Lo prohibido es:

$$
c_i\notin\operatorname{Seed}_i(\mathcal O_i)
\quad\text{y}\quad
c_i\leadsto a_i.
$$

### 0.4. Producción ontológica objetivo y GenEvent como implementación

Para no definir la genealogía por el propio inventario formal, OntProd se construye desde **modos objetivo independientes**. Todo modo admitido debe satisfacer:

- **OP1 / actuality:** existe una instancia token actual $e_i$;
- **OP2 / directed target:** la semántica propia del modo establece a $b_i$ como resultado, constituido, grounded o continuación ontológica respecto de $e_i,A_i$;
- **OP3 / support relevance:** ningún miembro de $A_i$ entra por mera co-presencia; cada antecedente forma parte del soporte productivo/constitutivo declarado por el modo;
- **OP4 / support completeness:** $A_i$ contiene todo antecedente conjuntamente requerido por esa instancia según la semántica del modo; soporte estructural adicional se registra en GenFoot;
- **OP5 / candidate independence:** el modo no menciona OriginCandidate, OntOrigin, Seed ni RootClosed;
- **OP6 / target independence:** no menciona $R_i$, Generated$^*$, CoReal, SameRegime, CommonGround, CGP ni equivalencia de índices;
- **OP7 / footprint auditability:** el evento, antecedentes, target y soporte ontológico obligatorio pueden auditarse en GenFoot;
- **OP8 / recoding invariance:** recodificaciones fieles preservan el juicio productivo.

Fijamos cuatro esquemas núcleo.

**CAU — producción causal.**

$$
\operatorname{CausalProd}_i(e_i,A_i,b_i)
$$

requiere una conexión causal productiva token-specific cuyo resultado es $b_i$ y cuyo soporte productivo relevante es $A_i$. Correlación, mera precedencia, background law o enabling no productivo no bastan.

**CON — constitución/realización.**

$$
\operatorname{ConstitutiveProd}_i(e_i,A_i,b_i)
$$

requiere que $b_i$ exista o sea el token/tipo ontológico relevante en virtud de una instancia constitutiva/realizadora $e_i$ soportada por $A_i$. Puede ser atemporal. Parthood no esencial o simple pertenencia a un agregado no bastan.

**GRD — grounding/dependencia ontológica dirigida.**

$$
\operatorname{GroundProd}_i(e_i,A_i,b_i)
$$

requiere una instancia independiente según la cual $b_i$ obtiene o depende ontológicamente de $A_i$ mediante $e_i$. No se presupone que grounding sea causal, temporal, bien fundado ni universalmente acíclico; esas propiedades pertenecen a la teoría concreta que suministre el testigo.

**PRC — continuidad/constitución procesual.**

$$
\operatorname{ProcessProd}_i(e_i,A_i,b_i)
$$

requiere que $b_i$ sea un estadio, estado o resultado cuya identidad/existencia procesual deriva de la instancia actual $e_i$ y del soporte $A_i$. Sucesión temporal, participación contingente o compartir proceso sin dependencia productiva no bastan.

$\operatorname{OntProd}_i(e_i,A_i,b_i)$ permanece como **relación objetivo independiente** sometida a OP1–OP8. Los cuatro modos son clasificadores suficientes, no su definición:

$$
\boxed{
\begin{aligned}
&\operatorname{CausalProd}_i(e_i,A_i,b_i)
\lor\operatorname{ConstitutiveProd}_i(e_i,A_i,b_i)\\
&\lor\operatorname{GroundProd}_i(e_i,A_i,b_i)
\lor\operatorname{ProcessProd}_i(e_i,A_i,b_i)
\Rightarrow
\operatorname{OntProd}_i(e_i,A_i,b_i).
\end{aligned}
}
$$

No existe un catch-all «generativo». La pregunta de si estos modos agotan OntProd se registra separadamente:

$$
\boxed{
\mathrm{ProdCoverage}_i:
\quad
\operatorname{OntProd}_i(e_i,A_i,b_i)
\Rightarrow
\begin{aligned}[t]
&\operatorname{CausalProd}_i(e_i,A_i,b_i)
\lor\operatorname{ConstitutiveProd}_i(e_i,A_i,b_i)\\
&\lor\operatorname{GroundProd}_i(e_i,A_i,b_i)
\lor\operatorname{ProcessProd}_i(e_i,A_i,b_i).
\end{aligned}
}
$$

ProdCoverage es una obligación metafísica real, no una definición. Una futura quinta familia puede ampliar la taxonomía si satisface OP1–OP8; en ese caso debe añadirse tanto al teorema de cobertura como a la implementación.

La implementación formal es:

$$
\boxed{
\operatorname{GenEvent}_i(e_i,A_i,b_i)
:\Longleftrightarrow
\operatorname{CausalProd}_i(e_i,A_i,b_i)
\lor
\operatorname{ConstitutiveProd}_i(e_i,A_i,b_i)
\lor
\operatorname{GroundProd}_i(e_i,A_i,b_i)
\lor
\operatorname{ProcessProd}_i(e_i,A_i,b_i).
}
$$

De la soundness individual de los cuatro modos se deriva GenSound. Además:

$$
\boxed{
\mathrm{ProdCoverage}_i
\Rightarrow
\mathrm{GenComplete}_i.
}
$$

Definimos:

$$
\boxed{
\mathrm{GenAdequate}_i
:\Longleftrightarrow
\mathrm{GenSound}_i\land\mathrm{GenComplete}_i.
}
$$

Bajo la taxonomía actual, ProdCoverage implica GenAdequate porque GenSound ya está derivado.

Por tanto REV-07b ya no puede cerrarse por estipulación: su carga pendiente principal es justificar ProdCoverage para la ontología/contexto al que se aplique ExistsR.

$A_i$ es soporte completo y relevante para la instancia, no una lista arbitraria de antecedentes. Puede haber más de un soporte admisible para un mismo target cuando la ontología concreta admita sobredeterminación o realizaciones alternativas; cada instancia se registra separadamente con su propio GenFoot.

#### 0.4.1. Contrato de GenFoot

Para toda instancia $\operatorname{OntProd}_i(e_i,A_i,b_i)$, el footprint debe satisfacer:

- **GF1 / core inclusion:** $A_i\cup\{e_i,b_i\}\preceq\operatorname{GenFoot}_i(e_i,A_i,b_i)$;
- **GF2 / required-support completeness:** todo token que la semántica independiente del modo declare constitutiva o productivamente necesario para esa instancia pertenece a GenFoot;
- **GF3 / relevance:** GenFoot no puede inflarse con tokens sin papel productivo/constitutivo en la instancia;
- **GF4 / candidate independence:** GenFoot no se define desde Seed, RootClosed, OntOrigin ni desde el carrier que se quiere cerrar;
- **GF5 / target independence:** no usa $R_i$, Generated$^*$, CoReal, SameRegime, CommonGround ni CGP;
- **GF6 / recoding invariance:** una recodificación fiel preserva el footprint hasta isomorfismo/imagen fiel.

GF2 y GF3 son importantes en direcciones opuestas: omitir soporte puede fabricar un falso RootClosed; añadir soporte irrelevante puede fabricar un falso antecedente externo y romper un origen legítimo.

#### 0.4.2. Modelos de control para REV-07b

**P1 — correlación sin producción.** Si $a_i$ y $b_i$ covarían pero no existe una instancia productiva/constitutiva/grounding/procesual dirigida, ninguno de CAU/CON/GRD/PRC vale; por tanto no hay GenEvent.

**P2 — enabling no productivo.** Si $z_i$ solo hace posible el evento pero no forma parte del soporte productivo declarado, no entra en $A_i$. Si la semántica concreta exige conservarlo como soporte estructural obligatorio, puede entrar en GenFoot por GF2 sin convertirse por ello en antecedente generativo.

**P3 — antecedente espectador.** Si:

$$
\operatorname{CausalProd}_i(e_i,\{a_i\},b_i)
$$

pero $z_i$ es irrelevante, entonces no es admisible reemplazar el soporte por $\{a_i,z_i\}$. OP3 prohíbe fabricar dependencias añadiendo espectadores.

**P4 — soporte omitido.** Si el modo exige conjuntamente $a_i$ y $z_i$ para la instancia, registrar solo $A_i=\{a_i\}$ viola OP4. Si $z_i$ es soporte estructural necesario pero no antecedente, omitirlo de GenFoot viola GF2.

**P5 — constitución atemporal.** Una instancia CON o GRD puede satisfacer OntProd sin prioridad temporal. Esto evita reducir genealogía a causalidad histórica.

**P6 — sucesión sin continuidad ontológica.** Que $a_i$ ocurra antes que $b_i$ dentro de un proceso no establece PRC. Debe demostrarse dependencia de identidad/existencia procesual o producción dirigida del estado/resultante.

**P7 — sobredeterminación/realizaciones alternativas.** Si dos soportes distintos $A_i$ y $A'_i$ producen legítimamente $b_i$, se registran como instancias productivas distintas o alternativas del mismo tipo; no se fuerza una unión artificial $A_i\cup A'_i$.

**P8 — hiperevento irreducible.** Si $\{a_i,b_i\}$ es conjuntamente requerido para $c_i$, la taxonomía conserva la hiperaridad. La proyección binaria GenStep no puede sustituir el soporte conjunto.

#### 0.4.3. Estado exacto de REV-07b

La arquitectura ya fija:

1. una relación objetivo OntProd independiente de GenEvent;
2. OP1–OP8 para sus modos admisibles;
3. CAU/CON/GRD/PRC como taxonomía núcleo;
4. GenSound derivado de soundness por modo;
5. GenComplete condicionado exactamente por ProdCoverage;
6. GF1–GF6 para evitar manipulación de RootClosed;
7. P1–P8 como modelos adversariales.

Por tanto REV-07b permanece **PARTIAL** por una sola deuda sustantiva principal: demostrar o asumir explícitamente ProdCoverage en el contexto usado por ExistsR. No debe marcarse RESOLVED mientras pueda existir una instancia de OntProd legítima fuera de CAU/CON/GRD/PRC.

#### 0.4.4. Relaciones ontológicas puras no son una quinta familia de OntProd

REV-07b no pretende que toda relación ontológica sea productiva. Introducimos:

$$
\operatorname{PureOntRel}_i(\rho_i;U_i),
$$

para una instancia relacional actual $\rho_i$ con pluralidad de relata $U_i$ cuya semántica propia conecta esos relata pero **no establece por sí sola una orientación productiva** hacia ninguno de ellos.

Debe satisfacer:

- **POR1 / actuality:** $\rho_i$ es una instancia actual, no mera posibilidad de relación;
- **POR2 / token-specific:** la instancia obtiene entre esos relata concretos;
- **POR3 / non-representational:** no es solo una relación entre descripciones/modelos;
- **POR4 / non-productive orientation:** para todo $x_i\preceq U_i$ y soporte $A_i\preceq U_i\setminus\{x_i\}$, $\neg\operatorname{OntProd}_i(\rho_i,A_i,x_i)$. Si aparece una orientación CAU/CON/GRD/PRC —o futura familia productiva— la instancia deja de contar como PureOntRel;
- **POR5 / support footprint:** existe $\operatorname{RelFoot}_i(\rho_i;U_i)$ con $U_i\cup\{\rho_i\}\preceq\operatorname{RelFoot}_i(\rho_i;U_i)$;
- **POR6 / candidate independence:** PureOntRel/RelFoot no mencionan Seed, OntOrigin, $R_i$, CoReal, SameRegime, CommonGround ni CGP;
- **POR7 / recoding invariance:** recodificaciones fieles preservan la instancia y su footprint.

Por tanto:

$$
\boxed{
\operatorname{PureOntRel}_i(\rho_i;U_i)
\not\Rightarrow
\operatorname{OntProd}_i(\rho_i,A_i,x_i).
}
$$

Esto no significa que $\rho_i$ carezca de genealogía. La **relación-token** puede ser fundamental, estar en el origen o ser target de CAU/CON/GRD/PRC. Lo que POR4 prohíbe es convertir su incidencia en producción de sus propios relata.

#### 0.4.5. No hay relaciones colgantes ni expansión gratuita por incidencia

Definimos cierre de soporte relacional para un carrier $X_i$:

$$
\operatorname{RelSupportClosed}_i(X_i)
:\Longleftrightarrow
\forall \rho_i,U_i[
\rho_i\preceq X_i
\land
\operatorname{PureOntRel}_i(\rho_i;U_i)
\Rightarrow
\operatorname{RelFoot}_i(\rho_i;U_i)\preceq X_i
].
$$

Una OriginConfig bien formada debe satisfacer:

$$
\boxed{
\operatorname{OriginConfig}_i(\mathcal O_i)
\Rightarrow
\operatorname{RelSupportClosed}_i(
\operatorname{Seed}_i(\mathcal O_i)
).
}
$$

Además GF2 se refuerza: si un GenFoot contiene una relación-token actual, contiene también su RelFoot obligatorio. Eso no autoriza a introducir endpoints gratis. Para toda relación pura presente en un footprint generativo:

$$
\boxed{
\begin{aligned}
&\operatorname{GenEvent}_i(e_i,A_i,b_i)
\land
\rho_i\preceq\operatorname{GenFoot}_i(e_i,A_i,b_i)\\
&\land
\operatorname{PureOntRel}_i(\rho_i;U_i)
\Rightarrow
U_i\setminus\{b_i\}\preceq A_i.
\end{aligned}
}
$$

Así, si el target es la propia relación $\rho_i$, todos sus relata deben estar ya disponibles; si el target $b_i$ es uno de los relata, los demás deben estar entre los antecedentes. La mera incidencia nunca introduce otro endpoint. Si relación y relata son genuinamente co-constitutivos por una estructura más fuerte, el caso deja de ser puro y debe justificarse mediante CON/GRD y, para OriginUnity, mediante EssConDep/ConstitutiveBridge.

En particular, PureOntRel **no puede ser por sí sola** el ConstitutiveBridge que convierta una suma de raíces en un origen único. RelSupportClosed garantiza well-formedness del hecho relacional; OriginUnity sigue exigiendo dependencia constitutiva esencial bilateral independiente.

Consecuencia: no hace falta introducir por ahora una segunda clausura $Cl^{Rel}$. Las relaciones actuales son contenido ontológico y sus footprints deben estar bien formados, pero la incidencia pura no añade nuevos relata a la genealogía.

#### 0.4.6. Stress test mixto: relación–genealogía–relación

Considérese:

$$
\operatorname{PureOntRel}_i(\rho_i;\{a_i,d_i\}),
\qquad
\operatorname{OntProd}_i(e_i,\{d_i\},c_i),
\qquad
\operatorname{PureOntRel}_i(\sigma_i;\{c_i,b_i\}).
$$

Existe entonces el camino ontológico mixto:

$$
a_i
\mathrel{-_{\rho_i}}
d_i
\xrightarrow{e_i}
c_i
\mathrel{-_{\sigma_i}}
b_i.
$$

Pero no se deriva:

$$
\operatorname{OntProd}_i(-,\{a_i\},b_i),
\qquad
\operatorname{OntProd}_i(-,\{b_i\},a_i),
$$

ni una capacidad causal mutua. **Conectividad ontológica no equivale a influencia causal.**

Si todos los tokens de la cadena están ya bien tipados bajo la misma instanciación $i$, la cadena es evidencia estructural de que $a_i$ y $b_i$ pertenecen a un mismo marco realizado. En cambio, a nivel pre-indexado, tres testigos pairwise separados no bastan: hace falta una única realización coherente que contenga simultáneamente $\rho,e,\sigma$ y sus relata.

Este caso no refuta ProdCoverage, porque PureOntRel no es OntProd. Sí crea un adversario directo para la tesis más fuerte de que una única genealogía productiva basta automáticamente para toda unidad de contexto. La cuestión se bifurca: REV-07e/CGP decide si existe un CommonGround cuando esa hipótesis se invoca; si las genealogías independientes ya están justificadamente tipadas en un mismo SharedOntSpace, su ensamblaje pertenece a GeneFamily/GeneBasis + RegimeClosure + RegimeTotal. GeneTotal queda únicamente como especialización singleton/monogeneal y no puede resolver por sí solo este caso multigeneal.

La proyección binaria:

$$
\operatorname{GenStep}_i(a_i,b_i)
:\Longleftrightarrow
\exists e_i\exists A_i[
\operatorname{GenEvent}_i(e_i,A_i,b_i)
\land
a_i\prec A_i
]
$$

solo registra dependencia/incidencia.

### 0.5. Contraejemplo a usar GenStep como closure rule

Supóngase un único hiperevento:

$$
\operatorname{GenEvent}_i(e_i,\{a_i,b_i\},c_i)
$$

y ningún evento con antecedente unitario que produzca $c_i$.

Por proyección:

$$
\operatorname{GenStep}_i(a_i,c_i)
\land
\operatorname{GenStep}_i(b_i,c_i).
$$

Si la clausura usase GenStep como regla binaria, entonces desde:

$$
\{a_i\}
$$

añadiría indebidamente:

$$
c_i.
$$

Pero la semántica correcta del hiperevento exige:

$$
\{a_i,b_i\}\preceq X_i
$$

antes de generar $c_i$.

Por tanto:

$$
\boxed{
\text{binary projection does not preserve generative closure in general}.
}
$$

### 0.6. Operador generativo

Definimos:

$$
\Gamma_i(X_i)
:=
X_i
\cup
\bigcup
\{
\operatorname{GenFoot}_i(e_i,A_i,b_i)
\mid
\operatorname{GenEvent}_i(e_i,A_i,b_i)
\land
A_i\preceq X_i
\}.
$$

Con una familia fija de GenEvent, $\Gamma_i$ es extensivo:

$$
X_i\preceq\Gamma_i(X_i),
$$

y monótono:

$$
X_i\preceq Y_i
\Rightarrow
\Gamma_i(X_i)\preceq\Gamma_i(Y_i).
$$

La monotonicidad se sigue porque cualquier familia de antecedentes contenida en $X_i$ también está contenida en $Y_i$.

### 0.7. Least generative closure sin presuponer existencia

Sea:

$$
B_i:=\operatorname{Seed}_i(\mathcal O_i).
$$

No usamos $\mu$ como operador total. Definimos primero el predicado:

$$
\operatorname{GenClosure}_i(\mathcal O_i,C_i)
$$

si y solo si:

$$
B_i\preceq C_i,
$$

$$
\Gamma_i(C_i)=C_i,
$$

y:

$$
\forall X_i[
B_i\preceq X_i
\land
\Gamma_i(X_i)=X_i
\Rightarrow
C_i\preceq X_i
].
$$

Definimos:

$$
\boxed{
\mathrm{GCExists}_i(\mathcal O_i)
:\Longleftrightarrow
\exists C_i\;
\operatorname{GenClosure}_i(\mathcal O_i,C_i).
}
$$

Si GCExists vale, la minimalidad hace único a $C_i$ respecto del orden $\preceq$ y podemos escribir:

$$
\operatorname{Cl}^{G}_i(\mathcal O_i)
$$

como abreviatura de ese carrier.

Condicionado a GCExists se obtienen:

**GC1 — extensividad del seed**

$$
B_i\preceq\operatorname{Cl}^{G}_i(\mathcal O_i).
$$

**GC2 — cierre**

$$
\Gamma_i(\operatorname{Cl}^{G}_i(\mathcal O_i))
=
\operatorname{Cl}^{G}_i(\mathcal O_i).
$$

**GC3 — minimalidad**

$$
B_i\preceq X_i
\land
\Gamma_i(X_i)=X_i
\Rightarrow
\operatorname{Cl}^{G}_i(\mathcal O_i)\preceq X_i.
$$

**GC4 — monotonía respecto del seed**, siempre que ambos closures existan:

$$
B_i\preceq B'_i
\Rightarrow
\operatorname{Cl}^{G}_i(B_i)
\preceq
\operatorname{Cl}^{G}_i(B'_i).
$$

Así la existencia de la least closure queda como obligación explícita de REV-07c y puede fallar si el marco fundacional no admite el carrier requerido.


### 0.8. Irredundancia del origen

Para bloquear seed-stuffing sin destruir orígenes cíclicos:

$$
\boxed{
\mathrm{Irredundant}_i(\mathcal O_i)
:\Longleftrightarrow
\neg\exists\mathcal O'_i\prec\mathcal O_i[
\operatorname{OriginCandidate}_i(\mathcal O'_i)
\land
\mathrm{GCExists}_i(\mathcal O'_i)
\land
\operatorname{Cl}^{G}_i(\mathcal O'_i)
=
\operatorname{Cl}^{G}_i(\mathcal O_i)
].
}
$$

Por tanto una subconfiguración solo compite si también es OriginConfig + OriginUnity + RootClosed. En el ciclo $a\leadsto b\leadsto a$, el singleton $\{a\}$ no derrota al origen completo cuando $b$ es una entrada productiva externa a ese singleton.

Esto permite representaciones equivalentes solo mediante una relación explícita de equivalencia de origen; no por igualdad extensional accidental.

### 0.9. OriginCandidate y OntOrigin provisional

Separamos el criterio pre-clausura:

$$
\operatorname{OriginCandidate}_i(\mathcal O_i)
:\Longleftrightarrow
\mathrm{OriginConfig}_i(\mathcal O_i)
\land
\mathrm{OriginUnity}_i(\mathcal O_i)
\land
\mathrm{RootClosed}_i(\mathcal O_i),
$$

del origen apto para una GeneUnit local:

$$
\operatorname{OntOrigin}_i(\mathcal O_i)
:\Longleftrightarrow
\operatorname{OriginCandidate}_i(\mathcal O_i)
\land
\mathrm{GenAdequate}_i
\land
\mathrm{GCExists}_i(\mathcal O_i)
\land
\mathrm{Irredundant}_i(\mathcal O_i).
$$

Esto hace explícito que OntOrigin exige dos obligaciones separadas: adecuación generativa (REV-07b) y existencia de la least closure (REV-07c). Ninguna se obtiene por definición del origen.

El criterio sigue siendo no circular respecto de $R_i$ siempre que OriginConfig, UnitFact/OriginUnity, OntProd y GenEvent sean caracterizados independientemente.


### 0.10. Generated local y GeneTotal monogeneal

$$
\boxed{
\operatorname{Generated}^{*}_i(\mathcal O_i,x_i)
:\Longleftrightarrow
\exists C_i[
\operatorname{GenClosure}_i(\mathcal O_i,C_i)
\land
x_i\in C_i
].
}
$$

Esta definición relacional es **local a una GeneUnit**. Si $\mathrm{GCExists}_i(\mathcal O_i)$ vale, la unicidad por minimalidad permite:

$$
\operatorname{Generated}^{*}_i(\mathcal O_i,x_i)
\Longleftrightarrow
x_i\in\operatorname{Cl}^{G}_i(\mathcal O_i).
$$

Bajo OntOrigin + GenAdequate la dirección correcta es soundness:

$$
\operatorname{Generated}^{*}_i(\mathcal O_i,x_i)
\Rightarrow
\operatorname{Real}_i(x_i).
$$

No vale en general la conversa: una GeneUnit local no tiene por qué generar todo el contenido real de $i$.

El caso monogeneal se conserva como:

$$
\operatorname{GeneTotal}_i(\mathcal O_i,R_i)
:\Longleftrightarrow
\exists C_i[
\operatorname{GeneUnit}_i(\mathcal O_i,C_i)
\land
\forall x_i[
\operatorname{Within}_i(x_i,R_i)
\leftrightarrow
\operatorname{Real}_i(x_i)
\leftrightarrow
x_i\in C_i
]
].
$$

### 0.10a. REV-07f — RegimeTotal multigeneal

Representamos la familia mediante una indexación puramente metateórica:

$$
\mathfrak G_i
=
\langle G_{\alpha,i}\rangle_{\alpha\in A},
\qquad
G_{\alpha,i}
=
\langle\mathcal O_{\alpha,i},C_{\alpha,i}\rangle.
$$

$A$ no es un sort ontológico ni una colección de contextos: solo parametriza los miembros de la familia en la metateoría. La formación de $\mathfrak G_i$ presupone que todos esos miembros ya están tipados en el mismo contexto $i$; por tanto GeneFamily no demuestra SharedOntSpace.

Definimos GeneFamily:

$$
\boxed{
\begin{aligned}
\operatorname{GeneFamily}_i(\mathfrak G_i)
:\Longleftrightarrow\;&
A\neq_{\mathsf M}\varnothing\\
&\land
\forall^{\mathsf M}\alpha\in A\;
\operatorname{GeneUnit}_i(
\mathcal O_{\alpha,i},
C_{\alpha,i}
)\\
&\land
\forall^{\mathsf M}\alpha,\beta\in A[
\alpha\neq_{\mathsf M}\beta
\land
\operatorname{GeneOverlap}_i(
G_{\alpha,i},
G_{\beta,i}
)
\Rightarrow
\operatorname{OverlapCoherence}_i(
G_{\alpha,i},
G_{\beta,i}
)
].
\end{aligned}
}
$$

La base familiar queda entonces determinada, no elegida:

$$
\boxed{
\operatorname{FamilyBase}_i(\mathfrak G_i,B_i)
:\Longleftrightarrow
\forall x_i[
x_i\in B_i
\leftrightarrow
\exists^{\mathsf M}\alpha\in A\;
x_i\in C_{\alpha,i}
].
}
$$

Los cuantificadores sobre $\alpha,\beta$ son metateóricos. OverlapCoherence se exige solo entre miembros distintos; una familia singleton no adquiere una obligación extra de self-coherence. Si la fundación elegida no permite la clase de indexación requerida por una familia concreta, falla RGCExists/REV-07c; no se obtiene existencia por notación.

La unión de closures locales no es todavía total porque puede habilitar producción transversal. Por eso:

$$
\boxed{
\begin{aligned}
\operatorname{RegimeClosure}_i(\mathfrak G_i,C_i)
:\Longleftrightarrow
\exists B_i[
&\operatorname{FamilyBase}_i(\mathfrak G_i,B_i)
\land
B_i\preceq C_i
\land
\Gamma_i(C_i)=C_i\\
&\land
\forall Y_i[
B_i\preceq Y_i
\land
\Gamma_i(Y_i)=Y_i
\Rightarrow
C_i\preceq Y_i
]
].
\end{aligned}
}
$$

Así:

$$
\mathrm{RGCExists}_i(\mathfrak G_i)
:\Longleftrightarrow
\exists C_i\;
\operatorname{RegimeClosure}_i(\mathfrak G_i,C_i),
$$

y:

$$
\boxed{
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i)
:\Longleftrightarrow
\exists C_i[
\operatorname{RegimeClosure}_i(\mathfrak G_i,C_i)
\land
x_i\in C_i
].
}
$$

La minimalidad de la base se formula sobre la **closure obtenida**, no sobre $R_i$. Para no sobrecargar $\prec$, que ya se usa para subconfiguraciones-originarias, introducimos el juicio metateórico $\operatorname{ProperSubfamily}^{\mathsf M}$:

$$
\boxed{
\begin{aligned}
\mathrm{FamilyIrredundant}_i(\mathfrak G_i)
:\Longleftrightarrow
\neg\exists^{\mathsf M}\mathfrak G'_i[
&\operatorname{ProperSubfamily}^{\mathsf M}
(\mathfrak G'_i,\mathfrak G_i)
\land
\operatorname{GeneFamily}_i(\mathfrak G'_i)\\
&\land
\mathrm{RGCExists}_i(\mathfrak G'_i)
\land
\forall x_i[
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G'_i,x_i)
\leftrightarrow
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i)
]
].
\end{aligned}
}
$$

Por tanto:

$$
\operatorname{GeneBasis}_i(\mathfrak G_i)
:\Longleftrightarrow
\operatorname{GeneFamily}_i(\mathfrak G_i)
\land
\mathrm{RGCExists}_i(\mathfrak G_i)
\land
\mathrm{FamilyIrredundant}_i(\mathfrak G_i),
$$

y:

$$
\boxed{
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
:\Longleftrightarrow
\operatorname{GeneBasis}_i(\mathfrak G_i)
\land
\forall x_i[
\operatorname{Within}_i(x_i,R_i)
\leftrightarrow
\operatorname{Real}_i(x_i)
\leftrightarrow
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i)
].
}
$$

Como la cláusula central incluye exhaustividad extensional del scope respecto de todo contenido real del contexto:

$$
\boxed{
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
\Rightarrow
\operatorname{OntTotal}_i(R_i).
}
$$

Este puente es una consecuencia de RegimeTotal, no una premisa adicional ni una propiedad obtenida desde SemTotal.

#### Singleton compatibility theorem

Sea $C_i$ la GenClosure de $\mathcal O_i$ y:

$$
\mathfrak G_i
=
\{
\langle\mathcal O_i,C_i\rangle
\}.
$$

Como $C_i$ ya es fijo de $\Gamma_i$, es también el menor fixed point que contiene FamilyBase. En una familia singleton no existen pares distintos $\alpha\neq_{\mathsf M}\beta$, así que la cláusula de OverlapCoherence es vacua; la irredundancia familiar también es vacua porque no existe subfamilia propia no vacía. Por tanto:

$$
\boxed{
\operatorname{GeneTotal}_i(\mathcal O_i,R_i)
\Longleftrightarrow
\operatorname{RegimeTotal}_i(
\{\langle\mathcal O_i,C_i\rangle\},
R_i
).
}
$$

Esto conserva toda consecuencia válida del caso monogeneal y, a la vez, impide que GeneTotal sea el único witness de existencia.

#### RT-07-MG — Multigeneal Reality Test

Sea un único contexto admisible $k$ con:

$$
D_k=\{a,b\},
\qquad
\operatorname{Real}_k=\{a,b\},
$$

dos configuraciones:

$$
\operatorname{Seed}(\mathcal O_1)=\{a\},
\qquad
\operatorname{Seed}(\mathcal O_2)=\{b\},
$$

y ninguna producción:

$$
\operatorname{OntProd}_k=\varnothing,
\qquad
\operatorname{GenEvent}_k=\varnothing.
$$

Entonces:

$$
C_1=\{a\},
\qquad
C_2=\{b\}
$$

son GenClosure. Los singleton satisfacen OriginUnity vacuamente bajo M1; RootClosed, ProdCoverage y GenAdequate son vacuos. Suponemos además la irredundancia local correspondiente. Por tanto:

$$
\operatorname{GeneUnit}_k(\mathcal O_1,C_1),
\qquad
\operatorname{GeneUnit}_k(\mathcal O_2,C_2).
$$

Fijamos:

$$
\mathrm{NoConstitutiveBridge}_k(\{a\},\{b\}),
$$

de modo que ninguna configuración con seed $\{a,b\}$ puede satisfacer OriginUnity. Como no hay GenEvent, ninguna otra base singleton puede generar ambos tokens.

Para:

$$
\mathfrak G_k
=
\{
\langle\mathcal O_1,C_1\rangle,
\langle\mathcal O_2,C_2\rangle
\},
$$

se obtiene:

$$
\operatorname{FamilyBase}_k(\mathfrak G_k,\{a,b\}),
\qquad
\Gamma_k(\{a,b\})=\{a,b\},
$$

y cada subfamilia propia no vacía cierra solo sobre uno de los dos tokens. Luego:

$$
\mathrm{FamilyIrredundant}_k(\mathfrak G_k),
$$

y para el scope exhaustivo $R_k$:

$$
\boxed{
\operatorname{RegimeTotal}_k(\mathfrak G_k,R_k)
\land
\neg\exists\mathcal O_k\;
\operatorname{GeneTotal}_k(\mathcal O_k,R_k).
}
$$

Éste es el contraejemplo exigido a la conversa del singleton theorem. El antiguo ExistsR basado solo en GeneTotal fallaba en este modelo; el nuevo ExistsR basado en RegimeTotal no.

#### RT-07-XP — Transversal Production Test

Sean:

$$
a_k\in C_{1,k},
\qquad
b_k\in C_{2,k},
$$

y un hiperevento:

$$
\operatorname{GenEvent}_k(e_k,\{a_k,b_k\},c_k).
$$

Aunque cada $C_{\alpha,k}$ sea localmente cerrado:

$$
c_k\notin C_{1,k}\cup C_{2,k}
$$

puede ocurrir, porque ningún cierre local dispone de ambos antecedentes. Supongamos ahora explícitamente:

$$
\mathrm{RGCExists}_k(\mathfrak G_k),
$$

y fijemos un testigo $C_k$ tal que:

$$
\operatorname{RegimeClosure}_k(\mathfrak G_k,C_k).
$$

FamilyBase contiene conjuntamente $a_k$ y $b_k$; como $C_k$ es fijo de $\Gamma_k$ y contiene esa base:

$$
\operatorname{GenFoot}_k(e_k,\{a_k,b_k\},c_k)
\preceq
C_k.
$$

Además:

$$
\bigcup_\alpha C_{\alpha,k}
\preceq
C_k,
\qquad
c_k\in C_k,
\qquad
c_k\notin\bigcup_\alpha C_{\alpha,k}.
$$

Por tanto:

$$
\boxed{
\bigcup_\alpha C_{\alpha,k}
\subsetneq
C_k
}
$$

es posible **condicionalmente a RGCExists**. El test no denota RegimeClosure como una función total ni presupone que el least fixed point exista en toda fundación. Una definición de RegimeTotal por mera unión falla este test.

#### RT-07-MG-TRIV — Singleton-per-token attack

FamilyIrredundant elimina unidades que no cambian RegimeClosure, pero no pretende declarar ilegítimas todas las raíces singleton. El guard sustantivo está antes: cada miembro debe satisfacer OntOrigin de forma independiente.

Si un token $b_i$ es realmente producido por:

$$
\operatorname{OntProd}_i(e_i,A_i,b_i),
$$

declarar $\{b_i\}$ como seed originario falla RootClosed salvo que todo GenFoot productor pertenezca al seed. Ocultar esa producción para salvar el singleton sería un fallo de la semántica de OntProd/ProdCoverage —REV-07b—, no una libertad introducida por RegimeTotal.

Si, en cambio, varios tokens son realmente primitivos, no producidos e independientes, una base compuesta por sus singleton GeneUnit es justamente lo que debe representar una realidad multigeneal.

#### Estado de REV-07f

El defecto de monogeneidad queda cerrado **arquitectónicamente**:

$$
\boxed{
\operatorname{GeneTotal}
\subsetneq
\operatorname{RegimeTotal}
}
$$

en el sentido de clase de realizaciones posibles, con equivalencia exacta en familias singleton y un contramodelo finito para la conversa general.

Esto no cierra REV-07b ni REV-07c: RegimeTotal sigue condicionado a la adecuación de OntProd/GenEvent y a la existencia fundacional de RegimeClosure.

### 0.11. Convergencia, reindexación y Common-Ground Principle

Considérense dos candidatos pre-indexados $C_a,C_b$ que parecen genealógicamente independientes y un hecho ontológico conjunto $e$ en el que ambos participan.

Hay que separar tres afirmaciones:

1. **integración observada:** existe un hecho ontológico bien tipado que involucra imágenes de ambos candidatos;
2. **unidad de contexto:** ambos son realizables conjuntamente bajo una misma instanciación admisible;
3. **common ground:** existe un OntOrigin independiente cuya clausura fundamenta fielmente ambos candidatos.

Introducimos el metaschema débil:

$$
\operatorname{Integrable}^{\mathsf M}(C_a,C_b)
\Rightarrow
\operatorname{JointRealizable}^{\mathsf M}(C_a,C_b).
$$

JointRealizable significa que existe alguna instanciación admisible de contexto en la que embeddings fieles de ambos candidatos y el hecho común están simultáneamente bien tipados. Esto invalida una hipótesis **provisional** de incompatibilidad final, pero no demuestra por sí solo genealogía común:

$$
\boxed{
\operatorname{JointRealizable}^{\mathsf M}(C_a,C_b)
\not\Rightarrow
\operatorname{CommonGround}^{\mathsf M}(C_a,C_b).
}
$$

CommonGround exige independientemente una instanciación admisible $i$ y testigos $\mathcal O_i,C_i$ tales que $\operatorname{OntOrigin}_i(\mathcal O_i)$, $\operatorname{GenClosure}_i(\mathcal O_i,C_i)$ y embeddings fieles de ambos candidatos en $C_i$. Así no se usa $\operatorname{Cl}^{G}_i$ fuera de GCExists. En particular, el propio evento convergente no puede servir de common ground solo por ser posterior/integrativo; ConstitutiveBridge + UnitFoot bloquean precisamente ese reciclaje porque exigen dependencia constitutiva esencial cruzada hacia ambos lados.

La tesis fuerte queda entonces:

$$
\mathrm{CGP}:
\quad
\operatorname{JointRealizable}^{\mathsf M}(C_a,C_b)
\Rightarrow
\operatorname{CommonGround}^{\mathsf M}(C_a,C_b).
$$

CGP **no es derivable de la doctrina vigente** y no se deriva de EXT-01. Solo puede recuperarse como premisa metafísica adicional que excluya el contramodelo finito de §0.11.4; si se adoptara, la convergencia sería «retroactiva» solo epistemológicamente y el common ground seguiría siendo independiente del evento integrador.

La alternativa conceptualmente distinta es una **ontogénesis por convergencia**:

$$
C_a,C_b
\xRightarrow{e}
R_k^{\mathrm{new}},
$$

donde la integración no revela una realidad común previa sino que constituye una nueva. La notación histórica con un evento cross-index queda SUPERSEDED: la doctrina vigente usa ContextGenesis en el metalenguaje, continuaciones tipadas y un witness child-side $g_k$; la génesis genuina exige GenesisConstitutiveUnity y novedad de índice.

Por tanto el caso de prueba obligatorio para REV-07e es:

$$
A\rightsquigarrow\cdots\rightsquigarrow a,
\qquad
B\rightsquigarrow\cdots\rightsquigarrow b,
\qquad
\operatorname{OntProd}(e,\{a,b\},c).
$$

La teoría distingue ahora sin circularidad entre: (i) espacio común preexistente revelado por una integración; y (ii) ontogénesis fuerte, donde un nuevo $k$ aparece con GenesisConstitutiveUnity child-side. Un hecho integrador por sí solo sigue estableciendo como máximo joint realizability/convergence, no génesis.

#### 0.11.1. Integración puramente relacional

El mismo problema aparece sin convergencia productiva. Para candidatos pre-indexados $C_a,C_b$, definimos el metaschema:

$$
\operatorname{RelIntegrable}^{\mathsf M}(C_a,C_b)
$$

cuando existe **una única instanciación admisible** $k$, embeddings fieles de ambos candidatos y una instancia $\rho_k$ de PureOntRel cuyos relata incluyen imágenes de contenido de ambos candidatos.

Entonces:

$$
\boxed{
\operatorname{RelIntegrable}^{\mathsf M}(C_a,C_b)
\Rightarrow
\operatorname{JointRealizable}^{\mathsf M}(C_a,C_b).
}
$$

Pero, igual que para integración productiva:

$$
\boxed{
\operatorname{RelIntegrable}^{\mathsf M}(C_a,C_b)
\not\Rightarrow
\operatorname{CommonGround}^{\mathsf M}(C_a,C_b).
}
$$

La exigencia de una **única** realización es esencial. De:

$$
\operatorname{RelIntegrable}^{\mathsf M}(C_a,C_d),
\qquad
\operatorname{RelIntegrable}^{\mathsf M}(C_c,C_b),
$$

y una realización separada de $d\to c$ no se sigue automáticamente que exista una realización común de $a,d,c,b$. La realizabilidad pairwise no es aquí una regla de transitividad.

#### 0.11.2. Cadena mixta coherente

La intuición:

$$
a-\rho-d\to c-\sigma-b
$$

se formaliza pre-indexadamente solo cuando existe un único contexto testigo $k$ en el que están simultáneamente bien tipados:

$$
\operatorname{PureOntRel}_k(\rho_k;\{a_k,d_k\}),
$$

$$
\operatorname{OntProd}_k(e_k,\{d_k\},c_k),
$$

$$
\operatorname{PureOntRel}_k(\sigma_k;\{c_k,b_k\}).
$$

Ese testigo establece que $a$ y $b$ están dentro de un **mismo marco realizado** en el sentido débil de JointRealizable. No establece por sí mismo:

- que $a$ produzca $b$;
- que $b$ produzca $a$;
- que exista un canal causal entre ellos;
- que compartan OntOrigin;
- que CGP sea verdadero.

La posible influencia causal requiere un testigo CAU/PRC adicional; no se deriva de la mera cadena relacional.

#### 0.11.3. HISTORICAL — dilema monogeneal pre-REV-07f

Este stress test fue el punto donde la arquitectura anterior mostró una falsa disyunción: trataba implícitamente la exhaustividad de $R_i$ como si exigiera una sola $\operatorname{Generated}^{*}_k(\mathcal O_k,-)$.

Si una cadena mixta coherente está enteramente contenida en una misma GeneUnit, el caso sigue siendo monogeneal y no hay dificultad adicional. Pero si existen dos GeneUnit independientemente adecuadas $G_a,G_b$ y una PureOntRel actual entre contenido de ambas, sin ningún OntOrigin independiente cuya GenClosure contenga ambas, puede darse:

$$
\operatorname{JointRealizable}^{\mathsf M}(G_a,G_b)
\land
\neg\operatorname{CommonGround}^{\mathsf M}(G_a,G_b).
$$

**REV-07f retira la inferencia de que esto obliga a buscar un único origen común.** En la arquitectura vigente, si ambas genealogías ya están justificadamente tipadas en el mismo SharedOntSpace, pueden formar una GeneFamily y la totalidad se expresa mediante:

$$
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i),
$$

con $\operatorname{RegimeClosure}_i$ re-cerrando $\Gamma_i$ sobre la base conjunta. El caso:

$$
R_i=\operatorname{Cl}^{G}_i(\mathcal O_i)
$$

queda exclusivamente como la especialización singleton/monogeneal, no como arquitectura general.

Por tanto, las alternativas actuales ya no son «encontrar un origen común o renunciar a un mismo $R_i$». El problema restante de REV-07e es **clasificatorio y genético**: decidir con fundamento independiente si la integración observada pertenece a un SharedOntSpace ya justificado, exige ContextGenesis, o permanece solo en JointRealizable sin licencia para identificar contextos. CGP sigue OPEN allí donde se invoque CommonGround; REV-07f no lo demuestra ni lo necesita para el caso multigeneal SharedOntSpace.

La existencia de PureOntRel sigue mostrando que el problema no depende de causalidad ni de convergencia productiva, pero ya no reinstala monogeneidad en RegimeTotal.

#### 0.11.4. Contramodelo finito de CGP bajo la doctrina actual

Podemos hacer el adversario más fuerte evitando postular una relación actual sin genealogía propia. Considérese un carrier pre-indexado finito con tokens:

$$
\{a,b,\rho,e\},
$$

dos candidatos raíz singulares:

$$
C_a=\{a\},
\qquad
C_b=\{b\},
$$

y una instancia constitutiva que genera **la relación-token**, no sus relata:

$$
\operatorname{ConstitutiveProd}(e,\{a,b\},\rho),
\qquad
\operatorname{PureOntRel}(\rho;\{a,b\}).
$$

El no-free-endpoints guard se satisface porque ambos relata de $\rho$ están ya en el soporte $\{a,b\}$. PureOntRel sigue siendo estrictamente no productiva hacia $a$ o $b$:

$$
\neg\operatorname{OntProd}(\rho,A,a),
\qquad
\neg\operatorname{OntProd}(\rho,A,b)
$$

para todo soporte admisible $A$ formado por el otro relatum.

Supóngase además:

1. $\{a\}$ y $\{b\}$ satisfacen separadamente los requisitos locales de raíz/origen que no presuponen unidad entre ambos;
2. no existe ningún EssConDep/ConstitutiveBridge entre $a$ y $b$;
3. no existen otros tokens ni eventos productivos capaces de generar uno de los dos desde el otro o desde una tercera base;
4. la instancia $e$ y la relación $\rho$ están simultáneamente bien tipadas con $a,b$ en una única realización pre-indexada $k$.

Entonces:

$$
\operatorname{RelIntegrable}^{\mathsf M}(C_a,C_b)
$$

y por tanto:

$$
\operatorname{JointRealizable}^{\mathsf M}(C_a,C_b).
$$

Sin embargo, cualquier seed que pretenda contener conjuntamente $a$ y $b$ admite la partición que separa ambas raíces. Por (2), esa partición carece de ConstitutiveBridge; por tanto falla OriginUnity. Como (3) excluye una tercera base que genere ambas, no existe $\mathcal O_k$ tal que su GenClosure contenga fielmente los dos candidatos y satisfaga OntOrigin. Luego:

$$
\boxed{
\operatorname{JointRealizable}^{\mathsf M}(C_a,C_b)
\land
\neg\operatorname{CommonGround}^{\mathsf M}(C_a,C_b).
}
$$

Por tanto **CGP no es derivable de la doctrina vigente**. Para recuperarlo habría que añadir una premisa nueva que descarte este modelo; no puede obtenerse de JointRealizable, PureOntRel, OntProd, RelSupportClosed ni OriginUnity tal como están definidos.

Este resultado es model-theoretic/arquitectónico, no una afirmación de que el mundo actual instancie el contramodelo.

#### 0.11.5. Consecuencia: distinguir ContextUnity de GeneUnity

El contramodelo muestra que actualmente tenemos dos nociones distintas:

$$
\operatorname{ContextUnity}^{\mathsf M}(C_a,C_b)
:= 
\operatorname{JointRealizable}^{\mathsf M}(C_a,C_b),
$$

y:

$$
\operatorname{GeneUnity}^{\mathsf M}(C_a,C_b)
:=
\operatorname{CommonGround}^{\mathsf M}(C_a,C_b).
$$

La doctrina vigente solo demuestra:

$$
\operatorname{GeneUnity}^{\mathsf M}
\Rightarrow
\operatorname{ContextUnity}^{\mathsf M},
$$

mientras la conversa es precisamente CGP y queda refutada como **teorema derivable** por el contramodelo anterior:

$$
\boxed{
\operatorname{ContextUnity}^{\mathsf M}
\not\Rightarrow_{\text{doctrina actual}}
\operatorname{GeneUnity}^{\mathsf M}.
}
$$

Esto no obliga todavía a redefinir $R_i$. Sí obliga a dejar de usar «mismo marco/contexto» y «misma realidad genealógica» como sinónimos antes de resolver REV-07e.

#### 0.11.6. Bifurcación fundamental: espacio compartido u ontogénesis

El contramodelo de CGP no deja cuatro interpretaciones ontológicas equiparables. Una integración estable entre genealogías tiene dos lecturas fundamentales:

$$
\boxed{
\text{integración estable}
\Rightarrow
\begin{cases}
\operatorname{SharedOntSpace}^{\mathsf M},\\
\operatorname{ContextGenesis}^{\mathsf M}.
\end{cases}
}
$$

La pregunta discriminante es si el contexto común **preexiste ontológicamente** a la integración o si la integración/estructura de formación **constituye un contexto nuevo**. La prioridad relevante es ontológica, no necesariamente temporal.

Context Assembly, $\Xi_i$ y las clausuras asociadas pasan a ser maquinaria formal neutral: pueden reconstruir un espacio ya compartido o implementar la formación de uno nuevo. No son una tercera tesis metafísica.

#### 0.11.6a. GeneUnit y solapamiento genealógico

Restauramos explícitamente la unidad genealógica local:

$$
\operatorname{GeneUnit}_i(\mathcal O_i,C_i)
:\Longleftrightarrow
\operatorname{OntOrigin}_i(\mathcal O_i)
\land
\operatorname{GenClosure}_i(\mathcal O_i,C_i).
$$

Para dos GeneUnit ya tipadas en el mismo contexto:

$$
\operatorname{GeneOverlap}_i(G_{\alpha,i},G_{\beta,i})
:\Longleftrightarrow
\exists x_i[
x_i\preceq C_{\alpha,i}
\land
x_i\preceq C_{\beta,i}
].
$$

El solapamiento no implica identidad de origen, CommonGround ni equivalencia de configuraciones:

$$
\operatorname{GeneOverlap}_i
\not\Rightarrow
\mathcal O_{\alpha,i}\simeq\mathcal O_{\beta,i}.
$$

Puede haber un mismo token con múltiples historias productivas suficientes. Lo exigible es **OverlapCoherence**: el token compartido conserva identidad tipada, hechos actuales y dependencias relevantes de manera compatible en ambas reconstrucciones; no se duplica ad hoc para salvar una genealogía ni se usa el solapamiento para fabricar retrospectivamente OriginUnity.

GeneOverlap es por tanto más fuerte que mera compatibilidad descriptiva y más débil que GeneUnity/CommonGround. En SharedOntSpace puede haber GeneUnit disjuntas o solapadas.

#### 0.11.7. Shared Ontological Space

Definimos metateóricamente:

$$
\operatorname{SharedOntSpace}^{\mathsf M}(C_a,C_b;k)
$$

cuando existe una instanciación admisible $k$ en la que hay realizaciones fieles de ambos candidatos y su coexistencia ontológica no depende constitutivamente del hecho integrador usado para descubrirla.

Entonces:

$$
\operatorname{SharedOntSpace}^{\mathsf M}(C_a,C_b;k)
\Rightarrow
\operatorname{JointRealizable}^{\mathsf M}(C_a,C_b).
$$

CommonGround es suficiente pero no necesario:

$$
\operatorname{CommonGround}^{\mathsf M}(C_a,C_b)
\Rightarrow
\exists k\,
\operatorname{SharedOntSpace}^{\mathsf M}(C_a,C_b;k),
$$

mientras:

$$
\operatorname{SharedOntSpace}^{\mathsf M}
\not\Rightarrow
\operatorname{CommonGround}^{\mathsf M}.
$$

Por tanto un único espacio ontológico puede contener varias genealogías locales con orígenes distintos. Una PureOntRel entre ellas puede **revelar** esa unidad de espacio sin crearla y sin convertirla en unidad de origen.

#### 0.11.8. Ontogénesis de contexto

La segunda posibilidad no presupone un contexto común previo. Introducimos exclusivamente en el metalenguaje:

$$
\operatorname{ContextGenesis}^{\mathsf M}
(C_i,C_j\Rightarrow k;\gamma).
$$

Su lectura es: $\gamma$ es un **juicio metateórico sobre una formación ontológica**, no una operación causal del metalenguaje. Registra que las realizaciones precursoras $i,j$ tienen continuaciones en una nueva instanciación $k$ cuya novedad está objetivamente testimoniada child-side por una estructura actual $g_k$.

No se escribe ningún evento objeto mal tipado:

$$
e(x_i,y_j).
$$

En su lugar, la génesis suministra mapas metateóricos de continuación/realización:

$$
\kappa_{i\to k}:x_i\rightsquigarrow x_k,
\qquad
\kappa_{j\to k}:y_j\rightsquigarrow y_k.
$$

$x_k$ y $y_k$ son contenido de $k$ que continúa fielmente contenido parental; no son literalmente los tokens cross-index $x_i,y_j$.

Las condiciones mínimas de ContextGenesis son:

1. **CGX1 / typed precursors:** cada precursor está bien tipado en su propio contexto;
2. **CGX2 / no cross-index event:** $\gamma$ no se expresa como relación objeto entre tokens incompatibles;
3. **CGX3 / faithful continuation:** las $\kappa$ preservan la estructura declarada de los precursores;
4. **CGX4 / constitutive novelty:** la existencia del contexto $k$ depende constitutivamente de la formación $\gamma$; no es solo un contexto preexistente descubierto;
5. **CGX5 / no retroactivity:** ninguna verdad, existencia o genealogía del token parental $x_i$ pasa a depender de $\gamma$;
6. **CGX6 / child-side auditability:** el contexto hijo contiene testigos tipados de la formación y de las continuaciones que permiten auditar qué estructura heredó;
7. **CGX7 / recoding invariance:** una recodificación fiel preserva el juicio de génesis y los mapas de continuación hasta equivalencia apropiada.

#### 0.11.9. Descendencia de contexto como relación metaontológica adicional

Definimos:

$$
\boxed{
i\prec_{\mathrm{ctx}}k
}
$$

cuando existe alguna ContextGenesis en la que $i$ es precursor de $k$.

Esto añade una relación conceptual adicional entre instanciaciones:

$$
i\simeq_{\mathrm{idx}}k,
\qquad
i\#k,
\qquad
i\prec_{\mathrm{ctx}}k.
$$

No forman una partición lógica automática. En particular:

$$
i\prec_{\mathrm{ctx}}k
\not\Rightarrow
i\simeq_{\mathrm{idx}}k
$$

y la mera descendencia tampoco implica por sí sola $i\#k$.

Para el caso de persistencia parental introducimos:

$$
\operatorname{PersistentParent}^{\mathsf M}(i,k),
$$

cuando existe una **co-realización efectiva padre–hijo**: una realización admisible en la que el contenido parental relevante y su continuación fiel en $k$ están simultáneamente representados como estructura ontológica actual, no solo enlazados por un mapa abstracto. Entonces:

$$
\boxed{
i\prec_{\mathrm{ctx}}k
\land
\operatorname{PersistentParent}^{\mathsf M}(i,k)
\Rightarrow
\neg(i\#k).
}
$$

Así una realidad nueva puede ser genuinamente nueva sin ser incompatible con su progenitora:

$$
i\not\simeq_{\mathrm{idx}}k,
\qquad
\neg(i\#k),
\qquad
i\prec_{\mathrm{ctx}}k.
$$

La novedad ontológica no equivale a incompatibilidad.

En una ontogénesis de reemplazo puede existir descendencia sin PersistentParent: los precursores solo tienen continuaciones en $k$. En ese caso no se decide $i\#k$ a partir de la descendencia sola.

#### 0.11.10. El origen del hijo no reescribe el origen del padre

Supóngase:

$$
\operatorname{ContextGenesis}^{\mathsf M}
(C_i,C_j\Rightarrow k;\gamma).
$$

El hijo puede poseer un testigo objeto $g_k$ de su formación y continuaciones:

$$
x_i\rightsquigarrow x_k,
\qquad
y_j\rightsquigarrow y_k.
$$

La dependencia constitutiva relevante es child-side:

$$
\operatorname{IdDep}_k(x_k;g_k\mid Y_k)
\lor
\operatorname{ConstExistDep}_k(x_k;g_k\mid Y_k),
$$

cuando la identidad/existencia de $x_k$ **como continuación dentro de $k$** requiere la estructura de génesis.

No se infiere:

$$
\operatorname{IdDep}_i(x_i;g_k\mid -)
$$

ni ninguna otra fórmula cross-index.

Por tanto la estructura de génesis puede contribuir a OriginUnity/OntOrigin de $k$ sin volverse retrospectivamente origen de $i$ o $j$. Tras G1–G4 se adopta No-Weak-Genesis: si las continuaciones no satisfacen dependencia constitutiva suficiente respecto de $g_k$, el caso no cuenta como ContextGenesis genuina y no se introduce un GenesisOrigin ad hoc.

#### 0.11.11. Las dos lecturas de una misma maquinaria de ensamblaje

Sea una familia de GeneUnit locales y links actuales:

$$
\mathfrak A_k=(\mathcal G_k,\mathcal L_k).
$$

La maquinaria de ensamblaje puede tener dos semánticas:

**Shared-space reconstruction.** $\mathfrak A_k$ reconstruye una estructura común que ya era real en $k$. AssemblyLink actúa como evidencia/cobertura y no como origen del contexto.

**Genesis construction.** $\mathfrak A_k$ está constituida por imágenes de continuación de precursores y por el witness $g_k$; el ensamblaje es parte de lo que hace existir el nuevo contexto $k$.

En ambos casos la mera unión de GeneUnit no basta. Si:

$$
a_k\in C_{\alpha,k},
\qquad
b_k\in C_{\beta,k},
\qquad
\operatorname{OntProd}_k(e_k,\{a_k,b_k\},c_k),
$$

el carrier debe cerrarse también bajo esa generación transversal.

#### 0.11.12. Operador conjunto de ensamblaje y generación

Conservamos el operador conjunto:

$$
\Xi_k(\mathcal G_k,K_k)
:=
\left(
\operatorname{LinkExpand}_k(\mathcal G_k,K_k),
\Gamma_k(
K_k\cup\operatorname{ExpandFoot}_k(\mathcal G_k,K_k)
)
\right).
$$

Su interpretación depende de la bifurcación anterior:

- en SharedOntSpace, el least fixed point pretende **reconstruir exhaustivamente** un espacio común preexistente;
- en ContextGenesis, el least fixed point pretende **construir/cerrar** el contenido del nuevo contexto a partir del witness de génesis y sus continuaciones.

Si LinkExpand es persistente bajo extensión y $\Gamma_k$ es monótono, $\Xi_k$ es monótono. ACExists continúa siendo la obligación de existencia de un least fixed point admisible; Knaster–Tarski solo la descarga condicionalmente en una implementación set-sized apropiada.

#### 0.11.13. Anti-agregación y anti-fusión

Ni SharedOntSpace ni ContextGenesis permiten bolsas arbitrarias.

Para SharedOntSpace hace falta un testigo independiente de coexistencia en $k$; que dos GeneUnit sean compatibles en abstracto no basta.

Para ContextGenesis hacen falta $\gamma$, continuaciones $\kappa$ y constitutive novelty. No vale introducir una génesis solo porque deseamos tratar dos contextos como padres de $k$.

Asimismo, un objeto/enlace actual dentro de $i$ nunca puede contener directamente términos de $j$ cuando $i\#j$. La formación de $k$ se expresa en el metalenguaje y solo sus imágenes child-side aparecen juntas en el lenguaje objeto de $k$.

#### 0.11.14. Stress tests revisados

**X1 — common ground.** Dos genealogías con OntOrigin común caen en SharedOntSpace; no hay ontogénesis.

**X2 — multi-origin shared space.** Dos GeneUnit sin CommonGround pero con coexistencia independiente en $k$ caen en SharedOntSpace. Una PureOntRel puede revelar la conexión sin crear $k$.

**X3 — ontogénesis genuina.** No existe espacio común previo; $\gamma$ constituye $k$ y las continuaciones parentales aparecen como $x_k,y_k$. No hay retroactividad.

**X4 — padre persistente.** Si contenido parental persiste mediante realización fiel dentro del espacio hijo, $i\prec_{\mathrm{ctx}}k$ y PersistentParent implican $\neg(i\#k)$ aunque $i\not\simeq_{\mathrm{idx}}k$.

**X5 — reemplazo.** Si solo existen continuaciones y no coexistencia padre-hijo, $i\prec_{\mathrm{ctx}}k$ no decide por sí mismo $i\#k$.

**X6 — producción transversal.** Una vez formadas/reconstruidas varias GeneUnit en $k$, GenEvent puede usar antecedentes de distintas unidades; $\Xi_k$ debe cerrar sus consecuencias.

**X7 — falsa génesis.** Una integración que ocurre dentro de un contexto común ya existente no satisface CGX4; clasificarla como ontogénesis sería reificar un evento interno como creador de su propio contexto.

**X8 — falso shared space.** Una operación de génesis no puede reinterpretarse retrospectivamente como prueba de que $k$ preexistía; hacerlo violaría CGX4/no-retroactivity.

#### 0.11.15. Consecuencia para R

REV-07e queda ahora reducido a dos arquitecturas sustantivas.

En el caso SharedOntSpace, $R_k$ puede ser **multigeneal**: varias GeneUnit locales comparten el mismo espacio sin CommonGround global. REV-07f formaliza este caso mediante GeneBasis + RegimeClosure + RegimeTotal; GeneTotal queda exactamente como la especialización singleton/monogeneal.

En el caso ContextGenesis, aparece una nueva $R_k$. Sus precursores no se insertan literalmente en $k$; entran mediante continuaciones tipadas. No-Weak-Genesis exige que la configuración child-side satisfaga OriginUnity; si falla, el caso se reclasifica como SharedOntSpace, transformación interna o génesis no justificada, no como una segunda especie de origen.

Por tanto la pregunta doctrinal ya no es CGP. Es:

$$
\boxed{
\text{¿el contexto común preexistía o fue constituido?}
}
$$

Context Assembly/$\Xi$ queda subordinado a esa respuesta y deja de ser una tercera ontología.

#### 0.11.16. Hipótesis fuerte: no hay ontogénesis débil

Probamos la hipótesis doctrinal:

$$
\boxed{
\operatorname{ContextGenesis}^{\mathsf M}
\Rightarrow
\operatorname{GenesisConstitutiveUnity}_k.
}
$$

GenesisConstitutiveUnity no significa que los tokens parentales pasados dependan retroactivamente de la génesis. Exige que **las continuaciones en el hijo, como contenido de $k$, y la estructura de formación child-side pertenezcan a una configuración que satisfaga OriginUnity$_k$**.

La separación de niveles es obligatoria:

- $\gamma$ es parte del **juicio metateórico** de transición entre tipados; no es una entidad, evento ni portador de Real;
- $g_k$ es el **witness ontológico actual child-side** de la novedad constitutiva;
- las continuaciones $\kappa_{i\to k}(x_i)=x_k$ y $\kappa_{j\to k}(y_j)=y_k$ sí son términos objeto de $k$;
- ninguna fórmula cross-index transforma a $\gamma$ en una superentidad que exista “entre” realidades.

Por tanto evitamos escribir:

$$
\operatorname{Real}(\gamma)
$$

o cualquier variante indexada de esa expresión. La metarelación registra una formación; la realidad de la novedad debe poder auditarse enteramente desde $k$ mediante $g_k$ y su estructura.

Definimos esquemáticamente:

$$
\operatorname{GenesisConstitutiveUnity}_k(\mathcal O_k;g_k)
$$

cuando:

1. $\mathcal O_k$ es una OriginConfig child-side que contiene las continuaciones relevantes y el footprint completo de $g_k$;
2. $g_k$ es actual, independiente del candidato y recoding-invariant;
3. toda partición no trivial de $\operatorname{Seed}_k(\mathcal O_k)$ posee un ConstitutiveBridge conforme ECD1–ECD7;
4. las particiones que separan imágenes de distintos precursores requieren dependencia constitutiva cruzada real, no mera causalidad, interacción o co-presencia;
5. las particiones que separan el witness/estructura de génesis de las continuaciones también deben quedar bridged: no basta con bilateralidad entre las dos ramas parentales;
6. quitar la estructura constitutiva de génesis puede dejar intactos los parentales $x_i,y_j$, pero no puede dejar intacta la identidad/existencia de sus continuaciones **como contenido de $k$**.

La condición (5) evita una falsa prueba donde $g_k$ es solo un evento externo que “pega” dos linajes. Una génesis fuerte exige una configuración child-side ontológicamente unificada.

#### 0.11.17. Test G1 — co-constitución bilateral/holística

Sean continuaciones:

$$
x_i\rightsquigarrow x_k,
\qquad
y_j\rightsquigarrow y_k,
$$

y una estructura actual $g_k$ tal que la semántica independiente justifica, al menos:

$$
\operatorname{IdDep}_k(x_k;g_k\mid Y_k)
\lor
\operatorname{ConstExistDep}_k(x_k;g_k\mid Y_k),
$$

con soporte cruzado que incluye contenido heredado de $j$, y simétricamente para $y_k$ respecto del sector heredado de $i$.

Esto supera la partición parental:

$$
X_k^{(i)}\mid Y_k^{(j)}.
$$

Pero eso **no basta todavía**. GenesisConstitutiveUnity exige que cualquier partición que aísle parte del footprint de $g_k$ también tenga un bridge. Por tanto el caso genuinamente positivo no es simplemente:

$$
x_k\leftarrow g_k\rightarrow y_k,
$$

sino una estructura holística/co-constitutiva en la que el witness de génesis y los sectores continuados forman una unidad bajo OriginUnity.

GenesisConstitutiveUnity descarga exactamente la deuda de OriginUnity para la configuración child-side. Para elevarla a OntOrigin siguen siendo necesarias las demás cláusulas vigentes:

$$
\boxed{
\begin{aligned}
&\operatorname{ContextGenesis}^{\mathsf M}
\land
\operatorname{GenesisConstitutiveUnity}_k(\mathcal O_k;g_k)
\land
\operatorname{RootClosed}_k(\mathcal O_k)\\
&\land
\operatorname{GenAdequate}_k
\land
\operatorname{GCExists}_k(\mathcal O_k)
\land
\operatorname{Irredundant}_k(\mathcal O_k)\\
&\Rightarrow
\operatorname{OntOrigin}_k(\mathcal O_k).
\end{aligned}
}
$$

En este caso **no hace falta GenesisOrigin**: OntOrigin ya es suficientemente general.

#### 0.11.18. Test G2 — dependencia unilateral

Supóngase que la identidad/existencia de $y_k$ como continuación en $k$ depende de $g_k$ y del sector $X_k^{(i)}$, pero $x_k$ permanece constitutivamente independiente:

$$
\operatorname{EssConDep}_k(y_k;g_k\mid X_k^{(i)})
$$

mientras no existe dependencia constitutiva admisible desde ningún contenido del sector $X_k^{(i)}$ hacia el otro lado.

Entonces la partición que aísla el sector independiente carece de bilateralidad:

$$
\mathrm{NoConstitutiveBridge}_k
(X_k^{(i)},\,\operatorname{Seed}_k(\mathcal O_k)\setminus X_k^{(i)}),
$$

y por REV-07a:

$$
\boxed{
\neg\operatorname{OriginUnity}_k(\mathcal O_k).
}
$$

Interpretación: incorporación, asimilación, extensión o producción unilateral pueden ser ontológicamente novedosas **dentro de un contexto**, pero no justifican por sí solas el nacimiento de una nueva $R_k$ común. Si todo lo demás ya estaba tipado en un espacio previo, el caso pertenece a SharedOntSpace/ordinary OntProd; si no existe ese espacio, todavía falta una génesis constitutiva fuerte.

#### 0.11.19. Test G3 — relación pura entre continuaciones

Supóngase únicamente:

$$
\operatorname{PureOntRel}_k(\rho_k;\{x_k,y_k\}).
$$

POR4 impide usar la incidencia pura como orientación productiva hacia sus relata, y la regla ya fijada prohíbe usar PureOntRel por sí sola como ConstitutiveBridge de OriginUnity.

Luego:

$$
\boxed{
\operatorname{PureOntRel}_k(\rho_k;\{x_k,y_k\})
\not\Rightarrow
\operatorname{GenesisConstitutiveUnity}_k.
}
$$

Si se demuestra que $x_k$ y $y_k$, **como continuaciones en $k$**, dependen constitutivamente de esa estructura relacional, la instancia deja de ser pura en el sentido POR4 y debe clasificarse bajo CON/GRD/HC/RLC u otra familia productiva justificada.

Por tanto no existe aquí una “ontogénesis débil por relación”: o la relación descubre/ocurre dentro de SharedOntSpace, o adquiere fuerza constitutiva y el caso migra al test G1.

#### 0.11.20. Test G4 — mera coexistencia

Supóngase que hay realizaciones child-side de ambos precursores:

$$
x_i\rightsquigarrow x_k,
\qquad
y_j\rightsquigarrow y_k,
$$

pero ninguna estructura actual produce dependencia constitutiva cruzada suficiente.

Entonces la coexistencia por sí sola no crea OriginUnity:

$$
\boxed{
\operatorname{JointRealizable}^{\mathsf M}
\not\Rightarrow
\operatorname{ContextGenesis}^{\mathsf M}.
}
$$

Si $k$ preexistía, es SharedOntSpace. Si no puede exhibirse ni espacio previo ni witness constitutivo child-side, la teoría no autoriza introducir $k$ como nueva realidad por mera estipulación.

#### 0.11.21. Resultado de los cuatro tests

| Caso | Unidad parental | OriginUnity completa | Clasificación |
|---|---|---|---|
| G1 co-constitución holística | sí | sí, si toda partición tiene bridge | ontogénesis fuerte |
| G2 unilateral | no | no | extensión/asimilación, no nueva R común |
| G3 PureOntRel | no | no | SharedOntSpace o relación interna; si se vuelve constitutiva pasa a G1 |
| G4 coexistencia | no | no | SharedOntSpace/JointRealizable, no génesis |

Esto apoya la **No-Weak-Genesis Thesis**:

$$
\boxed{
\operatorname{GenuineContextGenesis}^{\mathsf M}
\Rightarrow
\operatorname{GenesisConstitutiveUnity}_k.
}
$$

No es todavía un teorema de lógica pura: es una decisión doctrinal fuertemente motivada por REV-07a. Su ventaja es que no necesita inventar GenesisOrigin y evita que cualquier novedad contextual nominal cuente como nueva realidad.

#### 0.11.22. Necesidad del indexamiento para la ontogénesis genuina

La ontogénesis también aclara por qué el indexamiento no es decoración.

Si todos los precursores, el supuesto mecanismo integrador y sus efectos ya son expresables en un único lenguaje objeto $L_i$, entonces la transformación puede representarse mediante OntProd/GenEvent **dentro de $i$**. No hay motivo suficiente para introducir un nuevo contexto:

$$
\operatorname{InternalFormation}_i
\not\Rightarrow
\operatorname{ContextGenesis}^{\mathsf M}.
$$

Para una génesis genuina exigimos **index novelty**:

$$
\boxed{
\operatorname{GenuineContextGenesis}^{\mathsf M}(C_i,C_j\Rightarrow k;\gamma)
\Rightarrow
k\not\simeq_{\mathrm{idx}} i
\land
k\not\simeq_{\mathrm{idx}} j
}
$$

para los precursores que realmente participan como contextos parentales distintos.

Cuando además $i\#j$, ningún evento objeto pre-child puede tener simultáneamente términos de ambos tipos. Por eso la relación de precursoridad debe permanecer metaontológica, mientras toda novedad ontológica efectiva aparece ya tipada en $k$.

La arquitectura queda:

$$
\boxed{
\begin{array}{c}
i\#j\\
\Downarrow\;\text{solo juicio meta de precursoridad}\\
\operatorname{ContextGenesis}^{\mathsf M}(i,j\Rightarrow k;\gamma)\\
\Downarrow\;\text{continuaciones tipadas + witness actual}\\
x_k,\;y_k,\;g_k\\
\Downarrow\;\operatorname{GenesisConstitutiveUnity}_k\\
\operatorname{OntOrigin}_k.
\end{array}
}
$$

Así $\gamma$ no es una entidad “entre realidades”. El índice hace exactamente el trabajo de impedir esa reificación: separa las ontologías parentales y obliga a que la convergencia novedosa se manifieste como una nueva estructura interna del hijo.

#### 0.11.23. FaithfulContinuation como relación meta, no función

La notación funcional previa:

$$
\kappa_{i\to k}:x_i\rightsquigarrow x_k
$$

se conserva solo como abreviatura cuando hay unicidad local. La noción general es relacional:

$$
\operatorname{FaithfulContinuation}^{\mathsf M}_{i\to k}
(x_i,x_k;\gamma,\tau).
$$

No es un predicado objeto cross-index. Afirma metateóricamente que, bajo una transición/génesis concreta $\gamma$, el token $x_k$ es una continuación de $x_i$ y que $\tau$ traduce la parte preservada de su perfil ontológico.

El contrato mínimo es:

1. **FC1 / typed endpoints:** $x_i$ está bien tipado en $i$ y $x_k$ en $k$; nunca aparecen juntos en una fórmula objeto.
2. **FC2 / provenance:** la relación depende de una historia de formación concreta; semejanza, isomorfismo o duplicación accidental no bastan.
3. **FC3 / derived prior profile:** existe un ContinuationProfile no trivial derivado source-side de una PersistenceSpec/PersistenceBasis independently grounded; §§0.11.91a–0.11.91j formalizan el criterio y prohíben seleccionar post hoc justo lo que $x_k$ conserva.
4. **FC4 / translated preservation:** para cada rasgo declarado preservado $\varphi_i$ del perfil, $\tau_{ik}(\varphi_i)$ vale de $x_k$.
5. **FC5 / genealogical commuting where preserved:** si una dependencia, relación o paso generativo del perfil tiene continuaciones declaradas para todos sus relata, la estructura correspondiente se preserva o se marca explícitamente como transformada.
6. **FC6 / permitted novelty:** $x_k$ puede adquirir hechos y dependencias nuevos, especialmente respecto de $g_k$; continuidad no significa copia total.
7. **FC7 / no retroactivity:** ningún hecho nuevo de $k$ cambia la verdad ontológica previa sobre $x_i$.
8. **FC8 / no index collapse:** FaithfulContinuation no implica $i\simeq_{\mathrm{idx}}k$ ni identidad cross-index.
9. **FC9 / recoding invariance:** recodificaciones fieles de padre e hijo preservan el juicio de continuación.
10. **FC10 / auditability:** debe poder indicarse qué perfil se preserva, qué se transforma y qué trayectoria de formación distingue continuidad de mera réplica.

Así:

$$
\operatorname{FaithfulContinuation}^{\mathsf M}_{i\to k}(x_i,x_k)
\not\Rightarrow
x_i=x_k
$$

—la igualdad ni siquiera pertenece al lenguaje objeto común— y tampoco:

$$
\operatorname{FaithfulContinuation}^{\mathsf M}_{i\to k}(x_i,x_k)
\not\Rightarrow
i\simeq_{\mathrm{idx}}k.
$$

La continuidad es **descendencia estructuralmente preservadora**, no identidad.

#### 0.11.24. Test F1 — copia perfecta

Sean $x_k$ y $z_k$ dos tokens child-side isomorfos respecto del perfil traducido de $x_i$. Supóngase que solo $x_k$ está dentro de la trayectoria de formación procedente de $x_i$:

$$
\operatorname{Provenance}^{\mathsf M}(x_i\leadsto_\gamma x_k),
\qquad
\neg\operatorname{Provenance}^{\mathsf M}(x_i\leadsto_\gamma z_k).
$$

Entonces:

$$
\operatorname{FaithfulContinuation}^{\mathsf M}_{i\to k}(x_i,x_k;\gamma,\tau)
$$

puede valer mientras:

$$
\neg
\operatorname{FaithfulContinuation}^{\mathsf M}_{i\to k}(x_i,z_k;\gamma,\tau).
$$

Por tanto:

$$
\boxed{
\text{isomorfismo}
\not\Rightarrow
\text{continuación}.
}
$$

FC2 impide que una réplica perfecta espontánea herede genealogía solo por parecerse al padre.

#### 0.11.25. Test F2 — branching

La continuidad no es funcional. Es admisible:

$$
\operatorname{FC}^{\mathsf M}_{i\to k}(x_i,x_k^{(1)};\gamma,\tau_1)
\land
\operatorname{FC}^{\mathsf M}_{i\to k}(x_i,x_k^{(2)};\gamma,\tau_2),
$$

con:

$$
x_k^{(1)}\neq x_k^{(2)}
$$

dentro del lenguaje de $k$.

No se concluye que los dos descendientes sean idénticos entre sí ni al parental. Ambos pueden preservar suficiente perfil y provenance para ser continuaciones genuinas.

El branching puede ocurrir internamente, dentro de un mismo contexto, o a través de génesis. No introduce ninguna necesidad de escoger una “continuación verdadera” única.

#### 0.11.26. Test F3 — merger token-level

También se admite continuidad many-to-one. Para precursores distintos:

$$
\operatorname{FC}^{\mathsf M}_{i\to k}(x_i,z_k;\gamma,\tau_i)
\land
\operatorname{FC}^{\mathsf M}_{j\to k}(y_j,z_k;\gamma,\tau_j)
$$

definimos esquemáticamente:

$$
\operatorname{TokenMerger}^{\mathsf M}
(x_i,y_j\Rightarrow z_k;\gamma).
$$

Para ser merger genuino y no mera coincidencia deben cumplirse al menos:

1. ambos precursores aportan perfiles no triviales preservados en $z_k$;
2. ambas provenances son necesarias para la historia de formación declarada;
3. la identidad child-side de $z_k$ no se explica íntegramente como continuación de una sola rama dejando a la otra como input contingente;
4. cualquier pérdida o transformación de perfil queda auditada.

TokenMerger es una propiedad de la **geometría de la continuidad**. No implica por sí sola ContextGenesis.

Puede haber un merger interno:

$$
a_i,b_i\Rightarrow z_i
$$

producido por OntProd dentro de un mismo $R_i$. Eso es fusión ontológica de contenido, no nacimiento de contexto.

A la inversa, una ContextGenesis fuerte puede conservar:

$$
x_i\rightsquigarrow x_k,
\qquad
y_j\rightsquigarrow y_k,
\qquad
x_k\neq y_k,
$$

y constituirlos conjuntamente mediante $g_k$ sin ningún TokenMerger.

Por tanto:

$$
\boxed{
\operatorname{TokenMerger}
\not\Rightarrow
\operatorname{ContextGenesis},
\qquad
\operatorname{ContextGenesis}
\not\Rightarrow
\operatorname{TokenMerger}.
}
$$

#### 0.11.27. Convergence como noción más amplia que genesis

Definimos Convergence como el metaschema en el que **dos o más líneas precursoras distintas** adquieren una integración común y existe un witness ontológico actual en el contexto donde esa integración queda tipada. Las líneas precursoras no tienen por qué ser dos índices finales incompatibles:

$$
\operatorname{Convergence}^{\mathsf M}
(B_a,B_b\leadsto k;w_k).
$$

El witness $w_k$ puede ser productivo, constitutivo o puramente relacional según el caso. Convergence por sí sola no afirma que $k$ haya nacido de ella.

Hay dos especies principales:

$$
\boxed{
\operatorname{Convergence}
=
\operatorname{SharedSpaceConvergence}
\lor
\operatorname{GenesisConvergence}.
}
$$

**SharedSpaceConvergence.** $k$ preexiste ontológicamente al hecho integrador. Dos genealogías/candidatos ya co-tipables en $k$ convergen dentro de ese mismo espacio. No se interpretan como dos contextos finales $i\#j$ que luego entran mágicamente en $k$:

$$
\operatorname{SharedSpaceConvergence}^{\mathsf M}
\Rightarrow
\operatorname{SharedOntSpace}^{\mathsf M}
\land
\neg\operatorname{ContextGenesis}^{\mathsf M}
$$

respecto de esa convergencia.

**GenesisConvergence.** La novedad conjunta de dos o más ramas es constitutiva de un nuevo $k$ y satisface GenesisConstitutiveUnity:

$$
\operatorname{GenesisConvergence}^{\mathsf M}
\Rightarrow
\operatorname{GenuineContextGenesis}^{\mathsf M}.
$$

Luego:

$$
\boxed{
\operatorname{Convergence}
\not\Rightarrow
\operatorname{ContextGenesis}.
}
$$

Esto conserva todo el trabajo previo sobre Integrable/JointRealizable: una convergencia observada puede revelar un SharedOntSpace sin crear realidad nueva.

#### 0.11.28. ContextGenesis no debe ser forzosamente binaria

La notación:

$$
\operatorname{ContextGenesis}^{\mathsf M}(C_i,C_j\Rightarrow k;\gamma)
$$

era el caso de prueba mínimo, no una restricción de aridad.

El esquema general permite uno o más contextos precursores:

$$
\operatorname{ContextGenesis}^{\mathsf M}
(i_1,\ldots,i_n\Rightarrow k;\gamma),
\qquad
n\ge 1,
$$

entendido metalingüísticamente como lista/esquema de instanciaciones y **no** como un conjunto ontológico de índices.

Esto distingue:

**Unary genesis**

$$
i\Rightarrow k.
$$

Un único contexto precursor sufre una reorganización ontológicamente constitutiva que exige un nuevo índice. No hay convergencia de contextos distintos.

**Multi-parent genesis**

$$
i_1,\ldots,i_n\Rightarrow k,
\qquad
n\ge 2.
$$

Si al menos dos ramas precursoras contribuyen constitutivamente a GenesisConstitutiveUnity, entonces:

$$
\boxed{
\operatorname{MultiParentContextGenesis}^{\mathsf M}
\Rightarrow
\operatorname{GenesisConvergence}^{\mathsf M}.
}
$$

Por tanto **no toda génesis es convergencia**:

$$
\boxed{
\operatorname{ContextGenesis}^{\mathsf M}
\not\Rightarrow
\operatorname{Convergence}^{\mathsf M},
}
$$

porque existe conceptualmente la génesis unaria.

Pero toda génesis multiparental genuina sí es una convergencia constitutiva.

#### 0.11.29. Context merger frente a token merger

Reservamos:

$$
\operatorname{ContextMerger}^{\mathsf M}
(i_1,\ldots,i_n\Rightarrow k;\gamma)
$$

como nombre de la especie multiparental de ContextGenesis: el nuevo contexto tiene al menos dos contextos parentales constitutivamente necesarios.

$$
\boxed{
\operatorname{ContextMerger}
\Longleftrightarrow
\operatorname{MultiParentContextGenesis}
\Rightarrow
\operatorname{GenesisConvergence}.
}
$$

ContextMerger no exige TokenMerger. Las imágenes de los padres pueden permanecer diferenciadas en $k$ y, aun así, participar conjuntamente en la OriginUnity del hijo.

TokenMerger, en cambio, pregunta si varias líneas de **contenido** acaban en un mismo token child-side.

Así:

$$
\boxed{
\text{context merger}
\neq
\text{token merger}.
}
$$

Pueden coincidir, pero ninguno define al otro.

#### 0.11.30. Test F4 — gradualidad / Ship of Theseus

La sustitución gradual no obliga por sí sola a introducir ContextGenesis.

Sea una secuencia dentro del mismo contexto:

$$
x_i^{(0)}
\rightsquigarrow
x_i^{(1)}
\rightsquigarrow
\cdots
$$

en la que cada estadio preserva un ContinuationProfile suficiente aunque cambie material o estructura accidental.

Mientras toda la evolución siga expresable en $L_i$ y no aparezca GenesisConstitutiveUnity que exija un nuevo tipado, tenemos persistencia/transformación interna:

$$
\operatorname{GradualContinuation}_i
\not\Rightarrow
\operatorname{ContextGenesis}^{\mathsf M}.
$$

La continuidad compuesta entre estadios no es automática: requiere que sobreviva un subperfil no trivial y que las transformaciones declaradas compongan sin contradicción. Por tanto FC no se postula transitiva sin condiciones.

Si en algún estadio una reorganización constitutiva produce un nuevo contexto $k$, la frontera de génesis se localiza allí:

$$
x_i^{(m)}
\rightsquigarrow
x_k^{(m+1)},
$$

y debe satisfacer las condiciones ordinarias de ContextGenesis/GenesisConstitutiveUnity. La pérdida de piezas o sustitución material acumulada, por sí sola, no crea un índice nuevo.

#### 0.11.31. Matriz final: continuidad, convergencia, merger y genesis

| Fenómeno | many-to-one token | ≥2 contextos precursores | nuevo índice | GenesisConstitutiveUnity |
|---|---:|---:|---:|---:|
| branching | no | no necesariamente | no necesariamente | no |
| TokenMerger interno | sí | no | no | no |
| SharedSpaceConvergence | no necesariamente | no necesariamente como índices finales | no | no |
| unary ContextGenesis | no necesariamente | no | sí | sí |
| ContextMerger | no necesariamente | sí | sí | sí |
| ContextMerger + TokenMerger | sí | sí | sí | sí |

Las inclusiones doctrinales relevantes son:

$$
\boxed{
\operatorname{ContextMerger}
=
\operatorname{MultiParentContextGenesis}
\subset
\operatorname{GenesisConvergence}
\subset
\operatorname{Convergence}.
}
$$

En cambio:

$$
\boxed{
\operatorname{TokenMerger}
\;\text{es ortogonal a}\;
\operatorname{ContextGenesis}.
}
$$

La ontogénesis se individua por **nuevo tipado + novedad constitutiva child-side**; convergence por reunión/integración de líneas; merger por cardinalidad many-to-one de continuaciones.
#### 0.11.32. Ship of Theseus ataca FC3, no el número de piezas

El principal adversario de FaithfulContinuation no es branching ni merger, sino el criterio de selección del ContinuationProfile.

FC3 exige un perfil no trivial fijado **antes** de evaluar al descendiente. Pero si se responde simplemente que algunas propiedades de $x_i$ son “las importantes”, reaparece la circularidad:

$$
\text{¿qué fija qué propiedades cuentan para la continuidad?}
$$

No es admisible seleccionar retrospectivamente justo los rasgos que un candidato $x_k$ conserva. Tampoco sirve un umbral extensional —porcentaje de partes, semejanza global, identidad material— porque una realidad/contexto puede ser internamente iterativa y admitir sustitución extensa de contenido sin perder por ello su identidad de contexto.

Por tanto Ship of Theseus deja una deuda nueva y precisa:

$$
\boxed{
\text{ContinuationProfile no puede seguir siendo primitivo.}
}

**Resolución posterior:** §§0.11.91a–0.11.91i derivan ContinuationProfile desde PersistenceBasis, memo-equivalence y quotient dynamics; esta deuda deja de permanecer abierta a nivel de criterio.
$$

Debe derivarse de una estructura independiente que determine qué transformaciones son internas a un contexto y qué roles ontológicos de sus contenidos deben preservarse a través de ellas.

#### 0.11.33. Realidad iterativa y ancla de identidad de contexto

Una realidad indexada no se identifica con una fotografía extensional de su contenido en un estadio:

$$
R_i\neq X_i^{(t)}.
$$

Debe poder admitir, en principio, iteraciones internas:

$$
X_i^{(0)}
\to
X_i^{(1)}
\to
X_i^{(2)}
\to\cdots
$$

mediante OntProd/GenEvent y otras transformaciones bien tipadas sin crear automáticamente un nuevo índice.

Esto exige distinguir:

1. **cambio de estado/contenido dentro de $i$**;
2. **continuidad de identidad del propio contexto $i$**;
3. **ruptura ontogénica que exige un nuevo índice $k$**.

El mero reemplazo acumulativo de constituyentes no decide esta frontera. Debe existir alguna estructura anterior al test de continuidad que determine qué transformaciones cuentan como iteraciones admisibles del mismo contexto.

#### 0.11.34. Candidato abierto: firma ontogénica $\Omega_i$

Introducimos **solo como candidato de trabajo**, todavía no como definición doctrinal cerrada:

$$
\boxed{
\Omega_i
:=
\operatorname{OntogenicSignature}_i.
}
$$

La intuición es que $\Omega_i$ no sea una lista libre de propiedades ni un snapshot del contenido, sino la estructura derivada de la ontología de $i$ que fija, al menos:

- qué formas de generación/transformación pertenecen a la iteración interna del contexto;
- qué invariantes o equivalencias estructurales preservan identidad contextual;
- qué roles ontológicos de los tokens son relevantes para su continuidad;
- qué cambios son meramente internos y cuáles rompen el tipado previo.

No se adopta todavía ninguna tupla concreta para $\Omega_i$. En particular, queda **abierto** si debe derivarse únicamente de OntOrigin, de OntOrigin + estructura generativa, de la clase de iteraciones admisibles o de otra construcción independiente.

La obligación central que motiva $\Omega_i$ es:

$$
\boxed{
\operatorname{ContinuationProfile}_i(x_i)
\stackrel{?}{=}
\operatorname{Proj}_{x_i}(\Omega_i).
}
$$

La igualdad es por ahora esquemática. Si prospera, resolvería la circularidad de FC3: el perfil de $x_i$ no se elegiría mirando al descendiente, sino que vendría impuesto por el papel que $x_i$ ocupa en la estructura ontogénica del contexto.

La dependencia conceptual candidata sería:

$$
\operatorname{OntOrigin}_i
\Longrightarrow
\Omega_i
\Longrightarrow
\operatorname{ContinuationProfile}_i(x_i)
\Longrightarrow
\operatorname{FaithfulContinuation}^{\mathsf M}.
$$

Cada flecha sigue siendo una obligación, no un teorema ya demostrado.

#### 0.11.35. Seed/origin y firma no deben colapsarse prematuramente

No se identifica:

$$
\operatorname{Seed}_i(\mathcal O_i)=\Omega_i.
$$

Las funciones conceptuales son distintas.

OntOrigin/Seed responde a la unidad fundacional de la genealogía:

$$
\text{¿por qué esta genealogía existe como una unidad?}
$$

La firma candidata respondería a su persistencia iterativa:

$$
\text{¿qué hace que transformaciones sucesivas sigan siendo del mismo contexto?}
$$

La hipótesis de trabajo más económica es que $\Omega_i$ esté **derivada** de la estructura originaria/generativa, no que sea un segundo primitivo independiente. Pero eso es precisamente lo que debe demostrarse al atacar $\Omega_i$.

#### 0.11.36. Evolución interna frente a ontogénesis

Si existe una noción adecuada de continuidad de firma:

$$
\operatorname{SigContinuation}^{\mathsf M}
(\Omega_i^{(a)},\Omega_i^{(b)}),
$$

entonces cambios extensos de contenido pueden permanecer dentro del mismo contexto mientras preserven la estructura que esa relación declare relevante.

Una ContextGenesis unaria tendría, en cambio, provenance desde $i$ hacia $k$ pero no continuidad suficiente de firma para conservar identidad contextual:

$$
\operatorname{Provenance}^{\mathsf M}(\Omega_i\leadsto\Omega_k)
\land
\neg\operatorname{SigContinuation}^{\mathsf M}(\Omega_i,\Omega_k)
\land
\operatorname{GenesisConstitutiveUnity}_k.
$$

Entonces:

$$
i\prec_{\mathrm{ctx}}k
\land
i\not\simeq_{\mathrm{idx}}k.
$$

Para genesis multiparental:

$$
\Omega_{i_1},\ldots,\Omega_{i_n}
\leadsto
\Omega_k,
$$

la nueva firma debe depender constitutivamente de aportes no triviales de varias ramas si el caso ha de ser ContextMerger.

Esta sección no define todavía SigContinuation: muestra qué problema debe resolver $\Omega_i$ para que la frontera evolution/genesis deje de ser estipulativa.

#### 0.11.37. Stress test observable: constantes y “magic numbers”

Las constantes observables proporcionan un adversario útil para no trivializar $\Omega_i$.

No se admite:

$$
\Omega_i
=
\{\text{lista de constantes observadas}\}
$$

por estipulación.

Un valor observable puede ser variable de estado, parámetro de una fase, parámetro efectivo, output derivado de una estructura más profunda o auténtico componente/invariante de la firma.

La pregunta relevante no es simplemente si cambia un número, sino:

$$
\boxed{
\text{¿su variación está permitida por la firma,
o modifica la estructura que determina el propio tipado?}
}
$$

Así la firma observable podría ser solo una **realización/compilación** de una estructura ontogénica más profunda:

$$
\Omega_i
\Longrightarrow
\text{estructura física efectiva}
\Longrightarrow
\text{parámetros/constantes observables}.
$$

Este ejemplo es solo un stress test metodológico. No se afirma que ninguna constante física concreta sea parte de $\Omega_i$ ni que las constantes conocidas individúen nuestra realidad.

#### 0.11.38. Revisión del orden provisional: $\Omega_i$ no puede presuponerse

La cadena propuesta inicialmente:

$$
\operatorname{OntOrigin}_i
\Longrightarrow
\Omega_i
\Longrightarrow
\operatorname{ContinuationProfile}_i(x_i)
\Longrightarrow
\operatorname{FaithfulContinuation}^{\mathsf M}
$$

queda **SUPERSEDED como orden de derivación provisional**. Ship of Theseus sigue mostrando que ContinuationProfile no puede ser primitivo, pero la analogía con constantes/magic numbers sugiere que $\Omega_i$ puede ser un **resultado baked/canónico** de estructura generativa ya constituida, no necesariamente la estructura previa que decide desde fuera qué debe preservarse.

Por tanto no se descarta $\Omega_i$; se pospone su definición hasta caracterizar qué información de un proceso parental puede ser trivializada al constituirse un nuevo contexto.

#### 0.11.39. Baking: un resultado puede sustituir a un proceso respecto de un rol

Considérese, solo esquemáticamente, un proceso/configuración parental $P_i$ cuya estructura determina una contribución estable. Una operación de baking no afirma identidad ontológica entre proceso y resultado:

$$
P_i\neq \sigma_k.
$$

Afirma metateóricamente que, respecto de cierto rol child-side, una realización $\sigma_k$ contiene lo suficiente para que la estructura interna completa de $P_i$ deje de ser necesaria en las dependencias posteriores relevantes de $k$.

Introducimos el candidato:

$$
\operatorname{GenesisTrivialization}^{\mathsf M}_{i\to k}
(P_i\Rightarrow\sigma_k;\gamma).
$$

Sus obligaciones mínimas son:

1. **GT1 / provenance:** $\sigma_k$ procede realmente de la rama parental $P_i$ bajo la formación $\gamma$; coincidencia o isomorfismo no bastan.
2. **GT2 / child actuality:** $\sigma_k$ y la estructura que porta son contenido actual bien tipado de $k$; el baking no crea una entidad cross-index.
3. **GT3 / child sufficiency:** toda dependencia child-side atribuida a esa rama parental factoriza, para el rol considerado, a través de $\sigma_k$; la estructura interna de $P_i$ deja de ser necesaria para ese uso.
4. **GT4 / screening-off:** diferencias internas entre realizaciones parentales que no alteran la firma child-side no alteran tampoco las consecuencias de $k$ que solo dependen de ese rol.
5. **GT5 / no retroactivity:** trivializar $P_i$ para $k$ no elimina, simplifica ni reescribe los hechos que eran reales en $i$.
6. **GT6 / recoding invariance:** la clasificación no depende de una codificación accidental del padre o del hijo.
7. **GT7 / no meta-reification:** Bake/Trivialization son juicios metateóricos sobre una formación real; no se postula una máquina ontológica entre índices.

La condición GT3 es la intuición central:

$$
\boxed{
\text{para el rol child-side considerado, }
P_i\text{ importa en }k\text{ solo mediante }\sigma_k.
}
$$

Esto formaliza la analogía con una constante precalculada: el valor puede sustituir operacionalmente al proceso exactamente en los contextos donde es suficiente su resultado, sin que proceso y valor sean ontológicamente idénticos.

#### 0.11.40. Trivialización conservativa y trivialización quotient

GenesisTrivialization no presupone que el baking sea invertible.

**Conservative trivialization.** La firma child-side conserva información suficiente para reconstruir, bajo una teoría de decodificación adecuada, la estructura parental relevante:

$$
P_i\mapsto\sigma_k
\qquad
\operatorname{Recoverable}^{\mathsf M}(P_i\mid\sigma_k).
$$

**Quotient trivialization.** Varias estructuras parentales distintas pueden realizar la misma contribución child-side:

$$
P_i\mapsto\sigma_k,
\qquad
Q_j\mapsto\sigma_k,
\qquad
P_i\not\simeq Q_j.
$$

Entonces la firma ya no determina unívocamente qué representante parental produjo esa contribución. La no-inyectividad no es por sí sola un defecto: puede ser precisamente la estructura de una convergencia.

#### 0.11.41. Equivalencia inducida por el hijo y SignatureConvergence

Para evitar una relación objeto cross-index, definimos solo el juicio meta:

$$
P_i\sim_k^{\mathsf M}Q_j
$$

cuando existe algún $\sigma_k$ tal que:

$$
\operatorname{GenesisTrivialization}^{\mathsf M}_{i\to k}
(P_i\Rightarrow\sigma_k;\gamma)
\land
\operatorname{GenesisTrivialization}^{\mathsf M}_{j\to k}
(Q_j\Rightarrow\sigma_k;\gamma).
$$

$P_i\sim_k^{\mathsf M}Q_j$ no dice que los padres fueran idénticos, compatibles ni co-tipables. Dice que el nuevo contexto **trivializa esa diferencia parental respecto del rol representado por $\sigma_k$**.

Definimos provisionalmente:

$$
\operatorname{SignatureConvergence}^{\mathsf M}
(P_i,Q_j\Rightarrow\sigma_k;\gamma)
$$

cuando dos o más ramas distintas convergen mediante quotient trivialization en una misma contribución child-side.

Así, el antiguo “problema de colisiones” se invierte:

$$
\boxed{
\operatorname{Bake}_{i\to k}(P_i)
=
\operatorname{Bake}_{j\to k}(Q_j)
\text{ puede ser el fenómeno de convergencia que debe explicar la teoría.}
}
$$

#### 0.11.42. Dos geometrías de GenesisConvergence

La trivialización permite distinguir al menos dos geometrías multiparentales.

**Collapse/signature convergence:**

$$
P_i,Q_j\Longrightarrow\sigma_k.
$$

Las diferencias parentales relevantes quedan identificadas para un rol del hijo. Esto puede manifestarse objeto-level como TokenMerger si varias continuaciones terminan en un mismo token $z_k$.

**Compositional convergence:**

$$
P_i\Longrightarrow\sigma_i^k,
\qquad
Q_j\Longrightarrow\sigma_j^k,
\qquad
\sigma_i^k\neq\sigma_j^k,
$$

y las dos contribuciones permanecen diferenciadas pero son constitutivamente necesarias para la GenesisConstitutiveUnity del hijo.

Por tanto:

$$
\boxed{
\operatorname{ContextMerger}
\not\Rightarrow
\operatorname{TokenMerger}.
}
$$

SignatureConvergence ofrece un posible mecanismo para TokenMerger, mientras la convergencia composicional conserva las ramas diferenciadas.

#### 0.11.43. Ontogénesis como cambio de resolución ontológica

La hipótesis fuerte que emerge no es que la génesis borre los padres, sino que **cambia qué diferencias siguen siendo operativas en el nuevo contexto**.

Una estructura parental puede requerir internamente:

$$
P_i=\{a_i,b_i,e_i,\rho_i,\ldots\}
$$

mientras la contribución child-side relevante queda representada por:

$$
P_i\Longrightarrow\sigma_{i\to k}^k.
$$

Las distinciones internas de $P_i$ siguen siendo verdaderas en $i$. Pero si GT3–GT4 valen, $k$ ya no necesita tratarlas separadamente para el rol trivializado.

Esto motiva interpretar parte de ContextGenesis como un **cambio de resolución ontológica**: el hijo hereda provenance, pero puede quotientar distinciones parentales.

Una tesis de trabajo más fuerte queda abierta:

$$
\boxed{
\textbf{Ontogenesis as Trivialization:}
\quad
\text{provenance}
+
\text{trivialización parental}
+
\text{GenesisConstitutiveUnity}
+
\text{nuevo tipado}.
}
$$

No se adopta todavía como bicondicional ni como condición necesaria de toda ContextGenesis; se registra como candidato explicativo que unifica continuidad, convergence, merger e index novelty.

#### 0.11.44. No-invertibilidad e horizonte genealógico

Si la trivialización es no inyectiva:

$$
P_i\sim_k^{\mathsf M}Q_j
$$

la firma child-side no contiene por sí sola información suficiente para decidir cuál fue el representante parental concreto.

Es posible entonces:

$$
\operatorname{Provenance}^{\mathsf M}(P_i\leadsto\sigma_k)
\land
\neg\operatorname{Reconstructible}^{\mathsf M}_k(P_i\mid\sigma_k).
$$

Esto separa dos nociones que FC no debe confundir:

$$
\boxed{
\text{provenance objetiva}
\neq
\text{reconstruibilidad interna de provenance}.
}
$$

Cuando las diferencias parentales necesarias para discriminar historias han sido quotientadas y ningún certificado de provenance sobrevive en $k$, aparece un candidato a **horizonte genealógico**: hechos verdaderos sobre la historia ontogénica pueden no ser recuperables desde la estructura child-side disponible.

#### 0.11.45. Consecuencia para FaithfulContinuation y FC10

FaithfulContinuation puede ser metateóricamente verdadera aunque el hijo no pueda certificar internamente toda la historia parental:

$$
\operatorname{FaithfulContinuation}^{\mathsf M}_{i\to k}(x_i,x_k)
\not\Rightarrow
\operatorname{InternallyReconstructible}_k(x_i\leadsto x_k).
$$

Por tanto FC10/auditability no debe exigir siempre reconstrucción child-side completa. Debe exigir una **justificación metateórica no circular y recoding-invariant** de la provenance y del perfil/trivialización afirmados. Si además existe evidencia child-side, esta puede reforzar la certificación, pero no forma parte necesaria de toda continuidad real.

Esto evita que una ontogénesis genuinamente no-inyectiva quede declarada imposible solo porque trivializó precisamente la información necesaria para invertirla.

#### 0.11.46. Trivialización, Muro y REC: conexión sin identificación

REC y el Muro conservan su distinción normativa.

REC sigue siendo consecuencia estructural de una totalidad de régimen ya establecida:

$$
\operatorname{RegimeTotal}_k(\mathfrak G_k,R_k)
\Rightarrow
\operatorname{REC}_k(R_k).
$$

GeneTotal hereda esta consecuencia como caso singleton.

Un certificador **real y ontológicamente exterior** a una totalidad genuina la refutaría como totalidad; por tanto no puede usarse como solución gratuita a una provenance perdida.

El Muro, en cambio, trata la subdeterminación desde evidencia interna/accesible. GenesisTrivialization aporta un candidato concreto a mecanismo de esa subdeterminación:

$$
\boxed{
\operatorname{GenesisTrivialization}
\land
\text{non-injectivity}
\Rightarrow
\text{possible internal genealogical underdetermination}.
}
$$

No se deriva con ello la versión fuerte de REV-15. La trivialización puede ser conservativa, o puede sobrevivir un certificado child-side $c_k$ que desambigüe provenance. Pero cuando el quotient elimina la distinción y no queda tal certificado, la imposibilidad reconstructiva deja de ser mero desconocimiento contingente y pasa a estar motivada por la propia estructura de la génesis.

Así pueden coexistir:

$$
\boxed{
\text{provenance objetiva}
+
\text{no reconstruibilidad interna}
+
\text{ausencia de certificador real exterior admisible}.
}
$$

#### 0.11.47. Reubicación de $\Omega_i$

Después de la hipótesis de trivialización, $\Omega_i$ ya no debe suponerse anterior al baking. Un candidato más informativo es que la firma ontogénica sea una representación canónica de la estructura generativa **módulo las diferencias que el propio contexto trivializa**:

$$
\boxed{
\Omega_i
\stackrel{?}{=}
\operatorname{Bake}^{\mathsf M}
\left(
\mathcal G_i/\!\sim_i
\right).
}
$$

Esta expresión sigue siendo esquemática: ni $\mathcal G_i/\!\sim_i$ se asume como quotient set-theoretic ni los índices se convierten en objetos. Su función es fijar el nuevo orden de investigación:

$$
\boxed{
\operatorname{OntOrigin}_i
\Longrightarrow
\text{estructura generativa/iterativa}
\Longrightarrow
\text{trivializaciones admisibles }\sim_i
\Longrightarrow
\Omega_i
\Longrightarrow
\operatorname{ContinuationProfile}_i
\Longrightarrow
\operatorname{FaithfulContinuation}^{\mathsf M}
}
$$

fue una **ruta provisional**. Queda SUPERSEDED por §§0.11.91a–0.11.92: ContinuationProfile se deriva sin $\Omega_i$, a partir de PersistenceBasis + contract state + memo-equivalence + quotient dynamics; FaithfulContinuation usa después un ProfileMorphism + provenance. $\Omega_i$ permanece PARTIAL como posible canonicalización posterior de estructura generativa + perfiles + Bake/Prov data, nunca como premisa necesaria de FC3.

La deuda vigente de $\Omega_i$ es por tanto distinta: decidir si una familia contextualmente suficiente de perfiles y estructura generativa admite una normal form canónica sin reificar $R_i$, borrar provenance relevante ni usarse retroactivamente para ContextIndividuation.

#### 0.11.48. REV-07g — Cellular Reality: la individuación precede al índice

La arquitectura vigente permite formular una hipótesis más precisa que la antigua intuición de «realidad fractal»: una realidad indexada puede tratarse **estructuralmente como una unidad celular** si la analogía se descarga en condiciones formales de individuación, frontera, persistencia y ontogénesis. «Celular» no significa aquí biológico, espacial ni microscópico.

La primera corrección es de orden explicativo:

$$
\boxed{
\text{individuación}
\Longrightarrow
\text{tipado/contexto}
\Longrightarrow
\text{ascripción del metavariable }i,
}
$$

no:

$$
i\Longrightarrow\text{individuación}.
$$

EXT-02 ya impide convertir $i$ en una entidad o miembro de un dominio de índices. REV-07g añade que el índice tampoco debe cargar con la tarea metafísica de **crear** la diferencia que etiqueta. Si dos candidatos resultan ser realizables dentro del mismo espacio ontológico preexistente, SharedOntSpace obliga a retirar la separación provisional; si una ContextGenesis constituye una unidad nueva, el nuevo índice registra esa novedad después de justificarla.

Introducimos por ello, solo como obligación metateórica abierta, un testigo pre-indexado:

$$
\operatorname{IndividuationWitness}^{\mathsf M}(C;\chi).
$$

$C$ es aquí una **presentación/candidatura metateórica pre-indexada**: no se presupone todavía que corresponda a una única unidad ontológica. $\chi$ no es una pieza adicional de realidad. Para que el testigo no sea una renominación del índice debe satisfacer al menos:

1. **CI1 / pre-indexación:** su definición no usa $\operatorname{Real}_i$, SameRegime$_i$, $R_i$ ni la mera existencia del índice que pretende justificar;
2. **CI2 / no extensionalidad instantánea:** no identifica el contexto con un snapshot o con la lista actual de sus componentes;
3. **CI3 / poder de tipado:** explica por qué cierto contenido puede entrar en una misma semántica objeto y por qué otro contenido exigiría reindexación;
4. **CI4 / anclaje generativo:** es compatible con OntOrigin, OntProd/GenEvent, RegimeClosure y la distinción SharedOntSpace/ContextGenesis;
5. **CI5 / persistencia no post hoc:** no se selecciona retrospectivamente para hacer verdadera una FaithfulContinuation concreta;
6. **CI6 / invariancia de recodificación:** representaciones isomorfas del mismo soporte ontológico no producen individuaciones distintas por accidente notacional;
7. **CI7 / granularidad no arbitraria:** si dos testigos admisibles inducen cortes incompatibles sobre la misma presentación, la teoría debe justificar que corresponden a niveles distintos o demostrar su equivalencia; no puede elegir el corte que convenga al argumento;
8. **CI8 / anti-agregación:** una suma descriptiva de unidades ya individuadas no obtiene una nueva individuación solo porque pueda encerrarse en una presentación común.

La relación entre $\chi$ y $\Omega_i$ queda deliberadamente asimétrica. $\chi$ pretende descargar la deuda **pre-indexada** de por qué hay una unidad contextual; $\Omega_i$ sigue siendo un candidato **post-individuación** a representación canónica de la estructura generativa/iterativa módulo trivializaciones admisibles. Por tanto no se identifica:

$$
\chi=\Omega_i.
$$

Una ruta de investigación compatible con §0.11.47 es:

$$
\boxed{
\operatorname{IndividuationWitness}^{\mathsf M}(C;\chi)
\Longrightarrow
\text{contexto tipado }i
\Longrightarrow
\text{estructura generativa/iterativa}_i
\Longrightarrow
\Omega_i.
}
$$

Las flechas son obligaciones; no se afirma todavía el teorema.

#### 0.11.49. La «membrana» es un perfil estratificado, no una pared única

La sugerencia:

$$
\text{membrana}
\stackrel{?}{=}
\text{typing boundary}+\text{Muro}+\text{REC}
$$

captura una intuición importante, pero las tres piezas tienen tipos y direcciones lógicas distintos. Colapsarlas en un único predicado primitivo destruiría precisamente las distinciones ganadas por REV-15, EXT-01 y EXT-02.

REV-07g usa **membrana** solo como nombre de trabajo para un perfil de frontera con cuatro capas:

1. **TB / frontera de tipado.** Una vez individuado $i$, $\mathcal L_i$ determina qué términos y predicados forman fórmulas objeto bien tipadas. Para $i\#j$, un supuesto hecho objeto transversal no es falso sino mal tipado.
2. **OC / clausura de alcance.** Si se demuestra $\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)$, el scope es genealógicamente exhaustivo para ese régimen. De aquí se obtiene REC como consecuencia estructural; REC no individúa el contexto ni demuestra su existencia.
3. **EB / frontera epistémica.** El Muro mínimo impide inferir exhaustividad ontológica desde la mera ausencia de una extensión accesible de $U_i$. La versión fuerte sigue OPEN en REV-15.
4. **IF / interfaces ontogénicas.** La frontera no es impermeabilidad absoluta. ContextGenesis, FaithfulContinuation, Provenance y GenesisTrivialization permiten relaciones **metateóricas** entre contextos sin introducir hechos objeto cross-index.

Esquemáticamente:

$$
\boxed{
\partial^{\mathrm{cell}}_i
\sim
\langle
\mathrm{TB}_i,
\mathrm{OC}_i,
\mathrm{EB}_i,
\mathrm{IF}_i
\rangle,
}
$$

pero $\partial^{\mathrm{cell}}_i$ no se introduce todavía como objeto de la ontología ni la tupla como definición literal. Es un bookkeeping metateórico para impedir tres colapsos:

$$
\mathrm{TB}\neq\mathrm{REC},
\qquad
\mathrm{REC}\neq\mathrm{Muro},
\qquad
\mathrm{Muro}\neq\mathrm{IF}.
$$

La analogía celular mejora así: una membrana no es simplemente «lo que aísla», sino la estructura que mantiene una individuación mientras regula qué tipos de continuidad, intercambio o génesis son admisibles. La analogía con semipermeabilidad física termina aquí: para $i\#j$ **no hay import/export objeto de tokens entre contextos**. Una continuación child-side es contenido nuevamente tipado en el hijo, no el mismo token cruzando una pared. Además, RegimeClosure es clausura generativa de la propuesta y no debe identificarse sin argumento con la «closure of constraints» de la biología teórica.

#### 0.11.50. Qué haría no trivial a Cellular Reality

Si «célula» significase solo:

$$
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
+
\operatorname{REC}_i(R_i)
+
\text{tipado},
$$

REV-07g sería una abreviatura decorativa: REC ya sigue de RegimeTotal y el tipado ya pertenece a la arquitectura indexada.

La tesis solo añade contenido si obliga a resolver la **individuación diacrónica**. El candidato fuerte es:

$$
\operatorname{RealityCell}^{\mathsf M}(i)
$$

como clasificación metateórica de una realización que dispone de:

- fundamento no circular de individuación;
- frontera de tipado estable;
- clausura generativa suficiente para RegimeTotal;
- criterio de persistencia bajo transformación interna;
- interfaces tipadas para génesis/convergencia;
- y, si se pretende hablar de destrucción o muerte, un criterio positivo de cesación.

Por tanto:

$$
\boxed{
\text{Cellular Reality}
\text{ no se cierra con RegimeTotal; hereda el problema de identidad de REV-07e.}
}
$$

Esto explica por qué Ship of Theseus no era un problema lateral. En una lectura celular, es exactamente el ataque a la pregunta «¿qué hace que esta unidad siga siendo esta unidad mientras cambia casi todo su contenido?».

#### 0.11.51. Ciclo ontogénico: metabolismo, budding, fission, fusion y cesación

La arquitectura actual ya contiene casi todas las operaciones necesarias para hablar de un ciclo celular sin añadir hechos cross-index.

**Transformación interna / metabolismo ontológico.** OntProd/GenEvent y RegimeClosure pueden cambiar ampliamente el contenido sin cambiar automáticamente de índice:

$$
X_i^{(a)}
\leadsto
X_i^{(b)}.
$$

**Budding.** Una ContextGenesis puede producir un hijo $k$ mientras una realización del padre sigue co-realizada. PersistentParent es entonces evidencia de coexistencia padre–hijo y bloquea inferir $i\#k$ por mera descendencia.

**Fusion.** ContextMerger es el análogo estructural de fusión: varias ramas parentales son constitutivamente necesarias para una unidad $k$. Sigue sin implicar TokenMerger.

**Fission/division.** El branching de continuaciones puede producir varios descendientes. Para llamarlo división fuerte, sin embargo, no basta con que existan $k_1,k_2$: hace falta además explicar qué ocurre con la identidad parental.

Esto abre una deuda que la teoría actual no posee:

$$
\boxed{
\operatorname{ContextCessation}^{\mathsf M}(i;\delta).
}
$$

No se define por negación:

$$
\neg\operatorname{PersistentParent}^{\mathsf M}(i,k)
\not\Rightarrow
\operatorname{ContextCessation}^{\mathsf M}(i).
$$

La ausencia de un testigo de persistencia puede ser mera falta de información, exactamente el tipo de inferencia que el Muro obliga a tratar con cuidado. Una futura condición positiva de cesación deberá cumplir al menos:

1. **CCe1 / witness positivo:** existir una base metateóricamente justificable para afirmar terminación, no mero fracaso de reconstrucción;
2. **CCe2 / no retroactividad:** cesar no vuelve irreales los hechos históricos de $i$ ni reescribe su provenance;
3. **CCe3 / descendencia compatible:** un hijo puede persistir aunque el padre cese;
4. **CCe4 / separación de quotient:** pérdida de reconstructibilidad por GenesisTrivialization no cuenta por sí sola como muerte del padre;
5. **CCe5 / compatibilidad temporal:** la definición debe coordinarse con la semántica procesual antes de introducir instantes terminales ad hoc.

Hasta cerrar esta deuda, decir que un $R_i$ puede «ser destruido» solo puede significar provisionalmente **cesación de su continuación contextual**, no borrado ontológico de todo lo que fue real en $i$.

#### 0.11.52. Fractalidad pasa a ser una tesis secundaria

REV-13 cerró correctamente el uso argumental de «fractal» porque no había patrón, escala ni métrica de autosimilitud. Cellular Reality no reabre ese defecto.

La implicación:

$$
\operatorname{CellularReality}
\Rightarrow
\operatorname{FractalReality}
$$

**no** está justificada.

Para recuperar una tesis fractal harían falta, como mínimo:

1. una relación tipada de anidamiento o embedding entre contextos que no colapse en mero subdominio del mismo $i$;
2. recurrencia de una misma arquitectura de individuación/frontera en varios niveles;
3. un criterio explícito de similitud estructural;
4. una noción de escala o jerarquía respecto de la cual esa recurrencia sea no trivial.

En ausencia de eso, la relación correcta es metodológica:

$$
\boxed{
\text{celularidad}
\quad\text{puede generar una arquitectura recursiva;}
\quad
\text{fractalidad exigiría demostrar además autosimilitud.}
}
$$

Así «realidad celular» es conceptualmente anterior y más débil que «realidad fractal». Una realidad podría estar individuada en células contextuales, con génesis, fusión y cesación, sin exhibir ninguna autosimilitud.

#### 0.11.53. Stress tests de la lectura celular

**C1 — sandbox opaca.** Un dominio puede imitar el Muro porque ningún observador interno ve un exterior. Si no hay RegimeTotal ni fundamento independiente de individuación, eso no basta para convertirlo en RealityCell. La opacidad no crea membrana ontológica.

**C2 — subsistema ordinario.** Una región o subsistema dentro de $R_i$ puede poseer una frontera física nítida y seguir siendo contenido de $i$. Una boundary espacial no produce por sí sola un nuevo contexto.

**C3 — SharedOntSpace.** Dos candidatos provisionales aparentemente separados que admiten realizabilidad conjunta en un espacio preexistente no son dos células ontológicas por decreto. Deben re-tiparse dentro de la unidad común.

**C4 — child con padre persistente.** $i\prec_{\mathrm{ctx}}k$ y PersistentParent pueden coexistir. Por tanto la individuación de $k$ no exige que $i$ sea destruido ni que padre e hijo sean mutuamente exteriores en sentido espacial.

**C5 — quotient convergence.** Si $P_i\sim_k^{\mathsf M}Q_j$, el hijo puede trivializar diferencias parentales sin que $i$ y $j$ se vuelvan retrospectivamente la misma célula. La igualdad de una contribución baked no es identidad de contexto.

**C6 — reemplazo total de componentes.** Sustituir todos los tokens de una realización a lo largo de una historia no decide por sí solo si el índice persiste. Este test sigue abierto hasta que $\chi$, $\Omega_i$ y ContinuationProfile queden coordinados sin circularidad.

**C7 — coarse-graining rival.** Una misma presentación puede admitir dos particiones descriptivas igualmente cómodas. Si $\chi_1$ individúa «células» finas y $\chi_2$ unidades gruesas, la teoría no puede convertir ambas en índices ontológicos por conveniencia. Debe mostrar que una de las particiones carece de CI1–CI8, que ambas representan niveles ontológicos genuinamente distintos mediante una futura relación de embedding, o que son metateóricamente equivalentes. Este es el ataque principal contra una celularidad meramente perspectival.

#### 0.11.54. Estado de REV-07g

REV-07g queda **PARTIAL / hipótesis arquitectónica**.

Lo ya obtenido es una descomposición útil:

$$
\boxed{
\text{individuación}
\rightarrow
\text{índice/tipado}
\rightarrow
\text{RegimeTotal/REC}
}
$$

junto con una capa epistémica separada —Muro— y una capa de interfaces ontogénicas —ContextGenesis/FC/Provenance/Trivialization—.

Lo que todavía falta para convertir Cellular Reality en extensión formal fuerte es:

1. definir $\operatorname{IndividuationWitness}^{\mathsf M}$ sin reutilizar el índice ni RegimeTotal de forma circular;
2. demostrar que ese fundamento induce una frontera de tipado suficientemente determinada y no depende de un coarse-graining arbitrario;
3. cerrar la identidad diacrónica coordinando $\chi$, trivialización, $\Omega_i$ y ContinuationProfile;
4. dar un criterio positivo de ContextCessation;
5. decidir si existe una relación legítima de embedding/nesting entre contextos y cómo se distingue de una partición puramente descriptiva;
6. solo entonces reevaluar si alguna subclase de arquitecturas celulares satisface un criterio real de fractalidad.

La tesis central queda, por ahora:

$$
\boxed{
\textbf{Indexing is the notation of individuation, not its source.}
}
$$

y la membrana deja de ser metáfora si se entiende como **perfil de frontera tipada, clausura, epistemología e interfaces**, manteniendo esas capas formalmente separadas.

#### 0.11.55. Auditoría de dependencias: la maquinaria vigente todavía no deriva la individuación inicial

REV-07g permite formular una pregunta más dura: ¿puede $\chi$ eliminarse en favor de nociones ya presentes?

La respuesta actual es **no, no globalmente**. Cada candidato existente falla por una razón distinta.

**ContextUnity / JointRealizable es demasiado débil.**

$$
\operatorname{ContextUnity}^{\mathsf M}(C_a,C_b)
:=
\operatorname{JointRealizable}^{\mathsf M}(C_a,C_b)
$$

solo prueba realizabilidad conjunta. §0.11.6 ya mostró que una integración estable puede revelar SharedOntSpace o constituir ContextGenesis. Por tanto JointRealizable no decide por sí solo si hay una unidad preexistente.

**GeneUnity / CommonGround es demasiado fuerte.** REV-07f permite una $R_i$ multigeneal con varias GeneUnit independientes. Exigir common ground global volvería a introducir monogeneidad por la puerta de atrás.

**RegimeTotal llega demasiado tarde.** La fórmula:

$$
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
$$

ya presupone que $\mathfrak G_i$ es una GeneBasis tipada en **el mismo contexto $i$**. No puede explicar sin circularidad por qué ese $i$ era una unidad.

**REC llega aún más tarde.** Es consecuencia de RegimeTotal y, por tanto, no puede fundamentar el corte que RegimeTotal ya presupone.

**El Muro tiene la dirección equivocada.** Restringe inferencias epistemológicas desde $U_i$; una sandbox opaca puede satisfacer el patrón epistémico sin ser una unidad ontológica total.

**$\Omega_i$ es post-individuación.** §0.11.47 la reubica como posible representación canónica de estructura generativa módulo trivialización. Usarla para crear el contexto cuyo historial debe resumir sería circular.

**GenesisConstitutiveUnity sí explica algo, pero solo localmente.** Puede justificar la unidad child-side de una génesis concreta; no explica por sí sola la individuación de un contexto preexistente que no se esté tratando como hijo de una ContextGenesis conocida.

El resultado de dependencia es:

$$
\boxed{
\text{la doctrina actual presupone una noción de identidad/unidad de contexto
que todavía no reduce a sus demás predicados.}
}
$$

Esto no es una inconsistencia. Es exactamente la deuda que ya anunciaba el estado normativo al exigir justificar independientemente «qué hace que dos dominios pertenezcan al mismo régimen $i$». REV-07g la aísla ahora como problema de **individuación contextual**.

#### 0.11.56. Metavariable provisional frente a índice admitido

Hay una circularidad aparente en ContextGenesis:

1. para probar GenesisConstitutiveUnity escribimos ya $x_k,g_k,\operatorname{OriginUnity}_k$;
2. pero el propósito de esa prueba es precisamente justificar que existe un contexto nuevo $k$.

La salida no es eliminar el tipado provisional, sino distinguir su estatus lógico.

Usaremos esquemáticamente:

$$
\widehat{k}
$$

para un **parámetro de prueba provisional**. Permite comprobar si una candidatura child-side es internamente tipable y satisface las obligaciones de unidad, pero no afirma todavía que se haya admitido un nuevo contexto ontológico.

Por tanto:

$$
\boxed{
\text{usar }\widehat{k}\text{ para chequear una candidatura}
\not\Rightarrow
\text{haber justificado }k.
}
$$

La descarga final sería un juicio metateórico, no un evento objeto:

$$
\operatorname{IndexAdmission}^{\mathsf M}
(C_{\widehat{k}}\Downarrow k;\chi).
$$

Este juicio no introduce a $k$ como miembro de un dominio de índices. Registra que la candidatura provisional ha satisfecho un criterio de individuación suficiente para que el metalenguaje use en adelante $k$ como metavariable de contexto admitida.

La secuencia conceptual correcta pasa a ser:

$$
\boxed{
C
\xrightarrow{\text{provisional typing}}
C_{\widehat{k}}
\xrightarrow{\chi}
\operatorname{IndexAdmission}^{\mathsf M}(C_{\widehat{k}}\Downarrow k)
\xrightarrow{}
\text{investigación de RegimeTotal}_k.
}
$$

Así se conserva la intuición de que el índice es consecuencia de individuación sin exigir que la individuación se formule en un lenguaje completamente carente de tipos. Lo prioritario es la **justificación** del tipo, no la inexistencia de scaffolding tipado durante la prueba.

#### 0.11.57. La ontogénesis puede descargar parte de $\chi$; SharedOntSpace no

Para un hijo genuinamente constituido, la maquinaria ya ofrece un candidato parcial de individuación:

$$
\chi^{\mathrm{gen}}_{\widehat{k}}
:=
\langle
g_{\widehat{k}},
\operatorname{GenesisConstitutiveUnity}_{\widehat{k}},
\operatorname{OntOrigin}_{\widehat{k}},
\operatorname{NoInternalFormation}
\rangle,
$$

entendido otra vez como esquema metateórico y no como tupla-objeto.

La pieza decisiva es combinar:

1. unidad constitutiva child-side;
2. OntOrigin no retroactivo;
3. el test de §0.11.22: si toda la formación es representable como OntProd/GenEvent interno de un precursor, no hay motivo para admitir un índice nuevo;
4. CI6–CI8: invariancia de recodificación, granularidad no arbitraria y anti-agregación.

Esto sugiere una regla candidata:

$$
\boxed{
\operatorname{GenuineContextGenesis}^{\mathsf M}
+
\chi^{\mathrm{gen}}_{\widehat{k}}
\Longrightarrow
\operatorname{IndexAdmission}^{\mathsf M}
(C_{\widehat{k}}\Downarrow k).
}
$$

No se declara todavía teorema porque NoInternalFormation y la unicidad/granularidad de la individuación necesitan una semántica independiente.

El caso SharedOntSpace es más difícil. Precisamente porque puede ser multigeneal:

$$
\operatorname{SharedOntSpace}^{\mathsf M}
\not\Rightarrow
\operatorname{CommonGround}^{\mathsf M},
$$

ni OriginUnity global ni una génesis child-side pueden fundar su unidad. Hace falta una noción adicional de **Native/ambient Context Individuation** que explique por qué varias genealogías pertenecen a un mismo espacio previo sin definirlo simplemente como «todo lo que hemos decidido tipar junto».

Esto divide REV-07g en dos deudas:

$$
\boxed{
\begin{array}{ll}
\text{GI:} & \text{individuación por génesis — parcialmente descargable con REV-07e;}\\
\text{AI:} & \text{individuación de espacio preexistente — todavía abierta.}
\end{array}
}
$$

La segunda es la deuda fundamental. Si AI no se resuelve, SharedOntSpace sigue siendo una noción bien tipada para razonar condicionalmente, pero la teoría no posee todavía un criterio no circular completo para **descubrir** dónde termina una unidad contextual preexistente y empieza otra.

#### 0.11.58. Resultado: Cellular Reality localiza el verdadero problema de identidad

La principal ganancia de REV-07g no es haber demostrado que la realidad «es una célula». Es haber separado tres preguntas que antes podían confundirse:

$$
\boxed{
\begin{aligned}
\text{Individuación sincrónica:}&\quad
\text{¿por qué esto cuenta como una unidad contextual?}\\
\text{Persistencia diacrónica:}&\quad
\text{¿por qué sigue siendo la misma unidad tras cambiar?}\\
\text{Ontogénesis:}&\quad
\text{¿cuándo una transformación constituye una unidad nueva?}
\end{aligned}
}
$$

La arquitectura vigente tiene respuestas parciales muy distintas:

- **sincronía:** abierta en el caso SharedOntSpace/ambient;
- **persistencia:** abierta en FC3/$\Omega_i$/trivialización;
- **ontogénesis:** bastante más desarrollada mediante ContextGenesis + GenesisConstitutiveUnity + No-Weak-Genesis.

Por tanto no conviene introducir un nuevo primitivo CellIdentity. El target más económico es fortalecer una única familia metateórica de juicios de **ContextIndividuation**, de la que la admisión del índice sea una salida representacional:

$$
\boxed{
\operatorname{ContextIndividuation}^{\mathsf M}
\Longrightarrow
\operatorname{IndexAdmission}^{\mathsf M}.
}
$$

Después:

$$
\operatorname{IndexAdmission}^{\mathsf M}
\not\Rightarrow
\operatorname{RegimeTotal},
$$

porque haber individuado un contexto no demuestra todavía que su GeneBasis, RegimeClosure y scope total existan. Esto mantiene limpia la jerarquía:

$$
\boxed{
\text{individuación}
<
\text{tipado admitido}
<
\text{totalización de régimen}
<
\text{REC}.
}
$$

El Muro permanece ortogonal como restricción epistemológica.

En consecuencia, **Cellular Reality es útil incluso si el nombre se abandona después**: ha revelado que la deuda de identidad de REV-07 no es una sola. La teoría distingue ahora nacimiento, persistencia y unidad sincrónica, y el agujero más profundo está en la última para contextos preexistentes multigeneales.

#### 0.11.59. La ruta pre-ontológica no puede fabricar individuación contextual

La clausura generalizada \(\mathcal C_*\) parece a primera vista un candidato natural para AI porque se construye antes de fijar un índice. Esa lectura es incorrecta.

Por diseño:

\[
T_q^{\mathcal C}
:=
\mathcal C_*(\{q\})
\]

es solo un carrier candidato relativo a reglas \(\mathfrak G_*\) independientes. El teorema:

\[
\mathrm{CSet}
+
\mathrm{CProcStable}
+
\mathrm{CWF}
+
\mathrm{SigSmall}_{\mathcal C}
+
\mathrm{ActualSep}_{\mathcal C}
\Rightarrow
\operatorname{SemTotal}_{\mathcal C}(S_q^{\mathcal C})
\]

es explícitamente pre-ontológico. No contiene SameRegime, CoReal, StructAdm\(_i\), CS, CC ni un juicio de identidad de contexto.

El salto ontológico aparece solo después mediante:

\[
\eta_i^{\mathcal C}:
T_q^{\mathcal C}
\rightsquigarrow
\{x_i\},
\]

junto con CS\({}^{gen}_{\mathcal C,i}\), CC\({}^{gen}_{\mathcal C,i}\), RA y las obligaciones de realización de scope.

Por tanto usar ahora \(\mathcal C_*\) para **definir** el contexto \(i\) invertiría la dependencia:

\[
\mathcal C_*
\Longrightarrow
i
\Longrightarrow
\eta_i^{\mathcal C},
\]

cuando la arquitectura vigente solo autoriza:

\[
\mathcal C_*
+
\eta_i^{\mathcal C}
+
\text{adecuación ontológica}
\Longrightarrow
\text{reconstrucción dentro de }i.
\]

La conclusión es:

\[
\boxed{
\operatorname{SemTotal}_{\mathcal C}
\not\Rightarrow
\operatorname{ContextIndividuation}^{\mathsf M}.
}
\]

Esto no es una nueva limitación de la Ruta B; preserva exactamente la separación por la que fue construida. Una clausura semántica puede ser matemáticamente exhaustiva respecto de su carrier y seguir sin decir por qué ese carrier corresponde a **una** unidad ontológica en vez de a una selección representacional.

#### 0.11.60. SharedOntSpace tampoco descarga AI: presupone una instanciación común

La formulación vigente dice:

\[
\operatorname{SharedOntSpace}^{\mathsf M}(C_a,C_b;k)
\]

cuando existe una **instanciación admisible \(k\)** en la que ambos candidatos tienen realizaciones fieles y su coexistencia no depende constitutivamente del hecho integrador usado para descubrirla.

Esto es correcto como criterio **relativo a una unidad contextual ya disponible**. Pero precisamente por contener \(k\) no puede servir como explicación última de la admisibilidad de \(k\).

REV-07g obliga a distinguir dos preguntas:

\[
\boxed{
\begin{aligned}
\text{coalescencia local:}&\quad
\text{¿deben }C_a,C_b\text{ tratarse dentro del mismo contexto?}\\
\text{individuación global:}&\quad
\text{¿qué hace que ese contexto sea una unidad y dónde termina?}
\end{aligned}
}
\]

SharedOntSpace puede aportar evidencia fuerte para la primera. No responde automáticamente a la segunda.

En particular, cerrar transitivamente una relación de co-realizabilidad tampoco resuelve el problema:

\[
\operatorname{JointRealizable}^{\mathsf M}
\stackrel{*}{\longrightarrow}
\text{contexto}
\]

reintroduciría por otra vía la vieja idea de que conectividad/amalgamabilidad **define** SameRegime. El documento ya la rechazó: la conectividad solo puede reconstruir una unidad caracterizada independientemente.

Tampoco puede elegirse un contexto maximal bajo JointRealizable. Además de revivir REV-08, la maximalidad sería una propiedad de una familia de candidatos, no una explicación de por qué el corte maximal obtenido es una unidad ontológica bona fide.

#### 0.11.61. Resultado de no-reducción arquitectónica para AI

Con el vocabulario actualmente disponible, los candidatos se reparten así:

| Recurso | Por qué no descarga AI |
|---|---|
| OntOrigin / GeneUnit | demasiado local; varias genealogías independientes pueden compartir contexto |
| CommonGround / GeneUnity | demasiado fuerte; excluiría el SharedOntSpace multigeneal de REV-07f |
| JointRealizable / ContextUnity | demasiado débil; no decide SharedOntSpace frente a ContextGenesis |
| SharedOntSpace | ya cuantifica sobre una instanciación común admisible |
| \(\mathcal C_*\) / SemTotal\(_{\mathcal C}\) | semántico y pre-ontológico por construcción |
| RegimeTotal | downstream; presupone GeneBasis ya tipada en el mismo contexto |
| REC | consecuencia de RegimeTotal |
| Muro | restricción epistemológica, no criterio de unidad |
| \(\Omega_i\) | post-individuación y dependiente de estructura generativa/trivialización |
| GenesisConstitutiveUnity | útil para un hijo constituido; no cubre una unidad ambiental preexistente |

Por tanto obtenemos un **resultado de no-reducción arquitectónica**, no un teorema de indefinibilidad lógica absoluta:

\[
\boxed{
\text{AI no está actualmente descargada por ninguna combinación ya justificada
de la maquinaria vigente sin añadir semántica nueva.}
}
\]

La precisión “ya justificada” importa. No se afirma que sea imposible definir ContextIndividuation a partir de alguna teoría futura; se afirma que hacerlo hoy reutilizando sin más los predicados anteriores produciría o circularidad, o sobre-restricción monogeneal, o infra-determinación.

Un stress test resume el problema. Dos historias pueden desembocar en la misma presentación conjunta:

\[
C_a,C_b \leadsto C_{\widehat{k}},
\]

pero diferir en prioridad ontológica:

\[
\begin{array}{ll}
\text{Historia A:} & C_{\widehat{k}}\text{ preexiste y una integración solo lo revela;}\\
\text{Historia B:} & C_{\widehat{k}}\text{ existe constitutivamente por la integración.}
\end{array}
\]

Una descripción estática del carrier final no distingue A de B. Por eso la individuación no puede reducirse simplemente a “qué hay dentro” de la realización final.

#### 0.11.62. Opción mínima honesta: ContextIndividuation como juicio metaontológico primitivo restringido

Hasta disponer de una teoría independiente más reductiva, la opción formalmente más limpia es no esconder la deuda.

Introducimos provisionalmente:

\[
\operatorname{ContextIndividuation}^{\mathsf M}(C;\chi)
\]

como **juicio metaontológico primitivo sujeto a criterios de admisibilidad**, no como entidad, proceso ni hecho objeto.

Esto no significa “cualquier corte vale”. \(\chi\) debe satisfacer como mínimo las obligaciones CI1–CI8 ya fijadas y, además:

1. **CI9 / boundary coherence:** el corte no puede seccionar una relación objeto cuya propia semántica exija que sus relata estén co-tipados en una única realización; si aparece tal relación, o el corte era erróneo o debe modelarse una interfaz ontogénica distinta.
2. **CI10 / no connectivity definition:** conectividad, amalgamabilidad o closure de links pueden aportar evidencia, pero no constituyen por definición la identidad contextual.
3. **CI11 / no maximality definition:** maximalidad semántica o maximal joint realizability no individúan por sí mismas el contexto.
4. **CI12 / genesis sensitivity:** el juicio debe distinguir una unidad preexistente de una unidad cuya existencia depende constitutivamente de una formación.
5. **CI13 / level discipline:** si dos individuaciones admisibles están anidadas, debe existir una semántica explícita de nivel/embedding; la teoría no puede tratarlas simultáneamente como índices rivales del mismo nivel sin justificar esa relación.
6. **CI14 / no totality smuggling:** ContextIndividuation e IndexAdmission no implican RegimeTotal, OntTotal ni REC.

La salida sigue siendo:

\[
\boxed{
\operatorname{ContextIndividuation}^{\mathsf M}(C;\chi)
\Rightarrow
\operatorname{IndexAdmission}^{\mathsf M}(C\Downarrow i;\chi).
}
\]

La ventaja de declarar esta primitividad provisional es metodológica: la teoría deja visible exactamente qué necesita de una futura ontología de individuación. La alternativa —definir \(i\) por GeneBasis, por conectividad, por maximalidad o por SemTotal— volvería a esconder circularidades ya detectadas.

La **descarga** de esta deuda puede ser relativa a una teoría, pero el target no lo es: una física concreta, una ontología de procesos o una teoría independiente de sistemas puede aportar estructura que justifique \(\chi\) sin hacer que la individuación dependa de nuestra elección descriptiva. La propuesta general no debe inventar esa estructura para garantizar ExistsR.

#### 0.11.63. Consecuencia para ExistsR: REV-07g no es meramente decorativo

La forma vigente:

\[
\operatorname{ExistsR}
:\Longleftrightarrow
\exists^{\mathsf M} i\;
\bigl(
\exists\mathfrak G_i\exists R_i\;
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
\bigr)
\]

usa \(\exists^{\mathsf M}i\) como abreviatura sobre **instanciaciones admisibles del parámetro contextual**, no como cuantificador objeto.

Si ahora se sostiene:

\[
\text{admisibilidad de }i
\Leftarrow
\operatorname{ContextIndividuation}^{\mathsf M},
\]

entonces un witness no circular de ExistsR debe cargar también con esa obligación. No basta con escribir un subíndice y demostrar RegimeTotal condicionalmente dentro de él.

Por ello REV-07g debe distinguir dos alcances:

- **teoremas condicionales por contexto:** continúan siendo válidos fijando un \(i\) admisible como parámetro;
- **programa fuerte de existencia:** para exhibir un witness de ExistsR hay que justificar además la admisibilidad/individuación del contexto usado.

En ese segundo alcance, AI/GI pertenecen a la deuda fundacional de REV-07:

\[
\boxed{
\operatorname{ContextIndividuation}^{\mathsf M}
+
\operatorname{IndexAdmission}^{\mathsf M}
+
\operatorname{RegimeTotal}
\Longrightarrow
\text{witness admisible para ExistsR}.
}
\]

No se adopta la conversa ni se afirma que ContextIndividuation baste para RegimeTotal.

La consecuencia práctica es que REV-07g deja de ser una extensión puramente opcional si la PR pretende cerrar el **argumento no circular de existencia**. Puede seguir siendo no bloqueante para estudiar algebraicamente un contexto ya fijado, pero es blocker para convertir ese estudio en un witness ontológico fuerte de ExistsR.

#### 0.11.64. Stress test de indistinguibilidad: un contexto desconectado frente a dos contextos

Consideremos dos GeneUnit pre-indexadas \(A\) y \(B\) cuya estructura interna está independientemente especificada. Supóngase:

1. no hay CommonGround entre ellas;
2. no hay OntProd transversal;
3. no hay PureOntRel transversal;
4. no hay dependencia constitutiva entre ellas;
5. no hay ningún predicado objeto adicional que tome simultáneamente relata de \(A\) y \(B\).

Comparemos dos lecturas metaontológicas.

**Modelo S — shared ambient context.** Existe una candidatura \(\widehat{k}\) en la que \(A\) y \(B\) son dos sectores desconectados de un mismo contexto preexistente:

\[
A_{\widehat{k}}
\sqcup
B_{\widehat{k}}.
\]

**Modelo P — plurality.** \(A\) y \(B\) pertenecen a contextos distintos \(i\) y \(j\), sin ningún hecho objeto transversal:

\[
A_i
\qquad
B_j.
\]

Ahora olvidemos únicamente las etiquetas contextuales y conservemos toda la estructura objeto interna de cada sector. Por hipótesis no existe ninguna relación transversal que pueda perderse. El reducto estructural queda:

\[
\mathcal M_A\sqcup\mathcal M_B
\]

en ambos casos.

Por tanto cualquier criterio construido **solo** con las propiedades y relaciones objeto internas de \(A\) y \(B\) asigna el mismo perfil a S y P. Sin estructura ambiental adicional no puede recuperar qué partición contextual estaba presente.

Esto produce el lema adversarial:

\[
\boxed{
\textbf{AI-UD:}
\quad
\text{si un contexto puede contener sectores ontológicamente desconectados,}
\\
\text{la partición de contexto no es recuperable en general
del reducto objeto intrínseco de esos sectores.}
}
\]

AI-UD es condicional. No afirma que existan de hecho tales sectores desconectados. Afirma que **REV-07f los permite actualmente** al admitir SharedOntSpace multigeneal sin CommonGround ni exigir un enlace transversal universal.

La conclusión no depende de que S y P sean “el mismo mundo” en un sentido previo; precisamente muestra que esa diferencia no aparece en el vocabulario objeto supuesto por el stress test.

#### 0.11.65. Tres salidas frente a AI-UD

AI-UD obliga a elegir, o al menos distinguir, tres arquitecturas posibles.

**Ruta WMR — world-making structure.** Se fortalece la doctrina y se exige que toda unidad contextual posea alguna estructura independiente \(W\) que haga de world-making relation/structure:

\[
\operatorname{WorldMaking}^{\mathsf M}(W;C)
\Rightarrow
\operatorname{ContextIndividuation}^{\mathsf M}(C;\chi_W).
\]

\(W\) no tiene por qué ser binaria, local, espaciotemporal ni siquiera una única relación. Pero debe ser natural/ontológicamente justificada, recoding-invariant y suficientemente discriminante para decidir co-contextualidad.

Precio: esta ruta **excluye o reinterpreta** el caso de sectores completamente desconectados dentro de un mismo contexto. Además abre una nueva versión de ProdCoverage: ¿qué familia de estructuras puede hacer mundo?

**Ruta PRI — co-contextualidad primitiva restringida.** Se acepta que el hecho metaontológico de pertenecer a una misma unidad contextual no superviene en general sobre las relaciones objeto locales disponibles:

\[
\operatorname{ContextIndividuation}^{\mathsf M}
\quad\text{primitivo sujeto a CI1--CI14.}
\]

Precio: el programa deja de ser reductivo en este punto. Ventaja: no inventa un enlace universal que REV-07f no ha demostrado.

**Ruta TR — descarga teoría-relativa.** La ontología general deja \(\chi\) parametrizado y exige que cada teoría concreta proporcione su criterio:

\[
\mathcal T
\vdash
\operatorname{ContextCriterion}_{\mathcal T}
\Longrightarrow
\operatorname{ContextIndividuation}^{\mathsf M}.
\]

En una teoría podría ser estructura espaciotemporal; en otra, una relación más fundamental; en otra, una condición organizacional. La propuesta general impone solo los guards CI1–CI14.

Estas rutas no son equivalentes. En particular:

\[
\boxed{
\mathrm{TR}
\neq
\mathrm{PRI}
}
\]

porque TR conserva la aspiración reductiva **localmente a una teoría**, mientras PRI acepta primitividad incluso después de fijarla.

La literatura de worldmate muestra precedentes de WMR —por ejemplo, relaciones espaciotemporales en Lewis o propuestas de entanglement en ontologías no espaciales—, pero no autoriza a importar ninguna como solución universal.

#### 0.11.66. Consecuencia para la metáfora de membrana: bona fide frente a fiat

AI-UD también endurece la lectura celular.

Si dos particiones rivales del mismo contenido satisfacen todas las propiedades intrínsecas disponibles y ninguna estructura adicional selecciona una, llamar “membrana” a una de ellas sería, en el mejor de los casos, una **demarcación fiat** de la representación.

Por tanto REV-07g debe distinguir:

\[
\boxed{
\text{boundary represented}
\neq
\text{boundary ontologically grounded}.
}
\]

La distinción bona fide/fiat de Smith y Varzi es solo un precedente analógico sobre fronteras espaciales; no se traslada literalmente a contextos metafísicos. El punto metodológico sí permanece: una línea de demarcación puede ser precisa y útil sin corresponder por ello a una discontinuidad ontológica independiente.

Así, una verdadera Cellular Reality fuerte exigiría:

\[
\operatorname{ContextIndividuation}^{\mathsf M}(C;\chi)
\]

con \(\chi\) suficientemente independiente para impedir que la “membrana” sea simplemente el contorno elegido por nuestra representación.

Esto refuerza CI7/CI13: si hay nesting legítimo, debe estar ontológicamente estructurado; si solo hay múltiples coarse-grainings equivalentes, no debemos multiplicar índices.

#### 0.11.67. Qué puede salvarse sin decidir todavía WMR/PRI/TR

No es necesario elegir hoy una metafísica universal de individuación para conservar la arquitectura ganada.

Podemos fijar el contrato mínimo:

\[
\boxed{
\operatorname{AdmissibleContext}^{\mathsf M}(C;\chi)
:=
\operatorname{ContextIndividuation}^{\mathsf M}(C;\chi)
\land
\mathrm{CI1\text{-}CI14}(C,\chi).
}
\]

y usar:

\[
\operatorname{AdmissibleContext}^{\mathsf M}(C;\chi)
\Rightarrow
\operatorname{IndexAdmission}^{\mathsf M}(C\Downarrow i;\chi).
\]

El símbolo “:=” aquí es solo una abreviatura de contrato metateórico, no una reducción ontológica de \(\chi\).

A partir de ahí las obligaciones quedan ordenadas:

\[
\boxed{
\begin{array}{rcl}
\text{ContextIndividuation} &\to& \text{IndexAdmission}\\
&\to& \text{GeneBasis/RegimeClosure}\\
&\to& \text{RegimeTotal}\\
&\to& \text{REC},
\end{array}
}
\]

mientras:

\[
\text{Muro}
\]

permanece transversal como límite epistemológico y:

\[
\text{ContextGenesis / FaithfulContinuation / Trivialization}
\]

describen interfaces y dinámica entre individuaciones.

Esta organización permite continuar REV-07 sin fingir que AI está resuelta. El siguiente target formal ya no es “buscar más propiedades de la célula”, sino decidir si la propuesta quiere:

1. postular una WMR abstracta y someterla a countermodels;
2. aceptar ContextIndividuation como primitivo metaontológico restringido;
3. parametrizarla por teoría concreta y demostrar un teorema de transporte de criterios de individuación hacia IndexAdmission.

#### 0.11.68. Ruta de trabajo preferida: esquema de individuación parametrizado por teoría

Entre WMR, PRI y TR, la ruta provisionalmente más conservadora para una ontología general es **TR**: no fijar universalmente qué estructura individúa todo contexto, sino especificar qué debe demostrar cualquier teoría que pretenda hacerlo.

Sea \(\mathcal T\) una teoría ontológica/física independientemente motivada. Introducimos un juicio metateórico de **descarga**:

\[
\operatorname{Ind}_{\mathcal T}^{\mathsf M}(C;\chi),
\]

leído: “\(\mathcal T\), mediante la estructura representada por \(\chi\), ofrece un criterio para justificar que \(C\) constituye una unidad contextual”.

El target permanece objetivo y **no contiene el witness epistemológico**:

\[
\boxed{
\operatorname{ContextIndividuation}^{\mathsf M}(C).
}
\]

Cuando aparezca históricamente la anotación \(\operatorname{ContextIndividuation}(C;\chi)\), debe leerse solo como «esta conclusión fue certificada mediante \(\chi\)», no como una relación ontológica cuyo segundo argumento constituya al contexto.

Por tanto \(\operatorname{Ind}_{\mathcal T}\) no significa “\(C\) es una unidad porque \(\mathcal T\) lo dice”. Una teoría falsa, meramente instrumental o estructuralmente infiel no puede fabricar un contexto ontológico.

\(\mathcal T\) no es un objeto dentro de \(C\), ni un supercontexto, ni un elemento de un dominio ontológico de teorías. Es un parámetro del metalenguaje.

Para que el juicio pueda alimentar IndexAdmission exigimos:

\[
\operatorname{IndAdequate}^{\mathsf M}(\mathcal T,C,\chi).
\]

Sus obligaciones mínimas son:

0. **IA0 / structural fidelity:** la parte de \(\mathcal T\) usada por el criterio debe satisfacer dos obligaciones distintas: **IA0-R / realized modal support**, es decir, representar estructura efectivamente realizada y contrafácticamente soportada; y **IA0-U / individuation relevance**, es decir, justificar que esa misma estructura hace trabajo constitutivo/discriminante para la unidad contextual de \(C\), no solo para alguna propiedad, predicción o macroconducta real. Consistencia interna, conveniencia predictiva, projectability o causal efficacy por sí solas no bastan.
1. **IA1 / theory independence:** \(\mathcal T\) está justificada por razones independientes del deseo de obtener precisamente el corte \(C\); no se construye ad hoc a partir del target.
2. **IA2 / target independence:** \(\operatorname{Ind}_{\mathcal T}\) no usa \(R_i\), RegimeTotal, REC, SameRegime ni la existencia previa del índice que pretende admitir.
3. **IA3 / positive grounding:** debe existir estructura positiva de \(\mathcal T\) que funde el corte; no basta la ausencia de enlaces con el exterior.
4. **IA4 / recoding invariance:** recodificaciones fieles de la misma estructura preservan el juicio.
5. **IA5 / boundary coherence:** ningún hecho objeto que \(\mathcal T\) considere fundamentalmente co-tipado queda cortado arbitrariamente por la frontera.
6. **IA6 / anti-aggregation:** envolver una pluralidad de unidades ya individuadas en una descripción conjunta no produce una nueva unidad sin estructura adicional.
7. **IA7 / genesis discrimination:** la teoría debe poder distinguir, cuando sea relevante, una unidad preexistente de otra constituida por una génesis.
8. **IA8 / rival-cut discipline:** cortes incompatibles inducidos por la misma \(\mathcal T\) requieren equivalencia, una semántica explícita de nesting/nivel o rechazo de al menos uno.
9. **IA9 / no totality smuggling:** individuar el contexto no demuestra que su scope esté exhaustivamente realizado.
10. **IA10 / auditability:** debe poder señalarse qué rasgos de \(\mathcal T\) hacen el trabajo de individuación y qué contraejemplo haría fallar el criterio.

Entonces la descarga correcta tiene dos pasos:

\[
\boxed{
\operatorname{Ind}_{\mathcal T}^{\mathsf M}(C;\chi)
\land
\operatorname{IndAdequate}^{\mathsf M}(\mathcal T,C,\chi)
\Rightarrow
\operatorname{ContextIndividuation}^{\mathsf M}(C)
\Rightarrow
\operatorname{IndexAdmission}^{\mathsf M}(C\Downarrow i;\chi,\mathcal T).
}

El primer paso **elimina** \(\chi\) de la conclusión ontológica. El segundo puede conservarlo únicamente como provenance/audit metadata de la admisión metateórica.
\]

La primera implicación es la obligación de soundness de la descarga; la segunda es la regla formal de admisión. La teoría \(\mathcal T\) no se convierte en una realidad superior ni en creadora de la unidad que certifica.

El caso PRI se recupera como límite si una futura metafísica sostiene que no existe una reducción ulterior y toma ContextIndividuation como fundamental. WMR se recupera como caso de TR si \(\mathcal T\) proporciona una world-making structure adecuada.

#### 0.11.68a. Descarga relativa a teoría no es relativismo ontológico

Dos teorías \(\mathcal T_1,\mathcal T_2\) pueden proporcionar criterios distintos para la misma individuación objetiva:

\[
\operatorname{Ind}_{\mathcal T_1}^{\mathsf M}(C;\chi_1),
\qquad
\operatorname{Ind}_{\mathcal T_2}^{\mathsf M}(C;\chi_2),
\]

sin que existan por ello dos realidades “relativas a teorías”.

Si ambas descargas son adecuadas y sus testigos son equivalentes respecto del corte, ambas convergen sobre el mismo target:

\[
\operatorname{ContextIndividuation}^{\mathsf M}(C).
\]

Si divergen, la divergencia es un conflicto entre criterios/teorías que debe resolverse mediante IA0–IA10, evidencia adicional o una semántica de niveles. No se infiere automáticamente pluralidad ontológica.

Por tanto:

\[
\boxed{
\text{theory-relative discharge}
\neq
\text{theory-relative reality}.
}
\]

Esto también limita IndexRetraction: abandonar una teoría puede retirar nuestra justificación para un índice, pero solo muestra que la admisión anterior fue epistémicamente defectuosa si la nueva evaluación invalida su witness. No produce ContextCessation ni reescribe retroactivamente la ontología.

#### 0.11.68b. R-FORM — de ContextIndividuation a \(R_i\) sin fabricar totality

La arquitectura anterior ya imponía la dirección:

\[
\operatorname{ContextIndividuation}^{\mathsf M}(C)
\Rightarrow
\operatorname{IndexAdmission}^{\mathsf M}(C\Downarrow i),
\]

pero dejaba implícito qué significa exactamente pasar de un índice admitido a la notación \(R_i\). Si se interpreta esa flecha como existencia automática de una realidad total, IA9/CI14 quedan violados. Si, por el contrario, se exige RegimeTotal antes de poder escribir \(R_i\), reaparece la circularidad porque RegimeTotal ya presupone una GeneBasis comúnmente tipada por \(i\).

La solución es distinguir **formación tipada** de **totalización ontológica**.

Definimos la regla metateórica:

\[
\boxed{
\frac{
\operatorname{ContextIndividuation}^{\mathsf M}(C)
\qquad
\operatorname{IndexAdmission}^{\mathsf M}(C\Downarrow i)
}{
\vdash^{\mathsf M} R_i:\mathsf{OntScope}_i
}
\quad(\mathrm{R\text{-}FORM})
}
\]

La conclusión no es un hecho objeto ni un existencial ontológico. Significa únicamente que, una vez individuado \(C\) y admitido su parámetro contextual \(i\), el metalenguaje puede usar \(R_i\) como **candidato de scope ontológico de ese contexto** y puede formar expresiones como:

\[
\operatorname{Within}_i(x_i,R_i),
\qquad
\operatorname{OntTotal}_i(R_i),
\qquad
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i).
\]

No se introduce un predicado adicional ContextReality: la procedencia de \(R_i\) ya queda transportada por IndexAdmission y por el propio tipado \(i\). Duplicar esa información en una entidad puente solo reificaría la relación metateórica.

**RF1 / no existence promotion.**

\[
\vdash^{\mathsf M}R_i:\mathsf{OntScope}_i
\not\Rightarrow
\operatorname{OntTotal}_i(R_i).
\]

**RF2 / no genealogical promotion.**

\[
\operatorname{IndexAdmission}^{\mathsf M}(C\Downarrow i)
\not\Rightarrow
\exists\mathfrak G_i\;
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i).
\]

**RF3 / no bootstrap.** RegimeTotal solo puede evaluarse bajo un índice ya admitido. No se autoriza:

\[
\operatorname{RegimeTotal}_{\widehat{i}}(\mathfrak G,R)
\Rightarrow
\operatorname{IndexAdmission}^{\mathsf M}(C\Downarrow i),
\]

porque el antecedente usa precisamente el typing cuya legitimidad intenta demostrar. Un cálculo provisional bajo \(\widehat{i}\) puede ser evidence de una descarga independiente, pero no convierte RegimeTotal en criterio de individuación.

La jerarquía correcta queda:

\[
\boxed{
\operatorname{ContextIndividuation}
\longrightarrow
\operatorname{IndexAdmission}
\longrightarrow
\mathrm{WF}(R_i)
\longrightarrow
\operatorname{RegimeTotal}
\longrightarrow
\operatorname{OntTotal}.
}
\]

La tercera flecha es una **regla de formación** y la cuarta exige toda la maquinaria REV-07f; no son implicaciones ontológicas homogéneas.

#### 0.11.68c. CI–RT bridge y coextensionalidad del scope

Una instancia fuerte queda ahora normalizada como:

\[
\boxed{
\operatorname{ContextIndividuation}^{\mathsf M}(C)
\land
\operatorname{IndexAdmission}^{\mathsf M}(C\Downarrow i)
\land
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
\Rightarrow
\operatorname{OntTotal}_i(R_i)
\land
\operatorname{ExistsR}.
}
\]

Esto no añade poder deductivo misterioso a RegimeTotal. Hace explícitas dos cargas que antes estaban repartidas entre la semántica de \(\exists^{\mathsf M}i\) y REV-07g:

1. \(i\) debe proceder de una individuación admisible;
2. el scope \(R_i\) debe ser totalizado genealógicamente, no solo estar bien formado.

La conclusión ExistsR usa una sola instancia admitida como witness del metaschema. Por No-Free-Actuality, una descarga de ContextIndividuation que pretenda participar en un witness existencial debe además respetar IA0/realization; R-FORM por sí sola no aporta actualidad.

Hay además una consecuencia útil. Supóngase el mismo índice admitido \(i\) y dos scopes candidatos:

\[
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i),
\qquad
\operatorname{RegimeTotal}_i(\mathfrak H_i,R'_i).
\]

Por definición de RegimeTotal:

\[
\forall x_i[
\operatorname{Within}_i(x_i,R_i)
\leftrightarrow
\operatorname{Real}_i(x_i)
],
\]

y:

\[
\forall x_i[
\operatorname{Within}_i(x_i,R'_i)
\leftrightarrow
\operatorname{Real}_i(x_i)
].
\]

Luego:

\[
\boxed{
\forall x_i[
\operatorname{Within}_i(x_i,R_i)
\leftrightarrow
\operatorname{Within}_i(x_i,R'_i)
].
}
\]

Por tanto dos descargas RegimeTotal bajo el mismo índice no producen dos realidades contextuales distintas: producen scopes **coextensionales respecto de Within**. La teoría no infiere \(R_i=R'_i\) porque \(R_i\) no debe reificarse como objeto con identidad adicional y no se ha postulado extensionalidad de scopes.

Este resultado también aclara la relación con GeneBasis. Puede haber dos GeneBasis adecuadas que converjan extensionalmente sobre el mismo contenido real; decidir si son genealógicamente equivalentes es una cuestión posterior de identidad de genealogía, no de individuación de contexto.

#### 0.11.68d. Semántica explícita de \(\exists^{\mathsf M}i\)

La expresión:

\[
\exists^{\mathsf M}i\;\Phi_i
\]

no significa “hay un objeto \(i\)”. Significa que el metalenguaje dispone de una **instanciación admitida** del parámetro contextual. Tras REV-07g, esa admisibilidad debe transportar provenance de:

\[
\operatorname{ContextIndividuation}^{\mathsf M}(C)
\land
\operatorname{IndexAdmission}^{\mathsf M}(C\Downarrow i).
\]

Por tanto un subíndice escrito por conveniencia, un \(\widehat{i}\) provisional o un carrier semántico etiquetado no satisfacen el metaschema. Esta precisión bloquea el siguiente falso atajo:

\[
\text{escribir }i
\;+\;
\text{demostrar RegimeTotal condicionalmente}
\;\not\Rightarrow\;
\operatorname{ExistsR}.
\]

Para ExistsR debe existir una instancia de RegimeTotal cuyo índice sea **admisible en el sentido anterior**. La descarga de esa admisibilidad puede variar entre teorías sin relativizar el target ContextIndividuation.

#### 0.11.69. Equivalencia de testigos: varias pruebas no deben multiplicar índices

La individuación puede tener varias evidencias independientes. Por ejemplo, una teoría podría reconocer la misma frontera mediante dos estructuras distintas. No queremos:

\[
\chi_1\neq\chi_2
\Rightarrow
i\neq j.
\]

Introducimos esquemáticamente:

\[
\chi_1
\approx^{\mathsf M}_{C,\mathcal T}
\chi_2
\]

cuando ambos testigos, bajo \(\mathcal T\), inducen:

1. el mismo corte contextual;
2. el mismo régimen de tipado objeto;
3. las mismas clases de interfaces ontogénicas admisibles;
4. los mismos juicios de identidad contextual relevantes, módulo recodificación fiel.

Entonces:

\[
\boxed{
\operatorname{IndexAdmission}^{\mathsf M}(C\Downarrow i;\chi_1,\mathcal T)
\land
\chi_1\approx^{\mathsf M}_{C,\mathcal T}\chi_2
\Rightarrow
\chi_2\text{ no licencia un índice distinto por sí solo.}
}
\]

La inversa tampoco vale: dos testigos no equivalentes no implican automáticamente dos contextos. Pueden revelar niveles distintos o una disputa aún no resuelta sobre el corte.

Esto evita una nueva versión del problema de “colisiones”: aquí **múltiples certificados de la misma individuación son convergencia evidencial**, no multiplicación ontológica.

#### 0.11.69a. Witness no es truthmaker: separación evidencial/ontológica

El término “witness” había quedado haciendo dos trabajos distintos. Los separamos.

Un **ontic realizer** es estructura cuya obtención hace verdadera la afirmación de que la candidatura está realizada:

\[
\boxed{
\operatorname{OnticRealization}^{\mathsf M}
(
H,C;\varrho
)
}
\]

donde \(H\) representa soporte efectivo pre-indexado o host-side y \(\varrho\) una relación/mapa de realización estructural.

Un **evidence witness**:

\[
\boxed{
\operatorname{Evidences}^{\mathsf M}
(
\chi;
\operatorname{OnticRealization}(H,C;\varrho)
)
}
\]

es una vía epistémica para justificar esa relación.

Por tanto:

\[
\boxed{
\chi
\neq
\varrho
\neq
C.
}
\]

Y, crucialmente:

\[
\operatorname{Evidences}(\chi;P)
\]

no entra como constituyente de \(P\).

Esto bloquea dos errores opuestos.

**WE1 — observer creation fallacy.**

\[
\operatorname{Evidences}(\chi;P)
\not\Rightarrow
\text{\(\chi\) crea ontológicamente \(P\)}.
\]

**WE2 — no-evidence nonexistence fallacy.**

\[
\neg\exists\chi\;
\operatorname{Evidences}(\chi;P)
\not\Rightarrow
\neg P.
\]

Puede haber un contexto real cuya individuación no sea actualmente accesible a ningún observador/certificador.

#### 0.11.69b. OR1–OR9 — realización ontológica estructural

Para que \(\operatorname{OnticRealization}^{\mathsf M}(H,C;\varrho)\) pueda alimentar IA0, exigimos:

1. **OR1 / host actuality:** \(H\) no es una mera descripción posible; hay soporte/actividad efectiva.
2. **OR2 / typed realization:** \(\varrho\) relaciona estructura host-side con estados/eventos/relaciones de \(C\) respetando sus tipos locales.
3. **OR3 / dynamical commutation:** cuando la dinámica host realiza un paso relevante, su proyección local conmuta con la dinámica de \(C\), módulo la equivalencia admitida:

\[
\boxed{
\varrho\circ T_H
\simeq
T_C\circ\varrho.
}
\]

4. **OR4 / counterfactual support:** las dependencias locales declaradas no son mera correlación descriptiva; cambios host-side que realizan diferencias locales pertinentes sostienen las diferencias dinámicas correspondientes.
5. **OR5 / no certificate dependence:** la relación \(\varrho\) se caracteriza sin mencionar qué observador, log, certificado o teoría concreta la detecta.
6. **OR6 / realization covariance:** representaciones fieles \(\alpha_H,\alpha_C\) transportan \(\varrho\) a una realización equivalente:

\[
\varrho'
=
\alpha_C\circ\varrho\circ\alpha_H^{-1}
\]

cuando esas inversas/transportes estén definidos al nivel apropiado.
7. **OR7 / level non-collapse:** que \(H\) realice \(C\) no identifica ambos niveles ni convierte automáticamente todos los tokens host-side en tokens locales.
8. **OR8 / state-locality + prefix locality:** \(\varrho\) debe depender del estado/estructura host-side disponible en el punto relevante, no del futuro completo, de la posición temporal global ni de una clasificación retrospectiva de la trayectoria. Si dos prefixes host-side son localmente equivalentes para la teoría, no pueden mapearse distinto porque posteriormente diverjan.
9. **OR9 / pre-registration / anti-gerrymandering:** la regla que determina \(\varrho\) y las variables host-side relevantes debe fijarse independientemente del run concreto que pretende realizar. No cuenta una partición construida después de observar la trayectoria para forzar conmutación con cualquier autómata deseado.

Definimos:

\[
\operatorname{RealizationAdequate}^{\mathsf M}
(
H,C,\varrho
)
\]

por OR1–OR9.

IA0/structural fidelity puede descargarse por una OnticRealization adecuada. La teoría sigue haciendo trabajo epistémico/descriptivo; la realización hace el trabajo ontológico.

#### 0.11.69c. WC-T1 — witness covariance / eliminación del observador privilegiado

Sean \(\chi_1,\chi_2\) dos evidencias adecuadas de la misma realización objetiva:

\[
\operatorname{Evidences}(\chi_1;\varrho),
\qquad
\operatorname{Evidences}(\chi_2;\varrho).
\]

O, más generalmente, sean \(\varrho_1,\varrho_2\) realizaciones equivalentemente transportadas por OR6.

Si ambas descargas satisfacen IndAdequate, entonces:

\[
\boxed{
\operatorname{Ind}_{\mathcal T_1}(C;\chi_1)
+
\operatorname{Ind}_{\mathcal T_2}(C;\chi_2)
\Rightarrow
\operatorname{ContextIndividuation}^{\mathsf M}(C)
}
\]

sin indexar la conclusión por \(\chi_1\), \(\chi_2\), \(\mathcal T_1\) ni \(\mathcal T_2\).

Definimos este principio como:

\[
\boxed{
\operatorname{WitnessCovariance}^{\mathsf M}(C).
}
\]

Su contenido es:

> cambiar de evidence witness, representación o frame descriptivo fiel puede cambiar la ruta de certificación, pero no el hecho ontológico certificado.

La analogía con covariancia en teorías relativistas es deliberadamente limitada: no importamos la geometría de relatividad general. Importamos solo la disciplina metodológica de que **la estructura física/ontológica no dependa de una descripción privilegiada**.

#### 0.11.69d. WC-T2 — el witness ontológico trivializaría ExistsR

Si intentásemos exigir que el witness \(\chi\) fuese él mismo un objeto real del mismo target ontológico para demostrar ExistsR, aparecería:

\[
\operatorname{Real}(\chi)
\]

como premisa.

Pero entonces ya habríamos introducido realidad para probar que existe realidad.

Por tanto:

\[
\boxed{
\text{el evidence witness de ExistsR no puede ser su truthmaker ontológico.}
}
\]

El truthmaker debe estar en la estructura realizada \(H\overset{\varrho}{\Vdash}C\); \(\chi\) solo hace accesible/justificable esa estructura al metalenguaje.

Esto no elimina la necesidad de una premisa de actualidad para un teorema contingente. Sí elimina la dependencia respecto de **qué** observador/certificado la suministra.

#### 0.11.69e. Trilema de existencia: formalidad, actualidad y NoR

Una teoría puramente formal puede demostrar:

\[
\operatorname{Model}(XR1)
\]

o incluso la consecuencia condicional:

\[
\operatorname{OnticRealization}(H,XR1;\varrho)
\Rightarrow
\operatorname{ExistsR}.
\]

No puede obtener una afirmación contingente de actualidad solo de la satisfacibilidad del modelo.

Por NFA-T1/NFA-T2, para cerrar ExistsR quedan conceptualmente dos rutas no circulares:

1. **ruta realizacional/empírica:** exhibir alguna OnticRealization actual y adecuada; el witness que la evidencia se elimina de la conclusión por WC-T1;
2. **ruta NQ/a priori:** demostrar independientemente que NoR no es una realización admisible, de modo que alguna realización no nula sea necesaria.

La primera necesita actualidad pero no observador privilegiado. La segunda evitaría la premisa empírica, pero continúa abierta.

#### 0.11.69f. NFA-T1 — No-Free-Actuality theorem

La distinción witness/truthmaker permite aislar un límite lógico general.

Sea \(\Sigma\) un conjunto de premisas metateóricas. Definimos:

\[
\boxed{
\operatorname{NullCompatible}^{\mathsf M}(\Sigma)
}
\]

cuando existe una interpretación/realización nula admisible del metalenguaje en la que:

\[
\operatorname{NoR}
\]

y todas las fórmulas de \(\Sigma\) permanecen satisfechas.

No se introduce con ello un objeto “mundo nulo”. Es una propiedad semántica de la teoría/premisas: **las premisas no excluyen la ausencia de toda instanciación RegimeTotal**.

Entonces, por soundness elemental de consecuencia:

\[
\boxed{
\operatorname{NullCompatible}^{\mathsf M}(\Sigma)
\Rightarrow
\Sigma
\not\models
\operatorname{ExistsR}.
}
\]

**Demostración.** Si \(\Sigma\models ExistsR\), toda interpretación admisible que satisface \(\Sigma\) satisface ExistsR. Pero NullCompatible aporta una interpretación admisible que satisface \(\Sigma\land NoR\). Contradicción. \(\square\)

Éste es **NFA-T1 — No-Free-Actuality**.

Su contenido es fuerte:

> ninguna colección de definiciones, consistencia interna, closures, morphisms o principios puramente condicionales que siga siendo compatible con NoR puede demostrar ExistsR.

#### 0.11.69g. NFA-T2 — dicotomía de rutas hacia ExistsR

De NFA-T1 sigue que toda prueba no circular de ExistsR debe contener al menos una premisa \(\phi\) tal que:

\[
\neg
\operatorname{NullCompatible}^{\mathsf M}(\{\phi\}),
\]

o demostrar que Null no es admisible en absoluto.

Por tanto las rutas exhaustivas a este nivel son:

\[
\boxed{
\begin{array}{ll}
\textbf{A / actuality route:}
&
\operatorname{ActualStructuralRealization}(H,C;\varrho)
\text{ u otra premisa actual positiva};
\\[1mm]
\textbf{B / NQ route:}
&
\neg\operatorname{AdmissiblyRealizable}^{\mathsf M}(\operatorname{Null}^{\mathsf M}).
\end{array}
}
\]

La ruta A es contingente/realizacional. La ruta B sería necesaria/a priori si pudiera demostrarse.

No hay una tercera ruta puramente formal basada solo en construir un modelo no nulo:

\[
\operatorname{Model}(C)
\not\Rightarrow
\operatorname{ExistsR}.
\]

#### 0.11.69h. RSP-R no es la premisa de actualidad

La regla vigente de soporte realizacional es:

\[
\operatorname{ActualStructuralRealization}(H,C;\varrho)
+
\operatorname{MCAdequate}(C)
\Rightarrow
IA0\text{-}R(C).
\]

Es un principio de **soporte de realización**, no de existencia.

Bajo Null, su antecedente ActualStructuralRealization es falso; por tanto RSP-R puede ser verdadero vacuamente. En consecuencia:

\[
\boxed{
\mathrm{RSP\text{-}R}
\not\Rightarrow
\operatorname{ExistsR}.
}
\]

La carga anti-Null está en:

\[
\operatorname{Obtains}^{\mathsf M}(H),
\]

no en el evidence witness, RSP-R ni UnitGroundAdequate.

La antigua RSP hacia IA0 completo queda SUPERSEDED. Sustituir “el certificado existe” por “la estructura está realizada” tampoco resuelve por sí solo IA0-U.

#### 0.11.69i. Consecuencia epistemológica: prueba empírica vs prueba a priori

Una descarga de la ruta A puede justificar ExistsR del mismo modo que una prueba empírica de existencia justifica cualquier existential contingente:

\[
\operatorname{Evidences}(\chi;\operatorname{Obtains}(H))
\]

más una teoría adecuada permite inferir racionalmente:

\[
\operatorname{Obtains}(H),
\]

sin hacer de \(\chi\) un truthmaker.

Pero la inferencia seguirá siendo **empírico-metateórica**, no un teorema de lógica pura.

Por tanto deben distinguirse tres statuses:

1. **FORMAL-CONDITIONAL:** \(\phi\Rightarrow ExistsR\);
2. **EMPIRICALLY-DISCHARGED:** existe evidencia independiente adecuada para la premisa actual \(\phi\);
3. **A-PRIORI / UNCONDITIONAL:** ExistsR se obtiene sin premisa contingente de actualidad, por ejemplo si NQ queda demostrado.

Esta distinción evita llamar “incondicional” a una prueba cuya única condición ha sido descargada empíricamente.

#### 0.11.69j. Reentrada de \(\varepsilon\): emergencia como descarga positiva de IA0

La maquinaria de REV-03 fue construida al principio de la PR precisamente con una propiedad que ahora resulta crucial:

\[
\boxed{
\mathcal E_M
\text{ se define sin usar }R,\operatorname{RegimeTotal},\operatorname{Adm}
\text{ ni posibilidad ontológica derivada.}
}
\]

Además, un evento emergente exige actualización efectiva:

\[
e=(s_0,P,s_1)\in\mathcal E_M
\]

solo si:

\[
s_0\xrightarrow{+}_{M,\mathrm{act}}s_1
\]

junto con Macro-invariancia, novedad de \(P\) y un OrgWitness que controla el perfil local y demuestra capacidad dinámica habilitada.

Por tanto \(\varepsilon\) aporta una forma pre-indexada de **estructura organizacional efectivamente operativa**.

Sin embargo, REV-03 fue deliberadamente modesta:

\[
e\in\mathcal E_M
\not\Rightarrow
\text{irreducibilidad metafísica}
\]

y:

\[
e\in\mathcal E_M
\not\Rightarrow
\operatorname{ContextIndividuation}.
\]

La microdinámica puede implementar completamente la capacidad emergente.

La conexión correcta con TR-M exige una capa adicional de alineación.

#### 0.11.69k. EA1–EA8 — EpsilonAlignment

Sea \(C\) una candidatura pre-indexada con MemoContextCriterion y sea \(M_C\) una representación system-relative de su dinámica.

Definimos:

\[
\boxed{
\operatorname{EpsilonAligned}^{\mathsf M}_{\mathcal T}
(
C,e,\varrho;\epsilon
)
}
\]

cuando \(\epsilon\) descarga:

1. **EA1 / realized actuality:** el path actual del evento \(e\) es la proyección, mediante una realización OR1–OR9, de una transición/proceso host-side efectivo.
2. **EA2 / event locality:** \(s_0,P,s_1\) y el OrgWitness están tipados dentro de la misma candidatura \(C\); no se ensamblan relata de contextos rivales.
3. **EA3 / organizational control:** el witness compara configuraciones con perfil local equivalente y diferencia organizacional pertinente, exactamente como exige REV-03.
4. **EA4 / dynamical efficacy:** la organización de \(s_1\) habilita al menos una capacidad/traza ausente en el comparador controlado.
5. **EA5 / individuation alignment:** las relaciones organizacionales que hacen trabajo en \(P\) y Enables pertenecen a la misma estructura positiva que MC3–MC7 usa para justificar boundary, typing, interface mediation o counterfactual autonomy. Una emergencia accidental dentro de un contenedor arbitrario no individúa el contenedor.
6. **EA6 / interaction coverage:** las dependencias que producen la capacidad emergente no atraviesan hidden bypasses omitidos por la frontera; si lo hacen, MC4 obliga a ampliar/revisar el contexto.
7. **EA7 / recoding covariance:** recodificaciones fieles preservan el evento emergente y su alineación, además de OR6.
8. **EA8 / no post-hoc emergence cut:** \(M_C\), \(P\), el tipo de OrgWitness y la estructura usada para individuar \(C\) se fijan independientemente del run concreto; no se eligen después para hacer aparecer emergencia.

La conjunción:

\[
\operatorname{RealizedEmergence}^{\mathsf M}
(
H,C,e;\varrho
)
\]

abrevia:

\[
\operatorname{ActualStructuralRealization}(H,C;\varrho)
+
e\in\mathcal E_{M_C}
+
\operatorname{EpsilonAligned}(C,e,\varrho).
\]

#### 0.11.69l. \(\varepsilon\)-RSP — revisión tras el ataque a IA0

La formulación provisional original era:

\[
\operatorname{RealizedEmergence}
+
\operatorname{MCAdequate}
\Rightarrow
IA0.
\]

La auditoría posterior de §§0.11.91r-q–z muestra que esa inferencia colapsaba dos cargas diferentes. Una estructura macro puede estar realmente realizada, ser projectable, contrafácticamente robusta y causal/dinámicamente eficaz sin que se siga todavía que **esa estructura individúe una arena contextual**.

Por tanto la versión que infería IA0 completo queda:

\[
\boxed{
\varepsilon\mathrm{RSP}_{\mathrm{full}}
\quad\textbf{SUPERSEDED}.
}
\]

La consecuencia conservada es únicamente:

\[
\boxed{
\varepsilon\mathrm{RSP\text{-}R}
:
\operatorname{RealizedEmergence}(H,C,e;\varrho)
+
\operatorname{MCAdequate}(C)
\Rightarrow
IA0\text{-}R(C).
}
\]

Es decir: la emergencia realizada puede descargar **realized modal support** para la estructura usada por el criterio. Para IA0 completo falta además IA0-U / UnitGroundAdequate, formalizado en §§0.11.91r-v–z.

Esto no debilita REV-03: solo impide usar emergencia real como atajo desde “macroestructura real” hasta “contexto individuado”.

#### 0.11.69m. EF-T1 — por qué \(\varepsilon\)RSP no es mera etiqueta descriptiva

Bajo EA1–EA8:

- la macrocaracterística \(P\) es invariante a renombrado;
- el perfil local está controlado;
- variar la organización cambia \(P\);
- esa organización cambia el conjunto de capacidades/trazas disponibles;
- el evento que produce el nuevo estado fue efectivamente realizado;
- OR8/OR9 impiden definir retrospectivamente el mapping que hace aparecer esa organización;
- MC3–MC7 alinean esa eficacia con la frontera/contextualidad propuesta.

Por tanto el contenido usado para IA0 posee simultáneamente:

\[
\boxed{
\text{actuality}
+
\text{organization dependence}
+
\text{counterfactual discrimination}
+
\text{dynamical efficacy}
+
\text{boundary alignment}
+
\text{covariance}.
}
\]

Esto es exactamente el tipo de evidencia positiva que IA0 reclamaba frente a consistencia interna, conveniencia predictiva o ajuste puramente descriptivo.

Lo que EA1–EA8 demuestra con fuerza es **realidad modal/organizacional de la estructura**. El ataque IA0 añade una pregunta distinta:

> ¿la estructura que produce esa macroeficacia es además la estructura que constituye o discrimina la unidad contextual de \(C\)?

Responder “sí” solo porque la macroestructura es real sería **real-pattern promotion**. La respuesta exige IA0-U / UnitGroundAdequate. Por tanto EF-T1 respalda \(\varepsilon\)RSP-R, no el antiguo \(\varepsilon\)RSP_full.

#### 0.11.69n. XR-\(\varepsilon\): XR-1 reutiliza el toy emergentista original

XR-1 se refina sin ampliar su scope actual.

Interpretamos:

\[
s_0=p
\]

como la configuración camino de cuatro componentes ready, y:

\[
s_1=c
\]

como la configuración ciclo tras el evento actual:

\[
p\xrightarrow{\texttt{close}}_{\mathrm{act}}c.
\]

Sea:

\[
P(s)=\beta_1(G(s)).
\]

Entonces:

\[
P(p)=0,
\qquad
P(c)=1.
\]

Los cuatro componentes conservan el mismo perfil local:

\[
L(p)\cong L(c),
\]

y:

\[
\texttt{activate}
\in
\operatorname{Traces}(c)
\setminus
\operatorname{Traces}(p).
\]

Luego \(p\) funciona como OrgWitness controlado para \(c\), exactamente según REV-03:

\[
\boxed{
(p,P,c)\in\mathcal E_{M_{XR1}}.
}
\]

La configuración alcanzable por activate puede permanecer **potencial**: no entra en el scope actual XR-1 porque OrgWitness compara capacidades disponibles, no exige que toda capacidad se actualice.

El script scripts/xr1_witness.py verifica ahora:

- la actualización real host-side \(p\to c\);
- invariancia de \(\beta_1\) bajo todas las \(4!\) permutaciones type-preserving;
- igualdad del perfil local de los cuatro componentes;
- novedad macroestructural \(0\to1\);
- disponibilidad de activate solo tras la reorganización;
- OR2–OR9 de la realización host/local.

Así XR-1 deja de ser solo una DTS mínima:

\[
\boxed{
XR1
=
\text{finite GeneTotal candidate}
+
\text{actual realized }\varepsilon\text{-event}.
}
\]

#### 0.11.69o. XR\(\varepsilon\)-T — ruta emergentista revisada hacia ExistsR

Para XR-1, EA1–EA8 quedan descargables por construcción y por los tests ejecutables, mientras MC1–MC10 e IA1–IA10 ya fueron auditados.

La conclusión automática es ahora solo:

\[
\operatorname{RealizedEmergence}_{XR1}
+
\operatorname{MCAdequate}_{XR1}
\Rightarrow
IA0\text{-}R_{XR1}.
\]

Para obtener IA0 completo se necesita además:

\[
\operatorname{UnitGroundAdequate}^{\mathsf M}
(
\mathcal T_{\mathrm{DTS}},
C_{XR1};
g_{XR1},
\Xi_{XR1}
).
\]

Por tanto la ruta correcta queda:

\[
\boxed{
\varepsilon\mathrm{RSP\text{-}R}
+
\operatorname{RealizedEmergence}_{XR1}
+
\operatorname{UnitGroundAdequate}_{XR1}
+
\operatorname{IndAdequate}^{1\text{--}10}_{XR1}
\Rightarrow
\operatorname{ExistsR}.
}
\]

La superscript \(1\text{--}10\) indica que IA0 se descarga por separado: su parte **R** procede de emergencia realizada y su parte **U** requiere un ground de individuación adicional.

Esto sigue siendo una ruta realizacional, no a priori. Pero ahora deja visible exactamente el compromiso metafísico que antes quedaba escondido dentro de \(\varepsilon\)RSP.

#### 0.11.70. Auditoría posterior con \(\Omega_i\) sin circularidad

Una vez admitido \(i\), REV-07e intenta derivar una firma ontogénica:

\[
\Omega_i
\]

desde la estructura generativa/iterativa y sus trivializaciones admisibles.

Aunque \(\Omega_i\) no puede usarse retroactivamente como fundamento inicial de \(i\), sí puede funcionar como **auditor posterior** de la individuación:

\[
\operatorname{BoundaryCompatible}^{\mathsf M}(\chi,\Omega_i).
\]

Si la firma derivada muestra que transformaciones clasificadas por \(\chi\) como cross-boundary son en realidad iteraciones internas de la misma estructura, o viceversa, aparece una inconsistencia que debe resolverse.

Por tanto:

\[
\boxed{
\operatorname{BoundaryCompatible}^{\mathsf M}(\chi,\Omega_i)
}
\]

es una condición de coherencia posterior, no una premisa de IndexAdmission.

Esto produce un bucle epistemológico legítimo sin bucle definicional:

\[
\chi
\to
i
\to
\text{estructura generativa}
\to
\Omega_i
\to
\text{auditoría de }\chi.
\]

El último paso puede obligar a revisar nuestra **clasificación** del contexto, pero no altera retroactivamente los hechos ontológicos.

#### 0.11.71. IndexRetraction no es ContextCessation

La lectura celular introduce una distinción necesaria entre dos maneras muy distintas de “dejar de tener un índice”.

**Revisión metateórica.** Descubrimos que el testigo de individuación era defectuoso, que dos candidatos eran en realidad SharedOntSpace o que un corte era un coarse-graining arbitrario. Entonces puede haber:

\[
\operatorname{IndexRetraction}^{\mathsf M}(C\Downarrow i;\epsilon).
\]

Esto significa que el metalenguaje **retira una admisión previa**. No describe un evento ontológico en \(i\).

**Cesación ontológica.** Un contexto previamente bien individuado deja de continuar como tal:

\[
\operatorname{ContextCessation}^{\mathsf M}(i;\delta).
\]

Aquí la ontología cambia; la clasificación anterior no era un error.

Por tanto:

\[
\boxed{
\operatorname{IndexRetraction}^{\mathsf M}
\neq
\operatorname{ContextCessation}^{\mathsf M}.
}
\]

Y tampoco:

\[
\operatorname{IndexRetraction}^{\mathsf M}(i)
\Rightarrow
\text{“}R_i\text{ fue destruido”.}
\]

Una reindexación epistémica puede revelar que nunca hubo dos contextos. Una ContextCessation genuina presupone, por el contrario, que sí hubo una individuación correcta cuya continuidad terminó.

Esta distinción será obligatoria al volver sobre la pregunta “¿puede destruirse un \(R_i\)?”. Sin ella se confundiría corrección de nuestro mapa ontológico con muerte de aquello que el mapa pretendía describir.

#### 0.11.72. IndAdequate no es un nuevo primitivo

Para que TR no desplace simplemente la caja negra de \(\chi\) a IndAdequate, separamos dos contratos.

Las obligaciones sobre la **individuación objetiva** son:

\[
\operatorname{ContextAdequate}^{\mathsf M}(C,\chi)
:=
\bigwedge_{n=1}^{14}\mathrm{CI}_n(C,\chi).
\]

Las obligaciones sobre la **descarga proporcionada por una teoría** son:

\[
\operatorname{DischargeAdequate}^{\mathsf M}(\mathcal T,C,\chi)
:=
\bigwedge_{m=0}^{10}\mathrm{IA}_m(\mathcal T,C,\chi).
\]

Y usamos solo como abreviatura:

\[
\boxed{
\operatorname{IndAdequate}^{\mathsf M}(\mathcal T,C,\chi)
:=
\operatorname{ContextAdequate}^{\mathsf M}(C,\chi)
\land
\operatorname{DischargeAdequate}^{\mathsf M}(\mathcal T,C,\chi).
}
\]

Ninguno de estos nombres introduce un hecho metaontológico adicional que pueda postularse sin descarga: son **bundles de obligaciones de auditoría**.

Análogamente, \(\operatorname{Ind}_{\mathcal T}\) no recibe una definición universal en el núcleo. Cada teoría \(\mathcal T\) debe especificar qué estructura concreta pretende hacer el trabajo de individuación y demostrar que satisface IA0–IA10.

Por tanto la arquitectura no permite:

\[
\operatorname{Ind}_{\mathcal T}^{\mathsf M}(C;\chi)
\quad\text{“por estipulación”.}
\]

Debe existir una reducción theory-specific explícita:

\[
\operatorname{Criterion}_{\mathcal T}(C;\chi)
\Longleftrightarrow
\text{condiciones internas concretas de }\mathcal T,
\]

y después verificarse:

\[
\operatorname{Criterion}_{\mathcal T}
+
\mathrm{IA0\text{-}IA10}
\Rightarrow
\operatorname{ContextIndividuation}^{\mathsf M}.
\]

El núcleo general controla la forma de la descarga; no inventa su contenido.

#### 0.11.73. Toy TR-W: una world-making relation theory-specific sí puede descargar un índice

Para mostrar que TR no es vacía, consideremos una teoría de juguete \(\mathcal T_W\) que postula independientemente una relación fundamental \(W\) y justifica:

\[
\operatorname{WorldMaker}_{\mathcal T_W}(W).
\]

Esta tesis es parte del contenido propio de \(\mathcal T_W\), no una definición construida desde \(R_i\), SameRegime o el índice final.

Sean cuatro tokens pre-indexados:

\[
a,b,c,d,
\]

y supongamos que la estructura \(W\) satisface:

\[
W(a,b),
\qquad
W(b,c),
\]

sin ningún \(W\)-camino entre \(d\) y \(\{a,b,c\}\).

Definimos dentro de \(\mathcal T_W\):

\[
x\equiv_W y
\Longleftrightarrow
\text{existe un camino finito de }W\text{ entre }x\text{ e }y,
\]

y los carriers candidatos:

\[
C_1=[a]_{\equiv_W}=\{a,b,c\},
\qquad
C_2=[d]_{\equiv_W}=\{d\}.
\]

Aquí la conectividad **no** pretende ser una definición universal de contexto. Funciona porque \(\mathcal T_W\) ha justificado independientemente que \(W\), y no una relación arbitraria, es world-making.

Si además:

1. \(W\) es estructuralmente fiel para el dominio del toy (IA0);
2. WorldMaker\(_{\mathcal T_W}\) no se define mediante los componentes que queremos obtener (IA1–IA2);
3. la presencia de \(W\) es positiva y no mera ausencia de exterior (IA3);
4. isomorfismos de la estructura \(W\) preservan sus componentes (IA4);
5. ninguna relación que \(\mathcal T_W\) declare necesariamente co-contextual cruza entre \(C_1\) y \(C_2\) (IA5);
6. las restantes IA6–IA10 quedan satisfechas,

entonces:

\[
\operatorname{Ind}_{\mathcal T_W}^{\mathsf M}(C_1;\chi_W)
\land
\operatorname{IndAdequate}^{\mathsf M}(\mathcal T_W,C_1,\chi_W)
\]

puede descargar:

\[
\operatorname{ContextIndividuation}^{\mathsf M}(C_1;\chi_W)
\Rightarrow
\operatorname{IndexAdmission}^{\mathsf M}(C_1\Downarrow i;\chi_W,\mathcal T_W).
\]

Y análogamente para \(C_2\).

La admisión de ambos carriers como contextos distintos no implica todavía:

\[
i\mathrel{\#}j.
\]

La incompatibilidad es un juicio metaontológico adicional. El toy descarga diferencia de contexto bajo \(\mathcal T_W\), no todas las relaciones posibles entre los contextos admitidos.

El toy demuestra únicamente **consistencia arquitectónica** de TR: existe al menos una forma no circular en que una teoría suficientemente rica puede proporcionar el criterio que el núcleo deja parametrizado.

No demuestra que \(W\) exista en nuestra ontología ni que todo contexto real sea \(W\)-conexo.

#### 0.11.74. Stress tests de TR-W

**TW1 — relación elegida post hoc.** Se define \(W\) como “la relación que conecta exactamente los tokens que queremos meter en \(C_1\)”.

Falla IA1/IA2. La aparente individuación es una codificación del target.

**TW2 — relación demasiado pobre.** Aparece un hecho fundamental \(F(a,d)\) que, por la semántica independiente de \(\mathcal T_W\), exige que \(a\) y \(d\) sean relata del mismo contexto, pero \(W\) los mantiene separados.

Falla IA0 o IA5. La teoría debe ampliar/revisar su world-making structure o retirar la admisión; no puede declarar \(F\) mal tipado solo para proteger el índice.

**TW3 — enlace constitutivamente nuevo.** Antes de una formación no existe estructura que haga worldmates a dos sectores; la propia formación produce por primera vez el witness \(W_k\) que los unifica.

No es automáticamente SharedOntSpace. Si la existencia de la nueva unidad depende constitutivamente de esa formación, el caso migra a GI/ContextGenesis.

**TW4 — dos world-makers rivales.** \(\mathcal T\) ofrece \(W_1\) y \(W_2\), ambos aparentemente adecuados, pero sus componentes inducen cortes incompatibles del mismo nivel.

Falla IA8 hasta demostrar:

\[
W_1\sim_{\mathrm{ind}}W_2,
\]

una relación legítima de nesting/nivel, o una razón para descartar al menos uno.

**TW5 — mismo corte, estructuras distintas.** \(W_1\) y \(W_2\) inducen la misma individuación aunque sean relaciones distintas.

No hay multiplicación de índice. Los witnesses pueden ser distintos pero equivalentes respecto de ContextIndividuation, conforme §0.11.69.

#### 0.11.75. Rehabilitación condicionada de la conectividad

El toy revela una corrección importante a una lectura demasiado fuerte de las rondas anteriores.

La conclusión vigente no es:

\[
\boxed{
\text{“la conectividad nunca puede individuar un contexto”.}
}
\]

Es:

\[
\boxed{
\text{la conectividad de una relación elegida ad hoc
no puede definir por sí sola SameRegime.}
}
\]

Si una teoría independiente demuestra que una relación o estructura \(W\) es constitutiva de worldmatehood, sus componentes conexas **sí pueden** ser una implementación legítima del criterio de ContextIndividuation para esa teoría.

La diferencia de dependencia es:

\[
\begin{array}{ll}
\text{circular:}&
\text{SameContext}\Rightarrow\text{elegimos enlaces}\Rightarrow\text{componentes}\Rightarrow\text{SameContext};\\[2mm]
\text{admisible:}&
\mathcal T\Rightarrow\operatorname{WorldMaker}(W)
\Rightarrow\text{componentes de }W
\Rightarrow\operatorname{ContextIndividuation}.
\end{array}
\]

Esto también recoloca la reconstrucción histórica mediante \(\Lambda_*\). \(\Lambda_*\) no debe recuperar poder individuador por defecto, pero una teoría concreta podría demostrar que una subfamilia o estructura derivada de ella satisface un criterio world-making independiente. En ese caso la conectividad dejaría de ser mero algoritmo de reconstrucción y adquiriría una justificación ontológica adicional **theory-specific**.

#### 0.11.76. Un world-maker sincrónico no resuelve persistencia diacrónica

El toy TR-W individúa componentes en una presentación estática. Supongamos ahora una teoría con etapas \(s,t\) y world-making structures:

\[
W_s,
\qquad
W_t.
\]

Puede ocurrir:

\[
C_s=[a]_{W_s},
\qquad
C_t=[a']_{W_t},
\]

con una modificación extensa de conexiones.

Ni:

\[
C_s=C_t
\]

ni:

\[
C_s\neq C_t
\]

se siguen de la mera comparación extensional de componentes.

Un split de \(W\):

\[
C_s
\leadsto
C_t^{(1)}\sqcup C_t^{(2)}
\]

puede corresponder a:

- fission genuina;
- persistencia de un padre más aparición de un hijo;
- transformación interna donde la desconexión relevante no destruye la unidad;
- o error en haber tomado \(W\) como criterio suficiente de persistencia.

Por tanto TR-W descarga, como máximo, **individuación sincrónica** si la teoría lo justifica. La identidad diacrónica sigue requiriendo ContinuationProfile, \(\Omega\), FaithfulContinuation u otra semántica de persistencia:

\[
\boxed{
\operatorname{WorldMaker}_{\mathcal T}(W)
\not\Rightarrow
\text{criterio de identidad temporal del contexto}.
}
\]

Esto confirma la separación de §0.11.58: unidad, persistencia y ontogénesis son problemas distintos aunque una teoría concreta pueda relacionarlos.

#### 0.11.77. Individuación anidada exige ContextEmbedding, no inclusión literal cross-index

Una teoría puede justificar unidades en varios niveles, y una unidad puede ser simultáneamente **subsistema respecto de un host** y **contexto respecto de su propia arena local**. La inclusión/realización host-side no basta por sí sola para crear el contexto, pero tampoco lo invalida: ambos niveles deben satisfacer un criterio adecuado de ContextIndividuation.

Si \(i\) y \(k\) están legítimamente individuados, una relación de nesting se expresa solo metateóricamente:

\[
\operatorname{ContextEmbedding}^{\mathsf M}(i\hookrightarrow k;e),
\]

donde \(e\) es un testigo de representación/realización fiel entre estructuras tipadas.

No se escribe:

\[
R_i\in R_k
\]

ni se reutiliza literalmente un token \(x_i\) como objeto de \(k\). Si existe representación child/host-side, aparecen términos correctamente tipados y un mapa metateórico, del mismo modo que FaithfulContinuation evita transporte literal cross-index.

Requisitos mínimos:

1. **CE1 / dual individuation:** \(i\) y \(k\) están admitidos por criterios independientes; embedding no crea ninguno de los dos.
2. **CE2 / typed realization:** \(e\) relaciona presentaciones tipadas sin introducir fórmulas objeto cross-index.
3. **CE3 / faithfulness:** preserva exactamente la estructura declarada, no toda propiedad por defecto.
4. **CE4 / no collapse:** \(i\hookrightarrow k\) no implica \(i\simeq_{\mathrm{idx}}k\).
5. **CE5 / no incompatibility shortcut:** el embedding tampoco decide por sí solo \(i\#k\); eso exige su criterio propio.
6. **CE6 / level explicitness:** la teoría debe declarar la relación de nivel/embedding entre ambas individuaciones. “Subsystem” no es la negación de “context”: si ambos criterios se descargan, el nivel menor es un contexto anidado realizado en el host.

Solo con una relación de este tipo puede empezar a formularse en serio una arquitectura “celular dentro de celular”. Y aun entonces:

\[
\operatorname{ContextEmbedding}^{\mathsf M}
\not\Rightarrow
\text{fractalidad}.
\]

Faltan recurrencia estructural, una noción de escala/nivel y similitud no trivial.

#### 0.11.78. La frontera puede ser endógena: TR-O frente a TR-W

La analogía celular sería demasiado pobre si toda individuación exigiera una world-making relation externa ya dada. En organismos, una frontera puede estar mantenida por la propia organización cuya unidad ayuda a constituir.

Esto no viola IA1/IA2 si distinguimos **circularidad definicional** de **dependencia constitutiva mutua**.

Sea una teoría \(\mathcal T_O\) que especifica independientemente reglas organizacionales \(\mathfrak B_{\mathcal T_O}\). Sobre presentaciones candidatas —no sobre realidades ya indexadas— esas reglas inducen un operador de actualización:

\[
\mathcal J_{\mathcal T_O}(P).
\]

Una candidatura organizacionalmente cerrada satisface:

\[
\mathcal J_{\mathcal T_O}(P_*)
\simeq
P_*,
\]

donde \(\simeq\) es equivalencia de presentación apropiada, no identidad ontológica asumida.

Para que este fixed point tenga valor individuador se exige al menos:

1. **EO1 / rule independence:** \(\mathfrak B_{\mathcal T_O}\) se especifica sin usar el \(P_*\) final, el índice resultante, RegimeTotal o REC.
2. **EO2 / non-identity operator:** \(\mathcal J_{\mathcal T_O}\) no es el operador identidad ni hace fijo todo candidato.
3. **EO3 / boundary production:** la organización genera/mantiene estructura que discrimina interior, exterior e interfaces de manera positiva.
4. **EO4 / organizational dependence:** quitar la estructura de frontera altera la organización relevante, y quitar la organización relevante impide mantener la frontera; no basta una envoltura externa accidental.
5. **EO5 / recoding robustness:** el fixed point no depende de una codificación particular.
6. **EO6 / rival-solution discipline:** múltiples fixed points incompatibles requieren criterio de nivel, equivalencia o selección independiente.
7. **EO7 / genesis sensitivity:** la aparición de un nuevo fixed point no se identifica automáticamente con ContextGenesis; debe probarse novedad constitutiva y no mera reconfiguración interna.
8. **EO8 / no totality inference:** cierre organizacional no implica RegimeTotal ni REC.

Llamemos provisionalmente a esta familia **TR-O**.

TR-W y TR-O son dos realizaciones distintas del esquema general:

\[
\boxed{
\begin{array}{ll}
\mathrm{TR\text{-}W}:&
\text{individuación por estructura world-making independently characterized;}\\
\mathrm{TR\text{-}O}:&
\text{individuación por cierre organizacional/endogenous boundary.}
\end{array}
}
\]

No se afirma que agoten las posibilidades.

La literatura sobre autopoiesis y closure of constraints sirve aquí como precedente de que una frontera mantenida endógenamente puede coexistir con apertura causal/material; no demuestra que \(R_i\) sea un organismo ni que \(\mathcal J_{\mathcal T_O}\) exista para la realidad.

#### 0.11.79. Relectura definitiva de “membrana = typing boundary + Muro + REC”

Con REV-07g avanzado podemos responder con más precisión a la intuición inicial.

La expresión:

\[
\text{membrana}
\stackrel{?}{=}
\mathrm{TB}+\mathrm{Muro}+\mathrm{REC}
\]

mezcla **fundamento de individuación** con **consecuencias/roles de una unidad ya individuada**.

TB aparece una vez que el contexto ha sido admitido y se fija su sort.

REC aparece todavía más tarde, como consecuencia de RegimeTotal.

El Muro es una restricción epistemológica sobre lo que puede certificarse desde dentro; tampoco produce por sí mismo la unidad.

Por tanto el orden correcto es:

\[
\boxed{
\text{Individuation Ground}
\Longrightarrow
\text{Context Boundary / IndexAdmission}
\Longrightarrow
\mathrm{TB}
\Longrightarrow
\text{investigación de RegimeTotal}
\Longrightarrow
\mathrm{REC},
}
\]

mientras el Muro corta transversalmente las inferencias epistémicas.

Las capas TB/OC/EB/IF de §0.11.49 siguen siendo útiles, pero deben llamarse **perfil funcional de la membrana**, no fundamento de la membrana.

En una implementación TR-W, el ground puede ser \(W\).

En una implementación TR-O, el ground puede ser una organización endógena/fixed point independientemente especificada.

Esto evita la circularidad:

\[
\mathrm{REC}
\Rightarrow
\text{“hay una célula”}
\]

que sería inválida porque REC ya presupone una totalización dentro de un contexto.

La versión fuerte de Cellular Reality queda así:

\[
\boxed{
\text{Cellular Reality}
=
\text{individuación fundamentada}
+
\text{boundary profile}
+
\text{persistencia/ontogénesis disciplinadas},
}
\]

no “todo \(R_i\) es una célula porque tiene subíndice y closure”.


#### 0.11.79a. No-R no debe reificarse como estado precursor

La intuición «si nada existiera, de algún modo tendría que surgir algo» debe separarse de una transición ontológica literal:

$$
\operatorname{NoR}
\longrightarrow
\operatorname{ExistsR}.
$$

La formulación anterior sería engañosa si se leyera como una dinámica, porque:

$$
\operatorname{NoR}
:\Longleftrightarrow
\neg\operatorname{ExistsR}
$$

es una **metasentencia**, no un objeto, sustrato, estado físico ni contexto precursor capaz de ejecutar una operación. En particular, esta ruta queda descartada:

$$
\text{Nothing}
\xrightarrow{\operatorname{Inv}}
R_i.
$$

También queda descartado inferir existencia a partir de una mera negación lógica:

$$
\neg\operatorname{ExistsR}
\not\Rightarrow
\operatorname{ExistsR}.
$$

Por tanto, si la intuición contiene una tesis metafísica defendible, no puede ser «la Nada produce algo», sino una tesis de **imposibilidad de realización de la ausencia absoluta**.

Introducimos solo como esquema de investigación un marcador metateórico:

$$
\operatorname{Null}^{\mathsf M},
$$

que **no denota una entidad**. Abrevia la candidatura límite «ausencia de toda determinación ontológica realizada». La pregunta no es qué propiedades tiene una cosa llamada Null, sino si una candidatura de ausencia absoluta puede contar coherentemente como realización.

La hipótesis fuerte sería:

$$
\boxed{
\neg\operatorname{AdmissiblyRealizable}^{\mathsf M}
(\operatorname{Null}^{\mathsf M})
}
$$

o, si una futura metalógica modal lo permite sin introducir un dominio ilícito de mundos/contextos:

$$
\neg\Diamond^{\mathsf M}\operatorname{NoR}.
$$

Esta última notación es **provisional**: REV-07g no presupone todavía una semántica modal global capaz de cuantificar sobre realizaciones de todos los contextos. No puede usarse para importar de contrabando Absolute Generality, un conjunto de mundos posibles ni un sort ontológico de índices.

#### 0.11.79b. Reductio candidato: realización implica determinación

La vía conceptualmente más fuerte no hace que la nada «actúe». Ataca la coherencia de una realización absolutamente indeterminada.

Sea, todavía esquemáticamente:

$$
\operatorname{Realization}^{\mathsf M}(C)
$$

un juicio metateórico de realización que **no** equivale por definición a `ExistsR`, RegimeTotal, IndexAdmission ni ContextIndividuation. Su contenido debe justificarse independientemente antes de hacer trabajo doctrinal.

La hipótesis mínima a investigar es:

$$
\boxed{
\operatorname{Realization}^{\mathsf M}(C)
\Rightarrow
\operatorname{Determinate}^{\mathsf M}(C).
}
$$

No significa que toda realidad deba poseer una descripción completa, clásica o bivalente. `Determinate` significa únicamente que la realización no puede ser absolutamente carente de toda diferencia ontológicamente eficaz: debe haber algún rasgo cuya presencia/ausencia, estructura, rol o límite impida identificarla con una ausencia total de determinación.

Si además `Null^M` se caracteriza exactamente por:

$$
\operatorname{Null}^{\mathsf M}(C)
\Rightarrow
\neg\operatorname{Determinate}^{\mathsf M}(C),
$$

entonces la conjunción:

$$
\operatorname{Realization}^{\mathsf M}(C)
\land
\operatorname{Null}^{\mathsf M}(C)
$$

sería incoherente bajo esas premisas.

El objetivo sería obtener un resultado del tipo:

$$
\boxed{
\operatorname{Realization}^{\mathsf M}(C)
\Rightarrow
\neg\operatorname{Null}^{\mathsf M}(C).
}
$$

Esto todavía **no demuestra** `ExistsR`. Para hacerlo harían falta al menos dos puentes independientes:

1. justificar que existe alguna `Realization^M` sin presuponer `ExistsR`;
2. demostrar que una realización así satisface la arquitectura exigida por REV-07/REV-07g hasta producir una instanciación admisible de RegimeTotal.

Sin esos puentes, la tesis solo muestra una incompatibilidad conceptual entre «realización» y «ausencia absoluta de determinación».

#### 0.11.79c. La distinción cambia de papel: de causa del ser a condición de individuación

Esta separación corrige la hipótesis anterior de una «inversión primordial».

No necesitamos postular:

$$
\text{indeterminación}
\xrightarrow{\operatorname{Inv}^{0}}
\text{primera distinción}
\xrightarrow{}
R_i.
$$

La inversión ordinaria ya presupone una distinción orientada:

$$
D=\langle A,B\rangle,
\qquad
\operatorname{Inv}(D)=\langle B,A\rangle,
$$

por lo que usar la misma operación para explicar la primera distinción sería circular salvo que `Inv^0` recibiese una semántica independiente. Mientras esa semántica no exista, `Inv^0` no debe entrar en el núcleo.

La arquitectura de investigación queda dividida en dos preguntas:

$$
\boxed{
\begin{array}{ll}
\mathrm{NQ}:&
\text{¿puede la ausencia absoluta ser una realización admisible?}\\[1mm]
\mathrm{IQ}:&
\text{dada alguna realización, ¿qué diferencia efectiva funda su individuación contextual?}
\end{array}
}
$$

Una respuesta negativa fuerte a NQ podría explicar por qué no hay No-R sin convertir la Nada en causa. Una respuesta positiva a IQ podría descargar una teoría concreta de `ContextIndividuation`.

El candidato de IQ ya no es «cualquier diferencia». Debe ser una **distinción efectiva**:

$$
\operatorname{EffDist}^{\mathsf M}_{\mathcal T}(C;\delta),
$$

donde una teoría independiente `\mathcal T` justifica que `\delta` hace una diferencia constitutiva para el corte contextual. El esquema sería:

$$
\operatorname{EffDist}^{\mathsf M}_{\mathcal T}(C;\delta)
\land
\operatorname{DistAdequate}^{\mathsf M}(\mathcal T,C,\delta)
\Rightarrow
\operatorname{Ind}_{\mathcal T}^{\mathsf M}(C;\chi_{\delta}),
$$

y solo entonces:

$$
\operatorname{Ind}_{\mathcal T}^{\mathsf M}(C;\chi_{\delta})
\land
\operatorname{IndAdequate}^{\mathsf M}(\mathcal T,C,\chi_{\delta})
\Rightarrow
\operatorname{ContextIndividuation}^{\mathsf M}(C;\chi_{\delta})
\Rightarrow
\operatorname{IndexAdmission}^{\mathsf M}
(C\Downarrow i;\chi_{\delta},\mathcal T).
$$

`DistAdequate` debe heredar al menos IA0–IA10 y añadir guards específicos:

1. **DA1 / no bare partition:** una bipartición descriptiva `A|B` no basta; debe existir estructura positiva que haga ontológicamente eficaz la diferencia.
2. **DA2 / no null reification:** `\delta` no se obtiene atribuyendo propiedades, operaciones o potencia causal a Nothing/NoR.
3. **DA3 / effectivity:** variar, eliminar o invertir la diferencia debe alterar alguna condición relevante de co-tipado, boundary production, organización o interfaces bajo `\mathcal T`; una etiqueta sin consecuencias falla.
4. **DA4 / target independence:** el efecto no se define como «aquello que produce exactamente el contexto que queremos admitir».
5. **DA5 / rival-distinction discipline:** si dos diferencias efectivas inducen cortes incompatibles del mismo nivel, se exige equivalencia, nesting explícito o rechazo de al menos una.
6. **DA6 / no free promotion:** una diferencia interna ordinaria no produce automáticamente un contexto, pero tampoco se prohíbe que una unidad interna sea un contexto anidado. Si satisface independientemente un criterio TR-W/TR-O/TR-M u otro IndAdequate, la multiplicación de contextos es una consecuencia ontológica admisible, no un error de proliferación.
7. **DA7 / genesis sensitivity:** una diferencia preexistente y una diferencia constituida por una formación deben poder distinguir SharedOntSpace de ContextGenesis.
8. **DA8 / persistence separation:** una distinción sincrónica no decide por sí sola identidad diacrónica; si descarga ContextIndividuation, PersistenceBasis/ContinuationProfile/FaithfulContinuation gobiernan después su persistencia. \(\Omega_i\) no es requisito previo.

Por tanto:

$$
\boxed{
\text{difference}
\not\Rightarrow
\text{ContextIndividuation},
}
$$

pero queda abierta la ruta:

$$
\boxed{
\text{independently grounded effective distinction}
\Rightarrow
\operatorname{Ind}_{\mathcal T}
\Rightarrow
\text{ContextIndividuation}.
}
$$

#### 0.11.79d. Stress tests para NQ/IQ

**ND1 — “el hecho de que nada exista existe”.** Se intenta refutar No-R diciendo que existe el hecho/proposición «nada existe».

Falla por cambio ilegítimo de nivel. La disponibilidad metalingüística de una sentencia no produce un hecho objeto ni una GeneUnit.

**ND2 — “Nothing tiene una propiedad”.** Se atribuye a Nothing la propiedad de ser nada, indeterminada, inestable o capaz de invertirse.

Falla DA2: reifica exactamente aquello cuya ausencia se pretendía analizar.

**ND3 — negación clásica.** De `NoR = not ExistsR` se pretende derivar `ExistsR`.

Inválido sin una premisa adicional. NQ requiere una tesis metafísica independiente sobre realizabilidad/determinación.

**ND4 — determinación semántica.** Se argumenta que, como podemos describir `Null^M`, ya está determinada.

Falla: determinación de una representación metalingüística no implica determinación ontológica de lo representado.

**ND5 — partición arbitraria.** Dada una realización, un analista selecciona cualquier predicado `P` y usa `P/not-P` como primera distinción.

Falla DA1/DA4/DA5. La distinción debe hacer trabajo world-making independientemente del interés descriptivo.

**ND6 — quantum/indeterminacy objection.** Se interpreta `Determinate^M` como valores clásicos completos y se concluye que la indeterminación física refuta el esquema.

El ataque falla contra la versión mínima: `Determinate^M` no exige valores definidos para toda magnitud; exige únicamente no-nullidad ontológica, esto es, alguna estructura/diferencia efectiva.

**ND7 — empty structure.** Una teoría formal admite una estructura con dominio vacío y la identifica con No-R.

No basta. La existencia matemática/metalingüística de una estructura vacía no demuestra que constituya una realización ontológica admisible ni que satisfaga los puentes de REV-07.

**ND8 — existence smuggling.** Se define `Realization^M(C)` de tal manera que ya implique RegimeTotal o ExistsR.

Falla metodológicamente. El reductio sería circular y no añade evidencia.

#### 0.11.79e. Resultado provisional

La investigación queda reordenada:

$$
\boxed{
\text{No-R / null-realizability problem}
\quad\text{antes de}\quad
\text{context-individuation problem}.
}
$$

La cadena heurística más prometedora es:

$$
\text{no absolute null realization}
\leadsto
\text{some ontological realization}
\leadsto
\text{effective determination}
\leadsto
\text{effective distinction}
\leadsto
\text{ContextIndividuation}
\leadsto
\text{IndexAdmission}
\leadsto
\text{REV-07 genealogy/closure}.
$$

Las flechas `\leadsto` son **obligaciones de investigación**, no implicaciones demostradas.

Esto produce una separación conceptual importante:

- la imposibilidad de No-R, si se demuestra, respondería a por qué no puede haber ausencia ontológica absoluta;
- la distinción efectiva respondería a cómo una realización obtiene una frontera/unidad contextual;
- RegimeTotal respondería a cómo esa unidad realiza exhaustivamente un régimen;
- REV-07h seguiría tratando cómo unidades ya individuadas exponen interfaces, memorizan estado relevante y pueden ser baked en otros contextos.

La hipótesis de inversión queda por ahora degradada: puede reaparecer como operación sobre distinciones ya orientadas, pero **no** se usa para producir existencia ni para fundar la primera individuación.

#### 0.11.80. REV-07h — Interface, Memoization y Baking: qué puede importar aguas abajo

REV-07e introdujo GenesisTrivialization para expresar que una rama parental compleja puede quedar representada child-side por una contribución suficiente. REV-07g mostró después que la individuación no puede darse por supuesta: el índice registra una unidad ya justificada y no crea por sí mismo el corte que etiqueta.

Estas dos líneas revelan una deuda intermedia. Si se escribe directamente:

\[
\operatorname{Bake}_{i\to k}(P_i),
\]

para una estructura compleja \(P_i\), la notación presupone silenciosamente que ya sabemos por qué exactamente \(P_i\) —con ese alcance, esa historia y esa granularidad— constituye la unidad que debe ser transportada. Sin un criterio previo, el baking puede esconder el mismo coarse-graining arbitrario que CI7/CI8 y IA6/IA8 intentan bloquear.

REV-07h separa ahora cuatro niveles conceptualmente distintos:

\[
\boxed{
\text{estructura/historia compleja}
\;\xrightarrow{\text{unitización}}\;
\text{SourceUnit}
\;\xrightarrow{\text{Interface}}\;
\text{contrato observable/causal}
\;\xrightarrow{\text{Bake}}\;
\text{realización target-native}
\;\xrightarrow[\text{cuando aplique}]{\text{ContextGenesis}}\;
\text{GenesisTrivialization}.
}
\]

La pieza central ya no es memoization aislada, sino la **interfaz**. Una interfaz determina qué aspectos de una SourceUnit pueden hacer diferencia aguas abajo y, por tanto, qué diferencias upstream pueden ser legítimamente quotientadas sin alterar el rol consumido.

Las tesis de trabajo pasan a ser:

\[
\boxed{
\textbf{The interface determines relevance.}
}
\]

\[
\boxed{
\textbf{Memoization preserves an interface through history.}
}
\]

\[
\boxed{
\textbf{Baking realizes an interface across contexts.}
}
\]

Memoization no se convierte en requisito universal de todo baking. Una entidad simple o una unidad ya individuada por una teoría independiente puede satisfacer SourceUnit y exponer una interfaz sin memoization. El requisito general es:

\[
\boxed{
\operatorname{Bake}^{\mathsf M}_{i\to k}
\text{ exige una SourceUnit y una InterfaceContract source-side independientemente justificadas.}
}
\]

Memoization es la candidata específica para estructuras históricas cuya capacidad de seguir satisfaciendo una interfaz depende de conservar estado suficiente acerca de su pasado.

#### 0.11.81. SourceUnit: el contrato previo a cualquier baking

Introducimos el juicio metateórico:

\[
\operatorname{SourceUnit}^{\mathsf M}_i(u_i;\rho,\upsilon),
\]

leído: \(u_i\) está suficientemente individuado dentro de \(i\) para desempeñar el rol \(\rho\), bajo el witness de unitización \(\upsilon\).

\(\rho\) es explícito porque una estructura puede constituir una unidad para una familia de dependencias sin ser una unidad absoluta para toda descripción posible. \(\upsilon\) registra qué fundamento hace legítimo el corte: puede ser memoization, una estructura organizacional, un criterio world-making theory-specific o cualquier descarga independiente compatible con REV-07g.

SourceUnit debe satisfacer al menos:

1. **SU1 / source actuality:** el contenido cuya unidad se afirma pertenece realmente a \(i\); una descripción externa no fabrica la unidad.
2. **SU2 / non-arbitrary scope:** el corte no se elige post hoc para producir el resultado baked deseado.
3. **SU3 / role explicitness:** se declara qué familia de usos, dependencias o continuaciones fija \(\rho\).
4. **SU4 / recoding invariance:** recodificaciones fieles no cambian la unidad por accidente notacional.
5. **SU5 / anti-aggregation:** envolver estructuras independientes en una representación conjunta no crea una SourceUnit sin estructura integradora adicional.
6. **SU6 / temporal discipline:** para fuentes diacrónicas, la identidad no se reduce a igualdad de componentes instantáneos.
7. **SU7 / no context promotion:** ser SourceUnit para \(\rho\) no implica ContextIndividuation, IndexAdmission, RegimeTotal ni REC.

Por tanto:

\[
\boxed{
\operatorname{SourceUnit}^{\mathsf M}_i(u_i;\rho,\upsilon)
\not\Rightarrow
\operatorname{ContextIndividuation}^{\mathsf M}(u_i).
}
\]

Esta guardia es esencial: un subsistema, proceso, organismo o máquina puede ser una unidad funcionalmente robusta dentro de \(R_i\) sin convertirse por ello en un nuevo contexto \(R_j\).

#### 0.11.81a. InterfaceContract: el límite de relevancia downstream

Introducimos el juicio metateórico:

\[
\operatorname{InterfaceContract}^{\mathsf M}_i
(u_i;I_i^\rho,\rho,\iota),
\]

leído: la SourceUnit \(u_i\) expone, para el rol \(\rho\), una interfaz \(I_i^\rho\) cuya semántica está justificada por el witness \(\iota\).

\(I_i^\rho\) no es necesariamente un conector físico, una superficie espacial ni un objeto adicional. Puede ser una familia de magnitudes, eventos, operaciones, mensajes, disposiciones, invariantes o trazas a través de las cuales otra estructura depende de \(u_i\).

El caso intuitivo es una fuente eléctrica conectada a un ordenador. La historia upstream puede contener generación nuclear, solar, baterías, red, transformación y regulación. El ordenador no necesita que esas historias sean idénticas. Necesita que la interfaz eléctrica relevante satisfaga su contrato dentro de tolerancias admisibles.

Formalmente, sea:

\[
\operatorname{Tr}_{I^\rho}(u_i)
\]

la familia de trazas/comportamientos que \(u_i\) puede presentar a través de \(I^\rho\). Definimos equivalencia de interfaz:

\[
\boxed{
u_i
\equiv^{\mathsf M}_{I^\rho}
v_j
\Longleftrightarrow
\operatorname{Tr}_{I^\rho}(u_i)
\simeq_\rho
\operatorname{Tr}_{I^\rho}(v_j),
}
\]

donde la comparación cross-index es estrictamente metateórica y \(\simeq_\rho\) compara solo la estructura declarada por el contrato.

La consecuencia conceptual es:

\[
u_i\not\simeq v_j
\]

puede coexistir con:

\[
u_i\equiv^{\mathsf M}_{I^\rho}v_j.
\]

Por tanto la equivalencia de interfaz no afirma identidad de source, historia ni contexto. Afirma **indistinguibilidad respecto de lo que el consumidor puede recibir mediante ese contrato**.

#### 0.11.81b. Obligaciones IC1–IC10 de una interfaz admisible

Para que una interfaz haga trabajo ontológico y no sea una proyección escogida a conveniencia, exigimos:

1. **IC1 / source grounding:** la interfaz depende de estructura real de la SourceUnit; no es solo una lista externa de observables seleccionados por el analista.
2. **IC2 / consumer relevance:** cada dimensión del contrato tiene una semántica que explica qué dependencia aguas abajo puede afectar.
3. **IC3 / contract independence:** el contrato se fija independientemente de qué sources concretos se quiere hacer equivalentes.
4. **IC4 / trace adequacy:** las trazas retenidas son suficientes para discriminar todas las diferencias que la teoría considera relevantes para \(\rho\).
5. **IC5 / no hidden bypass:** ninguna dependencia atribuida al rol puede saltarse la interfaz y depender de estructura upstream que el contrato declara irrelevante.
6. **IC6 / recoding invariance:** implementaciones o codificaciones fieles preservan la equivalencia de interfaz.
7. **IC7 / non-vacuity:** una interfaz vacía o constante no puede trivializar universalmente sources salvo que la teoría demuestre que el rol es realmente trivial.
8. **IC8 / compositional discipline:** conectar interfaces no autoriza por sí solo a identificar sus SourceUnit ni sus contextos.
9. **IC9 / provenance retention:** equivalencia de interfaz no borra provenance objetiva ni convierte historias distintas en una única historia.
10. **IC10 / no context inference:** compartir interfaz o ser interface-equivalent no implica SharedOntSpace, ContextIndividuation, IndexAdmission ni RegimeTotal.

IC5 es la obligación crítica. Si el consumidor puede depender de una diferencia upstream por una vía no representada en \(I^\rho\), la interfaz no screens off esa diferencia y no puede justificar quotient baking.

#### 0.11.81c. El kernel legítimo viene de la interfaz

REV-07h había exigido en B7 un declared kernel para impedir que un Bake no inyectivo borrase diferencias arbitrarias. La interfaz proporciona ahora el fundamento de ese kernel.

Definimos:

\[
\ker(I^\rho)
:=
\{
(u,v)
\mid
u\equiv^{\mathsf M}_{I^\rho}v
\}.
\]

No se exige que este kernel sea un conjunto objeto; la notación resume metateóricamente la equivalencia inducida por el contrato.

El principio de soundness de quotient baking pasa a ser:

\[
\boxed{
\ker(\operatorname{Bake}^{\rho,\beta})
\subseteq
\ker(I^\rho),
}
\]

entendido de nuevo metateóricamente.

Es decir: Bake puede colapsar menos diferencias de las que la interfaz tolera, pero no más. Si:

\[
\operatorname{Bake}(u)
=
\operatorname{Bake}(v)
\]

mientras:

\[
u\not\equiv^{\mathsf M}_{I^\rho}v,
\]

la igualdad de outputs es una **colisión no autorizada**, no SignatureConvergence legítima.

Esto invierte la dependencia anterior:

\[
\boxed{
\text{el quotient no lo decide Bake;}
\quad
\text{lo licencia la semántica de la interfaz.}
}
\]

#### 0.11.81d. Factorización por interfaz

La forma más fuerte del screening-off puede escribirse:

\[
u_i
\longrightarrow
I_i^\rho
\longrightarrow
C_k,
\]

donde \(C_k\) representa dependencias/consecuencias target-side asociadas al rol.

La condición de interfaz exige que, para esas consecuencias:

\[
\boxed{
\text{Upstream detail}
\perp
C_k
\mid
I^\rho,
}
\]

usando \(\perp\) solo como notación estructural de screening-off, no como independencia probabilística salvo teoría adicional.

Equivalentemente: una vez fijada la realización de \(I^\rho\), diferencias upstream que pertenecen a \(\ker(I^\rho)\) no deben alterar ninguna consecuencia declarada como dependiente únicamente de ese rol.

Esta es la versión conceptualmente más precisa del antiguo GT3/GT4.

#### 0.11.81e. Toy eléctrico: provenance distinta, interfaz equivalente

Sean dos historias upstream:

\[
P_{\mathrm{nuc}},
\qquad
P_{\mathrm{solar}},
\]

con estructuras internas y provenance distintas:

\[
P_{\mathrm{nuc}}
\not\simeq
P_{\mathrm{solar}}.
\]

Supóngase que ambas alimentan una interfaz eléctrica \(I_{\mathrm{AC}}\) cuyo contrato exige, esquemáticamente:

\[
\langle
V(t),f(t),\operatorname{stability}(t),\operatorname{protection}(t)
\rangle
\in
\mathcal A_{\mathrm{AC}},
\]

para una región admisible \(\mathcal A_{\mathrm{AC}}\).

Si ambas histories producen el mismo conjunto relevante de trazas dentro de ese contrato:

\[
P_{\mathrm{nuc}}
\equiv^{\mathsf M}_{I_{\mathrm{AC}}}
P_{\mathrm{solar}},
\]

un consumidor cuya dependencia factoriza completamente por \(I_{\mathrm{AC}}\) no necesita reconstruir cuál de las dos histories upstream obtuvo.

Pero la provenance sigue siendo distinta:

\[
\operatorname{Prov}(P_{\mathrm{nuc}})
\neq
\operatorname{Prov}(P_{\mathrm{solar}}).
\]

El toy muestra exactamente la distinción buscada:

\[
\boxed{
\text{downstream equivalence}
\neq
\text{upstream identity}.
}
\]


#### 0.11.81f. Trace semantics: la interfaz como frontera observacional interactiva

La notación \(\operatorname{Tr}_{I^\rho}(u)\) anterior era deliberadamente esquemática. Para que IC4 e IC5 no puedan satisfacerse por elección del analista, fijamos ahora una semántica de trazas explícita.

Un contrato de interfaz para el rol \(\rho\) contiene los datos:

\[
\mathbb I^\rho
=
\left\langle
\Sigma^\rho,
\Gamma^\rho,
\pi^\rho,
\mathcal Q^\rho,
\mathfrak B^\rho
\right\rangle .
\]

Su lectura es:

- \(\Sigma^\rho\): firma de frontera tipada, con polaridad source/consumer cuando proceda, dominios de valores y estructura temporal/ordenada exigida por el rol;
- \(\Gamma^\rho\): familia independientemente fijada de interacciones, cargas, probes o estrategias de consumidor admisibles;
- \(\pi^\rho\): proyección de una ejecución source-side actual sobre la traza que cruza la frontera declarada;
- \(\mathcal Q^\rho\): familia de tests observacionales role-relevant, fijada antes de comparar sources concretos;
- \(\mathfrak B^\rho\): semántica de branching exigida por el rol. Puede conservar conjuntos de posibilidades, medidas de probabilidad, tiempo, fairness u otra estructura; no puede degradarlas silenciosamente a mera existencia.

Para una SourceUnit \(u_i\) y una interacción \(\gamma\in\Gamma^\rho\), sea:

\[
\operatorname{Exec}_i(u_i;\gamma)
\]

la familia de ejecuciones admisibles de \(u_i\) bajo \(\gamma\). Para \(e\in\operatorname{Exec}_i(u_i;\gamma)\):

\[
\tau
=
\pi^\rho(e)
\in
\operatorname{Trace}(\Sigma^\rho).
\]

La observación role-relative de una traza es:

\[
\operatorname{Obs}_{\mathbb I^\rho}(\tau)
:=
\left\langle
q(\tau)
\right\rangle_{q\in\mathcal Q^\rho}.
\]

Si algún \(q\) es parcial, la definedness forma parte del resultado; dos trazas no son equivalentes porque un test quede silenciosamente indefinido en una de ellas.

Definimos equivalencia de trazas por:

\[
\boxed{
\tau
\approx_{\mathbb I^\rho}
\tau'
\Longleftrightarrow
\forall q\in\mathcal Q^\rho\;
q(\tau)=q(\tau').
}
\]

El perfil completo de interfaz de \(u_i\) es:

\[
\boxed{
\operatorname{Prof}_{\mathbb I^\rho}(u_i)(\gamma)
:=
\mathfrak B^\rho
\left(
\left\{
\operatorname{Obs}_{\mathbb I^\rho}(\pi^\rho(e))
\mid
e\in\operatorname{Exec}_i(u_i;\gamma)
\right\}
\right).
}
\]

Por tanto la equivalencia source-side inducida por la interfaz queda finalmente definida como:

\[
\boxed{
u_i
\equiv^{\mathsf M}_{\mathbb I^\rho}
v_j
\Longleftrightarrow
\forall\gamma\in\Gamma^\rho\;
\operatorname{Prof}_{\mathbb I^\rho}(u_i)(\gamma)
=
\operatorname{Prof}_{\mathbb I^\rho}(v_j)(\gamma).
}
\]

La igualdad anterior es metateórica. No exige que \(i=j\), no introduce un objeto que contenga ambos contexts y no identifica sus tokens. Solo compara las conductas expuestas por un contrato comúnmente interpretable.

Esta definición corrige tres ambigüedades de la versión esquemática:

1. una interfaz puede ser **interactiva**: no se compara un único output, sino la respuesta bajo toda interacción admisible;
2. una interfaz puede ser **no determinista, probabilística o temporal**: \(\mathfrak B^\rho\) debe conservar precisamente la estructura que el rol considere relevante;
3. el quotient no se elige sobre sources directamente: se induce desde tests \(\mathcal Q^\rho\) y estrategias \(\Gamma^\rho\) justificadas independientemente.

Si todos los tests usan igualdad ordinaria sobre sus codominios, \(\approx_{\mathbb I^\rho}\) es automáticamente reflexiva, simétrica y transitiva. Igualdad punto a punto de perfiles hereda esas propiedades, de modo que:

\[
\boxed{
\equiv^{\mathsf M}_{\mathbb I^\rho}
\text{ es una relación de equivalencia}
}
\]

sobre toda clase de SourceUnits para la que el contrato esté bien tipado. Esto descarga la parte de la deuda de REV-07h relativa a que la equivalencia de interfaz no sea una semejanza informal.

#### 0.11.81g. IC1–IC10 como obligaciones formales

La interfaz admisible no se define solo por poseer el tuple anterior. El witness \(\iota\) debe descargar las diez obligaciones siguientes.

**IC1 — source grounding.** Toda observación no aportada por el entorno debe anclarse en una ejecución actual de la SourceUnit:

\[
\forall e\in\operatorname{Exec}_i(u_i;\gamma)\;
\operatorname{GroundedTrace}_i
\bigl(
u_i,e,\pi^\rho(e)
\bigr).
\]

GroundedTrace exige que cada símbolo, magnitud o evento source-polar de la traza tenga un anchor causal, constitutivo o realizativo en \(e\). Una columna inventada por el analista no satisface IC1.

**IC2 — consumer relevance.** Cada test del contrato debe corresponder a una dependencia downstream independently specified:

\[
\forall q\in\mathcal Q^\rho\;
\exists d\in\operatorname{Dep}_\rho\;
\operatorname{Sensitive}(d,q).
\]

Sensitive no significa que toda variación de \(q\) cambie de hecho todo consumidor, sino que \(q\) distingue una dimensión cuya variación está autorizada por la teoría del rol para cambiar alguna consecuencia downstream. Tests puramente decorativos no descargan IC2.

**IC3 — contract independence.** La especificación del contrato se fija sin nombrar los pares que se desean colapsar ni su resultado baked:

\[
\operatorname{IndependentSpec}^{\mathsf M}
\bigl(
\mathbb I^\rho,\rho
\bigr).
\]

En particular, \(\Gamma^\rho\), \(\mathcal Q^\rho\) y \(\mathfrak B^\rho\) no pueden elegirse después de observar qué diferencias separan justo a \(u\) de \(v\). El witness \(\iota\) debe aportar el fundamento externo del contrato: estándar físico, protocolo, semántica operacional, estructura receptor-ligando, contrato de API, teoría causal u otra fuente independiente.

**IC4 — trace adequacy.** Sea \(\operatorname{RelDist}_\rho(u,v)\) una diferencia role-relevant definida sin usar \(\mathbb I^\rho\). La interfaz debe ser completa respecto de esas diferencias:

\[
\boxed{
\operatorname{RelDist}_\rho(u,v)
\Longrightarrow
\operatorname{Prof}_{\mathbb I^\rho}(u)
\neq
\operatorname{Prof}_{\mathbb I^\rho}(v).
}
\]

Equivalentemente:

\[
u\equiv^{\mathsf M}_{\mathbb I^\rho}v
\Longrightarrow
\neg\operatorname{RelDist}_\rho(u,v).
\]

Así el perfil puede olvidar diferencias upstream solo cuando la teoría del rol ya las ha declarado irrelevantes por razones independientes.

**IC5 — no hidden bypass.** Toda consecuencia atribuida exclusivamente al rol debe factorizar por el perfil de interfaz. Para cada consumidor admisible \(C\) existe una aplicación role-side \(\widehat D_{C,\rho}\) tal que:

\[
\boxed{
D_{C,\rho}(u;\gamma)
=
\widehat D_{C,\rho}
\left(
\operatorname{Prof}_{\mathbb I^\rho}(u)(\gamma)
\right).
}
\]

Cuando la teoría dispone de un grafo o hipergrafo de dependencia, se exige además la forma estructural:

\[
\forall p\in
\operatorname{Path}_\rho(u\leadsto C):
\qquad
p\cap
\operatorname{Boundary}_{\mathbb I^\rho}(u)
\neq
\varnothing .
\]

La segunda fórmula convierte la interfaz en un cut de dependencia para el rol. Si existe un camino relevante que llega al consumidor sin atravesar la frontera representada, hay hidden bypass y el contrato falla.

**IC6 — recoding invariance.** Para toda recodificación fiel \(\alpha:u\cong u'\) que preserve la estructura source-side relevante existe la recodificación inducida \(\bar\alpha\) de trazas/perfiles y:

\[
\operatorname{Prof}_{\alpha\mathbb I^\rho}(\alpha u)
=
\bar\alpha
\left(
\operatorname{Prof}_{\mathbb I^\rho}(u)
\right).
\]

En particular:

\[
u\equiv_{\mathbb I^\rho}v
\Longleftrightarrow
\alpha u
\equiv_{\alpha\mathbb I^\rho}
\alpha v.
\]

**IC7 — non-vacuity.** Si el rol es no trivial:

\[
\operatorname{NonTrivialRole}(\rho),
\]

entonces el perfil no puede ser universalmente constante:

\[
\boxed{
\left|
\operatorname{Im}
\left(
\operatorname{Prof}_{\mathbb I^\rho}
\right)
\right|
\ge 2.
}
\]

Si la imagen tiene una sola clase, la carga de prueba se invierte: debe demostrarse \(\operatorname{TrivialRole}(\rho)\), no declararse irrelevante toda diferencia por conveniencia.

**IC8 — compositional discipline.** Cuando dos contratos admiten una operación de composición \(\otimes\), debe existir un witness de congruencia:

\[
u\equiv_{\mathbb I^\rho}u'
\land
v\equiv_{\mathbb J^\sigma}v'
\Longrightarrow
u\otimes v
\equiv_{\mathbb I^\rho\otimes\mathbb J^\sigma}
u'\otimes v'.
\]

Pero no se admite ninguna regla inversa desde composición o equivalencia hacia identidad de SourceUnit, common ground o identidad de contexto.

**IC9 — provenance retention.** El quotient observacional no es un quotient ontológico de historias:

\[
u\equiv_{\mathbb I^\rho}v
\not\Rightarrow
\operatorname{Prov}(u)=\operatorname{Prov}(v).
\]

La provenance continúa definida sobre los sources/historias pre-quotient. Si un artefacto downstream no la codifica, puede dejar de ser reconstruible desde ese canal, pero no deja retroactivamente de haber sido distinta.

**IC10 — no context inference.** Ninguna de las siguientes inferencias está licenciada:

\[
u_i\equiv^{\mathsf M}_{\mathbb I^\rho}v_j
\not\Rightarrow
i\equiv j,
\]

\[
u_i\equiv^{\mathsf M}_{\mathbb I^\rho}v_j
\not\Rightarrow
\operatorname{SharedOntSpace}^{\mathsf M}(i,j),
\]

\[
u_i\equiv^{\mathsf M}_{\mathbb I^\rho}v_j
\not\Rightarrow
\operatorname{ContextIndividuation}^{\mathsf M},
\operatorname{IndexAdmission}^{\mathsf M},
\operatorname{RegimeTotal}.
\]

IC10 es una restricción de regla de inferencia, no una afirmación de que contexts incompatibles deban compartir interfaces. Solo permite que el metalenguaje compare contratos cuando exista traducción suficiente para ello.

Con estas cláusulas:

\[
\boxed{
\operatorname{InterfaceContract}^{\mathsf M}_i
(u_i;\mathbb I^\rho,\rho,\iota)
}
\]

significa que \(u_i\) es SourceUnit para \(\rho\), que \(\mathbb I^\rho\) está bien tipada y que \(\iota\) descarga IC1–IC10.

#### 0.11.81h. Teoremas de sustitución y del kernel de Bake

**IT-1 — downstream substitutability.** Si IC4 e IC5 están descargadas y:

\[
u\equiv^{\mathsf M}_{\mathbb I^\rho}v,
\]

entonces para todo consumidor \(C\), interacción \(\gamma\) y consecuencia atribuida exclusivamente al rol:

\[
\boxed{
D_{C,\rho}(u;\gamma)
=
D_{C,\rho}(v;\gamma).
}
\]

**Demostración.** Por equivalencia de interfaz:

\[
\operatorname{Prof}_{\mathbb I^\rho}(u)(\gamma)
=
\operatorname{Prof}_{\mathbb I^\rho}(v)(\gamma).
\]

Por IC5 ambos lados pasan por la misma \(\widehat D_{C,\rho}\). Sustituyendo se obtiene igualdad de la consecuencia downstream. IC4 garantiza que la equivalencia no ha omitido previamente una diferencia que la teoría de \(\rho\) declarase relevante. \(\square\)

Este es el screening-off que antes solo se expresaba intuitivamente.

Sea ahora:

\[
q_{\mathbb I^\rho}(u)
:=
[u]_{\equiv_{\mathbb I^\rho}}
\]

el quotient metateórico inducido por la interfaz.

Una realización baked:

\[
B
=
\operatorname{Bake}^{\rho,\beta}
\]

es **interface-sound** si existe un decoder/realization map target-side \(d_\beta\) tal que:

\[
\boxed{
d_\beta(B(u))
=
q_{\mathbb I^\rho}(u).
}
\]

La dirección de esta factorización es importante: el output baked debe conservar información suficiente para recuperar la clase de interfaz. No se exige que el Bake sea él mismo el quotient mínimo.

**IT-2 — Bake kernel theorem.** Si existe \(d_\beta\) como arriba, entonces:

\[
\boxed{
\ker(B)
\subseteq
\ker(\mathbb I^\rho).
}
\]

**Demostración.** Si \(B(u)=B(v)\), aplicar \(d_\beta\) da:

\[
q_{\mathbb I^\rho}(u)
=
d_\beta(B(u))
=
d_\beta(B(v))
=
q_{\mathbb I^\rho}(v).
\]

Por definición del quotient:

\[
u\equiv_{\mathbb I^\rho}v.
\]

Luego todo par colapsado por Bake ya estaba autorizado por la equivalencia de interfaz. \(\square\)

Esto también aclara una sutileza categorial de la arquitectura: la condición correcta para permitir que Bake preserve **más** información que la interfaz es:

\[
q_{\mathbb I^\rho}
=
d_\beta\circ B,
\]

no \(B=\bar B\circ q_{\mathbb I^\rho}\). Esta última igualdad impondría la inclusión opuesta de kernels y correspondería a un Bake que depende solo del quotient.

Si además se exige minimalidad:

\[
u\equiv_{\mathbb I^\rho}v
\Longrightarrow
B(u)=B(v),
\]

entonces:

\[
\boxed{
\ker(B)
=
\ker(\mathbb I^\rho),
}
\]

y el Bake es un quotient exacto del contrato.

#### 0.11.81i. Modelo no trivial A — transductor stateful y quotient baking exacto

Sea una SourceUnit computacional implementada como máquina de Mealy determinista:

\[
M=(Q,q_0,A,B,\delta,\lambda),
\]

con estado interno \(Q\), alfabeto de inputs \(A\), outputs \(B\), transición \(\delta\) y output \(\lambda\).

El rol \(\rho_{\mathrm{IO}}\) es suministrar la transducción interactiva declarada por \(A/B\). El contrato fija:

\[
\Gamma^{\rho_{\mathrm{IO}}}
=
A^*,
\]

y para cada palabra de input \(w\in A^*\), la ejecución única de \(M\) produce una traza input/output:

\[
\tau_M(w).
\]

Tomamos como tests todos los observables de output tipados del protocolo; equivalentemente, el perfil es la función de transducción:

\[
F_M:A^*\to B^*.
\]

Entonces:

\[
\boxed{
M\equiv_{\mathbb I^{\rho_{\mathrm{IO}}}}N
\Longleftrightarrow
\forall w\in A^*:
F_M(w)=F_N(w).
}
\]

No se compara solo el output actual: se compara toda continuación input finita, por lo que estados internamente distintos se identifican únicamente cuando son observacionalmente indistinguibles para el rol.

Las obligaciones IC1–IC10 quedan descargadas así:

- **IC1:** cada símbolo de traza proviene de una transición efectiva de \(M\) o del input aportado por el entorno;
- **IC2:** \(A/B\) son precisamente los actos que el consumidor del protocolo puede emitir/recibir;
- **IC3:** el protocolo \(A/B\) y la familia \(A^*\) se fijan antes de elegir \(M,N\);
- **IC4:** cualquier diferencia role-relevant es, por definición operacional independiente del protocolo, una palabra \(w\) para la que difiere el output; \(A^*\) contiene ese discriminador;
- **IC5:** el modelo cerrado solo permite interacción source/consumer mediante las transiciones etiquetadas \(A/B\), de modo que todo path de dependencia atraviesa la frontera;
- **IC6:** renombrar estados internos por una biyección preserva \(F_M\);
- **IC7:** existen transductores con distinta respuesta para alguna palabra de \(A^*\), luego el perfil no es constante;
- **IC8:** la composición serial de transductores compatibles respeta equivalencia observacional; sustituir un componente por otro con la misma transducción conserva la transducción compuesta;
- **IC9:** dos grafos internos o histories de construcción distintos pueden implementar el mismo \(F_M\); la igualdad de perfil no iguala su provenance;
- **IC10:** dos realizaciones situadas en contexts distintos pueden implementar la misma transducción; de ello no se deriva identidad ni espacio ontológico compartido.

Definimos ahora:

\[
\operatorname{Bake}_{\min}(M)
:=
\operatorname{Canon}
\left(
\operatorname{MinMealy}(M)
\right),
\]

donde MinMealy identifica exactamente estados con la misma conducta futura y Canon elimina el accidente del nombre de estados.

Por unicidad de la realización determinista mínima hasta isomorfismo y por canonicalización:

\[
\boxed{
\operatorname{Bake}_{\min}(M)
=
\operatorname{Bake}_{\min}(N)
\Longleftrightarrow
M\equiv_{\mathbb I^{\rho_{\mathrm{IO}}}}N.
}
\]

Luego, en este modelo no trivial:

\[
\boxed{
\ker(\operatorname{Bake}_{\min})
=
\ker(\mathbb I^{\rho_{\mathrm{IO}}}).
}
\]

El ejemplo demuestra que quotient baking puede ser exacto sin convertir equivalencia de interfaz en identidad ontológica.

#### 0.11.81j. Modelo no trivial B — servicio key/value event-sourced frente a snapshot

Considérese un servicio stateful con operaciones:

\[
\operatorname{Put}(k,v),\qquad
\operatorname{Get}(k),\qquad
\operatorname{Delete}(k),
\]

y respuestas:

\[
\operatorname{Ack},
\qquad
\operatorname{Value}(v),
\qquad
\operatorname{NotFound}.
\]

El rol \(\rho_{\mathrm{KV}}\) se fija por la semántica operacional del servicio. \(\Gamma^{\rho_{\mathrm{KV}}}\) contiene todas las secuencias finitas well-typed de requests autorizadas. La traza conserva orden de request/response y, si el contrato lo exige, versión, errores y límites temporales; nada de ello puede omitirse después para hacer coincidir dos implementaciones.

Sean:

- \(E\): implementación event-sourced que conserva el log completo;
- \(S\): implementación snapshot que conserva solo el mapa actual más metadatos suficientes.

Supóngase mismo estado inicial y las reglas operacionales usuales:

\[
\begin{aligned}
\operatorname{Put}(k,v)&: m[k]\leftarrow v,\\
\operatorname{Delete}(k)&: m\leftarrow m\setminus\{k\},\\
\operatorname{Get}(k)&:
\begin{cases}
\operatorname{Value}(m[k]) & k\in\operatorname{dom}(m),\\
\operatorname{NotFound} & \text{en otro caso}.
\end{cases}
\end{aligned}
\]

Por inducción sobre la longitud de toda secuencia \(w\in\Gamma^{\rho_{\mathrm{KV}}}\), \(E\) y \(S\) alcanzan el mismo mapa abstracto tras cada prefijo y emiten la misma respuesta observable. Por tanto:

\[
\boxed{
E
\equiv_{\mathbb I^{\rho_{\mathrm{KV}}}}
S.
}
\]

Sin embargo:

\[
\operatorname{Prov}(E)
\neq
\operatorname{Prov}(S),
\]

y la información histórica recuperable puede diferir drásticamente.

IC1–IC10 se descargan porque la semántica del protocolo y sus operaciones fija independientemente el rol; la inducción sobre todas las request sequences prueba IC4; el modelo de servicio encapsulado impone IC5; cambios de serialización que preservan requests/responses descargan IC6; Put/Get proporcionan no-vacuidad; la composición con un cliente que solo usa el contrato conserva sustitución; provenance permanece separada; y ninguna equivalencia de servicio induce contexto.

Este modelo conecta directamente con Memoization. El snapshot puede convertirse después en candidato a MemoState, pero su suficiencia no se obtiene por llamarlo snapshot: se obtiene porque el estado actual es suficiente para reproducir todas las continuaciones del contrato KV. Si el protocolo añadiese una operación:

\[
\operatorname{History}(k),
\]

la prueba anterior dejaría de valer. La historia pasaría a ser role-relevant, IC4 detectaría la diferencia y \(E\not\equiv_{\mathbb I^{\rho_{\mathrm{KV}}}}S\). La interfaz, no el deseo de comprimir, decide qué puede olvidarse.

#### 0.11.81k. Modelo no trivial C — interfaz eléctrica bajo cargas variables

Para comprobar que la semántica no depende de ejemplos puramente computacionales, considérese el rol:

\[
\rho_{\mathrm{AC}}
=
\text{entrega eléctrica a un consumidor a través de un puerto declarado}.
\]

La firma de frontera puede incluir, según el contrato físico:

\[
\Sigma^{\rho_{\mathrm{AC}}}
=
\left\langle
V(t),
I(t),
f(t),
\operatorname{THD}(t),
I_{\mathrm{PE}}(t),
\operatorname{Protection}(t)
\right\rangle .
\]

\(\Gamma^{\rho_{\mathrm{AC}}}\) no contiene una sola carga nominal, sino una familia independiente de perfiles de carga admisibles:

\[
\gamma:t\mapsto Z_\gamma(t)
\]

dentro del envelope de operación. Los tests \(\mathcal Q^{\rho_{\mathrm{AC}}}\) miden únicamente magnitudes que el estándar/teoría de power delivery haya justificado como relevantes: tensión RMS, frecuencia, transitorios, armónicos, leakage, respuesta de protección y las demás que el rol requiera.

Sean dos assemblies upstream físicamente distintos:

\[
P_{\mathrm{grid}},
\qquad
P_{\mathrm{inv}},
\]

por ejemplo red+transformación frente a batería+inversor+regulación. Para obtener una descarga no tautológica, supóngase que dentro del bandwidth y envelope declarados ambos realizan la misma relación de puerto de Thévenin:

\[
V(t)
=
V_{\mathrm{oc}}(t)
-
(Z_{\mathrm{out}}*I)(t),
\]

con el mismo \(V_{\mathrm{oc}}\), la misma impedancia operacional \(Z_{\mathrm{out}}\) y la misma función de protección role-relevant. Para toda carga admisible \(\gamma\), cuya ley de respuesta puede escribirse:

\[
I
=
L_\gamma[V],
\]

el par cerrado fuente+carga satisface en ambos casos exactamente la misma ecuación de frontera:

\[
V
=
V_{\mathrm{oc}}
-
Z_{\mathrm{out}}*L_\gamma[V].
\]

Cuando esa ecuación tiene la misma solución admisible bajo las condiciones del contrato, ambas fuentes inducen los mismos \(V/I\) y, por construcción, los mismos observables derivados \(f,\operatorname{THD},I_{\mathrm{PE}}\) y estados de protección incluidos en \(\mathcal Q^{\rho_{\mathrm{AC}}}\). Por tanto:

\[
\forall\gamma\in\Gamma^{\rho_{\mathrm{AC}}}:
\operatorname{Prof}_{\mathbb I^{\rho_{\mathrm{AC}}}}
(P_{\mathrm{grid}})(\gamma)
=
\operatorname{Prof}_{\mathbb I^{\rho_{\mathrm{AC}}}}
(P_{\mathrm{inv}})(\gamma),
\]

y se deriva:

\[
\boxed{
P_{\mathrm{grid}}
\equiv_{\mathbb I^{\rho_{\mathrm{AC}}}}
P_{\mathrm{inv}}.
}
\]

La equivalencia es de puerto dentro del envelope contractual, no identidad física de las fuentes. Fuera de ese bandwidth, con otra clase de cargas o si la protección deja de coincidir, la conclusión no está licenciada.

La descarga de IC1–IC10 exige aquí una condición física adicional que hace al criterio falsable: el puerto declarado debe ser un cut efectivo para el rol. En un test rig con acoplos relevantes confinados al puerto eléctrico, IC5 se satisface. Si el consumidor también cambia por calor radiado, campo electromagnético, vibración, ground coupling u otra vía no representada, entonces:

\[
\operatorname{HiddenBypass}_{\rho_{\mathrm{AC}}}
\]

y el InterfaceContract falla hasta ampliar la frontera o restringir correctamente el rol.

Así el ejemplo no obtiene equivalencia simplemente ignorando diferencias incómodas. La posibilidad de un bypass físico es precisamente un falsador del contrato.

IC1 se descarga anclando las magnitudes en interacciones físicas del puerto; IC2 por la dependencia del receptor respecto de esas magnitudes; IC3 por el estándar/envelope fijado independientemente de la fuente; IC4 por barrer todas las cargas/tests declarados; IC5 por la condición de cut; IC6 por invariancia bajo cambio fiel de instrumentación/unidades; IC7 porque perfiles fuera de tolerancia son distinguibles; IC8 porque conectar un receptor no identifica fuente y receptor; IC9 porque grid e inverter conservan provenance distinta; IC10 porque una interfaz físicamente equivalente no decide por sí sola ninguna tesis sobre identidad de contexto.

#### 0.11.81l. Resultado de la descarga IC

Los tres modelos cubren estructuras distintas:

\[
\begin{array}{c|c|c|c}
\text{modelo}
&
\text{interacción}
&
\text{estado}
&
\text{riesgo principal}
\\
\hline
\text{Mealy}
&
\text{discreta/adversarial}
&
\text{interno}
&
\text{quotient arbitrario}
\\
\text{KV}
&
\text{secuencial}
&
\text{histórico}
&
\text{pérdida de historia relevante}
\\
\text{AC}
&
\text{continua/física}
&
\text{dinámico}
&
\text{hidden bypass}
\end{array}
\]

REV-07h obtiene por tanto una descarga formal no meramente verbal de InterfaceContract/trace semantics:

\[
\boxed{
\operatorname{InterfaceContract}
=
\text{trace profile interactivo}
+
\text{IC1--IC10}
+
\text{witness independiente}.
}
\]

Y dos resultados ya pueden elevarse a lemas de la arquitectura:

\[
\boxed{
u\equiv_{\mathbb I^\rho}v
+
\mathrm{IC5}
\Longrightarrow
\text{downstream substitutability para }\rho,
}
\]

\[
\boxed{
q^S_{\Theta}
=
d_\beta
\circ
q^T_{\Theta,k}
\circ
\operatorname{Bake}
\Longrightarrow
\equiv^\beta_{T,\Theta}
\subseteq
E^S_\Theta.
}
\]

La forma con quotient target contractual se desarrolla y generaliza en §0.11.87; evita identificar el kernel de Bake con igualdad literal de tokens target.

Esto cierra la deuda específica de **formalizar InterfaceContract/trace semantics y demostrar IC1–IC10 en ejemplos no triviales**. Las deudas posteriores de RoleAdequate, memo-equivalence composicional, update/invalidation, ContinuationProfile y TR-M quedan resueltas más adelante en REV-07h; permanecen abiertos InterfaceWall fuerte y la posible inducción de \(\Omega_i\).


#### 0.11.82. Memoization no es hashing: equivalencia por continuaciones

Sea \(\mathcal H_i\) una familia de historias/configuraciones source-side admisibles y sea \(\mathbb I_i^\rho\) una interfaz previamente justificada por IC1–IC10.

La formulación provisional hacía depender directamente la equivalencia de memoization de una familia elegida \(\mathcal K_{i,\rho}\). Eso deja todavía una libertad peligrosa: un analista podría escoger una test suite demasiado pobre y fabricar equivalencias por omisión.

REV-07h elimina ahora esa libertad separando:

\[
\boxed{
\text{semántica completa de continuación del rol}
\quad\neq\quad
\text{base característica usada para demostrarla}.
}
\]

La equivalencia viene de la primera. \(\mathcal K_{i,\rho}\) solo puede servir como base de prueba cuando se demuestra RoleAdequate.

#### 0.11.82a. Semántica completa de continuación del rol

Una teoría independiente del rol \(\mathcal T_\rho\), coordinada con \(\mathbb I_i^\rho\), fija primero una especificación de continuación:

\[
\mathbb C_{i,\rho}
=
\langle
\mathcal A_{i,\rho},
\epsilon_\rho,
\star_\rho,
\operatorname{WF}_{i,\rho},
\operatorname{Cl}_\rho
\rangle,
\]

donde \(\mathcal A_{i,\rho}\) contiene los generadores/acciones/estrategias atómicas autorizadas por el rol, \(\epsilon_\rho\) es la continuación identidad cuando exista, \(\star_\rho\) es composición tipada, WF fija well-formedness y \(\operatorname{Cl}_\rho\) declara las operaciones de cierre temporal que la teoría del rol licencia. Para roles continuos, un generador puede ser ya un perfil completo de carga/control; no se presupone discretización.

La familia completa se define por la **menor clausura autorizada**:

\[
\boxed{
\operatorname{Cont}_{i,\rho}
:=
\operatorname{Cl}_\rho
(
\mathcal A_{i,\rho}\cup\{\epsilon_\rho\}
).
}
\]

Minimalidad significa que no se añaden continuaciones externas al rol; closure significa que tampoco se omiten arbitrariamente composiciones o evoluciones exigidas por sus reglas. Así la arbitrariedad no se desplaza de \(\mathcal K\) a \(\operatorname{Cont}\).

La coordinación con la interfaz exige además que todo generador role-observable tenga interpretación mediante las estrategias/trazas de \(\mathbb I_i^\rho\), y que toda interacción declarada relevante por el rol pueda representarse por alguna continuación de \(\operatorname{Cont}_{i,\rho}\).

No se permite definir \(\mathbb C_{i,\rho}\) ni \(\operatorname{Cont}_{i,\rho}\) a partir de:

- un par concreto \(h,h'\) que se quiera identificar;
- el MemoState que se desea obtener;
- el quotient final;
- un Bake posterior;
- \(\Omega_i\);
- ContextIndividuation o RegimeTotal.

Cada \(c\in\operatorname{Cont}_{i,\rho}\) es un esquema de continuación tipado por la teoría del rol. Su aplicación a una historia puede estar habilitada, rechazada o ser semánticamente inaplicable. Esa diferencia no se borra silenciosamente.

Definimos por ello el resultado role-relative totalizado:

\[
\operatorname{ROut}_{i,\rho}(h,c)
:=
\begin{cases}
\langle
\mathsf{app},
\operatorname{Obs}_{i,\rho}(h\odot c)
\rangle,
&
\operatorname{App}_{i,\rho}(h,c),
\\[2mm]
\langle
\mathsf{inapp},
\operatorname{Reason}_{i,\rho}(h,c)
\rangle,
&
\neg\operatorname{App}_{i,\rho}(h,c).
\end{cases}
\]

Reason solo conserva las distinciones de inaplicabilidad que \(\mathcal T_\rho\) declare role-relevant; no abre una vía para inspeccionar estructura interna arbitraria.

La equivalencia contextual completa del rol es:

\[
\boxed{
h
\equiv^{\mathrm{ctx}}_{i,\rho}
h'
\Longleftrightarrow
\forall c\in\operatorname{Cont}_{i,\rho}\;
\operatorname{ROut}_{i,\rho}(h,c)
\simeq_\rho
\operatorname{ROut}_{i,\rho}(h',c).
}
\]

Y fijamos ahora:

\[
\boxed{
\equiv^{\mathrm{memo}}_{i,\rho}
:=
\equiv^{\mathrm{ctx}}_{i,\rho}.
}
\]

La memo-equivalence deja así de depender constitutivamente de una test suite escogida por el investigador.

Si \(\simeq_\rho\) es una equivalencia sobre resultados role-relative, entonces:

\[
\boxed{
\equiv^{\mathrm{memo}}_{i,\rho}
\text{ es reflexiva, simétrica y transitiva}.
}
\]

Esto se sigue porque es la intersección, sobre todas las continuaciones role-admisibles, de los kernels observacionales inducidos por cada \(c\).

#### 0.11.82b. RoleAdequate: \(\mathcal K\) como base característica, no como selector

Una familia:

\[
\mathcal K_{i,\rho}
\subseteq
\operatorname{Cont}_{i,\rho}
\]

es admisible solo si satisface:

\[
\operatorname{RoleAdequate}^{\mathsf M}_i
(\rho,\mathcal K_{i,\rho};\kappa),
\]

donde \(\kappa\) es el witness que demuestra que \(\mathcal K_{i,\rho}\) caracteriza la semántica completa del rol.

Para evitar confusión con RA de REV-24, denominamos **RKA1–RKA10** a sus obligaciones.

**RKA1 — independent role grounding.** La teoría \(\mathcal T_\rho\), la interfaz \(\mathbb I_i^\rho\), la especificación \(\mathbb C_{i,\rho}\) y su menor clausura \(\operatorname{Cont}_{i,\rho}\) se fijan independientemente de los histories concretos a comparar:

\[
\operatorname{IndependentRoleSpec}^{\mathsf M}
(
\mathcal T_\rho,
\mathbb I_i^\rho,
\mathbb C_{i,\rho}
)
\land
\operatorname{LeastRoleClosure}^{\mathsf M}
(
\mathbb C_{i,\rho},
\operatorname{Cont}_{i,\rho}
).
\]

Este segundo conjunct es necesario: una teoría no descarga RKA1 si simplemente bautiza como “todas las continuaciones” a un subconjunto escogido para eliminar un contraejemplo.

**RKA2 — admissible-test soundness.**

\[
\boxed{
\mathcal K_{i,\rho}
\subseteq
\operatorname{Cont}_{i,\rho}.
}
\]

Una prueba que observa variables internas, provenance o estados que el rol no puede consultar no es una continuación válida aunque discrimine muy bien.

**RKA3 — pair independence.** La construcción de \(\mathcal K_{i,\rho}\) no puede mencionar el par \(h,h'\), su código, el MemoState candidato ni el resultado que se pretende demostrar:

\[
\operatorname{PairIndependent}^{\mathsf M}
(\mathcal K_{i,\rho},\rho).
\]

Se permiten parámetros fijados por la **clase del rol** —por ejemplo un bound \(N\) de estados declarado antes de observar las máquinas—, no parámetros obtenidos inspeccionando el par bajo comparación.

**RKA4 — characteristic completeness.** Esta es la obligación central y cuantifica sobre **todos** los histories admisibles, no solo sobre una muestra:

\[
\boxed{
\forall h,h'\in\mathcal H_i:
\left[
\forall c\in\mathcal K_{i,\rho}\;
\operatorname{ROut}_{i,\rho}(h,c)
\simeq_\rho
\operatorname{ROut}_{i,\rho}(h',c)
\right]
\Longrightarrow
h\equiv^{\mathrm{memo}}_{i,\rho}h'.
}
\]

Equivalentemente, en forma discriminante:

\[
\boxed{
h\not\equiv^{\mathrm{memo}}_{i,\rho}h'
\Longrightarrow
\exists k\in\mathcal K_{i,\rho}:
\operatorname{ROut}_{i,\rho}(h,k)
\not\simeq_\rho
\operatorname{ROut}_{i,\rho}(h',k).
}
\]

Por RKA2, la implicación inversa es inmediata. Por tanto:

\[
\boxed{
h\equiv^{\mathrm{memo}}_{i,\rho}h'
\Longleftrightarrow
\forall k\in\mathcal K_{i,\rho}\;
\operatorname{ROut}_{i,\rho}(h,k)
\simeq_\rho
\operatorname{ROut}_{i,\rho}(h',k).
}
\]

solo **después** de demostrar RoleAdequate.

**RKA5 — horizon discipline.** No se permite sustituir una semántica de continuaciones potencialmente no acotada por un horizonte finito arbitrario:

\[
\operatorname{UnboundedRole}(\rho)
\land
|\mathcal K_{i,\rho}|<\infty
\]

requiere un teorema independiente de finite characterization:

\[
\operatorname{FiniteCharacterization}^{\mathsf M}
(\rho,\mathcal K_{i,\rho}).
\]

Sin él, una suite finita es evidencia empírica o testing, no una descarga ontológica de RoleAdequate.

**RKA6 — applicability sensitivity.** Si dos histories difieren en si una continuación role-admisible puede aplicarse, y esa diferencia es role-relevant, la base debe poder detectarla:

\[
\operatorname{RelevantAppDiff}_{i,\rho}(h,h')
\Longrightarrow
\exists k\in\mathcal K_{i,\rho}:
\operatorname{ROut}(h,k)
\not\simeq_\rho
\operatorname{ROut}(h',k).
\]

Así una equivalencia no puede aparecer por cuantificar solo sobre la intersección de las continuaciones que casualmente funcionan en ambos histories.

**RKA7 — non-vacuity.** Si el rol admite al menos dos histories contextualmente distinguibles:

\[
\exists h,h':
h\not\equiv^{\mathrm{memo}}_{i,\rho}h',
\]

entonces:

\[
\boxed{
\mathcal K_{i,\rho}\neq\varnothing
}
\]

y su mapa observacional no puede ser constante. Una \(\mathcal K=\varnothing\) solo es RoleAdequate cuando la propia semántica completa demuestra que el rol tiene una única clase contextual.

**RKA8 — recoding invariance.** Para una recodificación fiel \(\alpha\) de histories, continuations e interfaz debe existir una base transportada \(\alpha_*\mathcal K\) tal que:

\[
\operatorname{RoleAdequate}
(\rho,\mathcal K)
\Longleftrightarrow
\operatorname{RoleAdequate}
(\alpha\rho,\alpha_*\mathcal K),
\]

y:

\[
h\equiv^{\mathrm{memo}}_{i,\rho}h'
\Longleftrightarrow
\alpha h
\equiv^{\mathrm{memo}}_{i,\alpha\rho}
\alpha h'.
\]

Cambiar nombres de estados, serialización, unidades o identificadores no cambia qué continuaciones son discriminantes.

**RKA9 — residual adequacy.** RoleAdequate debe sobrevivir a estados alcanzables del mismo rol. Si \(p\in\operatorname{Cont}_{i,\rho}\) lleva \(h\) a un residual \(h\odot p\), la teoría debe justificar una base residual \(\mathcal K^{/p}_{i,\rho}\) obtenida por una regla fijada por el rol, no rediseñada para ese history:

\[
\operatorname{ResidualBasis}^{\mathsf M}
(
\mathcal K_{i,\rho},p
\Downarrow
\mathcal K^{/p}_{i,\rho}
)
\]

y:

\[
\operatorname{RoleAdequate}
(
\rho,
\mathcal K^{/p}_{i,\rho}
).
\]

Una base que caracteriza solo el estado inicial pero deja de ser completa después de una transición no basta para memoization reentrante.

**RKA10 — no ontological promotion.**

\[
\operatorname{RoleAdequate}^{\mathsf M}_i
(\rho,\mathcal K)
\]

no implica:

\[
\operatorname{SourceIdentity},
\quad
\operatorname{ContextIndividuation},
\quad
\operatorname{IndexAdmission},
\quad
\operatorname{RegimeTotal},
\quad
\operatorname{CommonGround}.
\]

RoleAdequate caracteriza únicamente el poder discriminante de una familia de continuaciones respecto de un rol ya fijado.

#### 0.11.82c. Teorema de invariancia de base

Sean dos familias diferentes:

\[
\mathcal K_{i,\rho},
\qquad
\mathcal L_{i,\rho},
\]

tales que:

\[
\operatorname{RoleAdequate}(\rho,\mathcal K_{i,\rho})
\land
\operatorname{RoleAdequate}(\rho,\mathcal L_{i,\rho}).
\]

Definamos las equivalencias inducidas operacionalmente por cada base:

\[
h\equiv_{\mathcal K}h'
\Longleftrightarrow
\forall k\in\mathcal K_{i,\rho}\;
\operatorname{ROut}(h,k)
\simeq_\rho
\operatorname{ROut}(h',k),
\]

y análogamente para \(\equiv_{\mathcal L}\). Usamos como abreviatura metateórica:

\[
\ker(\mathcal K)
:=
\{
(h,h')
\mid
h\equiv_{\mathcal K}h'
\}.
\]

Por RKA4:

\[
\equiv_{\mathcal K}
=
\equiv^{\mathrm{memo}}_{i,\rho}
=
\equiv_{\mathcal L}.
\]

Luego:

\[
\boxed{
\operatorname{RoleAdequate}(\rho,\mathcal K)
\land
\operatorname{RoleAdequate}(\rho,\mathcal L)
\Longrightarrow
\ker(\mathcal K)=\ker(\mathcal L).
}
\]

Éste es el principal guard anti-post-hoc. Dos test suites pueden tener tamaños, sintaxis y estrategias diferentes, pero si ambas son adecuadas **no pueden cambiar el quotient de historias**.

Corolario inmediato:

\[
\boxed{
\ker(\mathcal K)\neq\ker(\mathcal L)
\Longrightarrow
\neg\operatorname{RoleAdequate}(\mathcal K)
\lor
\neg\operatorname{RoleAdequate}(\mathcal L).
}
\]

No existe una pluralidad legítima de memo-equivalences dependiente del gusto del analista para un mismo rol completamente fijado.

#### 0.11.82d. Congruencia temporal bajo composición de continuaciones

Supóngase que \(\operatorname{Cont}_{i,\rho}\) contiene una continuación identidad \(\epsilon_\rho\) y es cerrada bajo composición well-typed:

\[
p,c\in\operatorname{Cont}_{i,\rho}
\land
\operatorname{WF}(p\star c)
\Longrightarrow
p\star c\in\operatorname{Cont}_{i,\rho},
\]

con asociatividad observacional:

\[
\operatorname{ROut}_{i,\rho}
(h,p\star c)
\simeq_\rho
\operatorname{ROut}_{i,\rho}
(h\odot p,c)
\]

siempre que ambas expresiones estén well-typed, incluyendo concordancia de aplicabilidad/inaplicabilidad.

Entonces:

\[
\boxed{
h\equiv^{\mathrm{memo}}_{i,\rho}h'
\land
\operatorname{App}(h,p)
\land
\operatorname{App}(h',p)
\Longrightarrow
h\odot p
\equiv^{\mathrm{memo}}_{i,\rho}
h'\odot p.
}
\]

**Demostración.** Sea \(c\) cualquier continuación admisible del residual. Por closure, \(p\star c\) es una continuación del rol desde el history original. Como \(h\equiv^{\mathrm{memo}}h'\), ambos histories coinciden observationally bajo \(p\star c\). Por asociatividad de composición, esto equivale a comparar \(h\odot p\) y \(h'\odot p\) bajo \(c\). Como \(c\) era arbitraria, los residuals son memo-equivalentes. \(\square\)

Este resultado descarga la **right-congruence temporal** de memo-equivalence para roles cuya continuación posea esa estructura composicional. No demuestra todavía toda la composicionalidad entre roles distintos.

#### 0.11.82e. Modelo RA-A — máquinas de Mealy con bound independiente

Considérese la clase:

\[
\mathfrak M_N
\]

de máquinas de Mealy deterministas sobre alfabetos **finitos y fijos** \(A/B\), cada una con como máximo \(N\) estados. El bound \(N\) forma parte de la especificación previa de la clase y no se obtiene inspeccionando el par de máquinas.

La semántica completa del rol es:

\[
\operatorname{Cont}_{\rho_{\mathrm{IO}}}
=
A^*.
\]

Sea:

\[
\mathcal K_N
:=
A^{\le N^2},
\]

el conjunto de palabras de longitud a lo sumo \(N^2\).

Si dos máquinas \(M,M'\in\mathfrak M_N\) no son observationally equivalent, existe una palabra discriminante. Considérese una de longitud mínima. Antes del primer output distinto, la ejecución conjunta visita pares de estados de:

\[
Q_M\times Q_{M'},
\]

que contiene como máximo \(N^2\) pares. Una palabra mínima no puede repetir un mismo par antes de discriminar: eliminar el ciclo produciría una palabra discriminante más corta. Por tanto existe un discriminador de longitud a lo sumo \(N^2\).

Luego:

\[
\boxed{
\operatorname{RoleAdequate}
(
\rho_{\mathrm{IO}},
A^{\le N^2}
).
}
\]

La base es finita sin ser post hoc porque su suficiencia viene de un teorema estructural sobre **toda** la clase \(\mathfrak M_N\).

Si se elimina el bound \(N\), la misma familia finita deja de estar justificada: RKA5 impide extrapolar el resultado a máquinas arbitrariamente grandes.

#### 0.11.82f. Modelo RA-B — servicio KV: una base infinita parametrizada y necesaria

Para el servicio key/value del modelo anterior, supónganse keys tomadas de un dominio \(K\) no finito y semántica determinista de:

\[
\operatorname{Put},
\quad
\operatorname{Get},
\quad
\operatorname{Delete}.
\]

La semántica completa contiene todas las secuencias finitas well-typed de requests.

Considérese la base esquemática:

\[
\mathcal K_{\mathrm{KV}}
=
\{
\operatorname{Get}(k)
\mid
k\in K
\}.
\]

Si dos estados abstractos \(m,m'\) producen el mismo resultado para todo \(\operatorname{Get}(k)\), entonces:

\[
\forall k\in K:
m(k)=m'(k),
\]

incluyendo ausencia/presencia. Por extensionalidad del mapa:

\[
m=m'.
\]

Dado que Put/Delete/Get son deterministas sobre ese estado abstracto, una inducción sobre la longitud de cualquier secuencia futura demuestra que ambos histories producen las mismas respuestas bajo toda continuación completa. Por tanto:

\[
\boxed{
\operatorname{RoleAdequate}
(
\rho_{\mathrm{KV}},
\mathcal K_{\mathrm{KV}}
).
}
\]

El ejemplo muestra que RoleAdequate no exige una base finita.

De hecho, ninguna base finita de Get puede ser adecuada cuando \(K\) es infinito. Si una suite finita menciona solo:

\[
k_1,\ldots,k_n,
\]

escoja:

\[
k_*\notin\{k_1,\ldots,k_n\}.
\]

Existen dos estados que coinciden en todos los \(k_1,\ldots,k_n\) y difieren solo en \(k_*\). La suite finita no los distingue, pero:

\[
\operatorname{Get}(k_*)
\]

sí. Por RKA4:

\[
\boxed{
\neg\operatorname{RoleAdequate}
(
\rho_{\mathrm{KV}},
\mathcal K_{\mathrm{finite}}
).
}
\]

Esto bloquea directamente la tentación de usar un test corpus finito como si demostrase equivalencia universal.

#### 0.11.82g. Modelo RA-C — puerto AC: sampling no equivale a adecuación

En el rol eléctrico:

\[
\rho_{\mathrm{AC}},
\]

la familia completa de continuaciones contiene todas las cargas/perturbaciones admitidas por el envelope contractual:

\[
\operatorname{Cont}_{\rho_{\mathrm{AC}}}
=
\Gamma^{\rho_{\mathrm{AC}}}.
\]

Un conjunto finito de cargas de laboratorio:

\[
\mathcal K_{\mathrm{sample}}
=
\{
\gamma_1,\ldots,\gamma_n
\}
\]

no es RoleAdequate por el mero hecho de que dos fuentes coincidan en él. En una clase funcional suficientemente rica pueden existir dos relaciones de puerto que coincidan exactamente en esos puntos y difieran en otra carga admisible \(\gamma_*\).

Por tanto:

\[
\boxed{
\text{finite sampling}
\not\Rightarrow
\operatorname{RoleAdequate}.
}
\]

Hay dos rutas legítimas:

1. tomar como base la familia completa del envelope cuando el marco fundacional lo permita; o
2. restringir independientemente la clase física a un modelo identificable —por ejemplo una familia paramétrica de puertos— y demostrar un theorem de system identification según el cual una familia de probes fijada de antemano determina todos los parámetros role-relevant.

En el modelo Thévenin/LTI usado antes, no basta decir “medimos varias cargas”. Debe demostrarse que los probes elegidos identifican \(V_{\mathrm{oc}}\), \(Z_{\mathrm{out}}\), protección y cualquier otra dimensión incluida en \(\mathcal Q^{\rho_{\mathrm{AC}}}\) sobre el bandwidth contractual.

RKA5 convierte así la diferencia entre **test engineering** y **equivalencia ontológicamente autorizada** en una obligación formal.

#### 0.11.82h. Stress tests de RoleAdequate

**RK-T1 — empty basis.** \(\mathcal K=\varnothing\) hace equivalentes todas las historias por vacuidad. Si el rol tiene más de una clase contextual, falla RKA7.

**RK-T2 — pair-crafted basis.** Se inspeccionan \(h,h'\) y se eligen solo continuaciones en las que coinciden. Falla RKA3 aunque los tests sean individualmente role-admisibles.

**RK-T3 — short-horizon deception.** Dos histories coinciden durante \(n\) pasos y divergen en \(n+1\). Usar continuaciones de longitud \(\le n\) falla RKA4/RKA5 salvo theorem independiente de finite characterization.

**RK-T4 — internal oracle.** Un test lee directamente un campo privado que nunca puede afectar la interfaz. Puede distinguir histories, pero falla RKA2/IC2: no pertenece al rol.

**RK-T5 — intersection trick.** Se cuantifica solo sobre continuaciones aplicables a ambos histories. Una capacidad presente en uno y ausente en otro desaparece del test. Falla RKA6.

**RK-T6 — initial-only suite.** Una base caracteriza el estado inicial pero, tras una transición admisible, dos residuals que la base no sabe separar aparecen como iguales. Falla RKA9.

**RK-T7 — benchmark overfitting.** Una implementación memoriza las respuestas del corpus \(\mathcal K\) pero diverge fuera de él. Esto demuestra que la suite no era característica: falla RKA4.

**RK-T8 — provenance oracle.** Se añade un test “¿de qué historia vienes?” aunque provenance no pertenezca al rol. Falla RKA2; IC9 preserva provenance objetiva sin convertirla automáticamente en observable de interfaz.

#### 0.11.82i. Estado de RoleAdequate

Queda formalmente fijada la dependencia correcta:

\[
\boxed{
\mathcal T_\rho+\mathbb I^\rho
\Longrightarrow
\operatorname{Cont}_{i,\rho}
\Longrightarrow
\equiv^{\mathrm{memo}}_{i,\rho}.
}
\]

Solo después puede introducirse una base:

\[
\boxed{
\operatorname{RoleAdequate}
(
\rho,\mathcal K
)
\Longrightarrow
\ker(\mathcal K)
=
\ker(
\operatorname{Cont}_{i,\rho}
).
}
\]

Por tanto:

\[
\boxed{
\mathcal K
\text{ demuestra la memo-equivalence;}
\qquad
\mathcal K
\text{ no la crea.}
}
\]

RKA1–RKA10, el teorema de invariancia de base y los modelos Mealy/KV/AC cierran la deuda específica de **formalizar RoleAdequate y la clase admisible de continuaciones sin circularidad ni selección post hoc**.

Además, bajo closure y asociatividad de las continuaciones del rol, la memo-equivalence completa queda demostrada como equivalencia y right-congruence temporal. Permanece abierta la composicionalidad más fuerte entre roles/interfaces distintos y su coordinación con MemoState/update/invalidation.


#### 0.11.82j. Composición cross-role: por qué la intersección de kernels no basta

Sea una familia finita o set-indexed de roles ya justificados:

\[
\mathbf R
=
\{\rho_a\}_{a\in A},
\]

cada uno con su interfaz \(\mathbb I^{\rho_a}\), su semántica completa de continuación \(\operatorname{Cont}_{i,\rho_a}\) y su memo-equivalence:

\[
E_a
:=
\equiv^{\mathrm{memo}}_{i,\rho_a}.
\]

El candidato ingenuo para la equivalencia conjunta sería:

\[
E_{\wedge}
:=
\bigcap_{a\in A}E_a.
\]

Pero en general:

\[
\boxed{
E_{\wedge}
\not\subseteq
E_{\otimes},
}
\]

donde \(E_{\otimes}\) es la memo-equivalence del rol compuesto \(\rho_{\otimes}\).

La razón es estructural: una continuación compuesta puede intercalar acciones de roles distintos y hacer visible una dependencia que ninguna semántica aislada puede excitar.

Definimos la **relevancia sinérgica cross-role**:

\[
\boxed{
\operatorname{SynRel}_{\mathbf R}(h,h')
:\Longleftrightarrow
h\,E_{\wedge}\,h'
\land
h\not E_{\otimes}h'.
}
\]

SynRel no es todavía la relación de emergencia del programa emergentista. Afirma únicamente que una diferencia irrelevante bajo cada rol considerado aisladamente se vuelve discriminable bajo la semántica de su composición.

Si existe un witness mínimo \(c_{\otimes}\in\operatorname{Cont}_{i,\rho_\otimes}\) que distingue \(h,h'\), llamamos:

\[
\operatorname{CrossRoleWitness}
(
h,h';c_\otimes
).
\]

Un witness genuinamente cross-role debe usar al menos dos tags/puertos de rol o un interaction primitive declarado; si pertenece enteramente a un único \(\rho_a\), contradice \(hE_ah'\).

#### 0.11.82k. Contraejemplo CR-X: write/read acoplados

Sean dos histories \(H_L,H_U\) con estado inicial visible \(x=0\).

Hay dos roles:

\[
\rho_A
=
\text{writer},
\qquad
\rho_B
=
\text{reader}.
\]

El rol \(A\) admite únicamente:

\[
\operatorname{SetA}(1)
\mapsto
\operatorname{Ack}.
\]

El rol \(B\), considerado aisladamente, admite únicamente secuencias de:

\[
\operatorname{ReadB}()
\]

y no modifica estado.

En \(H_L\) los puertos están **linked**:

\[
\operatorname{SetA}(1)
\text{ actualiza el estado que lee B}.
\]

En \(H_U\) están **unlinked**:

\[
\operatorname{SetA}(1)
\text{ actualiza un estado privado de A y no el estado leído por B}.
\]

Aislando cada rol:

\[
H_L
\equiv^{\mathrm{memo}}_{\rho_A}
H_U,
\]

porque toda continuación de \(A\) produce los mismos Ack, y:

\[
H_L
\equiv^{\mathrm{memo}}_{\rho_B}
H_U,
\]

porque sin acciones de \(A\), \(B\) lee siempre el mismo estado inicial \(0\).

Sin embargo el rol compuesto admite:

\[
c_\otimes
=
\operatorname{SetA}(1)
\star
\operatorname{ReadB}().
\]

Entonces:

\[
\operatorname{ROut}_{\otimes}(H_L,c_\otimes)
=
\langle Ack,1\rangle,
\]

mientras:

\[
\operatorname{ROut}_{\otimes}(H_U,c_\otimes)
=
\langle Ack,0\rangle.
\]

Por tanto:

\[
\boxed{
H_L
E_{\wedge}
H_U
\quad\land\quad
H_L
\not E_{\otimes}
H_U.
}
\]

El fallo exacto es que \(E_B\) no es estable bajo una acción de \(A\). Tras SetA(1):

\[
H_L\odot \operatorname{SetA}(1)
\not E_B
H_U\odot \operatorname{SetA}(1).
\]

Así la right-congruence demostrada dentro de cada rol no implica congruencia bajo acciones de otros roles.

#### 0.11.82l. Especificación del rol compuesto

El rol compuesto no se obtiene escribiendo simplemente \(\rho_1\times\rho_2\). Debe existir una especificación independiente:

\[
\mathbb C_{i,\mathbf R}^{\otimes}
=
\left\langle
\mathcal A_{\otimes},
\epsilon_{\otimes},
\star_{\otimes},
\operatorname{WF}_{\otimes},
\operatorname{Cl}_{\otimes}
\right\rangle
\]

que determine:

\[
\operatorname{Cont}_{i,\rho_{\otimes}}
=
\operatorname{Cl}_{\otimes}
(
\mathcal A_\otimes\cup\{\epsilon_\otimes\}
).
\]

Distinguimos dos casos.

**Composición separable.** No aparecen primitives interaction-only:

\[
\boxed{
\mathcal A_\otimes
=
\bigsqcup_{a\in A}
\jmath_a(\mathcal A_{i,\rho_a}),
}
\]

donde \(\jmath_a\) etiqueta fielmente cada generador componente. Toda conducta conjunta se construye por interleaving/composición de acciones ya pertenecientes a algún rol.

**Composición no separable.** Existe al menos un generador:

\[
g_\times
\in
\mathcal A_\otimes
\setminus
\bigsqcup_a
\jmath_a(\mathcal A_{i,\rho_a}).
\]

Ese generador no puede heredarse gratuitamente. Debe recibir semántica independiente —por ejemplo mediante un interaction role \(\rho_\times\), una extensión explícita del contrato o una teoría de sincronización— antes de entrar en una equivalencia compuesta.

La mera coexistencia de interfaces no licencia primitives conjuntos nuevos.

#### 0.11.82m. RoleCompositionAdequate: obligaciones CR1–CR8

Introducimos:

\[
\operatorname{RoleCompositionAdequate}^{\mathsf M}_i
(
\mathbf R,
\rho_\otimes;
\chi
),
\]

leído: \(\chi\) demuestra que la composición de los roles de \(\mathbf R\) es semánticamente adecuada para derivar la equivalencia conjunta.

**CR1 — independent composite specification.** \(\mathbb C^\otimes\) y la semántica observacional conjunta se fijan sin inspeccionar el par \(h,h'\) ni el quotient que se desea obtener.

**CR2 — conservative embedding.** Cada continuación componente se embebe preservando aplicabilidad y observación:

\[
\operatorname{ROut}_{\rho_a}(h,c)
\simeq_{\rho_a}
\operatorname{ROut}_{\otimes}
(h,\jmath_a(c))
\big|_{\rho_a}.
\]

Por tanto:

\[
\boxed{
E_\otimes
\subseteq
E_\wedge.
}
\]

La composición puede distinguir más, nunca borrar legítimamente una diferencia que ya era visible en un rol componente.

**CR3 — generator coverage.** Para derivar composición desde los roles existentes, todo generador conjunto debe provenir de algún componente:

\[
\mathcal A_\otimes
=
\bigsqcup_a\jmath_a(\mathcal A_{i,\rho_a}).
\]

Si hay un \(g_\times\) nuevo, CR3 falla hasta justificarlo como interaction primitive con contrato propio.

**CR4 — joint step congruence.** La intersección:

\[
E_\wedge
=
\bigcap_a E_a
\]

debe ser una congruencia para **cada** generador de la composición. Para todo \(g\in\mathcal A_\otimes\):

\[
hE_\wedge h'
\Longrightarrow
\operatorname{Step}_\otimes(h,g)
\;\widehat E_\wedge\;
\operatorname{Step}_\otimes(h',g),
\]

donde \(\widehat E_\wedge\) exige simultáneamente:

1. mismo status role-relevant de aplicabilidad/inaplicabilidad;
2. outputs step-local equivalentes;
3. si ambos steps producen residuals \(r,r'\), entonces \(rE_\wedge r'\).

CR4 es el guard que falla en CR-X.

**CR5 — no joint hidden observer.** El resultado de una continuación compuesta debe factorizar por la secuencia de resultados step-local y estado contractual explícito:

\[
\operatorname{ROut}_\otimes
(h,g_1\star\cdots\star g_n)
=
\widehat O_\otimes
\left(
o_1,\ldots,o_n
\right),
\]

con cada \(o_m\) generado por el step correspondiente. No puede existir un observador conjunto que lea estructura interna que ninguno de los contratos componentes ni un interaction contract declarado exponen.

**CR6 — closure compatibility.** \(\operatorname{Cl}_\otimes\) no puede introducir por cierre una interacción semánticamente nueva que no esté cubierta por CR3–CR5. Límites, sincronización, concurrencia, fairness o topologías continuas requieren preservación demostrada, no una extrapolación desde secuencias finitas.

**CR7 — recoding/composition invariance.** Recodificar fielmente componentes y luego componer debe inducir el mismo kernel que componer y después transportar la codificación.

**CR8 — no ontological promotion.**

\[
\operatorname{RoleCompositionAdequate}
\not\Rightarrow
\operatorname{ContextIndividuation},
\operatorname{CommonGround},
\operatorname{RegimeTotal}
\]

ni identidad de las SourceUnits participantes.

#### 0.11.82n. Teorema de composición segura

**CR-T1 — kernel intersection theorem.** Si CR1–CR6 están descargadas para una composición separable y las continuaciones compuestas se generan por composición finita well-typed, entonces:

\[
\boxed{
E_\otimes
=
E_\wedge
=
\bigcap_{a\in A}
\equiv^{\mathrm{memo}}_{i,\rho_a}.
}
\]

**Demostración.**

Por CR2:

\[
E_\otimes\subseteq E_\wedge.
\]

Para la conversa, sea:

\[
hE_\wedge h'.
\]

Tomemos cualquier continuación compuesta:

\[
c_\otimes
=
g_1\star\cdots\star g_n.
\]

Por inducción en \(n\):

- caso \(n=0\): la continuación identidad preserva \(E_\wedge\);
- paso inductivo: por CR4, aplicar \(g_{m+1}\) a residuals \(E_\wedge\)-equivalentes produce outputs equivalentes y residuals que siguen en \(E_\wedge\).

Por CR5, la observación conjunta está completamente determinada por esos outputs step-local; por tanto las dos ejecuciones producen resultados \(\rho_\otimes\)-equivalentes. Como \(c_\otimes\) era arbitraria:

\[
hE_\otimes h'.
\]

Luego:

\[
E_\wedge\subseteq E_\otimes.
\]

Combinando inclusiones:

\[
E_\otimes=E_\wedge.
\qquad\square
\]

Para closures infinitarias, concurrentes o continuas, el argumento anterior no se extiende automáticamente: CR6 exige el principio de preservación correspondiente.

#### 0.11.82o. Modelo positivo CR-P: dos namespaces KV independientes

Sea un estado:

\[
m
=
(m_A,m_B)
\]

con dos namespaces disjuntos. El rol \(\rho_A\) opera solo sobre \(m_A\) y \(\rho_B\) solo sobre \(m_B\).

Las operaciones son:

\[
Put_A,Get_A,Delete_A
\]

y:

\[
Put_B,Get_B,Delete_B.
\]

No hay operaciones cross-namespace ni shared hidden state.

La equivalencia de cada rol coincide con igualdad extensional de su coordenada:

\[
mE_A m'
\Longleftrightarrow
m_A=m'_A,
\]

\[
mE_B m'
\Longleftrightarrow
m_B=m'_B.
\]

Luego:

\[
mE_\wedge m'
\Longleftrightarrow
(m_A,m_B)=(m'_A,m'_B).
\]

Cualquier acción \(A\) modifica solo la primera coordenada y cualquier acción \(B\) solo la segunda, de modo que \(E_\wedge\) es step-congruence bajo todos los generadores. Las observaciones conjuntas son únicamente la secuencia de respuestas API.

Se descargan CR1–CR6 y:

\[
\boxed{
E_\otimes
=
E_A\cap E_B.
}
\]

La independencia ontológica de los namespaces no es necesaria como tesis general; aquí funciona como witness suficiente de no-interferencia operacional.

#### 0.11.82p. Interaction roles: cómo representar sinergia real sin esconderla

Cuando CR3 o CR4 fallan porque existe una interacción real entre roles, la respuesta correcta no es forzar:

\[
E_\otimes=E_\wedge.
\]

Se introduce explícitamente una capa de interacción:

\[
\rho_\times,
\]

con su propia teoría, interfaz/trace semantics cuando proceda y continuación:

\[
\operatorname{Cont}_{i,\rho_\times}.
\]

Entonces la familia relevante pasa a ser:

\[
\mathbf R^+
=
\mathbf R\cup\{\rho_\times\}.
\]

La diferencia cross-role deja de ser una sorpresa escondida y se convierte en una dimensión contractual explícita.

En CR-X, \(\rho_\times\) contiene al menos la dependencia:

\[
SetA
\leadsto
ReadB.
\]

Una vez esa interacción entra en la especificación, \(H_L\) y \(H_U\) ya no son equivalentes respecto de la familia enriquecida.

Esto proporciona una regla arquitectónica:

\[
\boxed{
\text{si la interacción crea poder discriminante nuevo,}
\;
\text{la interacción debe entrar en el contrato.}
}
\]

No debe ocultarse dentro de una supuesta composición automática.

#### 0.11.82q. Consecuencia para Baking: Bakes sound por separado pueden componer mal

Sea para cada rol:

\[
B_a
=
\operatorname{Bake}_{\rho_a}
\]

un Bake individualmente sound:

\[
\ker(B_a)
\subseteq
E_a.
\]

Considérese el Bake producto:

\[
B_\Pi(h)
=
\langle
B_a(h)
\rangle_{a\in A}.
\]

Entonces:

\[
\ker(B_\Pi)
=
\bigcap_{a\in A}
\ker(B_a).
\]

De la soundness individual solo se deriva:

\[
\ker(B_\Pi)
\subseteq
E_\wedge.
\]

Pero el contrato compuesto exige:

\[
\boxed{
\ker(B_\Pi)
\subseteq
E_\otimes.
}
\]

Si existe relevancia sinérgica:

\[
E_\otimes
\subsetneq
E_\wedge,
\]

la primera inclusión no basta.

En particular, si cada Bake es quotient exacto de su rol:

\[
\ker(B_a)=E_a,
\]

entonces:

\[
\ker(B_\Pi)=E_\wedge.
\]

Por tanto, ante cualquier witness:

\[
hE_\wedge h'
\land
h\not E_\otimes h',
\]

obtenemos:

\[
B_\Pi(h)=B_\Pi(h')
\]

aunque la composición debe distinguirlos. Luego:

\[
\boxed{
\operatorname{ExactBake}_{\rho_1}
+
\cdots+
\operatorname{ExactBake}_{\rho_n}
\not\Rightarrow
\operatorname{SoundBake}_{\rho_\otimes}.
}
\]

Esto es una deuda genuina de composición, no un bug accidental de implementación.

El criterio correcto para baking multi-role vuelve a ser:

\[
q_{\otimes}
=
d_{\otimes}
\circ
B_\Pi
\]

o, equivalentemente en kernel form:

\[
\ker(B_\Pi)
\subseteq
E_\otimes.
\]

Bajo CR-T1, \(E_\otimes=E_\wedge\), por lo que exact Bakes componentes sí pueden componerse de forma sound. Si CR-T1 falla, hace falta conservar información adicional sobre la interacción.

#### 0.11.82r. Stress tests de composición cross-role

**CR-S1 — marginal equivalence fallacy.** Igualdad bajo cada rol aislado se promueve a igualdad conjunta. CR-X refuta la regla; falla CR4.

**CR-S2 — undeclared synchronization.** Se añade un primitive simultáneo que no pertenece a ningún rol componente. Falla CR3.

**CR-S3 — hidden joint observer.** El compositor inspecciona un identificador interno compartido aunque ningún contrato lo expone. Falla CR5.

**CR-S4 — applicability coupling.** Una acción de \(A\) habilita/deshabilita una operación de \(B\), pero la composición ignora ese cambio. Falla CR4 por enabledness no congruente.

**CR-S5 — finite-interleaving extrapolation.** Todos los interleavings finitos coinciden, pero una condición de límite/fairness distingue ejecuciones infinitas. Falla CR6 si no existe theorem de preservación.

**CR-S6 — product-Bake collision.** Dos exact Bakes individuales colapsan un par que un cross-role witness distingue. Falla composite Bake soundness aunque cada componente satisfaga su contrato.

**CR-S7 — context promotion.** Una interacción robusta entre roles se usa para inferir un nuevo contexto. Falla CR8; la interacción puede seguir siendo una relación interna a un contexto ya individuado.

#### 0.11.82s. Estado de la composicionalidad cross-role

La deuda queda separada en dos resultados.

Primero, el caso general:

\[
\boxed{
\bigcap_a
\equiv^{\mathrm{memo}}_{\rho_a}
\not\Rightarrow
\equiv^{\mathrm{memo}}_{\rho_\otimes}.
}
\]

La diferencia exacta se captura por \(\operatorname{SynRel}_{\mathbf R}\).

Segundo, bajo RoleCompositionAdequate/CR1–CR8 y composición separable:

\[
\boxed{
\equiv^{\mathrm{memo}}_{\rho_\otimes}
=
\bigcap_a
\equiv^{\mathrm{memo}}_{\rho_a}.
}
\]

Así la composicionalidad cross-role queda **RESOLVED condicionalmente**: ya no existe una regla universal de producto, pero sí un criterio suficiente explícito y falsable para derivarla. Las interacciones no separables deben declararse como interaction roles/contracts y no esconderse en el compositor.

La consecuencia para REV-07h es importante: MemoState multi-role no puede limitarse a almacenar por separado un memo-state para cada rol. Debe preservar además toda información necesaria para los interaction roles que hagan fallar CR-T1. Ésta pasa a ser la entrada correcta para la siguiente deuda: **estatus ontológico/semántico de MemoState y semántica de update/invalidation**, especialmente cuando cambia el conjunto de roles o aparece una nueva interacción.


#### 0.11.83. Memo-state: estado suficiente y reentrante

La quotient class:

\[
[h_i]_{\equiv^{\mathrm{memo}}_{i,\rho}}
\]

es todavía una construcción metateórica. No se sigue de ella que exista dentro de \(i\) un objeto ontológico que sea literalmente esa clase.

La versión fuerte de memoization exige una realización source-side:

\[
\operatorname{MemoState}^{\mathsf M}_i
(h_i\Downarrow m_i;\rho,\mu),
\]

donde \(m_i\) es una estructura/estado actual de \(i\) y \(\mu\) es el witness que explica cómo \(m_i\) realiza la información suficiente del historial para el rol.

Las obligaciones mínimas son:

1. **M1 / actuality:** \(m_i\) es actual en \(i\); una canonicalización semántica externa no crea un memo-state ontológico.
2. **M2 / role independence:** \(\rho\) y su familia de continuaciones se justifican independientemente del deseo de identificar precisamente \(h_i\) con otra historia.
3. **M3 / interface sufficiency:** respecto de \(\rho\), \(m_i\) conserva al menos la información histórica necesaria para seguir determinando una realización correcta de \(I_i^\rho\) sin reabrir toda la historia interna de \(h_i\). Puede conservar información extra; minimalidad es una propiedad adicional, no requisito de soundness.
4. **M4 / reentrancy:** \(m_i\) puede actuar como estado de entrada para continuaciones futuras del rol; no es solo un resumen retrospectivo.
5. **M5 / equivalence soundness:** historias asignadas al mismo memo-state satisfacen la equivalencia por continuaciones declarada.
6. **M6 / discrimination completeness:** si una diferencia altera alguna continuación relevante de \(\rho\), la teoría no puede conservar silenciosamente el mismo memo-state sin una actualización explícita.
7. **M7 / recoding invariance:** la memoization no depende de identificadores, ordenaciones o codificaciones accidentales.
8. **M8 / provenance retention:** colapsar diferencias para \(\rho\) no implica que las historias objetivamente distintas dejen de haber ocurrido.
9. **M9 / anti-aggregation:** concatenar descripciones de dos fuentes independientes no genera por sí solo un memo-state unitario.
10. **M10 / no context inference:** MemoState no implica ContextIndividuation ni totalización.

Cuando M1–M10 están descargadas, usamos:

\[
\boxed{
\operatorname{MemoIndividuated}^{\mathsf M}_i
(h_i;m_i,\rho,\mu)
}
\]

y obtenemos una vía suficiente hacia SourceUnit:

\[
\boxed{
\operatorname{MemoIndividuated}^{\mathsf M}_i
(h_i;m_i,\rho,\mu)
\Rightarrow
\operatorname{SourceUnit}^{\mathsf M}_i(m_i;\rho,\mu).
}
\]

La unitización recae en el estado suficiente reentrante, no en una caja dibujada alrededor de una colección arbitraria de hechos. Pero el memo-state ya no fija por sí mismo qué debe importar downstream: esa carga pertenece a la interfaz.

La dependencia correcta es:

\[
\boxed{
\text{history}
\xrightarrow{\operatorname{Memo}}
\text{state sufficient to maintain }I^\rho
\xrightarrow{}
I^\rho.
}
\]

Así memoization conserva una interfaz a través del cambio; no inventa la interfaz que pretende conservar.

#### 0.11.83a. SemanticMemo frente a OnticMemo

La existencia del quotient:

\[
q^\rho_{\mathrm{memo}}:
\mathcal H_i
\to
\mathcal H_i/
{\equiv^{\mathrm{memo}}_{i,\rho}}
\]

no implica que exista dentro de \(i\) un token que sea literalmente esa clase.

Sea una representación de estado:

\[
\mu:
\mathcal H_i
\rightharpoonup
M.
\]

Definimos su kernel metateórico:

\[
\ker(\mu)
:=
\{
(h,h')
\mid
\mu(h)=\mu(h')
\}.
\]

Para un contract state \(\Theta\) —que fija rol, InterfaceContract, continuation semantics y, cuando proceda, interaction roles— sea:

\[
E_\Theta
\]

la memo-equivalence inducida por esa especificación completa.

La condición mínima de suficiencia es:

\[
\boxed{
\operatorname{MemoSound}(\mu;\Theta)
:\Longleftrightarrow
\ker(\mu)
\subseteq
E_\Theta.
}
\]

Es decir: el memo puede distinguir **más** de lo necesario, pero no menos.

Definimos además:

\[
\operatorname{MemoExact}(\mu;\Theta)
:\Longleftrightarrow
\ker(\mu)=E_\Theta,
\]

y:

\[
\operatorname{MemoOvercomplete}(\mu;\Theta)
:\Longleftrightarrow
\ker(\mu)\subsetneq E_\Theta.
\]

Por tanto la minimalidad no forma parte de M3. Un UUID perfectamente estable puede conservar provenance adicional y seguir siendo un memo sound, siempre que no fabrique por sí mismo la unitización ni el contrato.

Una **SemanticMemo** es cualquier representación \(\mu^{sem}\) que satisface MemoSound en el metalenguaje. Puede ser una clase cociente, una canonicalización matemática o una estructura calculada externamente:

\[
\operatorname{SemanticMemo}^{\mathsf M}
(
\mu^{sem};\Theta
).
\]

Esto no autoriza:

\[
\exists m_i\;
\operatorname{Real}_i(m_i).
\]

Para una implementación ontológica fuerte introducimos:

\[
\operatorname{OnticMemoImpl}^{\mathsf M}_i
(
\mu_i;M_i,\Theta,\omega
),
\]

con las obligaciones OMI1–OMI7.

**OMI1 — actuality.** Todo valor realizado:

\[
\mu_i(h)=m_i
\]

es un estado/estructura actual de \(i\):

\[
\operatorname{Real}_i(m_i).
\]

**OMI2 — terminal grounding.** \(m_i\) está grounded en el estado actual al término de \(h\); no se obtiene consultando un futuro todavía no realizado.

**OMI3 — source accessibility.** La capacidad futura de mantener la interfaz puede depender realmente de \(m_i\) mediante estructura causal, constitutiva, disposicional u operacional del source. Una etiqueta externa sin papel en la continuación no basta.

**OMI4 — memo soundness.**

\[
\ker(\mu_i)\subseteq E_\Theta.
\]

**OMI5 — prefix locality.** Si dos descripciones codifican fielmente el mismo prefijo actual, el estado ontic memo no cambia por información exclusivamente posterior.

**OMI6 — reentrancy debt.** La implementación debe admitir update/factorization para las continuaciones que pretenda soportar; esta deuda se formaliza en §0.11.83b.

**OMI7 — no ontological promotion.** OnticMemoImpl no implica ContextIndividuation, RegimeTotal ni que el memo-state sea una sustancia separada.

Así:

\[
\boxed{
\operatorname{OnticMemoImpl}
\Rightarrow
\operatorname{SemanticMemo}
}
\]

respecto del perfil que implementa, pero no a la inversa.

#### 0.11.83b. Update como factorización del futuro por el memo-state

Para una continuación atómica o step \(g\), una actualización puramente state-based exige una función:

\[
U_g:
M
\to
M
\]

tal que:

\[
\boxed{
\mu(h\odot g)
=
U_g(\mu(h))
}
\]

para todo history donde \(g\) sea aplicable y la transición esté dentro del rol.

Esta ecuación no puede asumirse. Existe un \(U_g\) bien definido sobre \(\operatorname{Im}(\mu)\) **si y solo si**:

\[
\boxed{
\mu(h)=\mu(h')
\Longrightarrow
\mu(h\odot g)
=
\mu(h'\odot g).
}
\]

Es decir:

\[
\boxed{
\ker(\mu)
\text{ debe ser right-congruence bajo }g.
}
\]

**MU-T1 — update factorization theorem.** Para semántica determinista de estado, la condición anterior es necesaria y suficiente para que exista \(U_g\) con:

\[
\mu\circ(-\odot g)
=
U_g\circ\mu.
\]

**Demostración.** Si \(U_g\) existe, histories con el mismo \(\mu\) reciben el mismo argumento y por tanto el mismo estado actualizado. Para la conversa, defínase:

\[
U_g(m)
:=
\mu(h\odot g)
\]

para cualquier \(h\) con \(\mu(h)=m\). La right-congruence de \(\ker(\mu)\) garantiza independencia del representante. \(\square\)

Para sistemas nondeterministic/probabilistic se reemplaza \(U_g\) por el kernel/relación de transición correspondiente y se exige la misma independencia respecto del representante.

**Corolario.** Si:

\[
\operatorname{MemoExact}(\mu;\Theta)
\]

y \(E_\Theta\) es right-congruence bajo \(g\), entonces el update state-based está bien definido.

Para un MemoOvercomplete el resultado no es automático: preservar más información puede exigir conservar también cómo evoluciona esa información extra.

#### 0.11.83c. Reentrancy fuerte y realización de interfaz

Un update correcto no solo debe producir otro código. Para una implementación ontic fuerte debe mantener el diagrama:

\[
\boxed{
\begin{array}{ccc}
h & \xrightarrow{\;g\;} & h\odot g\\
\downarrow\mu_i && \downarrow\mu_i\\
m_i & \xrightarrow{\;U_g\;} & m'_i
\end{array}
}
\]

y el nuevo \(m'_i\) debe seguir siendo MemoSound respecto del contract state vigente.

La interfaz futura debe factorizar por el estado actualizado:

\[
\operatorname{Prof}_{\mathbb I^\rho}
(h\odot g)
=
F_\rho(m'_i)
\]

para la parte de conducta que la implementación declara determinada por el memo.

Esto separa tres nociones que antes estaban mezcladas:

\[
\boxed{
\text{summary}
\neq
\text{sufficient memo}
\neq
\text{reentrant ontic state}.
}
\]

Un resumen retrospectivo puede ser SemanticMemo. Solo un estado actual, grounded y actualizable que mantiene la suficiencia puede descargar OnticMemoImpl.

#### 0.11.84. Invalidation: pérdida exacta de soundness

Sea:

\[
\Theta
\]

un contract state completo y:

\[
E_\Theta
\]

su memo-equivalence.

Un memo \(\mu\) es válido exactamente cuando:

\[
\operatorname{ValidMemo}(\mu;\Theta)
:\Longleftrightarrow
\ker(\mu)\subseteq E_\Theta.
\]

Definimos invalidación contractual por:

\[
\boxed{
\operatorname{Invalidate}^{\mathsf M}
(
\mu;
\Theta\rightsquigarrow\Theta'
)
}
\]

si y solo si:

\[
\operatorname{ValidMemo}(\mu;\Theta)
\land
\neg
\operatorname{ValidMemo}(\mu;\Theta').
\]

Equivalentemente:

\[
\boxed{
\exists h,h':
\mu(h)=\mu(h')
\land
h\not E_{\Theta'}h'.
}
\]

Así invalidation deja de significar simplemente “el estado cambió”. Significa que el estado anterior **colapsa ahora una diferencia que el contrato vigente necesita preservar**.

#### 0.11.84a. Refinement y coarsening del contrato

Definimos que \(\Theta'\) es un refinement discriminante de \(\Theta\) cuando:

\[
E_{\Theta'}
\subseteq
E_\Theta.
\]

El nuevo contrato distingue al menos todo lo anterior y quizá más.

Un refinement puede invalidar un memo existente:

\[
\ker(\mu)\subseteq E_\Theta
\not\Rightarrow
\ker(\mu)\subseteq E_{\Theta'}.
\]

En cambio, si \(\Theta'\) es un coarsening:

\[
E_\Theta
\subseteq
E_{\Theta'},
\]

entonces:

\[
\boxed{
\operatorname{ValidMemo}(\mu;\Theta)
\Longrightarrow
\operatorname{ValidMemo}(\mu;\Theta').
}
\]

**MI-T1 — coarsening monotonicity.** Quitar poder discriminante al contrato no puede volver insuficiente un memo que ya preservaba una partición más fina.

Añadir un interaction role suele actuar precisamente como refinement:

\[
E_\otimes
\subseteq
E_\wedge.
\]

Por eso la composición cross-role puede invalidar memo-states previamente correctos para todos los roles aislados.

#### 0.11.84b. No-recovery theorem: lo olvidado no reaparece por update local

Supóngase:

\[
\operatorname{Invalidate}
(
\mu;
\Theta\rightsquigarrow\Theta'
).
\]

Entonces existen \(h,h'\) tales que:

\[
\mu(h)=\mu(h')
\]

pero:

\[
h\not E_{\Theta'}h'.
\]

Considérese cualquier transformación que solo vea el memo antiguo:

\[
F:M\to M'.
\]

Defina:

\[
\mu'
=
F\circ\mu.
\]

Como:

\[
\mu(h)=\mu(h'),
\]

se sigue:

\[
\mu'(h)=\mu'(h').
\]

Luego:

\[
\ker(\mu')
\not\subseteq
E_{\Theta'}.
\]

Por tanto:

\[
\boxed{
\operatorname{Invalidate}
(
\mu;
\Theta\rightsquigarrow\Theta'
)
\Longrightarrow
\forall F\;
\neg
\operatorname{MemoSound}
(
F\circ\mu;
\Theta'
).
}
\]

Éste es **MI-T2 — no recovery from forgotten state**.

Una invalidación producida por información ya quotientada no puede repararse aplicando una función al memo viejo. Hace falta una fuente adicional:

\[
z
\]

proveniente del source actual, history persistido, provenance certificate, external witness u otra estructura independently justified:

\[
\mu'
=
F(\mu,z).
\]

El side information \(z\) debe distinguir al menos los pares que el nuevo contrato separa y el memo viejo colapsaba.

Esto da una semántica fuerte a rehydration: no es recalcular el mismo cache; es **readquirir información perdida**.

#### 0.11.84c. Invalidation por transición del source

Aunque el contrato \(\Theta\) no cambie, una arquitectura de memo puede fallar reentrancy si no existe update factorization.

Definimos:

\[
\operatorname{TransitionInvalid}_{g}(\mu)
\]

cuando existen histories:

\[
\mu(h)=\mu(h')
\]

pero:

\[
\mu(h\odot g)
\neq
\mu(h'\odot g).
\]

Entonces ningún update \(U_g\) que dependa solo del estado memo previo puede ser well-defined.

Esto no significa necesariamente que el rol haya cambiado; significa que el supuesto memo-state no era suficiente como **estado reentrante** para esa dinámica.

Si el contrato exige soportar \(g\), OMI6/M4 fallan hasta ampliar el estado o aportar side information.

#### 0.11.84d. Ejemplo MI-A — snapshot KV y nueva operación History

Sea el rol inicial KV:

\[
\Theta_{\mathrm{KV}}
=
\{Put,Get,Delete\}.
\]

Un snapshot del mapa actual:

\[
\mu_{\mathrm{snap}}(h)
=
m_h
\]

es MemoExact para ese rol operacional bajo las hipótesis del modelo anterior.

Extiéndase el contrato:

\[
\Theta_{\mathrm{KV+H}}
=
\{Put,Get,Delete,History\}.
\]

Dos histories pueden producir el mismo mapa actual:

\[
\mu_{\mathrm{snap}}(h)
=
\mu_{\mathrm{snap}}(h')
\]

pero logs distintos:

\[
History_h(k)
\neq
History_{h'}(k).
\]

Luego:

\[
h\not E_{\Theta_{\mathrm{KV+H}}}h',
\]

y:

\[
\boxed{
\operatorname{Invalidate}
(
\mu_{\mathrm{snap}};
\Theta_{\mathrm{KV}}
\rightsquigarrow
\Theta_{\mathrm{KV+H}}
).
}
\]

Por MI-T2, ninguna función solo del snapshot puede reconstruir un memo sound para History. Hace falta el log, un certificado externo equivalente o información adicional que nunca fue quotientada.

#### 0.11.84e. Ejemplo MI-B — interacción cross-role invalida el producto de memos

Sean memos exactos por rol:

\[
\ker(\mu_A)=E_A,
\qquad
\ker(\mu_B)=E_B.
\]

El memo producto:

\[
\mu_\Pi
=
\langle
\mu_A,\mu_B
\rangle
\]

satisface:

\[
\ker(\mu_\Pi)
=
E_A\cap E_B
=
E_\wedge.
\]

Si existe SynRel:

\[
E_\otimes
\subsetneq
E_\wedge,
\]

entonces:

\[
\boxed{
\neg
\operatorname{MemoSound}
(
\mu_\Pi;
\Theta_\otimes
).
}
\]

El mismo par \(H_L,H_U\) de CR-X constituye un witness.

Y por MI-T2 tampoco puede arreglarse la composición únicamente mediante una función de \((\mu_A,\mu_B)\).

Hay que conservar o readquirir la relación de interacción —por ejemplo el wiring/linkage que conecta writer y reader—.

Esto unifica la deuda de cross-role composition con invalidation: **la nueva interacción refina el quotient y puede convertir en insuficiente un conjunto de memos individualmente perfectos**.

#### 0.11.84f. Invalidation no es ContextCessation

No se adopta:

\[
\operatorname{Invalidate}
\Longleftrightarrow
\operatorname{ContextCessation}.
\]

Puede cambiar un contrato, aparecer un interaction role, perderse un cache o requerirse rehydration mientras el mismo contexto persiste.

La invalidación es relativa a:

\[
\Theta,
\]

no una sentencia absoluta sobre existencia.

Su uso para Ship of Theseus queda ahora más preciso: reemplazar todos los componentes puede ser compatible con persistencia de una SourceUnit si los MemoStates relevantes permanecen sound y reentrantes; conservar todos los componentes puede ser insuficiente si el contract state se refina o una interacción nueva revela diferencias previamente quotientadas.

#### 0.11.84g. Estado de MemoState/update/invalidation

La arquitectura distingue finalmente:

\[
\boxed{
\begin{array}{rcl}
\operatorname{SemanticMemo}
&:&
\text{representación metateórica sound},\\
\operatorname{OnticMemoImpl}
&:&
\text{estado actual grounded que realiza esa suficiencia},\\
\operatorname{Update}
&:&
\text{factorización del cambio por el estado memo},\\
\operatorname{Invalidate}
&:&
\text{fallo de }\ker(\mu)\subseteq E_\Theta,\\
\operatorname{Rehydrate}
&:&
\text{adquisición de información adicional tras pérdida irreversible}.
\end{array}
}
\]

MU-T1 caracteriza exactamente cuándo existe update state-based en el caso determinista. MI-T1 prueba monotonicidad bajo coarsening. MI-T2 demuestra que una diferencia ya olvidada no puede recuperarse mediante una transformación del memo antiguo.

La deuda formal de **distinguir SemanticMemo/OnticMemo y dar semántica a update/invalidation** queda por tanto **RESOLVED a nivel de criterio**. La existencia de un OnticMemoImpl concreto sigue siendo una obligación de cada teoría/source, igual que la existencia de testigos concretos de InterfaceContract no se obtiene de la definición.

#### 0.11.85. Memoization es role-relative sin convertirse en relativismo ontológico

Puede ocurrir:

\[
h_i\equiv^{\mathrm{memo}}_{i,\rho_1}h'_i
\]

pero:

\[
h_i\not\equiv^{\mathrm{memo}}_{i,\rho_2}h'_i.
\]

Esto no significa que la historia objetiva dependa del observador ni que \(h_i\) y \(h'_i\) sean “la misma cosa” sin calificación. Significa que una diferencia puede ser irrelevante para un contrato de continuación y decisiva para otro.

Por ello la identidad producida por memoization es:

\[
\boxed{
\text{role-unit identity},
}
\]

no identidad ontológica absoluta por decreto.

La revisión posterior de §§0.11.91k–0.11.91r corrige una cautela demasiado fuerte: que una unidad sea normalmente descrita como **subsistema** no impide que sea además un **contexto anidado**. “Subsistema” describe su relación con un host; “contexto” describe si posee una arena local de tipado, frontera/interfaz y dinámica suficientemente individuadas.

Esto mantiene abierta —y formaliza— una implementación genuina de la ruta theory-relative:

\[
\mathrm{TR\text{-}M}.
\]

Su criterio no es “tener memoria”. Es disponer, **pre-indexadamente**, de una máquina contextual local cuya dinámica reentrante y frontera de interfaz descarguen CI/IA sin usar el índice resultante. Bajo los guards de §§0.11.91k–0.11.91r, un termostato, un servicio KV, una célula o un proceso pueden ser contextos anidados si la teoría correspondiente justifica esa estructura; estar realizados dentro de otro contexto no los descalifica.

Por tanto sigue siendo falso:

\[
\operatorname{MemoState}
\Rightarrow
\operatorname{ContextIndividuation},
\]

pero puede valer:

\[
\boxed{
\operatorname{MemoContextCriterion}_{\mathcal T}(C;\Xi)
+
\operatorname{IndAdequate}^{\mathsf M}(\mathcal T,C,\chi_\Xi)
\Rightarrow
\operatorname{ContextIndividuation}^{\mathsf M}(C;\chi_\Xi).
}
\]

TR-M no se identifica con TR-O ni TR-W. Puede solaparse con ellas cuando la misma estructura local es además organizational closure o world-making structure.

#### 0.11.86. Baking se separa de ContextGenesis

Definimos baking como juicio metateórico genérico:

\[
\boxed{
\operatorname{Bake}^{\mathsf M}_{i\to k}
(u_i\Downarrow\sigma_k;I^\rho,\beta),
}
\]

donde:

- \(u_i\) es una SourceUnit ya justificada en \(i\);
- \(I^\rho\) es una InterfaceContract admisible que fija qué puede importar aguas abajo para el rol \(\rho\);
- \(\sigma_k\) es una realización actual y bien tipada de \(k\);
- \(\beta\) especifica cómo se realiza/preserva esa interfaz en el target.

Bake no es una función objeto entre índices. No existe un token que atraviese literalmente una frontera:

\[
u_i\not\in R_k.
\]

El juicio dice que existe una relación de provenance y suficiencia por la que una estructura target-native \(\sigma_k\) puede desempeñar en \(k\) el rol heredado de \(u_i\).

Por tanto:

\[
\boxed{
\operatorname{Bake}^{\mathsf M}_{i\to k}
\not\Rightarrow
\operatorname{ContextGenesis}^{\mathsf M}.
}
\]

Puede haber baking en continuidad, embedding, reconstrucción o composición sin que nazca un contexto nuevo. ContextGenesis es una aplicación ontogénica particular, no la definición general de baking.

#### 0.11.87. Contrato B1–B10 de baking

La formulación anterior de B7 hablaba de \(\ker(Bake)\) como si el output relevante fuese la identidad literal de \(\sigma_k\). Eso es demasiado intensional: dos realizaciones target-side distintas pueden implementar exactamente el mismo contrato.

Por tanto Baking se tipa ahora respecto de un **contract state**:

\[
\Theta
=
\langle
\rho,
\mathbb I^\rho,
\operatorname{Cont}_\rho,
\text{interaction roles cuando apliquen}
\rangle.
\]

Sea:

\[
E^S_\Theta
\]

la equivalencia source-side autorizada por ese contrato y:

\[
q^S_\Theta(u)
=
[u]_{E^S_\Theta}
\]

su quotient metateórico.

En el target \(k\) definimos una equivalencia contractual:

\[
\sigma_k
\approx^T_{\Theta,k}
\tau_k
\]

cuando ambas realizaciones presentan el mismo perfil target-side para \(\Theta\), incluyendo interacciones declaradas. Escribimos:

\[
q^T_{\Theta,k}(\sigma_k)
=
[\sigma_k]_{\approx^T_{\Theta,k}}.
\]

La igualdad de tokens target no es necesaria:

\[
\sigma_k\neq\tau_k
\]

puede coexistir con:

\[
q^T_{\Theta,k}(\sigma_k)
=
q^T_{\Theta,k}(\tau_k).
\]

El juicio de baking queda:

\[
\boxed{
\operatorname{Bake}^{\mathsf M}_{i\to k}
(
u_i\Downarrow\sigma_k;
\Theta,\beta,\pi
),
}
\]

donde \(\beta\) es el witness de realización contractual y \(\pi\) el witness de provenance. Ambos hacen trabajos distintos: \(\beta\) demuestra sustitución downstream; \(\pi\) demuestra por qué esa realización target puede atribuirse a esa source y no a una coincidencia independiente.

Se exige:

1. **B1 / source unit:** existe \(\operatorname{SourceUnit}^{\mathsf M}_i(u_i;\rho,\upsilon)\) compatible con \(\Theta\). Bake no selecciona retrospectivamente qué agregado source-side debe contar como unidad.
2. **B2 / target actuality:** \(\sigma_k\) es contenido actual de \(k\). El juicio metateórico no fabrica ontología target-side.
3. **B3 / provenance grounding:** \(\operatorname{ProvLink}^{\mathsf M}_{i\to k}(u_i,\sigma_k;\pi)\) debe estar independently justified. Igualdad de interfaz, semejanza, correlación o isomorfismo no bastan.
4. **B4 / typed realization:** todo predicado objeto sobre \(\sigma_k\) está tipado en \(k\); Bake no introduce relaciones objeto cross-index.
5. **B5 / target contract realization:** \(\beta\) demuestra que \(\sigma_k\) realiza target-side el contrato \(\Theta\), incluidos interaction roles relevantes, con una traducción de trazas/perfiles explícita.
6. **B6 / target factorization:** toda consecuencia target-side atribuida a \(\Theta\) factoriza por el perfil contractual de \(\sigma_k\). No existe hidden bypass hacia detalles upstream que \(\Theta\) declara quotientables.
7. **B7 / quotient decodability:** existe una decodificación metateórica \(d_\beta\) tal que, para todo source admisible bakeado por \(\beta\),

\[
\boxed{
q^S_\Theta(u)
=
d_\beta
\left(
q^T_{\Theta,k}(\sigma)
\right).
}
\]

8. **B8 / recoding invariance:** recodificaciones fieles source/target y traducciones fieles del contrato preservan el juicio y el diagrama B7.
9. **B9 / provenance retention + no retroactivity:** quotientar diferencias para \(\Theta\) no elimina hechos source-side ni autoriza a identificar sus provenance. Si la provenance no se codifica en \(\sigma_k\), puede quedar no reconstruible desde ese canal, pero no deja de ser objetiva.
10. **B10 / no genesis/context inference:** Bake no implica ContextGenesis, ContextMerger, TokenMerger, ContextIndividuation, IndexAdmission ni RegimeTotal.

B7 reemplaza la antigua formulación meramente extensional de kernel por una condición más fuerte y tipada. El target debe conservar suficiente estructura contractual para recuperar **la clase source autorizada**, no el token source completo.

#### 0.11.87a. Provenance no es equivalencia de interfaz

Introducimos el witness:

\[
\operatorname{ProvLink}^{\mathsf M}_{i\to k}
(
u_i,\sigma_k;\pi
).
\]

\(\pi\) debe satisfacer al menos:

- **PV1 / source-target anchoring:** identifica source y target actuales ya independientemente tipados;
- **PV2 / genealogical support:** aporta una cadena histórica, productiva, constitutiva, transmisiva o documental cuya teoría explique la atribución target-from-source;
- **PV3 / no similarity inference:** \(u\equiv_I\sigma\), semejanza o isomorfismo no producen ProvLink;
- **PV4 / non-circularity:** \(\pi\) no puede usar como premisa el Bake, GenesisTrivialization o provenance que pretende justificar;
- **PV5 / chain transparency:** si el witness pasa por etapas intermedias, éstas se registran metateóricamente; no se reemplaza una cadena por una relación objeto cross-index;
- **PV6 / non-uniqueness tolerance:** varias sources pueden contribuir a una realización target y una source puede tener varias realizaciones; provenance no presupone función ni identidad.

Así se separan dos preguntas:

\[
\boxed{
\begin{array}{rcl}
\beta &:& \text{¿realiza correctamente el target el contrato?}\\
\pi &:& \text{¿por qué esta realización procede de esta source?}
\end{array}
}
\]

Puede existir una implementación target perfectamente interface-equivalent pero sin \(\pi\); entonces hay **independent reimplementation**, no Bake desde esa source.

#### 0.11.87b. BS-T1 — teorema general de soundness de Bake

Definimos la equivalencia inducida por la realización target:

\[
u
\equiv^{\beta}_{T,\Theta}
v
\]

cuando existen realizaciones bakeadas \(\sigma,\tau\) tales que:

\[
q^T_{\Theta,k}(\sigma)
=
q^T_{\Theta,k}(\tau).
\]

Si B7 vale, entonces:

\[
\boxed{
\equiv^{\beta}_{T,\Theta}
\subseteq
E^S_\Theta.
}
\]

**Demostración.** Si los perfiles target coinciden, aplicar el mismo decoder \(d_\beta\) produce:

\[
q^S_\Theta(u)
=
d_\beta(q^T(\sigma))
=
d_\beta(q^T(\tau))
=
q^S_\Theta(v).
\]

Luego \(uE^S_\Theta v\). \(\square\)

Ésta es la forma correcta de:

\[
\ker(Bake)\subseteq\ker(I^\rho).
\]

El kernel relevante es el del **perfil contractual target**, no el de identidad literal de tokens.

Si además:

\[
uE^S_\Theta v
\Longrightarrow
u\equiv^\beta_{T,\Theta}v,
\]

el Bake es **contract-exact**:

\[
\boxed{
\equiv^\beta_{T,\Theta}
=
E^S_\Theta.
}
\]

Un Bake puede ser sound y conservar más distinciones que el contrato requiere.

#### 0.11.87c. Horizontal composition: product Bake y interaction debt

Sea una familia de roles:

\[
\mathbf R
=
\{\rho_a\}_{a\in A}
\]

con Bakes individuales \(B_a\) y contract states \(\Theta_a\). Supóngase cada uno sound:

\[
\equiv^{B_a}_{T,\Theta_a}
\subseteq
E_a.
\]

El producto:

\[
B_\Pi(u)
=
\langle
B_a(u)
\rangle_{a\in A}
\]

solo preserva por defecto la equivalencia marginal:

\[
E_\wedge
=
\bigcap_aE_a.
\]

El contrato compuesto requiere:

\[
E_\otimes.
\]

Por tanto definimos:

\[
\boxed{
\operatorname{CompositeBakeSound}
(
B_\Pi;\Theta_\otimes
)
}
\]

si existe un decoder conjunto:

\[
d_\otimes
\]

tal que:

\[
\boxed{
q^S_{\Theta_\otimes}(u)
=
d_\otimes
\left(
q^T_{\Theta_\otimes,k}
(B_\Pi(u))
\right).
}
\]

De aquí:

\[
\equiv^{B_\Pi}_{T,\Theta_\otimes}
\subseteq
E_\otimes.
\]

La soundness de cada componente no basta cuando:

\[
E_\otimes
\subsetneq
E_\wedge.
\]

En particular, si cada Bake es exacto marginalmente:

\[
\equiv^{B_a}_{T,\Theta_a}=E_a,
\]

pero existe SynRel, el producto que conserva únicamente esas clases marginales colapsa al menos un par que \(E_\otimes\) separa.

Por tanto:

\[
\boxed{
\bigwedge_a
\operatorname{BakeSound}(B_a;\Theta_a)
\not\Rightarrow
\operatorname{CompositeBakeSound}(B_\Pi;\Theta_\otimes).
}
\]

Bajo CR-T1, si:

\[
E_\otimes=E_\wedge
\]

y la composición target no añade hidden observers, los decoders marginales pueden combinarse para obtener un decoder conjunto. En el caso no separable hace falta información adicional de interacción.

#### 0.11.87d. Interaction-aware Bake

Cuando existe:

\[
\operatorname{SynRel}_{\mathbf R},
\]

un target sound debe conservar además una contribución de interacción:

\[
B_\times(u).
\]

Definimos el Bake enriquecido:

\[
B_+(u)
=
\left\langle
\{B_a(u)\}_{a\in A},
B_\times(u)
\right\rangle.
\]

La condición suficiente es:

\[
\boxed{
q^S_{\Theta_\otimes}
=
d_+
\circ
q^T_{\Theta_\otimes,k}
\circ
B_+.
}
\]

No se exige que \(B_\times\) sea un objeto separado si la interacción está realizada de forma distribuida; la notación representa la **información adicional** que evita la colisión conjunta.

En CR-X, esa información debe distinguir al menos el caso linked del caso unlinked. Guardar por separado el estado del writer y el del reader sin preservar su wiring no basta.

#### 0.11.87e. Vertical composition: encadenar Bakes sin perder soundness

Considérese:

\[
i
\overset{B_1}{\longrightarrow}
k
\overset{B_2}{\longrightarrow}
\ell
\]

como abreviatura metateórica de dos familias de juicios Bake compatibles.

Para que la segunda etapa esté siquiera tipada, cada realización intermedia \(\sigma_k=B_1(u_i)\) que entre en \(B_2\) debe satisfacer una SourceUnit adecuada en \(k\):

\[
\operatorname{SourceUnit}^{\mathsf M}_k
(
\sigma_k;\rho_2,\upsilon_2
).
\]

Definimos **StageCompatibility** como la conjunción de esa unitización intermedia, compatibilidad de typing/provenance y alineación del quotient que la segunda etapa promete preservar.

Supóngase que la primera etapa admite:

\[
q^S_{\Theta,i}
=
d_1
\circ
q^T_{\Theta,k}
\circ
B_1,
\]

y que, bajo StageCompatibility, la segunda preserva precisamente esa clase intermedia:

\[
q^T_{\Theta,k}
=
d_2
\circ
q^T_{\Theta,\ell}
\circ
B_2.
\]

Entonces:

\[
q^S_{\Theta,i}
=
d_1
\circ
d_2
\circ
q^T_{\Theta,\ell}
\circ
B_2
\circ
B_1.
\]

Por tanto:

\[
\boxed{
\operatorname{BakeSound}(B_1)
+
\operatorname{BakeSound}(B_2)
+
\operatorname{StageCompatibility}
\Longrightarrow
\operatorname{BakeSound}(B_2\circ B_1).
}
\]

La condición StageCompatibility es esencial e incluye ContractAlignment. Dos etapas individualmente sound para contratos distintos, o cuyo target intermedio no sea una SourceUnit admisible para la segunda, no pueden componerse por mera transitividad verbal.

La provenance también se conserva solo como cadena:

\[
\pi_{i\to k}
\star
\pi_{k\to\ell}.
\]

No se infiere una relación causal objeto \(i\to\ell\); se conserva un witness metateórico de lineage compuesto.

#### 0.11.87f. Bake invalidation bajo refinement contractual

Sea un Bake sound para \(\Theta\), con abstracción target:

\[
b_\Theta(u)
:=
q^T_{\Theta,k}(\sigma_u).
\]

Supóngase un refinement:

\[
E_{\Theta'}
\subseteq
E_\Theta.
\]

Definimos:

\[
\operatorname{BakeInvalidate}
(
B;
\Theta\rightsquigarrow\Theta'
)
\]

cuando:

\[
\operatorname{BakeSound}(B;\Theta)
\]

pero:

\[
\neg
\operatorname{BakeSound}(B;\Theta').
\]

Equivalentemente existe un par:

\[
b_\Theta(u)
=
b_\Theta(v)
\]

tal que:

\[
u\not E_{\Theta'}v.
\]

Esto es el análogo target-side de Memo invalidation.

#### 0.11.87g. BS-T2 — no rehydration desde un Bake ya colapsado

Supóngase:

\[
\operatorname{BakeInvalidate}
(
B;
\Theta\rightsquigarrow\Theta'
).
\]

Entonces existen \(u,v\) con el mismo perfil baked viejo:

\[
b_\Theta(u)=b_\Theta(v)
\]

pero:

\[
u\not E_{\Theta'}v.
\]

Para cualquier postprocesamiento que dependa únicamente de ese perfil:

\[
F:
\operatorname{Im}(b_\Theta)
\to Z,
\]

se cumple:

\[
F(b_\Theta(u))
=
F(b_\Theta(v)).
\]

Por tanto:

\[
\boxed{
\forall F:
\quad
F\circ b_\Theta
\text{ sigue siendo unsound para }\Theta'.
}
\]

Éste es **BS-T2 — baked no-recovery theorem**.

El target solo puede rehidratarse si recibe side information adicional:

\[
z(u),
\]

y la representación aumentada:

\[
\widetilde b(u)
=
\langle
b_\Theta(u),z(u)
\rangle
\]

satisface:

\[
\boxed{
\ker(\widetilde b)
\subseteq
E_{\Theta'}.
}
\]

No basta con postular un \(z\) matemáticamente discriminante. Introducimos:

\[
\operatorname{RehydrateSource}^{\mathsf M}
(
z;B,\Theta',\zeta
),
\]

donde \(\zeta\) descarga:

1. **RH1 / actuality or persistence:** \(z\) existe actualmente o persiste en un registro/canal cuya teoría admite como real;
2. **RH2 / independent grounding:** su contenido no se define usando la respuesta correcta que la rehydration pretende reconstruir;
3. **RH3 / accessibility:** el procedimiento de rehydration dispone de un canal tipado para adquirir \(z\);
4. **RH4 / recoding/provenance discipline:** recodificaciones fieles preservan su poder discriminante y, si \(z\) contiene provenance, esa provenance cuenta con witness independiente.

Definimos entonces:

\[
\boxed{
\operatorname{RehydrateAdequate}
(
z;
B,\Theta'
)
}
\]

si:

\[
\operatorname{RehydrateSource}^{\mathsf M}
(
z;B,\Theta',\zeta
)
\]

y:

\[
\ker
\left(
u\mapsto
\langle b_\Theta(u),z(u)\rangle
\right)
\subseteq
E_{\Theta'}.
\]

La provenance puede actuar como \(z\), pero **solo si está disponible y es discriminativamente suficiente** para \(\Theta'\). Un certificado que dice “procede de P” sin conservar la diferencia concreta requerida por el nuevo contrato no rehidrata nada.

#### 0.11.87h. Provenance-preserving y provenance-erasing Bake

La existencia objetiva de \(\pi\) no implica que el target la conserve internamente.

Distinguimos:

\[
\operatorname{ProvPreservingBake}
\]

cuando existe una codificación target-side \(p_k(\sigma)\) y un decoder de provenance suficiente para la clase declarada, frente a:

\[
\operatorname{ProvErasingBake},
\]

cuando B9 conserva la verdad objetiva del lineage pero el perfil target contractual no permite reconstruirla.

Un QuotientBake puede ser perfectamente sound y a la vez provenance-erasing.

Esta distinción enlaza rehydration con InterfaceWall:

- si provenance persiste en un canal lateral/certificado, puede servir como side information para refinements futuros;
- si fue borrada de **todos** los canales físicamente/ontológicamente disponibles, no puede reaparecer por postprocesamiento del Bake.

La segunda afirmación todavía no demuestra el Muro genealógico fuerte: exige demostrar exhaustividad de canales, deuda que permanece en REV-15.

#### 0.11.87i. Estado de B1–B10

B1–B10 quedan ahora coordinadas con la semántica previa:

\[
\boxed{
\begin{array}{rcl}
\text{SourceUnit} &\to& \text{B1},\\
\text{actualidad target} &\to& \text{B2},\\
\text{ProvLink} &\to& \text{B3/B9},\\
\text{typing} &\to& \text{B4},\\
\text{Interface/RoleComposition} &\to& \text{B5/B6},\\
q^S_\Theta=d_\beta\circ q^T_{\Theta,k} &\to& \text{B7},\\
\text{recoding} &\to& \text{B8},\\
\text{no context inference} &\to& \text{B10}.
\end{array}
}
\]

BS-T1 prueba el kernel bound contractual; horizontal composition identifica la interaction debt; vertical composition es sound bajo StageCompatibility —incluida unitización intermedia y ContractAlignment—; BS-T2 demuestra no-recovery tras quotient baking; RehydrateSource RH1–RH4 + RehydrateAdequate caracterizan información lateral real, accesible y suficiente para reparar un refinement.

Por tanto la deuda específica de **coordinar B1–B10 con la semántica de interfaces/memoization, composite Bake soundness y rehydration/provenance** queda **RESOLVED a nivel de criterio**.

#### 0.11.88. ConservativeBake y QuotientBake

La nueva separación permite conservar la taxonomía previa sin identificarla con GenesisTrivialization.

**ConservativeBake.** El contrato \(\beta\) preserva información suficiente para reconstruir la SourceUnit relevante, dada una teoría de decodificación adicional a B7:

\[
\operatorname{Bake}^{\mathsf M}_{i\to k}
(u_i\Downarrow\sigma_k;\Theta,\beta,\pi)
+
\operatorname{Recoverable}^{\mathsf M}(u_i\mid\sigma_k,\beta,\pi).
\]

ConservativeBake es más fuerte que BakeSound: B7 solo exige recuperar la **clase contractual source**, mientras ConservativeBake exige recuperar la SourceUnit al nivel declarado por la teoría de reconstrucción.

**QuotientBake.** Dos SourceUnit genuinamente distintas pueden realizar target tokens distintos o iguales y, sin embargo, caer en la misma clase contractual target:

\[
\operatorname{Bake}^{\mathsf M}_{i\to k}
(u_i\Downarrow\sigma_k;\Theta,\beta,\pi_u),
\]

\[
\operatorname{Bake}^{\mathsf M}_{j\to k}
(v_j\Downarrow\tau_k;\Theta,\beta,\pi_v),
\]

con:

\[
u_i\not\simeq v_j,
\qquad
q^T_{\Theta,k}(\sigma_k)
=
q^T_{\Theta,k}(\tau_k).
\]

Definimos solo metateóricamente:

\[
u_i
\sim^{\mathsf M}_{\operatorname{Bake},k,\Theta,\beta}
v_j
\Longleftrightarrow
u_i\equiv^\beta_{T,\Theta}v_j.
\]

La igualdad literal de outputs deja de ser el criterio. La pregunta correcta es:

\[
\boxed{
\text{¿la equivalencia contractual target satisface B7 respecto de }E^S_\Theta,
\text{ o es una pérdida de distinción no autorizada?}
}
\]

Solo en el primer caso la colisión es una quotient convergence legítima.

#### 0.11.89. Tres niveles de equivalencia: Memo, Interface y Bake

Esta separación impide confundir tres equivalencias conceptualmente diferentes.

El kernel de memoization:

\[
h_i
\equiv^{\mathrm{memo}}_{i,\rho}
h'_i
\]

dice que diferencias internas de dos historias no son necesarias para sus continuaciones source-side bajo \(\rho\).

La equivalencia de interfaz:

\[
u_i
\equiv^{\mathsf M}_{I^\rho}
v_j
\]

dice que, pese a poder seguir siendo SourceUnit e historias distintas, ambas presentan el mismo comportamiento relevante al consumidor bajo el contrato.

La equivalencia inducida por baking:

\[
u_i
\sim^{\mathsf M}_{\operatorname{Bake},k,\Theta,\beta}
v_j
\Longleftrightarrow
u_i\equiv^\beta_{T,\Theta}v_j
\]

dice que las realizaciones target-side caen en la misma clase contractual, aunque sus tokens puedan seguir siendo distintos. Para ser sound debe respetar:

\[
\equiv^{\beta}_{T,\Theta}
\subseteq
E^S_\Theta.
\]

Así Interface/contract state fija la máxima equivalencia downstream admisible y Bake decide qué parte de esa equivalencia realiza de hecho, comparando perfiles target y no identidad literal de tokens.

Por tanto puede ocurrir:

\[
h_i
\not\equiv^{\mathrm{memo}}_{i,\rho}
h'_i
\]

mientras:

\[
q^T_{\Theta,k}
(
\operatorname{Bake}(m_i)
)
=
q^T_{\Theta,k}
(
\operatorname{Bake}(m'_i)
).
\]

La abreviatura expresa igualdad de clase contractual target, no identidad necesaria de los tokens realizados.

Esta geometría es exactamente la que necesita SignatureConvergence: dos fuentes que siguen siendo realmente diferentes source-side pueden converger en una misma contribución porque **el hijo trivializa una diferencia que el padre todavía necesitaba**.

La composición conceptual queda:

\[
\boxed{
P_i
\xrightarrow{\operatorname{Memo}^{\Theta}}
m_i
\longrightarrow
\mathbb I_i^\rho
\overset{\mathsf M}{\xrightarrow{\operatorname{Bake}^{\Theta,\beta,\pi}_{i\to k}}}
\sigma_k.
}
\]

Memo responde “¿qué del pasado necesito conservar para seguir satisfaciendo la interfaz?”. Interface responde “¿qué puede importar al consumidor?”. Bake responde “¿cómo realizo ese contrato dentro del target?”.

#### 0.11.90. GenesisTrivialization pasa a ser una aplicación de Bake

REV-07e queda refinado, no eliminado.

Para una ContextGenesis real:

\[
\operatorname{ContextGenesis}^{\mathsf M}(\ldots\Rightarrow k;\gamma),
\]

una contribución parental puede satisfacer:

\[
\operatorname{Bake}^{\mathsf M}_{i\to k}
(u_i\Downarrow\sigma_k;\Theta,\beta,\pi).
\]

Cuando además esa realización desempeña el papel constitutivo/suficiente exigido por la formación \(\gamma\), obtenemos el caso ontogénico:

\[
\boxed{
\operatorname{GenesisTrivialization}^{\mathsf M}_{i\to k}
(u_i\Rightarrow\sigma_k;\gamma,\Theta,\beta,\pi).
}
\]

Por tanto, arquitectónicamente:

\[
\boxed{
\operatorname{GenesisTrivialization}
\subset
\operatorname{Bake},
}
\]

entendiendo \(\subset\) aquí como relación entre clases de juicios metateóricos, no como inclusión de objetos.

Los antiguos GT1–GT7 se redistribuyen:

- provenance, actuality, factorization, screening-off, no-retroactivity y recoding invariance pasan a obligaciones generales B2–B9;
- la conexión específica con una formación constitutiva permanece en GenesisTrivialization;
- ContextGenesis deja de ser condición para hablar de baking en general.

Esto reduce la sobrecarga conceptual de REV-07e y permite reutilizar la teoría de baking en ContextEmbedding, FaithfulContinuation y otras interfaces futuras sin fingir que toda recontextualización es nacimiento de un contexto.

#### 0.11.90a. Interface Wall: una forma estructural candidata del Muro genealógico

La interfaz permite formular con más precisión la subdeterminación genealógica de REV-15.

Supóngase:

\[
P_i\not\simeq Q_j,
\qquad
P_i\equiv^{\mathsf M}_{I^\rho}Q_j.
\]

Si además toda evidencia disponible para un consumidor \(C_k\) sobre ese upstream factoriza por \(I^\rho\), entonces desde ese canal:

\[
\operatorname{Evidence}_{C_k}(P_i)
=
\operatorname{Evidence}_{C_k}(Q_j).
\]

Bajo esas condiciones, la provenance completa no es recuperable **desde la interfaz sola**:

\[
\boxed{
I^\rho
\not\Rightarrow
\text{unique upstream provenance}.
}
\]

Esto es más fuerte que mera ignorancia contingente, pero todavía más débil que el Muro universal. Para obtener irreconstruibilidad de principio hay que demostrar además que no existe ningún canal independiente, certificado persistente o interfaz lateral que discrimine los representantes del kernel.

Definimos por ello solo el candidato:

\[
\operatorname{InterfaceWall}^{\mathsf M}
(P_i,Q_j;I^\rho,C_k)
\]

cuando:

1. \(P_i\not\simeq Q_j\);
2. \(P_i\equiv_{I^\rho}^{\mathsf M}Q_j\);
3. toda evidencia downstream relevante de \(C_k\) sobre esa contribución factoriza por \(I^\rho\);
4. no se ha supuesto ya la ausencia absoluta de otros canales para obtener la conclusión.

Entonces InterfaceWall demuestra **subdeterminación relativa al canal**. REV-15 solo podrá promoverla a Muro genealógico fuerte si se prueba que el canal relevante es exhaustivo para la reconstrucción considerada.

#### 0.11.91. Derivación de ContinuationProfile: de invariantes elegidos a dinámica quotientada

Ship of Theseus había dejado FC3 abierto porque ContinuationProfile era una lista primitiva de rasgos supuestamente importantes. La maquinaria de Interface/Memoization permite eliminar esa primitivización.

La idea central es:

\[
\boxed{
\operatorname{ContinuationProfile}
\neq
\text{lista de propiedades que deben permanecer iguales}.
}
\]

Un perfil de continuación debe describir **qué futuros role-relevant siguen abiertos, cómo evoluciona el estado suficiente y qué estructura debe conmutar durante esa evolución**.

Para ello introducimos primero una base source-side fijada antes de mirar cualquier candidato descendiente.

#### 0.11.91a. PersistenceBasis independiente del descendiente

Para evitar desplazar la selección post hoc desde ContinuationProfile hacia la propia PersistenceBasis, una teoría de persistencia \(\mathcal T_P\) debe fijar previamente una especificación source-side:

\[
\mathbb P_i^x
=
\left\langle
\operatorname{MaintRole},
\operatorname{MaintStep},
\operatorname{ProvPolicy},
\operatorname{NoveltyPolicy}
\right\rangle.
\]

Estos clasificadores no pueden mencionar un child candidato, un ProfileMorphism futuro ni el resultado deseado de FaithfulContinuation.

Para un token o SourceUnit \(x_i\), una **PersistenceBasis** es:

\[
\boxed{
\operatorname{PersistenceBasis}^{\mathsf M}_i
(
x_i;\Pi_i^x,\psi
)
}
\]

con:

\[
\Pi_i^x
=
\left\langle
\mathcal R_x,
\Theta_x,
\mathcal G_x,
\mathfrak P_x,
\mathcal N_x
\right\rangle.
\]

Sus componentes son:

- \(\mathcal R_x\): familia de roles cuya continuidad está grounded source-side;
- \(\Theta_x\): contract state conjunto, cerrado bajo interaction roles relevantes;
- \(\mathcal G_x\): generadores de transformación/update internos que la teoría source-side admite;
- \(\mathfrak P_x\): requisitos de provenance/lineage que una continuación debe satisfacer;
- \(\mathcal N_x\): política de novedad permitida —qué cambios pueden aparecer sin destruir por ello la continuación.

El witness \(\psi\) debe descargar **PB1–PB8**.

**PB1 — present-source grounding.** La selección se fundamenta en estructura actual de \(x_i\): SourceUnit, dependencias constitutivas/causales/organizacionales, InterfaceContracts o dinámica productiva ya justificadas. No se deriva de un futuro child.

**PB2 — candidate independence.**

\[
\operatorname{IndependentOfChild}^{\mathsf M}
(
\Pi_i^x,x_k
)
\]

para todo candidato posterior \(x_k\). Ningún componente de \(\Pi_i^x\) puede seleccionarse porque precisamente ese candidato lo conserve.

**PB3 — role grounding + coverage.** Introducimos un clasificador source-side:

\[
\operatorname{MaintRole}^{\mathsf M}_i
(
x_i,\rho;\eta
),
\]

cuyo witness \(\eta\) solo puede usar estructura actual ya justificada —SourceUnit, constitución, causalidad, organización, InterfaceContract o dinámica productiva— y no ContinuationProfile, FaithfulContinuation ni ningún child candidato.

Todo \(\rho\in\mathcal R_x\) debe satisfacer MaintRole. Para una FaithfulContinuation **no cualificada** se exige además coverage:

\[
\boxed{
\operatorname{MaintRole}^{\mathsf M}_i(x_i,\rho)
\Longrightarrow
\rho\in\mathcal R_x.
}
\]

Puede estudiarse una continuidad deliberadamente scoped respecto de un subconjunto \(\mathcal S\subset\mathcal R_x\), pero el juicio debe quedar explícitamente cualificado:

\[
\operatorname{FaithfulContinuation}^{\mathsf M,\mathcal S}.
\]

Una continuación scoped no puede promoverse por omisión a FaithfulContinuation no cualificada. Del mismo modo, si existen PersistenceSpecs rivales \(\mathbb P\) y \(\mathbb P'\), el juicio debe escribirse theory-relative; no hay una elección silenciosa de la teoría que favorezca al candidato.

**PB4 — interaction closure.** Si dos roles de \(\mathcal R_x\) presentan SynRel o una dependencia cross-role independently grounded, \(\Theta_x\) debe incluir el interaction role/contract correspondiente. No se permite construir persistencia a partir de marginals ignorando una interacción conocida.

**PB5 — transition grounding.** Cada \(g\in\mathcal G_x\) debe ser una transformación well-typed admitida por la teoría actual del source —por ejemplo update, proceso productivo, reemplazo organizacional o transición operacional— y no una transformación inventada para conectar retrospectivamente dos endpoints.

**PB6 — maintenance coverage.** Toda dependencia source-side cuya alteración pueda cambiar la satisfacción futura de algún rol de \(\Theta_x\) debe quedar representada por el contract state, un interaction role o los generadores de transición. Si una dependencia relevante queda fuera, la base es incompleta.

**PB7 — provenance/novelty independence.** \(\mathfrak P_x\) y \(\mathcal N_x\) se fijan antes de evaluar al descendiente. La teoría puede permitir novedad, branching o quotienting, pero debe decirlo antes del caso concreto.

**PB8 — least closure + recoding + no ontological promotion.** \(\Pi_i^x\) debe ser la menor estructura cerrada que satisface los clasificadores de \(\mathbb P_i^x\), PB3–PB7 y las reglas de interaction/transition closure. No pueden añadirse ni omitirse componentes solo para alterar el resultado del test. Recodificaciones fieles preservan esa closure; PersistenceBasis no implica por sí sola ContextIndividuation, identidad absoluta ni RegimeTotal.

PersistenceBasis no pretende decidir de manera universal qué hace que “un barco sea el mismo barco”. Hace una afirmación más precisa: **dada una teoría de persistencia source-side independently grounded, fija todo lo que el test de continuación puede consultar**. Si hay teorías de persistencia rivales, los juicios deben quedar indexados por \(\mathcal T_P\); la notación no cualificada solo suprime ese parámetro cuando la teoría ambiente ya lo ha fijado.

#### 0.11.91b. Quotient dinámico de continuación

Sea:

\[
E_{\Theta_x}
=
\equiv^{\mathrm{memo}}_{i,\Theta_x}
\]

la memo-equivalence completa inducida por el contract state de la PersistenceBasis.

Sea \(h_x\) una historia actual que termina en la realización \(x_i\). Denotamos:

\[
q_x
:=
[h_x]_{E_{\Theta_x}}.
\]

Sea:

\[
\operatorname{Cl}_{\mathcal G_x}
\]

la menor clausura de continuaciones generada por \(\mathcal G_x\) y las continuation semantics de \(\Theta_x\).

Definimos el espacio alcanzable quotientado:

\[
Q_x^\Pi
:=
\left\{
[h_x\odot c]_{E_{\Theta_x}}
\;\middle|\;
c\in\operatorname{Cl}_{\mathcal G_x},
\;
\operatorname{App}(h_x,c)
\right\}.
\]

Para cada generador \(g\in\mathcal G_x\), proponemos:

\[
[h]
\xrightarrow{g}_{\Pi}
[h\odot g].
\]

Esta transición está bien definida solo si:

\[
\boxed{
E_{\Theta_x}
\text{ es right-congruence para todo }g\in\mathcal G_x.
}
\]

Si falla, el supuesto estado suficiente no soporta la dinámica de persistencia: debe refinarse el memo/contract state antes de hablar de un ContinuationProfile reentrante.

La observación contractual quotientada es:

\[
O^\Pi_x([h])
:=
\operatorname{Obs}_{\Theta_x}(h),
\]

entendida módulo la equivalencia observacional fijada por \(\Theta_x\).

#### 0.11.91c. Definición derivada de ContinuationProfile

Cuando PB1–PB8 están descargadas y las transiciones quotient son well-defined, definimos:

\[
\boxed{
\operatorname{ContinuationProfile}_i
(
x_i;\Pi_i^x
)
:=
\mathsf{CP}_i^x
}
\]

con:

\[
\boxed{
\mathsf{CP}_i^x
=
\left\langle
Q_x^\Pi,
q_x,
\mathcal G_x,
\Rightarrow_\Pi,
O_x^\Pi,
\mathfrak P_x,
\mathcal N_x
\right\rangle.
}
\]

Por tanto el perfil es un **sistema de transición apuntado y observado**, no una colección de invariantes extensionales.

Sus componentes responden a preguntas distintas:

\[
\begin{array}{rcl}
Q_x^\Pi &:& \text{qué estados futuros cuentan como equivalentes para la persistencia},\\
q_x &:& \text{estado quotient actual},\\
\mathcal G_x &:& \text{qué transformaciones internas están autorizadas},\\
\Rightarrow_\Pi &:& \text{cómo evolucionan las clases bajo esas transformaciones},\\
O_x^\Pi &:& \text{qué conducta contractual debe seguir siendo observable},\\
\mathfrak P_x &:& \text{qué lineage exige una continuación real},\\
\mathcal N_x &:& \text{qué novedad puede aparecer sin destruir continuidad}.
\end{array}
\]

El perfil puede ser infinito, branching o no determinista. No presupone que exista una lista finita de propiedades esenciales.

#### 0.11.91d. CP-T0/CP-T1 — invariancia de base y well-definedness

**CP-T0 — persistence-basis invariance.** Sean \(\Pi\) y \(\Pi'\) dos realizaciones de PersistenceBasis para el mismo \(x_i\) y la misma especificación \(\mathbb P_i^x\), ambas satisfaciendo least closure y recoding invariance. Entonces las diferencias puramente representacionales entre ambas no pueden alterar la semántica de continuidad: sus sistemas quotient deben ser bisimilares mediante una recodificación que preserve root, labels role-relevant y observaciones:

\[
\boxed{
\operatorname{PersistenceBasis}_{\mathbb P}(x;\Pi)
\land
\operatorname{PersistenceBasis}_{\mathbb P}(x;\Pi')
\Longrightarrow
\mathsf{CP}(x;\Pi)
\simeq_{\mathrm{bis}}
\mathsf{CP}(x;\Pi').
}
\]

Si dos supuestas bases para la **misma** \(\mathbb P\) producen perfiles no bisimilares, al menos una viola least closure, coverage o recoding invariance. Si proceden de especificaciones \(\mathbb P\) genuinamente rivales, el desacuerdo es teórico y debe hacerse explícito; no se oculta bajo una FaithfulContinuation no indexada.

**CP-T1 — well-definedness.** Si:



1. \(\operatorname{PersistenceBasis}(x_i;\Pi,\psi)\);
2. \(E_\Theta\) es una equivalencia;
3. \(E_\Theta\) es right-congruence bajo cada generador \(g\in\mathcal G_x\);
4. \(O^\Pi_x\) es constante sobre clases \(E_\Theta\);

entonces \(\mathsf{CP}_i^x\) es independiente del representante history elegido dentro de cada clase.

**Demostración.** Sean:

\[
hE_\Theta h'.
\]

Por right-congruence:

\[
h\odot g
E_\Theta
h'\odot g,
\]

luego la clase target de la transición no depende del representante. Por definición de \(E_\Theta\), las observaciones contractuales tampoco dependen del representante. Las clausuras compuestas siguen por inducción sobre continuaciones finitas y por el principio adicional de closure cuando la semántica sea infinitaria/continua. \(\square\)

Así el ContinuationProfile está derivado del quotient semántico y de su dinámica; no de una codificación particular del history.

#### 0.11.91e. Realización por MemoState: el perfil no se reifica automáticamente

\(\mathsf{CP}_i^x\) sigue siendo una estructura metateórica. No implica que exista dentro de \(i\) un objeto cuyo contenido sea literalmente el quotient.

Si existe:

\[
\operatorname{OnticMemoImpl}^{\mathsf M}_i
(
\mu_i;M_i,\Theta_x,\omega
)
\]

y updates:

\[
U_g:M_i\to M_i
\]

que satisfacen MU-T1 para los generadores de \(\mathcal G_x\), entonces el sistema de estados memo realiza el perfil mediante:

\[
r_\mu:
M_i
\to
Q_x^\Pi,
\qquad
r_\mu(\mu(h))
=
[h]_{E_{\Theta_x}}.
\]

Para un MemoExact, \(r_\mu\) identifica exactamente las clases del perfil. Para un MemoOvercomplete, varios estados memo pueden mapear a la misma clase contractual.

Por tanto:

\[
\boxed{
\operatorname{OnticMemoImpl}
\text{ puede realizar }
\operatorname{ContinuationProfile},
}
\]

pero:

\[
\boxed{
\operatorname{ContinuationProfile}
\not\Rightarrow
\operatorname{OnticMemoImpl}.
}
\]

#### 0.11.91f. TargetRealizationProfile y ProfileMorphism

Para comprobar que \(y_k\) continúa a \(x_i\) no exigimos que el child posea ya una PersistenceBasis propia idéntica a la parental. Eso sería demasiado fuerte y podría confundir “realiza el legado source” con “se individúa autónomamente por el mismo criterio”.

Una traducción de continuidad:

\[
\tau
=
\langle
\tau_G,
\tau_O
\rangle
\]

transporta la parte preservable de \(\Pi_i^x\) a un contrato target:

\[
\tau\Pi_i^x.
\]

Si \(y_k\) realiza ese contrato target y sus continuaciones traducidas están bien definidas, construimos el **TargetRealizationProfile**:

\[
\boxed{
\operatorname{TargetRealizationProfile}^{\mathsf M}_k
(
y_k;\tau\Pi_i^x
)
=
\mathsf{TRP}_{k}^{y\mid\tau\Pi}.
}
\]

Su construcción repite el quotient dinámico de §§0.11.91b–0.11.91d, pero restringida al contrato heredado/traducido que debe realizarse en \(k\). No afirma todavía que ese contrato agote la identidad propia del child.

Si \(y_k\) dispone además de una PersistenceBasis propia \(\Pi_k^y\), debe existir una compatibilidad explícita entre \(\mathsf{TRP}_{k}^{y\mid\tau\Pi}\) y la proyección correspondiente de \(\mathsf{CP}_k^y\) para poder usar \(y_k\) como stage intermedio de futuras continuaciones.

La traducción puede enviar un generador source a una continuación target:

\[
\tau_G(g)
\in
\operatorname{Cont}_{k,\tau\Theta_x},
\]

no necesariamente a un único step atómico.

Definimos:

\[
\boxed{
\operatorname{ProfileMorphism}^{\mathsf M}_{i\to k}
(
\mathsf{CP}_i^x,
\mathsf{TRP}_{k}^{y\mid\tau\Pi};
\Phi,\tau
)
}
\]

cuando se satisfacen **PM1–PM8**.

**PM1 — root preservation.**

\[
\Phi(q_x)=q_y
\]

al nivel contractual declarado.

**PM2 — transition simulation.** Si:

\[
q\xrightarrow{g}_\Pi q',
\]

entonces:

\[
\Phi(q)
\xRightarrow{\tau_G(g)}
\Phi(q').
\]

La flecha target puede expandir un source step en una secuencia, proceso o realization equivalente.

**PM3 — observation preservation.**

\[
O_y(\Phi(q))
\simeq_\tau
\tau_O(O_x(q))
\]

para todas las dimensiones que \(\Theta_x\) exige preservar.

**PM4 — explicit transformation.** Una estructura source declarada transformable puede cambiar solo mediante una regla de \(\mathcal N_x\) o traducción explicitada; no puede desaparecer silenciosamente.

**PM5 — permitted novelty.** El target puede contener estados, observables o dependencias adicionales siempre que no contradigan PM2–PM4 ni la política \(\mathcal N_x\).

**PM6 — interaction preservation.** Interaction roles incluidos por PB4 deben preservarse/traducirse conjuntamente. No basta con preservar cada marginal si el source profile contiene SynRel relevante.

**PM7 — recoding invariance.** Recodificaciones fieles de ambos perfiles transportan \(\Phi,\tau\) sin cambiar la existencia del morphism.

**PM8 — no inverse requirement.** \(\Phi\) no tiene que ser inyectiva ni sobreyectiva. Continuación permite branching, implementation expansion y quotienting autorizado; un morphism no implica identidad.

#### 0.11.91g. FC3 queda descargado: FaithfulContinuation derivada

Reformulamos la arquitectura de FaithfulContinuation.

Para admitir:

\[
\operatorname{FaithfulContinuation}^{\mathsf M}_{i\to k}
(
x_i,y_k;
\gamma,\tau
),
\]

se requiere:

1. endpoints correctamente tipados;
2. una PersistenceBasis source-side:

\[
\operatorname{PersistenceBasis}^{\mathsf M}_i
(
x_i;\Pi_i^x,\psi
);
\]

3. el ContinuationProfile derivado \(\mathsf{CP}_i^x\);
4. un TargetRealizationProfile \(\mathsf{TRP}_{k}^{y\mid\tau\Pi}\) para la PersistenceBasis traducida;
5. provenance independently grounded de la trayectoria \(\gamma\), mediante ProvLink o witness específico de formación;
6. un ProfileMorphism:

\[
\operatorname{ProfileMorphism}^{\mathsf M}_{i\to k}
(
\mathsf{CP}_i^x,
\mathsf{TRP}_{k}^{y\mid\tau\Pi};
\Phi,\tau
);
\]

7. no retroactivity y no index collapse.

Si el juicio pretende ser FaithfulContinuation no cualificada, PB3 exige role coverage completo respecto de MaintRole. Si solo se ha demostrado un subconjunto de roles, el resultado permanece explícitamente scoped.

Con ello, la antigua FC3:

\[
\text{“existe un ContinuationProfile previo no post hoc”}
\]

queda sustituida por un criterio constructivo:

\[
\boxed{
\operatorname{PersistenceBasis}
+
E_\Theta
+
\text{quotient dynamics}
\Longrightarrow
\operatorname{ContinuationProfile}.
}
\]

La independencia respecto del child viene de PB2, no de una promesa informal.

FC4 y FC5 quedan absorbidas por PM2–PM4; FC6 por PM5; FC9 por PM7. FC2 sigue siendo indispensable y separado: un ProfileMorphism perfecto sin provenance describe una réplica estructural, no una continuación genealógica.

FC10/auditability exige ahora exhibir:

\[
\boxed{
\mathbb P_i^x,\;
\psi,\;
\Theta_x,\;
\mathsf{CP}_i^x,\;
\mathsf{TRP}_{k}^{y\mid\tau\Pi},\;
\pi_\gamma,\;
\Phi,\;
\tau
}
\]

o equivalentes formalmente transportados. No exige que el child reconstruya internamente toda la provenance.

#### 0.11.91h. FC-T1 — réplica, branching y composición

**Réplica perfecta.** Puede existir:

\[
\operatorname{ProfileMorphism}
(
\mathsf{CP}_i^x,
\mathsf{TRP}_k^{z\mid\tau\Pi}
)
\]

sin ProvLink. Entonces:

\[
\boxed{
\operatorname{ProfileMorphism}
\not\Rightarrow
\operatorname{FaithfulContinuation}.
}
\]

Se conserva el resultado F1 sin recurrir a semejanza superficial.

**Branching.** Un mismo profile source puede admitir:

\[
\Phi_1:
\mathsf{CP}_i^x\to\mathsf{TRP}_k^{y_1\mid\tau_1\Pi},
\qquad
\Phi_2:
\mathsf{CP}_i^x\to\mathsf{TRP}_k^{y_2\mid\tau_2\Pi}
\]

con provenance válida para ambas trayectorias. FaithfulContinuation sigue siendo relacional, no funcional.

**Composición condicional.** Supóngase:

\[
x_i
\overset{FC}{\longrightarrow}
y_k
\overset{FC}{\longrightarrow}
z_\ell.
\]

Si:

1. el stage intermedio \(y_k\) posee una PersistenceBasis propia cuya proyección es compatible con el TargetRealizationProfile heredado, y los ProfileMorphisms resultantes son composables;
2. las traducciones satisfacen coherencia:

\[
\tau_{i\ell}
\simeq
\tau_{k\ell}\circ\tau_{ik};
\]

3. la provenance compone como witness metateórico;
4. no ocurre una invalidación intermedia del contract state no reparada mediante rehydration;

entonces:

\[
\boxed{
\operatorname{FC}_{i\to k}(x,y)
+
\operatorname{FC}_{k\to\ell}(y,z)
+
\operatorname{FCStageCompatibility}
\Longrightarrow
\operatorname{FC}_{i\to\ell}(x,z).
}
\]

Así la antigua cautela “FC no es transitiva automáticamente” se conserva, pero ahora sabemos exactamente qué hace falta para componerla.

#### 0.11.91i. Ship of Theseus: qué queda resuelto y qué no

Sea una secuencia:

\[
x^{(0)}
\leadsto
x^{(1)}
\leadsto
\cdots
\leadsto
x^{(n)}
\]

en la que incluso todos los constituyentes materiales pueden haber sido reemplazados.

Si existe una PersistenceBasis independently grounded y cada transición induce updates well-defined sobre el mismo quotient dinámico —o refinements correctamente rehidratados—, entonces el cambio total de piezas **no refuta** la continuidad:

\[
\operatorname{Parts}(x^{(0)})
\cap
\operatorname{Parts}(x^{(n)})
=
\varnothing
\]

es compatible con una cadena de ProfileMorphisms/updates.

A la inversa, conservar todas las piezas tampoco basta si se rompe la dinámica contractual, la provenance exigida o aparece una invalidación no reparada.

La maquinaria no pretende resolver por decreto todos los casos ordinarios de “el mismo barco”. Si una teoría no puede justificar PB1–PB8 para el barco, no obtiene una respuesta gratuita. Lo que sí queda resuelto es la circularidad formal de FC3:

\[
\boxed{
\text{el perfil ya no se selecciona mirando qué conserva el descendiente.}
}
\]

Se deriva source-side de roles, interfaces, interactions, memo-equivalence y dinámica de update previamente justificados.

Por tanto la deuda específica de **derivar ContinuationProfile y coordinarlo con FaithfulContinuation sin invariantes post hoc** queda **RESOLVED a nivel de criterio**.

#### 0.11.91j. Stress tests de ContinuationProfile

**CP-S1 — child-tailored profile.** Se observa primero \(y_k\) y se eligen solo los roles/transformaciones de \(x_i\) que \(y_k\) conserva. Falla PB2.

**CP-S2 — role omission.** Dos MaintRole están independently grounded pero se omite uno porque rompe la continuidad candidata. El resultado puede ser una FaithfulContinuation scoped, nunca la no cualificada; falla PB3 coverage.

**CP-S3 — marginal-only persistence.** Se incluyen dos roles individualmente pero se omite su interaction role pese a SynRel. Falla PB4 y puede fabricar un quotient demasiado grueso.

**CP-S4 — non-congruent memo.** Un memo parece suficiente en el estado actual pero dos histories colapsados evolucionan a clases distintas bajo un generador de \(\mathcal G_x\). La transición quotient no está bien definida; CP-T1 no aplica.

**CP-S5 — perfect replica.** El child realiza un TargetRealizationProfile isomorfo pero no existe provenance. ProfileMorphism puede valer; FaithfulContinuation falla por FC2.

**CP-S6 — material conservatism.** Se preservan todos los componentes pero una dependencia de mantenimiento o interaction role deja de satisfacerse. La mera identidad material no preserva el perfil.

**CP-S7 — total replacement.** Ningún constituyente inicial sobrevive, pero los updates/profile morphisms satisfacen el quotient dinámico y provenance. El reemplazo extensional total no refuta por sí mismo la continuidad.

**CP-S8 — inherited-contract fallacy.** El child realiza perfectamente el contrato parental y se infiere que esa estructura agota su propia identidad futura. Falla la distinción entre TargetRealizationProfile y PersistenceBasis propia del child.

Estos tests muestran que la construcción evita simultáneamente dos trivializaciones opuestas: no permite declarar continuidad escogiendo lo que sobrevivió, ni exige identidad material/estructural total para conservarla.

#### 0.11.91k. TR-M revisado: contextos locales y anidados

La objeción “un termostato o un servicio KV son solo subsistemas” no resuelve la cuestión de individuación. Un mismo realizador puede ocupar dos estatutos compatibles:

\[
\boxed{
\text{objeto/subsistema en el host}
\quad+\quad
\text{contexto para una arena interna}.
}
\]

No se identifica el token host-side con el contexto interno. Si ambos niveles son admitidos, su relación se expresa después mediante:

\[
\operatorname{ContextEmbedding}^{\mathsf M}(j\hookrightarrow k;e).
\]

Por tanto TR-M debe intentar individuar **local contextuality**, no “worldhood maximal”.

Sea \(C\) una candidatura pre-indexada. Una teoría \(\mathcal T\) propone:

\[
\boxed{
\operatorname{MemoContextCriterion}_{\mathcal T}^{\mathsf M}
(
C;\Xi_C
)
}
\]

con:

\[
\Xi_C
=
\left\langle
\widehat{\Lambda}_C,
\widehat{\mathbb I}_C,
\widehat{\mathbb P}_C,
\widehat{\mathsf{CP}}_C,
\partial_C
\right\rangle.
\]

Aquí:

- \(\widehat{\Lambda}_C\) es un esquema local de typing/operations definido sobre la candidatura, no sobre un índice ya admitido;
- \(\widehat{\mathbb I}_C\) fija las interfaces entre dinámica local y entorno;
- \(\widehat{\mathbb P}_C\) es una PersistenceSpec pre-indexada;
- \(\widehat{\mathsf{CP}}_C\) es el quotient dinámico candidato inducido por esa spec;
- \(\partial_C\) es el boundary/cut efectivo que media las dependencias relevantes entre local y externo.

La notación con sombrero importa: estas estructuras deben construirse sin usar \(\operatorname{Real}_i\), \(R_i\), SameRegime o la mera existencia del índice que pretenden justificar.

#### 0.11.91l. MC1–MC10: cuándo una máquina local puede descargar contextualidad

Para que MemoContextCriterion pueda alimentar \(\operatorname{Ind}_{\mathcal T}\), exigimos **MC1–MC10**.

**MC1 — pre-index independence.** \(\Xi_C\) se especifica sobre una candidatura \(C\) sin usar el índice, RegimeTotal, REC ni un ContextEmbedding futuro como premisa de su propia individuación.

**MC2 — local typing power.** \(\widehat{\Lambda}_C\) no es solo una etiqueta. Debe distinguir operaciones/estados localmente well-typed de inputs externos que requieren una regla de interfaz/traducción:

\[
\operatorname{LocalWF}_{\widehat\Lambda_C}
\neq
\text{WF global irrestricta}.
\]

Así se descarga una versión pre-indexada de CI3.

**MC3 — positive boundary.** \(\partial_C\) debe estar positivamente grounded por estructura causal, operacional, constitutiva, protocolar u organizacional de \(\mathcal T\). No basta “todo lo que decidimos llamar interior”.

**MC4 — interface mediation.** Toda dependencia externa que \(\mathcal T\) considere relevante para la dinámica local debe atravesar \(\widehat{\mathbb I}_C\) o un interaction contract declarado:

\[
\forall p\in
Path_{\mathcal T}
(
\mathrm{Ext}\leadsto\mathrm{Local}
):
\quad
p\cap\partial_C\neq\varnothing.
\]

Los hidden bypasses invalidan el boundary declarado o fuerzan a ampliarlo.

**MC5 — reentrant local state.** Existe un quotient de histories candidato cuya evolución bajo MaintStep es well-defined:

\[
\widehat E_C
\text{ es right-congruence bajo }
\widehat{\mathcal G}_C.
\]

No se exige memoria física no trivial: un sistema memoryless puede tener una única clase reentrante si el resto de guards es no trivial.

**MC6 — role/interaction coverage.** Todos los MaintRole independently grounded y sus SynRel relevantes están incluidos. No puede obtenerse contextualidad escogiendo solo las interfaces que hacen parecer autónomo al candidato.

**MC7 — counterfactual autonomy.** Fijado un estado local quotientado y una misma secuencia de inputs de interfaz, variar detalles host-side que \(\mathcal T\) declara externos/irrelevantes no cambia la evolución/observación local:

\[
\widehat q
+
\operatorname{InputTrace}_{\partial_C}
\Longrightarrow
\operatorname{LocalFuture}
\]

módulo la branching semantics admitida.

Esto no exige aislamiento causal absoluto; exige **screening-off por la frontera declarada**.

**MC8 — anti-arbitrary aggregation.** Si \(C=A\sqcup B\) se forma juntando dos máquinas contextuales sin boundary conjunto, interaction closure ni dinámica que las unifique, la suma no hereda contextualidad solo por empaquetado descriptivo.

**MC9 — level/rival-cut discipline.** Cortes anidados pueden ser simultáneamente válidos. Cortes incompatibles del mismo nivel requieren equivalencia, overlap semantics explícita o una razón theory-specific para privilegiar uno. Nesting no cuenta como rivalidad.

**MC10 — genesis/persistence discipline.** El criterio distingue que una máquina local preexista, sea constituida por ContextGenesis o cese. Su ContinuationProfile gobierna persistencia, pero no retrocrea la individuación inicial.

Definimos:

\[
\operatorname{MCAdequate}^{\mathsf M}
(
\mathcal T,C,\Xi_C
)
\]

como MC1–MC10 más los CI1–CI14/IA0–IA10 aplicables.

#### 0.11.91m. TM-T1 — descarga condicional de TR-M

Si:

\[
\operatorname{MemoContextCriterion}_{\mathcal T}^{\mathsf M}
(
C;\Xi_C
)
\]

y:

\[
\operatorname{MCAdequate}^{\mathsf M}
(
\mathcal T,C,\Xi_C
),
\]

entonces la estructura pre-indexada puede actuar como la reducción theory-specific exigida por §0.11.72:

\[
\boxed{
\operatorname{MemoContextCriterion}_{\mathcal T}(C;\Xi_C)
+
\operatorname{MCAdequate}(\mathcal T,C,\Xi_C)
\Rightarrow
\operatorname{Ind}_{\mathcal T}^{\mathsf M}(C;\chi_{\Xi})
}
\]

y, si la descarga general IndAdequate queda satisfecha:

\[
\boxed{
\operatorname{Ind}_{\mathcal T}^{\mathsf M}(C;\chi_{\Xi})
+
\operatorname{IndAdequate}^{\mathsf M}(\mathcal T,C,\chi_\Xi)
\Rightarrow
\operatorname{ContextIndividuation}^{\mathsf M}(C;\chi_\Xi).
}
\]

TR-M es así una realización legítima de TR, no la regla:

\[
\operatorname{MemoState}\Rightarrow\operatorname{ContextIndividuation}.
\]

La diferencia está precisamente en MC1–MC10.

#### 0.11.91n. TM-T2 — nesting theorem: subsystem no excluye contexto

Supóngase que el host \(H\) ya descarga:

\[
\operatorname{ContextIndividuation}^{\mathsf M}(H;\chi_H)
\Rightarrow
H\Downarrow k,
\]

y una candidatura local \(C\) realizada host-side descarga independientemente TR-M:

\[
\operatorname{ContextIndividuation}^{\mathsf M}(C;\chi_C)
\Rightarrow
C\Downarrow j.
\]

Si existe un witness host/local que satisface CE1–CE6, entonces:

\[
\boxed{
\operatorname{ContextEmbedding}^{\mathsf M}
(
j\hookrightarrow k;e
).
}
\]

De ello no se sigue:

\[
j\simeq_{\mathrm{idx}}k,
\]

ni:

\[
j\#k.
\]

Tampoco se escribe:

\[
R_j\in R_k.
\]

El host contiene una realización/presentación \(c_k\) del contexto \(j\), y \(e\) relaciona ambas estructuras metateóricamente.

Por tanto:

\[
\boxed{
\text{subsystem}(C,H)
\not\Rightarrow
\neg\text{context}(C).
}
\]

La doctrina pasa de **anti-proliferation** a **disciplined contextual abundance**.

#### 0.11.91o. Modelo TM-A — servicio KV como contexto software anidado

Sea una teoría software \(\mathcal T_{\mathrm{KV}}\) que toma como primitivas operacionales:

\[
Put,\;Get,\;Delete
\]

sobre un store persistente.

La candidatura \(C_{KV}\) posee:

- typing local de keys/values/requests;
- interfaz API explícita;
- estado snapshot/event-sourced suficiente;
- update reentrante;
- RoleAdequate para futuras requests;
- hidden-bypass discipline respecto de la semántica software declarada.

Entonces puede satisfacer MC1–MC10 y ser admitida como contexto:

\[
C_{KV}\Downarrow j.
\]

El proceso/VM/máquina que la aloja puede estar ya en otro contexto \(k\):

\[
j\hookrightarrow k.
\]

Un debugger que modifica memoria “por detrás” no refuta automáticamente el contexto software. Si \(\mathcal T_{\mathrm{KV}}\) excluye ese canal de su ontología operacional, es un hecho de otro nivel. Si la teoría pretende capturar además esa intervención como fundamental para la dinámica del servicio, MC4 obliga a ampliar la interfaz o retirar la descarga.

Así la contextualidad sigue siendo objetiva **respecto de una teoría estructuralmente fiel a su nivel**, no una ficción elegida por conveniencia.

#### 0.11.91p. Modelo TM-B — termostato como contexto físico/control anidado

Sea \(C_T\) un termostato con estado controlador \(m\), sensor input \(s(t)\), alimentación, outputs hacia actuador y una dinámica:

\[
m_{t+1}
=
U(m_t,s_t).
\]

Una teoría de control/física local puede fijar:

\[
\widehat{\Lambda}_T,
\quad
\widehat{\mathbb I}_T,
\quad
\widehat{\mathbb P}_T.
\]

Si toda influencia relevante para el comportamiento controlador entra mediante los canales declarados —sensor, alimentación, perturbaciones incluidas por el modelo— y la evolución interna factoriza por \(m\) + inputs, MC3–MC7 pueden descargarse.

Entonces no hay contradicción en:

\[
\boxed{
\text{termostato}
=
\text{objeto físico en }k
+
\text{contexto de control }j.
}
\]

Si radiación, manipulación mecánica o EMI cambian su estado por un canal omitido que la teoría considera relevante, falla MC4 hasta ampliar la membrana funcional.

#### 0.11.91q. Modelo TM-C — agregación arbitraria sigue fallando

Tómense un termostato \(T\) y un servicio KV \(D\) que no comparten:

- boundary conjunto;
- transition closure conjunta;
- interaction role constitutivo;
- local typing scheme que los trate como una única máquina.

Construir:

\[
C=T\sqcup D
\]

en una estructura de datos no satisface MC8.

Por tanto la nueva doctrina no implica:

\[
\boxed{
\text{cualquier subconjunto arbitrario}
\Rightarrow
\text{contexto}.
}
\]

Sí permite que \(T\), \(D\), el host que los contiene y quizá una unidad mayor que realmente los integre sean **todos contextos en niveles distintos** si cada uno descarga su criterio.

#### 0.11.91r. Consecuencias doctrinales de TR-M

TR-M obliga a separar definitivamente:

\[
\boxed{
\text{contexto}
\neq
\text{mundo maximal}
\neq
\text{objeto host-side}.
}
\]

Un contexto es una arena local independently individuated de typing/dynamics/interfaces. Puede estar embebido en otra arena.

Así, la “Cellular Reality” gana una lectura literal estructural:

\[
\boxed{
\text{contextos pueden contener realizaciones de otros contextos}
}
\]

sin convertir índices en objetos ni permitir import/export literal de tokens.

El guard correcto deja de ser:

\[
\text{“no demasiados contextos”.}
\]

Pasa a ser:

\[
\boxed{
\text{“ningún contexto sin criterio de individuación grounded,}
\;
\text{y ningún nesting sin embedding explícito”.}
}
\]

Esto también modifica cómo interpretar \(i\#j\): índices distintos no son por ello incompatibles. Embedding, SharedOntSpace, genealogía o coexistencia pueden bloquear esa inferencia. \(i\#j\) sigue reservado para ausencia de common ontological typing en el sentido fuerte ya definido.

La deuda TR-M queda por tanto **RESOLVED condicionalmente**: existe una ruta formal no circular mediante una máquina contextual pre-indexada y MC1–MC10; su éxito en cada dominio depende de una teoría \(\mathcal T\) que descargue structural fidelity e IndAdequate.

#### 0.11.91r-a. Rival cuts: la adecuación de individuación es también una obligación entre candidatos

IA8 y MC9 no pueden quedar como cautelas verbales. Una teoría puede satisfacer aparentemente todos los tests locales para una candidatura y, sin embargo, producir dos cortes incompatibles cuando se la aplica a la misma presentación pre-indexada.

Introducimos por ello un juicio **de auditoría**, no un hecho objeto:

\[
\operatorname{CutProposal}_{\mathcal T}^{\mathsf M}
(C\mid P;\kappa_C),
\]

donde \(P\) es una presentación común usada únicamente para comparar candidaturas antes de IndexAdmission y \(\kappa_C\) registra la estructura theory-specific que propone el corte. \(P\) no es un supercontexto ontológico ni \(\kappa_C\) una frontera ya admitida.

Dos propuestas son **rival cuts del mismo nivel** cuando:

\[
\boxed{
\operatorname{RivalCut}_{\mathcal T}^{\mathsf M}
(C,D\mid P)
}
\]

y se cumplen conjuntamente:

1. ambas son propuestas de \(\mathcal T\) sobre la misma presentación de auditoría \(P\);
2. sus clasificaciones interior/exterior o sus boundaries son incompatibles de forma no meramente notacional;
3. ninguna está ya justificada como un nivel local contenido en la otra;
4. no se trata simplemente de dos candidatos disjuntos que no compiten por el mismo soporte;
5. la diferencia no se explica por comparar etapas distintas de una ContextGenesis o de persistencia.

La condición 4 es esencial: **pluralidad no es rivalidad**. Dos contextos separados pueden ser ambos legítimos sin necesitar que uno derrote al otro. RivalCut se reserva para dos intentos incompatibles de responder a la misma pregunta de individuación al mismo nivel.

#### 0.11.91r-b. Resoluciones admisibles de un rival cut

Definimos un bundle metateórico de resolución:

\[
\operatorname{RivalResolution}_{\mathcal T}^{\mathsf M}
(C,D\mid P)
\]

si se descarga al menos una de las siguientes rutas con estructura independently grounded:

1. **RE / equivalencia de individuación:** los dos cuts son recodificaciones fieles o witnesses diferentes de la misma unidad objetiva:

\[
C\simeq_{\mathrm{ind}}^{\mathsf M}D.
\]

2. **RN / nesting:** ambos candidatos descargan individuación propia y existe una semántica pre-indexada de nivel/local realization que, tras admisión, puede satisfacer CE1–CE6 y producir ContextEmbedding. En este caso no son rivales del mismo nivel.

3. **RO / overlap semantics:** \(\mathcal T\) justifica explícitamente por qué dos unidades parcialmente solapadas pueden ser ontológicamente distintas sin que el solapamiento sea una selección arbitraria. La mera intersección extensional no cuenta como semántica de overlap.

4. **RG / genesis staging:** la aparente incompatibilidad proviene de comparar una unidad preexistente con una unidad constituida en una etapa posterior; ContextGenesis/ContinuationProfile decide la relación, no IA8 por sí sola.

5. **RP / priority or rejection:** \(\mathcal T\) contiene una razón target-independent para mostrar que uno de los cortes falla IA0–IA10/CI1–CI14.

No se incluye una opción “ambos valen porque son perspectivas útiles”. La utilidad descriptiva puede justificar dos coarse-grainings, pero no dos ContextIndividuation objetivas sin una de las rutas anteriores.

Definimos entonces adecuación conjunta:

\[
\boxed{
\begin{aligned}
\operatorname{PairIndAdequate}_{\mathcal T}^{\mathsf M}
(C,D\mid P;\chi_C,\chi_D)
:\Longleftrightarrow\;&
\operatorname{IndAdequate}^{\mathsf M}(\mathcal T,C,\chi_C)\\
&\land
\operatorname{IndAdequate}^{\mathsf M}(\mathcal T,D,\chi_D)\\
&\land
\bigl(
\operatorname{RivalCut}_{\mathcal T}(C,D\mid P)
\Rightarrow
\operatorname{RivalResolution}_{\mathcal T}(C,D\mid P)
\bigr).
\end{aligned}
}
\]

La definición no vuelve relativa la individuación: formaliza que IA8 es **global respecto de las alternativas que la misma teoría es capaz de generar**, no un check aislado por candidato.

#### 0.11.91r-c. RC-T1 — unresolved rival-cut theorem

De la definición anterior:

\[
\operatorname{RivalCut}_{\mathcal T}(C,D\mid P)
\land
\neg
\operatorname{RivalResolution}_{\mathcal T}(C,D\mid P)
\]

implica:

\[
\boxed{
\neg
\operatorname{PairIndAdequate}_{\mathcal T}
(C,D\mid P;\chi_C,\chi_D).
}
\]

Por tanto dos cuts incompatibles del mismo nivel **no pueden autorizar conjuntamente dos IndexAdmission** mediante el mismo paquete de adecuación mientras la rivalidad permanezca sin resolver.

Esto no demuestra:

\[
\neg\operatorname{ContextIndividuation}(C)
\quad\text{o}\quad
\neg\operatorname{ContextIndividuation}(D).
\]

La conclusión es epistemológico-metateórica y más estricta: la teoría \(\mathcal T\) todavía **no ha descargado de forma suficiente** la individuación conjunta. Puede faltar estructura, uno de los witnesses puede ser erróneo o puede existir una semántica de nesting/overlap todavía no formulada.

RC-T1 evita convertir underdetermination en pluralidad ontológica por decreto.

#### 0.11.91r-d. No-Free-Promotion: el target es el witness, no prohibir contextos abundantes

El guard de Cellular Reality no debe formularse como:

\[
\text{“pocos contextos”.}
\]

Eso sería incompatible con TM-T2 y con la posibilidad real de nested contexts.

Definimos en cambio una propiedad del **soporte de promoción**:

\[
\operatorname{PackagingOnly}_{\mathcal T}^{\mathsf M}
(C;\chi)
\]

cuando \(\chi\) obtiene el candidato únicamente a partir de una o varias de estas operaciones:

- enumerar un conjunto de componentes;
- introducir una etiqueta o nombre común;
- encerrarlos en un contenedor o región descriptiva;
- seleccionar una coordenada, mitad geométrica o predicado construido desde el target;
- tomar la unión de unidades ya individuadas;
- exigir solo ausencia de interacción visible con el exterior;

y no aporta ninguna estructura positiva theory-specific que descargue IA3/IA5/IA6 o, para TR-M, MC2–MC8.

**NFP-T1 — no promotion from packaging.**

\[
\boxed{
\operatorname{PackagingOnly}_{\mathcal T}(C;\chi)
\Rightarrow
\neg
\operatorname{IndAdequate}^{\mathsf M}
(\mathcal T,C,\chi).
}
\]

La conclusión es deliberadamente **witness-relative**. No se infiere que \(C\) no pueda ser un contexto. Se infiere que **ese modo de seleccionarlo** no basta. Otra estructura independiente \(\chi'\) podría descargar legítimamente la misma unidad:

\[
\operatorname{PackagingOnly}(C;\chi)
\land
\operatorname{IndAdequate}(C;\chi')
\]

es consistente.

Este punto impide que No-Free-Promotion se convierta en un principio conservador anti-emergencia.

#### 0.11.91r-e. NFP-T2 — la unión de contextos no hereda contextualidad

Sean dos candidaturas \(A,B\) que descargan independientemente ContextIndividuation. Formemos la presentación conjunta:

\[
U=A\sqcup B.
\]

Introducimos solo como nombre de auditoría:

\[
\operatorname{JointUnitGround}_{\mathcal T}^{\mathsf M}
(A,B\Rightarrow U;\zeta)
\]

para cualquier estructura positiva independiente que explique por qué la pluralidad constituye además **una unidad**: por ejemplo una world-making structure conjunta, interaction closure constitutiva, dinámica reentrante conjunta o GenuineContextGenesis. El núcleo no identifica universalmente cuál de ellas debe existir.

Si no existe un ground de ese tipo y el único apoyo de \(U\) es la unión descriptiva:

\[
\neg\exists\zeta\;
\operatorname{JointUnitGround}_{\mathcal T}(A,B\Rightarrow U;\zeta),
\]

entonces no vale:

\[
\operatorname{ContextIndividuation}(A)
+
\operatorname{ContextIndividuation}(B)
\Rightarrow
\operatorname{ContextIndividuation}(U).
\]

Más precisamente, el witness heredado por mera unión cae bajo NFP-T1/IA6/MC8:

\[
\boxed{
\operatorname{Ind}(A)
\land
\operatorname{Ind}(B)
\land
\neg\operatorname{JointUnitGround}(A,B\Rightarrow U)
\not\Rightarrow
\operatorname{Ind}(U).
}
\]

Esto no prohíbe contextos de orden superior. Dice exactamente qué les falta: **una razón positiva de unidad adicional a la contextualidad de sus partes**.

#### 0.11.91r-f. NFP-T3 — un subcut descriptivo tampoco hereda contextualidad

Sea \(H\) una candidatura ya individuada y sea:

\[
C_P
=
\{x\in H\mid P(x)\},
\]

donde \(P\) es un predicado seleccionado porque produce el subgrupo que queremos tratar como contexto.

Si:

1. \(P\) no está independently grounded por \(\mathcal T\);
2. no induce typing local adicional;
3. no existe boundary/interface mediation positiva;
4. no existe dinámica/persistencia local que haga trabajo de screening-off;
5. recodificaciones fieles pueden cambiar \(P\) sin cambiar la estructura ontológica,

entonces el witness basado en \(P\) falla IA1–IA4 y, en TR-M, MC2–MC7:

\[
\boxed{
\operatorname{TargetSelectedSubcut}_{\mathcal T}(C_P;P)
\Rightarrow
\neg
\operatorname{IndAdequate}^{\mathsf M}
(\mathcal T,C_P,\chi_P).
}
\]

De nuevo, esto no demuestra que ninguna mitad espacial, módulo o subestructura pueda ser contexto. Si una teoría independiente aporta una frontera bona fide, una interfaz, closure o world-making structure para exactamente esa región, aparece otro witness y el resultado puede cambiar.

#### 0.11.91r-g. NFP-T4 — contextual abundance theorem

No-Free-Promotion tiene una conversa importante **que no debe añadirse**:

\[
\neg\operatorname{PackagingOnly}(C)
\not\Rightarrow
\operatorname{ContextIndividuation}(C).
\]

Evitar arbitrariedad es necesario para la descarga, no suficiente.

Pero TM-T2 sí permite demostrar la compatibilidad estructural de abundancia:

\[
\boxed{
\begin{aligned}
&
\operatorname{ContextIndividuation}^{\mathsf M}(C)
\land
\operatorname{ContextIndividuation}^{\mathsf M}(H)\\
&
\land
\mathrm{CE1\text{-}CE6}(C,H;e)
\\
&\Rightarrow
\text{tras IndexAdmission, TM-T2 puede descargar ContextEmbedding.}
\end{aligned}
}
\]

Por tanto:

\[
\boxed{
\text{No-Free-Promotion}
\neq
\text{No-Context-Proliferation}.
}
\]

Puede haber muchos niveles reales de individuación. Lo que no puede haber es una **promoción inferencial gratuita** desde membership, packaging, geometría o conveniencia descriptiva hasta ContextIndividuation.

#### 0.11.91r-h. RC-X — particiones cruzadas bajo simetría

Construyamos un stress test mínimo sobre cuatro módulos pre-indexados:

\[
a,b,c,d.
\]

Una teoría \(\mathcal T_S\) ve exactamente la misma estructura local en los cuatro y admite un automorfismo:

\[
\pi:
b\leftrightarrow c
\]

que preserva todos sus predicados y relaciones independently grounded.

Considérense dos particiones:

\[
\Pi_1
=
\{\{a,b\},\{c,d\}\},
\]

y:

\[
\Pi_2
=
\{\{a,c\},\{b,d\}\}.
\]

Supóngase que los únicos witnesses de “unidad” son precisamente las etiquetas de bloque elegidas en \(\Pi_1\) o \(\Pi_2\). No existe boundary, world-maker, interaction closure, génesis o dinámica adicional que seleccione una partición.

Entonces:

- privilegiar \(\Pi_1\) frente a \(\Pi_2\) viola IA1/IA2/IA4;
- admitir ambas como dos sistemas de contextos rivales del mismo nivel viola IA8 mientras no exista RivalResolution;
- describirlas como dos coarse-grainings útiles es compatible con la teoría, pero no descarga dos ontologías contextuales.

Por tanto el caso queda:

\[
\boxed{
\operatorname{RivalCut}_{\mathcal T_S}(\Pi_1,\Pi_2)
\land
\neg\operatorname{RivalResolution}
\Rightarrow
\neg\operatorname{PairIndAdequate}
(\Pi_1,\Pi_2\mid P;\chi_1,\chi_2).
}
\]

RC-X es el adversario formal de “cualquier partición puede ser una realidad”.

#### 0.11.91r-i. Batería adversarial de No-Free-Promotion

**NFP-X1 — caja con piedras.** Una caja proporciona una frontera espacial descriptivamente precisa, pero si \(\mathcal T\) no atribuye a esa frontera typing local, mediation, closure o dinámica unificadora, el witness “están dentro de la misma caja” es PackagingOnly. No se descarga contexto.

**NFP-X2 — mitad izquierda de un ordenador.** El predicado geométrico “\(x\) está a la izquierda del plano \(p\)” corta arbitrariamente buses, memoria, procesos y relaciones que la propia teoría computacional considera co-funcionales. Falla IA3/IA5 y normalmente MC4/MC6/MC7. No se sigue que ninguna región física pueda ser contexto; falla ese cut.

**NFP-X3 — RAM + silla.** La unión tiene una descripción extensional exacta pero ninguna razón positiva de unidad. Falla NFP-T2.

**NFP-P1 — ordenador funcional.** Bajo una teoría que justifique typing de instrucciones/estado, buses/interfaces, dinámica reentrante, roles completos y boundary mediation, el ordenador completo puede descargar TR-M. Su éxito no proviene de “ser una caja”.

**NFP-P2 — CPU dentro del ordenador.** Una CPU puede descargar un contexto local propio si su ISA/estado/interfaces/dinámica satisfacen independientemente MC1–MC10. Si además CE1–CE6 relacionan su realización con el host, CPU y ordenador son contextos nested, no rival cuts.

**NFP-P3 — dos servicios coordinados.** Dos microservicios independientes no constituyen automáticamente un tercer contexto por compartir datacenter. Si un protocolo constitutivo, estado conjunto, interaction role no separable o dinámica reentrante de orden superior proporciona JointUnitGround, la composición puede convertirse en un contexto adicional. Sin ese ground permanecen dos unidades relacionadas.

**NFP-P4 — célula biológica.** La membrana física por sí sola no basta. Una teoría biológica puede, sin embargo, aportar closure organizacional, regulación, interfaces metabólicas, persistencia y counterfactual autonomy suficientes para una descarga theory-specific. La conclusión correcta es “candidata fuerte bajo una teoría adecuada”, no “toda cosa con membrana es \(R_i\)”.

Esta batería demuestra que el criterio no selecciona una **escala privilegiada**. Selecciona una clase de **justificaciones de unidad**.

#### 0.11.91r-j. Resultado doctrinal: unidad, escala y dimensión se desacoplan

Con RC-T1 y NFP-T1–T4, la lectura fuerte de Cellular Reality puede formularse sin maximalismo ni perspectivismo:

\[
\boxed{
R_i
\text{ no significa una escala de realidad;}
\quad
R_i
\text{ exige una unidad de individuación ontológicamente admisible.}
}
\]

De aquí no se sigue que toda cosa individuada tenga RegimeTotal: R-FORM mantiene separada la formación del scope de su totalización genealógica.

Tampoco se sigue que dos niveles admisibles deban competir. Si una célula, un organismo, un ordenador, una CPU o un proceso descargan criterios independientes y sus relaciones de nivel están justificadas, la teoría admite **disciplined contextual abundance**.

El avance concreto sobre IA8/MC9 es:

\[
\boxed{
\text{local adequacy}
+
\text{rival-cut closure}
\Rightarrow
\text{admissible individuation audit}.
}
\]

REV-07g permanece PARTIAL globalmente porque ninguna teoría universal decide todos los casos de individuación. Pero **No-Free-Promotion y rival-cut discipline quedan ahora cerrados a nivel de criterio**: sabemos qué inferencias están prohibidas, qué tipos de resolución permiten coexistencia y qué clase de estructura adicional debe aportar una teoría concreta.

#### 0.11.91r-k. Protocolo de robustez cross-domain

No-Free-Promotion solo es interesante si el mismo contrato distingue candidaturas en dominios donde las fuentes de unidad son radicalmente distintas. Para evitar adaptar retrospectivamente los guards a cada ejemplo, fijamos antes de mirar los casos el siguiente protocolo:

\[
\boxed{
\operatorname{DomainAudit}_{\mathcal T}^{\mathsf M}
(C;\Xi,\chi)
}
\]

requiere, sin alterar IA0–IA10 ni MC1–MC10:

1. una reducción theory-specific explícita de \(\operatorname{Criterion}_{\mathcal T}(C)\);
2. un witness pre-indexado \(\Xi\) que no use el resultado deseado;
3. descarga positiva de boundary/typing/dynamics y no solo ausencia de exterior;
4. tratamiento de todos los bypasses que la propia \(\mathcal T\) considere relevantes;
5. un rival cut negativo construido dentro del mismo dominio;
6. una candidatura nested o de orden superior que muestre que el test no es anti-proliferation;
7. separación entre **evidence of a boundary** y **ground of contextual unity**;
8. ausencia de cualquier inferencia directa hacia RegimeTotal.

El protocolo tiene una regla adicional de disciplina de nivel que no añade un axioma nuevo, sino que explicita conjuntamente IA0, IA1, MC4 y MC7:

**DL1 / no level escape.** Una teoría efectiva no puede salvar un cut declarando simplemente “fuera de nivel” un mecanismo que altera las transiciones, observables o persistencia que su propio criterio usa para individuar \(C\). O el mecanismo se incorpora como input/interface/interaction relevante, o la descarga falla.

Por tanto:

\[
\boxed{
\text{abstracción legítima}
\neq
\text{omisión conveniente}.
}
\]

Una microdiferencia puede quedar quotientada si, fijados el estado local y los inputs declarados, no cambia el futuro relevante. Si sí lo cambia, MC7 impide esconderla bajo coarse-graining.

#### 0.11.91r-l. SW-A — software: servicio KV realizado frente a API puramente nominal

Tomemos \(\mathcal T_{\mathrm{SW}}\) como una teoría operacional de un servicio realmente ejecutado. No basta el documento de API. La candidatura positiva \(C_{\mathrm{KV}}\) debe poseer en la realización:

\[
\Xi_{\mathrm{KV}}
=
\langle
\widehat\Lambda_{\mathrm{req/state}},
\widehat{\mathbb I}_{\mathrm{API+host}},
\widehat{\mathbb P}_{\mathrm{service}},
\widehat{\mathsf{CP}}_{\mathrm{KV}},
\partial_{\mathrm{proc}}
\rangle.
\]

La descarga usa exactamente MC1–MC10:

- **MC1:** el proceso/store se especifica antes de admitir índice;
- **MC2:** requests, keys, values, estado y errores poseen typing operacional local;
- **MC3:** process isolation, address-space/state ownership y protocolo proporcionan estructura positiva; una etiqueta de microservicio no basta;
- **MC4:** requests, almacenamiento, clock/IO y host interventions que \(\mathcal T_{\mathrm{SW}}\) considere semánticamente eficaces deben aparecer como interfaces o interaction channels;
- **MC5:** snapshot/event-state suficiente factoriza la continuación;
- **MC6:** background tasks, retries, timers, replication y demás roles relevantes no pueden omitirse para fabricar autonomía;
- **MC7:** fijados estado e input trace, variaciones host-side declaradas irrelevantes no alteran la continuación operacional;
- **MC8:** dos procesos puestos bajo un mismo deployment label no se vuelven una unidad;
- **MC9:** proceso, VM y host pueden ser nested si cada uno descarga su criterio;
- **MC10:** restart, migration y replacement se tratan con ContinuationProfile, no por identidad material.

El **rival cut negativo** es:

\[
C_{\mathrm{odd}}
=
\text{mitad de las keys}
+
\text{la mitad de un worker}
\]

seleccionado por una regla construida después de observar la implementación. Aunque sea enumerable con precisión, corta roles y state transitions sin boundary mediation propia. Falla IA1/IA3/IA5 y MC3/MC4/MC6.

El ataque importante es el debugger/host bypass. Si un debugger puede cambiar memoria de modo que altera la transición del servicio:

\[
m_t
\leadsto
m'_t
\]

sin pasar por ninguna entrada reconocida por \(\widehat{\mathbb I}\), solo hay dos opciones admisibles:

1. \(\mathcal T_{\mathrm{SW}}\) considera esa intervención posible y relevante: entonces MC4 obliga a modelarla como host-intervention channel;
2. pretende ignorarla mientras sigue usando transiciones que la intervención puede alterar: entonces DL1/MC7 hacen fallar la descarga.

No se permite responder “el debugger no cuenta” únicamente porque estorba al cut.

**Resultado SW-R.** Un servicio software puede ser un candidato fuerte de contexto **cuando su unidad está realizada operacionalmente** y la abstracción satisface screening-off. Una especificación/API por sí sola es evidence insuficiente:

\[
\boxed{
\operatorname{APISpec}(C)
\not\Rightarrow
\operatorname{ContextIndividuation}(C).
}
\]

Esto separa artefacto descriptivo de máquina contextual realizada.

#### 0.11.91r-m. BIO-A — célula: boundary material + organización mantenida

Sea \(\mathcal T_{\mathrm{BIO}}\) una teoría biológica de organización celular que toma en serio, al menos, regulación, metabolismo, transporte, reparación/reproducción de componentes relevantes y persistencia organizacional.

La candidatura \(C_{\mathrm{cell}}\) no se individúa por la membrana desnuda. Su witness usa conjuntamente:

\[
\Xi_{\mathrm{cell}}
=
\langle
\widehat\Lambda_{\mathrm{bio}},
\widehat{\mathbb I}_{\mathrm{transport/signaling}},
\widehat{\mathbb P}_{\mathrm{org}},
\widehat{\mathsf{CP}}_{\mathrm{org}},
\partial_{\mathrm{cell}}
\rangle.
\]

El grounding positivo puede incluir una teoría independently justified de closure organizacional/autopoiesis, pero Exergism no identifica sin argumento su propia RegimeClosure con biological closure of constraints.

Aplicando el mismo contrato:

- **MC2:** la teoría distingue estados/procesos internos y entradas ambientales relevantes;
- **MC3:** la membrana y la organización que la produce/mantiene aportan un boundary positivo; la superficie sola no basta;
- **MC4:** nutrientes, señales, intercambio iónico, fuerzas, calor u otros canales que la teoría considere relevantes deben estar mediados/modelados;
- **MC5:** existe una dinámica reentrante a nivel organizacional aunque cambien continuamente moléculas concretas;
- **MC6:** pathways o constraints críticos no pueden eliminarse para que aparezca artificialmente closure;
- **MC7:** variación ambiental no transmitida por los canales/variables relevantes debe quedar screened-off respecto de la continuación organizacional;
- **MC8:** célula + molécula cercana no heredan unidad por proximidad;
- **MC9:** organelo, célula y organismo pueden ser candidaturas nested si cada una posee grounding independiente;
- **MC10:** división, muerte y diferenciación requieren semántica de genesis/persistence/cessation, no snapshots.

El **rival cut negativo** es la mitad geométrica de una célula:

\[
C_{\frac12}
=
\{x\in C_{\mathrm{cell}}:
x\text{ está a un lado de un plano }p\}.
\]

Salvo que una estructura biológica independiente coincida con ese cut, secciona transporte, regulación y organización sin boundary propio. NFP-T3 lo rechaza como witness.

El caso positivo nested puede ser un organelo solo si \(\mathcal T_{\mathrm{BIO}}\) demuestra más que membership espacial: boundary/interface propio, dinámica local, roles suficientes y una relación CE1–CE6 con la célula. No se adopta:

\[
\text{organelo}
\Rightarrow
\text{contexto}.
\]

**Resultado BIO-R.** La célula proporciona un test especialmente fuerte porque material boundary, organization y persistence pueden converger sobre la misma candidatura sin ser idénticos entre sí:

\[
\boxed{
\text{material boundary}
+
\text{organizational unity}
+
\text{mediated openness}
}
\]

es compatible con ContextIndividuation sin exigir aislamiento. Esto apoya la lectura celular de la arquitectura, pero no la demuestra universalmente.

#### 0.11.91r-n. PHY-A — termostato/control: el diagrama de bloques no es todavía ontología física

Sea \(\mathcal T_{\mathrm{CTRL}}\) una teoría de control realizada físicamente con controlador \(m\), sensor, alimentación y actuador:

\[
m_{t+1}
=
U(m_t,s_t,u_t).
\]

El modelo TM-B mostraba que esta estructura puede satisfacer MC3–MC7. La auditoría cross-domain introduce ahora un adversario más duro: un **block diagram** diseñado por el ingeniero puede coincidir con una dinámica útil sin que su boundary funcional sea por ello una frontera ontológica autónoma.

Por tanto distinguimos:

\[
\operatorname{ControlDecomposition}(C;\partial)
\]

de:

\[
\operatorname{GroundedControlUnit}_{\mathcal T_{\mathrm{CTRL}}}(C;\Xi).
\]

El segundo exige que el boundary funcional esté realizado por estructura causal/operacional efectiva:

- sensor/actuator channels y power/perturbation paths identificados;
- estado controlador reentrante;
- factorization del futuro por state + input trace;
- ausencia de bypass relevante no modelado;
- persistence/role closure suficiente.

Un dibujo del sistema no satisface estas condiciones por sí mismo.

El rival cut negativo puede ser:

\[
C_{\mathrm{board-left}}
\]

la mitad izquierda de la PCB. Si corta feedback, alimentación y state propagation sin interface propia, falla el mismo contrato que en software y biología.

El test de orden superior es más interesante. Considérese:

\[
C_T
=
\text{thermostat}
\]

y:

\[
C_{TR}
=
\text{thermostat + room + heater}.
\]

El segundo **no** hereda contextualidad de \(C_T\). Puede, sin embargo, descargar una nueva unidad si la teoría demuestra closed-loop dynamics relevante:

\[
T
\rightarrow
Heater
\rightarrow
Room
\rightarrow
Sensor
\rightarrow
T
\]

con estado conjunto, interaction closure y boundary mediating la relación con el exterior. Éste es precisamente un posible:

\[
\operatorname{JointUnitGround}
(T,Room,Heater\Rightarrow C_{TR};\zeta).
\]

Por tanto NFP-T2 no impide sistemas de control de orden superior; exige que su unidad esté en la dinámica conjunta, no en la llave dibujada alrededor.

**Resultado PHY-R.** \(\mathcal T_{\mathrm{CTRL}}\) puede descargar una **unidad contextual de control** si el diagrama factoriza una organización causal real y pasa DL1. No se obtiene gratuitamente una afirmación de “fundamental physical worldhood”:

\[
\boxed{
\text{control-context witness}
\not\Rightarrow
\text{maximal/fundamental physical context}.
}
\]

Esto es compatible con TR: ContextIndividuation no exige maximalidad y un contexto puede estar realizado dentro de otro nivel físico.

#### 0.11.91r-o. DR-T1 — resultado de portabilidad de criterio, no de identidad de mecanismo

Los tres dominios no comparten un único world-maker:

\[
W_{\mathrm{software}}
\neq
W_{\mathrm{biology}}
\neq
W_{\mathrm{control}}.
\]

Tampoco comparten una única clase material de boundary. Lo que permanece invariante es la **forma de la carga de prueba**:

\[
\boxed{
\begin{array}{c}
\text{positive grounded unity}\\
+\text{local typing / admissible operations}\\
+\text{interface-mediated openness}\\
+\text{reentrant dynamics / persistence}\\
+\text{counterfactual screening}\\
+\text{anti-aggregation}\\
+\text{rival-cut closure}
\end{array}
}
\]

Cada dominio realiza estas obligaciones mediante recursos distintos.

Definimos:

\[
\operatorname{CriterionPortable}^{\mathsf M}
(D_1,D_2,D_3)
\]

cuando una misma lista de obligaciones puede auditar candidaturas en los tres dominios sin:

1. añadir una excepción domain-specific a IA0–IA10/MC1–MC10;
2. retirar un counterexample solo porque falla un dominio favorito;
3. identificar los mecanismos concretos de grounding entre dominios.

Para SW-A, BIO-A y PHY-A la auditoría anterior proporciona un witness de **portabilidad de criterio** en este sentido limitado:

\[
\boxed{
\operatorname{CriterionPortable}^{\mathsf M}
(\mathrm{SW},\mathrm{BIO},\mathrm{CTRL}).
}
\]

Esto **no** demuestra:

\[
\forall \mathcal T\;\exists C\;
\operatorname{ContextIndividuation}(C),
\]

ni demuestra que los tres candidatos positivos sean efectivamente contextos del mundo actual sin las premisas empíricas/ontológicas de sus respectivas teorías.

El resultado es metodológico-formal: el contrato no necesita convertirse en “biología disfrazada”, “teoría de software disfrazada” o “control theory disfrazada” para distinguir promoción gratuita de individuación plausible.

#### 0.11.91r-p. Asimetría empírica entre dominios

La portabilidad no implica igual fuerza evidencial.

- **Software:** la unidad puede estar fuertemente realizada operacionalmente, pero hay que vigilar que specification/design intent no sustituya causal realization.
- **Biología:** material boundary, self-maintaining organization y persistence ofrecen varias fuentes parcialmente independientes de grounding; el caso puede ser más robusto, pero sigue dependiendo de una teoría biológica concreta.
- **Control:** la factorización funcional es especialmente susceptible a cortes diseñados por el modelador; DL1 y MC7 son aquí decisivos para distinguir un closed-loop real de un mero block diagram.

Por tanto no adoptamos un ranking ontológico entre dominios. Registramos únicamente que los **failure modes son distintos** y que el mismo contrato los detecta.

La consecuencia para Cellular Reality es:

\[
\boxed{
\text{substrate-independence candidate}
=
\text{portable individuation obligations},
}
\]

no:

\[
\text{todos los substratos realizan las mismas fronteras o mecanismos}.
\]

Éste es el punto relevante para un futuro paper: la tesis no necesita que una célula, una CPU y un controlador “sean la misma clase de cosa”. Necesita que **ser contexto** sea una propiedad estructural descargable por mecanismos distintos sin cambiar el criterio de admisibilidad.

#### 0.11.91r-q. Evidencia externa no es todavía ContextIndividuation

La ronda anterior demostró portabilidad del **criterio** entre dominios. El siguiente paso es más exigente: sustituir los toys por sistemas concretos documentados externamente.

Para no convertir documentación técnica o literatura empírica en metafísica por decreto, introducimos solo un juicio de auditoría:

\[
\operatorname{EmpiricalSupport}^{\mathsf M}
(E,C;Q),
\]

leído: el conjunto de fuentes/evidencias \(E\) respalda de forma independiente la proposición estructural \(Q\) sobre la candidatura \(C\).

No se adopta:

\[
\boxed{
\operatorname{EmpiricalSupport}(E,C;Q)
\not\Rightarrow
\operatorname{ContextIndividuation}^{\mathsf M}(C).
}
\]

La evidencia puede descargar premisas concretas de IA/MC, pero sigue haciendo falta demostrar que el mapping:

\[
Q_1,\dots,Q_n
\Longrightarrow
\mathrm{IA/MC\ obligations}
\]

es adecuado y que no quedan bypasses o rival cuts relevantes omitidos.

Distinguimos tres clases de evidencia sin imponer un ranking ontológico universal:

1. **implementation/documentation evidence:** especificaciones, código fuente y documentación oficial muestran la arquitectura efectivamente implementada;
2. **mechanism evidence:** literatura experimental/biológica o documentación funcional establece mecanismos causalmente eficaces;
3. **token/run evidence:** observación de una instancia concreta ejecutándose/funcionando.

Una arquitectura documentada puede ser real como artefacto sin que esta auditoría haya observado un token particular; un mecanismo biológico puede estar experimentalmente bien establecido sin que se haya seguido una célula concreta de principio a fin. Ninguno de esos huecos debe ocultarse bajo IA0.

#### 0.11.91r-r. EMP-SW-REDIS — Redis Open Source como candidatura software concreta

Tomamos ahora un sistema software específico: **Redis Open Source server**.

Fuentes externas verificables:

- la documentación oficial define una interacción client/server por comandos: el cliente envía una orden y el servidor procesa y devuelve una respuesta;
- RESP es el wire protocol de Redis y el servidor expone un vocabulario explícito de comandos/capacidades;
- Redis implementa un event loop propio basado en polling del sistema operativo y timers;
- Redis puede reconstruir su dataset tras restart mediante RDB y/o AOF; AOF registra write operations y las replayea para reconstruir estado.

Fuentes:
- https://redis.io/docs/latest/develop/using-commands/
- https://redis.io/docs/latest/develop/reference/
- https://redis.io/docs/latest/operate/oss_and_stack/reference/internals/internals-rediseventlib/
- https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/

Mapeo conservador:

\[
\begin{array}{lll}
\mathrm{MC2} & \text{fuerte} &
\text{commands/arguments/replies proporcionan typing operacional explícito};\\
\mathrm{MC3} & \text{parcial-fuerte} &
\text{server state + protocol endpoints son estructura positiva, no mera etiqueta};\\
\mathrm{MC4} & \text{fuerte para el nivel declarado} &
\text{socket I/O/timers/persistence aparecen como canales efectivos};\\
\mathrm{MC5} & \text{fuerte} &
\text{dataset + event loop + persistence soportan continuidad/reentrada};\\
\mathrm{MC6} & \text{parcial} &
\text{background persistence, timers y client roles están documentados, no todos los host effects};\\
\mathrm{MC7} & \text{parcial} &
\text{la documentación no demuestra por sí sola screening-off frente a todo host-side intervention};\\
\mathrm{MC8} & \text{fuerte} &
\text{un deployment label o unión con otro proceso no aparece como fuente de unidad};\\
\mathrm{MC10} & \text{parcial-fuerte} &
\text{restart/reconstruction están documentados, pero identidad ontológica no se sigue de persistence}.
\end{array}
\]

La objeción debugger/host del stress test anterior permanece real. La existencia de una event loop y un protocolo no demuestra que cualquier modificación de memoria, señal OS o fallo de hardware sea irrelevant. DL1 exige que, si la teoría software pretende incluir esos mecanismos en el mismo nivel causal, se modelen como inputs/interventions.

**Resultado REDIS-R.** Redis es una candidatura software **externamente respaldada a nivel de implementación** para TR-M. Pero estas fuentes no constituyen token/run evidence de una instancia particular ni descargan por sí solas IA0:

\[
\boxed{
\operatorname{RedisImplementationEvidence}
\Rightarrow
\text{strong TR-M candidate}
\not\Rightarrow
\operatorname{ContextIndividuation}.
}
\]

#### 0.11.91r-s. EMP-BIO-ECOLI — E. coli como candidatura biológica concreta

Tomamos **Escherichia coli**, no “una célula” abstracta.

La literatura revisada establece al menos:

1. la envoltura de bacterias Gram-negativas define una frontera con el ambiente y participa en uptake selectivo, respiración y secreción;
2. existen envelope-stress responses que detectan daño/defectos de ensamblaje y regulan reparación/remodelado para sostener supervivencia;
3. E. coli dispone de transporte activo/regulado de nutrientes a través de membrana, incluido uptake dependiente de disponibilidad ambiental;
4. la división se ejecuta mediante un divisome trans-envelope; el proceso coordina FtsZ, síntesis/remodelado de peptidoglicano, invaginación de envelope y scission en dos células hijas.

Fuentes:
- A. Konovalova, “Homeostasis of the Gram-Negative Cell Envelope” (2021), PMC8577651: https://pmc.ncbi.nlm.nih.gov/articles/PMC8577651/
- “Regulation Systems of Bacteria such as Escherichia coli in Response to Nutrient Limitation and Environmental Stresses”, PMC4018673: https://pmc.ncbi.nlm.nih.gov/articles/PMC4018673/
- “Localization, Assembly, and Activation of the Escherichia coli Cell Division Machinery”, PMC8919703: https://pmc.ncbi.nlm.nih.gov/articles/PMC8919703/

Mapeo:

\[
\begin{array}{lll}
\mathrm{MC2} & \text{fuerte a nivel biológico} &
\text{la teoría distingue procesos/estados internos y señales/transportes};\\
\mathrm{MC3} & \text{fuerte} &
\text{envelope + homeostasis proporcionan boundary positivo y mantenido};\\
\mathrm{MC4} & \text{fuerte pero no exhaustivo} &
\text{transport/signaling/respiration muestran apertura mediada};\\
\mathrm{MC5} & \text{fuerte-candidata} &
\text{regulación/homeostasis soportan dinámica organizacional reentrante};\\
\mathrm{MC6} & \text{parcial} &
\text{ningún pequeño corpus bibliográfico demuestra cobertura causal completa};\\
\mathrm{MC7} & \text{parcial} &
\text{la robustez/homeostasis apoya screening, no demuestra autonomía contrafactual total};\\
\mathrm{MC8} & \text{fuerte} &
\text{proximidad o inclusión espacial de moléculas externas no genera unidad};\\
\mathrm{MC10} & \text{fuerte para genesis, parcial para persistence} &
\text{divisome/scission documentan división; identidad diacrónica sigue siendo teoría adicional}.
\end{array}
\]

El rival cut “media célula geométrica” queda especialmente mal parado: la literatura atribuye las funciones de boundary, transport, stress response y division a una arquitectura distribuida que ese plano corta arbitrariamente.

**Resultado ECOLI-R.** E. coli es el caso de los tres con evidencia causal/experimental más directamente alineada con unidad mantenida y apertura mediada. Aun así, no convertimos esa robustez en una prueba de ContextIndividuation porque MC6/MC7 y el bridge IA0 siguen siendo obligaciones:

\[
\boxed{
\operatorname{EColiMechanismEvidence}
\Rightarrow
\text{strong evidence-backed candidate}
\not\Rightarrow
\operatorname{ContextIndividuation}.
}
\]

#### 0.11.91r-t. EMP-PHY-NEST — Nest Thermostat + Heat Link como lazo físico concreto

Tomamos un sistema físico/control comercial y documentado: **Google Nest Thermostat en configuración europea con Heat Link**.

La documentación oficial establece:

- el termostato detecta temperatura ambiente y puede usar sensores externos;
- cuando un Nest Temperature Sensor está activo, su lectura se usa para decidir cuándo encender/apagar el sistema;
- el termostato mantiene la temperatura programada enviando una señal al Heat Link;
- el Heat Link es el dispositivo que ordena al sistema de calefacción encenderse/apagarse;
- schedules y selección de sensor cambian qué input de temperatura controla el lazo.

Fuentes:
- https://support.google.com/googlehome/answer/9248154
- https://support.google.com/googlenest/answer/9256498
- https://support.google.com/googlehome/answer/10184481

Mapeo:

\[
\begin{array}{lll}
\mathrm{MC2} & \text{fuerte} &
\text{temperature/setpoint/mode/sensor selection tienen semántica operacional};\\
\mathrm{MC3} & \text{fuerte para control} &
\text{thermostat + Heat Link realizan una unidad funcional física, no solo un diagrama};\\
\mathrm{MC4} & \text{fuerte para el lazo declarado} &
\text{sensor data y señal Heat Link median input/output de control};\\
\mathrm{MC5} & \text{fuerte-candidata} &
\text{setpoint/schedule/sensor state determinan continuación del control};\\
\mathrm{MC6} & \text{parcial} &
\text{manual override, wiring faults, power loss y HVAC internals no quedan agotados};\\
\mathrm{MC7} & \text{parcial} &
\text{closed-loop behavior está documentado, pero no screening-off de toda perturbación física};\\
\mathrm{MC8} & \text{fuerte} &
\text{meter una habitación adicional bajo una llave descriptiva no crea unidad};\\
\mathrm{MC10} & \text{parcial} &
\text{schedule/state transitions están claras; persistence/cessation ontológica no}.
\end{array}
\]

Este caso aclara además el higher-order candidate:

\[
C_{\mathrm{home-loop}}
=
\text{thermostat + Heat Link + heater + room}.
\]

La documentación confirma feedback físico entre lectura de temperatura y activación de calefacción, pero no basta por sí sola para afirmar que toda esa composición forma un contexto adicional. Para eso sigue siendo necesaria una teoría que justifique JointUnitGround y su boundary frente al resto de la vivienda/ambiente.

**Resultado NEST-R.**

\[
\boxed{
\operatorname{NestControlEvidence}
\Rightarrow
\text{real physical-control candidate}
\not\Rightarrow
\operatorname{ContextIndividuation}.
}
\]

#### 0.11.91r-u. EMP-T1 — qué ha sido realmente descargado

La comparación ya no es solo entre toys. Tenemos tres sistemas concretos con fuentes externas heterogéneas:

\[
\mathrm{Redis},
\qquad
\mathrm{E.\ coli},
\qquad
\mathrm{Nest/HeatLink}.
\]

En los tres, el mismo esquema identifica correctamente:

- una unidad positiva más fuerte que packaging;
- operaciones/estados localmente definidos;
- apertura por interfaces/canales;
- dinámica reentrante o regulada;
- un rival cut arbitrario que falla;
- posibles contextos nested/higher-order que requieren grounding adicional.

No apareció una excepción domain-specific nueva a IA0–IA10/MC1–MC10.

Pero la auditoría también localiza el cuello de botella común:

\[
\boxed{
\mathrm{MC6}
+
\mathrm{MC7}
+
\mathrm{IA0}
}
\]

son justamente donde evidencia de mecanismos/documentación deja de equivaler a una demostración ontológica completa.

Por tanto el resultado empírico honesto es:

\[
\boxed{
\begin{aligned}
&
\operatorname{ExternalEvidence}
+
\operatorname{CrossDomainMappingAdequate}\\
&\Rightarrow
\operatorname{EvidenceBackedContextCandidate},
\end{aligned}
}
\]

pero:

\[
\boxed{
\operatorname{EvidenceBackedContextCandidate}
\not\Rightarrow
\operatorname{ContextIndividuation}.
}
\]

**EMP-T1 — empirical non-promotion.** La misma disciplina de No-Free-Promotion se aplica a la propia evidencia científica/técnica: una lista convincente de mecanismos no debe promocionarse automáticamente a ontología. El bridge necesita quedar identificado y defendido.

Esto es un avance para Cellular Reality porque desplaza la duda. La objeción ya no es “el contrato solo funciona en toys”. La deuda queda más precisa:

> ¿qué evidencia/teoría es suficiente para pasar de una estructura causal-organizacional bien respaldada a la afirmación objetiva de que existe una unidad contextual?

Ese es ahora el punto exacto donde debe concentrarse una futura defensa de IA0/IndAdequate.

#### 0.11.91r-v. IA0 se descompone: realidad estructural no es todavía unidad contextual

La auditoría EMP-T1 dejó el cuello en IA0. El ataque adversarial revela que “structural fidelity” estaba haciendo dos trabajos:

\[
\boxed{
IA0
=
IA0\text{-}R
+
IA0\text{-}U.
}
\]

**IA0-R / realized modal support.** La estructura invocada por \(\mathcal T\) está efectivamente realizada y soporta las dependencias modales/counterfactuals que el criterio le atribuye. OR1–OR9, RealizedEmergence y evidencia independiente pueden descargar esta parte.

**IA0-U / individuation relevance.** La estructura realizada no es solo un patrón, mecanismo o variable macro real: hace trabajo constitutivo/discriminante para **la unidad de \(C\)**, es decir, para el mismo perfil pre-indexado de typing, boundary, interface mediation y dinámica que pretende justificar ContextIndividuation.

Por tanto queda rechazado:

\[
\boxed{
IA0\text{-}R
\not\Rightarrow
IA0.
}
\]

Y también:

\[
\boxed{
\operatorname{RealPattern}(P)
\not\Rightarrow
\operatorname{ContextIndividuation}(C).
}
\]

La ontología puede ser realistamente plural respecto de patterns/effective structures sin que cada patrón real genere automáticamente un índice.

#### 0.11.91r-w. UnitGroundAdequate — qué falta para IA0-U

TR-M ya dispone de un perfil pre-indexado:

\[
\Xi_C
=
\left\langle
\widehat\Lambda_C,
\widehat{\mathbb I}_C,
\widehat{\mathbb P}_C,
\widehat{\mathsf{CP}}_C,
\partial_C
\right\rangle.
\]

Introducimos un witness theory-specific \(g\) de **ground de unidad** y el juicio:

\[
\boxed{
\operatorname{UnitGroundAdequate}^{\mathsf M}
(
\mathcal T,C;g,\Xi_C
).
}
\]

No es un nuevo truthmaker por nombre. Es un bundle de obligaciones que debe reducirse a estructura concreta de \(\mathcal T\):

1. **UG1 / pre-index independence:** \(g\) se caracteriza sin \(R_i\), ContextIndividuation, IndexAdmission, RegimeTotal o SameRegime.
2. **UG2 / positive actuality:** \(g\) está efectivamente realizado; una regularidad del modelo o una frontera dibujada no bastan.
3. **UG3 / profile relevance:** \(g\) fundamenta al menos una parte no eliminable de \(\Xi_C\); si se elimina \(g\) de la teoría sin alterar typing, boundary, interfaces, persistence/dynamics ni rival-cut status, \(g\) no estaba individuando \(C\).
4. **UG4 / constitutive sensitivity:** existen intervenciones admisibles sobre \(g\), fijadas pre-indexadamente y con controles negativos apropiados, que producen un `UnitProfileBreak` en \(\Xi_C\). `UnitProfileBreak` se define sin ContextIndividuation/IndexAdmission: exige pérdida de typing/boundary/interface/continuation/rival-cut coherence del perfil candidato, no mera variación de output.
5. **UG5 / exterior screening de unidad:** fijados \(g\), las interfaces declaradas y el estado relevante, variaciones externas que \(\mathcal T\) declara irrelevantes no cambian el perfil de unidad; si lo hacen aparece un hidden constitutive bypass.
6. **UG6 / rival-cut discrimination:** \(g\) debe resolver o clasificar las rivalidades relevantes mediante equivalencia, nesting, overlap, genesis o rejection; no puede ser compatible indiferentemente con cualquier partición conveniente.
7. **UG7 / no real-pattern promotion:** projectability, compresión, macroeficacia, autonomía causal o utilidad explicativa de \(P\) no cuentan por sí solas como UG3–UG6.
8. **UG8 / covariance:** recodificaciones fieles y witnesses epistémicos alternativos preservan el mismo juicio de ground de unidad.

Entonces:

\[
\boxed{
IA0\text{-}R(C)
+
\operatorname{UnitGroundAdequate}_{\mathcal T}(C;g,\Xi_C)
\Rightarrow
IA0(C).
}
\]

Esta regla explicita el contenido de IA0; no prueba universalmente que exista \(g\). Cada dominio debe exhibirlo.

#### 0.11.91r-x. Countermodels contra la promoción de estructura real a contexto

**IA0-X1 — real pattern sin ground de unidad.** Un host realiza un patrón macro \(P\) que es recoding-invariant, projectable, dinámicamente eficaz y contrafácticamente robusto. Sin embargo \(P\) puede borrarse de la teoría de individuación sin cambiar \(\Xi_C\), o puede aparecer sobre múltiples cuts incompatibles. Entonces IA0-R vale, UG3/UG6 fallan y no se obtiene contexto.

**IA0-X2 — mecanismo real relativo a fenómeno.** Una descomposición mecanística puede identificar componentes/actividades reales y explicar un fenómeno seleccionado. Eso establece estructura causal efectiva, pero la descomposición puede depender del fenómeno explanandum y no seleccionar una unidad contextual autónoma. IA0-R puede valer mientras IA0-U quede abierta.

**IA0-X3 — causal emergence sin contextualidad.** Incluso si una macrodescripción supera a una microdescripción respecto de una métrica causal/informacional, eso demuestra relevancia causal de la macroescala, no que su partition sea una unidad contextual. Hace falta UG3–UG6.

**IA0-X4 — dos patrones efectivos cruzados.** El mismo host puede soportar dos patterns \(P,Q\) igualmente projectables y modalmente robustos cuyos cuts se cruzan. Si ninguno aporta una resolución grounded de la rivalidad, admitir ambos índices por mera realidad de patrón viola IA8/UG6.

Estos countermodels no sostienen que patterns, mecanismos o macrocausas sean irreales. Precisamente funcionan porque pueden ser **reales sin ser automáticamente context-individuating**.

#### 0.11.91r-y. Resultado adversarial sobre RSP y epsilon-RSP

La forma genérica:

\[
\operatorname{ActualStructuralRealization}
+
\operatorname{MCAdequate}
\Rightarrow
IA0
\]

queda rechazada como demasiado fuerte.

La forma emergentista anterior:

\[
\operatorname{RealizedEmergence}
+
\operatorname{MCAdequate}
\Rightarrow
IA0
\]

también queda **SUPERSEDED** en su conclusión completa.

Lo que sí sobrevive es:

\[
\boxed{
\operatorname{RealizedEmergence}
+
\operatorname{MCAdequate}
\Rightarrow
IA0\text{-}R.
}
\]

Para llegar a IA0:

\[
\boxed{
IA0\text{-}R
+
\operatorname{UnitGroundAdequate}
\Rightarrow
IA0.
}
\]

Por tanto la emergencia deja de ser el bridge metafísico final. Hace un trabajo indispensable pero más preciso: demuestra que la organización no es una ficción descriptiva. El paso desde **estructura real** a **unidad contextual** pertenece a la teoría de individuación.

#### 0.11.91r-z. Consecuencia para Cellular Reality y XR-epsilon

El resultado adversarial fortalece la arquitectura aunque debilite el teorema existencial condicional previo.

Cellular Reality ya no puede formularse como:

\[
\text{real organization}
\Rightarrow
\text{context}.
\]

Su forma rigurosa es:

\[
\boxed{
\text{real modal organization}
+
\text{ground of unity}
\Rightarrow
\text{admissible context individuation}.
}
\]

Para Redis, E. coli y Nest, la evidencia externa puede contribuir a IA0-R y a partes de UG2–UG5, pero ninguna auditoría actual demuestra exhaustivamente UnitGroundAdequate.

Para XR-\(\varepsilon\), el script y EA1–EA8 descargan IA0-R. Falta un argumento independiente de UG3–UG6 que muestre que la organización path→cycle no es simplemente un real emergent pattern dentro del host, sino el ground de la unidad contextual exacta \(C_{XR1}\).

Por tanto:

\[
\boxed{
XR\varepsilon
\text{ sigue siendo un witness formal/realizacional fuerte,}
\quad
\text{pero ExistsR conserva una deuda explícita de IA0-U.}
}
\]

Esta revisión elimina el riesgo de obtener ContextIndividuation simplemente porque Exergism ya es emergentista.

#### 0.11.91r-aa. UGAudit — PASS, PARTIAL y FAIL son estados epistémicos de descarga

Para aplicar UG1–UG8 sin convertir ausencia de evidencia en inexistencia ontológica, introducimos:

\[
\operatorname{UGAudit}^{\mathsf M}
(
\mathcal T,C;g,\Xi_C,E
)
\in
\{\mathsf{PASS},\mathsf{PARTIAL},\mathsf{FAIL}\}^{8}.
\]

La clasificación es **por obligación**:

- **PASS:** la teoría + evidencia disponible descargan positivamente el guard;
- **PARTIAL:** el guard no ha sido refutado, pero la descarga es incompleta o depende de evidencia/intervenciones no disponibles;
- **FAIL:** existe una razón positiva para negar el guard al witness \(g\) propuesto.

No se adopta:

\[
\mathsf{PARTIAL}
\Rightarrow
\neg\operatorname{UnitGroundAdequate}.
\]

Ni:

\[
\mathsf{PASS}
\Rightarrow
\operatorname{ContextIndividuation},
\]

si faltan otras obligaciones de IndAdequate.

**UG-T0 / complete discharge.**

\[
\boxed{
\operatorname{UnitGroundAdequate}
\Rightarrow
\bigwedge_{k=1}^{8}
\operatorname{UGAudit}_k=\mathsf{PASS}.
}
\]

La conversa solo vale cuando cada PASS proviene de la teoría/evidencia declaradas y no de una etiqueta manual.

#### 0.11.91r-ab. UG-XR1 — auditoría del witness ejecutable

Para XR-1 el candidato natural de ground no es la macropropiedad \(\beta_1\) aislada. Tomamos:

\[
g_{XR1}
=
\langle
\text{typed host/local realization},
\text{transition integration},
\text{declared interaction boundary}
\rangle.
\]

La organización path→cycle aporta IA0-R, pero \(g_{XR1}\) pretende hacer el trabajo de **unidad**.

Auditoría:

\[
\begin{array}{lll}
UG1 & \mathsf{PASS} &
g_{XR1}\text{ se define en DTS/host realization antes de }R_i;\\
UG2 & \mathsf{PASS} &
\text{el run host-side es ejecutado y OR1 queda evidenciado};\\
UG3 & \mathsf{PASS} &
\text{quitar transition integration altera }\widehat{\mathbb P},\widehat{\mathsf{CP}}\text{ y el typing dinámico};\\
UG4 & \mathsf{PASS} &
\text{CIT-XR1 usa phase/payload como brazo positivo e irrelevant_noise como control negativo sin presuponer identidad};\\
UG5 & \mathsf{PASS} &
\texttt{irrelevant_noise}\text{ se varía explícitamente y queda screened-off};\\
UG6 & \mathsf{PARTIAL} &
\text{anti-gerrymandering existe, pero el script no enumera rival cuts alternativos y demuestra su rechazo};\\
UG7 & \mathsf{PASS} &
\beta_1\text{/emergencia ya no se usan como ground suficiente};\\
UG8 & \mathsf{PASS} &
\text{OR6 verifica una recodificación fiel del host/local mapping}.
\end{array}
\]

Por tanto:

\[
\boxed{
\operatorname{UGAudit}_{XR1}
=
\langle
P,P,P,P,P,\partial,P,P
\rangle,
}
\]

donde \(P=\mathsf{PASS}\) y \(\partial=\mathsf{PARTIAL}\).

**XR1-UG-R.** CIT-XR1 cierra UG4 sin usar ContextIndividuation como premisa. La única deuda UnitGround restante para XR-1 es UG6 / rival-cut discrimination.

#### 0.11.91r-ac. UG-REDIS — proceso/estado/protocolo como ground candidato

Para Redis tomamos:

\[
g_{\mathrm{Redis}}
=
\langle
\text{server process},
\text{owned dataset/state},
\text{event loop},
\text{RESP/command boundary},
\text{persistence machinery}
\rangle.
\]

No tomamos “Redis” como brand, deployment label ni API document.

Auditoría con las fuentes de §14.1:

\[
\begin{array}{lll}
UG1 & \mathsf{PASS} &
\text{process/protocol/state se especifican independientemente de Exergism};\\
UG2 & \mathsf{PARTIAL} &
\text{la implementación es real/documentada, pero aquí no se observa un token server concreto};\\
UG3 & \mathsf{PASS} &
\text{event loop, dataset ownership y protocol boundary son no eliminables para el perfil declarado};\\
UG4 & \mathsf{PARTIAL} &
\text{crash/restart/configuration muestran sensibilidad, pero falta una intervención diseñada para reindividuación};\\
UG5 & \mathsf{PARTIAL} &
\text{host signals, debugger writes, scheduler/memory faults y otros bypasses no están agotados};\\
UG6 & \mathsf{PARTIAL} &
\text{cuts como odd-keys+half-worker son rechazables por roles, pero no existe una enumeración/teorema de rival cuts};\\
UG7 & \mathsf{PASS} &
\text{la utilidad de la API o predictibilidad del servicio no se usan como suficiencia};\\
UG8 & \mathsf{PASS} &
\text{renaming/serialization/implementation-preserving recodings no cambian el criterio arquitectónico}.
\end{array}
\]

Así:

\[
\boxed{
\operatorname{UGAudit}_{Redis}
=
\langle
P,\partial,P,\partial,\partial,\partial,P,P
\rangle.
}
\]

Redis sigue siendo un **evidence-backed candidate**, no una descarga de UnitGroundAdequate.

#### 0.11.91r-ad. UG-ECOLI — organización mantenida como ground candidato

Para E. coli, el candidato de ground no es “tener membrana”, sino una organización integrada:

\[
g_{\mathrm{Ecoli}}
=
\langle
\text{cell-envelope homeostasis},
\text{regulated transport},
\text{metabolic/regulatory organization},
\text{division/repair machinery}
\rangle.
\]

Auditoría:

\[
\begin{array}{lll}
UG1 & \mathsf{PASS} &
\text{los mecanismos biológicos se caracterizan sin el target metaontológico};\\
UG2 & \mathsf{PASS} &
\text{los mecanismos están experimentalmente observados en células reales, aunque no se siga aquí un token único};\\
UG3 & \mathsf{PASS} &
\text{envelope/homeostasis/transport son constitutivos del perfil celular usado};\\
UG4 & \mathsf{PARTIAL} &
\text{stress/damage/division muestran sensibilidad constitutiva, pero la transición exacta a reindividuación/cessation no está formalizada};\\
UG5 & \mathsf{PARTIAL} &
\text{la apertura mediada está bien respaldada, no el screening-off de toda perturbación relevante};\\
UG6 & \mathsf{PARTIAL} &
\text{half-cell y molecule+cell cuts quedan mal fundados, pero no hay completitud sobre todas las particiones biológicas rivales};\\
UG7 & \mathsf{PASS} &
\text{homeostasis/autopoiesis/closure no se convierten por nombre en suficiencia ontológica};\\
UG8 & \mathsf{PASS} &
\text{el criterio depende de organización/mecanismo, no de nombres moleculares o representación particular}.
\end{array}
\]

Por tanto:

\[
\boxed{
\operatorname{UGAudit}_{Ecoli}
=
\langle
P,P,P,\partial,\partial,\partial,P,P
\rangle.
}
\]

E. coli tiene una descarga empírica más directa de UG2–UG4 que los artefactos documentales, pero **UG5/UG6 siguen PARTIAL**. No se declara UnitGroundAdequate completo.

#### 0.11.91r-ae. UG-NEST — closed-loop control como ground candidato

Para Nest/Heat Link:

\[
g_{\mathrm{Nest}}
=
\langle
\text{sensor selection},
\text{controller state/schedule},
\text{Heat Link actuation},
\text{closed-loop feedback}
\rangle.
\]

Auditoría:

\[
\begin{array}{lll}
UG1 & \mathsf{PASS} &
\text{la arquitectura de control existe independientemente de la ontología};\\
UG2 & \mathsf{PARTIAL} &
\text{el producto físico está documentado, pero no se instrumenta aquí una instalación/token concreto};\\
UG3 & \mathsf{PASS} &
\text{quitar sensing/actuation/feedback destruye el perfil de control declarado};\\
UG4 & \mathsf{PARTIAL} &
\text{cambiar sensor/setpoint/wiring altera control, pero no se formaliza cuándo cambia la unidad};\\
UG5 & \mathsf{PARTIAL} &
\text{manual override, power, HVAC internals y perturbaciones ambientales no están exhaustivamente screened};\\
UG6 & \mathsf{PARTIAL} &
\text{PCB-half y arbitrary-room-union fallan, pero el lazo ampliado home-loop permanece un rival/higher-order candidate};\\
UG7 & \mathsf{PASS} &
\text{closed-loop usefulness no se identifica con contextualidad};\\
UG8 & \mathsf{PASS} &
\text{el criterio es invariante a representaciones fieles del mismo lazo}.
\end{array}
\]

Luego:

\[
\boxed{
\operatorname{UGAudit}_{Nest}
=
\langle
P,\partial,P,\partial,\partial,\partial,P,P
\rangle.
}
\]

El resultado se parece a Redis por una razón metodológica: la documentación fija bien la arquitectura nominal/funcional, pero no proporciona por sí sola la intervención completa necesaria para UG4–UG6.

#### 0.11.91r-af. UG-COMP — comparación sin ranking ontológico

La matriz conjunta es:

\[
\boxed{
\begin{array}{c|cccccccc}
 & UG1&UG2&UG3&UG4&UG5&UG6&UG7&UG8\\
\hline
XR1   &P&P&P&P&P&\partial&P&P\\
Redis &P&\partial&P&\partial&\partial&\partial&P&P\\
Ecoli &P&P&P&\partial&\partial&\partial&P&P\\
Nest  &P&\partial&P&\partial&\partial&\partial&P&P
\end{array}
}
\]

No es un ranking de “qué cosa es más real”. La matriz mide **qué obligaciones hemos descargado con la teoría/evidencia actual**.

Dos hallazgos sí son robustos:

1. **UG3 no es el cuello principal.** En los cuatro casos puede identificarse estructura cuya eliminación cambia el perfil local relevante.
2. **UG4–UG6 concentran la deuda cross-domain, pero XR-1 ya cierra UG4 por CIT.** Lo difícil en los casos empíricos sigue siendo demostrar sensibilidad constitutiva con controles; para XR-1 la deuda se reduce a discriminar exhaustivamente cuts rivales.

Esto refina el problema de IA0-U:

\[
\boxed{
\text{unity grounding}
\approx
\text{constitutive sensitivity}
+
\text{constitutive screening}
+
\text{rival-cut discrimination},
}
\]

sin definirlo todavía como equivalencia.

#### 0.11.91r-ag. UG-T1 — ninguna descarga completa todavía

Con la evidencia y teoría actuales:

\[
\boxed{
\neg\operatorname{Discharged}^{\mathsf M}
(
\operatorname{UnitGroundAdequate}_{XR1}
)
}
\]

y análogamente para Redis, E. coli y Nest.

Esto **no** implica que ninguno sea contexto. Implica que el corpus todavía no posee una prueba positiva completa de UG1–UG8 para ninguno.

La consecuencia para la estrategia de investigación es precisa. Añadir más casos similares tiene rendimiento decreciente. El siguiente trabajo debe centrarse en formalizar y atacar:

\[
UG5,\quad UG6,
\]

El criterio de **constitutive intervention** queda resuelto a nivel formal por CIT/UnitProfileBreak y descargado para XR-1. Para los casos empíricos sigue faltando evidencia controlada que distinga:

\[
\text{cambio de comportamiento dentro de la misma unidad}
\]

de:

\[
\text{cambio que destruye, divide, fusiona o reindividúa la unidad}.
\]

Sin esa distinción, UG4 corre el riesgo de presuponer exactamente la individuación que pretende fundamentar.

#### 0.11.91r-ah. UnitProfileBreak — sensibilidad constitutiva sin presuponer reindividuación

La formulación inicial de UG4 contenía una circularidad potencial: exigir una intervención que “fuerce reindividuación” puede presuponer que ya sabemos qué cuenta como la misma unidad.

La reemplazamos por un test completamente pre-indexado.

Sea:

\[
\Xi_C
=
\left\langle
\widehat\Lambda_C,
\widehat{\mathbb I}_C,
\widehat{\mathbb P}_C,
\widehat{\mathsf{CP}}_C,
\partial_C
\right\rangle.
\]

Definimos:

\[
\boxed{
\operatorname{UnitProfileBreak}^{\mathsf M}_{\mathcal T}
(
C,\Xi_C;\delta
)
}
\]

cuando una intervención \(\delta\) produce al menos uno de estos fallos, evaluados sin usar ContextIndividuation:

1. **UPB1 / typing break:** operaciones/estados anteriormente co-tipados dejan de satisfacer las reglas locales que justificaban \(\widehat\Lambda_C\);
2. **UPB2 / boundary break:** \(\partial_C\) deja de mediar una dependencia que la teoría considera constitutivamente relevante;
3. **UPB3 / interface break:** aparece una dependencia relevante que no factoriza por \(\widehat{\mathbb I}_C\);
4. **UPB4 / continuation break:** la dinámica ya no induce el mismo tipo de continuation profile o deja de estar definida bajo el contract state correspondiente;
5. **UPB5 / closure/role break:** un rol constitutivo previamente cubierto desaparece o queda desacoplado de la organización candidata;
6. **UPB6 / rival-cut break:** la estructura que privilegiaba \(C\) deja de discriminarlo frente a un rival cut anteriormente rechazado.

No cuenta como UnitProfileBreak:

\[
\text{output changes}
\quad\text{con}\quad
\Xi_C\text{ preservado}.
\]

Así distinguimos:

\[
\boxed{
\text{behavioral sensitivity}
\neq
\text{constitutive sensitivity}.
}
\]

#### 0.11.91r-ai. CIT — Constitutive Intervention Test

Sea \(\Delta_g\) una familia pre-registrada de intervenciones sobre el ground candidato \(g\), definida sin usar el resultado “\(C\) es contexto”.

Definimos:

\[
\operatorname{CITAdequate}^{\mathsf M}
(
\mathcal T,C;g,\Xi_C,\Delta_g
)
\]

si:

1. **CIT1 / preregistration:** \(g,\Xi_C,\Delta_g\) se fijan antes de observar qué intervención favorece el cut;
2. **CIT2 / positive arm:** existe \(\delta^+\in\Delta_g\) que altera una parte del ground postulada como constitutiva y produce UnitProfileBreak;
3. **CIT3 / negative control:** existe \(\delta^-\) sobre una variable declarada irrelevante que cambia físicamente/operacionalmente el host sin producir UnitProfileBreak;
4. **CIT4 / matched background:** las diferencias no dirigidas al contraste relevante se mantienen fijas o quedan explícitamente modeladas;
5. **CIT5 / no output substitution:** un cambio de output sin UPB1–UPB6 no satisface CIT2;
6. **CIT6 / recoding covariance:** recodificaciones fieles preservan qué intervenciones son constitutive-positive y cuáles controles;
7. **CIT7 / bypass discipline:** si \(\delta\) actúa por un canal no representado pero constitutivamente relevante, el resultado es revisar \(\Xi_C\), no declararlo “externo”;
8. **CIT8 / no identity premise:** ninguna condición contiene SameContext, ContextIndividuation, IndexAdmission o “reindividuación” como antecedente.

Entonces UG4 se descarga por:

\[
\boxed{
\operatorname{CITAdequate}
\Rightarrow
UG4.
}
\]

CIT no demuestra UG5 ni UG6. Una unidad puede ser constitutivamente sensible a su ground y seguir mal delimitada respecto del exterior o de rival cuts.

#### 0.11.91r-aj. CIT-XR1 — XR-1 sí descarga UG4

XR-1 ya contiene un experimento mínimo de intervención:

- variables localmente relevantes: \(\texttt{phase}\), \(\texttt{payload}\);
- control host-side declarado irrelevante: \(\texttt{irrelevant\_noise}\);
- mapping \(\varrho\) pre-registrado;
- transición host/local pre-registrada.

El script prueba:

\[
\delta^-:
\texttt{irrelevant\_noise}
\mapsto
n
\]

para múltiples \(n\), manteniendo:

\[
\rho(h)=s_0,
\qquad
\rho(T_H(h))=s_1.
\]

Por tanto el control negativo no produce UnitProfileBreak.

En cambio:

\[
\delta^+_1:
(\texttt{phase}=0,\texttt{payload}=0)
\mapsto
(0,1)
\]

o:

\[
\delta^+_2:
(0,0)
\mapsto
(1,0)
\]

hacen que \(\rho\) deje de reconocer un estado local válido. Eso es un UPB1/UPB4: se rompe el typing/continuation profile de la realización candidata, no solo una salida.

OR5/OR8/OR9 aportan preregistration/no-certificate/prefix-locality y OR6 la covariancia.

Por tanto:

\[
\boxed{
\operatorname{CITAdequate}_{XR1}
}
\]

y actualizamos:

\[
\boxed{
UG4_{XR1}=\mathsf{PASS}.
}
\]

La matriz XR-1 pasa a:

\[
\operatorname{UGAudit}_{XR1}
=
\langle
P,P,P,P,P,\partial,P,P
\rangle.
\]

**Resultado:** para XR-1 la única deuda UnitGround restante es ahora **UG6 / rival-cut discrimination**.

#### 0.11.91r-ak. CIT no promociona automáticamente los casos empíricos

Para Redis, E. coli y Nest existen perturbaciones naturales plausibles:

- crash/configuration/state corruption;
- envelope damage/stress/division perturbations;
- sensor/wiring/power/controller perturbations.

Pero el corpus actual no posee para ellos un diseño de intervención suficientemente especificado que separe:

\[
\delta^+
\quad\text{de}\quad
\delta^-
\]

bajo background matching y mida UPB1–UPB6.

Por tanto permanecen:

\[
UG4_{\mathrm{Redis}}
=
UG4_{\mathrm{Ecoli}}
=
UG4_{\mathrm{Nest}}
=
\mathsf{PARTIAL}.
\]

Esto evita convertir “sabemos que el sistema cambia cuando lo dañamos” en constitutive sensitivity.

#### 0.11.91r-al. Deuda reducida: UG5 y UG6, con UG6 único blocker de XR-1

Tras CIT-XR1:

\[
\boxed{
\operatorname{UGAudit}_{XR1}
=
\langle
P,P,P,P,P,\partial,P,P
\rangle.
}
\]

Por tanto, si logramos descargar UG6 para XR-1 mediante una enumeración/teorema de rival cuts pre-indexados, tendremos:

\[
\boxed{
\operatorname{UnitGroundAdequate}_{XR1}.
}
\]

Eso cerraría IA0-U para el witness finito **sin** afirmar todavía que el criterio general esté universalmente resuelto.

Para los tres casos empíricos, UG4–UG6 siguen parciales. El próximo target formal de mayor rendimiento es, por tanto:

\[
\boxed{
UG6_{XR1}.
}
\]

XR-1 es finito y puede permitir un ataque exhaustivo sobre la clase de cuts admitida por \(\mathcal T_{\mathrm{DTS}}\). La condición crítica será no definir esa clase usando retrospectivamente la closure o el scope que queremos justificar.

#### 0.11.91r-am. XR1FiniteRivalClass — clase adversarial pre-indexada

El audit ejecutable de UG6 no puede cuantificar sobre “todo cut imaginable” sin convertir la obligación en una clase informal incontrolable. Definimos primero una clase adversarial generada exclusivamente por estructura pre-indexada de XR-1:

\[
\boxed{
\mathfrak R^{\mathrm{fin}}_{XR1}
}
\]

contiene:

1. **role subcuts:** todos los subconjuntos propios no vacíos de los roles declarados \(\{s_0,e_0,s_1\}\);
2. **fixed-signature state maps:** todos los maps binarios desde las dos clases host coherentes pre/post hacia \(\{s_0,s_1\}\);
3. **state quotients:** el quotient no trivial que identifica \(s_0\sim s_1\);
4. **noise refinements:** refinamientos cuya única nueva distinción depende de \(\texttt{irrelevant\_noise}\);
5. **faithful recodings:** transportes que solo cambian representación y deben clasificarse como equivalencia, no como nueva unidad.

La clase se define antes de ContextIndividuation y sin usar GeneClosure, RegimeTotal o el scope final.

#### 0.11.91r-an. XR1-RC-T1 — cierre exhaustivo dentro de la clase finita

El script scripts/xr1_witness.py verifica ahora cuatro hechos adicionales.

**FR1 / proper role cuts fail fixed signature.** Todo subcut propio omite al menos un miembro del footprint de la única transición productiva:

\[
\{s_0,e_0,s_1\}.
\]

Por tanto no preserva la misma signature transicional completa.

**FR2 / fixed-signature state mapping is unique.** Hay exactamente cuatro funciones binarias sobre las dos clases host coherentes. Exigiendo surjectivity y la transición dirigida declarada:

\[
s_0\xrightarrow{e_0}s_1,
\]

solo sobrevive la asignación canónica pre→\(s_0\), post→\(s_1\).

**FR3 / merged-state quotient is not observationally faithful.**

\[
\operatorname{Available}(s_0)
\neq
\operatorname{Available}(s_1),
\]

porque \(\texttt{close}\) e \(\texttt{activate}\) pertenecen a perfiles distintos. El quotient \(s_0\sim s_1\) borra una distinción operacional declarada.

**FR4 / noise-only refinements fail relevance.** \(\rho\) es sintácticamente independiente de \(\texttt{irrelevant\_noise}\), y OR4 ya demuestra screening-off bajo variaciones de esa coordenada. Una unidad adicional distinguida solo por noise falla UG3/UG7.

Así:

\[
\boxed{
\forall D\in\mathfrak R^{\mathrm{fin}}_{XR1},
\quad
D
\text{ es rechazado o equivalente al cut XR-1}.
}
\]

Esto es un resultado UG6 real, pero todavía **relativo a la clase**.

#### 0.11.91r-ao. RivalClassCompleteness — lo que falta para convertir FR1–FR4 en UG6 completo

Definimos:

\[
\boxed{
\operatorname{RivalClassComplete}^{\mathsf M}_{\mathcal T}
(
C,\mathfrak R
)
}
\]

cuando todo same-level rival cut que la teoría \(\mathcal T\) puede formular mediante su vocabulario/estructuras admisibles satisface al menos una de estas condiciones:

1. pertenece a \(\mathfrak R\);
2. es una faithful recoding de un miembro;
3. está clasificado independientemente como nesting/overlap/genesis y por tanto no compite al mismo nivel;
4. viola una regla preexistente de \(\mathcal T\) no introducida para proteger \(C\).

Exigimos además:

- **RCC1 / signature closure:** \(\mathfrak R\) cubre todas las construcciones de cut permitidas por la firma relevante;
- **RCC2 / recoding closure:** recodificaciones fieles no crean escapes;
- **RCC3 / no target filter:** la pertenencia a \(\mathfrak R\) no usa “preserva \(C\)” como criterio;
- **RCC4 / observable closure:** todos los observables/ports/roles que \(\mathcal T\) permite usar para individuación están incluidos;
- **RCC5 / environment closure:** no se excluyen arbitrariamente cortes inducidos por diferentes interacciones con el entorno;
- **RCC6 / auditability:** un contraejemplo concreto puede falsar completeness exhibiendo un rival permitido fuera de \(\mathfrak R\).

Entonces:

\[
\boxed{
\operatorname{XR1FiniteRivalAudit}
+
\operatorname{RivalClassComplete}_{\mathcal T}
(C_{XR1},\mathfrak R^{\mathrm{fin}}_{XR1})
\Rightarrow
UG6_{XR1}.
}
\]

#### 0.11.91r-ap. DTS-UG6 finding — un DTS desnudo no demuestra RivalClassCompleteness

La teoría determinista de transición usada hasta ahora fija states, events y transición. Eso basta para OR/GenClosure de XR-1, pero no contiene por sí sola una teoría general de:

- qué actions son inputs, outputs o internal;
- qué interacciones pertenecen al environment;
- qué assumptions/guarantees definen una component interface;
- qué refinements preservan la frontera de componente;
- qué candidate cuts son admisibles como componentes del mismo nivel.

Por tanto no podemos demostrar RCC4–RCC5 desde la estructura de un DTS desnudo sin añadir una premisa nueva.

El resultado correcto es:

\[
\boxed{
\mathcal T_{\mathrm{DTS}}
\not\vdash
\operatorname{RivalClassComplete}
(
C_{XR1},
\mathfrak R^{\mathrm{fin}}_{XR1}
).
}
\]

No es un contraejemplo a XR-1. Es un **insufficiency finding sobre la teoría usada para individuarlo**.

La literatura de I/O automata e interface automata ofrece precedentes independientes para una teoría más rica donde component/environment boundary, input/output actions, compatibility y refinement forman parte del formalismo. Una futura ruta XR-I/O puede usar ese vocabulario **si se especifica independientemente antes de volver a auditar el cut**.

Por tanto no fortalecemos \(\mathcal T_{\mathrm{DTS}}\) ad hoc en esta sección. Registramos la deuda:

\[
\boxed{
\operatorname{RivalClassCompleteness}_{XR1}
\quad\text{requiere una teoría de interfaz/componente independiente.}
}
\]

#### 0.11.91r-aq. T-IODTS — ruta independiente de teoría de interfaz

La insuficiencia de \(\mathcal T_{\mathrm{DTS}}\) no obliga a inventar una semántica específica de Exergism. I/O automata e interface automata proporcionan precedentes independientes donde el sistema se modela con interacción explícita con el entorno.

Adoptamos solo como **candidate theory**, no como ontología ya validada:

\[
\mathcal T_{\mathrm{IODTS}}
=
\langle
S,
A^{in},
A^{out},
A^{int},
\to
\rangle,
\]

con \(A^{in},A^{out},A^{int}\) disjuntos y cuya unión agota el alfabeto relevante.

La motivación independiente es operacional:

- inputs son acciones controladas/proporcionadas por el entorno;
- outputs son acciones localmente controladas y externamente expuestas;
- internal actions permanecen bajo control del componente y no cruzan su interfaz declarada;
- compatibility/refinement se evalúan respecto de esa polaridad y dinámica, no de un contorno dibujado después.

Exergism no importa la conclusión “todo I/O automaton es contexto”. Solo usa esta teoría como una posible fuente independently grounded para RCC4/RCC5.

#### 0.11.91r-ar. XR-I/O — interfaz pre-registrada para ejecuciones posteriores

El script XR-1 contiene ahora, antes de nuevas ejecuciones, la firma candidata:

\[
A^{in}_{XR}
=
\varnothing,
\]

\[
A^{out}_{XR}
=
\{\texttt{activate}\},
\]

\[
A^{int}_{XR}
=
\{\texttt{close},\texttt{idle}\}.
\]

La asignación se registra en código y CI verifica:

1. disjointness de las tres clases;
2. exhaustividad sobre las actions declaradas;
3. \(\texttt{close}\) solo está habilitada en \(s_0\) y se clasifica internal;
4. \(\texttt{activate}\) solo está habilitada en \(s_1\) y se clasifica output;
5. \(\texttt{idle}\) permanece internal en ambos estados;
6. el único split no trivial de \(\{s_0,s_1\}\) hace cruzar la transición internal \(\texttt{close}\), por lo que no preserva la misma component interface.

Esto mejora UG6 porque la frontera deja de ser solo un subconjunto de roles: hay una semántica explícita de action ownership.

#### 0.11.91r-as. IO-RC-T1 — qué rivales elimina la firma de interfaz

Bajo la firma fija anterior:

- separar \(s_0\) y \(s_1\) en dos componentes convertiría \(\texttt{close}\) de internal a cross-boundary; no preserva la misma interface;
- identificar \(s_0\sim s_1\) elimina la diferencia de enabled output \(\texttt{activate}\);
- añadir \(\texttt{irrelevant\_noise}\) como estado local introduce una distinción que no afecta ninguna action/interface/continuation relevante;
- recodificaciones fieles permanecen equivalentes;
- proper role cuts siguen fallando FR1.

Así la teoría de interfaz reduce materialmente la clase rival.

Sin embargo:

\[
\boxed{
\text{pre-registered interface signature}
\not\Rightarrow
\text{ontically grounded interface}.
}
\]

#### 0.11.91r-at. IAI-T1 — Interface Assignment Independence

Para usar \(\mathcal T_{\mathrm{IODTS}}\) en IA0-U necesitamos una condición adicional:

\[
\boxed{
\operatorname{InterfaceAssignmentIndependent}^{\mathsf M}
(
C,
A^{in},A^{out},A^{int};
\eta
).
}
\]

\(\eta\) debe justificar la polaridad/control de las actions mediante estructura operacional independiente del objetivo de obtener el cut.

Requisitos mínimos:

1. **IAI1 / control locus:** la clasificación input/output/internal corresponde a quién puede producir/aceptar la acción en la realización, no al nombre del label;
2. **IAI2 / realized mediation:** al menos las clases de interacción usadas para ground de frontera poseen una realización host/environment efectiva;
3. **IAI3 / no relabel rescue:** cambiar una action de internal a output no puede hacerse solo para salvar un rival cut;
4. **IAI4 / environment witness:** cuando se afirma una interacción externa, existe una estructura environment-side distinta del estado local;
5. **IAI5 / bypass accounting:** interacciones relevantes no clasificadas fuerzan revisión de la firma;
6. **IAI6 / covariance:** recodificaciones fieles preservan la polaridad/control operacional.

Entonces:

\[
\operatorname{InterfaceAssignmentIndependent}
+
\operatorname{XR1FiniteRivalAudit}
\]

puede alimentar RCC4/RCC5.

#### 0.11.91r-au. XR-I/O todavía no cierra IAI2/IAI4

La firma recién pre-registrada resuelve el problema **post-hoc** para runs futuros, pero no fabrica una interacción externa que el witness actual no contiene.

En el XR-1 vigente:

- \(\texttt{close}\) se ejecuta dentro de la función host-side;
- \(\texttt{activate}\) aparece como capacidad habilitada, no como output efectivamente emitido hacia un environment token distinto;
- no existe todavía una estructura environment-side cuya interacción sea parte del run certificado.

Por tanto:

\[
\boxed{
IAI1/IAI3/IAI6
\text{ son fuertes candidatos,}
\qquad
IAI2/IAI4
\text{ permanecen abiertos.}
}
\]

Y en consecuencia:

\[
\boxed{
UG6_{XR1}
\text{ sigue PARTIAL.}
}
\]

La pre-registration no se usa retroactivamente para elevar el status del run anterior.

#### 0.11.91r-av. Requisitos de XR-2 — componente realmente abierto

El siguiente witness ejecutable debe añadir una interacción environment/component sin perder las garantías formales ganadas.

Definimos el target **XR-2** por obligaciones, todavía no por implementación:

1. **XIO1 / separate environment:** existe \(E_H\) host-side distinto del component state;
2. **XIO2 / pre-registered channel:** input/output/internal alphabet y channel semantics se fijan en código antes del run;
3. **XIO3 / actual input or output:** al menos una transición actual cruza la interfaz mediante el channel declarado;
4. **XIO4 / local mediation:** el efecto del environment sobre el estado local factoriza por el input channel; no hay acceso oculto necesario;
5. **XIO5 / output witness:** cuando una capacidad output se declara constitutiva, existe un receiver/environment-side observation independiente;
6. **XIO6 / negative controls:** variaciones environment-side fuera del channel que se declaran irrelevantes quedan screened-off;
7. **XIO7 / rival closure:** la semántica I/O permite demostrar RCC1–RCC6 para la clase de cuts del witness;
8. **XIO8 / scope discipline:** cualquier interaction token actual se coordina con OntProd/GenEvent/RegimeTotal; no se ocultan eventos reales fuera del scope para salvar el witness.

XR-2 no debe ser “XR-1 con más código”. Su razón de ser es atacar exactamente:

\[
\boxed{
IAI2 + IAI4 + RCC5 + UG6.
}
\]

Solo después tendría sentido volver a preguntar si XR-2 descarga UnitGroundAdequate completo.

#### 0.11.91r-aw. XR2-E — ejecución efectiva del componente abierto

XR-2 queda implementado en scripts/xr2_open_component.py y ejecutado por CI después de pre-registrar su teoría candidata de interfaz.

La realización host-side usa:

\[
E_H
\quad\text{(proceso environment/parent)}
\]

y:

\[
C_H
\quad\text{(proceso component/child)}
\]

con PIDs distintos y un channel IPC de multiprocessing.

El episodio actual es:

\[
E_H
\xrightarrow{\texttt{close}}
C_H
:
s_0\to s_1
\xrightarrow{\texttt{activate}}
E_H.
\]

CI verifica:

\[
\boxed{
\begin{array}{ll}
XIO1 &: \text{environment y component son procesos distintos};\\
XIO2 &: \text{input/output/internal partition disjunta y exhaustiva};\\
XIO3 &: \texttt{close}\text{ entra realmente y }\texttt{activate}\text{ sale realmente};\\
XIO4 &: \text{el worker recibe el channel como única entrada environment-side};\\
XIO5 &: \text{el receiver environment-side observa }\texttt{activate};\\
XIO6 &: \text{dos environment-noise controls distintos producen la misma traza local};\\
XIO8 &: \text{GenSound/GenComplete y scope exacto incluyen ambos interaction tokens}.
\end{array}
}
\]

El scope actual XR-2 es:

\[
\{s_0,\texttt{close},s_1,\texttt{activate}\}.
\]

La closure se obtiene en dos etapas:

\[
\{s_0\}
\leadsto
\{s_0,\texttt{close},s_1\}
\leadsto
\{s_0,\texttt{close},s_1,\texttt{activate}\}.
\]

Por tanto XR-2 no oculta el output actual fuera de RegimeGenerated: la disciplina XIO8 queda satisfecha para la instancia finita.

#### 0.11.91r-ax. IAI-XR2 — qué cambia respecto de XR-I/O nominal

XR-2 permite elevar:

\[
IAI2=\mathsf{PASS},
\qquad
IAI4=\mathsf{PASS}.
\]

Hay mediación realizada y un environment witness distinto.

Además:

- **IAI1 / control locus:** \(\texttt{close}\) es enviado por environment y \(\texttt{activate}\) emitido por component; PASS para el run;
- **IAI3 / no relabel rescue:** la polaridad está fijada en código antes de la ejecución certificada; PASS respecto de este run;
- **IAI6 / covariance:** sigue respaldada por la disciplina representacional previa, pero no se ha añadido todavía un segundo IPC recoding; PARTIAL-PASS;
- **IAI5 / bypass accounting:** permanece PARTIAL porque la realización corre sobre OS/runtime y no se ha demostrado una cobertura exhaustiva de señales, termination, scheduler/IPC failure u otras intervenciones host-side constitutivas.

Por tanto:

\[
\boxed{
\operatorname{InterfaceAssignmentIndependent}_{XR2}
\text{ está mucho más descargado, pero no cerrado globalmente.}
}
\]

#### 0.11.91r-ay. XR2-UG finding — interface actuality tampoco basta

XR-2 derrota una objeción concreta contra XR-1:

> “la interfaz solo existe en el dibujo/modelo”.

Ahora existe una interacción actual entre estructuras host-side distintas.

Pero no se adopta:

\[
\boxed{
\text{actual IPC boundary}
\Rightarrow
\operatorname{ContextIndividuation}.
}
\]

La primera auditoría UnitGround de XR-2 dejó UG4/UG5/UG6 abiertos y UG8 parcialmente apoyado. Esa clasificación queda **SUPERSEDED** por §§0.11.91r-ba–bi: el CIT positivo posterior cierra UG4, la recodificación explícita cierra UG8 y la enumeración de firma cierra UG6-S. Permanecen UG5 y UG6-H.

El avance estable de esta sección es que **IAI2/IAI4 dejan de ser deuda abstracta**; la descarga final detallada se mantiene en §0.11.91r-bi.
\]

#### 0.11.91r-az. Consecuencia metodológica: boundary evidence y unity evidence son distintas

XR-2 obliga a separar:

\[
\boxed{
\text{boundary actuality}
\neq
\text{unity sufficiency}.
}
\]

Un OS process, pipe, membrana biológica o protocolo puede suministrar evidencia muy fuerte de **dónde ocurren interacciones mediadas**. Todavía hace falta demostrar que esa estructura selecciona la unidad frente a todos los rivales relevantes y no es solo una frontera útil dentro de un host mayor.

Esto preserva No-Free-Promotion incluso después de abandonar toys puramente cerrados.

#### 0.11.91r-ba. UG5 no exige aislamiento físico absoluto: RealizationEnvelope

UG5 no puede significar:

\[
\forall \delta_{\mathrm{physical}}
\quad
\delta
\text{ no altera }C,
\]

porque entonces ningún organismo, proceso software o sistema de control abierto podría satisfacerlo.

Pero tampoco aceptamos:

\[
\text{“esa perturbación está fuera de nivel”}
\]

como cláusula libre.

Introducimos un **RealizationEnvelope** theory-relative y falsable:

\[
\boxed{
\operatorname{RealizationEnvelope}^{\mathsf M}_{\mathcal T}
(
C;\mathcal A,\mathcal F,\mathcal N,\Gamma
)
}
\]

donde:

- \(\mathcal A\) = interacciones environment/component ordinarias admitidas por la teoría;
- \(\mathcal F\) = fault/lifecycle interventions relevantes que pueden romper el perfil o producir cessation y, por tanto, **no** se llaman irrelevantes;
- \(\mathcal N\) = variaciones declaradas irrelevantes que deben quedar screened-off;
- \(\Gamma\) = assumptions explícitas de realización necesarias para interpretar el componente en ese nivel.

La partición no puede definirse desde el resultado. Debe fijarse independientemente y ser revisable por evidencia.

**RE1 / exhaustive classification relative to the theory.** Toda intervención que \(\mathcal T\) reconoce como relevante para la realización cae en \(\mathcal A\cup\mathcal F\cup\mathcal N\) o fuerza revisión del envelope.

**RE2 / ordinary mediation.** Toda \(\delta\in\mathcal A\) actúa mediante interfaces/channels declarados.

**RE3 / fault honesty.** Ninguna \(\delta\in\mathcal F\) puede presentarse como contraejemplo irrelevante; si rompe \(\Xi_C\), cuenta como fault/cessation/UnitProfileBreak según la teoría.

**RE4 / negative screening.** Toda \(\delta\in\mathcal N\) preserva el perfil relevante dentro de las assumptions \(\Gamma\).

**RE5 / assumption observability.** Una violación de \(\Gamma\) debe ser detectable como assumption violation, crash/fault o pérdida de realization; no puede reinterpretarse silenciosamente como comportamiento normal.

**RE6 / no protective assumptions.** \(\Gamma\) no puede incluir “el cut \(C\) sigue siendo la unidad” ni excluir exactamente los casos que derrotan la individuación.

**RE7 / extension pressure.** Si aparece una intervención reproducible que altera \(\Xi_C\) sin pertenecer a \(\mathcal A\) o \(\mathcal F\), UG5 falla hasta revisar el envelope.

Así UG5 se vuelve una obligación de **cobertura de interacción**, no de invulnerabilidad.

#### 0.11.91r-bb. UG5-T1 — Constitutive Screening relativo al envelope

Definimos:

\[
\operatorname{EnvelopeScreeningAdequate}^{\mathsf M}
(
C;\mathcal A,\mathcal F,\mathcal N,\Gamma
)
\]

si RE1–RE7 están descargados y:

\[
\forall \delta\in\mathcal N:
\neg\operatorname{UnitProfileBreak}(C,\Xi_C;\delta),
\]

mientras:

\[
\forall \delta\in\mathcal A:
\delta
\text{ factoriza por la interfaz declarada},
\]

y toda \(\delta\in\mathcal F\) que rompe el perfil queda clasificada positivamente como fault/cessation en vez de ocultarse.

Entonces:

\[
\boxed{
\operatorname{EnvelopeScreeningAdequate}
\Rightarrow
UG5.
}
\]

Esto es compatible con sistemas abiertos: el exterior puede afectar al contexto, pero debe hacerlo mediante canales o clases de fault explícitas.

#### 0.11.91r-bc. XR2-Envelope — contrato ejecutable mínimo

Para XR-2 fijamos antes del run:

\[
\mathcal A_{XR2}
=
\{\texttt{close}\},
\]

\[
\mathcal F_{XR2}
=
\{\texttt{unsupported\_input},\texttt{channel\_loss}\},
\]

\[
\mathcal N_{XR2}
=
\{\texttt{environment\_noise}\},
\]

y assumptions:

\[
\Gamma_{XR2}
=
\{
\text{component process starts},
\text{IPC endpoint exists until the classified episode terminates}
\}.
\]

La clasificación no afirma que el OS sea irrelevante. Un kill/crash que impida el episodio viola \(\Gamma\) y se registra como pérdida de realización/cessation candidate, no como una variación de \(\mathcal N\).

Para fortalecer RE3/RE5, XR-2 debe ejecutar tres familias:

1. **normal:** close produce \(s_1\) + activate;
2. **negative control:** cambia environment_noise sin cambiar la traza;
3. **fault arm:** un input no soportado produce una respuesta de error explícita y no se confunde con la transición normal.

El envelope sigue siendo **finito y relativo a \(\mathcal T_{\mathrm{IODTS}}\)**. No pretende enumerar todos los fallos físicos del ordenador.

#### 0.11.91r-bd. Theory-relative screening no es relativismo ontológico

El qualifier “relative to \(\mathcal T\)” no significa que cualquier teoría pueda declarar conveniente su exterior.

La teoría debe:

- tener una semántica independiente de component/environment interaction;
- permitir falsar su envelope;
- registrar nuevas dependencias relevantes cuando se descubren;
- mantener separadas ordinary interaction, fault/cessation e irrelevant variation.

Por tanto:

\[
\boxed{
\text{theory-relative screening}
\neq
\text{arbitrary exclusion}.
}
\]

La relación es análoga a assume/guarantee contracts: el componente garantiza ciertas conductas bajo assumptions explícitas sobre environments permisibles; una violación de assumptions no prueba la guarantee, pero tampoco puede esconderse como si fuera una variación irrelevante.

#### 0.11.91r-be. UG6 se descompone: signature rivals frente a host rivals

La noción anterior de RivalClassCompleteness mezclaba dos espacios adversariales distintos.

Definimos:

\[
\boxed{
UG6
=
UG6\text{-}S
+
UG6\text{-}H.
}
\]

**UG6-S / signature rival discrimination.** Todo rival del mismo nivel expresable mediante los constructores de la teoría formal usada para individuar \(C\) es rechazado, clasificado como equivalente o reclasificado independientemente como nesting/overlap/genesis.

**UG6-H / host rival coverage.** La realización concreta no contiene una estructura constitutivamente relevante que genere un rival del mismo nivel y que haya sido omitida por la firma formal.

Así:

\[
UG6\text{-}S
\]

es una obligación de completitud **intra-teoría**, mientras:

\[
UG6\text{-}H
\]

es una obligación de adecuación de la teoría respecto de su realizador.

No se adopta:

\[
UG6\text{-}S
\Rightarrow
UG6.
\]

#### 0.11.91r-bf. RivalGrammar de \(\mathcal T_{\mathrm{IODTS}}\)

Para el witness finito XR-2 fijamos antes de la conclusión una gramática de transformaciones rivales generada por los primitivos de la teoría:

1. **state quotient/partition:** identificar o separar estados locales;
2. **action-polarity reassignment:** reasignar cada action a input/output/internal;
3. **environment refinement:** introducir distinciones environment-side presentes en el RealizationEnvelope;
4. **closed composition:** añadir el environment al componente y obtener un sistema compuesto de orden superior;
5. **faithful recoding:** renombrar estados/actions preservando transición y polaridad.

La gramática no usa \(R_i\), RegimeTotal ni “preserva el contexto correcto” para seleccionar sus miembros.

Para XR-2 la parte combinatoria finita es explícita:

\[
3^3=27
\]

asignaciones de polaridad para:

\[
\{\texttt{close},\texttt{activate},\texttt{idle}\},
\]

dos quotients relevantes sobre \(\{s_0,s_1\}\) —identidad y merge— y un split no trivial de los dos estados.

#### 0.11.91r-bg. XR2-SIG-T — descarga de UG6-S

El script enumera las 27 asignaciones de polaridad. El control locus realizado selecciona una única asignación:

\[
\texttt{close}\mapsto in,
\qquad
\texttt{activate}\mapsto out,
\qquad
\texttt{idle}\mapsto internal.
\]

Las otras 26 contradicen quién produce/recibe efectivamente las actions en el episodio host-side.

Además:

- el quotient \(s_0\sim s_1\) borra la diferencia de enabled external profile;
- el split \(s_0|s_1\) no preserva la misma ownership/interface de la transición input-mediated;
- el refinement por environment_noise falla UG3/RE4 porque la variación queda screened-off;
- añadir \(E_H\) al component produce el **closed composition** \(E_H\oplus C_H\), candidato de orden superior, no un same-level rival del open component;
- la recodificación explícita \(s_0,s_1,\texttt{close},\texttt{activate},\texttt{idle}\mapsto q_0,q_1,\texttt{seal},\texttt{signal},\texttt{stutter}\) preserva polaridad y trace structure y queda clasificada como equivalencia.

Por tanto:

\[
\boxed{
UG6\text{-}S_{XR2}
=
\mathsf{PASS}.
}
\]

Este PASS es exhaustivo **respecto de la RivalGrammar declarada de \(\mathcal T_{\mathrm{IODTS}}\)**.

#### 0.11.91r-bh. UG6-H sigue abierto

La realización XR-2 vive sobre Python, multiprocessing, un OS y hardware. La firma I/O no enumera directamente toda estructura host-side posible.

UG6-H exige que cualquier dependencia host-side constitutivamente relevante:

1. esté absorbida por la relación de realización y preserve el mismo perfil;
2. aparezca como ordinary interaction de \(\mathcal A\);
3. aparezca como fault/lifecycle event de \(\mathcal F\);
4. o falsifique de forma observable la realization/envelope vigente.

Si aparece una dependencia que altera \(\Xi_C\) sin caer en ninguno de estos casos, XR-2 falla UG6-H hasta revisar la teoría.

Con la evidencia actual:

\[
\boxed{
UG6\text{-}H_{XR2}
=
\mathsf{PARTIAL}.
}
\]

y, por tanto:

\[
\boxed{
UG6_{XR2}
=
\mathsf{PARTIAL}.
}
\]

Esto evita dos errores opuestos: exigir una enumeración microscópica de todo el hardware o declarar completa una firma porque el modelador decidió ignorar el host.

#### 0.11.91r-bi. Estado actualizado de UnitGround para XR-2

El nuevo CIT positivo elimina el rol output y produce una pérdida observable del output constitutivo, mientras el control environment_noise deja intacta la traza. Por tanto:

\[
\boxed{
UG4_{XR2}
=
\mathsf{PASS}.
}
\]

La recodificación explícita preserva state/action typing, polaridad y estructura de trace:

\[
\boxed{
UG8_{XR2}
=
\mathsf{PASS}.
}
\]

La auditoría queda:

\[
\boxed{
\operatorname{UGAudit}_{XR2}
=
\langle
P,P,P,P,\partial,\partial,P,P
\rangle.
}
\]

con refinamiento:

\[
UG6\text{-}S=P,
\qquad
UG6\text{-}H=\partial.
\]

El cuello de XR-2 se reduce por tanto a:

\[
\boxed{
UG5
+
UG6\text{-}H.
}
\]

Ambas deudas son ahora dos caras del mismo problema: **cobertura de la relación entre firma y realizador**, no falta de una frontera operacional.

#### 0.11.91r-bj. RealizerCoverageAdequate — el bridge firma↔host

UG5 y UG6-H comparten la misma deuda: la teoría local puede ser internamente completa y, sin embargo, omitir una dependencia constitutivamente relevante presente en el realizador.

Introducimos:

\[
\boxed{
\operatorname{RealizerCoverageAdequate}^{\mathsf M}
(
\mathcal T,C,H;
\varrho,
\mathcal E
)
}
\]

donde \(\mathcal E\) es el RealizationEnvelope vigente.

No sustituye OR1–OR9. OR1–OR9 preguntan si \(H\) realiza fielmente la dinámica local. RCA pregunta además si **la abstracción ha cubierto las dependencias host-side que importan para la unidad**.

Requisitos:

1. **RCA1 / independent host theory:** la semántica relevante de \(H\) y de \(\varrho\) se fija sin ContextIndividuation/IndexAdmission;
2. **RCA2 / dependency projection:** toda dependencia host-side que la teoría del realizador reconoce como capaz de cambiar typing, interface, continuation o boundary proyecta a state/interface/fault de \(\mathcal T\), o invalida explícitamente la realización;
3. **RCA3 / no hidden constituent:** no existe un elemento/relación host-side conocido como necesario para las transiciones/roles constitutivos que sea invisible tanto a \(\varrho\) como al envelope;
4. **RCA4 / fault projection:** fallos/lifecycle events relevantes se proyectan a \(\mathcal F\) o a pérdida observable de realization; nunca a \(\mathcal N\);
5. **RCA5 / irrelevant covariance:** variaciones host-side declaradas irrelevantes y admitidas por la teoría preservan \(\Xi_C\);
6. **RCA6 / host-rival projection:** cualquier cut rival construible desde dependencias host-side reconocidas induce un rival de firma, un higher-order/nested case o una violación observable de realization/envelope;
7. **RCA7 / recoding invariance:** recodificaciones fieles del realizador preservan la clasificación de dependencias;
8. **RCA8 / falsifiability:** un counterexample host-side no proyectado reabre RCA/UG5/UG6-H en vez de ser excluido retrospectivamente.

Entonces:

\[
\boxed{
\operatorname{RealizerCoverageAdequate}
+
UG6\text{-}S
\Rightarrow
UG5
+
UG6\text{-}H.
}
\]

Por tanto:

\[
\boxed{
\operatorname{RealizerCoverageAdequate}
+
UG6\text{-}S
\Rightarrow
UG5+UG6.
}
\]

La regla no resuelve RCA; concentra la deuda sin duplicarla.

#### 0.11.91r-bk. RCA no es MC6/MC7 renombrado

MC6 y MC7 operan en la candidatura pre-indexada:

- MC6 exige cobertura de roles/interacciones relevantes;
- MC7 exige screening-off contrafactual respecto del nivel declarado.

RCA añade una obligación **inter-level**:

\[
H
\xrightarrow{\varrho}
C.
\]

Pregunta si la teoría que justifica el paso host→local es suficientemente completa para sostener precisamente MC6/MC7 y UG5/UG6-H.

Por tanto:

\[
\boxed{
MC6/MC7
\text{ son obligaciones locales;}
\qquad
RCA
\text{ es la auditoría del bridge de realización.}
}
\]

Si el realizador se tratara como mero “hardware irrelevante” sin RCA, el programa reintroduciría por debajo el mismo no-free-promotion que intenta bloquear por arriba.

#### 0.11.91r-bl. RCA-XR2 — auditoría actual

Para XR-2:

\[
H_{XR2}
=
\text{Python process pair + multiprocessing IPC + runtime/OS realization}.
\]

Estado:

\[
\begin{array}{lll}
RCA1 & \mathsf{PASS} &
\text{la semántica process/IPC y la firma I/O se fijan independientemente};\\
RCA2 & \mathsf{PARTIAL} &
\text{channel, output-role break y unsupported input están proyectados; no toda dependencia runtime/OS};\\
RCA3 & \mathsf{PARTIAL} &
\text{no se ha probado ausencia de hidden constituents del runtime/OS};\\
RCA4 & \mathsf{PARTIAL} &
\text{unsupported input se clasifica como fault; lifecycle/channel-loss coverage no está agotada};\\
RCA5 & \mathsf{PASS} &
\text{environment_noise y la recodificación fiel preservan el profile};\\
RCA6 & \mathsf{PARTIAL} &
\text{UG6-S pasa, pero no todo host rival conocido está probado proyectable};\\
RCA7 & \mathsf{PASS} &
\text{state/action recoding preserva polaridad y trace structure};\\
RCA8 & \mathsf{PASS} &
\text{RE7 y los guards obligan a reabrir ante bypass reproducible}.
\end{array}
\]

Así:

\[
\boxed{
\operatorname{RCAAudit}_{XR2}
=
\langle
P,\partial,\partial,\partial,P,\partial,P,P
\rangle.
}
\]

El resultado explica por qué añadir más tests de firma tiene rendimiento decreciente: la deuda restante ya no está dentro del autómata.

#### 0.11.91r-bm. Teorema de cuello de botella XR-2

Con las descargas actuales:

\[
UG1,UG2,UG3,UG4,UG7,UG8
=
\mathsf{PASS},
\]

y:

\[
UG6\text{-}S
=
\mathsf{PASS}.
\]

Por §0.11.91r-bj, cerrar RCA bastaría para descargar simultáneamente:

\[
UG5
\quad\text{y}\quad
UG6\text{-}H,
\]

y por tanto:

\[
\boxed{
\operatorname{RealizerCoverageAdequate}_{XR2}
\Rightarrow
\operatorname{UnitGroundAdequate}_{XR2}.
}
\]

Esto **no** equivale a:

\[
\operatorname{RealizerCoverageAdequate}_{XR2}
\Rightarrow
\operatorname{ExistsR},
\]

porque todavía deben mantenerse las demás obligaciones de IndAdequate, IndexAdmission y RegimeTotal del witness correspondiente.

El research target queda reducido de “qué es una unidad contextual” a una pregunta mucho más concreta para XR-2:

> ¿puede una relación de realización host→component descargarse con cobertura suficiente sin exigir una descripción microscópicamente total del host ni esconder dependencias constitutivas?

#### 0.11.91r-bn. RCA-X1 — ninguna batería finita prueba ausencia universal de hidden constituents

Sea:

\[
\Delta
=
\{\delta_1,\ldots,\delta_n\}
\]

una batería finita de intervenciones sobre un realizador \(H\), y supongamos que todas proyectan correctamente a la teoría local o preservan el perfil.

Construimos dos realizadores:

\[
H
\qquad\text{y}\qquad
H^{+z},
\]

tales que:

1. son observacionalmente indistinguibles bajo toda \(\delta_k\in\Delta\);
2. inducen exactamente la misma traza local y los mismos certificados para la batería;
3. \(H^{+z}\) contiene una dependencia adicional \(z\) no activada por ninguna \(\delta_k\);
4. existe una intervención \(\delta_z\notin\Delta\) bajo la cual \(z\) altera una parte constitutiva de \(\Xi_C\) sin estar proyectada por \(\varrho\) ni clasificada por el envelope.

Entonces:

\[
\forall \delta\in\Delta:
\operatorname{Obs}_{\delta}(H)
=
\operatorname{Obs}_{\delta}(H^{+z}),
\]

pero RealizerCoverageAdequate puede tener distinto valor en ambos realizadores.

Por tanto:

\[
\boxed{
\text{finite intervention success}
\not\Rightarrow
\operatorname{RealizerCoverageAdequate}.
}
\]

Esto no convierte los tests en inútiles: pueden **falsar** RCA y descargar familias concretas, pero no establecer por enumeración finita la ausencia de toda dependencia oculta.

#### 0.11.91r-bo. RCA-T1 — hace falta una teoría del realizador, no infinitos tests

Para cerrar RCA introducimos una teoría independiente del realizador:

\[
\mathcal H
=
\langle
Q_H,
\Lambda_H,
\to_H,
\mathsf{Dep}_H,
\mathsf{Fault}_H
\rangle.
\]

No tiene que ser una microfísica total. Debe cubrir el vocabulario host-side que se afirma relevante para la realización actual.

Definimos:

\[
\boxed{
\operatorname{HostProjectionComplete}^{\mathsf M}
(
\mathcal H,\mathcal T,H;
\varrho,\mathcal E
)
}
\]

si toda transición/dependencia admitida por \(\mathcal H\) cae en una clase predefinida:

1. **HPC1 / local step:** proyecta a una transición de \(\mathcal T\);
2. **HPC2 / interface step:** proyecta a una interacción de \(\mathcal A\);
3. **HPC3 / stutter:** preserva \(\Xi_C\) y pertenece a \(\mathcal N\) o a una equivalencia de realización;
4. **HPC4 / fault/lifecycle:** proyecta a \(\mathcal F\) o pérdida observable de realización;
5. **HPC5 / recoding/refinement:** cambia implementación sin cambiar el perfil abstracto;
6. **HPC6 / no residual relevant step:** no queda una transición/dependencia que altere \(\Xi_C\) fuera de HPC1–HPC5.

Además:

- **HPC7 / independent grammar:** las clases de \(\mathcal H\) se fijan sin usar el éxito de \(C\);
- **HPC8 / counterexample openness:** una nueva transición host-side reproducible no cubierta invalida HostProjectionComplete hasta revisar \(\mathcal H\).

Entonces:

\[
\boxed{
\operatorname{HostTheoryAdequate}(\mathcal H,H)
+
\operatorname{HostProjectionComplete}
\Rightarrow
\operatorname{RealizerCoverageAdequate}.
}
\]

La carga se desplaza correctamente desde “hemos probado muchos casos” a “tenemos una abstracción host→local cuya cobertura puede auditarse”.

#### 0.11.91r-bp. No-Microscopic-Totality — RCA no exige describir todos los microestados

HostTheoryAdequate no significa que \(\mathcal H\) enumere cada transistor, scheduler tick o estado físico.

La obligación relevante es más estrecha:

\[
\boxed{
\text{todo factor reconocido como constitutivamente capaz de alterar }\Xi_C
\text{ debe proyectar o invalidar la realización.}
}
\]

Los detalles microfísicos pueden quedar quotientados cuando la teoría independiente del host justifica que, respecto del perfil:

\[
h_1\sim_{\varrho,\mathcal E} h_2.
\]

Por tanto:

\[
\boxed{
\text{realizer coverage}
\neq
\text{microscopic totality}.
}
\]

Pero la equivalencia tampoco se decreta. Si un detalle previamente quotientado produce un UnitProfileBreak reproducible, HPC8 obliga a refinar la teoría.

Este principio evita una regresión infinita puramente epistemológica: cada nivel de realización puede usar una teoría independently grounded y falsable sin pretender agotar físicamente su sustrato.

#### 0.11.91r-bq. Relación con abstract interpretation y equivalencia conductual

La forma de HostProjectionComplete tiene precedentes formales claros:

- abstract interpretation permite describir computaciones concretas en un dominio abstracto conservando la información relevante para las propiedades objetivo;
- simulation/bisimulation-style relations permiten demostrar que pasos concretos y abstractos preservan una conducta observacional seleccionada;
- I/O/interface theories añaden la distinción sistema/entorno necesaria para no confundir stutter interno con interacción exterior.

Exergism añade una exigencia propia: la propiedad preservada no es solo comportamiento observable, sino el **pre-index unit profile** usado por IA0-U.

Por tanto no se infiere:

\[
\text{sound abstraction}
\Rightarrow
\text{ContextIndividuation}.
\]

La inferencia permitida es únicamente:

\[
\text{sound host projection}
\Rightarrow
\text{evidence para RCA},
\]

dentro del resto de UnitGroundAdequate.

#### 0.11.91s. Generaciones contextuales: profundidad ontogénica, no totalidad

La nueva lectura de contextos anidados permite introducir una distinción que no estaba disponible cuando \(R\) se trataba como si tuviera que ser una totalidad maximal.

Una realidad/contexto puede ser **original** o puede depender ontogénicamente de otros contextos.

Definimos primero la relación parental:

\[
\boxed{
\operatorname{CtxParent}^{\mathsf M}
(
p,k;\gamma
)
}
\]

cuando existe una GenuineContextGenesis que constituye \(k\) y \(p\) pertenece a la familia de precursores **constitutivamente necesarios** de esa génesis.

Por tanto:

\[
\operatorname{CtxParent}(p,k;\gamma)
\Rightarrow
p\prec_{\mathrm{ctx}} k.
\]

La conversa no se adopta si \(\prec_{\mathrm{ctx}}\) se usa en algún pasaje con sentido más débil de precursor/provenance.

No generan parentalidad contextual por sí solos:

\[
\operatorname{ContextEmbedding},
\quad
\operatorname{FaithfulContinuation},
\quad
\operatorname{Bake},
\quad
\operatorname{SharedOntSpace}.
\]

En particular:

\[
j\hookrightarrow k
\not\Rightarrow
\operatorname{CtxParent}(k,j)
\]

y:

\[
j\hookrightarrow k
\not\Rightarrow
\operatorname{CtxParent}(j,k).
\]

**Generación mide génesis, no nesting.**

#### 0.11.91t. Generación 0: realidad original

Introducimos un juicio theory-relative de originalidad:

\[
\boxed{
\operatorname{OriginaryContext}^{\mathsf M}_{\mathcal T}
(
i;\zeta
)
}
\]

donde \(\zeta\) debe satisfacer **OG1–OG6**.

**OG1 — admitted context.** \(i\) ya ha satisfecho ContextIndividuation/IndexAdmission por una ruta independiente. Ser Gen0 no crea el índice.

**OG2 — independent root ground.** La teoría aporta un fundamento positivo para la unidad de \(i\) que no depende de una ContextGenesis parental.

**OG3 — parent completeness.** La teoría posee suficiente cobertura genealógica para que la ausencia de padres contextuales no sea mera ausencia de información.

**OG4 — no hidden negative inference.**

\[
\neg\exists\gamma,p\;
\operatorname{KnownCtxParent}(p,i;\gamma)
\]

no basta para OriginaryContext.

**OG5 — recoding invariance.** Recodificaciones fieles preservan la clasificación de originalidad.

**OG6 — no totality/maximality.** Ser original no implica ser maximal, contener todos los demás contextos, agotar lo real ni ser único.

Definimos entonces:

\[
\boxed{
\operatorname{Generation}^{\mathsf M}_{\mathcal T}(i,0)
:\Longleftrightarrow
\operatorname{OriginaryContext}^{\mathsf M}_{\mathcal T}(i;\zeta)
}
\]

para algún witness \(\zeta\) adecuado.

Ésta es la lectura precisa de **realidad de generación 0**.

Puede haber:

\[
R_i^{[0]},
\qquad
R_j^{[0]},
\qquad
R_k^{[0]}
\]

sin que exista una entidad superior que los reúna.

La notación:

\[
R_i^{[0]}
\]

es solo una anotación metateórica:

\[
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
+
\operatorname{Generation}(i,0).
\]

No añade un nuevo tipo objeto.

En este sentido, la intuición histórica del \(R\) “original” encuentra un sucesor más preciso en \(R_i^{[0]}\): **una realidad no derivada de otra realidad contextual**, no “la totalidad de todo lo real”.

#### 0.11.91u. Rank generacional finito

Sea una GenuineContextGenesis de \(k\) con familia parental completa:

\[
\mathcal P_k
=
\{p_1,\ldots,p_m\}.
\]

Si todos los padres tienen rank finito:

\[
\operatorname{Generation}(p_r,n_r),
\]

definimos:

\[
\boxed{
\operatorname{Generation}(k,n)
}
\]

con:

\[
\boxed{
n
=
1+\max_{1\le r\le m} n_r.
}
\]

Para una génesis unaria:

\[
\operatorname{Generation}(p,n)
+
\operatorname{CtxParent}(p,k)
\Rightarrow
\operatorname{Generation}(k,n+1).
\]

Para dos Gen0:

\[
0+0
\overset{\text{genesis}}{\longrightarrow}
1.
\]

Para un Gen0 y un Gen1:

\[
0+1
\overset{\text{genesis}}{\longrightarrow}
2.
\]

El uso de \(\max+1\) garantiza:

\[
\boxed{
\operatorname{CtxParent}(p,k)
\Rightarrow
\operatorname{GenRank}(p)
<
\operatorname{GenRank}(k).
}
\]

Así el rank mide la **máxima profundidad ontogénica requerida** por la existencia contextual actual.

No cuenta tiempo cronológico ni distancia espacial.

#### 0.11.91v. GR1–GR8: cuándo el rank está bien definido

Definimos:

\[
\operatorname{GenerationAdequate}^{\mathsf M}_{\mathcal T}
(
i;n,\omega
)
\]

con **GR1–GR8**.

**GR1 — grounded genesis.** Cada arista parental usada en el rank procede de GenuineContextGenesis, no de semejanza, causalidad, embedding o coexistencia.

**GR2 — complete parent family.** La familia parental usada por cada génesis contiene todos los contextos constitutivamente necesarios según la teoría.

**GR3 — rival genealogy discipline.** Si dos reconstrucciones adecuadas de la génesis del mismo contexto producen parent families incompatibles, el rank queda unresolved hasta demostrar equivalencia, nesting genealógico explícito o descartar al menos una.

**GR4 — well-foundedness.** El componente genealógico rankeado no contiene ciclos de dependencia parental. Una teoría que permita genealogías no well-founded necesita una semántica distinta; no se le asigna fraudulentamente un natural.

**GR5 — no unknown-to-zero.** Falta de provenance o Muro genealógico no autorizan Gen0.

**GR6 — witness invariance.** Dos witnesses equivalentes de la misma génesis inducen el mismo rank.

**GR7 — no embedding depth substitution.** La profundidad de ContextEmbedding no entra en el cálculo del rank generacional.

**GR8 — no complexity inflation.** El rank no se interpreta como número de piezas, sofisticación, información, valor o tamaño.

Si GR1–GR8 no pueden descargarse:

\[
\operatorname{GenerationUnresolved}^{\mathsf M}_{\mathcal T}(i)
\]

es la clasificación correcta.

#### 0.11.91w. Firma generacional: el número no basta

El rank:

\[
n
\]

colapsa información relevante. Dos contextos Gen2 pueden proceder de genealogías muy distintas.

Definimos por ello una **GenerationSignature**:

\[
\boxed{
\operatorname{GenSig}^{\mathsf M}_{\mathcal T}(k)
=
\left\langle
n_k,
\mu_k,
\mathsf{ParSpec}_k,
\nu_k
\right\rangle.
}
\]

Donde:

- \(n_k\) es el rank;
- \(\mu_k\) es el modo de génesis: originary, unary, multi-parent, y subtipos theory-specific como ContextMerger cuando estén justificados;
- \(\mathsf{ParSpec}_k\) es el multiset/espectro de ranks parentales:

\[
\mathsf{ParSpec}_k
=
[n_1,\ldots,n_m];
\]

- \(\nu_k\) registra únicamente patrones de persistencia parental positivamente certificados —por ejemplo qué parents satisfacen PersistentParent—, sin inferir cesación de los demás por silencio.

Así pueden distinguirse:

\[
\mathrm{Gen1}
\langle
multi,[0,0]
\rangle
\]

de:

\[
\mathrm{Gen1}
\langle
unary,[0]
\rangle,
\]

y:

\[
\mathrm{Gen2}
\langle
multi,[0,1]
\rangle
\]

de:

\[
\mathrm{Gen2}
\langle
unary,[1]
\rangle.
\]

La generación tiene por tanto **altura** y **geometría**.

#### 0.11.91x. Escala de simplicidad ontogénica

El rank induce una noción restringida de simplicidad:

\[
\boxed{
i
\prec_{\mathrm{gen}}
j
:\Longleftrightarrow
\operatorname{GenRank}(i)
<
\operatorname{GenRank}(j).
}
\]

La lectura correcta es:

> \(i\) requiere menos capas de ContextGenesis en su provenance constitutiva que \(j\).

Por tanto Gen0 es minimal en **profundidad genealógica contextual**.

Pero no se deriva:

\[
\operatorname{GenRank}(i)
<
\operatorname{GenRank}(j)
\Rightarrow
\operatorname{StructuralComplexity}(i)
<
\operatorname{StructuralComplexity}(j).
\]

Una realidad Gen0 puede contener una dinámica enormemente compleja y una Gen4 ser operacionalmente trivial.

Por eso “escala de simplicidad” solo es válida como abreviatura de:

\[
\boxed{
\text{ontogenic dependency depth}.
}
\]

#### 0.11.91y. Generación y nesting son coordenadas ortogonales

La nueva arquitectura permite distinguir situaciones que antes quedaban mezcladas.

Puede ocurrir:

\[
j\hookrightarrow k
\]

con:

\[
\operatorname{GenRank}(j)
=
\operatorname{GenRank}(k),
\]

si dos contextos de la misma generación quedan embebidos por una relación posterior no constitutiva.

También puede ocurrir:

\[
j\hookrightarrow k,
\qquad
\operatorname{GenRank}(j)
>
\operatorname{GenRank}(k),
\]

por ejemplo cuando un contexto de generación alta se realiza dentro de un host genealógicamente más básico.

O:

\[
j\hookrightarrow k,
\qquad
\operatorname{GenRank}(j)
<
\operatorname{GenRank}(k),
\]

si el host es él mismo resultado de una ontogénesis más profunda.

Por tanto:

\[
\boxed{
\text{generation depth}
\neq
\text{embedding depth}.
}
\]

Un host solo cuenta como parent de un contexto embebido si participó **constitutivamente** en la ContextGenesis de ese contexto.

Esto proporciona una segunda coordenada para la Cellular Reality:

\[
\boxed{
\text{contextual position}
\sim
\left\langle
\text{generation},
\text{embedding relations},
\text{generation signature}
\right\rangle.
}
\]

No es una dirección objeto ni convierte índices en puntos de un espacio.

#### 0.11.91z. Root theorem y generaciones derivadas

Para cualquier contexto con rank finito:

\[
\operatorname{Generation}(k,n),
\]

si \(n>0\), existe al menos una cadena parental:

\[
p_0
\prec_{\mathrm{ctx}}
p_1
\prec_{\mathrm{ctx}}
\cdots
\prec_{\mathrm{ctx}}
p_n=k
\]

tal que:

\[
\operatorname{Generation}(p_r,r)
\]

tras elegir una rama de profundidad máxima.

Por inducción:

\[
\boxed{
\operatorname{Generation}(k,n)
\Rightarrow
\exists^{\mathsf M}p_0\;
[
\operatorname{Generation}(p_0,0)
\land
p_0\prec_{\mathrm{ctx}}^{*}k
].
}
\]

Esto no dice que haya **una** raíz universal.

Puede haber múltiples Gen0 y una generación multiparental puede reunir linajes procedentes de varias de ellas.

La consecuencia conceptual es exactamente:

\[
\boxed{
\text{las generaciones derivadas son genealogías de interacción entre realidades originales.}
}
\]

#### 0.11.91aa. Stress tests generacionales

**GN-S1 — unknown ancestry = Gen0.** No conocemos ningún parent de \(i\), luego se declara Gen0. Falla OG3/GR5.

**GN-S2 — embedding counted as parent.** Un servicio \(j\) corre dentro de host \(k\), luego se pone \(Gen(j)=Gen(k)+1\). Falla GR1/GR7 salvo que exista una ContextGenesis constitutiva independiente.

**GN-S3 — interaction without genesis.** Dos Gen0 interactúan dentro de SharedOntSpace. No aparece Gen1 por la mera interacción:

\[
\operatorname{interaction}
\not\Rightarrow
\operatorname{ContextGenesis}.
\]

Solo una interacción que constituya un nuevo contexto genera nueva generación.

**GN-S4 — multi-parent flattening.** Dos Gen2 tienen el mismo rank pero parent spectra distintos. El rank coincide; GenSig los distingue.

**GN-S5 — complexity confusion.** Una Gen0 físicamente complejísima se declara “menos compleja” que una Gen3 simple. Solo puede afirmarse menor ontogenic dependency depth.

**GN-S6 — hidden cycle.** \(i\) se usa como ancestor de \(j\) y \(j\) como ancestor constitutivo de \(i\). Falla GR4; no se asigna rank natural.

**GN-S7 — universal root smuggling.** De que todo contexto rankeado tenga algún Gen0 ancestor se infiere una única realidad original. No se sigue: varias raíces son compatibles con toda la arquitectura.

#### 0.11.91ab. Estado de la hipótesis generacional

La hipótesis queda formalizada sin tocar ExistsR:

\[
\operatorname{ExistsR}
\]

sigue afirmando únicamente que existe al menos un contexto con RegimeTotal.

Introducimos opcionalmente:

\[
\boxed{
\operatorname{ExistsGen0R}
:\Longleftrightarrow
\exists^{\mathsf M}i\;
\exists\mathfrak G_i\exists R_i[
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
\land
\operatorname{Generation}(i,0)
].
}
\]

No se adopta:

\[
\operatorname{ExistsR}
\Rightarrow
\operatorname{ExistsGen0R}
\]

sin una hipótesis de well-foundedness/completitud genealógica suficiente.

La ganancia doctrinal es otra: una vez admitida la pluralidad y nesting de contextos, **Generation** permite estratificarlos por dependencia ontogénica sin volver a una totalidad global.

La intuición del antiguo \(R\) se conserva mejor como:

\[
\boxed{
R_i^{[0]}
=
\text{realidad contextual original}
}
\]

y las demás realidades se clasifican por cómo emergen genealógicamente de interacciones constitutivas entre contextos anteriores.

#### 0.11.91ac. XR-1 — witness mínimo ejecutable para \(\operatorname{ExistsR}\)

La definición vigente de ExistsR es existencial. Por tanto no exige cerrar REV-07b/c/d universalmente: basta una instancia concreta en la que sus obligaciones queden descargadas.

XR-1 es una máquina software finita:

\[
s_0\xrightarrow{e_0}s_1.
\]

XR-1 **no introduce una teoría ontológica ad hoc propia**. Se interpreta como una instancia mínima de \(\mathcal T_{\mathrm{DTS}}\), la teoría ordinaria de sistemas de transición deterministas finitos: un conjunto tipado de states, un alfabeto de events y una función/relación de transición parcial. La motivación y semántica de \(\mathcal T_{\mathrm{DTS}}\) son independientes del objetivo ExistsR; XR-1 solo selecciona su instancia no trivial mínima.

En esa teoría operacional pre-indexada se fija primero, independientemente de GenEvent, una única instancia productiva actual:

\[
\operatorname{ProcessProd}(e_0,\{s_0\},s_1),
\]

con footprint:

\[
\{s_0,e_0,s_1\}.
\]

El inventario formal contiene exactamente:

\[
\operatorname{GenEvent}(e_0,\{s_0\},s_1).
\]

El script `scripts/xr1_witness.py` ejecuta realmente el episodio, compara OntProd operacional con GenEvent, calcula la closure y emite un certificado que CI conserva como artifact.

Esto no convierte ejecución en ontología por sintaxis. Separa el núcleo formal-operacional de la descarga metaontológica.

#### 0.11.91ad. XR1-F — descarga formal/generativa

Tomamos:

\[
\mathcal O_{\mathrm{XR1}}=\{s_0\}.
\]

OriginUnity es vacua respecto de particiones no triviales del singleton. RootClosed vale porque la teoría local no contiene OntProd con target \(s_0\). La producción host-side del proceso no se reescribe como OntProd interno.

La relación productiva y el inventario generativo coinciden extensionalmente, pero están especificados por rutas distintas:

\[
\mathsf{OntProd}_{XR1}
=
\mathsf{GenEvent}_{XR1}
=
\{\langle e_0,\{s_0\},s_1\rangle\}.
\]

Por exhaustión finita:

\[
\boxed{\mathrm{GenSound}_{XR1}\land\mathrm{GenComplete}_{XR1}.}
\]

El operador satisface:

\[
\Gamma(\{s_0\})=\{s_0,e_0,s_1\}
\]

y:

\[
\Gamma(\{s_0,e_0,s_1\})=\{s_0,e_0,s_1\}.
\]

Todo fixed point que contiene \(s_0\) contiene el footprint completo. Luego:

\[
\boxed{
\operatorname{GenClosure}
(
\mathcal O_{XR1},
C_{XR1}
)
}
\]

con:

\[
C_{XR1}=\{s_0,e_0,s_1\}.
\]

Así GCExists queda demostrado para esta instancia finita, aunque REV-07c siga abierto universalmente. El singleton no posee subconfiguración originaria propia no vacía con la misma closure, luego Irredundant vale. Por tanto OntOrigin y GeneUnit quedan descargados para XR-1.

#### 0.11.91ae. XR1-R — realidad local independiente de la closure

Sea \(a\) una ejecución concreta. La semántica operacional fija independientemente:

\[
\operatorname{ExecToken}_{\mathcal T_{DTS}}(a,x)
\]

cuando \(x\) ocurre efectivamente como state/event token local.

El run ejecutado tiene:

\[
\operatorname{ExecTokens}(a)=\{s_0,e_0,s_1\}.
\]

Definimos:

\[
\operatorname{Real}^{a}_{XR1}(x)
\Longleftrightarrow
\operatorname{ExecToken}_{\mathcal T_{DTS}}(a,x).
\]

Esto no menciona GenClosure. Independientemente:

\[
C_{XR1}=\{s_0,e_0,s_1\}.
\]

Luego:

\[
\boxed{
\operatorname{Real}^{a}_{XR1}(x)
\Longleftrightarrow
x\in C_{XR1}.
}
\]

#### 0.11.91af. XR1-S — scope finito

XR-1 no necesita comprensión irrestricta. Introducimos directamente el plural finito:

\[
rr_{XR1}=s_0,e_0,s_1
\]

con:

\[
x\prec rr_{XR1}
\Longleftrightarrow
x=s_0\lor x=e_0\lor x=s_1.
\]

Entonces:

\[
x\prec rr_{XR1}
\Longleftrightarrow
\operatorname{Real}^{a}_{XR1}(x)
\Longleftrightarrow
x\in C_{XR1}.
\]

Escribimos \(R_{XR1}\) para ese scope plural sin convertirlo en objeto colector.

#### 0.11.91ag. XR1-C — descarga TR-M e IndAdequate

La candidatura dispone pre-indexadamente de typing local State/Event, transición operacional, frontera de proceso, interfaces de boot/termination y estado reentrante.

Bajo la teoría independiente \(\mathcal T_{\mathrm{DTS}}\), MC1–MC10 se descargan: la especificación no usa el índice; typing y boundary son positivos; toda influencia admitida entra por interfaces declaradas; el update es determinista; no hay roles/interacciones omitidos; fijado estado + inputs el futuro lógico queda determinado; no existe agregación arbitraria; el host puede ser otro contexto vía ContextEmbedding; y genesis/persistence permanecen separados.

Además XR-1 permite auditar **IA1–IA10** sin introducir el target como premisa:

- **IA1:** \(\mathcal T_{\mathrm{DTS}}\) es una teoría matemática/operacional general anterior e independiente de XR-1; la instancia fue elegida por minimalidad, no para fabricar su frontera.
- **IA2:** ninguna regla DTS menciona \(R_i\), RegimeTotal, REC, SameRegime ni un índice admitido.
- **IA3:** el corte está positivamente grounded por sorts, transición y realization boundary.
- **IA4:** OR6 y el test de recoding covariance preservan la individuación bajo codificación fiel.
- **IA5:** los grados host-side ignorados por \(\varrho\) deben quedar contrafácticamente screened-off; si afectan la transición local, OR4/MC4 fallan.
- **IA6:** XR-1 posee una sola máquina transitionally integrated; juntar otra máquina independiente no hereda el criterio.
- **IA7:** boot/formation del realizador se distingue de sus pasos internos; la transición \(s_0\to s_1\) no se usa para explicar retroactivamente la existencia del contexto.
- **IA8:** el corte local y el host son niveles nested, no rival cuts del mismo nivel.
- **IA9:** ContextIndividuation no basta para scope; XR1-S descarga el scope por separado.
- **IA10:** OR/MC/XR-A1–A7 identifican explícitamente qué haría fallar la individuación.

Queda entonces concentrada IA0 en la realización estructural actual:

\[
\boxed{
\operatorname{ActualStructuralRealization}^{\mathsf M}
(
H,C;\varrho
)
:=
\operatorname{Obtains}^{\mathsf M}(H)
\land
\operatorname{StructuralRealization}^{\mathsf M}(H,C;\varrho),
}
\]

donde StructuralRealization abrevia OR2–OR9.

El script XR-1 verifica mecánicamente OR2–OR9 sobre un host realizer distinto del autómata local y aporta evidencia de que el paso host fue efectivamente ejecutado.

#### 0.11.91ah. XR1-REAL — realización actual y principio de suficiencia

El run de CI es evidence, no truthmaker. El truthmaker candidato es una estructura host-side efectiva:

\[
\operatorname{ActualStructuralRealization}^{\mathsf M}
(
H_a,C_{XR1};\varrho_a
).
\]

Para XR-1, el realizer host contiene estructura adicional que no pertenece al contexto local —por ejemplo irrelevant_noise— y:

\[
\varrho_a:
H_a
\to
\{s_0,s_1,e_0\}
\]

es many-to-one respecto de esa estructura. Esto descarga OR7 y evita identificar modelo y realizador.

La verificación ejecutable comprueba:

\[
\boxed{
\begin{array}{ll}
OR2 &: \text{typed realization},\\
OR3 &: \varrho_a\circ T_H=T_C\circ\varrho_a,\\
OR4 &: \text{screening-off de variación irrelevante + sensibilidad relevante},\\
OR5 &: \varrho_a\text{ no depende del certificado},\\
OR6 &: \text{covariancia bajo recodificación fiel},\\
OR7 &: \text{no colapso host/local},\\
OR8 &: \text{proyección state/prefix-local},\\
OR9 &: \text{mapping predeclarado, no ajustado post hoc}.
\end{array}
}
\]

El paso efectivamente ejecutado aporta evidencia de OR1/Obtains. Por WitnessCovariance, ningún certificado concreto entra en la conclusión.

Aquí queda expuesta la parte **realizacional** de IA0:

\[
\boxed{
\mathrm{RSP\text{-}R}
:
\operatorname{ActualStructuralRealization}(H,C;\varrho)
+
\operatorname{MCAdequate}(C)
\Rightarrow
IA0\text{-}R(C).
}
\]

**RSP-R — Realization Support Principle** dice únicamente que una estructura local cuya dinámica y typing están efectivamente realizados, contrafácticamente soportados y covariantemente preservados no es una mera ficción descriptiva.

La antigua conclusión:

\[
\operatorname{ActualStructuralRealization}
+
\operatorname{MCAdequate}
\Rightarrow
IA0
\]

queda **SUPERSEDED** por §§0.11.91r-v–z. OR2–OR9 + MC1–MC10 pueden establecer realization y autonomía estructural; todavía falta UnitGroundAdequate para mostrar que esa estructura es unity-making para el cut exacto.

Por tanto:

\[
\boxed{
\mathrm{RSP\text{-}R}
+
\mathrm{XR1\text{-}REAL}
+
\mathrm{MCAdequate}
+
\operatorname{UnitGroundAdequate}_{XR1}
+
IA1\text{--}IA10
\Rightarrow
\operatorname{ContextIndividuation}^{\mathsf M}(C_{XR1}).
}
\]

#### 0.11.91ai. XR1-T — teorema existencial condicional

Tras IndexAdmission tomamos la familia singleton:

\[
\mathfrak G_{XR1}
=
\{\langle\mathcal O_{XR1},C_{XR1}\rangle\}.
\]

Por el singleton compatibility theorem, XR1-F/R/S descargan:

\[
\operatorname{RegimeTotal}_{i_{XR1}}
(
\mathfrak G_{XR1},
R_{XR1}
).
\]

Por tanto:

\[
\boxed{
\mathrm{RSP\text{-}R}
+
\mathrm{XR1\text{-}REAL}
+
\operatorname{UnitGroundAdequate}_{XR1}
+
\mathrm{IndAdequate}_{XR1}
\Rightarrow
\operatorname{ExistsR}.
}
\]

REV-07b/c permanecen abiertos universalmente, pero no bloquean este existential witness porque GenComplete y GCExists han sido probados por exhaustión finita para XR-1.

#### 0.11.91aj. Ataques adversariales

**XR-A1 — Real definido como closure.** No: Real se fija por ExecToken y la coincidencia se demuestra después.

**XR-A2 — GenComplete tautológico.** No: ProcessProd procede de la semántica operacional y GenEvent se audita contra ella.

**XR-A3 — singleton origin trivial.** Hace vacua OriginUnity, pero no RootClosed, GenAdequate, GCExists, Irredundant, ContextIndividuation ni scope exactness. El contrato vigente no prohíbe orígenes singleton.

**XR-A4 — tokens físicos ocultos.** Pertenecen al host salvo que la teoría los tipifique como locales. Si son constitutivamente necesarios al nivel declarado, XA3/XA5 obliga a incorporarlos y XR-1 debe rehacerse.

**XR-A5 — software no es realidad.** La objeción solo derrota XR-1 si muestra que no existe una realización OR1–OR9 del nivel local en el proceso host. Una prohibición nominal contra «software» no basta; tampoco basta afirmar realizabilidad sin exhibir structural/dynamical support.

**XR-A6 — CI no prueba metafísica.** Correcto. CI proporciona un evidence witness reproducible; no es el truthmaker. La carga ontológica está en XR1-REAL/OR1–OR9 + IndAdequate.

**XR-A7 — scope setificado.** No: \(rr_{XR1}\) es plural finito explícito.

#### 0.11.91ak. Estado de XR-1

XR-1 demuestra un **witness formal/generativo + ejecución actual + realized modal support**. Eso ya no se presenta como suficiente para ExistsR.

La máquina/CI descargan el núcleo formal, OR2–OR9 y evidencia reproducible de OR1 para un run. IA1–IA10 quedan auditadas contra la teoría independiente DTS. Tras el ataque IA0, la deuda filosófica restante es **IA0-U / UnitGroundAdequate**: mostrar que la estructura local realizada es la que constituye/discrimina la unidad contextual exacta y no solo un real pattern eficaz.

Por tanto ExistsR sigue siendo **FORMAL-CONDITIONAL** respecto de ese bridge de unidad.

#### 0.11.92. Relación con \(\Omega_i\): ContinuationProfile ya no depende de \(\Omega_i\)

REV-07e había dejado abierta una ruta provisional en la que \(\Omega_i\) podía anteceder a ContinuationProfile. Esa dirección queda ahora **SUPERSEDED**: §§0.11.91a–0.11.91i derivan \(\mathsf{CP}_i^x\) directamente desde PersistenceBasis + contract state + memo-equivalence + quotient dynamics.

Por tanto no se usa:

\[
\Omega_i
\Longrightarrow
\operatorname{ContinuationProfile}_i.
\]

La pregunta restante va en la dirección opuesta. Si una teoría dispone de una familia independently grounded de PersistenceBases y perfiles:

\[
\left\{
\mathsf{CP}_i^x
\right\}_{x\in\mathcal U_i},
\]

coordinada con estructura generativa y Bakes admisibles, puede investigarse si existe alguna canonicalización conjunta:

\[
\Omega_i
\stackrel{?}{\simeq}
\operatorname{Can}
\left(
\text{generative structure},
\{\mathsf{CP}_i^x\},
\text{admissible Bake/Prov data}
\right).
\]

No se adopta esta igualdad como definición. Permanecen al menos cuatro deudas:

1. qué familia de PersistenceBases/perfiles es suficiente para una firma de contexto y no meramente para units locales;
2. cómo canonicalizar perfiles branching, interaction roles y transformaciones sin borrar estructura generativa relevante;
3. si existe una normal form canónica bajo recoding y Bakes admisibles;
4. cómo coordinar esa canonicalización con provenance y ContextIndividuation sin usar \(\Omega_i\) retroactivamente.

La ruta de dependencia admisible sería:

\[
\boxed{
\chi
\to
i
\to
\text{estructura generativa/iterativa}
\to
\operatorname{PersistenceBasis}
\to
\operatorname{ContinuationProfile}
\to
\text{auditoría de continuidad/baking}
\to?
\Omega_i.
}
\]

\(\Omega_i\) sigue sin poder usarse retroactivamente para crear la individuación inicial de \(i\).

#### 0.11.93. Stress tests de REV-07h

**MB1 — hash collision.** Dos historias reciben el mismo código pero existe \(c_i\in\mathcal K_{i,\rho}\) que las distingue. Falla M5/M6. No existe memo-equivalence aunque la representación colisione.

**MB2 — rol vacío.** Se toma \(\mathcal K_{i,\rho}=\varnothing\), por lo que todas las historias resultan vacuamente equivalentes. Falla RoleAdequate/M2. La memoization trivial no individúa nada.

**MB3 — rol post hoc.** Después de observar dos histories distintas se define \(\rho\) precisamente para ignorar su diferencia. Falla M2/SU2 aunque el quotient resultante sea matemáticamente coherente.

**MB4 — subsistema/contexto anidado.** Un termostato, organismo, servicio o proceso dentro de una realización host puede poseer un MemoState excelente. El MemoState solo no basta, pero la condición de subsistema tampoco lo excluye: si una presentación pre-indexada satisface TR-M/MC1–MC10 + IndAdequate, puede admitirse como contexto \(j\) embebido en el host \(i\). Lo que falla es la promoción gratuita, no la contextualidad anidada.

**MB5 — reemplazo completo de componentes.** Todos los componentes de una SourceUnit cambian, pero la cadena de memo-states conserva suficiencia/reentrancy con invalidaciones correctas. El caso permanece compatible con persistencia y muestra por qué la identidad no puede reducirse al snapshot material.

**MB6 — mismo memo-state, provenance distinta.** Dos historias source-side pueden ser memo-equivalentes para \(\rho\) y conservar provenance objetiva distinta. Memoization no borra el pasado; solo determina qué diferencias siguen siendo necesarias para ese rol.

**MB6a — interfaz vacía.** Se define \(I^\rho\) sin dimensiones discriminantes y todas las sources resultan equivalentes. Falla IC2/IC4/IC7. Una interfaz no puede justificar quotient por ser deliberadamente ciega.

**MB6b — hidden bypass.** Dos sources son equivalentes en la interfaz declarada, pero el consumidor depende además de una variable upstream por otro canal. Falla IC5/B6. La interfaz no screens off la diferencia.

**MB6c — misma interfaz, provenance distinta.** Dos sistemas energéticos internamente distintos presentan trazas equivalentes en \(I_{\mathrm{AC}}\). No hay identidad upstream; sí equivalencia downstream para consumidores cuyo acoplamiento factoriza por esa interfaz.

**MB7 — quotient bake legítimo.** Dos SourceUnit no memo-equivalentes producen la misma \(\sigma_k\), y la igualdad target-side satisface B7 respecto de \(E^S_\Theta\). Es SignatureConvergence candidata, no colisión defectuosa.

**MB8 — quotient bake excesivo.** Dos SourceUnit producen la misma \(\sigma_k\), pero una diferencia eliminada cambia una dependencia target-side atribuida a \(\rho\). Falla B6/B7; el baking es unsound.

**MB9 — baking sin memoization.** Un source elemental ya está individuado por una teoría independiente y satisface SourceUnit directamente. Bake puede ser admisible. Esto refuta la versión demasiado fuerte “todo baking requiere memoization” y conserva solo el requisito correcto de unitización previa.

**MB10 — baking sin génesis.** Una SourceUnit tiene realización fiel dentro de una estructura host/embedded target sin nueva ContextGenesis. Bake puede valer mientras GenesisTrivialization no. Esto prueba que ambas nociones no deben identificarse.

#### 0.11.94. Estado de REV-07h

REV-07h queda **PARTIAL / arquitectura candidata**.

Se obtiene una separación no presente en REV-07e:

\[
\boxed{
\begin{array}{rcl}
\text{SourceUnit} &:& \text{qué estructura cuenta como unidad para un rol},\\
\text{Interface} &:& \text{qué de esa unidad puede importar downstream},\\
\text{Memoization} &:& \text{qué historia debe conservarse para mantener la interfaz},\\
\text{Baking} &:& \text{cómo se realiza la interfaz en otro contexto},\\
\text{GenesisTrivialization} &:& \text{Bake usado constitutivamente en ContextGenesis}.
\end{array}
}
\]

Y aparecen tres resultados arquitectónicos fuertes:

\[
\boxed{
\operatorname{Bake}
\text{ no debe seleccionar por sí mismo qué cuenta como su source complejo;}
}
\]

\[
\boxed{
\operatorname{MemoIndividuated}
\not\Rightarrow
\operatorname{ContextIndividuation};
}
\]

\[
\boxed{
\operatorname{GenesisTrivialization}
\text{ es una especialización ontogénica de Bake, no su definición.}
}
\]

Las deudas de InterfaceContract, RoleAdequate y MemoState/update/invalidation quedan **RESOLVED formal/a nivel de criterio**; la composicionalidad cross-role queda **RESOLVED condicionalmente**. §§0.11.87–0.11.87i coordinan B1–B10 con esos resultados: B7 usa ahora decodificación entre quotients contractuales source/target, BS-T1 demuestra soundness, la composición horizontal exige preservar interaction information, la vertical exige ContractAlignment y BS-T2 prueba no-recovery desde un Bake ya colapsado; RehydrateAdequate caracteriza side information suficiente. Para cerrar REV-07h completo falta:

1. precisar cuándo InterfaceWall es mera subdeterminación de canal y cuándo puede elevarse a irreconstruibilidad genealógica de principio;
2. investigar, sin presuponerlo, si una familia contextualmente adecuada de ContinuationProfiles + estructura generativa/Bake puede inducir \(\Omega_i\).

TR-M queda **RESOLVED condicionalmente** en §§0.11.91k–0.11.91r: MemoState no individúa por sí solo, pero una máquina contextual pre-indexada que satisface MC1–MC10 + IndAdequate puede descargar un contexto local/anidado.

La ganancia inmediata no es demostrar identidad contextual, sino aislar la estructura que faltaba entre individuación y recontextualización:

\[
\boxed{
\text{la interfaz fija qué diferencias upstream pueden dejar de importar downstream.}
\]

Memoization mantiene esa interfaz a través de la historia; invalidation marca cuándo deja de hacerlo; Bake realiza la interfaz en el target; GenesisTrivialization usa esa realización constitutivamente durante una génesis.


**RECONSTRUCTION LAYER.** La maquinaria de enlaces que sigue se conserva únicamente para comprobar si $\Lambda_*$ o $\mathcal C_*$ reconstruyen la clausura generativa. Queda SUPERSEDED cualquier lectura en la que conectividad finita defina primariamente el régimen.

**Advertencia PureOntRel.** Una relación pura puede servir como enlace ontológico de marco sin preservar una única genealogía. Por ello no se incorpora automáticamente a $\Lambda_*$ cuando esta pretende reconstruir $\operatorname{Generated}^{*}$: si conecta dos genealogías sin common ground, produciría sobreinclusión y haría fallar $\mathrm{RS}^{\mathrm{gen}}_{\Lambda,i}$. Su admisión como enlace reconstructivo requiere una justificación adicional de soundness; RelIntegrable por sí sola no basta.


### 1. Tokens ontológicos actuales

Sea $\mathbb T$ una clase/set de trabajo de **tokens ontológicos actuales** relevantes para la teoría procesual: estados, eventos, entidades, estructuras o relaciones efectivamente instanciadas.

No se exige que todos los tokens sean del mismo tipo.

### 2. Familia de enlaces ontológicos admisibles

Sea $\Lambda$ una familia de tipos de relación ontológica actual. Ejemplos posibles, según la ontología concreta, incluyen:

- relación causal actual;
- pertenencia a un mismo proceso actual;
- relación constitutiva/parte-todo efectivamente instanciada;
- dependencia ontológica efectivamente instanciada;
- relación espaciotemporal cuando esa categoría sea aplicable;
- incidencia estado-evento en una estructura procesual.

No cuentan por sí solas:

- mera semejanza;
- compartir leyes descriptivas;
- posibilidad de interacción;
- isomorfismo estructural;
- ser representables en una misma teoría;
- existencia postulada de una cota común.

Estas exclusiones son importantes: de otro modo la relación de régimen volvería a introducir por definición la conclusión metaontológica.

### 3. Enlace ontológico inmediato

Definimos una relación simétrica:

$$
q\bowtie r
$$

si y solo si existe $\lambda\in\Lambda$ tal que:

$$
\lambda(q,r)
\lor
\lambda(r,q).
$$

La relación $\bowtie$ debe satisfacer:

**L1 — actualidad.** Solo cuentan relaciones efectivamente instanciadas.

**L2 — independencia de amalgamación.** La definición de $\bowtie$ no puede mencionar $K3$, una cota común, $R_i$, `SameIndex` ni pertenencia previa a un régimen.

**L3 — invariancia representacional.** Si dos representaciones preservan la misma estructura ontológica relevante, deben preservar también si $q\bowtie r$.

**L4 — no trivialidad.** No toda pareja de tokens queda enlazada por defecto.

### 4. Relación de co-régimen

Definimos:

$$
q\sim r
$$

como la clausura reflexivo-transitiva de $\bowtie$.

Como $\bowtie$ es simétrica, $\sim$ es reflexiva, simétrica y transitiva. Por tanto es una relación de equivalencia.

Las clases:

$$
[q]_{\sim}
$$

son los **regímenes ontológicos candidatos**.

Escribimos:

$$
\operatorname{Reg}(q)
:=
[q]_{\sim}.
$$

Así, dos tokens son worldmates/regimemates no porque admitan una cota común, sino porque están conectados por una cadena finita de relaciones ontológicas actuales.

### 5. Regímenes de dominios procesuales

Sea:

$$
\operatorname{Tok}(X)
:=
\{q\in\mathbb T\mid q\trianglelefteq X\}.
$$

Para un dominio no vacío $X$, definimos:

$$
\operatorname{Reg}(X)=i
$$

si:

$$
\forall q\in\operatorname{Tok}(X),
\quad
\operatorname{Reg}(q)=i.
$$

Como las clases de equivalencia de $\sim$ son disjuntas, si $\operatorname{Tok}(X)\neq\varnothing$ entonces $\operatorname{Reg}(X)$, cuando existe, es único.

Un objeto que solo **describe conjuntamente** tokens de dos clases diferentes no pasa por ello a ser un dominio ontológico local: es un artefacto metalingüístico o representacional, salvo que exista una relación ontológica actual que conecte ambas clases y las fusione bajo $\sim$.

### 6. SameRegime ya no implica K3

Definimos:

$$
\operatorname{SameRegime}(X,Y)
\iff
\operatorname{Reg}(X)=\operatorname{Reg}(Y).
$$

Esto es independiente de la existencia de una cota común.

Contraejemplo mínimo:

$$
\mathbb T=\{a,b\},
\qquad
a\bowtie b.
$$

Entonces:

$$
a\sim b.
$$

Sea:

$$
\mathfrak D_i=\{X,Y\}
$$

con:

$$
\operatorname{Tok}(X)=\{a\},
\qquad
\operatorname{Tok}(Y)=\{b\}.
$$

Ambos dominios pertenecen al mismo régimen $i$, pero si $\mathfrak D_i$ no contiene ningún tercer dominio $Z$ con:

$$
X\preceq_i Z
\land
Y\preceq_i Z,
$$

entonces K3_i falla.

Por tanto:

$$
\boxed{
\operatorname{SameRegime}(X,Y)
\not\Rightarrow
\exists Z\,[X\preceq_i Z\land Y\preceq_i Z].
}
$$

Esto demuestra que la identidad de régimen ya no contiene K3 por definición.

### 7. Qué haría falta para derivar K3_i

K3_i necesitaría una premisa adicional de **admisibilidad de agregación/extensión dentro del régimen**.

Por ejemplo, una condición candidata sería:

$$
\operatorname{BridgeAdmissible}_i(X,Y)
\Rightarrow
\exists Z\in\mathfrak D_i:
X\preceq_i Z
\land
Y\preceq_i Z.
$$

Pero `BridgeAdmissible` no puede definirse como «existe tal $Z$», porque volvería a ser circular.

Una vía futura sería justificarla mediante cierre de los dominios admisibles bajo incorporación de cadenas finitas de enlaces actuales, y luego estudiar qué hipótesis adicionales hacen falta para dominios infinitos.

### 8. Relación con Lewis y con la ontología de procesos

La estrategia tiene un antecedente metodológico claro en Lewis: su relación de worldmate se apoya en conexión espaciotemporal, no en la existencia previa de un mundo común. Aquí no se adopta su modal realism ni se restringe la unidad ontológica a relaciones espaciotemporales; $\Lambda$ puede incluir vínculos causales, constitutivos, procesuales o de dependencia.

Las event structures de Winskel ofrecen otro antecedente formal para pensar procesos como redes de ocurrencias enlazadas por causalidad/enabling, aunque aquí la noción de régimen es más amplia que una event structure.

### 9. Límites de la propuesta

La elección de $\Lambda$ es sustantiva. Si se introducen relaciones demasiado amplias —por ejemplo, mera semejanza o compartir leyes— el criterio puede colapsar regímenes que deberían permanecer separados. Si $\Lambda$ es demasiado estrecha, puede fragmentar una realidad que intuitivamente se quiere tratar como una.

Por eso REV-07 no queda RESOLVED todavía.

El criterio de cierre pasa a ser:

1. justificar una familia $\Lambda$ de enlaces actuales con contenido ontológico independiente;
2. demostrar invariancia representacional suficiente para $\sim$;
3. mostrar que los dominios relevantes quedan tipados de forma estable por $\operatorname{Reg}$;
4. justificar K3_i mediante una premisa adicional distinta de la propia identidad de régimen.

---

---

## REV-07 — criterios de admisibilidad para la familia de enlaces

El criterio de régimen necesita una familia de tipos de relación definida **antes** de conocer los regímenes. La notamos:

$$
\Lambda_*.
$$

El subíndice `*` indica nivel pre-régimen: $\Lambda_*$ no puede depender de $i$, $R_i$, K3_i ni de `SameRegime`.

### 1. Instancia relacional actual

Para un tipo de relación $\lambda$, escribimos:

$$
\rho:\lambda(q,r)
$$

para una **instancia relacional actual** que tiene a $q$ y $r$ como relata.

No es necesario comprometerse aquí con una reificación universal de relaciones. La notación solo expresa que el hecho relacional está efectivamente instanciado y puede actuar como testigo local.

### 2. Condiciones necesarias de admisibilidad

Un tipo $\lambda$ puede pertenecer a $\Lambda_*$ solo si sus instancias candidatas satisfacen las siguientes condiciones.

**A1 — actualidad.**

$$
\rho:\lambda(q,r)
\Rightarrow
\operatorname{Actual}(\rho).
$$

No basta que $q$ y $r$ pudieran interactuar, relacionarse o coexistir.

**A2 — carácter ontológico, no meramente representacional.**

La relación debe obtener entre los relata mismos, no únicamente entre sus descripciones, nombres, modelos o representaciones.

**A3 — sensibilidad a los relata.**

La instancia relacional debe ser genuinamente token-specific: sustituir arbitrariamente uno de los relata por un duplicado cualitativo no tiene por qué preservar la misma instancia relacional.

Esto excluye como criterios suficientes:

- compartir un universal;
- instanciar el mismo tipo o propiedad;
- obedecer la misma ley;
- satisfacer la misma ecuación;
- ser estructuralmente isomorfos;
- mera semejanza cualitativa.

Esas relaciones pueden ser reales o verdaderas, pero no conectan por sí mismas dos tokens en una única realidad ontológica.

**A4 — rol integrador.**

La instancia debe pertenecer a al menos una familia cuyo contenido ontológico conecte concretamente los relata:

$$
\Lambda_*
\subseteq
\Lambda_{\mathrm{proc}}
\cup
\Lambda_{\mathrm{causal}}
\cup
\Lambda_{\mathrm{constit}}
\cup
\Lambda_{\mathrm{dep}}
\cup
\Lambda_{\mathrm{st}}.
$$

Lectura de las familias:

- $\Lambda_{\mathrm{proc}}$: incidencia en un mismo evento/proceso actual, por ejemplo participante-evento, source-event-target o enabling efectivamente instanciado;
- $\Lambda_{\mathrm{causal}}$: relación causal actual entre relata o acontecimientos;
- $\Lambda_{\mathrm{constit}}$: parthood, constitución o composición actual cuando la ontología concreta reconoce esa relación como ontológicamente genuina;
- $\Lambda_{\mathrm{dep}}$: dependencia ontológica token-specific, en particular dependencia existencial o de identidad;
- $\Lambda_{\mathrm{st}}$: relaciones espaciotemporales actuales cuando los relata pertenecen a una ontología a la que esa categoría se aplica.

Esta lista es una **taxonomía de roles integradores**, no una afirmación de que todos ellos sean primitivos ni de que toda ontología tenga que contenerlos.

**A5 — localidad semántica.**

Determinar si $\rho:\lambda(q,r)$ no puede requerir cuantificar sobre:

$$
R_i,
\quad
R_{\mathrm{abs}},
\quad
\operatorname{Reg}(q),
\quad
K3_i
$$

ni sobre una totalidad cuya existencia sea precisamente lo que se intenta derivar.

**A6 — invariancia representacional.**

Si dos representaciones son fieles al mismo hecho relacional, deben coincidir en si existe la instancia de enlace relevante. El régimen no puede cambiar por renombrar nodos, cambiar coordenadas o escoger otra codificación isomorfa.

### 3. Definición refinada de enlace

Definimos:

$$
q\bowtie_* r
$$

si existe $\lambda\in\Lambda_*$ y una instancia actual admisible:

$$
\rho:\lambda(q,r).
$$

Usamos la simetrización solo para conectividad:

$$
q\bowtie r
\iff
q\bowtie_* r
\lor
r\bowtie_* q.
$$

La dirección original de causalidad, dependencia o constitución no se borra de la ontología; solo se ignora al calcular componentes conexas.

Después:

$$
\sim
:=
(\bowtie)^{*}
$$

es la clausura reflexivo-transitiva usada para formar los regímenes candidatos.

### 4. Tests positivos

**P1 — proceso actual.** Si un evento actual $e$ tiene a $s_0$ como source y a $s_1$ como target, la incidencia source/target proporciona enlaces del perfil $\Lambda_{\mathrm{proc}}$.

**P2 — causalidad actual.** Si un acontecimiento $a$ causa actualmente $b$, la instancia causal puede enlazarlos aunque la relación sea dirigida.

**P3 — constitución.** Si $p$ es parte actual de un todo $w$, la instancia mereológica/constitutiva puede enlazar $p$ y $w$ si esa ontología acepta la relación relevante.

**P4 — dependencia ontológica.** Si la identidad o existencia de un token $x$ depende de un token concreto $y$, la instancia de dependencia puede enlazarlos.

**P5 — espaciotiempo.** Dos entidades concretas con una relación espaciotemporal actual pueden quedar conectadas por $\Lambda_{\mathrm{st}}$, sin exigir interacción causal directa.

### 5. Tests negativos anti-colapso

**N1 — universal compartido.** Dos objetos rojos no quedan enlazados solo por instanciar `Rojo`.

**N2 — ley compartida.** Dos sistemas que obedecen la misma ecuación dinámica no quedan enlazados por ello.

**N3 — isomorfismo.** Dos procesos isomorfos pueden pertenecer a regímenes distintos.

**N4 — posibilidad causal.** Que $q$ pudiera causar $r$ en otras condiciones no es una instancia causal actual.

**N5 — co-representación.** Un modelo, teoría o documento que describa conjuntamente $q$ y $r$ no los hace worldmates.

**N6 — dependencia de tipo.** Dos tokens que dependan ambos de la misma clase, ley, universal o definición no quedan enlazados salvo que exista además una dependencia token-specific admisible entre ellos.

### 6. Caso delicado: correlación y entrelazamiento

Una correlación estadística no pertenece automáticamente a $\Lambda_*$. Para contar como enlace debe existir una interpretación ontológica independiente según la cual esa correlación corresponde a una relación actual del tipo admitido.

Lo mismo vale para relaciones físicas no clásicas como el entrelazamiento: la teoría no decide por decreto si pertenecen a $\Lambda_*$. Si una ontología física los trata como relación real entre tokens, deben evaluarse por A1–A6.

### 7. No-colapso por hubs abstractos

Las condiciones A3–A4 bloquean un problema importante.

Si compartir una propiedad universal $U$ fuera suficiente, entonces:

$$
q\operatorname{Inst}U
\land
r\operatorname{Inst}U
\Rightarrow
q\sim r
$$

y universales muy generales podrían conectar casi todo el espacio ontológico.

Esta inferencia queda rechazada.

El mismo argumento bloquea leyes, tipos, categorías y descripciones universales como nodos-hub de régimen.

### 8. Qué se ha conseguido

$\Lambda_*$ deja de ser una lista intuitiva y pasa a estar sometida a seis constraints explícitos más tests positivos/negativos.

Pero la teoría no ha demostrado que esta sea **la única** familia correcta de enlaces ontológicos.

REV-07 permanece PARTIAL hasta:

1. justificar filosóficamente los roles integradores admitidos;
2. decidir qué variantes de constitución/dependencia cuentan en casos controvertidos;
3. demostrar suficiente invariancia de $\sim$ bajo las representaciones usadas por REV-18;
4. justificar K3_i mediante una premisa separada.

---

---

## REV-07 — derivación local de directedness para una reconstrucción $\Lambda_*$

**CURRENT TYPING.** Los caminos finitos de $\bowtie$ definen solo una **componente candidata de reconstrucción**. No se identifica con el régimen genealógico $i$ hasta demostrar:

$$
\mathrm{RS}_{\Lambda}^{\mathrm{gen}}
\land
\mathrm{RC}_{\Lambda}^{\mathrm{gen}}.
$$

EEA + OAM pueden demostrar directedness del poset asociado a esa componente candidata. Solo bajo RS+RC esa directedness puede reetiquetarse legítimamente como $K3_i$ del régimen genealógico.

### 1. EEA — Edge Extension Admissibility

Para todo dominio no vacío $X\in\mathfrak D_i^{\mathrm{proc}}$, si:

$$
q\trianglelefteq_i X
$$

y existe un enlace actual:

$$
q\bowtie r,
$$

entonces existe un dominio admisible:

$$
X'\in\mathfrak D_i^{\mathrm{proc}}
$$

tal que:

$$
X\preceq_i X'
$$

y:

$$
r\trianglelefteq_i X'.
$$

Además, la instancia relacional que testimonia $q\bowtie r$ debe quedar representada en $X'$ cuando el tipo de dominio la modele explícitamente.

Intuición: un dominio actual que contiene uno de los relata puede ampliarse localmente para representar también el otro extremo de una relación ontológica actual que los conecta.

EEA no dice que cualquier par de dominios tenga una cota común.

### 2. OAM — Overlap Amalgamation

Para cualesquiera:

$$
X,Y\in\mathfrak D_i^{\mathrm{proc}},
$$

si existe un token actual $q$ con:

$$
q\trianglelefteq_i X
\land
q\trianglelefteq_i Y,
$$

entonces existe:

$$
Z\in\mathfrak D_i^{\mathrm{proc}}
$$

tal que:

$$
X\preceq_i Z
\land
Y\preceq_i Z.
$$

Intuición: dos dominios ontológicos actuales que literalmente solapan en contenido actual no pueden ser realidades completamente aisladas; si ambos son descripciones/subdominios admisibles del mismo contenido actual, debe existir una extensión conjunta admisible.

OAM es mucho más débil que K3_i: solo habla de dominios con solapamiento actual explícito.

### 3. Lema de directedness interna

**Lema REV-07.1 — candidate directedness.** Supóngase:

1. los dominios considerados son no vacíos;
2. se fija una componente candidata $C=[q]_{\sim}$ de $\sim=(\bowtie)^*$;
3. EEA;
4. OAM.

Entonces el poset procesual restringido a $C$ es dirigido:

$$
\boxed{K3_{\Lambda,C}.}
$$

Si además:

$$
\mathrm{RS}_{\Lambda}^{\mathrm{gen}}
\land
\mathrm{RC}_{\Lambda}^{\mathrm{gen}},
$$

de modo que $C$ coincide con la clausura $\operatorname{Generated}^{*}_i(\mathcal O_i,-)$, entonces:

$$
\boxed{
K3_{\Lambda,C}
\Rightarrow
K3_i.
}
$$

**Demostración.**

Sean:

$$
X,Y\in\mathfrak D_i^{\mathrm{proc}}.
$$

Como son no vacíos, elijamos:

$$
q_0\trianglelefteq_i X
$$

y:

$$
q_n\trianglelefteq_i Y.
$$

Como ambos pertenecen al mismo régimen $i$:

$$
q_0\sim q_n.
$$

Por definición de $\sim$ existe un camino finito:

$$
q_0\bowtie q_1\bowtie\cdots\bowtie q_n.
$$

Aplicando EEA iterativamente obtenemos:

$$
X=X_0
\preceq_i
X_1
\preceq_i
\cdots
\preceq_i
X_n
$$

con:

$$
q_k\trianglelefteq_i X_k
$$

para cada $k$, y en particular:

$$
q_n\trianglelefteq_i X_n.
$$

Pero también:

$$
q_n\trianglelefteq_i Y.
$$

Así $X_n$ y $Y$ se solapan actualmente en $q_n$.

Por OAM existe $Z\in\mathfrak D_i^{\mathrm{proc}}$ con:

$$
X_n\preceq_i Z
\land
Y\preceq_i Z.
$$

Y como:

$$
X\preceq_i X_n,
$$

por transitividad:

$$
X\preceq_i Z
\land
Y\preceq_i Z.
$$

Por tanto $K3_{\Lambda,C}$ para dominios no vacíos. Bajo $\mathrm{RS}_{\Lambda}^{\mathrm{gen}}+\mathrm{RC}_{\Lambda}^{\mathrm{gen}}$, la componente $C$ es la genealogía del índice $i$ y el resultado se reetiqueta como $K3_i$. $\square$

**Caso del dominio vacío.** Si $\mathfrak D_i^{\mathrm{proc}}$ contiene un dominio vacío $0_i$, para recuperar K3_i sobre todo el poset basta exigir:

$$
0_i\preceq_i X
$$

para todo $X\in\mathfrak D_i^{\mathrm{proc}}$.

Entonces cualquier par donde intervenga $0_i$ tiene como cota al otro dominio. Si no se desea asumir un bottom vacío, el lema debe leerse sobre el subposet no vacío.

### 4. Qué gana esta derivación

Directedness de la componente candidata ya no necesita ser una premisa global primitiva. Se reduce a dos compromisos locales:

$$
\boxed{
\mathrm{EEA}+\mathrm{OAM}
\Rightarrow
K3_{\Lambda,C}.
}
$$

y solo con reconstrucción genealógica completa:

$$
\boxed{
\mathrm{RS}_{\Lambda}^{\mathrm{gen}}
+
\mathrm{RC}_{\Lambda}^{\mathrm{gen}}
+
K3_{\Lambda,C}
\Rightarrow
K3_i.
}
$$

Ni EEA ni OAM usan `SameRegime` como sinónimo de amalgamabilidad:

- EEA habla de un único dominio y un único enlace actual;
- OAM habla de dos dominios que ya comparten literalmente contenido actual.

### 5. Límites y posibles contraejemplos

**EEA puede fallar** si la noción de dominio admisible impone restricciones que impiden incorporar uno de los extremos de una relación ontológica actual. Eso sería conceptualmente extraño, pero no contradictorio.

**OAM puede fallar** si dos dominios que comparten un token codifican aspectos ontológicos mutuamente incompatibles o si la clase de dominios no está cerrada bajo su combinación. En ese caso K3_i tampoco queda demostrado.

Por tanto la derivación no es una prueba gratuita de directedness: desplaza la carga a principios locales más transparentes y falsables.

### 6. Relación con REV-18 y REV-19

EEA depende directamente de que la incidencia:

$$
q\trianglelefteq_i X
$$

tenga una interpretación ontológica estable. Por ello REV-18 sigue siendo relevante.

OAM depende de la noción precisa de:

$$
\preceq_i
$$

y de qué cuenta como dominio procesual admisible, por lo que REV-19 también sigue abierto.

Así, REV-07 ya no es un blocker autónomo completamente separado: su parte de directedness puede cerrarse si REV-18/19 justifican EEA y OAM.

---

---

## REV-21 — caracterización completa de los puntos fijos de $F_i$

Sea el grafo dirigido de eventos emergentes del régimen/sistema:

$$
G_i=(\Sigma_i,E_i),
$$

donde:

$$
(s,t)\in E_i
$$

si existe al menos un evento emergente actual que lleva de $s$ a $t$.

Sea:

$$
F_i(A)
:=
\{
t\in\Sigma_i
\mid
\exists s\in A:
s\to_{E_i}^{*}t
\}.
$$

### 1. Puntos fijos = subconjuntos forward-closed

**Proposición REV-21.1.**

$$
F_i(A)=A
$$

si y solo si $A$ es cerrado hacia adelante:

$$
\forall s\in A,
\quad
s\to_{E_i}^{*}t
\Rightarrow
t\in A.
$$

**Prueba.**

Si $F_i(A)=A$, toda configuración alcanzable desde $A$ pertenece por definición a $F_i(A)$ y por tanto a $A$.

Recíprocamente, si $A$ es forward-closed, toda configuración añadida por alcanzabilidad ya pertenece a $A$. Como la clausura es reflexiva, $A\subseteq F_i(A)$; luego $F_i(A)=A$. $\square$

### 2. Punto fijo mínimo generado por un estado

Para $s\in\Sigma_i$, definimos:

$$
\operatorname{Reach}_i(s)
:=
\{t\in\Sigma_i\mid s\to_{E_i}^{*}t\}.
$$

Entonces:

$$
\boxed{
F_i(\{s\})
=
\operatorname{Reach}_i(s).
}
$$

Además, $\operatorname{Reach}_i(s)$ es el menor punto fijo que contiene a $s$.

### 3. Cuándo existe un punto fijo propio no vacío

Supongamos $\Sigma_i\neq\varnothing$.

Existe un punto fijo propio no vacío:

$$
\varnothing\neq A
\subsetneq
\Sigma_i
$$

si y solo si existe algún estado $s$ tal que:

$$
\operatorname{Reach}_i(s)
\neq
\Sigma_i.
$$

Una dirección es inmediata tomando:

$$
A=\operatorname{Reach}_i(s).
$$

Para la conversa, si $A$ es un punto fijo propio no vacío y $s\in A$, forward-closure implica:

$$
\operatorname{Reach}_i(s)\subseteq A
\subsetneq
\Sigma_i.
$$

### 4. Degeneración total y fuerte conectividad

**Teorema REV-21.2.** Para $\Sigma_i\neq\varnothing$, las siguientes condiciones son equivalentes:

1. el único punto fijo no vacío de $F_i$ es $\Sigma_i$;
2. para todo $s\in\Sigma_i$:

$$
\operatorname{Reach}_i(s)=\Sigma_i;
$$

3. $G_i$ es fuertemente conexo.

Por tanto:

$$
\boxed{
\operatorname{Fix}(F_i)\setminus\{\varnothing\}
=
\{\Sigma_i\}
\iff
G_i\text{ es fuertemente conexo}.
}
$$

Así la degeneración temida en REV-21 no es genérica: tiene una condición gráfica exacta.

### 5. Caracterización por SCCs

Sea:

$$
\operatorname{SCC}(G_i)
$$

el conjunto de componentes fuertemente conexas, y sea:

$$
\operatorname{Cond}(G_i)
$$

el grafo de condensación, que es acíclico.

Todo punto fijo de $F_i$ es una unión de SCCs que es forward-closed en el grafo de condensación.

Recíprocamente, toda unión forward-closed de SCCs determina un punto fijo.

Por tanto:

$$
\boxed{
\operatorname{Fix}(F_i)
\cong
\{
U\subseteq\operatorname{SCC}(G_i)
\mid
U\text{ es forward-closed en }\operatorname{Cond}(G_i)
\}.
}
$$

Esto caracteriza por completo el poder discriminante de la clausura de alcanzabilidad.

### 6. Funciones de progreso y ausencia de degeneración

Sea:

$$
\mu:\Sigma_i\to(Q,<)
$$

una función hacia un orden estricto tal que todo evento emergente satisface:

$$
s\to_{E_i}t
\Rightarrow
\mu(s)<\mu(t).
$$

Entonces $G_i$ es acíclico: un ciclo implicaría:

$$
\mu(s_0)
<
\mu(s_1)
<
\cdots
<
\mu(s_n)=\mu(s_0),
$$

contradicción.

En particular, si:

$$
|\Sigma_i|>1,
$$

un grafo acíclico no puede ser fuertemente conexo. Por REV-21.2:

$$
\boxed{
\text{progreso estricto global}
\Rightarrow
\text{existe un punto fijo propio no vacío}.
}
$$

Si $G_i$ es finito y acíclico, sus SCCs son singletons y el grafo de condensación coincide con el propio DAG; los cierres propios pueden leerse directamente como subconjuntos forward-closed.

### 7. Interpretación de la ciclicidad

Para que el único cierre no vacío sea todo $\Sigma_i$, el grafo debe permitir retorno dirigido entre cualesquiera dos estados. Cuando $|\Sigma_i|>1$, esto exige ciclos emergentes.

Si una misma macrovariable ordenada aumenta estrictamente en todos los eventos emergentes relevantes, esos ciclos están prohibidos.

Si diferentes eventos usan macrovariables distintas, o una macrovariable puede disminuir después, la ciclicidad vuelve a ser posible. Por eso la afirmación correcta es condicional a la existencia de una función de progreso global $\mu$, no a que cada evento aislado tenga alguna macrocaracterística cambiante.

### 8. Estado de REV-21

REV-21 puede marcarse **RESOLVED**.

El criterio de cierre solicitado queda satisfecho:

- los puntos fijos están caracterizados exactamente;
- se sabe cuándo existen cierres propios;
- se sabe exactamente cuándo la clausura degenera a $\Sigma_i$ para todo conjunto no vacío;
- se identifica una condición suficiente simple que impide la degeneración.

---

---

## REV-19 — tipo y orden procesual normalizados

El problema de REV-19 era que la emergencia es diacrónica mientras el antiguo target era una instantánea. La solución no requiere una teoría temporal completa: basta fijar el tipo semántico de un **fragmento procesual actual** y distinguirlo de la cuestión adicional de si ese fragmento es ontológicamente admisible.

### 1. Fragmentos procesuales semánticos

Fijado un régimen $i$, un fragmento procesual semántico es una estructura:

$$
X=(T_X,\Phi_X),
$$

donde:

- $T_X$ es un conjunto set-sized de **tokens ontológicos actuales** del régimen $i$;
- $\Phi_X$ es un conjunto de **hechos relacionales actuales** cuyos relata pertenecen a $T_X$.

El vocabulario procesual mínimo puede contener átomos como:

$$
\operatorname{State}(s),
\quad
\operatorname{Event}(e),
\quad
\operatorname{src}(e,s),
\quad
\operatorname{tgt}(e,t),
\quad
e\prec f,
$$

además de instancias admisibles de relaciones de $\Lambda_*$ cuando sean relevantes.

$X$ es un **contenido semántico**, no una serialización, grafo RDF, tupla de IDs ni modelo sintáctico. Una representación concreta debe denotar este contenido; cambiar la codificación no cambia $X$.

### 2. Well-formedness estructural

Sea $\mathfrak P_i^{\mathrm{proc}}$ la colección de fragmentos que cumplen:

**PW1 — homogeneidad de régimen.**

$$
q\in T_X
\Rightarrow
\operatorname{Reg}(q)=i.
$$

**PW2 — actualidad.** Todo token y todo hecho de $X$ está efectivamente instanciado.

**PW3 — localidad de relata.** Si un hecho $\varphi\in\Phi_X$ menciona un token $q$, entonces:

$$
q\in T_X.
$$

**PW4 — integridad mínima de eventos.** Si:

$$
\operatorname{Event}(e)\in\Phi_X,
$$

entonces existen tokens únicos $s,t\in T_X$ tales que:

$$
\operatorname{src}(e,s)\in\Phi_X
$$

y:

$$
\operatorname{tgt}(e,t)\in\Phi_X.
$$

Así no se representa un evento actual sin sus extremos.

**PW5 — coherencia procesual.** Los hechos de precedencia incluidos en $\Phi_X$ son compatibles con una relación estricta acíclica de precedencia/dependencia.

**PW6 — positividad.** Un fragmento puede omitir contenido actual adicional, pero no contiene negaciones ontológicas que una extensión posterior tenga que retractar.

PW6 es importante: $Y$ puede añadir nuevos hechos actuales entre tokens ya presentes en $X$ sin que eso signifique que $X$ fuese falso. El orden es de **crecimiento de contenido positivo**, no de teoría completa.

### 3. Orden procesual

Para:

$$
X,Y\in\mathfrak P_i^{\mathrm{proc}},
$$

definimos:

$$
\boxed{
X\preceq_i^{\mathrm{proc}}Y
\iff
T_X\subseteq T_Y
\land
\Phi_X\subseteq\Phi_Y.
}
$$

Este es un orden parcial:

- reflexividad: inclusión reflexiva;
- transitividad: inclusión transitiva;
- antisimetría: si $T_X=T_Y$ y $\Phi_X=\Phi_Y$, los contenidos semánticos son el mismo fragmento.

No es una equivalencia conductual ni una extensión conservativa de REV-02. $Y$ puede añadir eventos, relaciones y capacidades que cambien el comportamiento del contenido anterior.

### 4. Representaciones concretas

Si un artefacto/modelo $H$ representa un fragmento, escribimos:

$$
\llbracket H\rrbracket=X.
$$

Dos representaciones son ontológicamente equivalentes cuando:

$$
\llbracket H\rrbracket
=
\llbracket H'\rrbracket.
$$

El orden se aplica a los contenidos denotados, no a nombres de nodos ni a la sintaxis:

$$
H\preceq H'
$$

solo como abreviatura de:

$$
\llbracket H\rrbracket
\preceq_i^{\mathrm{proc}}
\llbracket H'\rrbracket.
$$

Esto hace explícita la invariancia representacional requerida por REV-07/REV-18.

### 5. Incidencia deja de ser primitiva

Sobre el tipo procesual normalizado:

$$
q\trianglelefteq_i X
\iff
q\in T_X.
$$

Para un hecho relacional actual $\rho$:

$$
\rho\trianglelefteq_i X
\iff
\rho\in\Phi_X.
$$

El dominio **no se identifica con un mero conjunto de tokens**: es la estructura $(T_X,\Phi_X)$. Pero la incidencia de un token ya tiene semántica precisa como pertenencia al carrier semántico del fragmento.

Esto avanza REV-18 sin convertir `EClosed` en una definición circular.

### 6. Dominios ontológicamente admisibles

No todo fragmento formalmente well-formed tiene que ser un dominio ontológico admisible.

Introducimos un predicado separado:

$$
\operatorname{Adm}_i(X),
$$

y definimos:

$$
\mathfrak D_i^{\mathrm{proc}}
:=
\{
X\in\mathfrak P_i^{\mathrm{proc}}
\mid
\operatorname{Adm}_i(X)
\}.
$$

El orden del teorema es la restricción de $\preceq_i^{\mathrm{proc}}$ a $\mathfrak D_i^{\mathrm{proc}}$.

Esta separación evita resolver por decreto las cargas restantes:

- REV-20 pregunta si todo dominio admisible tiene una extensión admisible E-closed;
- REV-09 pregunta si uniones/límites formales de cadenas admisibles siguen siendo admisibles;
- EEA pregunta si ampliar un dominio a lo largo de un enlace actual conserva admisibilidad;
- OAM pregunta si la unión/amalgama de dominios solapados conserva admisibilidad.

Todos ellos son ahora problemas sobre $\operatorname{Adm}_i$, no ambigüedades sobre qué significa el orden.

### 7. Relectura de EEA y OAM

Sea $\rho:\lambda(q,r)$ una instancia admisible de $\Lambda_*$.

Definimos el **footprint mínimo** de $\rho$ como el contenido finito/local necesario para representar $r$, $\rho$ y cualquier endpoint estructural obligatorio.

En la capa formal:

$$
X
\preceq_i^{\mathrm{proc}}
\operatorname{WF}(X\cup\operatorname{Foot}(\rho)),
$$

donde $\operatorname{WF}$ añade solo el contenido exigido por PW3–PW5.

EEA se reduce entonces a:

$$
\operatorname{Adm}_i(X)
\Rightarrow
\operatorname{Adm}_i(
\operatorname{WF}(X\cup\operatorname{Foot}(\rho))
).
$$

Del mismo modo, si $X,Y$ solapan, su unión semántica formal es:

$$
X\sqcup Y
:=
(T_X\cup T_Y,\Phi_X\cup\Phi_Y)
$$

seguida de well-formedness si fuese necesario.

OAM es exactamente la afirmación de que esa amalgama formal tiene alguna extensión admisible común.

Así REV-07 queda conectado limpiamente con la noción de admisibilidad, no con la definición del orden.

### 8. Relectura de EClosed

Sea $e$ un evento emergente actual del régimen con:

$$
\operatorname{src}(e)=s
$$

y:

$$
\operatorname{tgt}(e)=t.
$$

Entonces:

$$
\operatorname{EClosed}_i(X)
$$

significa ahora:

$$
s\in T_X
\Rightarrow
e,t\in T_X
$$

junto con los hechos estructurales relevantes:

$$
\operatorname{Event}(e),
\operatorname{src}(e,s),
\operatorname{tgt}(e,t)
\in
\Phi_X.
$$

Esto es una propiedad semántica de un fragmento procesual; no depende de su serialización.

### 9. Uniones de cadenas

Para una cadena creciente:

$$
X_0\preceq_i^{\mathrm{proc}}X_1\preceq_i^{\mathrm{proc}}\cdots,
$$

la unión formal es:

$$
T_\infty
=
\bigcup_\alpha T_{X_\alpha},
\qquad
\Phi_\infty
=
\bigcup_\alpha\Phi_{X_\alpha}.
$$

El lema anterior de REV-09 demuestra que EClosed se preserva. Lo único que queda por probar es:

$$
\operatorname{Adm}_i(X_\alpha)\;\forall\alpha
\Rightarrow
\operatorname{Adm}_i(X_\infty).
$$

Así la deuda de K2 queda tipada exactamente.

### 10. Secciones sincrónicas

Una instantánea no es el tipo primario del teorema emergentista.

Si en el futuro se dispone de una función/relación temporal suficientemente justificada, una sección sincrónica puede definirse como una operación derivada:

$$
\operatorname{Slice}_t(X)
$$

que selecciona contenido co-actual según esa teoría temporal.

No se necesita definir $\operatorname{Slice}_t$ para el teorema procesual.

### 11. Estado de REV-19

REV-19 puede marcarse **RESOLVED en su criterio de tipado y orden**:

- el objeto primario es un fragmento procesual semántico $(T_X,\Phi_X)$;
- el orden es inclusión de contenido positivo actual;
- representación y contenido se distinguen;
- incidencia queda tipada;
- admisibilidad queda explícitamente separada y permanece como deuda de REV-18/REV-20/REV-09/REV-07;
- la recuperación de snapshots es una extensión opcional, no una premisa del teorema.

Esto no resuelve la ontología de $\operatorname{Adm}_i$; simplemente elimina la ambigüedad de tipo que era el finding REV-19.

---


---

## Aplicabilidad fundacional — esqueleto cofinal set-sized

La restricción set-sized del Zorn ordinario no exige necesariamente que **todo** el régimen ontológico forme un conjunto.

Sea:

$$
(\mathfrak D_i^{\mathrm{proc}},\preceq_i)
$$

una colección potencialmente class-sized.

Supóngase que existe un subposet:

$$
\mathfrak C_i
\subseteq
\mathfrak D_i^{\mathrm{proc}}
$$

que satisface:

**S0 — no-vacuidad**

$$
\mathfrak C_i\neq\varnothing.
$$

**S1 — smallness**

$$
\mathfrak C_i
\text{ es set-sized}.
$$

**S2 — cofinalidad respecto del régimen**

$$
\forall X\in\mathfrak D_i^{\mathrm{proc}}
\;\exists Y\in\mathfrak C_i:
X\preceq_i Y.
$$

Sea:

$$
\mathfrak K_i^{C}
:=
\mathfrak C_i
\cap
\mathfrak K_i.
$$

Supóngase además que dentro de $\mathfrak C_i$ valen:

**S3 — cofinalidad cerrada**

$$
\forall X\in\mathfrak C_i
\;\exists Y\in\mathfrak K_i^{C}:
X\preceq_i Y.
$$

**S4 — inductividad por cadenas cerradas**

Toda cadena en $\mathfrak K_i^{C}$ tiene una cota superior en $\mathfrak K_i^{C}$.

**S5 — directedness interna de $\mathfrak C_i$**

$$
\forall X,Y\in\mathfrak C_i
\;\exists Z\in\mathfrak C_i:
X\preceq_i Z
\land
Y\preceq_i Z.
$$

### Teorema del esqueleto cofinal

Bajo S0–S5 existe:

$$
S_i\in\mathfrak K_i^{C}
$$

tal que:

$$
\boxed{
\forall X\in\mathfrak D_i^{\mathrm{proc}},
\quad
X\preceq_i S_i.
}
$$

**Demostración.**

Por S0 elegimos $X_0\in\mathfrak C_i$. Por S3 existe $Y_0\in\mathfrak K_i^{C}$ con $X_0\preceq_i Y_0$; luego $\mathfrak K_i^{C}\neq\varnothing$. Por S1, $\mathfrak C_i$ es un poset set-sized y también lo es $\mathfrak K_i^{C}$. Por S4, toda cadena en $\mathfrak K_i^{C}$ tiene una cota superior en $\mathfrak K_i^{C}$. Zorn produce un elemento maximal:

$$
S_i\in\mathfrak K_i^{C}.
$$

Sea $Y\in\mathfrak C_i$. Por S5 existe $W\in\mathfrak C_i$ con:

$$
S_i\preceq_i W
\land
Y\preceq_i W.
$$

Por S3 existe $Z\in\mathfrak K_i^{C}$ con:

$$
W\preceq_i Z.
$$

Entonces:

$$
S_i\preceq_i Z.
$$

Por maximalidad de $S_i$ en $\mathfrak K_i^{C}$:

$$
Z=S_i.
$$

Por tanto:

$$
Y\preceq_i S_i.
$$

Así $S_i$ es máximo de $\mathfrak C_i$.

Ahora sea:

$$
X\in\mathfrak D_i^{\mathrm{proc}}.
$$

Por S2 existe $Y\in\mathfrak C_i$ con:

$$
X\preceq_i Y.
$$

Y ya hemos probado:

$$
Y\preceq_i S_i.
$$

Luego:

$$
X\preceq_i S_i.
$$

$\square$

Como $S_i\in\mathfrak K_i^{C}\subseteq\mathfrak K_i$, el candidato es E-closed, y la propiedad demostrada de dominación global da:

$$
\boxed{
\operatorname{SemTotal}_i(S_i).
}
$$

Este teorema es exclusivamente semántico. No permite sustituir $S_i$ por un $R_i$ ni concluir $\operatorname{ExistsR}$. La existencia pertenece a REV-07; REV-24 solo añade presentación:

$$
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
\Rightarrow
\operatorname{ExistsR},
$$

y:

$$
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
+
\operatorname{SemTotal}_i(S_i)
+
\mathrm{OTB}_i
\Rightarrow
\operatorname{Presents}_i(S_i,R_i)
\Rightarrow
\operatorname{WitnessedR}.
$$

Ninguna de estas inferencias decide One-$R$/Many-$R$; esa cuestión pertenece al metalenguaje de índices.

### Consecuencia

Para aplicar Zorn al régimen no es necesario asumir:

$$
\mathfrak D_i^{\mathrm{proc}}
\text{ set-sized}.
$$

Basta demostrar la existencia de un **esqueleto cofinal set-sized** que preserve las obligaciones K relevantes.

Esto no elimina la deuda fundacional: la traslada a justificar S1–S2 sin presuponer ya un máximo.

La alternativa sería adoptar explícitamente una teoría de clases y un principio de maximalidad de clases suficientemente fuerte; esa ruta no se presupone aquí.

---


---

## REV-20 — construcción estructural de una extensión E-closed

K1 exige:

$$
\forall X\in\mathfrak D_i^{\mathrm{proc}}
\;\exists Y\in\mathfrak K_i:
X\preceq_i Y.
$$

En vez de asumir esa existencia global, puede derivarse de principios locales de preservación de admisibilidad.

### 1. Obligaciones emergentes pendientes

Sea:

$$
X=(T_X,\Phi_X)
\in
\mathfrak D_i^{\mathrm{proc}}.
$$

Para cada evento emergente actual $e$ con:

$$
\operatorname{src}(e)=s,
\qquad
\operatorname{tgt}(e)=t,
$$

hay una obligación pendiente sobre $X$ si:

$$
s\in T_X
$$

pero falta alguno de los contenidos exigidos por EClosed: el token de evento, su target o los hechos estructurales Event/src/tgt.

Sea:

$$
\operatorname{Pend}_i(X)
$$

la colección de obligaciones pendientes. Entonces:

$$
\boxed{
\operatorname{EClosed}_i(X)
\iff
\operatorname{Pend}_i(X)=\varnothing.
}
$$

### 2. OEA — One-Event Admissible Extension

Si:

$$
\operatorname{Adm}_i(X)
$$

y:

$$
o\in\operatorname{Pend}_i(X),
$$

OEA exige que exista un dominio admisible:

$$
Y\in\mathfrak D_i^{\mathrm{proc}}
$$

tal que:

$$
X\preceq_i Y
$$

y la obligación concreta $o$ quede satisfecha en $Y$.

OEA no dice que $Y$ sea E-closed. Solo afirma que **un evento emergente actual individual** puede incorporarse sin destruir admisibilidad.

Por tanto OEA es estrictamente local y más débil que K1.

### 3. CUA — Chain Union Admissibility

Para toda cadena set-indexed creciente de dominios admisibles:

$$
\{X_\alpha\}_{\alpha<\lambda},
$$

CUA exige que la unión semántica:

$$
X_\lambda
=
\left(
\bigcup_{\alpha<\lambda}T_{X_\alpha},
\;
\bigcup_{\alpha<\lambda}\Phi_{X_\alpha}
\right)
$$

sea well-formed y admisible:

$$
\operatorname{Adm}_i(X_\lambda).
$$

CUA es exactamente la parte ontológica de K2 que REV-09 mantiene abierta.

### 4. SO — Set-sized closure cone

Para un dominio inicial $X$, sea $\operatorname{Cone}_i(X)$ el contenido que puede aparecer mediante una cadena **finita** de eventos emergentes actuales cuyo primer source ya está en $T_X$.

SO$_i(X)$ exige que los tokens, eventos y hechos estructurales de ese cono estén contenidos en una colección set-sized.

No hace falta que todo el régimen sea set-sized:

$$
\boxed{
\operatorname{Cone}_i(X)\text{ set-sized}
}
$$

es suficiente para construir la clausura de $X$.

Esto es más débil que smallness global y conecta directamente con REV-22.

### 5. Lema de una ronda

Sea $X$ admisible y supóngase que:

$$
\operatorname{Pend}_i(X)
$$

es set-sized.

Bien ordenamos las obligaciones pendientes:

$$
\{o_\alpha\}_{\alpha<\kappa}.
$$

Partimos de:

$$
Y_0=X.
$$

En cada sucesor, si $o_\alpha$ sigue pendiente, aplicamos OEA; si ya fue satisfecha por una extensión anterior, dejamos el dominio sin cambio.

En ordinales límite tomamos la unión; CUA preserva admisibilidad.

Al terminar la enumeración obtenemos un dominio admisible:

$$
\operatorname{Round}_i(X)
$$

que satisface **todas las obligaciones que ya estaban pendientes en $X$**.

Las extensiones realizadas durante la ronda pueden activar obligaciones nuevas; esas se dejan para la ronda siguiente.

### 6. Iteración por profundidad finita

Definimos:

$$
X_0=X,
$$

y:

$$
X_{n+1}
=
\operatorname{Round}_i(X_n).
$$

Cada $X_n$ es admisible por OEA + CUA.

Tomamos:

$$
X_\omega
=
\bigcup_{n<\omega}X_n.
$$

Por CUA:

$$
\operatorname{Adm}_i(X_\omega).
$$

### 7. Teorema de clausura admisible

**Teorema REV-20.1.**

Si para un dominio admisible $X$ valen:

1. OEA$_i$;
2. CUA$_i$ para cadenas set-indexed;
3. SO$_i(X)$;
4. elección suficiente para bien ordenar cada conjunto de obligaciones pendientes;

entonces existe:

$$
Y\in\mathfrak D_i^{\mathrm{proc}}
$$

tal que:

$$
X\preceq_i Y
$$

y:

$$
\operatorname{EClosed}_i(Y).
$$

Podemos tomar:

$$
Y=X_\omega.
$$

**Demostración.**

Supongamos que existe una obligación pendiente $o$ en $X_\omega$ con source $s$.

Como:

$$
s\in T_{X_\omega}
=
\bigcup_{n<\omega}T_{X_n},
$$

existe un $n$ finito con:

$$
s\in T_{X_n}.
$$

Entonces $o$ ya está pendiente —o queda satisfecha— durante la construcción de:

$$
X_{n+1}
=
\operatorname{Round}_i(X_n).
$$

Por definición de Round, al finalizar esa ronda $o$ está satisfecha.

Como el orden procesual solo añade contenido positivo, una obligación satisfecha no vuelve a quedar insatisfecha.

Contradicción.

Luego:

$$
\operatorname{Pend}_i(X_\omega)=\varnothing,
$$

es decir:

$$
\operatorname{EClosed}_i(X_\omega).
$$

Además:

$$
X=X_0\preceq_i X_\omega.
$$

$\square$

### 8. Consecuencia para K1

Si OEA$_i$, CUA$_i$ y SO$_i(X)$ valen para todo:

$$
X\in\mathfrak D_i^{\mathrm{proc}},
$$

entonces:

$$
\boxed{K1_i.}
$$

En forma compacta:

$$
\boxed{
\mathrm{OEA}_i
+
\mathrm{CUA}_i
+
\mathrm{SO}_i
\Rightarrow
K1_i.
}
$$

### 9. Por qué no es K1 rebautizada

Las tres premisas pueden fallar independientemente:

- **OEA** falla si existe un evento emergente actual individual que no puede incorporarse a ninguna extensión admisible del dominio que contiene su source;
- **CUA** falla si una acumulación creciente de fragmentos admisibles deja de ser admisible;
- **SO** falla si el cono emergente actual generado por un dominio no puede controlarse mediante una colección set-sized.

Ninguna de ellas afirma directamente que exista una extensión E-closed completa.

### 10. Relación con otros findings

- **REV-07 / EEA:** una EEA suficientemente fuerte para footprints de eventos implica OEA.
- **REV-09:** CUA es exactamente la deuda de admisibilidad que queda en K2.
- **REV-18:** OEA necesita una semántica independiente de Adm$_i$ y del footprint ontológico de un evento.
- **REV-22:** SO puede derivarse de smallness local del cono, de un esqueleto cofinal adecuado o de compromisos fundacionales más fuertes.

### 11. Compatibilidad con el Muro

La prueba es estructural, no empírica.

No exige conocer todos los dominios, identificar $R_i$ ni inspeccionar todas las obligaciones desde dentro. Exige demostrar propiedades generales de la ontología: OEA, CUA y SO.

Por tanto es compatible con el Muro.

### 12. Estado de REV-20

REV-20 pasa de **OPEN** a **PARTIAL**.

K1 ya no es una existencia global opaca: se deriva de tres obligaciones locales y separables.

No se marca RESOLVED porque OEA, CUA y SO todavía requieren justificación ontológica/fundacional independiente.

---

---

## REV-18/REV-20 — admisibilidad estructural mínima

La arquitectura actual permite preguntar si el predicado abstracto $\operatorname{Adm}_i$ añade realmente contenido o si puede reducirse a las condiciones semánticas ya impuestas a un fragmento procesual.

### 1. Definición candidata

Definimos:

$$
\operatorname{StructAdm}_i(X)
$$

si y solo si $X=(T_X,\Phi_X)$ satisface PW1–PW6 del tipo procesual normalizado:

1. todos sus tokens pertenecen al régimen $i$;
2. todos los tokens y hechos incluidos son actuales;
3. todo hecho incluido contiene sus relata en $T_X$;
4. todo evento incluido contiene source y target únicos;
5. la precedencia incluida es acíclica/coherente;
6. el fragmento contiene solo contenido positivo, de modo que una extensión puede añadir hechos sin retractar los anteriores.

La propuesta candidata es:

$$
\boxed{
\operatorname{Adm}_i(X)
:=
\operatorname{StructAdm}_i(X).
}
$$

Esta definición no dice que $X$ sea total, cerrado, maximal ni amalgamable. Solo dice que es un fragmento ontológico positivo coherente de contenido actual.

### 2. OEA se deriva

Sea $X$ estructuralmente admisible y sea $e$ un evento emergente actual con:

$$
\operatorname{src}(e)=s\in T_X,
\qquad
\operatorname{tgt}(e)=t.
$$

Como $e$ es un evento actual del mismo régimen, los tokens:

$$
e,t
$$

y los hechos:

$$
\operatorname{Event}(e),
\quad
\operatorname{src}(e,s),
\quad
\operatorname{tgt}(e,t)
$$

son contenido actual del régimen $i$.

Sea $Y$ el fragmento obtenido añadiendo ese footprint mínimo a $X$.

Entonces:

- PW1 se preserva porque source, evento y target están en el mismo régimen procesual;
- PW2 se preserva porque solo se añade contenido actual;
- PW3/PW4 se preservan añadiendo todos los relata/endpoints obligatorios;
- PW5 se preserva porque una relación de precedencia genuinamente actual no puede introducir un ciclo finito real; cualquier ciclo finito añadido sería ya una incoherencia del propio contenido actual;
- PW6 se preserva porque solo añadimos contenido positivo.

Por tanto:

$$
\boxed{
\operatorname{StructAdm}_i(X)
\land
o\in\operatorname{Pend}_i(X)
\Rightarrow
\exists Y\succeq_i X:
\operatorname{StructAdm}_i(Y)
\land
o\text{ satisfecha}.
}
$$

Es decir:

$$
\boxed{\mathrm{OEA}_i.}
$$

### 3. CUA se deriva para cadenas set-indexed

Sea:

$$
\{X_\alpha\}_{\alpha<\lambda}
$$

una cadena set-indexed de fragmentos estructuralmente admisibles, y definamos:

$$
T_\infty
=
\bigcup_{\alpha<\lambda}T_{X_\alpha},
\qquad
\Phi_\infty
=
\bigcup_{\alpha<\lambda}\Phi_{X_\alpha}.
$$

Como la familia está indexada por un conjunto y cada carrier es set-sized, $T_\infty$ y $\Phi_\infty$ son conjuntos en ZFC.

PW1/PW2 se preservan por unión.

PW3/PW4 se preservan porque cualquier hecho/evento de la unión apareció ya en algún estadio que contenía sus relata/endpoints.

PW5 también se preserva. Si la unión contuviese un ciclo finito de precedencia, las finitísimas aristas del ciclo aparecerían en finitísimos estadios. Como la familia es una cadena, existe un estadio que contiene todas ellas, contradiciendo su coherencia.

PW6 se preserva porque la unión solo acumula contenido positivo.

Por tanto:

$$
\boxed{
\operatorname{StructAdm}_i(X_\alpha)\;\forall\alpha<\lambda
\Rightarrow
\operatorname{StructAdm}_i\left(\bigcup_{\alpha<\lambda}X_\alpha\right).
}
$$

Es decir:

$$
\boxed{\mathrm{CUA}_i}
$$

para cadenas set-indexed.

### 4. OAM también se deriva

Sean $X,Y$ dos fragmentos estructuralmente admisibles del mismo régimen.

Consideremos:

$$
Z=(T_X\cup T_Y,\Phi_X\cup\Phi_Y).
$$

PW1–PW4 y PW6 se preservan como antes.

Para PW5, cualquier ciclo finito en $Z$ estaría compuesto por hechos de precedencia actuales. Si la semántica de $\prec$ es una precedencia/dependencia estricta realmente instanciada, tal ciclo no puede existir en la realidad procesual subyacente.

Así:

$$
\boxed{
\operatorname{StructAdm}_i(X)
\land
\operatorname{StructAdm}_i(Y)
\Rightarrow
\operatorname{StructAdm}_i(X\cup Y).
}
$$

y:

$$
X\preceq_i Z
\land
Y\preceq_i Z.
$$

Por tanto OAM se deriva, incluso sin exigir solapamiento explícito, **una vez que ambos dominios ya están independientemente tipados como pertenecientes al mismo régimen**.

Esto no vuelve circular SameRegime: la pertenencia al régimen sigue viniendo de $\sim$, no de la existencia de $Z$.

### 5. EEA se deriva para footprints de $\Lambda_*$

El mismo argumento vale para una instancia actual:

$$
\rho:\lambda(q,r),
\qquad
\lambda\in\Lambda_*.
$$

Si $q\in T_X$, añadir $r$, la instancia $\rho$ y su footprint estructural positivo produce otro fragmento estructuralmente admisible.

Por tanto la versión local de EEA necesaria para REV-07 se deriva de StructAdm.

### 6. Consecuencia para los findings

Si se acepta:

$$
\operatorname{Adm}_i
:=
\operatorname{StructAdm}_i,
$$

entonces:

- la parte de incidencia/admisibilidad de REV-18 deja de ser una premisa abierta: incidencia es pertenencia al carrier semántico y admisibilidad es well-formedness actual positiva;
- REV-09 queda resuelto para cadenas set-indexed;
- OEA y OAM/EEA dejan de ser premisas independientes;
- REV-20 se reduce a SO/smallness del cono emergente;
- REV-07 se reduce a justificar $\Lambda_*$ y la identidad de régimen, no la directedness.

### 7. Precio conceptual

Esta reducción adopta una concepción concreta de «dominio ontológico»:

> un dominio es un fragmento semántico positivo de contenido actual, no una entidad adicional de la ontología.

Eso evita reificar el dominio como sustancia u objeto colector.

Pero requiere aceptar que **todo fragmento positivo well-formed de hechos/tokens actuales es un dominio legítimo** para el propósito del teorema.

Si la doctrina exige restricciones adicionales sobre qué fragmentos cuentan como dominio —por ejemplo completitud causal, cierre nomológico, criterios mereológicos especiales o restricciones globales— entonces StructAdm sería demasiado débil y los findings de admisibilidad tendrían que reabrirse.

### 8. Cobertura semántica del contenido actual

Para que un máximo de estos fragmentos cubra todo el contenido actual **representable por el formalismo**, se exige además cobertura atómica:

$$
\mathrm{COV}_i:
$$

para todo token/hecho actual $q$ del régimen representable por la firma vigente existe algún fragmento estructuralmente admisible $X$ con:

$$
q\trianglelefteq_i X.
$$

Con StructAdm, COV es inmediata para tokens simples representables mediante fragmentos mínimos; para eventos/hechos relacionales representables se toma el footprint well-formed mínimo que contiene sus relata obligatorios.

Si $S_i$ domina todos los dominios admisibles, entonces por COV contiene todo token/hecho actual cubierto por esa condición.

Así el máximo formal $S_i$ no es solo maximal respecto de una familia arbitraria: demuestra exhaustividad semántica respecto del contenido cubierto por la firma y por COV. No se sigue todavía $\exists R_i[\operatorname{Presents}_i(S_i,R_i)\land\operatorname{OntTotal}_i(R_i)]$ sin REV-24/$\mathrm{OTB}_i$.

### 9. Estado propuesto

Esta sección permite cerrar REV-18 y REV-09 **si** se adopta normativamente StructAdm como la noción de dominio admisible.

REV-20 quedaría PARTIAL exclusivamente por SO/smallness.

REV-07 permanecería PARTIAL solo por la justificación de $\Lambda_*$ y la individuación del régimen.

---

---

## REV-20 — smallness local del cono emergente

Tras adoptar admisibilidad estructural mínima, OEA y CUA dejan de ser premisas independientes. El único ingrediente restante de la construcción de K1 es SO: que el cono emergente generado por un dominio set-sized siga siendo set-sized.

### 1. LSE — Local Set-like Emergence

Definimos:

$$
\mathrm{LSE}_i:
$$

para todo conjunto de tokens $S$ del régimen, la colección de eventos emergentes actuales cuyo source pertenece a $S$ es un conjunto:

$$
\{
e
\mid
\operatorname{Emergent}_i(e)
\land
\operatorname{src}(e)\in S
\}
\text{ es set-sized}.
$$

Como `src` y `tgt` son funcionales para cada token de evento, los targets de ese conjunto de eventos forman también un conjunto por Replacement.

LSE no exige que el régimen completo sea set-sized. Permite una realidad class-sized con ramificación emergente localmente set-like.

### 2. Construcción por niveles

Sea $X=(T_X,\Phi_X)$ con $T_X$ set-sized.

Definimos:

$$
S_0=T_X.
$$

Dado $S_n$, sea:

$$
E_n
:=
\{
e
\mid
\operatorname{Emergent}_i(e)
\land
\operatorname{src}(e)\in S_n
\}.
$$

Por LSE, $E_n$ es set-sized.

Sea:

$$
U_n
:=
\{
\operatorname{tgt}(e)
\mid
e\in E_n
\}.
$$

Por Replacement, $U_n$ es set-sized.

Definimos:

$$
S_{n+1}
:=
S_n
\cup
E_n
\cup
U_n.
$$

Cada $S_n$ es un conjunto.

Finalmente:

$$
S_\omega
:=
\bigcup_{n<\omega}S_n.
$$

Por Union/Replacement sobre $\omega$, $S_\omega$ es set-sized.

Todo token/evento alcanzable desde $T_X$ mediante una cadena finita de eventos emergentes aparece en algún $S_n$.

Por tanto:

$$
\boxed{
\mathrm{LSE}_i
\Rightarrow
\mathrm{SO}_i(X)
}
$$

para todo dominio set-sized $X$.

### 3. Consecuencia para K1

Con StructAdm, ya se demostraron OEA y CUA.

Así:

$$
\boxed{
\mathrm{StructAdm}_i
+
\mathrm{LSE}_i
\Rightarrow
K1_i.
}
$$

más precisamente: todo dominio set-sized estructuralmente admisible posee una extensión set-sized E-closed.

### 4. Qué significa el posible fallo

Si LSE falla, existe algún conjunto set-sized de sources desde el que parten **proper-class many** eventos emergentes actuales.

Entonces una clausura emergente de un fragmento set-sized puede verse forzada a abandonar el universo de dominios set-sized en un solo paso.

Ésta es una forma precisa de potencialismo/indefinite extensibility capaz de bloquear K1 dentro de fundamentos ordinarios.

### 5. Relación con REV-22

LSE resuelve la smallness **local de cada cierre**.

No demuestra que la colección:

$$
\mathfrak D_i^{\mathrm{proc}}
$$

de todos los dominios del régimen sea set-sized.

Por tanto:

- REV-20 puede resolverse bajo StructAdm + LSE;
- REV-22 sigue abierto como condición de aplicabilidad global de Zorn, salvo que se exhiba un esqueleto cofinal set-sized o se adopten fundamentos de clases adecuados.

---

---

## REV-20 — reducción de LSE a branching set-like por token

Definimos la condición puntual:

$$
\mathrm{PSB}_i:
$$

para todo token de estado $s$ del régimen, la colección de eventos emergentes actuales con source $s$ es set-sized:

$$
\operatorname{Out}_i(s)
:=
\{e\mid \operatorname{Emergent}_i(e)\land \operatorname{src}(e)=s\}
$$

es un conjunto.

### Proposición

En ZFC/NBG con Replacement/Union ordinarios:

$$
\boxed{
\mathrm{PSB}_i
\Rightarrow
\mathrm{LSE}_i.
}
$$

**Demostración.** Sea $S$ un conjunto de sources. Por PSB, para cada $s\in S$ existe el conjunto $\operatorname{Out}_i(s)$. Por Replacement obtenemos una familia set-indexed:

$$
\{\operatorname{Out}_i(s)\mid s\in S\}.
$$

Por Union:

$$
\bigcup_{s\in S}\operatorname{Out}_i(s)
$$

es un conjunto.

Pero esa unión es exactamente la colección de eventos emergentes actuales cuyo source pertenece a $S$. Luego LSE. $\square$

### Consecuencia

REV-20 puede formularse con una única condición local por token:

$$
\boxed{
\operatorname{StructAdm}_i
+
\mathrm{PSB}_i
\Rightarrow
K1_i.
}
$$

PSB no afirma que el régimen sea set-sized ni que exista un máximo. Solo excluye una explosión local en la que un único estado actual sea source de proper-class many eventos emergentes actuales.

### Interpretación

Si PSB falla, queda bloqueada esta **ruta local set-sized hacia K1/\operatorname{SemTotal}_i** mediante cierre de eventos:

> desde un único estado set-sized parten proper-class many actualizaciones emergentes actualmente instanciadas.

Esa posibilidad es lógicamente distinta del potencialismo ordinario de «siempre hay una extensión más»; es una ramificación propia-clase ya en un solo paso. Pero no implica $\operatorname{NoR}$ ni refuta por sí sola $\operatorname{ExistsR}$ mediante otras rutas de clausura.

---

---

## REV-20 — caracterización exacta de K1 mediante PSB

Con la arquitectura normativa actual podemos demostrar que PSB no es solo suficiente para K1: es también necesaria.

### 1. Premisas de contexto

Trabajamos con:

1. dominios procesuales set-sized;
2. $\operatorname{Adm}_i:=\operatorname{StructAdm}_i$;
3. cobertura mínima COV$_i$: todo token actual del régimen pertenece a algún fragmento admisible set-sized;
4. `EClosed_i` exige que, si el source de un evento emergente actual pertenece al dominio, entonces el token de evento, su target y su footprint estructural también pertenecen al dominio.

### 2. K1 implica PSB

Supongamos K1$_i$.

Sea $s$ un estado actual cualquiera del régimen.

Por COV existe un dominio set-sized:

$$
X_s\in\mathfrak D_i^{\mathrm{proc}}
$$

tal que:

$$
s\in T_{X_s}.
$$

Por K1 existe:

$$
Y_s\in\mathfrak K_i
$$

con:

$$
X_s\preceq_i Y_s.
$$

Como $Y_s$ es E-closed, para todo evento emergente actual $e$ con:

$$
\operatorname{src}(e)=s,
$$

se cumple:

$$
e\in T_{Y_s}.
$$

Por tanto:

$$
\operatorname{Out}_i(s)
\subseteq
T_{Y_s}.
$$

Pero $T_{Y_s}$ es un conjunto. Luego:

$$
\operatorname{Out}_i(s)
$$

es set-sized.

Como $s$ era arbitrario:

$$
\boxed{K1_i\Rightarrow \mathrm{PSB}_i.}
$$

### 3. PSB implica K1

La dirección recíproca ya fue demostrada:

$$
\mathrm{PSB}_i
\Rightarrow
\mathrm{LSE}_i
\Rightarrow
\mathrm{SO}_i
$$

y, con StructAdm, OEA/CUA se derivan. La construcción por rondas produce para cada dominio $X$ una extensión E-closed set-sized.

Por tanto:

$$
\boxed{\mathrm{PSB}_i\Rightarrow K1_i.}
$$

### 4. Equivalencia

Bajo las premisas de contexto:

$$
\boxed{
K1_i
\iff
\mathrm{PSB}_i.
}
$$

Así REV-20 deja de ser una cuestión vaga sobre «si existen cierres». Tiene una condición estructural exacta:

> K1 falla exactamente cuando existe al menos un estado actual que es source de proper-class many eventos emergentes actuales.

### 5. Consecuencia para No-R

Esta equivalencia identifica una vía precisa por la que el potencialismo/extensibilidad podría bloquear la prueba dentro de dominios set-sized:

$$
\neg K1_i
\iff
\neg\mathrm{PSB}_i
$$

es decir, una explosión de ramificación emergente propia-clase desde algún estado.

El potencialismo ordinario de «siempre puede añadirse algo más» no basta por sí solo para refutar K1: mientras la ramificación sea set-like, el cierre por rondas existe como dominio set-sized.

### 6. Estado lógico

REV-20 ya no necesita más matemática de cierre.

Su única deuda es filosófico-fundacional:

$$
\boxed{\mathrm{PSB}_i?}
$$

Si PSB se adopta o deriva independientemente, REV-20 puede marcarse RESOLVED.

---

---

## Teorema directo de exhaustividad semántica sobre una componente $\Lambda$ tipada

Este teorema no define el contexto $i$ ni toma cardinalidad de $i$. Fijado un parámetro de contexto ya disponible en el metalenguaje y un seed $q_i$, construye un máximo semántico **relativo a la componente finita** generada por $\Lambda_i$.

### 0. Smallness doctrinal de la capa semántica

La condición común no es PON ni CSet. Para cualquier carrier semántico candidato $T$ definimos:

$$
\operatorname{SemCarrierSmall}(T)
:\Longleftrightarrow
T\text{ es set-sized}.
$$

Esta es la premisa doctrinal de **la implementación semántica set-based actual**, no una tesis ontológica de que $R$ sea un conjunto. Las rutas la descargan de maneras distintas:

$$
\mathrm{PON}_i
\Rightarrow
\operatorname{SemCarrierSmall}(T^{\Lambda}_{i,q}),
$$

mientras CSet es exactamente $\operatorname{SemCarrierSmall}(T_q^{\mathcal C})$ para la ruta generalizada, y TransClSmall la obtiene en un estadio transfinito estabilizado.

Por tanto PON, CSet y TransClSmall son condiciones de implementación/ruta; ninguna es por sí sola condición de existencia de $R$. SigSmall y ActualSep siguen siendo obligaciones adicionales sobre la firma y la selección del diagrama positivo.

### 1. PON$_i$ — Pointwise Ontological Neighborhood Smallness

Sea:

$$
N_i(q_i)
:=
\{r_i\mid q_i\bowtie_i r_i\}.
$$

Definimos:

$$
\mathrm{PON}_i:
\quad
\forall q_i\;
N_i(q_i)\text{ es set-sized}.
$$

PON$_i$ afirma smallness de vecinos dentro del tipo $i$. No cuantifica sobre contextos ni convierte $i$ en una colección.

Cuando la incidencia de eventos emergentes está incluida en $\Lambda_i$, PON$_i$ implica la versión local correspondiente de PSB$_i$.

### 2. La componente finita del seed es set-sized

Fijemos $q_i$ y definamos:

$$
S_0=\{q_i\},
$$

$$
S_{n+1}
=
S_n
\cup
\bigcup_{x_i\in S_n}N_i(x_i).
$$

Por PON$_i$, Replacement y Union, cada $S_n$ es set-sized. Entonces:

$$
S_\omega
=
\bigcup_{n<\omega}S_n
$$

es set-sized.

Como $\sim_i$ es la clausura reflexivo-transitiva finita de $\bowtie_i$:

$$
\boxed{
S_\omega
=
[q_i]_{\sim_i}
=:
T^{\Lambda}_{i,q}.
}
$$

Por tanto:

$$
\boxed{
\mathrm{PON}_i
\Rightarrow
T^{\Lambda}_{i,q}\text{ es set-sized}.
}
$$

Este resultado no atribuye cardinalidad al parámetro de contexto $i$ ni identifica $T^{\Lambda}_{i,q}$ con toda la realidad tipada.

### 3. Smallness de los hechos

Sea:

$$
T^{\Lambda}_{i,q}
=
[q_i]_{\sim_i}.
$$

Bajo:

$$
\mathrm{SigSmall}_i:
\quad
\mathcal L_i\text{ set-sized}
\land
\forall\sigma_i\in\mathcal L_i\;
\operatorname{ar}(\sigma_i)\text{ set-sized},
$$

el espacio:

$$
\operatorname{Atoms}_{\mathcal L_i}(T^{\Lambda}_{i,q})
$$

es set-sized.

Con $\mathrm{ActualSep}_i$:

$$
\Phi^{\Lambda,\mathrm{all}}_{i,q}
=
\{
\varphi_i\in
\operatorname{Atoms}_{\mathcal L_i}(T^{\Lambda}_{i,q})
\mid
\operatorname{Actual}_i(\varphi_i)
\}.
$$

Esta colección es precisamente el **diagrama atómico positivo actual** del carrier bajo $\mathcal L_i$:

$$
\Phi^{\Lambda,\mathrm{all}}_{i,q}
=
\operatorname{Diag}^{+}_{\mathcal L_i}(T^{\Lambda}_{i,q}).
$$

Se usa la noción Robinson/Hodges de positive diagram: átomos verdaderos con los elementos nombrados; no el diagrama atómico completo con literales negativos.

### 4. Construcción directa

Definimos:

$$
S^{\Lambda,*}_{i,q}
:=
(T^{\Lambda}_{i,q},\Phi^{\Lambda,\mathrm{all}}_{i,q}).
$$

Sea $\mathfrak D^{\Lambda}_{i,q}$ el poset de fragmentos StructAdm cuyo carrier y hechos están soportados en esa componente.

Para cualquier:

$$
X_i=(T_X,\Phi_X)
\in
\mathfrak D^{\Lambda}_{i,q},
$$

se tiene:

$$
T_X\subseteq T^{\Lambda}_{i,q}
$$

y:

$$
\Phi_X\subseteq\Phi^{\Lambda,\mathrm{all}}_{i,q}.
$$

Por tanto:

$$
\boxed{
\forall X_i\in\mathfrak D^{\Lambda}_{i,q},
\quad
X_i\preceq_i S^{\Lambda,*}_{i,q}.
}
$$

### 5. EClosed relativo a la componente

Si los footprints de los eventos emergentes relevantes están incluidos en $\Lambda_i$, source, evento y target permanecen dentro de la componente finita. Entonces:

$$
\operatorname{EClosed}^{\Lambda}_{i,q}(S^{\Lambda,*}_{i,q}).
$$

Esta afirmación es closure-relative; no demuestra que la componente contenga todo $Real_i$.

### 6. Teorema directo closure-relative

Supóngase, para un contexto fijo $i$ y seed $q_i$:

1. PON$_i$;
2. $\mathrm{SigSmall}_i$;
3. $\mathrm{ActualSep}_i$;
4. StructAdm relativo a $T^{\Lambda}_{i,q}$;
5. estabilidad de los footprints emergentes bajo $\Lambda_i$.

Entonces:

$$
\boxed{
\operatorname{SemTotal}^{\Lambda}_{i,q}
(S^{\Lambda,*}_{i,q}).
}
$$

donde SemTotal$^{\Lambda}_{i,q}$ significa máximo semántico de $\mathfrak D^{\Lambda}_{i,q}$.

### 7. Upgrade genealógico

El resultado anterior puede llamarse $\operatorname{SemTotal}_i$ **solo** después de establecer que la componente reconstruye la clausura genealógica:

$$
\mathrm{RS}^{\mathrm{gen}}_{\Lambda,i}:
\quad
x_i\in T^{\Lambda}_{i,q}
\Rightarrow
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i),
$$

$$
\mathrm{RC}^{\mathrm{gen}}_{\Lambda,i}:
\quad
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i)
\Rightarrow
x_i\in T^{\Lambda}_{i,q}.
$$

Con ambas:

$$
\boxed{
T^{\Lambda}_{i,q}
=
\{x_i\mid
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i)
\}.
}
$$

y, junto con la adecuación factual/representacional necesaria:

$$
\operatorname{SemTotal}^{\Lambda}_{i,q}
\Longrightarrow
\operatorname{SemTotal}_i.
$$

Por tanto la conectividad nunca vuelve a definir el índice: primero produce una componente semántica; RS/RC deciden si esa componente reconstruye la genealogía.


### 8. REV-24 — presentación semántica de una realidad genealógica

**CURRENT TARGET.** REV-07 debe establecer primero $\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)$. REV-24 no produce existencia ontológica; intenta demostrar:

$$
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
+
\operatorname{SemTotal}_i(S_i)
+
\mathrm{OA}_i(S_i;\mathfrak G_i)
+
\mathrm{MC}_i(S_i;\mathfrak G_i)
+
\mathrm{RA}_i(S_i,R_i)
\Rightarrow
\operatorname{Presents}_i(S_i,R_i).
$$

con:

$$
\mathrm{OA}_i(S;\mathfrak G_i)
:=
\forall a\in T_S\exists x[
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x)
\land
\operatorname{Den}_i(a,x)
],
$$

$$
\mathrm{MC}_i(S;\mathfrak G_i)
:=
\forall x[
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x)
\Rightarrow
\exists a\in T_S\operatorname{Den}_i(a,x)
].
$$

RA debe preservar/reflejar estructura generativa y procesual, no solo membership.

**SUPERSEDED DERIVATIONAL LAYER.** Las subsecciones 8.1–8.5 conservan el desarrollo seed/CoReal anterior y sus stress tests. Son historia técnica útil para evaluar $\Lambda_*$/$\mathcal C_*$, pero quedan superseded donde tratan CoReal como primitivo, hacen de SR una obligación de REV-24 o presentan OTB como productor de existencia.

El teorema anterior demuestra exhaustividad respecto del tipo formal elegido: todos los fragmentos semánticos admisibles quedan contenidos en $S_i^*$.

No demuestra que el objeto semántico sea él mismo un alcance ontológico. La formulación:

$$
\operatorname{OntTotal}_i(S_i^*)
$$

queda **SUPERSEDED por error de tipos**.

La arquitectura vigente distingue:

$$
S_i
\quad\text{(presentación semántica)}
$$

de:

$$
R_i
\quad\text{(alcance ontológico)}.
$$

Y reserva:

$$
\operatorname{Presents}_i(S_i,R_i)
$$

para el puente entre ambos.

#### 8.1. Carrier anchoring vigente

Para la componente finita tipada:

$$
T^{\Lambda}_{i,q}
=
[q_i]_{\sim_i},
$$

OA se formula respecto de la genealogía objetivo:

$$
\mathrm{OA}_i(S;\mathcal O_i)
:=
\forall a_i\in T_S\;
\exists x_i[
\operatorname{Generated}^{*}_i(\mathcal O_i,x_i)
\land
\operatorname{Den}_i(a_i,x_i)
].
$$

Con denotación canónica:

$$
\mathrm{CD}_{i,q}^{\Lambda}:
\quad
x_i\in T^{\Lambda}_{i,q}
\Rightarrow
\operatorname{Den}_i(x_i,x_i),
$$

y soundness genealógica:

$$
\mathrm{RS}^{\mathrm{gen}}_{\Lambda,i}:
\quad
x_i\in T^{\Lambda}_{i,q}
\Rightarrow
\operatorname{Generated}^{*}_i(\mathcal O_i,x_i),
$$

se obtiene:

$$
\boxed{
\mathrm{RS}^{\mathrm{gen}}_{\Lambda,i}
+
\mathrm{CD}_{i,q}^{\Lambda}
\Rightarrow
\mathrm{OA}_i(S^{\Lambda,*}_{i,q};\mathcal O_i).
}
$$

En Ruta A, EXT-01 + EdgeTyped$_i$ + seed tipado proporcionan una vía hacia RS; el anclaje factual fuerte sigue dependiendo de RA/REV-25.

#### 8.2. Membership Completeness vigente

MC se formula:

$$
\mathrm{MC}_i(S;\mathcal O_i)
:=
\forall x_i[
\operatorname{Generated}^{*}_i(\mathcal O_i,x_i)
\Rightarrow
\exists a_i\in T_S\;
\operatorname{Den}_i(a_i,x_i)
].
$$

La obligación de reconstruction completeness es:

$$
\mathrm{RC}^{\mathrm{gen}}_{\Lambda,i}:
\quad
\operatorname{Generated}^{*}_i(\mathcal O_i,x_i)
\Rightarrow
x_i\in T^{\Lambda}_{i,q}.
$$

Por tanto:

$$
\boxed{
\mathrm{RC}^{\mathrm{gen}}_{\Lambda,i}
+
\mathrm{CD}_{i,q}^{\Lambda}
\Rightarrow
\mathrm{MC}_i(S^{\Lambda,*}_{i,q};\mathcal O_i).
}
$$

Así RS controla sobreinclusión; RC controla subinclusión. Ninguna define el índice ni la genealogía: ambas comparan una reconstrucción $\Lambda_i$ con $\operatorname{Cl}^{G}_i(\mathcal O_i)$ ya caracterizada independientemente.


##### Posibles contraejemplos a $\mathrm{RC}^{\mathrm{gen}}_{\Lambda,i}$

RC falla si existe $x_i$ generado junto con $q_i$ en el contexto fijo $i$ pero cuya integración solo puede establecerse mediante:

- una condición global que no se descompone en enlaces token-specific;
- una dependencia esencialmente de límite sin cadena finita de incidencias;
- una relación infinitaria que no admite representación mediante un token de relación actual y sus incidencias;
- un modo de unidad ontológica no cubierto por causalidad, proceso, constitución, dependencia o estructura espaciotemporal.

Una relación infinitaria de aridad set-sized no fuerza por sí sola clausura transfinita si su instancia puede tratarse como token actual de relación conectado por incidencias a cada relatum. Si la aridad o vecindad resultante fuera proper-class, reaparece REV-23.

No se permite definir $\operatorname{CoReal}$ como $\operatorname{Reg}^{\Lambda}$ para declarar RC demostrado: eso convertiría la prueba en una estipulación.

##### Reducción a una tesis de descomposición integrativa finita

Introducimos, para un contexto fijo $i$, una relación de instancia tipada:

$$
\operatorname{IntInst}_i(g_i;x_i,y_i),
$$

donde $g_i$ es un testigo relacional actual que integra $x_i$ e $y_i$ mediante causalidad, proceso, constitución, dependencia u otra relación ontológica admitida **sin usar** $\Lambda_i$, $\sim_i$, $S_i$, $R_i$ ni SameRegime.

La relación binaria utilizada por FID queda definida solo sobre testigos admisibles del mismo contexto:

$$
\operatorname{AdmIntRel}_i(x_i,y_i)
:\Longleftrightarrow
\exists g_i[
\mathrm{WA}_i(g_i)
\land
\operatorname{IntInst}_i(g_i;x_i,y_i)
].
$$

Se separan entonces dos obligaciones:

$$
\mathrm{LA}_i:
\quad
\operatorname{AdmIntRel}_i(x_i,y_i)
\Rightarrow
x_i\bowtie_i y_i,
$$

**Link Adequacy**: toda relación integradora independientemente admitida dentro de $i$ es reconocida por $\Lambda_i$;

y:

$$
\mathrm{FID}_i:
\quad
\operatorname{Generated}^{*}_i(\mathcal O_i,x_i)
\Rightarrow
\exists n<\omega\;
\exists z_{0,i},\dots,z_{n,i}
[
z_{0,i}=q_i
\land
z_{n,i}=x_i
\land
\forall k<n\;\operatorname{AdmIntRel}_i(z_{k,i},z_{k+1,i})
].
$$

**Finite Integrative Decomposition**: todo contenido generado del contexto $i$ puede resolverse, respecto del seed tipado $q_i$, en una cadena finita de relaciones integradoras independientemente caracterizadas.

Entonces:

$$
\boxed{
\mathrm{FID}_i
+
\mathrm{LA}_i
\Rightarrow
\mathrm{RC}^{\mathrm{gen}}_{\Lambda,i}.
}
$$

**Demostración.** FID$_i$ proporciona una cadena finita de $\operatorname{AdmIntRel}_i$. LA$_i$ convierte cada paso WA-admisible en $\bowtie_i$. Por definición de $\sim_i=(\bowtie_i)^*$, $x_i\in[q_i]_{\sim_i}=T^{\Lambda}_{i,q}$. $\square$

LA$_i$ es principalmente una obligación de taxonomía de $\Lambda_i$. La carga metafísica profunda queda concentrada en FID$_i$.

##### Contraesquema de límite

Considérese, dentro de un contexto fijo $i$, una familia actual:

$$
q_{0,i},q_{1,i},q_{2,i},\dots
$$

con:

$$
\operatorname{AdmIntRel}_i(q_{n,i},q_{n+1,i})
$$

para todo $n$, y un token actual $\ell_i$ cuya dependencia ontológica sea esencialmente de la **totalidad/límite** de la secuencia, sin que exista ningún $n$ ni ningún testigo relacional actual $g_i$ para el que una cadena finita de $\operatorname{AdmIntRel}_i$ conecte $q_{n,i}$ con $\ell_i$.

Si una teoría ontológica independiente justifica:

$$
\operatorname{Generated}^{*}_i(\mathcal O_i,\ell_i),
$$

pero no existe tal cadena desde $q_i:=q_{0,i}$, entonces FID$_i$ falla y la arquitectura finita no puede derivar $\mathrm{RC}^{\mathrm{gen}}_{\Lambda,i}$ para ese caso.

El contraesquema desaparece si la dependencia global tiene una instancia relacional actual $g$ de aridad set-sized y la ontología admite incidencias:

$$
q_{0,i}\bowtie_i g_i
\quad\text{y}\quad
g_i\bowtie_i \ell_i.
$$

Por tanto, «infinitario» no equivale automáticamente a «no finitamente conectable». Lo decisivo es si la integración global dispone de un **testigo ontológico actual** que pueda entrar en la red sin reificar por fiat la totalidad $R_i$.

Este análisis reduce el siguiente frente a dos preguntas:

1. ¿es FID defendible para toda co-realidad relevante?;
2. si no lo es, ¿puede ampliarse la ontología de tokens relacionales para capturar los aparentes contraejemplos sin trivializar $\Lambda_*$ ni violar PON?

El siguiente trabajo sustantivo es dar contenido independiente suficiente a $\operatorname{CoReal}$/$\operatorname{AdmIntRel}$ y someter FID a contraejemplos.

##### Contraejemplo abstracto a FID como principio lógico

Sea $X$ un espacio conectado pero no path-connected; la curva seno del topólogo es el ejemplo estándar.

Definimos, solo para este stress test:

$$
\operatorname{CoReal}_X(x,q)
:\Longleftrightarrow
x,q\text{ están en la misma componente conexa},
$$

y:

$$
\operatorname{AdmIntRel}_X(x,y)
:\Longleftrightarrow
x,y\text{ están conectados por un camino en }X.
$$

Elijamos $q$ y $x$ en componentes por caminos distintas del mismo $X$ conectado. Entonces:

$$
\operatorname{CoReal}_X(x,q)
$$

pero no existe una cadena finita de $\operatorname{AdmIntRel}_X$ entre ellos. Si existiese:

$$
q=z_0,\dots,z_n=x,
$$

la concatenación de los caminos que testifican cada paso produciría un camino de $q$ a $x$.

Por tanto:

$$
\boxed{
\operatorname{CoReal}_X(x,q)
\land
\neg\mathrm{FID}_X.
}
$$

El ejemplo no afirma que `CoReal` sea conectividad topológica. Su función es metateórica: demuestra que pasar de una noción global de unidad a una descomposición finita en enlaces es una premisa sustantiva.

##### Contraesquema de dependencia infinitaria

Considérese una cadena actual:

$$
E_1
\succ E_{1/2}
\succ E_{1/4}
\succ\cdots
$$

de dependencia ontológica inmediata WA-admisible. Supóngase además que una teoría metafísica independiente considera que toda la cadena está ultimadamente fundada en $F$, pero que no existe ningún $n<\omega$ tal que $E_1$ alcance $F$ mediante $n$ pasos de dependencia inmediata.

Si:

$$
\operatorname{CoReal}(E_1,F),
$$

entonces:

$$
\boxed{
\neg\mathrm{FID}.
}
$$

aun cuando cada eslabón individual sea ontológicamente impecable. El punto no es adoptar metafysical infinitism, sino mostrar que FID incorpora una restricción de **longitud finita** que no se sigue de la mera existencia de grounding/dependence.

##### Ruta alternativa si FID falla: clausura integrativa generalizada

Sea $\mathcal C_*$ un operador de clausura pre-régimen construido a partir de una familia $\mathfrak G_*$ de reglas integrativas independientes, potencialmente incluyendo reglas globales/de límite además de enlaces finitos.

Se exige:

$$
\mathrm{CGI}:
\quad
\mathfrak G_*
\text{ se especifica sin usar }
\operatorname{CoReal},R_i,S_i,\operatorname{Presents}_i,\operatorname{OntTotal}_i
\text{ ni la extensión final de }\mathcal C_*.
$$

Además $\mathcal C_*$ debe ser mínima respecto de esas reglas:

$$
\mathrm{CMin}:
$$

1. $A\subseteq\mathcal C_*(A)$;
2. $\mathcal C_*(A)$ es cerrada bajo $\mathfrak G_*$;
3. si $A\subseteq B$ y $B$ es cerrada bajo $\mathfrak G_*$, entonces $\mathcal C_*(A)\subseteq B$.

Esto prohíbe definir la clausura por ajuste extensional a `CoReal` y después declarar CC demostrado.

Para el seed $q$:

$$
T_q^{\mathcal C}
:=
\mathcal C_*(\{q\}).
$$

La construcción semántica pre-indexada solo exige aquí:

$$
\mathrm{CSet}:
\quad
T_q^{\mathcal C}\text{ es set-sized}.
$$

No se formula todavía CS/CC contra CoReal ni se reutiliza el mismo token a ambos lados de un cambio de contexto.

La adecuación ontológica se introduce **después** mediante un mapa de realización:

$$
\eta_i^{\mathcal C}:
T_q^{\mathcal C}
\rightsquigarrow
\{x_i\},
$$

cuya existencia no se presupone. Soundness y completeness son entonces:

$$
\mathrm{CS}^{\mathrm{gen}}_{\mathcal C,i}:
\quad
a\in T_q^{\mathcal C}
\land
\eta_i^{\mathcal C}(a)=x_i
\Rightarrow
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i),
$$

$$
\mathrm{CC}^{\mathrm{gen}}_{\mathcal C,i}:
\quad
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i)
\Rightarrow
\exists a\in T_q^{\mathcal C}\;
\eta_i^{\mathcal C}(a)=x_i.
$$

La fidelidad/injectividad estructural del mapa pertenece a RA. Aunque esta subsección conserva la derivación histórica de Ruta B, CS/CC se han elevado aquí a `RegimeGenerated*` para no reintroducir accidentalmente el caso monogeneal tras REV-07f. Solo después de esta realización es legítimo hablar de la clausura candidata como representación de una genealogía indexada.

Para reconstruir el máximo semántico se añade:

$$
\mathrm{CProcStable}:
$$

si un evento emergente actual tiene source en $T_q^{\mathcal C}$, sus tokens/eventos/targets requeridos permanecen en $T_q^{\mathcal C}$.

Entonces, en la capa **puramente closure-relative**, la construcción semántica usa exactamente las premisas del teorema que sigue:

$$
\mathrm{CSet}
+
\mathrm{CWF}
+
\mathrm{CProcStable}
+
\mathrm{SigSmall}_{\mathcal C}
+
\mathrm{ActualSep}_{\mathcal C}.
$$

No se usa $\operatorname{StructAdm}_i$, SameRegime, CS ni CC en esta maximalidad formal. Con esas premisas se construye $S_q^{\mathcal C}$ y se obtiene $\operatorname{SemTotal}_{\mathcal C}(S_q^{\mathcal C})$; el teorema detallado aparece inmediatamente debajo.

La ruta finita actual se recupera como caso especial cuando:

$$
\mathcal C_*(\{q\})=[q]_{\sim}
$$

y FID/LA justifican completeness.

Por tanto FID es una **condición suficiente de la instanciación finita**, no una condición necesaria de `ExistsR` ni una condición sobre One-$R$/Many-$R`.

##### Implementación transfinita candidata

Una realización concreta de $\mathcal C_*$ puede iterar una regla de expansión integrativa $G$ por ordinales:

$$
C_0:=\{q\},
$$

$$
C_{\alpha+1}:=G(C_\alpha),
$$

y para límite $\lambda$:

$$
C_\lambda:=\bigcup_{\beta<\lambda}C_\beta.
$$

Si existe un **ordinal set-sized** $\kappa$ tal que:

$$
C_\kappa=C_{\kappa+1}
$$

y todos los $C_\alpha$ para $\alpha\leq\kappa$ son sets, entonces:

$$
T_q^{\mathcal C}:=C_\kappa
$$

es set-sized y puede alimentar la construcción semántica directa.

Esta ruta sustituye PON+clausura finita por una obligación diferente:

$$
\mathrm{TransClSmall}_{\mathcal C}:
\quad
\exists\kappa\in\mathrm{Ord}\text{ set-sized }
[C_\kappa=C_{\kappa+1}\land C_\kappa\text{ set-sized}].
$$

No se presupone que tal $\kappa$ exista. Si la clausura requiere recorrido proper-class o no estabiliza en ningún ordinal set-sized, reaparece un blocker fundacional análogo a REV-23.

Esta formulación muestra exactamente qué perderíamos al abandonar FID: no la posibilidad de construir $S_i$, sino la prueba sencilla de smallness mediante niveles finitos $n<\omega$.

##### Teorema semántico parametrizado por una clausura candidata

Mientras CS/CC no estén justificadas, $\mathcal C_*(\{q\})$ no se denomina todavía «régimen $i$». Sea:

$$
T_q^{\mathcal C}:=\mathcal C_*(\{q\}).
$$

Fijamos una firma candidata $\mathcal L_{\mathcal C}$ y definimos una admisibilidad **puramente closure-relative**:

$$
\operatorname{CFragAdm}_{\mathcal C}(X)
$$

para $X=(T_X,\Phi_X)$ cuando:

1. $T_X\subseteq T_q^{\mathcal C}$;
2. $\Phi_X\subseteq\operatorname{Atoms}_{\mathcal L_{\mathcal C}}(T_X)$;
3. todo $\varphi\in\Phi_X$ satisface el mismo predicado $\operatorname{Actual}_{\mathcal C}(\varphi)$ usado para construir $\Phi_q^{\mathrm{all},\mathcal C}$;
4. todo hecho contiene sus relata en $T_X$;
5. todo evento representado tiene source/target únicos y la dependencia representada es coherente;
6. el contenido es positivo/monótono bajo inclusión.

Crucialmente, $\operatorname{CFragAdm}_{\mathcal C}$ **no exige** que todos los tokens sean ya ontológicamente actuales ni que pertenezcan a un régimen previamente identificado. Sí exige actualidad **semántica de los hechos representados** relativa al mismo predicado $\operatorname{Actual}_{\mathcal C}$ que usa el máximo; de otro modo no se seguiría $\Phi_X\subseteq\Phi_q^{\mathrm{all},\mathcal C}$. CS/CC/CRType siguen siendo obligaciones ontológicas posteriores sobre el carrier.

Definimos:

$$
\mathfrak D_{\mathcal C}^{\mathrm{proc}}
:=
\{X\mid \operatorname{CFragAdm}_{\mathcal C}(X)\}.
$$

Y el orden puramente semántico:

$$
X\preceq_{\mathcal C}Y
\iff
T_X\subseteq T_Y
\land
\Phi_X\subseteq\Phi_Y.
$$

Sea:

$$
\mathrm{SigSmall}_{\mathcal C}:
\quad
\mathcal L_{\mathcal C}\text{ es set-sized}
\land
\forall\sigma\in\mathcal L_{\mathcal C},
\operatorname{ar}(\sigma)\text{ es set-sized}.
$$

Bajo CSet + $\mathrm{SigSmall}_{\mathcal C}$, los átomos candidatos sobre $T_q^{\mathcal C}$ forman un set. Sea $\mathrm{ActualSep}_{\mathcal C}$ la disponibilidad metateórica del predicado de actualidad sobre ese set. Definimos:

$$
\Phi_q^{\mathrm{all},\mathcal C}
:=
\{
\varphi\in\operatorname{Atoms}_{\mathcal L_{\mathcal C}}(T_q^{\mathcal C})
\mid
\operatorname{Actual}_{\mathcal C}(\varphi)
\}.
$$

Análogamente:

$$
\Phi_q^{\mathrm{all},\mathcal C}
=
\operatorname{Diag}^{+}_{\mathcal L_{\mathcal C}}(T_q^{\mathcal C}).
$$

y:

$$
S_q^{\mathcal C}
:=
(T_q^{\mathcal C},\Phi_q^{\mathrm{all},\mathcal C}).
$$

Para que $S_q^{\mathcal C}$ sea closure-relative well-formed exigimos:

$$
\mathrm{CWF}:
\quad
\operatorname{CFragAdm}_{\mathcal C}(S_q^{\mathcal C}).
$$

Entonces, para todo $X\in\mathfrak D_{\mathcal C}^{\mathrm{proc}}$:

$$
X\preceq_{\mathcal C}S_q^{\mathcal C}.
$$

Definimos $\operatorname{CEClosed}_{\mathcal C}(S)$ como la versión closure-relative de EClosed: todo evento actual representable cuyo source está en el carrier de $S$ tiene dentro de $S$ los tokens/hechos source-event-target requeridos.

Sea CProcStable la condición de que, si un evento actual relevante tiene source en $T_q^{\mathcal C}$, sus tokens source/event/target requeridos permanecen en $T_q^{\mathcal C}$. Bajo CProcStable y la construcción de $\Phi_q^{\mathrm{all},\mathcal C}$:

$$
\operatorname{CEClosed}_{\mathcal C}(S_q^{\mathcal C}).
$$

Por tanto, definiendo:

$$
\operatorname{SemTotal}_{\mathcal C}(S)
:=
\operatorname{CEClosed}_{\mathcal C}(S)
\land
\forall X\in\mathfrak D_{\mathcal C}^{\mathrm{proc}},
\;X\preceq_{\mathcal C}S,
$$

obtenemos:

$$
\boxed{
\mathrm{CSet}
+
\mathrm{CProcStable}
+
\mathrm{CWF}
+
\mathrm{SigSmall}_{\mathcal C}
+
\mathrm{ActualSep}_{\mathcal C}
\Rightarrow
\operatorname{SemTotal}_{\mathcal C}(S_q^{\mathcal C}).
}
$$

Este teorema es deliberadamente **pre-ontológico**: no contiene StructAdm_i, SameRegime, CS, CC ni CoReal.

Solo después de CGI/CMin y de una realización $\eta_i^{\mathcal C}$ que satisfaga:

$$
\mathrm{CS}^{\mathrm{gen}}_{\mathcal C,i}
\land
\mathrm{CC}^{\mathrm{gen}}_{\mathcal C,i},
$$

puede compararse el carrier candidato con $\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,-)$ para alguna GeneBasis ya justificada. Si además RA establece fidelidad de identidad/estructura, la presentación semántica puede reetiquetarse dentro del contexto $i$.

La Ruta A finita y la Ruta B generalizada comparten el patrón lógico, pero no identifican sus carriers por notación:

1. **construcción semántica relativa a un carrier candidato:** smallness + well-formedness + estabilidad;
2. **realización tipada del carrier:** identidad/denotación hacia un contexto $i$;
3. **adecuación ontológica:** soundness/completeness frente a $\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,-)$;
4. **adecuación estructural:** RA.

En consecuencia PON permanece como blocker de la instanciación finita, no como condición necesaria de toda ruta a una exhaustividad semántica relativa.
##### FID no es generación local finita

FID restringe la **longitud del camino de integración**, no el número de relata de cada relación. Si una relación global actual $g$ tiene set-many relata y la ontología admite su instancia como token relacional, puede mediar una conexión finita por incidencia.

Por tanto:

$$
\text{no-localidad}
\not\Rightarrow
\neg\mathrm{FID}
$$

y:

$$
\text{aridad infinita set-sized}
\not\Rightarrow
\neg\mathrm{FID}.
$$

Para evitar que esto trivialice FID, se introduce un filtro independiente de **Witness Admissibility**:

$$
\mathrm{WA}(g).
$$

WA exige que $g$ sea una instancia actual y ontológica, con relata identificados sin totalización, rol integrador independiente, invariancia representacional e incidencia compatible con las obligaciones de smallness. No se admite un testigo cuyo único fundamento sea «hay que conectar estos relata para salvar FID».

##### Stress test AQFT / superselección

En AQFT, el álgebra cuasilocal puede ser la completación $C^*$ de la unión dirigida de las álgebras locales. Por ello la unión local puede ser densa sin coincidir con el álgebra cuasilocal. Éste es un modelo matemático preciso de contenido que existe en una completación y no en ningún estadio local individual.

Además, en teorías con sectores de superselección pueden fallar propiedades de aditividad: ciertos operadores no son generados por las álgebras de regiones menores y algunos aparecen solo tras una operación de completación/doble conmutante.

Esto muestra que la siguiente tesis sería demasiado fuerte:

$$
\text{todo contenido co-real está generado en algún estadio local finito}.
$$

Pero FID no necesita esa tesis. El caso se convierte en contraejemplo a FID solo si concurren tres condiciones:

$$
\operatorname{Actual}(x)
\land
\operatorname{CoReal}(x,q)
\land
\neg\exists\text{ cadena finita de testigos }g\text{ con }\mathrm{WA}(g).
$$

Por tanto AQFT no refuta FID por sí sola; proporciona una clase concreta donde la existencia ontológica de **testigos de límite** debe justificarse y no puede darse por supuesta.

##### Gauge y topological order

Las obstrucciones de factorización en gauge theory y los observables extendidos/topológicos son adversarios importantes de una ontología localista, pero tampoco producen automáticamente $\neg\mathrm{FID}$. Edge modes, constraints de borde, Wilson loops u otros observables extendidos pueden actuar como testigos finitos de incidencia si son ontológicamente admisibles bajo WA.

Así, el contraejemplo decisivo debe ser más fuerte que «la estructura es no local»: debe mostrar **co-realidad sin ningún testigo ontológico admisible de profundidad finita**.

#### 8.3. SUPERSEDED pre-genealogical RA sketch

$\mathrm{RA}_i(S)$ exige fidelidad de la presentación: identidad, denotación y las relaciones relevantes usadas para individuar el régimen deben preservarse/reflejarse bajo representaciones fieles.

RA no se identifica con «todos los hechos verdaderos están escritos en $S$». La completitud factual fuerte puede depender de la firma y de REV-25; para la cuestión de existencia de un alcance $R_i$, puede ser suficiente una noción más débil de adecuación estructural. Determinar exactamente cuánta adecuación se necesita es parte abierta de REV-24c.

#### 8.3.1. MOVED — Scope Realization now belongs to REV-07

Aun suponiendo que OA/MC/RA hayan fijado correctamente el contenido ontológico presentado por $S_i$, falta justificar que ese perfil corresponda a un objeto del tipo **alcance ontológico**.

Se introduce:

$$
\operatorname{Within}_i(x,R)
$$

sin interpretar $R$ como set. La condición de realización relativa a $q$ es:

$$
\mathrm{SR}_i(q)
:=
\exists R_i\;
\forall x\,
[
\operatorname{Within}_i(x,R_i)
\Longleftrightarrow
(\operatorname{Actual}(x)\land\operatorname{CoReal}(x,q))
].
$$

SR no se deriva de Separation ni de la existencia del carrier semántico. Si la metateoría acepta libremente una comprensión de scopes para todo predicado, ese principio debe declararse como compromiso fundacional. Si no, SR requiere una justificación ontológica independiente.

El propósito de REV-24d es bloquear el atajo:

$$
R_i := \{x\mid\operatorname{CoReal}(x,q)\}
$$

porque esa notación reintroduciría exactamente la reificación/setificación que la propuesta intenta evitar.

**SUPERSEDED:** esta formulación pertenecía al target pre-indexado. En la arquitectura vigente, scope realization forma parte de REV-07/RegimeTotal; GeneTotal es solo el caso singleton. REV-24 no produce existencia y REV-26 no es requisito de `ExistsR`.

##### Ruta plural

Sea:

$$
\varphi_q(x)
:=
\operatorname{Actual}(x)
\land
\operatorname{CoReal}(x,q).
$$

Adoptando el esquema de comprensión plural:

$$
\exists x\,\varphi_q(x)
\Rightarrow
\exists rr_i\;
\forall x[
x\prec rr_i
\Longleftrightarrow
\varphi_q(x)
],
$$

y suponiendo:

$$
\operatorname{Actual}(q)
\land
\operatorname{CoReal}(q,q),
$$

obtenemos:

$$
\boxed{
\exists rr_i\;
\forall x[
x\prec rr_i
\Longleftrightarrow
(\operatorname{Actual}(x)\land\operatorname{CoReal}(x,q))
].
}
$$

$rr_i$ es una variable plural: la fórmula no postula una entidad singular cuyos miembros sean esos objetos. Por tanto proporciona una realización de scope compatible con la cláusula anti-setificación, al precio explícito de plural comprehension.

Si se adopta esta fundamentación, $R_i$ puede permanecer como notación doctrinal legible mientras la capa formal estricta usa $rr_i$. En particular, `\exists R_i` debe leerse como abreviatura de cuantificación sobre scopes/plurales y no como existencia de un objeto colector first-order.

Esta ruta no se extiende automáticamente a $R_{\mathrm{abs}}$: la comprensión plural irrestricta sobre un dominio absolutamente general es filosóficamente controvertida y algunas lógicas plurales críticas la restringen.

Esta ruta **no cambia el estado de REV-24d**: el target de scope realization fue MOVED a REV-07/RegimeTotal. La derivación plural anterior queda como antecedente histórico/condicional para la obligación de realización de scope de REV-07, y además conserva el perfil superseded `Actual/CoReal(-,q)`; por tanto no descarga por sí sola el target vigente basado en la extensión `RegimeGenerated*`. REV-24 permanece restringido a presentación de una realidad ya justificada.

> **Status contract:** `REV-24d = UNCHANGED`; `scope realization owner = REV-07/RegimeTotal`; `Actual/CoReal plural route = NON-DISCHARGING for RegimeGenerated*`.

#### 8.4. Esquema vigente de presentación

El esquema pre-genealógico que hacía que REV-24 produjese un $R_i$ queda **SUPERSEDED**.

Fijado un parámetro de contexto $i$ y una realidad ya justificada:

$$
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i),
$$

REV-24 tiene únicamente el target:

$$
\boxed{
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
+
\operatorname{SemTotal}_i(S_i)
+
\mathrm{OA}_i(S_i;\mathfrak G_i)
+
\mathrm{MC}_i(S_i;\mathfrak G_i)
+
\mathrm{RA}_i(S_i,R_i)
\Rightarrow
\operatorname{Presents}_i(S_i,R_i).
}
$$

$\mathrm{OTB}_i$ abrevia una justificación suficiente de OA/MC/RA dentro de ese contexto. Nunca cuantifica sobre índices ni produce existencia ontológica.

#### 8.5. `ExistsR` como metasentencia

El símbolo $i$ es metavariable de contexto, no término del lenguaje objeto.

Se introduce la abreviatura:

$$
\exists^{\mathsf M} i\;\Phi_i
$$

para «hay una instanciación admisible del contexto $i$ que satisface $\Phi_i$». No se postula un dominio $I$ de índices.

Entonces:

$$
\boxed{
\operatorname{ExistsR}
:\Longleftrightarrow
\exists^{\mathsf M} i\;
\bigl(
\exists\mathfrak G_i\exists R_i\;
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
\bigr).
}
$$

y una presentación semántica produce únicamente:

$$
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
+
\operatorname{SemTotal}_i(S_i)
+
\mathrm{OTB}_i
\Rightarrow
\operatorname{Presents}_i(S_i,R_i).
$$

#### 8.6. Metaontología de contextos

Los parámetros $i,j$ no son elementos de una colección ontológica. La incompatibilidad se expresa mediante el juicio metateórico:

$$
i\mathrel{\#}j.
$$

Para $i\#j$, aplicar un predicado de $j$ a un término de tipo $i$ es mal tipado. No se expresa como una falsedad:

$$
\operatorname{Real}_j(x_i)
$$

no es una fórmula válida.

##### One-$R$

One-$R$ significa que toda pareja de realizaciones admisibles de RegimeTotal que el metalenguaje compare resulta equivalente bajo:

$$
i\simeq_{\mathrm{idx}}j.
$$

##### Many-$R$

Many-$R$ significa que el metalenguaje dispone de dos realizaciones admisibles con:

$$
i\mathrel{\#}j.
$$

Eso no crea un hecho real que relacione ambos contextos.

##### Cluster-$R$

Cluster-$R$ solo se usa antes de fijar el tipado definitivo. CommonGround implica SharedOntSpace pero no lo agota. Una integración estable debe clasificarse como SharedOntSpace preexistente o ContextGenesis constitutiva; Context Assembly/$\Xi$ es maquinaria formal subordinada a esa bifurcación.

##### Verdad entre contextos

Para $p_i\in\mathcal L_i$, una comparación con $j$ exige una traducción metalingüística:

$$
\tau_{ij}:\mathcal L_i\rightsquigarrow\mathcal L_j.
$$

Puede darse:

$$
\operatorname{True}_i(p_i)
\qquad\text{y}\qquad
\operatorname{False}_j(\tau_{ij}(p_i)),
$$

sin contradicción transversal, porque no existe un mismo $p$ bien tipado en ambos contextos.

##### Consecuencia epistemológica

Si $i\#j$, ninguna evidencia real de $i$ puede tener contenido de tipo $j$. Por tanto Many-$R$ no puede certificarse internamente mediante un hecho transversal.


### 9. Zorn deja de ser necesario para SemTotal

La construcción produce $S_i^*$ explícitamente. Por ello K1/K2/K3 y Zorn siguen siendo resultados estructurales útiles, pero no son necesarios para demostrar $\operatorname{SemTotal}$ bajo PON + REV-25.

Además, bajo esas premisas, la colección de fragmentos StructAdm es un subconjunto de:

$$
\mathcal P(T_i)
\times
\mathcal P(\operatorname{Atoms}_{\mathcal L_i}(T_i)),
$$

por lo que es set-sized.

### 10. Precio exacto

Las dos construcciones semánticas tienen premisas distintas y no deben mezclarse:

- **Ruta finita ya indexada por régimen:** $\Lambda_*$ + PON + $\operatorname{StructAdm}_i$ + $\mathrm{SigSmall}_i$ + $\mathrm{ActualSep}_i$.
- **Ruta generalizada pre-ontológica:** CGI/CMin para la generación no circular de $\mathcal C_*$ y, para el teorema semántico, CSet + CWF + CProcStable + $\mathrm{SigSmall}_{\mathcal C}$ + $\mathrm{ActualSep}_{\mathcal C}$. La realización posterior usa $\eta_i^{\mathcal C}$ + CS$^{gen}_{\mathcal C,i}$/CC$^{gen}_{\mathcal C,i}$ + RA; $\operatorname{StructAdm}_i$ no es premisa de esta maximalidad.

La existencia ontológica **local** pertenece a REV-07: GeneUnit locales independientemente justificadas + GeneBasis + RegimeClosure + scope realization deben justificar $\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)$. GeneTotal queda como corolario singleton. REV-24a/b/c se añaden después para justificar que $S_i$ presenta ese $R_i$.

REV-26 queda como extensión metateórica no bloqueante: One-$R$/Many-$R$ y expresividad del metalenguaje. Los índices son parámetros de contexto, no entidades cuantificadas por el lenguaje objeto.

### 11. Emergencia y existencia

La emergencia no produce la existencia del máximo semántico. Las condiciones de identidad y smallness permiten construir $S_i^*$; la teoría de emergencia determina la propiedad adicional:

$$
\operatorname{EClosed}_i(S_i^*).
$$

Tampoco la emergencia resuelve la existencia genealógica de REV-07 ni la presentación de REV-24. Por ello no debe afirmarse que «la emergencia demuestra que existe $R$»; como máximo participa en la propiedad EClosed de una presentación tipada.

---
