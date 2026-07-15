import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------
# PLOT 1: PHARMACOKINETIC PROFILE & TOXICITY THRESHOLD
# ----------------------------------------------------
t = np.linspace(0, 48, 1000)

# Parameter definitions for Bateman Open One-Compartment Model
F = 0.08         # Optimized Bioavailability
Vd = 1.4         # Volume of distribution (L/kg)
Dose = 500       # Dose in mg
ka = 0.35        # Absorption rate constant (influenced by Gum Acacia)
ke = 0.12        # Elimination rate constant

# Single Dose Curve Calculation
C_single = (F * Dose * ka) / (Vd * (ka - ke)) * (np.exp(-ke * t) - np.exp(-ka * t))

# Multiple Dose Dosing Simulation (Every 12 Hours)
C_multi = np.zeros_like(t)
for dose_time in:
    mask = t >= dose_time
    t_dose = t[mask] - dose_time
    C_multi[mask] += (F * Dose * ka) / (Vd * (ka - ke)) * (np.exp(-ke * t_dose) - np.exp(-ka * t_dose))

fig, ax1 = plt.subplots(figsize=(10, 5))
ax1.plot(t, C_multi, color='#008080', linewidth=2.5, label='Azadirachtin D Plasma Concentration')
ax1.axhline(y=15.0, color='#D32F2F', linestyle='--', linewidth=1.5, label='Minimum Toxic Concentration (MTC)')
ax1.axhline(y=1.5, color='#388E3C', linestyle=':', linewidth=1.5, label='Minimum Effective Concentration (MEC)')
ax1.set_title('Azadirachtin D Pharmacokinetic Simulation: Pure Matrix Tablet', fontsize=12, fontweight='bold', pad=15)
ax1.set_xlabel('Time Post-Administration (Hours)', fontsize=10)
ax1.set_ylabel('Plasma Concentration (mg/L)', fontsize=10)
ax1.set_xlim(0, 48)
ax1.set_ylim(0, 18)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='upper right', frameon=True, facecolor='#FFFFFF', edgecolor='#E0E0E0')
plt.tight_layout()
plt.savefig('images/pharmacokinetic_toxicity_profile.png', dpi=300)
plt.close()

# ----------------------------------------------------
# PLOT 2: DOSE-RESPONSE CURVE (HILL EQUATION MODEL)
# ----------------------------------------------------
dose_range = np.logspace(0, 4, 1000)
ED50 = 250   # Effective Dose 50% (mg)
TD50 = 2500  # Toxic Dose 50% (mg)
n = 2.2      # Hill Coefficient (Sigmoid Steepness)

# Hill Equation Calculation: E = Dose^n / (ED50^n + Dose^n)
efficacy = (dose_range**n) / (ED50**n + dose_range**n) * 100
toxicity = (dose_range**n) / (TD50**n + dose_range**n) * 100

plt.figure(figsize=(10, 5))
plt.semilogx(dose_range, efficacy, color='#2E7D32', linewidth=2.5, label='Therapeutic Efficacy (%)')
plt.semilogx(dose_range, toxicity, color='#C62828', linewidth=2.5, label='Systemic Hepatotoxicity Risk (%)')
plt.axvline(x=500, color='#1565C0', linestyle='--', label='Target Formulated Tablet Dose (500mg)')
plt.title('Azadirachta indica Therapeutic Index & Safety Margin Model', fontsize=12, fontweight='bold', pad=15)
plt.get_current_fig_manager()
plt.xlabel('Log Dose Concentration (mg)', fontsize=10)
plt.ylabel('Mathematical Probability Response (%)', fontsize=10)
plt.grid(True, which="both", linestyle=':', alpha=0.5)
plt.legend(loc='lower right', frameon=True, facecolor='#FFFFFF', edgecolor='#E0E0E0')
plt.tight_layout()
plt.savefig('images/dose_response_hill_model.png', dpi=300)
plt.close()
