print("\n========== FEATURE DESCRIPTIONS ==========\n")

feature_info = {
    'class': ('Target Class', {'e': 'Edible', 'p': 'Poisonous'}),
    'cap-shape': ('Shape of mushroom cap', {
        'b': 'Bell', 'c': 'Conical', 'x': 'Convex', 'f': 'Flat',
        'k': 'Knobbed', 's': 'Sunken'
    }),
    'cap-surface': ('Surface texture of cap', {
        'f': 'Fibrous', 'g': 'Grooves', 'y': 'Scaly', 's': 'Smooth'
    }),
    'cap-color': ('Color of cap', {
        'n': 'Brown', 'b': 'Buff', 'c': 'Cinnamon', 'g': 'Gray',
        'r': 'Green', 'p': 'Pink', 'u': 'Purple', 'e': 'Red',
        'w': 'White', 'y': 'Yellow'
    }),
    'bruises': ('Bruises on cap', {'t': 'Yes', 'f': 'No'}),
    'odor': ('Odor of mushroom', {
        'a': 'Almond', 'l': 'Anise', 'c': 'Creosote', 'y': 'Fishy',
        'f': 'Foul', 'm': 'Musty', 'n': 'None', 'p': 'Pungent', 's': 'Spicy'
    }),
    'gill-attachment': ('Gill attachment to stalk', {'a': 'Attached', 'f': 'Free'}),
    'gill-spacing': ('Spacing between gills', {'c': 'Close', 'w': 'Crowded', 'd': 'Distant'}),
    'gill-size': ('Size of gills', {'b': 'Broad', 'n': 'Narrow'}),
    'gill-color': ('Color of gills', {
        'k': 'Black', 'n': 'Brown', 'b': 'Buff', 'h': 'Chocolate',
        'g': 'Gray', 'r': 'Green', 'o': 'Orange', 'p': 'Pink',
        'u': 'Purple', 'e': 'Red', 'w': 'White', 'y': 'Yellow'
    }),
    'stalk-shape': ('Shape of stalk', {'e': 'Enlarging', 't': 'Tapering'}),
    'stalk-root': ('Root type of stalk', {
        'b': 'Bulbous', 'c': 'Club', 'u': 'Cup', 'e': 'Equal',
        'z': 'Rhizomorphs', 'r': 'Rooted', '?': 'Missing'
    }),
    'stalk-surface-above-ring': ('Stalk surface above ring', {
        'f': 'Fibrous', 'y': 'Scaly', 'k': 'Silky', 's': 'Smooth'
    }),
    'stalk-surface-below-ring': ('Stalk surface below ring', {
        'f': 'Fibrous', 'y': 'Scaly', 'k': 'Silky', 's': 'Smooth'
    }),
    'stalk-color-above-ring': ('Stalk color above ring', {
        'n': 'Brown', 'b': 'Buff', 'c': 'Cinnamon', 'g': 'Gray',
        'o': 'Orange', 'p': 'Pink', 'e': 'Red', 'w': 'White', 'y': 'Yellow'
    }),
    'stalk-color-below-ring': ('Stalk color below ring', {
        'n': 'Brown', 'b': 'Buff', 'c': 'Cinnamon', 'g': 'Gray',
        'o': 'Orange', 'p': 'Pink', 'e': 'Red', 'w': 'White', 'y': 'Yellow'
    }),
    'veil-type': ('Type of veil', {'p': 'Partial', 'u': 'Universal'}),
    'veil-color': ('Color of veil', {'n': 'Brown', 'o': 'Orange', 'w': 'White', 'y': 'Yellow'}),
    'ring-number': ('Number of rings', {'n': 'None', 'o': 'One', 't': 'Two'}),
    'ring-type': ('Type of ring', {
        'c': 'Cobwebby', 'e': 'Evanescent', 'f': 'Flaring',
        'l': 'Large', 'n': 'None', 'p': 'Pendant', 's': 'Sheathing', 'z': 'Zone'
    }),
    'spore-print-color': ('Color of spore print', {
        'k': 'Black', 'n': 'Brown', 'b': 'Buff', 'h': 'Chocolate',
        'r': 'Green', 'o': 'Orange', 'u': 'Purple', 'w': 'White', 'y': 'Yellow'
    }),
    'population': ('Population distribution', {
        'a': 'Abundant', 'c': 'Clustered', 'n': 'Numerous',
        's': 'Scattered', 'v': 'Several', 'y': 'Solitary'
    }),
    'habitat': ('Natural habitat', {
        'g': 'Grasses', 'l': 'Leaves', 'm': 'Meadows', 'p': 'Paths',
        'u': 'Urban', 'w': 'Waste', 'd': 'Woods'
    })
}

for feature, (desc, values) in feature_info.items():
    print(f"\nFeature: {feature}")
    print("Description:", desc)
    print("Possible Values:")
    for k, v in values.items():
        print(f"  {k} = {v}")

print("\n==========================================\n")
