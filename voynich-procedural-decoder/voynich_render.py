import argparse
import matplotlib.pyplot as plt
import numpy as np
import sys

def parse_eva_tokens(text):
    """
    Cleans and tokenizes EVA text, removing non-alphanumeric noise.
    """
    # Simple whitespace tokenization; strip potential punctuation
    tokens = text.replace('-', ' ').replace('.', ' ').split()
    return [t.lower() for t in tokens if t.isalnum()]

def render_polar_plot(tokens, output_file="voynich_spiral.png"):
    """
    Interprets Voynich tokens as polar coordinates (r, theta) rather than words.
    Hypothesis: 
      - Prefix '4' (q) = Rotate (Step Angle)
      - Suffix '89' = Outer Radius
      - Suffix '9' = Inner Radius
    """
    
    # Coordinates
    r_values = []
    theta_values = []
    colors = []
    sizes = []
    
    current_angle = 0
    # 15 degrees assumes a 24-sector circle (common in Voynich diagrams)
    ANGLE_STEP = 15  
    
    print(f"[*] Processing {len(tokens)} tokens...")

    for token in tokens:
        r = 0
        color = 'gray'
        size = 10
        
        # --- RULE SET: THE PHYSICS HYPOTHESIS ---
        
        # Rule 1: Rotation Command
        # The prefix '4' (q) appears to be a "Next Step" or "Delta" command.
        if token.startswith('4'):
            current_angle += ANGLE_STEP
            color = 'blue' # Mark the instruction point
        
        # Rule 2: Radius Magnitude
        # '89' appears frequently in outer rings
        if '89' in token:
            r = 89
            size = 50
            color = '#8B0000'  # Dark Red (Outer)
        # '9' (without 8) appears in inner rings
        elif '9' in token and '8' not in token:
            r = 30
            size = 30
            color = '#228B22' # Forest Green (Inner)
        # '8' (without 9) appears in middle rings
        elif '8' in token and '9' not in token:
            r = 60
            size = 20
            color = '#DAA520' # Goldenrod (Middle)
            
        # Only plot points that have a valid coordinate geometry
        if r > 0:
            # Convert degrees to radians for matplotlib
            theta_rad = np.radians(current_angle)
            r_values.append(r)
            theta_values.append(theta_rad)
            colors.append(color)
            sizes.append(size)

    # --- PLOTTING ---
    print(f"[*] Generated {len(r_values)} coordinate points.")
    
    plt.figure(figsize=(10, 10), facecolor='white')
    ax = plt.subplot(111, projection='polar')
    
    # Plot the scatter
    ax.scatter(theta_values, r_values, c=colors, s=sizes, alpha=0.75, edgecolors='none')
    
    # Aesthetic adjustments to match manuscript style
    ax.set_ylim(0, 100)
    ax.set_yticklabels([]) # Hide radial degree numbers
    ax.set_xticklabels([]) # Hide angular degree numbers
    ax.grid(True, linestyle='--', alpha=0.3, color='gray')
    
    plt.title(f"Procedural Rendering of Voynich Text\n({len(tokens)} Instructions Processed)", pad=20)
    
    # Save output
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"[+] Render saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render Voynich EVA text as procedural geometry.")
    parser.add_argument("file", help="Path to the EVA text file (.txt)")
    parser.add_argument("--out", default="voynich_spiral.png", help="Output image path")
    
    args = parser.parse_args()
    
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tokens = parse_eva_tokens(content)
        render_polar_plot(tokens, args.out)
        
    except FileNotFoundError:
        print(f"Error: Could not find file {args.file}")
