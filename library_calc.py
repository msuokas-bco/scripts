#!/usr/bin/env python3

import locale

# Set locale for number formatting
locale.setlocale(locale.LC_ALL, '')

def dna_molarity(dna_length, concentration_ng_per_ul):
    """Calculate DNA molarity in pM/µl and nM/µl given DNA length and concentration (ng/µl)."""
    if dna_length <= 0 or concentration_ng_per_ul <= 0:
        return "Invalid input: DNA length and concentration must be positive numbers."
    
    try:
        # Calculate molarity in pM/µl
        molarity_pM_ul = (concentration_ng_per_ul * 1e6) / (660 * dna_length)
        
        # Convert to nM/µl
        molarity_nM_ul = molarity_pM_ul / 1000  # 1 nM = 1000 pM
        
        return f"Molarity: {locale.format_string('%.2f', molarity_pM_ul)} pM/µl or {locale.format_string('%.3f', molarity_nM_ul)} nM/µl"
    except Exception as e:
        return f"Error in calculation: {e}"

# Prompt user for input
try:
    dna_length = float(input("Enter DNA size in bp: "))
    concentration_ng_ul = float(input("Enter DNA concentration in ng/µl: "))
    
    # Calculate and display molarity
    print(dna_molarity(dna_length, concentration_ng_ul))
except ValueError:
    print("Invalid input: Please enter numeric values.")

