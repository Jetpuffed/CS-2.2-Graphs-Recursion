from final import a_star


# Website used for locations: https://lowlidev.com.au/destiny/maps/earth
# All locations used are part of the Destiny franchise, owned by Bungie, Inc.

EDZ = {
    "Trostland":
    [
        ("Salt Mines", 1),
        ("Maevic Square", 2),
        ("Outskirts", 3),
        ("The Reservoir", 4),
    ],
    "Salt Mines":
    [
        ("Trostland", 1),
    ],
    "Maevic Square":
    [
        ("Trostland", 1),
        ("The Reservoir", 2),
    ],
    "Outskirts":
    [
        ("Sojourner's Camp", 1),
        ("Trostland", 2),
        ("Winding Cove", 3),
        ("The Sludge", 4),
    ],
    "Sojourner's Camp":
    [
        ("Outskirts", 1),
    ],
    "Winding Cove":
    [
        ("Firebase Hades", 1),
        ("Outskirts", 2),
    ],
    "The Sludge":
    [
        ("The Gulch", 1),
        ("Outskirts", 2),
        ("The Dark Forest", 3),
    ],
    "Firebase Hades":
    [
        ("Legion's Anchor", 1),
        ("Winding Cove", 2),
        ("The Gulch", 3),
    ],
    "The Gulch":
    [
        ("The Tunnels", 1),
        ("The Sludge", 2),
        ("Firebase Hades", 3),
    ],
    "The Dark Forest":
    [
        ("The Sludge", 1),
    ],
    "Legion's Anchor":
    [
        ("Firebase Hades", 1),
        ("Sunken Isles", 2),
    ],
    "The Tunnels":
    [
        ("The Gulch", 1),
        ("Sunken Isles", 1),
    ],
    "Sunken Isles":
    [
        ("Echion Hold", 1),
        ("The Tunnels", 2),
        ("Legion's Anchor", 3),
    ],
    "Echion Hold":
    [
        ("Sunken Isles", 1),
        ("Echion Battledeck", 2),
        ("Echion Control", 3),
    ],
    "Echion Battledeck":
    [
        ("Echion Hold", 1),
        ("Echion Control", 2),
    ],
    "Echion Control":
    [
        ("Echion Battledeck", 1),
        ("Echion Hold", 2),
    ]
}


def test_a_star():
    result_one = a_star(EDZ, "Trostland", "Firebase Hades")
    result_two = a_star(EDZ, "Winding Cove", "Sunken Isles")
    result_three = a_star(EDZ, "Echion Control", "The Reservoir")

    assert result_one == ['Trostland', 'Outskirts', 'Winding Cove', 'Firebase Hades']
    assert result_two == ['Winding Cove', 'Firebase Hades', "Legion's Anchor", 'Sunken Isles']
    assert result_three == ['Echion Control', 'Echion Hold', 'Sunken Isles', 'The Tunnels', 'The Gulch', 'The Sludge', 'Outskirts', 'Trostland', 'The Reservoir']
