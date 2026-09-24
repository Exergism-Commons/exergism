# Autodescripción, realidad y distinción — crónica consolidada

**Estado:** propuesta doctrinal exploratoria, no canónica.  
**PR:** #12 — *Derive regime-local semantic exhaustivity and isolate the Exists-R bridge*.  
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

Las derivaciones técnicas detalladas se mantienen fuera del estado normativo en:

- [derivaciones técnicas de emergencia, cierre y proceso](work/autodescripcion-realidad-distincion-derivaciones-2026-09-22.md)

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

## 1. Objetivo conceptual — totalidad de régimen frente a Realidad Total

La auditoría de REV-24 obliga a separar dos preguntas que la versión anterior volvió a mezclar:

1. ¿existe un alcance ontológico exhaustivo **de algún régimen**?;
2. ¿existe el $R$ de la doctrina original, es decir, la **totalidad de todo lo real**?

Estas tesis no son equivalentes.

### 1.1. Exhaustividad semántica, presentación y totalidad ontológica

Para un régimen ontológico $i$:

$$
\operatorname{SemTotal}_i(S)
:=
\operatorname{EClosed}_i(S)
\land
\forall X\in\mathfrak D_i^{\mathrm{proc}},
\;X\preceq_i S.
$$

$\operatorname{SemTotal}_i(S)$ es una propiedad de un **objeto semántico** $S$.

Reservamos:

$$
\operatorname{OntTotal}_i(R)
$$

para una propiedad de **alcances ontológicos**: $R$ agota efectivamente el alcance ontológico del régimen $i$.

Y:

$$
\operatorname{Presents}_i(S,R)
$$

relaciona ambos tipos. No significa $S=R$ y no contiene por definición $\operatorname{OntTotal}_i(R)$.

### 1.2. Horizonte empírico $U_i$ y Muro

$U_i$ designa el horizonte físico/empírico accesible desde una posición interna. No se identifica por definición con $S_i$ ni con $R_i$.

$$
\operatorname{Rep}_i(U_i)\preceq_i S_i.
$$

El Muro mínimo exige:

$$
\boxed{
\operatorname{NoAccessibleExtension}_i(U_i)
\not\Rightarrow
\operatorname{ExhaustsOntScope}_i(U_i).
}
$$

La arquitectura permanece:

$$
U_i
\xrightarrow{\operatorname{Rep}_i}
S_i
\dashrightarrow_{\mathrm{REV\text{-}24}/\mathrm{OTB}_i}
R_i.
$$

**Motivación física limitada.** Static-patch observables, gravitational dressing y reconstrucción holográfica motivan distinguir acceso, representación y alcance, pero no demuestran ninguna identificación $U_i=S_i=R_i$ ni ninguna tesis de totalidad. Véase el [mapa de literatura, §13](autodescripcion-realidad-distincion-references.md#13-horizontes-observables-gravitatorios-y-reconstrucción-holográfica).

### 1.3. El índice es un parámetro de tipo, no una entidad

La ontología primaria es **indexada**, pero el índice no forma parte de la ontología.

Los símbolos:

$$
i,j,k,\dots
$$

son **metavariables/parámetros de contexto**. No designan instancias reales, lugares, mundos-objeto ni elementos de una colección $I$.

En particular, la teoría no postula:

$$
I=\{i,j,k,\dots\},
$$

ni presupone que los índices sean enumerables, accesibles entre sí o comparables desde una realidad superior.

Cada contexto $i$ determina su propio tipado ontológico. Una variable escrita $x_i$ pertenece al sort/contexto de objetos de $i$; una fórmula:

$$
\operatorname{Real}_i(x_i)
$$

solo está bien formada en ese contexto.

**Admisión del índice.** El subíndice no produce por notación la unidad que etiqueta. Usar ontológicamente \(i\) presupone una individuación contextual metateóricamente admisible. La propuesta general no fija una world-making relation universal: una teoría independiente \(\mathcal T\) puede descargar el criterio solo mediante:

$$
\operatorname{Ind}_{\mathcal T}^{\mathsf M}(C;\chi)\land
\operatorname{IndAdequate}^{\mathsf M}(\mathcal T,C,\chi)
\Rightarrow
\operatorname{ContextIndividuation}^{\mathsf M}(C;\chi)
\Rightarrow
\operatorname{IndexAdmission}^{\mathsf M}(C\Downarrow i;\chi,\mathcal T).
$$

La relatividad a \(\mathcal T\) pertenece a la **descarga**, no a la realidad individuada. IndAdequate exige fidelidad estructural, independencia del target, fundamento positivo, invariancia, coherencia de frontera, anti-agregación, discriminación de génesis, disciplina de cortes rivales y no-totalización; REV-07g contiene los tests completos. IndexAdmission no implica RegimeTotal ni REC. Un parámetro provisional \(\widehat{i}\) puede servir para auditar una candidatura sin admitirla. IndexRetraction corrige una admisión metateórica defectuosa y no equivale a ContextCessation ontológica.

### 1.4. Juicios metaontológicos de contexto

Introducimos como juicios metateóricos —no predicados ontológicos— identidad e incompatibilidad:

$$
i\simeq_{\mathrm{idx}}j
$$

«dos presentaciones/candidatos corresponden al mismo contexto ontológico», y:

$$
\boxed{
i\mathrel{\#}j
}
$$

«los contextos son genuinamente incompatibles».

$i\mathrel{\#}j$ no describe una relación real entre $R_i$ y $R_j$: es una restricción de tipado. REV-07e añade además la descendencia metaontológica $i\prec_{\mathrm{ctx}}k$ cuando una ContextGenesis tiene a $i$ como precursor de $k$. Descendencia, equivalencia e incompatibilidad no forman una dicotomía/partición automática.

Por ello, si:

$$
i\mathrel{\#}j
$$

entonces expresiones como:

$$
\operatorname{Real}_j(x_i)
$$

o:

$$
\operatorname{Relatum}_j(x_i,f_j)
$$

son **mal tipadas**, no proposiciones falsas.

Ésta es la lectura formal de «la incompatibilidad es el índice».

### 1.5. Primitivas genealógicas

Cada **unidad genealógica local** debe estar fundada en una configuración-originaria ontológicamente unificada $\mathcal O_i$. Un régimen exhaustivo puede contener una o varias unidades genealógicas independientemente justificadas; por tanto, OntOrigin ya no implica por sí solo exhaustividad del contexto.

$\mathcal O_i$ puede ser internamente compleja, pero no puede ser una mera suma, lista o unión metalingüística de raíces independientes. La unidad de cada origen local debe estar testimoniada por estructura ontológica interna independientemente caracterizada.

Introducimos:

$$
\operatorname{OntOrigin}_i(\mathcal O_i),
$$

y eventos generativos de hiperaridad:

$$
\operatorname{GenEvent}_i(e_i,A_i,b_i),
$$

«el evento/proceso ontológico $e_i$, con antecedentes conjuntos $A_i$, genera $b_i$».

La relación binaria:

$$
\operatorname{GenStep}_i(a_i,b_i)
$$

es solo una proyección auxiliar de GenEvent; no basta por sí sola para generar $b_i$ cuando la producción requiere antecedentes conjuntos.

No se presupone un operador mínimo total. Con el predicado de testigo $\operatorname{GenClosure}_i(\mathcal O_i,C_i)$, definido técnicamente en §5.1:

$$
\mathrm{GCExists}_i(\mathcal O_i)
:\Longleftrightarrow
\exists C_i\,\operatorname{GenClosure}_i(\mathcal O_i,C_i),
\qquad
\operatorname{Generated}^{*}_i(\mathcal O_i,x_i)
:\Longleftrightarrow
\exists C_i[
\operatorname{GenClosure}_i(\mathcal O_i,C_i)\land x_i\in C_i
].
$$

Solo bajo GCExists la minimalidad permite abreviar el testigo como $\operatorname{Cl}^{G}_i(\mathcal O_i)$. Para una unidad local la obligación correcta es **soundness**, no exhaustividad del contexto:

$$
\boxed{
\operatorname{OntOrigin}_i(\mathcal O_i)
\land
\operatorname{Generated}^{*}_i(\mathcal O_i,x_i)
\Rightarrow
\operatorname{Real}_i(x_i).
}
$$

La conversa $\operatorname{Real}_i(x_i)\Rightarrow\operatorname{Generated}^{*}_i(\mathcal O_i,x_i)$ solo se obtiene en el caso monogeneal GeneTotal; en general la completitud se formula respecto de RegimeClosure.

$\operatorname{OntOrigin}_i$ es **ontológico, no cronológico ni espacial**: no exige un primer instante, una localización inicial ni un átomo simple. Puede ser atemporal, estructural, cíclico o contener soporte mutuo. Una regresión temporal infinita no refuta por sí sola OntOrigin; REV-07d pregunta, más fuertemente, si puede existir una genealogía sin ninguna base ontológica mínima admisible. Lo que no vale como origen es una agregación arbitraria diseñada para hacer exhaustiva la clausura.

**No circularidad:** OntOrigin, GenEvent y las reglas de clausura no pueden definirse mediante $R_i$, CoReal, SameRegime, SemTotal, Presents ni la extensión final que quieren producir.


### 1.6. $R_i$ — totalización genealógica mono- y multigeneal

Una unidad genealógica local es:

$$
\operatorname{GeneUnit}_i(\mathcal O_{\alpha,i},C_{\alpha,i})
:\Longleftrightarrow
\operatorname{OntOrigin}_i(\mathcal O_{\alpha,i})
\land
\operatorname{GenClosure}_i(\mathcal O_{\alpha,i},C_{\alpha,i}).
$$

GeneTotal se conserva como el caso **monogeneal**:

$$
\operatorname{GeneTotal}_i(\mathcal O_i,R_i)
:\Longleftrightarrow
\exists C_i[
\operatorname{GeneUnit}_i(\mathcal O_i,C_i)
\land
\forall x_i[
\operatorname{Within}_i(x_i,R_i)
\Longleftrightarrow
\operatorname{Real}_i(x_i)
\Longleftrightarrow
x_i\in C_i
]
].
$$

Para una familia metateóricamente parametrizada $\mathfrak G_i$ de GeneUnit ya tipadas en el mismo contexto, §5.1 define GeneBasis, FamilyBase, RegimeClosure y:

$$
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i)
:\Longleftrightarrow
\exists C_i[
\operatorname{RegimeClosure}_i(\mathfrak G_i,C_i)
\land
x_i\in C_i
].
$$

La totalización general es:

$$
\boxed{
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
:\Longleftrightarrow
\operatorname{GeneBasis}_i(\mathfrak G_i)
\land
\forall x_i[
\operatorname{Within}_i(x_i,R_i)
\Longleftrightarrow
\operatorname{Real}_i(x_i)
\Longleftrightarrow
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i)
].
}
$$

RegimeClosure vuelve a cerrar $\Gamma_i$ sobre la base conjunta y por ello incluye producción transversal entre unidades; la mera unión $\bigcup_\alpha C_{\alpha,i}$ no basta. La familia es no vacía, overlap-coherent e irredundante respecto de su propia closure, y su tipado común debe estar justificado **antes** de formar la familia: GeneBasis no puede fabricar SharedOntSpace.

Para $C_i$ la GenClosure de $\mathcal O_i$:

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

La equivalencia vale solo para familias singleton. En general:

$$
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
\not\Rightarrow
\exists\mathcal O_i\;\operatorname{GeneTotal}_i(\mathcal O_i,R_i).
$$

### 1.7. Cierre de hechos e imposibilidad de cruce

Sea:

$$
\operatorname{RealFact}_i(f_i)
$$

un hecho real bien tipado en $i$. Su incidencia satisface:

$$
\boxed{
\operatorname{RealFact}_i(f_i)
\Rightarrow
\forall x_i[
\operatorname{Relatum}_i(x_i,f_i)
\Rightarrow
\operatorname{Real}_i(x_i)
].
}
$$

Si un supuesto hecho conecta dos candidatos que iban a recibir índices diferentes, es evidencia **previa a la indexación** de realizabilidad conjunta. REV-07e distingue ahora dos lecturas: SharedOntSpace si el contexto común preexiste ontológicamente; ContextGenesis si la estructura integradora constituye un contexto nuevo. Ninguna se reduce a CommonGround.

No se formula después:

$$
\operatorname{CrossRealFact}(i,j)
$$

como una relación ontológica entre índices genuinos. Para $i\mathrel{\#}j$, tal expresión queda fuera del lenguaje objeto.

Lo mismo vale para un supuesto origen común: si aparece una base ontológica que genera ambos candidatos, la conclusión es:

$$
i\simeq_{\mathrm{idx}}j,
$$

no que dos realidades incompatibles estén conectadas por una tercera cosa.

### 1.8. CoReal derivada

Dentro de un contexto ya justificado:

$$
\boxed{
\operatorname{CoReal}_i(x_i,y_i)
:\Longleftrightarrow
\operatorname{Real}_i(x_i)
\land
\operatorname{Real}_i(y_i).
}
$$

Bajo RegimeTotal esto equivale a que ambos tokens pertenezcan a la misma RegimeClosure testigo. Solo en el caso singleton GeneTotal puede reescribirse además mediante una única $\operatorname{Generated}^{*}_i(\mathcal O_i,-)$.

CoReal no exige conectividad causal o por caminos entre ambos tokens ni CommonGround entre sus genealogías locales.

### 1.9. ExistsR es una metasentencia, no un cuantificador sobre índices

Para abreviar el metalenguaje escribimos:

$$
\exists^{\mathsf M} i\;\Phi_i
$$

con el significado:

> existe una instanciación admisible del parámetro de contexto $i$ para la cual la sentencia indexada $\Phi_i$ está satisfecha.

$\exists^{\mathsf M}$ **no** es un cuantificador del lenguaje ontológico y no presupone un dominio $I$ de índices.

El target doctrinal se escribe ahora:

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

Y:

$$
\boxed{
\operatorname{NoR}
:\Longleftrightarrow
\neg\operatorname{ExistsR}.
}
$$

Una GeneTotal sigue bastando para refutar No-$R$ por la equivalencia singleton, pero deja de ser el único witness posible.

La versión testimoniada es igualmente metateórica:

$$
\boxed{
\operatorname{WitnessedR}
:\Longleftrightarrow
\exists^{\mathsf M} i\;
\exists S_i\exists\mathfrak G_i\exists R_i[
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
\land
\operatorname{SemTotal}_i(S_i)
\land
\operatorname{Presents}_i(S_i,R_i)
].
}
$$

### 1.10. One-$R$, Many-$R$ y Cluster-$R$ como metatesis

**One-$R$** significa: ExistsR es verdadero y cualesquiera dos realizaciones admisibles de RegimeTotal que el metalenguaje compare resultan del mismo tipo:

$$
i\simeq_{\mathrm{idx}}j.
$$

**Many-$R$** significa: hay metateóricamente dos realizaciones admisibles de RegimeTotal:

$$
i\mathrel{\#}j.
$$

Esto no postula una bolsa que contenga a $i$ y $j$. Es un juicio sobre dos instanciaciones del esquema de realidad.

**Cluster-$R$** solo se aplica a candidatos todavía no tipados definitivamente. Un origen común independientemente justificado fuerza equivalencia de índice; un hecho integrador solo establece JointRealizable. CGP no es derivable de la doctrina vigente y solo podría añadirse como premisa metafísica adicional. Una vez establecido legítimamente $i\mathrel{\#}j$, un «colapso posterior» exige mostrar que aquel juicio era erróneo o introducir explícitamente una teoría de formación/ensamblaje entre contextos.

### 1.11. Verdad, falsedad e incompatibilidad inter-index

Las proposiciones/facts también están tipadas. Sea:

$$
p_i\in\mathcal L_i.
$$

Si:

$$
i\mathrel{\#}j,
$$

entonces $p_i$ no es una proposición de $\mathcal L_j$. Por tanto no se afirma:

$$
\operatorname{False}_j(p_i)
$$

ni:

$$
\neg\operatorname{RealFact}_j(p_i);
$$

ambas expresiones intentan aplicar predicados de $j$ a un término de tipo $i$.

Una comparación externa requiere, **si existe**, una traducción metalingüística parcial o total:

$$
\tau_{ij}:\mathcal L_i\rightsquigarrow\mathcal L_j.
$$

La teoría no postula que tal traducción exista para todo par de contextos. Si no existe ninguna traducción fiel relevante, no hay siquiera una comparación verdad/falsedad entre esos contenidos: hay incommensurabilidad semántica desde el metalenguaje.

Puede ocurrir, por ejemplo:

$$
\operatorname{True}_i(p_i)
\qquad\text{y}\qquad
\operatorname{False}_j(\tau_{ij}(p_i)).
$$

Eso no es una contradicción ontológica transversal: son juicios sobre proposiciones tipadas distintas relacionados solo por una traducción del metalenguaje.

En este sentido:

$$
\boxed{
\text{incompatibilidad inter-index}
\;>\;
\text{contradicción interna}.
}
$$

Para contradecirse literalmente, dos afirmaciones deben compartir un contexto en el que ambas estén bien formadas.

### 1.12. Nada fuera de $R_i$ desde el contexto $i$

Desde el lenguaje interno de $R_i$, un hipotético $R_j$ incompatible no es «algo real pero inaccesible». No pertenece al dominio de tipado de $i$.

Por tanto, dentro de $i$, «fuera de $R_i$» no denota un exterior ontológico oculto. Denota ausencia de contenido bien tipado como real en $i$.

El metalenguaje puede formular la hipótesis Many-$R$, pero esa formulación no constituye un hecho real transversal ni proporciona acceso de $R_i$ a $R_j$.


## 2. Consecuencias estructurales del tipado indexado

Fijado un parámetro de contexto $i$ y una realización:

$$
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i),
$$

se sigue dentro de ese contexto:

$$
\boxed{
\operatorname{Real}_i(x_i)
\Longleftrightarrow
\operatorname{Within}_i(x_i,R_i).
}
$$

Por tanto un supuesto «real de $i$ fuera de $R_i$» es contradictorio:

$$
\operatorname{Real}_i(x_i)
\land
\neg\operatorname{Within}_i(x_i,R_i)
\Rightarrow
\bot.
$$

Esto no demuestra que exista una realización del esquema: esa carga pertenece a REV-07.

### 2.1. Cierre de hechos reales

Si:

$$
\operatorname{RealFact}_i(f_i),
$$

entonces:

$$
\forall x_i[
\operatorname{Relatum}_i(x_i,f_i)
\Rightarrow
\operatorname{Real}_i(x_i)
].
$$

Un término $x_j$ de un contexto incompatible $j$ no puede ocupar esa posición: no es un relatum falso de $f_i$, sino un término de sort incorrecto.

### 2.2. Incompatibilidad como juicio de tipado

El juicio:

$$
i\mathrel{\#}j
$$

no afirma una relación negativa entre dos objetos-realidad. Afirma metateóricamente que no existe un único contexto bien tipado en el que ambos candidatos puedan coexistir como contenido real.

Si antes de cerrar la indexación aparece coexistencia dentro de un **mismo contexto preexistente**, el diagnóstico es SharedOntSpace y las etiquetas provisionales no pueden mantenerse como incompatibles. Una base/origen común añade además CommonGround.

Dos contextos ya establecidos como $i\#j$ no pueden fusionarse mediante un hecho objeto cross-index. Sí pueden figurar como precursores de una relación metateórica $\operatorname{ContextGenesis}^{\mathsf M}(C_i,C_j\Rightarrow k;\gamma)$, cuyas continuaciones se tipan ya en el nuevo contexto $k$.

### 2.3. Consecuencia epistemológica

Si Many-$R$ es metateóricamente verdadero y $i\#j$, ningún hecho real de $R_i$ puede certificar $R_j$, porque una certificación real tendría que ser una fórmula/hecho bien tipado en $i$ con contenido de tipo $j$.

Eso no sería falso: sería imposible de formar dentro de $\mathcal L_i$.

Por ello One-$R$ y Many-$R$ pueden diferir en el metalenguaje sin producir una diferencia internamente certificable en una realización concreta $R_i$.

### 2.4. Verdad invertida entre realizaciones

Sea $p_i\in\mathcal L_i$ y sea una traducción metalingüística:

$$
\tau_{ij}:\mathcal L_i\rightsquigarrow\mathcal L_j.
$$

Es coherente que:

$$
\operatorname{True}_i(p_i)
$$

y:

$$
\operatorname{False}_j(\tau_{ij}(p_i)).
$$

Esto no produce:

$$
p\land\neg p
$$

en ningún contexto común. $p_i$ y $\tau_{ij}(p_i)$ son expresiones tipadas distintas; la correspondencia entre ellas pertenece al metalenguaje.

Por tanto todos los hechos reales de $i$ pueden carecer de cualquier realización homóloga verdadera en $j$ —incluso admitir traducciones invertidas— sin que $i$ y $j$ entren en contradicción ontológica.


## 3. Estado actual del programa emergentista

La propuesta ya dispone de una definición independiente y event-local de emergencia, un operador system-relative construido desde ella, pruebas de F1–F3 dentro de ese tipo y un punto fijo propio explícito.

Por tanto, REV-01, REV-02 y REV-04 están cerrados en sus criterios originales, mientras REV-03 permanece PARTIAL por alcance doctrinal.

El programa dispone de dos construcciones semánticas condicionales. La ruta finita usa el carrier tipado $T^{\Lambda}_{i,q}=[q_i]_{\sim_i}$, PON y $\operatorname{StructAdm}_i$. La ruta generalizada es deliberadamente pre-ontológica: usa $T_q^{\mathcal C}$, `CFragAdm_C`, CSet/CWF/CProcStable y smallness/Separation relativas a la clausura; solo tras adecuación genealógica puede reindexarse como un régimen. Ninguna ruta semántica demuestra por sí sola $\operatorname{ExistsR}$; tampoco decide metateóricamente One-$R$ frente a Many-$R$.

Los bloqueadores activos relevantes pasan a ser:

- **REV-07:** origen y clausura ontológica del régimen: justificar $\operatorname{OntOrigin}_i$, una relación objetivo independiente $\operatorname{OntProd}_i$, una implementación $\operatorname{GenEvent}_i$ con GenSound + GenComplete, y $\mathrm{GCExists}_i$ antes de usar la clausura abreviada; $\operatorname{GenStep}_i$ queda solo como proyección auxiliar y $\Lambda_*$/$\mathcal C_*$ como reconstrucciones candidatas de esa genealogía;
- **REV-07g:** individuación contextual previa a la admisión del índice. Para un witness fuerte de ExistsR, no basta demostrar RegimeTotal condicionalmente bajo un subíndice: la instanciación contextual usada por $\exists^{\mathsf M}i$ debe ser admisible. AI-UD muestra que el reducto objeto interno no recupera siempre la partición contextual; la ruta de trabajo parametriza la descarga mediante $\operatorname{Ind}_{\mathcal T}^{\mathsf M}$ + IndAdequate. No bloquea resultados condicionales con $i$ ya fijado;
- **REV-23:** PON — smallness por-token de la ruta finita; la ruta generalizada puede sustituirlo por `CSet/TransClSmall`;
- **REV-24:** puente de presentación: dado un $R_i$ genealógico justificado por REV-07, demostrar que $S_i$ lo presenta adecuadamente mediante OA/MC/RA;
- **REV-25:** smallness de la firma y legitimidad del paso por Separation sobre «actualmente verdadero»;
- **REV-20:** PSB/K1, ahora derivables de PON en la ruta estructural;
- **REV-22:** aplicabilidad de Zorn, subordinada a las premisas de smallness aunque la ruta directa a $\operatorname{SemTotal}$ no lo necesita;
- **REV-15:** consecuencias metaontológicas discriminantes;
- **REV-26:** extensión metaontológica no bloqueante para el target principal: One-$R$/Many-$R$, generalidad absoluta y comparación entre índices;

## 3.1. Resumen formal vigente

Las demostraciones, contraejemplos y modelos de trabajo que originaron este estado se han movido al [documento de derivaciones técnicas](work/autodescripcion-realidad-distincion-derivaciones-2026-09-22.md). Esta sección registra solo resultados vigentes.

| Finding | Estado | Resultado vigente |
|---|---|---|
| REV-01 | RESOLVED formal | Para un sistema fijo $M$, la relación de eventos emergentes induce $F_M$ como clausura reflexivo-transitiva; F1, F2 interna y F3 se derivan. Para la ruta de Zorn, F2 es redundante: F1 + F3 bastan para elevar cotas a puntos fijos. |
| REV-02 | RESOLVED tipado | La inhibición compara sistemas/operadores distintos, no entradas del mismo $F_M$. Una extensión conductualmente conservativa caracteriza cuándo un evento puede transportarse entre sistemas. |
| REV-03 | PARTIAL | Existe una definición de emergencia event-local, independiente de $R$, basada en macro-invariancia, testigo organizacional y capacidad dinámica habilitada. Sigue pendiente validar su alcance doctrinal en casos ricos. |
| REV-04 | RESOLVED mínimo | El toy de cuatro componentes produce un punto fijo propio explícito de $F_M$. Esto demuestra que el operador no es necesariamente «la unión de todo», pero no caracteriza todavía sistemas ricos. |
| REV-18 | RESOLVED tipado | Un dominio se toma como fragmento semántico positivo actual $X=(T_X,\Phi_X)$; incidencia es pertenencia al carrier semántico y `EClosed_i` es una propiedad del contenido, no de la serialización. No se reifica el dominio como entidad adicional. Este cierre no identifica exhaustividad semántica con totalidad ontológica; esa deuda queda en REV-24. |
| REV-19 | RESOLVED tipado | El objeto primario queda fijado como fragmento procesual semántico $X=(T_X,\Phi_X)$; $\preceq_i^{\mathrm{proc}}$ es inclusión de contenido positivo actual. Admisibilidad ontológica se separa como $\operatorname{Adm}_i$ y queda en REV-18/20/09/07. |
| REV-20 | PARTIAL subordinado | Bajo StructAdm + COV, $K1_i\iff\mathrm{PSB}_i$; PON implica PSB. K1 deja de ser blocker independiente de la ruta directa. |
| REV-22 | PARTIAL subordinado | PON + las condiciones de smallness de REV-25 hacen set-sized cada régimen y su poset de fragmentos, resolviendo condicionalmente la ruta A de Zorn. La ruta directa a $\operatorname{SemTotal}$ no necesita Zorn. |
| REV-09 | RESOLVED set-indexed | Con `Adm_i := StructAdm_i`, la unión de una cadena set-indexed de fragmentos positivos actuales sigue siendo well-formed y admisible; junto con el lema previo de preservación de `EClosed`, K2 queda demostrada dentro del alcance set-sized del teorema. La aplicabilidad class-sized queda en REV-22. |
| REV-10 | RESOLVED vigente | La ruta actual ya no usa la inferencia oculta de StageFactorization/presentabilidad criticada en H8. |
| REV-21 | RESOLVED formal | Los puntos fijos de $F_i$ son exactamente los subconjuntos forward-closed del grafo emergente; la degeneración al único punto fijo no vacío $\Sigma_i$ ocurre exactamente cuando el grafo es fuertemente conexo. |
| REV-23 | OPEN para ruta finita | PON no está justificada. Hace set-sized el componente finitamente conectado, pero la ruta generalizada puede sustituirla por `CSet/TransClSmall`. Ninguna condición de smallness implica por sí sola `ExistsR`. |
| REV-24 | OPEN blocker doctrinal local | El máximo semántico no produce un $R_i$. REV-07 debe justificar primero $\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)$; REV-24 queda reducido a OA/MC/RA sobre la closure de régimen para demostrar $\operatorname{Presents}_i(S_i,R_i)$. Su cierre fortalece `ExistsR` a `WitnessedR`; no crea existencia ontológica. |
| REV-25 | OPEN blocker fundacional/semántico | El teorema usa smallness de la firma y un paso de Separation sobre los hechos «actualmente verdaderos». Deben justificarse la firma/aridades y la disponibilidad metateórica del predicado de actualidad. |
| REV-07g | PARTIAL / blocker de witness fuerte | La identidad contextual no se obtiene de JointRealizable, CommonGround, $\mathcal C_*$, RegimeTotal, REC ni $\Omega_i$ sin circularidad/sobre-restricción. AI-UD muestra subdeterminación si se permiten sectores sin estructura transversal. La ruta vigente usa ContextIndividuation theory-relative + IndAdequate antes de IndexAdmission; la individuación no implica totalidad. |
| REV-26 | OPEN extensión metaontológica | **One-$R$/Many-$R$ y generalidad entre índices.** No bloquea $\operatorname{ExistsR}$. Un origen común entre dos candidatos implica que pertenecen al mismo índice; Many-$R$ genuino exige índices incompatibles por tipado, no una condición adicional de aislamiento. |

### Corrección histórica importante sobre F2

Durante la exploración se sostuvo temporalmente que sin F2 no podía elevarse una cota $U$ de una cadena de puntos fijos a una cota fija. Ese diagnóstico fue **erróneo** y queda marcado `SUPERSEDED` en el documento técnico.

Si:

$$
X\preceq U
$$

y F1 da:

$$
U\preceq F(U),
$$

entonces, por transitividad:

$$
X\preceq F(U).
$$

F2 no interviene. F3 garantiza después:

$$
F(F(U))=F(U).
$$

Por tanto, la monotonía interna de $F_M$ sigue siendo verdadera, pero **no es necesaria para ese paso de Zorn**.

### Alcance de los cierres formales

Los cierres de REV-01 y REV-04 son deliberadamente limitados:

- REV-01 demuestra propiedades formales de una clausura reflexivo-transitiva; esas propiedades valdrían para cualquier relación binaria del mismo tipo. El contenido específicamente emergentista reside en la definición y justificación de $\mathcal E_M$, todavía PARTIAL bajo REV-03.
- REV-04 demuestra la existencia de un punto fijo propio en un toy mínimo. No demuestra por sí solo que $F_M$ siga siendo discriminante en sistemas con redes densas o fuertemente conectadas de eventos emergentes. Esa cuestión se registra separadamente en el ledger.

### Blockers ontológicos actuales

La existencia ontológica y su representación quedan ahora separadas:

1. **REV-07/REV-07g:** justificar primero una individuación contextual admisible/IndexAdmission y, dentro de ese contexto, GeneUnit locales, una GeneBasis no redundante, la relación objetivo independiente $\operatorname{OntProd}_i$, una implementación $\operatorname{GenEvent}_i$ sound-and-complete y existencia de RegimeClosure; solo entonces $\operatorname{RegimeGenerated}^{*}_i$ puede realizar un $R_i$, mientras $\operatorname{GenStep}_i$ permanece una proyección auxiliar;
2. **REV-23:** justificar PON solo si se conserva la reconstrucción finita por $\Lambda_*$;
3. **REV-24:** dado un $R_i$ genealógico ya justificado, demostrar OA/MC/RA y $\operatorname{Presents}_i(S_i,R_i)$;
4. **REV-25:** justificar la smallness de firma/aridades y el predicado de actualidad usado por Separation.

REV-26 queda fuera de esta lista: es una extensión metaontológica no bloqueante sobre One-$R$/Many-$R$ y expresividad global. REV-20 y REV-22 quedan como consecuencias/alternativas de las premisas de smallness. El teorema semántico directo entrega $\operatorname{SemTotal}$; la existencia de una realidad depende de REV-07, no de la maximalidad semántica.

---

## 3.2. Localidad ontológica de la emergencia

La propuesta adopta provisionalmente una separación fuerte entre **emergencia interna a una realidad ontológica concreta** y **metaontología de la pluralidad de realidades**.

Fijado un régimen ontológico $i$, la maquinaria emergentista se indexa:

$$
\mathcal E_i,
\qquad
\mathfrak D_i^{\mathrm{proc}},
\qquad
\preceq_i,
\qquad
\mathfrak K_i,
$$

y, cuando exista una representación system-relative apropiada:

$$
F_i.
$$

El teorema de máximo pregunta únicamente por la estructura interna del poset semántico del régimen:

$$
K1_i+K2_i+K3_i
\Rightarrow
\exists S_i\in\mathfrak K_i:
\forall X\in\mathfrak D_i^{\mathrm{proc}},
\quad
X\preceq_i S_i.
$$

Como $S_i\in\mathfrak K_i$, además:

$$
\operatorname{EClosed}_i(S_i).
$$

Por tanto K1–K3 producen exactamente:

$$
\boxed{\operatorname{SemTotal}_i(S_i).}
$$

### Objetivo real de esta maquinaria: presentación semántica

K1–K3 producen exactamente:

$$
\boxed{\operatorname{SemTotal}_i(S_i).}
$$

Eso no establece una genealogía ontológica.

La existencia local fuerte pertenece a REV-07:

$$
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
\Rightarrow
\operatorname{ExistsR}.
$$

GeneTotal conserva esta implicación como corolario singleton.

Si REV-07 ha justificado esa genealogía, REV-24 intenta demostrar:

$$
\operatorname{SemTotal}_i(S_i)
+
\mathrm{OTB}_i
\Rightarrow
\operatorname{Presents}_i(S_i,R_i),
$$

y por tanto:

$$
\boxed{
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
+
\operatorname{SemTotal}_i(S_i)
+
\mathrm{OTB}_i
\Rightarrow
\operatorname{Presents}_i(S_i,R_i)
\land
\operatorname{WitnessedR}.
}
$$

La maquinaria semántica no crea el origen, la clausura ni el alcance ontológico.

One-$R$/Many-$R$ quedan como extensiones metateóricas de REV-26 y no forman parte de esta inferencia.

### Qué significa aquí «cerrado»

La conclusión inmediata del teorema actual es:

$$
\boxed{
\operatorname{EClosed}_i(S_i)
}
$$

porque $S_i\in\mathfrak K_i$.

No debe escribirse todavía, sin una precisión adicional de tipos:

$$
S_i=F_i(S_i).
$$

Esa igualdad solo estará justificada si se construye un operador sobre **el mismo tipo de dominios procesuales**:

$$
F_i^{\mathrm{proc}}:
\mathfrak D_i^{\mathrm{proc}}
\to
\mathfrak D_i^{\mathrm{proc}}
$$

con:

$$
\operatorname{Fix}(F_i^{\mathrm{proc}})
=
\mathfrak K_i.
$$

En ese caso sí:

$$
S_i\in\mathfrak K_i
\Rightarrow
F_i^{\mathrm{proc}}(S_i)=S_i.
$$

La forma tipada del resultado semántico es «existe un máximo $S_i$ y es E-closed». La existencia ontológica de $R_i$ requiere REV-07 y una base genealógica total:

$$
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i).
$$

REV-24 solo debe justificar después:

$$
\operatorname{Presents}_i(S_i,R_i).
$$

Por tanto no se identifica por mera maximalidad:

$$
\boxed{
S_i
\neq_{\mathrm{justified}}
R_i
}
$$

mientras REV-24 permanezca abierto.

### Emergencia local no implica One-$R$

Si el metalenguaje considera dos realizaciones con:

$$
i\mathrel{\#}j,
$$

sus teorías internas pueden estar ambas bien formadas sin relación ontológica transversal:

$$
\mathcal E_i
\qquad\text{y}\qquad
\mathcal E_j.
$$

Así:

$$
\boxed{
\text{emergencia local}
\not\Rightarrow
\text{One-R global}.
}
$$

La posibilidad de Strong Many-R queda, por tanto, **desacoplada** del teorema de emergencia.

### K3 queda estrictamente indexada

La condición de amalgamación se interpreta desde ahora como:

$$
K3_i:
\forall X,Y\in\mathfrak D_i^{\mathrm{proc}}\;
\exists Z\in\mathfrak D_i^{\mathrm{proc}}:
X\preceq_i Z
\land
Y\preceq_i Z.
$$

K3_i excluye incomparabilidad fuerte **dentro de $i$**, pero no entre $i$ y $j$.

No se permite inferir, ni siquiera metateóricamente:

$$
\bigl(\forall^{\mathsf M} i\;K3_i\bigr)
\Rightarrow
K3_{\mathrm{abs}}.
$$

Tampoco se introduce cuantificación objeto universal/existencial sobre el parámetro de contexto ni un dominio ontológico de índices.

El problema One-R/Many-R queda como problema metaontológico independiente.

### Meta-notación sin colector ontológico

La formulación vigente evita toda notación que presente los $R_i$ como una familia indexada por un dominio de índices. Para comparar varias realizaciones se usan directamente metavariables de contexto y juicios como:

$$
i\simeq_{\mathrm{idx}}j
\qquad\text{o}\qquad
i\mathrel{\#}j.
$$

Esta metanotación no afirma un conjunto universal de realidades ni una realidad superior que contenga a todas.

En particular:

$$
\boxed{
\text{hablar pluralmente de }R_i
\not\Rightarrow
\exists R_{\mathrm{abs}}.
}
$$

### Exhaustividad interna y verdad absoluta

Se abandona la identificación histórica:

$$
\operatorname{VA}(o)=R_i.
$$

Se distinguen:

$$
\operatorname{Truth}_i
$$

como verdad/exhaustividad relativa a todo lo que constituye el régimen $i$, de una hipotética:

$$
\operatorname{Truth}_{\mathrm{abs}},
$$

cuya existencia y coherencia permanecen abiertas.

Por tanto:

$$
\boxed{
\text{exhaustividad interna}
\neq
\text{absolutidad global}.
}
$$

Esto neutraliza la antigua solución verbal de llamar «Verdad Absoluta indexada» a un máximo relativo.

### Consecuencia metodológica

REV-18, REV-19, REV-20 y REV-09 deben resolverse **por régimen $i$**. Ninguna de sus soluciones necesita primero resolver One-R/Many-R.

REV-07 queda reducido a una obligación más precisa: justificar independientemente qué hace que dos dominios pertenezcan al mismo régimen $i$ y por qué ese régimen satisface K3_i, sin definir «mismo régimen» como «amalgamable».

---

## 3.3. Admisibilidad estructural mínima

El predicado abstracto $\operatorname{Adm}_i$ se concreta normativamente como **well-formedness de contenido ontológico positivo actual**.

Un dominio procesual:

$$
X=(T_X,\Phi_X)
$$

es admisible cuando:

1. todos sus tokens pertenecen al mismo régimen $i$;
2. todos los tokens y hechos incluidos son actuales;
3. todo hecho incluye en $T_X$ sus relata;
4. todo evento incluye source y target únicos;
5. la precedencia/dependencia incluida es acíclica/coherente;
6. el fragmento contiene solo contenido positivo: una extensión puede añadir hechos sin retractar los anteriores.

Es decir:

$$
\boxed{
\operatorname{Adm}_i(X)
:=
\operatorname{StructAdm}_i(X).
}
$$

Esta elección tiene una lectura ontológica deliberadamente austera:

> un dominio no es una entidad adicional dentro de la realidad; es un **fragmento semántico de alcance ontológico actual**.

Por tanto, un máximo $S_i$ del poset de dominios no introduce una sustancia, conjunto universal o colector físico adicional: representa exhaustivamente el contenido semántico del régimen dentro del tipo formal elegido. REV-24 no autoriza a renombrarlo como $R_i$; debe justificar una relación $\operatorname{Presents}_i(S_i,R_i)$ con un alcance ontológico distinto.

### Consecuencias demostradas

Con esta definición:

- **incidencia:** $q\trianglelefteq_i X$ significa exactamente $q\in T_X$; esto cierra REV-18 en su problema de tipos;
- **extensión por evento:** añadir el footprint de un evento emergente actual preserva StructAdm, por lo que OEA se deriva;
- **extensión por enlace:** añadir el footprint de una relación actual de $\Lambda_*$ preserva StructAdm, por lo que la EEA relevante se deriva;
- **unión binaria:** la unión de dos fragmentos del mismo régimen sigue siendo StructAdm; por tanto K3$_i$ se deriva directamente una vez fijada la identidad del régimen;
- **uniones de cadenas set-indexed:** preservan StructAdm; combinadas con la preservación formal de EClosed, demuestran K2$_i$ en el alcance set-sized.

La razón de coherencia es que solo se acumulan hechos positivos **actuales**. Un conflicto funcional o un ciclo finito de precedencia no puede aparecer por unir hechos que son conjuntamente verdaderos en el mismo régimen; si apareciese, la propia semántica de actualidad/proceso sería inconsistente.

### Cobertura

Para todo token o hecho actual de aridad finita del régimen existe un footprint well-formed set-sized que lo contiene. Por tanto:

$$
\mathrm{COV}_i:
\quad
\forall q\text{ actual en }i
\;\exists X\in\mathfrak D_i^{\mathrm{proc}}:
q\trianglelefteq_i X.
$$

Si un máximo semántico domina todos los dominios admisibles, COV$_i$ implica que contiene todo contenido actual del régimen representable por la firma procesual. Esta conclusión es $\operatorname{SemTotal}$; identificarla con totalidad ontológica requiere además REV-24.

### Precio conceptual

Este paso adopta como tesis metodológica que **todo fragmento positivo actual y well-formed cuenta como dominio legítimo** para el teorema. Si en el futuro se exige una noción más fuerte de dominio —por ejemplo cierre causal o nomológico previo— REV-18/REV-09 deberán reabrirse.

---

## 3.4. Construcción de K1 y smallness local

Con StructAdm, la cofinalidad K1 ya no necesita asumirse globalmente.

Definimos:

$$
\operatorname{Pend}_i(X)
$$

como las obligaciones emergentes actuales cuyo source ya está en $X$ pero cuyo evento/target/footprint todavía no está completamente incorporado.

Una ronda satisface todas las obligaciones pendientes de un dominio; las nuevas obligaciones activadas se procesan en la ronda siguiente.

Como la emergencia se propaga por caminos finitos, la unión de las rondas:

$$
X_0
\preceq_i
X_1
\preceq_i
\cdots
\preceq_i
X_\omega
$$

es E-closed siempre que cada ronda maneje un conjunto de obligaciones.

### PSB — Pointwise Set-like Branching

La condición suficiente más local es:

$$
\mathrm{PSB}_i:
\quad
\forall s,
\;
\operatorname{Out}_i(s)
=
\{e\mid \operatorname{Emergent}_i(e)\land\operatorname{src}(e)=s\}
\text{ es set-sized}.
$$

Para cualquier conjunto de sources $S$, Replacement + Union dan:

$$
\bigcup_{s\in S}\operatorname{Out}_i(s)
$$

como conjunto. Por tanto PSB implica que cada ronda y todo cono de alcanzabilidad emergente finita generado desde un dominio set-sized permanecen set-sized.

Con StructAdm, las extensiones de un evento y las uniones set-indexed preservan admisibilidad. Así:

$$
\boxed{
\operatorname{StructAdm}_i
+
\mathrm{PSB}_i
\Rightarrow
K1_i.
}
$$

El documento técnico contiene la construcción completa por rondas.

### Estado de REV-20

REV-20 permanece **PARTIAL** y queda reducido a una única cuestión estructural.

Con StructAdm, COV y dominios set-sized se demuestra además la conversa:

$$
K1_i
\Rightarrow
\mathrm{PSB}_i,
$$

porque una extensión E-closed de un fragmento que contiene $s$ debe contener todos los eventos emergentes actuales salientes de $s$, y su carrier es un conjunto.

Por tanto:

$$
\boxed{
K1_i
\iff
\mathrm{PSB}_i.
}
$$

La pregunta restante es exactamente:

> ¿puede un único estado actual ser source de proper-class many eventos emergentes actuales?

El potencialismo ordinario de «siempre hay una extensión más» no basta para negar K1; dentro de esta arquitectura, debe aparecer una ramificación propia-clase local.

PSB es independiente de REV-22: resuelve la smallness **local del cierre de cada dominio**, mientras REV-22 pregunta por la smallness/aplicabilidad global de Zorn sobre la colección de dominios.

## 4. Núcleo formal vigente

Esta sección contiene solo los **enunciados normativos** necesarios para auditar la propuesta. Las demostraciones completas, contraejemplos, rutas alternativas y stress tests viven en [derivaciones técnicas](work/autodescripcion-realidad-distincion-derivaciones-2026-09-22.md).

La separación es deliberada: el documento normativo no debe volver a crecer por acreción técnica.

### 4.1. Ruta A — exhaustividad semántica sobre una componente $\Lambda$ tipada

Fijado un parámetro de contexto $i$ y un seed bien tipado $q_i$, definimos la componente candidata:

$$
T^{\Lambda}_{i,q}
:=
[q_i]_{\sim_i},
$$

donde $\sim_i$ es la clausura por caminos finitos de $\bowtie_i$ **dentro del contexto $i$**.

La hipótesis local de smallness es también tipada:

$$
\mathrm{PON}_i:
\quad
\forall q_i\;
N_i(q_i)
=
\{r_i\mid q_i\bowtie_i r_i\}
\text{ es set-sized}.
$$

Esto prueba smallness de $T^{\Lambda}_{i,q}$, no cardinalidad del parámetro $i$.

Con $\mathrm{SigSmall}_i$ y $\mathrm{ActualSep}_i$, definimos:

$$
\Phi^{\Lambda,\mathrm{all}}_{i,q}
=
\{
\varphi\in
\operatorname{Atoms}_{\mathcal L_i}(T^{\Lambda}_{i,q})
\mid
\operatorname{Actual}_i(\varphi)
\},
$$

$$
S^{\Lambda,*}_{i,q}
:=
(T^{\Lambda}_{i,q},\Phi^{\Lambda,\mathrm{all}}_{i,q}).
$$

Aquí $\Phi^{\Lambda,\mathrm{all}}_{i,q}=\operatorname{Diag}^{+}_{\mathcal L_i}(T^{\Lambda}_{i,q})$: el diagrama atómico positivo actual en el sentido Robinson/Hodges, no el diagrama completo con literales negativos.

El resultado matemático correcto es **closure-relative**:

$$
\boxed{
\mathrm{PON}_i
+
\mathrm{SigSmall}_i
+
\mathrm{ActualSep}_i
+
\operatorname{StructAdm}^{\Lambda}_{i,q}
\Rightarrow
\operatorname{SemTotal}^{\Lambda}_{i,q}(S^{\Lambda,*}_{i,q}).
}
$$

No se escribe todavía $\operatorname{SemTotal}_i$: la componente finitamente conectada puede subincluir la genealogía real.

El upgrade de carrier exige reconstrucción genealógica:

$$
\mathrm{RS}^{\mathrm{gen}}_{\Lambda,i}
\land
\mathrm{RC}^{\mathrm{gen}}_{\Lambda,i}.
$$

Bajo esas dos obligaciones:

$$
T^{\Lambda}_{i,q}
=
\{x_i\mid
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i)
\},
$$

y entonces, junto con la adecuación semántica/factual restante, puede reetiquetarse el resultado como:

$$
\operatorname{SemTotal}_i(S_i^*).
$$

La condición común de la implementación semántica set-based es $\operatorname{SemCarrierSmall}(T):\Leftrightarrow T$ set-sized. PON la deriva para $T^{\Lambda}_{i,q}$; CSet es su instancia en Ruta B y TransClSmall puede descargarla en un estadio estabilizado. Ninguna es condición ontológica de existencia de $R$.


### 4.2. Ruta B — clausura integrativa generalizada pre-ontológica

Si la clausura finita es insuficiente, se permite una clausura candidata:

$$
\mathcal C_*:A\mapsto\mathcal C_*(A),
$$

generada por reglas integrativas especificadas mediante CGI/CMin sin usar $\operatorname{CoReal}$, $R_i$, $S_i$, $\operatorname{Presents}$, $\operatorname{OntTotal}$ ni el resultado final de la propia clausura.

Para un seed $q$:

$$
T_q^{\mathcal C}:=\mathcal C_*(\{q\}).
$$

Mientras CS/CC no estén justificadas, este carrier **no se denomina régimen** y no recibe índice ontológico $i$.

El teorema semántico closure-relative usa únicamente:

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

Con esas premisas se construye $S_q^{\mathcal C}$ usando igualmente $\Phi_q^{\mathrm{all},\mathcal C}=\operatorname{Diag}^{+}_{\mathcal L_{\mathcal C}}(T_q^{\mathcal C})$, y:

$$
\boxed{
\mathrm{CSet}
+
\mathrm{CWF}
+
\mathrm{CProcStable}
+
\mathrm{SigSmall}_{\mathcal C}
+
\mathrm{ActualSep}_{\mathcal C}
\Rightarrow
\operatorname{SemTotal}_{\mathcal C}(S_q^{\mathcal C}).
}
$$

Este teorema es deliberadamente **pre-ontológico**. No contiene $\operatorname{StructAdm}_i$, SameRegime, CS, CC ni $\operatorname{CoReal}$ entre sus premisas.

Solo después, dada una realización tipada $\eta_i^{\mathcal C}$, se investigan las obligaciones vigentes:

$$
\mathrm{CS}^{\mathrm{gen}}_{\mathcal C,i}:\;
a\in T_q^{\mathcal C}\land\eta_i^{\mathcal C}(a)=x_i
\Rightarrow\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i),
\qquad
\mathrm{CC}^{\mathrm{gen}}_{\mathcal C,i}:\;
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i)
\Rightarrow\exists a\in T_q^{\mathcal C}\;\eta_i^{\mathcal C}(a)=x_i.
$$

Junto con CRType, RA y scope realization, estas obligaciones permiten reindexar la construcción como $S_i^{\mathcal C}$.

FID es solamente una condición suficiente de la Ruta A; un fallo de FID no implica $\neg\operatorname{ExistsR}$.

### 4.3. REV-24 — presentación semántica de una realidad genealógica

$S_i$ y $R_i$ son tipos distintos. REV-07 debe justificar primero:

$$
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i).
$$

REV-24 pregunta después si un máximo semántico $S_i$ presenta adecuadamente esa realidad. GeneTotal queda cubierto automáticamente como caso singleton.

#### REV-24a — Ontological Anchoring (OA)

$$
\mathrm{OA}_i(S;\mathfrak G_i):
\quad
\forall a\in T_S\;
\exists x[
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x)
\land
\operatorname{Den}_i(a,x)
].
$$

OA impide que el carrier semántico sobreincluya contenido ajeno a la closure total del régimen. En Ruta A, RS se interpreta como soundness respecto de RegimeGenerated$^*$.

#### REV-24b — Membership Completeness (MC)

$$
\mathrm{MC}_i(S;\mathfrak G_i):
\quad
\forall x[
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x)
\Rightarrow
\exists a\in T_S\;
\operatorname{Den}_i(a,x)
].
$$

MC impide que $S_i$ omita contenido de la closure del régimen. En Ruta A, RC debe cubrir RegimeGenerated$^*$; en Ruta B, la realización tipada $\eta_i^{\mathcal C}$ debe ser completa respecto de la misma extensión. FID sigue siendo solo una vía suficiente para casos monogeneales/finitamente reconstruibles y no una condición de RegimeTotal.

#### REV-24c — Representational Adequacy (RA)

$\mathrm{RA}_i(S,R_i)$ debe garantizar que la presentación preserva y refleja no solo miembros, sino la estructura genealógica/procesual relevante:

- identidades;
- relaciones de generación locales y transversales;
- dependencias constitutivas relevantes;
- procesos que mantienen la closure;
- invariancia bajo recodificaciones fieles.

RA permanece OPEN y debe coordinarse con REV-25.

#### REV-24d — Scope Realization

La realización de scope no es algo que $S_i$ produzca: forma parte de establecer RegimeTotal en REV-07. Una ruta plural no reificante puede escribirse como:

$$
\exists rr_i\;
\forall x[
x\prec rr_i
\Longleftrightarrow
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x)
],
$$

condicionada a la lógica plural adoptada.

#### Esquema OTB local revisado

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

REV-24 **no demuestra la existencia de $R_i$**. Si REV-07 ya ha establecido RegimeTotal, ExistsR ya es una conclusión ontológica; REV-24 permite fortalecerla a WitnessedR.

### 4.4. Ruta Zorn — resultado auxiliar

La ruta operator-free se conserva como resultado estructural auxiliar.

Sea $(\mathfrak D,\preceq)$ un poset set-sized no vacío y $\mathfrak K\subseteq\mathfrak D$. Si:

- K1: $\mathfrak K$ es cofinal en $\mathfrak D$;
- K2: toda cadena de $\mathfrak K$ tiene una cota superior en $\mathfrak K$;
- K3: $\mathfrak D$ es directed;

entonces existe $S\in\mathfrak K$ tal que:

$$
\boxed{
\forall X\in\mathfrak D,\quad
X\preceq S.
}
$$

El resultado es semántico. Zorn no proporciona $R_i$, no resuelve REV-24 y no es necesario para las dos construcciones directas anteriores cuando sus premisas de smallness están disponibles.

Para un operador extensivo e idempotente, F1 + F3 bastan para elevar cotas a puntos fijos en esta ruta concreta; F2 es redundante para ese paso. La demostración completa permanece en work/.

### 4.5. Estado normativo del núcleo formal

**Demostrado condicionalmente:**

1. Ruta A: PON$_i$ + $\mathrm{SigSmall}_i$ + $\mathrm{ActualSep}_i$ + $\operatorname{StructAdm}^{\Lambda}_{i,q}$ producen $\operatorname{SemTotal}^{\Lambda}_{i,q}(S^{\Lambda,*}_{i,q})$; solo RS/RC permiten elevarlo a $\operatorname{SemTotal}_i$.
2. Ruta B: CSet + CWF + CProcStable + $\mathrm{SigSmall}_{\mathcal C}$ + $\mathrm{ActualSep}_{\mathcal C}$ producen $\operatorname{SemTotal}_{\mathcal C}(S_q^{\mathcal C})$ sin suponer todavía que la clausura sea un régimen.
3. K1–K3 producen un máximo semántico bajo las condiciones fundacionales declaradas.
4. En Ruta A, RS$^{gen}_{\Lambda,i}$ + CD descargan condicionalmente OA del carrier; RC$^{gen}_{\Lambda,i}$ + CD descargan condicionalmente MC.

**No demostrado:**

1. la existencia/adecuación de una base $\mathcal O_i$ y de su clausura ontológica —REV-07—;
2. la adecuación de $\Lambda_*$ o $\mathcal C_*$ como reconstrucción de esa genealogía;
3. REV-24c/RA y, por tanto, la presentación completa por $S_i$;
4. $\operatorname{ExistsR}$ sin cerrar la obligación genealógica de REV-07;
5. One-$R$/Many-$R$ y cualquier generalidad meta-indexada, que quedan en REV-26 y no bloquean el target principal.

Esta separación es normativa. Cualquier detalle técnico nuevo debe incorporarse primero al documento work/; el normativo solo se amplía cuando cambie uno de estos enunciados, dependencias o estados.

---

## 5. Identidad genealógica de régimen — REV-07

La identidad de una realidad indexada queda anclada primariamente en **origen + clausura ontológica**, no en K3, maximalidad semántica ni conectividad elegida ad hoc.

### 5.1. Criterio primario: origen unificado + generación independiente

REV-07 exige una configuración-originaria que no pueda fabricarse agregando raíces independientes. OriginConfig es además relacionalmente well-formed: ninguna relación-token actual puede quedar en el seed sin su footprint ontológico obligatorio.

$$
\boxed{
\operatorname{OriginCandidate}_i(\mathcal O_i)
:\Longleftrightarrow
\mathrm{OriginConfig}_i(\mathcal O_i)
\land
\mathrm{OriginUnity}_i(\mathcal O_i)
\land
\mathrm{RootClosed}_i(\mathcal O_i)
}
$$

y:

$$
\boxed{
\operatorname{OntOrigin}_i(\mathcal O_i)
:\Longleftrightarrow
\operatorname{OriginCandidate}_i(\mathcal O_i)
\land
\mathrm{GenAdequate}_i
\land
\mathrm{GCExists}_i(\mathcal O_i)
\land
\mathrm{Irredundant}_i(\mathcal O_i)
}
$$

**OriginUnity.** El antiguo $\operatorname{OriginConstitutive}_i(f_i,U_i)$ queda SUPERSEDED por un criterio relativo a la partición. $\operatorname{ConstitutiveBridge}_i(f_i,U_i;A_i,B_i)$ exige un UnitFact actual cuyo UnitFoot contenga dependencia constitutiva esencial cruzada hacia **ambos** lados; esa dependencia, $\operatorname{EssConDep}_i$, se caracteriza sin Seed, OriginUnity, $R_i$, CoReal, Generated$^*$, SameRegime, equivalencia de índice ni CGP.

$$
\boxed{
\operatorname{OriginUnity}_i(\mathcal O_i)
\Longleftrightarrow
\forall A_i,B_i[
\operatorname{Partition}_i(\operatorname{Seed}_i(\mathcal O_i);A_i,B_i)
\Rightarrow
\exists f_i,U_i[
\operatorname{ConstitutiveBridge}_i(f_i,U_i;A_i,B_i)
\land
\operatorname{UnitFoot}_i(f_i,U_i)\preceq\operatorname{Seed}_i(\mathcal O_i)
]].
}
$$

La bilateralidad admite co-dependencia fundamental, constitución relacional/holística y co-constitución procesual cuando satisfacen ECD1–ECD7, pero rechaza una mera convergencia $a_i,b_i\to c_i$: que $c_i$ dependa del evento no vuelve dependientes retroactivamente a $a_i$ y $b_i$. El work/ fija los esquemas MOD/RLC/HC/PC, seis modelos de control y demuestra candidate-independence + no-retroactivity. REV-07a queda RESOLVED como criterio; la existencia de testigos concretos pertenece a OntOrigin/ExistsR. En particular:

$$
\operatorname{Seed}_i(\mathcal O_i)=A_i\cup B_i
\land
\mathrm{NoConstitutiveBridge}_i(A_i,B_i)
\Rightarrow
\neg\operatorname{OriginUnity}_i(\mathcal O_i).
$$

**RootClosed.** La producción objetivo independiente es $\operatorname{OntProd}_i(e_i,A_i,b_i)$ y su footprint incluye al menos $A_i\cup\{e_i,b_i\}$. Se exige:

$$
b_i\in\operatorname{Seed}_i(\mathcal O_i)
\land
\operatorname{OntProd}_i(e_i,A_i,b_i)
\Rightarrow
\operatorname{GenFoot}_i(e_i,A_i,b_i)
\preceq
\operatorname{Seed}_i(\mathcal O_i).
$$

Esto permite ciclos internos pero excluye antecedentes o eventos productores externos.

**Irredundant.** Solo compiten subconfiguraciones que siguen siendo OriginCandidate y tienen closure:

$$
\mathrm{Irredundant}_i(\mathcal O_i)
\Longleftrightarrow
\neg\exists\mathcal O'_i\prec\mathcal O_i[
\operatorname{OriginCandidate}_i(\mathcal O'_i)
\land
\mathrm{GCExists}_i(\mathcal O'_i)
\land
\operatorname{Cl}^{G}_i(\mathcal O'_i)
=
\operatorname{Cl}^{G}_i(\mathcal O_i)
].
$$

**Adecuación generativa.** $\operatorname{OntProd}_i$ permanece como relación objetivo independiente. El work/ fija OP1–OP8 y cuatro modos núcleo —CAU/CON/GRD/PRC— que implican OntProd; $\operatorname{GenEvent}_i$ implementa exactamente esos modos. Por ello GenSound se deriva, mientras GenComplete exige la obligación sustantiva:

$$
\mathrm{ProdCoverage}_i:\quad
\operatorname{OntProd}_i(e_i,A_i,b_i)
\Rightarrow
\operatorname{CausalProd}_i\lor\operatorname{ConstitutiveProd}_i\lor\operatorname{GroundProd}_i\lor\operatorname{ProcessProd}_i.
$$

GF1–GF6 impiden omitir o inflar GenFoot y P1–P8 fijan los contraejemplos. PureOntRel es ontológica pero no productiva: POR1–POR7 + RelSupportClosed impiden relaciones colgantes o endpoints introducidos gratis, y no cuenta como quinta familia de ProdCoverage. REV-07b sigue PARTIAL exactamente por ProdCoverage; GenStep continúa siendo solo una proyección auxiliar.

El operador generativo añade el footprint completo de cada hiperevento cuyos antecedentes están disponibles:

$$
\Gamma_i(X_i)
:=
X_i
\cup
\bigcup\{
\operatorname{GenFoot}_i(e_i,A_i,b_i)
\mid
\operatorname{GenEvent}_i(e_i,A_i,b_i)
\land
A_i\preceq X_i
\}.
$$

**Existencia de closure.** No se presupone un operador $\mu$ total. `GenClosure_i(O_i,C_i)` significa que $C_i$ contiene el seed, es fijo de $\Gamma_i$ y es mínimo entre esos carriers; entonces:

$$
\boxed{
\mathrm{GCExists}_i(\mathcal O_i)
:\Longleftrightarrow
\exists C_i\;
\operatorname{GenClosure}_i(\mathcal O_i,C_i).
}
$$

Generated$^*$ permanece siempre definido relacionalmente mediante un testigo GenClosure; **solo** la abreviatura $\operatorname{Cl}^{G}_i(\mathcal O_i)$ requiere GCExists. Las demostraciones de extensividad, monotonía, minimalidad y el detalle fundacional están en `work/`.

**REV-07f — cierre de una base genealógica plural.** La familia es maquinaria **metateórica**, no un colector ontológico. La representamos como:

$$
\mathfrak G_i
=
\langle G_{\alpha,i}\rangle_{\alpha\in A},
\qquad
G_{\alpha,i}
=
\langle\mathcal O_{\alpha,i},C_{\alpha,i}\rangle,
$$

donde $A$ es solo un parámetro de indexación del metalenguaje, ajeno al sort ontológico de $i$. La familia se forma únicamente después de que sus miembros hayan sido tipados en el mismo contexto; no puede usarse para demostrar retrospectivamente SharedOntSpace ni para colapsar índices incompatibles.

Formalmente:

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

Los cuantificadores sobre $\alpha,\beta$ pertenecen al metalenguaje y no introducen objetos en $R_i$. OverlapCoherence se exige solo entre **miembros distintos**; la coherencia de una GeneUnit consigo misma no es una premisa adicional de GeneFamily. La fundación concreta de $A$ —set, clase, pluralidad u otra presentación— queda subordinada a REV-07c cuando afecte a existencia de closure.

La base extensional de la familia queda fijada, sin elegirla post hoc, por:

$$
\boxed{
\operatorname{FamilyBase}_i(\mathfrak G_i,B_i)
:\Longleftrightarrow
\forall x_i[
x_i\in B_i
\Longleftrightarrow
\exists^{\mathsf M}\alpha\in A\;
x_i\in C_{\alpha,i}
].
}
$$

La closure del régimen **no** es esa unión. Debe volver a cerrar el mismo operador generativo para recoger producción transversal:

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

Definimos:

$$
\mathrm{RGCExists}_i(\mathfrak G_i)
:\Longleftrightarrow
\exists C_i\;
\operatorname{RegimeClosure}_i(\mathfrak G_i,C_i),
$$

y RegimeGenerated$^*$ como en §1.6.

Para bloquear family stuffing usamos la relación metateórica $\operatorname{ProperSubfamily}^{\mathsf M}$, no el orden interno de configuraciones-originarias:

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
\Longleftrightarrow
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i)
]
].
\end{aligned}
}
$$

Finalmente:

$$
\boxed{
\operatorname{GeneBasis}_i(\mathfrak G_i)
:\Longleftrightarrow
\operatorname{GeneFamily}_i(\mathfrak G_i)
\land
\mathrm{RGCExists}_i(\mathfrak G_i)
\land
\mathrm{FamilyIrredundant}_i(\mathfrak G_i).
}
$$

Cada miembro sigue teniendo que ser una GeneUnit independientemente justificada por OntOrigin + GenClosure. Si un token derivado se intenta reetiquetar como origen singleton, RootClosed/OntProd debe rechazarlo cuando su producción esté correctamente representada; si OntProd omite esa producción, el fallo pertenece a REV-07b, no a REV-07f. Una pluralidad de raíces realmente primitivas e independientes, en cambio, es precisamente un caso multigeneal legítimo.

La existencia fundacional de RegimeClosure hereda REV-07c: la definición no presupone que toda GeneFamily admisible posea automáticamente un least fixed point.

### 5.2. Co-realidad derivada

Una vez fijado un régimen total:

$$
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
\Rightarrow
\Bigl(
\operatorname{CoReal}_i(x_i,y_i)
\Longleftrightarrow
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i)
\land
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,y_i)
\Bigr).
$$

Por tanto SameRegime deja de ser una noción obtenida por conectividad formal. La conectividad es una **hipótesis de reconstrucción** de una unidad de régimen previamente caracterizada; no exige que todos sus contenidos desciendan de un único origen.

Para dominios procesuales, $\operatorname{SameRegime}(X,Y)$ significa que los tokens ontológicos representados por ambos pertenecen a la misma RegimeClosure. Esto sigue sin implicar K3:

$$
\boxed{
\operatorname{SameRegime}(X,Y)
\not\Rightarrow
K3_i(X,Y).
}
$$

La identidad ontológica y la amalgamabilidad semántica continúan separadas.

### 5.3. Ruta A — reconstrucción mediante $\Lambda_*$

La familia pre-régimen:

$$
\Lambda_*
$$

se conserva como implementación candidata, pero ya no define CoReal por decreto.

Sus tipos de enlace deben seguir cumpliendo:

1. actualidad;
2. carácter ontológico;
3. sensibilidad token-specific;
4. rol generativo/integrador;
5. independencia respecto de $R_i$/SameRegime;
6. invariancia bajo recodificación fiel.

La indexación fuerte permite derivar la **soundness** de la conectividad si cada arista está testimoniada por un hecho ontológico real.

Sea:

$$
\mathrm{EdgeTyped}_i:
\quad
q_i\bowtie_i r_i
\Rightarrow
\exists f_i[
\operatorname{RealFact}_i(f_i)
\land
\operatorname{Relatum}_i(q_i,f_i)
\land
\operatorname{Relatum}_i(r_i,f_i)
].
$$

Por cierre de hechos reales:

$$
\operatorname{RealFact}_i(f_i)
\Rightarrow
\operatorname{Real}_i(q_i)
\land
\operatorname{Real}_i(r_i).
$$

Fijado además un seed ya tipado:

$$
\operatorname{Real}_i(q_i),
$$

la incompatibilidad de índice impide que una cadena finita cambie de índice entre aristas. Por inducción sobre la longitud del camino —incluido el caso de longitud cero—:

$$
\boxed{
\operatorname{Real}_i(q_i)
+
\mathrm{EdgeTyped}_i
+
\mathrm{EXT\text{-}01}
\Rightarrow
\forall x_i[
x_i\in[q_i]_{\sim_i}
\Rightarrow
\operatorname{Real}_i(x_i)
]
\Rightarrow
\mathrm{RS}_{\Lambda}^{\mathrm{gen}}.
}
$$

Por tanto, para la Ruta A, **sobreinclusión entre índices deja de ser el problema principal** siempre que la definición de $\Lambda_*$ mantenga $\mathrm{EdgeTyped}_i$.

La deuda fuerte es completeness: compartir índice/origen no implica que exista un camino finito de enlaces locales entre cualesquiera dos contenidos reales.

La componente finita tipada:

$$
T^{\Lambda}_{i,q}
=
[q_i]_{\sim_i}
$$

es adecuada solo si reconstruye exhaustivamente la genealogía:

$$
\mathrm{RS}^{\mathrm{gen}}_{\Lambda,i}:
\quad
x_i\in T^{\Lambda}_{i,q}
\Rightarrow
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i),
$$

y:

$$
\mathrm{RC}^{\mathrm{gen}}_{\Lambda,i}:
\quad
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i)
\Rightarrow
x_i\in T^{\Lambda}_{i,q}.
$$

FID + LA sigue siendo una vía suficiente hacia RC para esta ruta, no una verdad doctrinal general.

### 5.4. Ruta B — clausura generativa generalizada

Si la genealogía no admite reconstrucción por caminos finitos, la clausura candidata:

$$
\mathcal C_*
$$

debe generarse mediante reglas independientes CGI/CMin.

Como $T_q^{\mathcal C}$ es pre-indexado, no se identifica directamente con tokens de $i$. La comparación exige un mapa de realización/denotación:

$$
\eta_i^{\mathcal C}:
T_q^{\mathcal C}
\rightsquigarrow
\{x_i\},
$$

cuya existencia tampoco se presupone.

La soundness exige que todo elemento realizado del carrier corresponda a contenido generado:

$$
\mathrm{CS}^{\mathrm{gen}}_{\mathcal C,i}:
\quad
a\in T_q^{\mathcal C}
\land
\eta_i^{\mathcal C}(a)=x_i
\Rightarrow
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x_i).
$$

La completeness exige cobertura del contenido generado:

$$
\mathrm{CC}^{\mathrm{gen}}_{\mathcal C,i}:
\quad
\operatorname{Generated}^{*}_i(\mathcal O_i,x_i)
\Rightarrow
\exists a\in T_q^{\mathcal C}\;
\eta_i^{\mathcal C}(a)=x_i.
$$

La fidelidad/injectividad necesaria para preservar identidad y estructura pertenece a RA. La Ruta B puede incorporar reglas globales, de límite o transfinitas si se justifican sin usar la clausura final como premisa.

### 5.5. Directedness sigue siendo posterior

Con:

$$
\operatorname{Adm}_i:=\operatorname{StructAdm}_i,
$$

y una vez fijada legítimamente la genealogía del régimen, la unión semántica positiva de dos fragmentos del mismo régimen proporciona una cota común; por tanto se deriva:

$$
\boxed{K3_i.}
$$

Así K3 no individua el régimen: es una propiedad del poset semántico **después** de que REV-07 haya justificado la genealogía.

### 5.6. Scope realization

La realización no reificante de la closure total:

$$
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,-)
$$

puede expresarse pluralmente:

$$
\exists rr_i\;
\forall x[
x\prec rr_i
\Longleftrightarrow
\operatorname{RegimeGenerated}^{*}_i(\mathfrak G_i,x)
].
$$

Esta instancia sigue dependiendo de la lógica plural/scope adoptada. El finding histórico REV-24d permanece aquí: la realización de alcance pertenece a la existencia ontológica de $R_i$, no a su presentación por $S_i$.

### 5.7. Qué sigue abierto

REV-07 permanece **PARTIAL**. La arquitectura elimina ya la agregación arbitraria y la reducción binaria de la generación. Para cerrarlo hay que justificar:

1. caracterizar $\operatorname{OntProd}_i$ independientemente y demostrar GenSound + GenComplete para el inventario de modos causales/constitutivos/dependencia/continuidad;
2. existencia de las least closures locales y de $\operatorname{RegimeClosure}_i$ en el marco fundacional elegido —set, plural, clase o clausura transfinita—;
3. si existen genealogías sin ninguna base ontológica mínima admisible —distinto de carecer meramente de primer instante temporal— y qué implicaría eso para OntOrigin;
4. equivalencia entre configuraciones-originarias distintas que generan la misma clausura sin volver a mera extensionalidad;
5. qué ruta —$\Lambda_*$ finita o $\mathcal C_*$ generalizada— reconstruye adecuadamente RegimeClosure, incluida la producción transversal;
6. qué principio de scope/pluralidad realiza esa closure como $R_i$ sin setificarla;
7. **espacio compartido vs ontogénesis:** descargar existencia/totalización bajo la bifurcación ya fijada: SharedOntSpace preexistente o ContextGenesis fuerte; no se admite ontogénesis débil.
8. **memoization/baking:** justificar qué convierte una historia o estructura compleja en SourceUnit antes de recontextualizarla; formalizar RoleAdequate, MemoState/update/invalidation y el contrato B1–B10 sin promover automáticamente una role-unit a ContextIndividuation.

Una convergencia bien tipada prueba como máximo realizabilidad conjunta, no co-origen:

$$
\operatorname{Integrable}^{\mathsf M}(C_a,C_b)
\Rightarrow
\operatorname{JointRealizable}^{\mathsf M}(C_a,C_b),
\qquad
\operatorname{JointRealizable}^{\mathsf M}(C_a,C_b)
\not\Rightarrow
\operatorname{CommonGround}^{\mathsf M}(C_a,C_b).
$$

CGP **no es derivable**. SharedOntSpace cubre unidad común preexistente. ContextGenesis genuina exige $\operatorname{GenesisConstitutiveUnity}_k$; FaithfulContinuation es relacional y Convergence se separa de TokenMerger/ContextMerger. Ship-of-Theseus deja FC3 PARTIAL: ContinuationProfile no puede elegirse post hoc. La ruta provisional $\operatorname{OntOrigin}_i\Rightarrow\Omega_i\Rightarrow ContinuationProfile$ queda SUPERSEDED como orden de derivación.

REV-07h refina la hipótesis de trivialización de REV-07e separando tres niveles. Primero, una estructura compleja debe satisfacer un contrato source-side de $\operatorname{SourceUnit}^{\mathsf M}_i(u_i;\rho,\upsilon)$; memoization es una vía candidata para obtener esa unidad mediante equivalencia por continuaciones, estado suficiente reentrante y reglas explícitas de update/invalidation. Segundo, baking se generaliza como el juicio metateórico $\operatorname{Bake}^{\mathsf M}_{i\to k}(u_i\Downarrow\sigma_k;\rho,\beta)$, que exige source unit previa, actuality/typing target-side, provenance, factorization, preservation contract y declared kernel. Tercero, GenesisTrivialization pasa a ser la aplicación ontogénica de Bake dentro de ContextGenesis, no la definición de baking en general.

Memoization no es hashing ni un criterio automático de contexto: $\operatorname{MemoIndividuated}\not\Rightarrow\operatorname{ContextIndividuation}$. Una role-unit puede ser un subsistema ordinario de $R_i$. ConservativeBake y QuotientBake se mantienen, pero la no-inyectividad solo es admisible cuando las diferencias colapsadas pertenecen al kernel declarado por $\beta$ y no alteran dependencias target-side del rol. Esta separación permite explicar SignatureConvergence sin confundir colisiones de representación, identidad source-side y trivialización child-side. $\Omega_i$ queda reubicada provisionalmente como posible canonicalización posterior de estructura generativa/memoization módulo trivializaciones admisibles, no como primitivo ni como fundamento retroactivo de IndexAdmission.

**Estado: PARTIAL — REV-07. REV-07f queda resuelto arquitectónicamente por GeneBasis + RegimeClosure + RegimeTotal; REV-07g mantiene abierta la individuación contextual y REV-07h mantiene abierta la descarga formal de memoization/baking. La existencia concreta sigue dependiendo de REV-07b/c, ContextIndividuation admisible y scope realization. REV-24 queda reservado a la presentación semántica de un $R_i$ ya justificado.**

## 6. Metaontología de contextos — REV-26

REV-26 no forma parte de la demostración de $\operatorname{ExistsR}$. Estudia qué afirmaciones puede hacer el metalenguaje acerca de distintas **instanciaciones del esquema indexado**.

### 6.1. Meta-cuantificación

Cuando se escriba:

$$
\exists^{\mathsf M} i\;\Phi_i
$$

o:

$$
\forall^{\mathsf M} i\;\Phi_i,
$$

se trata de abreviaturas metateóricas sobre sustituciones/realizaciones admisibles del parámetro $i$. No existe por ello un sort ontológico de índices ni una entidad que los reúna.

### 6.2. One-$R$

One-$R$ afirma:

1. $\operatorname{ExistsR}$;
2. si el metalenguaje compara dos realizaciones admisibles de RegimeTotal, sus parámetros resultan equivalentes:

$$
i\simeq_{\mathrm{idx}}j.
$$

No exige conectividad causal interna total.

### 6.3. Many-$R$

Many-$R$ afirma que existen metateóricamente dos realizaciones admisibles de RegimeTotal cuyos parámetros satisfacen:

$$
\boxed{
i\mathrel{\#}j.
}
$$

No se añade una segunda condición de aislamiento. $i\#j$ **es** la incompatibilidad de tipos.

Por ello no se escriben, para índices ya genuinos, predicados objeto cross-index. $i\#j$ prohíbe hechos objeto transversales, pero no la relación metateórica ContextGenesis: dos contextos incompatibles pueden ser precursores de $k$ sin que ningún token de $i$ aparezca directamente en fórmulas de $j$ o $k$.

### 6.4. Cluster-$R$

Cluster-$R$ es un diagnóstico anterior a la tipificación definitiva.

Dados candidatos $C_a,C_b$, un common ground independientemente justificado fuerza equivalencia provisional de contexto, mientras una mera integración solo prueba realizabilidad conjunta:

$$
\operatorname{CommonGround}^{\mathsf M}(C_a,C_b)\Rightarrow i\simeq_{\mathrm{idx}}j,
\qquad
\operatorname{Integrable}^{\mathsf M}(C_a,C_b)\lor\operatorname{RelIntegrable}^{\mathsf M}(C_a,C_b)\Rightarrow\operatorname{JointRealizable}^{\mathsf M}(C_a,C_b).
$$

La segunda implicación no decide por sí sola entre **SharedOntSpace** y **ContextGenesis**. En el primer caso la integración revela un espacio común previo; en el segundo constituye $k$ y solo las continuaciones child-side coexisten en su lenguaje objeto. CommonGround es una subposibilidad del primer caso, no el criterio general de unidad.

Una vez justificado:

$$
i\mathrel{\#}j,
$$

un supuesto hecho objeto común refuta la indexación anterior; una ContextGenesis posterior no las «fusiona» cross-index, sino que produce una nueva instanciación $k$ relacionada por $\prec_{\mathrm{ctx}}$.

### 6.5. Metalenguaje no es superrealidad

El metalenguaje puede escribir pares sintácticos:

$$
\langle i,x_i\rangle,
$$

comparar teorías $\mathcal L_i,\mathcal L_j$ o definir traducciones $\tau_{ij}$.

Nada de ello es contenido ontológico de un $R_k$ superior. Es infraestructura formal externa a los lenguajes objeto.

AG, comprensión plural global y NoAbsFinality quedan DEFERRED como cuestiones sobre la fuerza del metalenguaje, no como premisas de $\operatorname{ExistsR}$.

### 6.6. Metaindecidibilidad interna

Para:

$$
i\mathrel{\#}j,
$$

ninguna fórmula bien tipada en $\mathcal L_i$ puede tener como relatum un objeto, hecho o scope de tipo $j$.

Así, si Many-$R$ es verdadero, ningún $R_i$ puede certificar internamente la existencia de un $R_j$ incompatible.

### 6.7. Estado de REV-26

- **REV-26a / AG:** DEFERRED; solo metalenguaje global.
- **REV-26b / comprensión plural global:** DEFERRED.
- **REV-26c / origen común:** test pre-indexado de equivalencia de contextos; no blocker de ExistsR.
- **REV-26d / NoAbsFinality:** DEFERRED y distinto de No-$R$.
- **REV-26e:** RESOLVED — el target es una realización genealógica indexada.

## 7. Arquitectura final de realidad, presentación e índice

### 7.1. Arquitectura ontológica/semántica

Para un parámetro de contexto fijo $i$:

$$
\boxed{
\mathfrak G_i
\xrightarrow{\operatorname{RegimeClosure}_i}
R_i
\xleftarrow{\operatorname{Presents}_i}
S_i.
}
$$

$\mathfrak G_i$ es un parámetro metateórico de base genealógica, no una entidad adicional de $R_i$; para una familia singleton se recupera $\mathcal O_i\xrightarrow{\operatorname{Cl}^{\mathrm{ont}}_i}R_i$. $i$ tampoco es un nodo: es el tipo/contexto en el que el diagrama está escrito.

### 7.2. Existencia como metasentencia

$$
\boxed{
\operatorname{ExistsR}
\Longleftrightarrow
\exists^{\mathsf M} i\;
\bigl(
\exists\mathfrak G_i\exists R_i\;
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
\bigr).
}
$$

Esto basta para negar No-$R$ y no requiere One-$R$.

### 7.3. Presentación testimoniada

Fijada una realización $i$, REV-24 intenta demostrar:

$$
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
+
\operatorname{SemTotal}_i(S_i)
+
\mathrm{OA}_i
+
\mathrm{MC}_i
+
\mathrm{RA}_i
\Rightarrow
\operatorname{Presents}_i(S_i,R_i).
$$

### 7.4. Incompatibilidad ontológica

El juicio:

$$
\boxed{i\mathrel{\#}j}
$$

significa que los dos contextos no admiten un único tipado ontológico común. No significa que exista una relación `#` dentro de alguna realidad.

### 7.5. Consecuencia para nuestro acceso

Toda evidencia, proceso o estructura real accesible está necesariamente tipada dentro de algún contexto $i$.

Desde $R_i$, cualquier supuesto contenido de un contexto incompatible carece de referencia ontológica en $\mathcal L_i$.

Por eso la apariencia metateórica de One-$R$ o Many-$R$ no cambia el hecho operativo fundamental:

$$
\boxed{
\text{acceso, proceso, estructura y evidencia}
\subseteq_i
R_i.
}
$$

### 7.6. Verdad interna

Puede existir una presentación/verdad interna $\operatorname{Truth}_i$. No se proyecta automáticamente a otro contexto ni existe una `Truth_abs` por mera comparación metalingüística.


## 8. K2, localidad, compacidad y colímites

La ruta vigente ya no presenta localidad, compacidad lógica y colímites como «tres pruebas independientes».

Para dominios procesuales de un régimen fijo $i$, se ha demostrado formalmente que `EClosed_i` se preserva bajo uniones de cadenas compatibles. Esto elimina la antigua necesidad de hacer factorizar un testigo finito por algún estadio.

Por tanto:

- **REV-10: RESOLVED** para la ruta vigente; la premisa oculta de StageFactorization ya no se usa.
- **REV-09: PARTIAL**; falta demostrar que la unión/direct limit formal de una cadena de dominios procesuales admisibles sigue siendo un dominio ontológicamente admisible de $i$.

La compacidad lógica y la maquinaria categórica pueden seguir siendo herramientas futuras para justificar esa admisibilidad, pero no cuentan como resultados ontológicos por sí mismas.


## 9. Proceso, admisibilidad y extensiones diferidas

REV-19 permanece **RESOLVED en tipado y orden** y REV-18 queda **RESOLVED en el puente semántico mínimo**.

El objeto primario es:

$$
X=(T_X,\Phi_X),
$$

con orden:

$$
X\preceq_iY
\iff
T_X\subseteq T_Y
\land
\Phi_X\subseteq\Phi_Y.
$$

La admisibilidad vigente es StructAdm: fragmento positivo, actual, homogéneo de régimen y well-formed.

Con esta elección, REV-09 queda RESOLVED para cadenas set-indexed y K3$_i$ deja de requerir OAM como premisa: la unión de dos dominios del mismo régimen ya proporciona una cota común admisible.

Siguen fuera del núcleo demostrado:

- una teoría temporal concreta;
- branching como tesis física universal;
- meta-capacidades;
- AbsoluteBruteNovelty;
- fractalidad.

«Fractal» no participa en ninguna inferencia vigente.


## 10. REC, Muro y el estatuto de la demostración

REC y el Muro deben mantenerse separados porque tienen **estatus y dirección lógica distintos**.

### 10.1. REC — consecuencia estructural de una totalidad real

$\operatorname{REC}_i(R_i)$ (R Enigmatic Certification) no se adopta como premisa para demostrar que $R_i$ existe. Se atribuye solo después de justificar una realización total de régimen:

$$
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i).
$$

La abreviatura estrictamente tipada es:

$$
\operatorname{REC}_i(R_i)
:=
\neg\exists x_i[
\operatorname{Real}_i(x_i)
\land
\operatorname{OutsideOntScope}_i(x_i,R_i)
\land
\operatorname{CertifiesTotality}_i(x_i,R_i)
].
$$

Por tanto:

$$
\boxed{
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)
\Rightarrow
\operatorname{REC}_i(R_i).
}
$$

La razón es estructural: si existiera un certificador **real y ontológicamente exterior** al alcance exhaustivo atribuido a $R_i$, ese mismo testigo mostraría que el candidato no era ontológicamente total.

Así, para cualquier candidato $C$:

$$
\boxed{
\operatorname{ExternalRealCertification}_i(C)
\Rightarrow
\neg\operatorname{OntTotal}_i(C).
}
$$

Una certificación externa exitosa no certifica que $C$ sea $R_i$: descarta esa identificación y amplía el alcance ontológico relevante.

REC no significa que $R_i$ sea incognoscible, indescriptible o indemostrable por cualquier vía. Excluye específicamente un **punto de certificación real situado ontológicamente fuera de una totalidad genuina**.

Por ello REC solo se atribuye propiamente después de disponer de $\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)$. GeneTotal hereda REC como caso singleton. No se atribuye por mera clausura a $U_i$ ni a un máximo semántico $S_i$.

### 10.2. Muro — subdeterminación desde un horizonte o candidato

El Muro es una restricción epistemológica distinta. Su forma mínima dice que la ausencia de una extensión accesible no certifica exhaustividad ontológica:

$$
\boxed{
\operatorname{NoAccessibleExtension}_i(U_i)
\not\Rightarrow
\operatorname{ExhaustsOntScope}_i(U_i).
}
$$

Y, en el nivel semántico:

$$
\boxed{
\operatorname{SemTotal}_i(S_i)
\not\Rightarrow
\exists\mathfrak G_i\exists R_i\;
\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i).
}
$$

Y, aun suponiendo una genealogía ontológica ya justificada:

$$
\operatorname{SemTotal}_i(S_i)
\not\Rightarrow
\operatorname{Presents}_i(S_i,R_i).
$$

Una sandbox o cuasisingularidad puede por tanto **imitar epistemológicamente** el comportamiento que un observador esperaría de REC —no aparece ningún certificador exterior accesible— sin poseer REC en sentido ontológico. Si realmente existe un exterior, el dominio era parcial aunque ese exterior fuese inaccesible desde dentro.

La asimetría queda resumida así:

$$
\boxed{
\begin{array}{rcl}
\text{exterior real que certifica un candidato}
&\Rightarrow&
\text{el candidato no era ontológicamente total}
\\
\text{ningún exterior accesible}
&\not\Rightarrow&
\text{el candidato es ontológicamente total}.
\end{array}
}
$$

La primera línea es la consecuencia estructural asociada a REC. La segunda es el Muro.

La versión fuerte del Muro —que ninguna evidencia puramente interna pueda **jamás** discriminar la metaontología última— no se da por demostrada y permanece dentro de REV-15. La trivialización ontogénica no-inyectiva aporta ahora un **mecanismo candidato** de subdeterminación genealógica: provenance objetiva puede no ser reconstruible desde el hijo si el quotient eliminó la distinción y no sobrevive un certificado child-side; esto no identifica Muro con REC ni demuestra todavía la versión fuerte.

### 10.3. Estatuto del teorema semántico

La distinción normativa correcta sigue siendo:

$$
\boxed{
\text{existencia condicional de un máximo semántico }S_i
\neq
\text{certificación ontológica de }R_i.
}
$$

Si para algún régimen $i$ se justifican K1$_i$, K2$_i$ y K3$_i$, el teorema puede demostrar que existe un máximo E-closed $S_i$ aunque ningún observador interno pueda identificarlo empíricamente.

Por tanto, el Muro no bloquea el paso formal:

$$
K1_i+K2_i+K3_i
\Rightarrow
\exists S_i\;\operatorname{SemTotal}_i(S_i).
$$

Pero ese paso **no es**:

$$
K1_i+K2_i+K3_i
\Rightarrow
\exists R_i.
$$

La existencia de $R_i$ requiere una genealogía de REV-07. REV-24/$\mathrm{OTB}_i$ entra solo después para justificar que $S_i$ presenta ese $R_i$.

### Acceso causal y reconstruibilidad

El Muro tampoco debe identificar «causalmente accesible» con «representable/reconstruible». En AdS/CFT, Dong–Harlow–Wall demuestran reconstrucción de operadores del bulk en el entanglement wedge, que puede extenderse más allá de la causal wedge. Almheiri–Dong–Harlow relacionan esta redundancia reconstructiva con quantum error correction.

Esto proporciona un precedente físico concreto para admitir, en modelos donde esas hipótesis aplican:

$$
\operatorname{Reconstructible}_i(x)
\land
\neg\operatorname{DirectCausalAccess}_i(x).
$$

La propuesta **no universaliza** este resultado a toda ontología ni lo usa para probar el Muro. Solo muestra que acceso causal directo y alcance representacional son nociones físicamente separables; por tanto, la ausencia de acceso causal adicional no certifica el alcance de $R_i$. Véase el [mapa de literatura, §13](autodescripcion-realidad-distincion-references.md#13-horizontes-observables-gravitatorios-y-reconstrucción-holográfica).

### Restricción epistemológica sobre K1

K1$_i$ cuantifica sobre todos los dominios admisibles del régimen:

$$
\forall X\in\mathfrak D_i^{\mathrm{proc}}
\;\exists Y\in\mathfrak K_i:
X\preceq_i Y.
$$

Un observador interno no puede establecer esta universalidad inspeccionando una muestra finita o creciente de dominios. Por ello:

$$
\boxed{
\text{evidencia por muestreo}
\not\Rightarrow
K1_i.
}
$$

El criterio de cierre de REV-20 exige una justificación **estructural y no enumerativa**. La evidencia empírica puede motivar o apoyar sus premisas, pero no sustituir la cuantificación universal requerida.

### Alcance del Muro

El Muro deja abiertas simultáneamente estas posibilidades:

- existe un máximo semántico $S_i$ pero no puede identificarse desde dentro;
- una cuasisingularidad es indistinguible localmente de $S_i$;
- existe o no existe una base genealógica total $\operatorname{RegimeTotal}_i(\mathfrak G_i,R_i)$ y, si existe, $S_i$ la presenta o no adecuadamente;
- existen otras genealogías $R_j$ si REV-07 las justifica, con independencia de que sus presentaciones semánticas cierren REV-24;
- existe o no existe un $R_{\mathrm{abs}}$.

Nada de ello resta valor lógico a una demostración condicional de $\exists S_i\;\operatorname{SemTotal}_i(S_i)$. Tampoco sustituye la justificación genealógica de REV-07 ni la adecuación representacional de REV-24.

**Estado:** REC queda clasificado como consecuencia estructural condicionada a una totalidad indexada ya establecida, en línea con REV-06. REV-15 permanece OPEN para las consecuencias discriminantes y para cualquier versión fuerte del Muro. El Muro se conserva como límite epistemológico, no como puente hacia `ExistsR` ni como evidencia de One-$R$/Many-$R`.

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

- Muro: **DEFERRED** históricamente como epistemología. **Corrección normativa posterior (§10):** REC no es otra versión del Muro; queda reclasificado como consecuencia estructural condicionada a `OntTotal`.
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
