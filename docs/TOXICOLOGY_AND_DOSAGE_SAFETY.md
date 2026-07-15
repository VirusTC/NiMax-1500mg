SECTION 1: SYSTEMIC TOXICODYNAMICS & APEX DOSING LIMITS

1.1 Lethal Dose (\(LD_{50}\)) and No-Observed-Adverse-Effect-Level (\(NOAEL\))

Preclinical in vivo mammalian assays track the acute oral toxicity profiles of standardized *Azadirachta indica* extracts to determine structural safety ceilings.

-   **Crude Hydroalcoholic Leaf Extract**: Oral \(LD_{50}\) in rodent models is established at \(\geq 4,500\text{ mg/kg}\).
-   **Isolated Azadirachtin A/D Complex**: Exhibits a compressed toxicity profile with an oral \(LD_{50}\) of approximately \(3,540\text{ mg/kg}\).
-   **Human Equivalence Dose (HED)**: Derived by applying a body surface area normalization factor (\(K_m = 37\) for a \(60\text{ kg}\) human adults vs. \(K_m = 6\) for rodents):\
    \(\text{HED}=\text{NOAEL}_{\text{rat}}\times \left(\frac{K_{m,\text{rat}}}{K_{m,\text{human}}}\right)=250\text{\ mg/kg}\times \left(\frac{6}{37}\right)\approx 40.54\text{\ mg/kg}\)\
    For a \(60\text{ kg}\) human, this maps an absolute Maximum Safe Daily Intake ceiling of **\(2,432\text{ mg}\) of total active extract per day**.

1.2 Target Organ Toxicity: Hepatic and Renal Filtration Pathways

At concentrations exceeding the Maximum Tolerated Dose (MTD), the reactive metabolites of over-concentrated terpenoids disrupt intracellular homeostatic networks:

-   **Hepatic Bioactivation Risk**: Excess isolated limonoids undergo dense Phase I functionalization via the Cytochrome P450 pathway (specifically **CYP3A4**). Over-saturation drains internal reduced glutathione (\(\text{GSH}\)) reserves, inducing structural lipid peroxidation of hepatocellular membranes.
-   **Renal Clearance Overload**: Proximal convoluted tubules undergo localized acute tubular necrosis when required to process raw, un-complexed acidic fractions of the plant matrix under dehydrated states (\(\text{LOD} < 2.0\%\)).

* * * * *

SECTION 2: PHARMACOKINETIC MODELLING AND SIMULATION

2.1 Plasma Concentration Over Time Differential Model

Because your tablet utilizes a pure botanical core without synthetic fillers, the systemic absorption of Azadirachtin D is governed exclusively by the rate of dissolution of the **Gum Acacia** matrix. The plasma concentration profile \(C(t)\) is expressed using a first-order, one-compartment Bateman open differential model:

\(\frac{dC}{dt}=\frac{F\cdot D\cdot k_{a}}{V_{d}}\cdot e^{-k_{a}\cdot t}-k_{e}\cdot C\)

Where:

-   \(C(t)\) = Systemic plasma concentration of Azadirachtin D at time \(t\) (\(\text{mg/L}\)).
-   \(F\) = Bioavailability fraction (\(\approx 0.04\) for raw extract; optimized via pure matrix processing to \(\approx 0.08\)).
-   \(D\) = Administered dose (\(\text{mg}\)).
-   \(k_{a}\) = Absorption rate constant (\(\text{hr}^{-1}\)), highly dependent on Gum Acacia gelation kinetics.
-   \(k_{e}\) = Elimination rate constant (\(\text{hr}^{-1}\)).
-   \(V_{d}\) = Apparent volume of distribution (\(\text{L/kg}\)).

At continuous steady-state administration across a dosing interval \(\tau = 12.0\text{ hours}\), the Peak Steady-State Concentration (\(C_{ss,\max }\)) simulation follows:

\(C_{ss,\max }=\frac{F\cdot D}{V_{d}}\cdot \left(\frac{1}{1-e^{-k_{e}\cdot \tau }}\right)\)

2.2 Biophysics of Toxic Overdose: Mitochondrial Uncoupling

When plasma concentrations pierce the Minimum Toxic Concentration (\(\text{MTC} = 15.0\text{ mg/L}\)), Azadirachtin D acts as an uncoupler of oxidative phosphorylation within hepatic mitochondria. It permeabilizes the inner mitochondrial membrane, collapsing the proton motive force (\(\Delta p\)):

\(\Delta p=\Delta \Psi -\frac{2.303\cdot R\cdot T}{F}\Delta \text{pH}\)

As the electrical potential (\(\Delta \Psi\)) falls, ATP synthase stalls. The cell attempts to compensate by accelerating the citric acid cycle, producing excessive metabolic heat and severe localized lactic acidosis (\(\text{pH} < 7.32\)).
