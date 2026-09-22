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

### Estado de REV-18

REV-18 permanece **PARTIAL**.

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

### 3.5.8. Estado de REV-19

REV-19 pasa de **OPEN** a **PARTIAL**.

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

### 3.7.6. Estado de REV-09

REV-09 pasa de **OPEN** a **PARTIAL**.

Se ha demostrado que EClosed se preserva formalmente bajo uniones de cadenas compatibles.

Falta demostrar la parte ontológica:

$$
\text{la cota formal es un dominio procesual admisible/actual}.
$$

Esa es ahora la forma precisa de K2.

---

---

## REV-07 — criterio independiente de identidad de régimen

El objetivo es definir cuándo dos contenidos pertenecen a la misma realidad ontológica sin usar K3, amalgamabilidad, máximos, `SameIndex`, `EClosed` ni la existencia de un dominio común.

### 1. Tokens ontológicos actuales

Sea $\Omega$ una clase/set de trabajo de **tokens ontológicos actuales** relevantes para la teoría procesual: estados, eventos, entidades, estructuras o relaciones efectivamente instanciadas.

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
\{q\in\Omega\mid q\trianglelefteq X\}.
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
\Omega=\{a,b\},
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

## REV-07 — derivación local de K3_i

Una vez que la identidad de régimen se define mediante caminos finitos de enlaces $\bowtie$, K3_i puede reducirse a dos principios de extensión estrictamente locales.

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

**Lema REV-07.1.** Supóngase:

1. los dominios considerados son no vacíos;
2. los regímenes se definen por las clases de equivalencia de $\sim=(\bowtie)^*$;
3. EEA;
4. OAM.

Entonces cada:

$$
(\mathfrak D_i^{\mathrm{proc}},\preceq_i)
$$

es dirigido:

$$
\boxed{K3_i.}
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

Por tanto K3_i para dominios no vacíos. $\square$

**Caso del dominio vacío.** Si $\mathfrak D_i^{\mathrm{proc}}$ contiene un dominio vacío $0_i$, para recuperar K3_i sobre todo el poset basta exigir:

$$
0_i\preceq_i X
$$

para todo $X\in\mathfrak D_i^{\mathrm{proc}}$.

Entonces cualquier par donde intervenga $0_i$ tiene como cota al otro dominio. Si no se desea asumir un bottom vacío, el lema debe leerse sobre el subposet no vacío.

### 4. Qué gana esta derivación

K3_i ya no necesita ser una premisa global primitiva.

Se reduce a dos compromisos locales:

$$
\boxed{
\mathrm{EEA}+\mathrm{OAM}
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

Este teorema es exclusivamente semántico. No permite sustituir $S_i$ por un $R_i$ ni concluir $\operatorname{ExistsRegR}$ sin REV-24/$\mathrm{OTB}_i$; tampoco contiene ningún paso hacia $\operatorname{ExistsAbsR}$:

$$
\operatorname{SemTotal}_i(S_i)
+
\mathrm{OTB}_i
\Rightarrow
\exists R_i[
\operatorname{Presents}_i(S_i,R_i)
\land
\operatorname{OntTotal}_i(R_i)
]
\Rightarrow
\operatorname{WitnessedRegR}
\Rightarrow
\operatorname{ExistsRegR}.
$$

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

Si PSB falla, No-R puede defenderse mediante una forma extremadamente fuerte de extensibilidad local:

> desde un único estado set-sized parten proper-class many actualizaciones emergentes actualmente instanciadas.

Esa posibilidad es lógicamente distinta del potencialismo ordinario de «siempre hay una extensión más»; es una ramificación propia-clase ya en un solo paso.

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

## Teorema directo de exhaustividad semántica por conectividad localmente set-like

La definición actual de régimen permite construir directamente un máximo semánticamente exhaustivo. El paso adicional desde ese máximo a una **totalidad ontológica** se mantiene separado.

### 1. PON — Pointwise Ontological Neighborhood Smallness

Sea:

$$
N(q):=\{r\mid q\bowtie r\}.
$$

Definimos:

$$
\mathrm{PON}:\quad \forall q,\;N(q)\text{ es set-sized}.
$$

PON afirma que ningún token actual está inmediatamente enlazado, mediante las relaciones admitidas de $\Lambda_*$, con proper-class many tokens.

PSB es un caso particular: los eventos emergentes salientes de un estado están enlazados con él mediante incidencia procesual, por lo que:

$$
\mathrm{PON}\Rightarrow\mathrm{PSB}_i.
$$

### 2. Un régimen generado por un token es set-sized

Fijemos un token actual $q_0$ y definamos:

$$
S_0=\{q_0\},
$$

$$
S_{n+1}=S_n\cup\bigcup_{q\in S_n}N(q).
$$

Por PON, Replacement y Union, cada $S_n$ es set-sized. Entonces:

$$
S_\omega=\bigcup_{n<\omega}S_n
$$

también es set-sized.

Como $\sim$ es por definición la clausura reflexivo-transitiva **finita** de $\bowtie$:

$$
\boxed{S_\omega=[q_0]_{\sim}.}
$$

Por tanto:

$$
\boxed{\mathrm{PON}\Rightarrow |i|\text{ set-sized}}
$$

para el régimen definido por conectividad finita.

Este resultado depende de esa elección de identidad. Si existen relaciones que solo conectan mediante cadenas esencialmente transfinitarias o condiciones de límite, quedan fuera de $[q_0]_{\sim}$ por definición. La suficiencia ontológica de la clausura finita pertenece a REV-07, no al argumento de smallness.

### 3. Smallness de los hechos

Sea $T_i=[q_0]_{\sim}$.

Definimos:

$$
\mathrm{SigSmall}_i:
\quad
\mathcal L_i\text{ es set-sized}
\land
\forall \sigma\in\mathcal L_i,\;
\operatorname{ar}(\sigma)\text{ es set-sized}.
$$

La anterior exigencia de aridad finita era una condición suficiente, pero más fuerte de lo necesario. Si cada aridad es un set, entonces para cada símbolo $\sigma$ el espacio $T_i^{\operatorname{ar}(\sigma)}$ es un set y, por Replacement + Union sobre la firma set-sized, también lo es:

$$
\operatorname{Atoms}_{\mathcal L_i}(T_i).
$$

Para seleccionar de ese set los hechos actualmente verdaderos necesitamos además que la condición de actualidad esté disponible como predicado definible en la metateoría:

$$
\mathrm{ActualSep}_i.
$$

Bajo esa condición, Separation permite formar:

$$
\Phi_i^{\mathrm{all}}
=
\{\varphi\in\operatorname{Atoms}_{\mathcal L_i}(T_i)
\mid \operatorname{Actual}_i(\varphi)\}.
$$

REV-25 registra independientemente tanto $\mathrm{SigSmall}_i$ como $\mathrm{ActualSep}_i$.

### 4. Construcción directa del máximo semántico

Definimos:

$$
S_i^*:=(T_i,\Phi_i^{\mathrm{all}}).
$$

$S_i^*$ es StructAdm bajo las premisas vigentes de contenido positivo actual.

### 5. Máximo

Para cualquier $X=(T_X,\Phi_X)\in\mathfrak D_i^{\mathrm{proc}}$ se tiene:

$$
T_X\subseteq T_i
$$

y:

$$
\Phi_X\subseteq\Phi_i^{\mathrm{all}}.
$$

Luego:

$$
\boxed{
\forall X\in\mathfrak D_i^{\mathrm{proc}},
\quad X\preceq_i S_i^*.
}
$$

$S_i^*$ es máximo en el poset semántico, no solo maximal.

### 6. EClosed

Si $e$ es un evento emergente actual con source $s\in T_i$, las relaciones source/event/target son enlaces procesuales admitidos. Por tanto evento y target pertenecen a la misma clase finitamente conectada, y sus hechos pertenecen a $\Phi_i^{\mathrm{all}}$.

Luego:

$$
\boxed{\operatorname{EClosed}_i(S_i^*).}
$$

### 7. Teorema directo de SemTotal

**Teorema.**

Supóngase que existe al menos un token actual $q_0$ y que:

1. la identidad de régimen se define por la clausura finita $\sim=(\bowtie)^*$;
2. PON;
3. $\mathrm{SigSmall}_i$;
4. $\mathrm{ActualSep}_i$;
5. los dominios son fragmentos StructAdm del contenido actual del régimen.

Entonces existe $S_i^*\in\mathfrak D_i^{\mathrm{proc}}$ tal que:

$$
\operatorname{EClosed}_i(S_i^*)
$$

y:

$$
\forall X\in\mathfrak D_i^{\mathrm{proc}},
\quad X\preceq_i S_i^*.
$$

Por tanto:

$$
\boxed{\operatorname{SemTotal}_i(S_i^*).}
$$

### 8. REV-24: el puente ontológico no está incluido en el teorema

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

#### 8.1. REV-24a — Ontological Anchoring (OA)

Como disciplina de tipos, $\operatorname{CoReal}$ se aplica solo a tokens actuales:

$$
\mathrm{CRType}:
\quad
\operatorname{CoReal}(x,q)
\Rightarrow
\operatorname{Actual}(x)
\land
\operatorname{Actual}(q).
$$

Esta cláusula no decide qué hace co-reales a dos tokens; solo fija el tipo ontológico de los relata.

OA se formula sobre la misma relación ontológica independiente que MC:

$$
\mathrm{OA}_i(S;q)
:=
\forall a\in T_S\;
\exists x\,
[
\operatorname{Actual}(x)
\land
\operatorname{CoReal}(x,q)
\land
\operatorname{Den}_i(a,x)
].
$$

Para el carrier directo $T_i=[q]_{\sim}$ y la denotación canónica:

$$
\mathrm{CD}_i:
\quad
x\in T_i
\Rightarrow
\operatorname{Den}_i(x,x).
$$

Entonces:

$$
\boxed{
\mathrm{RS}_{\Lambda}
+
\mathrm{CD}_i
\Rightarrow
\mathrm{OA}_i(S_i^*;q).
}
$$

**Demostración.** Sea $a\in T_i=[q]_{\sim}$. Por RS, $\operatorname{CoReal}(a,q)$; por CRType, $\operatorname{Actual}(a)$. CD da $\operatorname{Den}_i(a,a)$. Tomando $x=a$ se obtiene OA. $\square$

Así RS controla **sobreinclusión** y OA del carrier; RC controla **subinclusión** y MC. Bajo RS + RC + CD, el carrier de $S_i^*$ coincide extensionalmente, vía denotación canónica, con la co-realidad relativa a $q$.

El anclaje/fidelidad de hechos $\Phi_i^{\mathrm{all}}$ sigue abierto y pertenece a RA/REV-25.

#### 8.2. REV-24b — Membership Completeness (MC)

MC se formula directamente respecto de la relación ontológica objetivo $\operatorname{CoReal}$ y de un token semilla actual $q$:

$$
\mathrm{MC}_i(S;q)
:=
\forall x\,
[
\operatorname{Actual}(x)
\land
\operatorname{CoReal}(x,q)
\Rightarrow
\exists a\in T_S\;\operatorname{Den}_i(a,x)
].
$$

Así se evita introducir un predicado $\operatorname{Reg}_i(x)$ cuya relación con $\operatorname{CoReal}$ tendría que justificarse por separado.

Si se desea una abreviatura extensional del régimen relativo a $q$, se define solo después:

$$
\operatorname{Reg}^{\mathrm{ont}}_q(x)
:\Longleftrightarrow
\operatorname{Actual}(x)
\land
\operatorname{CoReal}(x,q).
$$

El criterio formal generado por $\Lambda_*$ sigue siendo:

$$
\operatorname{Reg}^{\Lambda}(x;q)
:\Longleftrightarrow
x\in[q]_{\sim}.
$$

Las dos obligaciones de adecuación son:

$$
\mathrm{RS}_{\Lambda}:
\quad
\operatorname{Reg}^{\Lambda}(x;q)
\Rightarrow
\operatorname{CoReal}(x,q),
$$

y:

$$
\mathrm{RC}_{\Lambda}:
\quad
\operatorname{CoReal}(x,q)
\Rightarrow
\operatorname{Reg}^{\Lambda}(x;q).
$$

RS es soundness; RC es completeness.

Para el carrier directo:

$$
T_i=[q]_{\sim}.
$$

Como sus elementos son los propios tokens actuales usados en la construcción, se dispone de la denotación canónica:

$$
\mathrm{CD}_i:
\quad
x\in T_i
\Rightarrow
\operatorname{Den}_i(x,x).
$$

Entonces:

$$
\boxed{
\mathrm{RC}_{\Lambda}
+
\mathrm{CD}_i
\Rightarrow
\mathrm{MC}_i(S_i^*;q).
}
$$

**Demostración.** Sea $x$ actual con $\operatorname{CoReal}(x,q)$. Por RC:

$$
x\in[q]_{\sim}=T_i.
$$

Por CD:

$$
\operatorname{Den}_i(x,x).
$$

Tomando $a=x\in T_i$ se obtiene el testigo exigido por MC. $\square$

Obsérvese que RS no interviene en este lema. RS cumple la función complementaria de impedir **sobreinclusión** del carrier; RC impide **subinclusión**. Bajo ambas:

$$
\operatorname{CoReal}(x,q)
\Longleftrightarrow
x\in[q]_{\sim}.
$$

##### Posibles contraejemplos a $\mathrm{RC}_{\Lambda}$

RC falla si existe $x$ que co-pertenece ontológicamente con $q$ pero cuya integración solo puede establecerse mediante:

- una condición global que no se descompone en enlaces token-specific;
- una dependencia esencialmente de límite sin cadena finita de incidencias;
- una relación infinitaria que no admite representación mediante un token de relación actual y sus incidencias;
- un modo de unidad ontológica no cubierto por causalidad, proceso, constitución, dependencia o estructura espaciotemporal.

Una relación infinitaria de aridad set-sized no fuerza por sí sola clausura transfinita si su instancia puede tratarse como token actual de relación conectado por incidencias a cada relatum. Si la aridad o vecindad resultante fuera proper-class, reaparece REV-23.

No se permite definir $\operatorname{CoReal}$ como $\operatorname{Reg}^{\Lambda}$ para declarar RC demostrado: eso convertiría la prueba en una estipulación.

##### Reducción a una tesis de descomposición integrativa finita

Introducimos provisionalmente una relación de instancia:

$$
\operatorname{IntInst}(g;x,y),
$$

donde $g$ es un testigo relacional actual que integra $x$ e $y$ mediante causalidad, proceso, constitución, dependencia u otra relación ontológica admitida **sin usar** $\Lambda_*$, $\sim$, $S_i$, $R_i$ ni SameRegime.

La relación binaria utilizada por FID queda definida solo sobre testigos admisibles:

$$
\operatorname{AdmIntRel}(x,y)
:\Longleftrightarrow
\exists g[
\mathrm{WA}(g)
\land
\operatorname{IntInst}(g;x,y)
].
$$

Se separan entonces dos obligaciones:

$$
\mathrm{LA}:
\quad
\operatorname{AdmIntRel}(x,y)
\Rightarrow
x\bowtie y,
$$

**Link Adequacy**: toda relación integradora independientemente admitida es reconocida por $\Lambda_*$;

y:

$$
\mathrm{FID}:
\quad
\operatorname{CoReal}(x,q)
\Rightarrow
\exists n<\omega\;
\exists z_0,\dots,z_n
[
z_0=q
\land
z_n=x
\land
\forall k<n\;\operatorname{AdmIntRel}(z_k,z_{k+1})
].
$$

**Finite Integrative Decomposition**: toda co-pertenencia ontológica puede resolverse en una cadena finita de relaciones integradoras independientemente caracterizadas.

Entonces:

$$
\boxed{
\mathrm{FID}
+
\mathrm{LA}
\Rightarrow
\mathrm{RC}_{\Lambda}.
}
$$

**Demostración.** FID proporciona una cadena finita de $\operatorname{AdmIntRel}$. LA convierte cada paso WA-admisible en $\bowtie$. Por definición de $\sim=(\bowtie)^*$, $x\in[q]_{\sim}$. $\square$

LA es principalmente una obligación de taxonomía de $\Lambda_*$. La carga metafísica profunda queda concentrada en FID.

##### Contraesquema de límite

Considérese una familia actual:

$$
q_0,q_1,q_2,\dots
$$

con:

$$
\operatorname{AdmIntRel}(q_n,q_{n+1})
$$

para todo $n$, y un token actual $\ell$ cuya dependencia ontológica sea esencialmente de la **totalidad/límite** de la secuencia, sin que exista ningún $n$ ni ningún testigo relacional actual $g$ para el que una cadena finita de $\operatorname{AdmIntRel}$ conecte $q_n$ con $\ell$.

Si una teoría ontológica independiente justifica:

$$
\operatorname{CoReal}(\ell,q_0),
$$

entonces FID falla y, por tanto, la arquitectura actual no puede derivar RC para ese caso.

El contraesquema desaparece si la dependencia global tiene una instancia relacional actual $g$ de aridad set-sized y la ontología admite incidencias:

$$
q_0\bowtie g
\quad\text{y}\quad
g\bowtie \ell.
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

Se exigen:

$$
\mathrm{CS}:
\quad
x\in T_q^{\mathcal C}
\Rightarrow
\operatorname{CoReal}(x,q),
$$

$$
\mathrm{CC}:
\quad
\operatorname{CoReal}(x,q)
\Rightarrow
x\in T_q^{\mathcal C},
$$

y:

$$
\mathrm{CSet}:
\quad
T_q^{\mathcal C}\text{ es set-sized}.
$$

CS y CC son todavía criterios de adecuación de una **clausura candidata**. Antes de justificarlos no se asigna un índice ontológico $i$ ni se invocan OA/MC de régimen.

Si CS+CC se justifican, CRType garantiza que los elementos co-reales son actuales; tras realizar el scope local correspondiente, la construcción puede reindexarse como $T_i^{\mathcal C},S_i^{\mathcal C}$ y entonces se recuperan los lemas tipados de OA/MC.

Para reconstruir el máximo semántico se añade:

$$
\mathrm{CProcStable}:
$$

si un evento emergente actual tiene source en $T_q^{\mathcal C}$, sus tokens/eventos/targets requeridos permanecen en $T_q^{\mathcal C}$.

Entonces, bajo:

$$
\mathrm{CSet}
+\mathrm{SigSmall}_i
+\mathrm{ActualSep}_i
+\operatorname{StructAdm}
+\mathrm{CProcStable},
$$

la misma construcción:

$$
S_q^{\mathcal C}
:=
(T_q^{\mathcal C},\Phi_q^{\mathrm{all},\mathcal C})
$$

produce condicionalmente un máximo semántico E-closed de la clausura generalizada.

La ruta finita actual se recupera como caso especial cuando:

$$
\mathcal C_*(\{q\})=[q]_{\sim}
$$

y FID/LA justifican completeness.

Por tanto FID es una **condición suficiente de la instanciación finita**, no una condición necesaria de `ExistsRegR` y mucho menos de `ExistsAbsR`.

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
\mathrm{TransClSmall}_i:
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
3. todo hecho contiene sus relata en $T_X$;
4. todo evento representado tiene source/target únicos y la dependencia representada es coherente;
5. el contenido es positivo/monótono bajo inclusión.

Crucialmente, $\operatorname{CFragAdm}_{\mathcal C}$ **no exige** que todos los tokens sean actuales ni que pertenezcan ya al mismo régimen. Esas son obligaciones ontológicas de CS/CC/CRType, no premisas de la maximalidad semántica.

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

Solo después, si se justifican CGI/CMin y además:

$$
\mathrm{CS}:\quad
x\in T_q^{\mathcal C}\Rightarrow\operatorname{CoReal}(x,q),
$$

$$
\mathrm{CC}:\quad
\operatorname{CoReal}(x,q)\Rightarrow x\in T_q^{\mathcal C},
$$

CRType garantiza actualidad de los tokens cubiertos por CS, y puede establecerse el puente desde la clausura candidata a un régimen ontológico. En ese estadio —no antes— es legítimo reindexar la construcción como $T_i^{\mathcal C},S_i^{\mathcal C}$.

La ruta original se recupera cuando:

$$
\mathcal C_*(\{q\})=[q]_{\sim},
$$

PON prueba CSet y la definición de $\Lambda_*$ proporciona la información ontológica necesaria para intentar RS/RC.

Esto separa definitivamente:

1. **construcción semántica relativa a una clausura candidata:** CSet/CWF/CProcStable + smallness semántica;
2. **adecuación ontológica de esa clausura:** CGI/CMin + CS/CC/CRType, o RS/RC en la ruta finita.

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

#### 8.3. REV-24c — Representational Adequacy (RA)

$\mathrm{RA}_i(S)$ exige fidelidad de la presentación: identidad, denotación y las relaciones relevantes usadas para individuar el régimen deben preservarse/reflejarse bajo representaciones fieles.

RA no se identifica con «todos los hechos verdaderos están escritos en $S$». La completitud factual fuerte puede depender de la firma y de REV-25; para la cuestión de existencia de un alcance $R_i$, puede ser suficiente una noción más débil de adecuación estructural. Determinar exactamente cuánta adecuación se necesita es parte abierta de REV-24c.

#### 8.3.1. REV-24d — Scope Realization (SR)

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

SR tampoco basta por sí sola para `ExistsRegR`: todavía hay que justificar que el alcance realizado cumple $\operatorname{OntTotal}_i$; y ningún cierre de REV-24 local basta por sí solo para `ExistsAbsR`, que requiere REV-26.

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

Así REV-24d pasa a PARTIAL: existe una derivación condicional precisa, pero la PR aún no adopta definitivamente PFO/PFO+ ni una variante crítica como base formal.

#### 8.4. Esquema objetivo de OTB

La obligación conjunta se registra como:

$$
\boxed{
\operatorname{SemTotal}_i(S_i)
+
\mathrm{OA}_i(S_i;q)
+
\mathrm{MC}_i(S_i;q)
+
\mathrm{RA}_i(S_i)
+
\mathrm{SR}_i(q)
\Rightarrow
\exists R_i
[
\operatorname{Presents}_i(S_i,R_i)
\land
\operatorname{OntTotal}_i(R_i)
].
}
$$

Este esquema **no está demostrado**. $\mathrm{OTB}_i$ abrevia una justificación independiente suficiente para obtenerlo.

La relación $\operatorname{Presents}_i(S,R)$ no puede definirse como «$R$ es total y $S$ lo describe», porque eso haría trivial el esquema. Debe caracterizarse mediante denotación, pertenencia independiente y preservación estructural.

#### 8.5. Consecuencia conceptual

Esta descomposición muestra que la pregunta «¿existe un alcance ontológico exhaustivo?» puede no requerir una descripción completa de todos los hechos de ese alcance. Si MC pudiera justificarse desde una individuación ontológica independiente del régimen, parte del trabajo de existencia podría desacoplarse de $\mathrm{ActualSep}_i$ y de una firma factualmente completa.

Eso **no** se da por probado: abre una posible ruta futura en la que REV-25 seguiría siendo necesario para el teorema fuerte de $\operatorname{SemTotal}$, pero quizá no para una tesis ontológica más austera sobre existencia de alcance.

Bajo la ruta actualmente construida, solo si OTB se justifica se obtiene:

$$
\boxed{
\mathrm{PON}
+\mathrm{SigSmall}_i
+\mathrm{ActualSep}_i
+\operatorname{StructAdm}
+\mathrm{OTB}_i
\Rightarrow
\operatorname{WitnessedRegR}
\Rightarrow
\operatorname{ExistsRegR}.
}
$$

### 8.6. REV-26 — existencia del $R$ absoluto

REV-24 es local al régimen. Incluso una demostración completa de:

$$
\operatorname{WitnessedRegR}
$$

no contiene por sí sola una totalidad de **todo** lo real.

#### 8.6.1. AG

`AG` es una condición metalingüística sobre el alcance del cuantificador de `Real(x)`: el cuantificador debe ser absolutamente general y no esconder un índice/contexto.

#### 8.6.2. APC$_{Real}$

La instancia relevante de comprensión plural es:

$$
\mathrm{APC}_{Real}:
\quad
(\exists x\,\operatorname{Real}(x))
\Rightarrow
\exists rr_{\mathrm{abs}}
\forall x[
x\prec rr_{\mathrm{abs}}
\Longleftrightarrow
\operatorname{Real}(x)
].
$$

#### 8.6.3. Lema de reducción

Definimos en semántica plural:

$$
\operatorname{AbsTotal}(rr)
:\Longleftrightarrow
\forall x[
x\prec rr
\Longleftrightarrow
\operatorname{Real}(x)
].
$$

y:

$$
\operatorname{ExistsAbsR}
:\Longleftrightarrow
\exists rr\;\operatorname{AbsTotal}(rr).
$$

Bajo realidad no vacía:

$$
\boxed{
\mathrm{AG}
+
\exists x\,\operatorname{Real}(x)
\Rightarrow
[
\mathrm{APC}_{Real}
\Longleftrightarrow
\operatorname{ExistsAbsR}
].
}
$$

**Demostración.** APC$_{Real}$ proporciona exactamente un testigo plural de `AbsTotal`. Recíprocamente, un testigo de `ExistsAbsR` satisface el consecuente de APC$_{Real}$. AG fija la lectura absolutamente general de los cuantificadores; no añade un paso deductivo interno. $\square$

Por tanto:

$$
\mathrm{AG}
+
\mathrm{APC}_{Real}
+
\operatorname{NonEmptyReality}
\Rightarrow
\operatorname{ExistsAbsR}
$$

es una consecuencia inmediata del principio de formación de scope adoptado. No constituye evidencia independiente a favor de APC$_{Real}$.

#### 8.6.4. REV-26e — no-trivialidad del target

Si el $R$ doctrinal original es literalmente:

$$
R:=\operatorname{Scope}(\operatorname{Real}),
$$

y `Scope` se interpreta pluralmente, la existencia desnuda de $R$ queda reducida a:

1. AG;
2. una instancia suficiente de plural comprehension;
3. no-vacuidad de realidad.

La maquinaria emergentista no interviene.

Si se desea un target más fuerte, debe escribirse explícitamente:

$$
\operatorname{ExistsStructuredAbsR}_Q
:=
\exists rr[
\operatorname{AbsTotal}(rr)
\land
Q(rr)
].
$$

donde $Q$ podría expresar integración, conectividad, clausura u otra estructura. Pero $Q$ **no** puede introducirse únicamente para hacer no trivial el teorema: debe venir de la doctrina y su justificación es independiente.

Así el programa tiene dos capas:

- **bare absolute scope:** problema de AG/comprensión;
- **estructura del scope:** problema ontológico adicional, potencialmente relacionado con regímenes, emergencia o globalización.

#### 8.6.5. Independencia respecto de la maquinaria emergentista

El lema de reducción no usa:

$$
\mathrm{PON},\;
\mathrm{SigSmall},\;
\operatorname{SemTotal},\;
\operatorname{EClosed},\;
\mathrm{OTB},\;
F
\text{ ni Zorn}.
$$

Hay tres puntos de ataque no equivalentes:

1. negar AG;
2. aceptar AG pero negar/restringir APC$_{Real}$;
3. negar que una pluralidad exhaustiva sea suficiente para el sentido doctrinal de scope, en cuyo caso debe especificarse un fortalecimiento $Q$.


#### 8.6.6. Ruta indexada

Si `Real` solo existe como familia `Real_i`, comprensión plural puede producir scopes $rr_i$ sin producir $rr_{abs}$. Para pasar de:

$$
\operatorname{ExistsRegR}
$$

a:

$$
\operatorname{ExistsAbsR}
$$

se requiere entonces un Globalization Bridge independiente `GB`. Una jerarquía de contextos siempre ampliable puede bloquear GB sin negar cada totalidad indexada.

Esto formaliza por qué:

$$
\boxed{
\operatorname{ExistsRegR}
\not\Rightarrow
\operatorname{ExistsAbsR}.
}
$$

#### 8.6.7. No-$R$ clásico frente a no-finalidad relativista

Si AG es admisible:

$$
\operatorname{NoR}_{\mathrm{AG}}
:=
\neg\operatorname{ExistsAbsR}
$$

es una negación ordinaria en el mismo marco semántico.

Si se adopta generality relativism, esa formulación no puede darse por neutral: la tesis rival rechaza que exista un alcance final de los cuantificadores. Se representa entonces mediante un **metaschema**:

$$
\mathrm{ER}[I]:
\quad
\exists I^+[
I\prec I^+
\land
\exists^{I^+}x\,\neg\operatorname{Covered}_I(x)
].
$$

para cada interpretación admisible $I$ que pretenda ser final.

La colección de todas las instancias ER no se reifica como una cuantificación objeto sobre todas las interpretaciones. Es una disciplina metalingüística: ante cualquier candidato $I$, debe poder darse una expansión $I^+$.

Denotamos esa posición por:

$$
\operatorname{NoAbsFinality}.
$$

Así:

$$
\boxed{
\operatorname{NoR}_{\mathrm{AG}}
\text{ y }
\operatorname{NoAbsFinality}
\text{ no son la misma fórmula ni presuponen la misma semántica}.
}
$$

Esto importa para la carga probatoria: refutar $\operatorname{NoR}_{\mathrm{AG}}$ mediante AG+APC$_{Real}$ no refuta por sí solo generality relativism, porque este último cuestiona AG/APC antes de que la negación clásica quede disponible con lectura absoluta.


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

La construcción semántica requiere una **clausura de régimen** suficientemente small y process-stable: en la ruta finita esto se implementa con $\Lambda_*$ + PON; en la ruta generalizada con $\mathcal C_*$ + CSet/CProcStable. Ambas rutas requieren además $\mathrm{SigSmall}_i$ y $\mathrm{ActualSep}_i$.

La conclusión ontológica **local** añade REV-24a/OA + REV-24b/MC + REV-24c/RA + REV-24d/SR para justificar un $R_i$ presentado por $S_i$.

La conclusión doctrinal **absoluta** añade todavía REV-26: AG + APC$_{Real}$ o un Globalization Bridge equivalente.

### 11. Emergencia y existencia

La emergencia no produce la existencia del máximo semántico. Las condiciones de identidad y smallness permiten construir $S_i^*$; la teoría de emergencia determina la propiedad adicional:

$$
\operatorname{EClosed}_i(S_i^*).
$$

Tampoco la emergencia resuelve $\mathrm{OTB}_i$ ni REV-26. Por ello no debe afirmarse que «la emergencia demuestra que existe $R$»; como máximo participa en la propiedad EClosed de una presentación local.

---
