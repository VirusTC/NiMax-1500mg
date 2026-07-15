# NiMax-1500mg: Specialized Expanded Access Compliance Framework

[![License: BSL-1.0](https://shields.io)](LICENSE)
[![Language: Python](https://shields.io)](src/)

This repository serves as the definitive administrative, toxicological, and operational source for the **NiMax-1500mg** Investigational Review Board (IRB) Expanded Access (Compassionate Use) program. The target formulation is a specialized, 100% active, pure botanical matrix utilizing certified organic *Azadirachta indica* (Neem) bound with Gum Acacia and stabilized with isolated Azadirachtin D.

## 🔬 Formulation Architecture
Unlike conventional tablets that rely on synthetic bulking agents, the NiMax matrix utilizes raw plant fractions as both the Active Pharmaceutical Ingredient (API) and the primary filler:
*   **Active Core:** Standardized Organic *Azadirachta indica* Extract / Powder.
*   **Polymeric Binder:** 5.0% w/w Certified Organic Gum Acacia (Gum Arabic).
*   **Target Compounds:** Azadirachtin A & Azadirachtin D (Stabilized via strict processing moisture limits, $\text{LOD} < 2.0\%$, to prevent hydrolytic ester cleavage).
*   **Exclusions:** Trace congener Azadirachtin M has been intentionally omitted from tracking due to agricultural volatility and unnecessary FDA Chemistry, Manufacturing, and Controls (CMC) regulatory burdens.

---

## 🛑 Strict Clinical & Temporal Stop-Gates

Because of the potential for lipophilic tissue saturation and hepatocyte stress, this protocol enforces absolute safety boundaries:
1.  **Daily Max Ceiling:** One (1) core tablet orally every 12 hours ($q12h$). Absolute max of two (2) tablets per 24-hour cycle (2500mg/day total exposure).
2.  **3-Week Limit:** Administration is locked to an absolute protocol ceiling of twenty-one (21) consecutive days. 
3.  **Mandatory Washout:** On Day 21, the patient enters a mandatory 14-day zero-drug clearance loop to restore hepatic glutathione (GSH) reserves.
4.  **Day 14 Stop-Gate:** If the mandatory mid-cycle laboratory audit displays a Transaminase spike ($\text{ALT/AST} > 1.5\times$ baseline), dosing is revoked instantly.

---

## 🚽 Public Health & Environmental Containment

To prevent persistent active botanical residues and parasitic vectors from entering public wastewater systems, a strict dual-action containment method is enforced:
*   **Alkaline Hydrolysis:** A continuous-release Sodium Hypochlorite ($\text{NaOCl}$ / Bleach) puck is installed in the upper toilet flush tank to chemically cleave the active limonoid ring scaffolds before waste exits the building grid.
*   **Non-Handling Feedback Loop:** On Washout Days 22, 23, and 24, patients deploy surface-floating tetramethylbenzidine (TMB) colorimetric test strips. A vibrant cyan-blue change indicates remaining biological shedding, forcing execution of the `CONTINGENCY_DOSING_AND_RE-TREATMENT` track.

---

## 📂 Repository File Structure

├── data/\
│ └── PATIENT_MASTER_COMPLIANCE_LOG.tsv # Real-time tabular clinical audit tracking\
├── docs/\
│ ├── CHRONIC_TOXICITY_AND_TERMINATION_PROTOCOL.md # Long-term safety stop-gates\
│ ├── IRB_EXPANDED_ACCESS_PROTOCOL.md # Clinical dosing architecture\
│ ├── PATIENT_INFORMED_CONSENT_EXPANDED_ACCESS.md # Patient legal sign-off file\
│ ├── POST_CYCLE_SANITATION_AND_RETESTING.md # Toilet bleach puck & dye workflows\
│ └── TOXICOLOGY_AND_DOSAGE_SAFETY.md # Equations and Bateman PK models\
├── forms/\
│ ├── CONTINGENCY_DOSING_AND_RE-TREATMENT.md # Day 24 alternative path logic\
│ ├── DAY_14_CLINICAL_MONITORING_CRITERIA.md # Mid-cycle CMP checklist\
│ ├── FDA_EXPANDED_ACCESS_AUDIT_LEDGER.tsv # 21 CFR § 312.315 retention ledger\
│ ├── FORM_FDA_3500A_MANDATORY_MEDWATCH.tsv # SAE MedWatch data-mapping\
│ ├── FORM_FDA_3926_INDIVIDUAL_EXPANDED_ACCESS.md # Individual compassionate use template\
│ └── INSURANCE_BILLING_AND_HCPCS_CODES.tsv # CPT and J-code financial data\
├── images/ # Script-generated analytics folder\
└── src/\
├── compliance_audit_engine.py # Automatic TSV parsing safety engine\
└── toxicology_plots.py # PK, Hill, and Arrhenius graph engines


---

## ⚙️ Core Mathematical Frameworks Deployed

### 1. Human Equivalent Dose (HED) Normalization
$$\text{HED} = \text{NOAEL}_{\text{animal}} \times \left( \frac{K_{m, \text{animal}}}{K_{m, \text{human}}} \right)$$

### 2. Pharmacokinetic Bateman Open Oral Model
$$\frac{dC}{dt} = \frac{F \cdot D \cdot k_a}{V_d} \cdot e^{-k_a \cdot t} - k_e \cdot C$$

### 3. Proton Motive Force Collapse (Mitochondrial Uncoupling at Overdose)
$$\Delta p = \Delta \Psi - \frac{2.303 \cdot R \cdot T}{F} \Delta \text{pH}$$

---

## 🛠️ Automated Python Verification
To run the automated compliance data audit engine and verify if data entries inside the `.tsv` ledgers match the mandatory IRB safety thresholds, execute:

```bash
python src/compliance_audit_engine.py
```

***

### 📋 Medical & Legal Disclaimer
The documentation, ledgers, and structural models maintained in this repository describe theoretical chemical, pharmacokinetic, and administrative parameters for software validation and compliance design. They do not constitute personalized medical advice, formal legal counsel, or official healthcare diagnostics. Any live implementation of individual expanded access frameworks must be formally reviewed, approved, and tracked by licensed institutional review boards (IRBs) and federal health authorities.
