from rdkit import Chem
from rdkit.Chem import AllChem

def print_conformer_coordinates(mol, conf_id):
    """Prints the atomic coordinates of a single conformer of a molecule"""
    conf = mol.GetConformer(conf_id)
    for i, atom in enumerate(mol.GetAtoms()):
        pos = conf.GetAtomPosition(i)
        #print("pos.x:", pos.x)
        print(f'{atom.GetSymbol()}{i+1}: ({pos.x:.4f},' 
              f' {pos.y:.4f}, {pos.z:.4f})')

def print_molecule_conformers(mol, num_confs=1):
    """Prints the atomic coordinates of all conformers of a molecule"""
    for i in range(mol.GetNumConformers()):
        print(f'Conformer {i+1}:')
        print_conformer_coordinates(mol, i)

# Create the ethanol molecule
ethanol = Chem.MolFromSmiles('CCO')
ethanol = Chem.AddHs(ethanol)
AllChem.EmbedMultipleConfs(ethanol, 3)

# Print the atomic coordinates of 3 conformations of ethanol
print_molecule_conformers(ethanol)
print(f"\nConformer 0")
print_conformer_coordinates(ethanol, 0)