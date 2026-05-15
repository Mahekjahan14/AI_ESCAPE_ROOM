"""Escape room themes — 5 scenario-based levels per theme."""

from pathlib import Path

TOTAL_LEVELS = 5
BASE_LEVEL_SCORE = 1000
HINT_PENALTY = 200
WRONG_GUESS_PENALTY = 50

_ASSETS = Path(__file__).resolve().parent.parent / "assets" / "images"


def _img(seed: str) -> str:
    """Picsum URLs load reliably; optional local override in assets/images/."""
    local = _ASSETS / f"{seed}.jpg"
    if local.is_file() and local.stat().st_size > 5000:
        return str(local)
    return f"https://picsum.photos/seed/escape-{seed}/800/480"


THEMES = {
    "space_station": {
        "title": "Space Station",
        "tagline": "Trapped in orbit. Read each room, find the clue, unlock the door.",
        "cover_image": _img("space-cover"),
        "rooms": [
            {
                "name": "Airlock",
                "image": _img("space-r1"),
                "description": (
                    "Alarms scream. A red gauge on the wall points to **EMPTY**. "
                    "Your **oxygen mask** hangs beside a sign: "
                    "'Refill tank with the gas humans need to breathe.' "
                    "The keypad wants one word."
                ),
                "necessities": ["Oxygen mask", "Pressure gauge", "Tank valve"],
                "question": "Using the sign and the empty gauge — what gas must fill the tank?",
                "answer": "oxygen",
                "hints": [
                    "The sign says what humans need to breathe.",
                    "Plants release this during photosynthesis.",
                    "One word, starts with O."
                ],
            },
            {
                "name": "Observation Window",
                "image": _img("space-r2"),
                "description": (
                    "Through the round window you see a grey cratered sphere hanging in black sky — "
                    "not the Sun. A logbook on the desk is open to **'NIGHT PASS — EARTH'S ___'**. "
                    "The door lock waits for that missing word."
                ),
                "necessities": ["Logbook", "Telescope", "Window shutter"],
                "question": "What is the grey sphere in the window, named in the logbook blank?",
                "answer": "moon",
                "hints": [
                    "Look at what's outside the round window.",
                    "Neil Armstrong walked on it.",
                    "Rhymes with 'soon'."
                ],
            },
            {
                "name": "Solar Panel Bay",
                "image": _img("space-r3"),
                "description": (
                    "Cables run to roof panels. A maintenance tag reads: "
                    "**'Panels face the ___ — do not rotate away.'** "
                    "Outside, the sky is bright with daylight from one blazing star."
                ),
                "necessities": ["Solar wrench", "Cable tester", "Safety tether"],
                "question": "What does the maintenance tag say the panels must face?",
                "answer": "sun",
                "hints": [
                    "Read the tag on the panel cable.",
                    "It rises in the morning and sets at evening.",
                    "Three letters."
                ],
            },
            {
                "name": "Cargo Bay",
                "image": _img("space-r4"),
                "description": (
                    "Crates are stamped with a red planet logo and the words **'DESTINATION: ___'**. "
                    "A poster shows a dusty red world — fourth rock from our star."
                ),
                "necessities": ["Cargo scanner", "Magnetic boots", "Crate opener"],
                "question": "What planet name is missing on the red crate stamp?",
                "answer": "mars",
                "hints": [
                    "Read the crate stamp and poster.",
                    "Called the Red Planet.",
                    "Four letters."
                ],
            },
            {
                "name": "Escape Pod",
                "image": _img("space-r5"),
                "description": (
                    "The pod hatch has a launch checklist. Step 1 is scratched out except: "
                    "**'Board the ___ and strap in.'** "
                    "Through the porthole you see a tall white vehicle on the launch pad."
                ),
                "necessities": ["Launch key", "Harness", "Emergency beacon"],
                "question": "What vehicle does Step 1 tell you to board?",
                "answer": "rocket",
                "hints": [
                    "Read Step 1 on the checklist.",
                    "It blasts off with fire underneath.",
                    "Six letters."
                ],
            },
        ],
    },
    "cyber_lab": {
        "title": "Cyber Lab",
        "tagline": "Locked inside the lab. Every answer is hidden in the room around you.",
        "cover_image": _img("cyber-cover"),
        "rooms": [
            {
                "name": "Workstation Bay",
                "image": _img("cyber-r1"),
                "description": (
                    "A monitor shows **'ACCESS DENIED — enter the device name on the sticker.'** "
                    "The tower under the desk has a label: **'DELL ___'** (the machine with keyboard and screen)."
                ),
                "necessities": ["USB drive", "Keyboard", "Sticky notes"],
                "question": "What device name on the tower sticker unlocks the door?",
                "answer": "computer",
                "hints": [
                    "Read the sticker on the tower under the desk.",
                    "You type on it and watch the monitor.",
                    "Eight letters."
                ],
            },
            {
                "name": "Server Closet",
                "image": _img("cyber-r2"),
                "description": (
                    "Blinking racks hum. A yellow cable tag reads **'CAT-6 ___'** "
                    "and points to the wall port that links PCs to the building network."
                ),
                "necessities": ["Cable tester", "Flashlight", "Fan"],
                "question": "The yellow tag names the cable type — what word completes 'CAT-6 ___'?",
                "answer": "ethernet",
                "hints": [
                    "Look at the yellow cable tag on the rack.",
                    "Common wired network cable type.",
                    "Eight letters."
                ],
            },
            {
                "name": "Security Desk",
                "image": _img("cyber-r3"),
                "description": (
                    "A locked drawer holds the exit key. The screen says: "
                    "**'Type the secret word you use to log in — see the Post-it on the monitor.'** "
                    "The note says: 'Not your username — your ____.'"
                ),
                "necessities": ["ID badge", "Post-it pad", "Drawer key"],
                "question": "What does the Post-it say you must type (your login secret)?",
                "answer": "password",
                "hints": [
                    "Read the note on the monitor.",
                    "Keep it private; you type it after your username.",
                    "Eight letters."
                ],
            },
            {
                "name": "Inbox Terminal",
                "image": _img("cyber-r4"),
                "description": (
                    "An old terminal only opens if you name what's in the **@inbox** folder. "
                    "A whiteboard shows sketches of envelopes flying to a laptop — "
                    "**'digital ___'**."
                ),
                "necessities": ["Headset", "Charger", "Whiteboard marker"],
                "question": "What does the whiteboard call messages in @inbox? (one word)",
                "answer": "email",
                "hints": [
                    "Look at the whiteboard near @inbox.",
                    "You need an address with @ to send it.",
                    "Five letters."
                ],
            },
            {
                "name": "Firewall Exit",
                "image": _img("cyber-r5"),
                "description": (
                    "The final door shows a padlock shaped like a globe with **'WWW'** on it. "
                    "A plaque reads: **'You are on the ___ — the world wide web.'**"
                ),
                "necessities": ["Router reset pin", "LAN cable", "Admin card"],
                "question": "What word completes the plaque after 'You are on the ___'?",
                "answer": "internet",
                "hints": [
                    "Read the plaque under the WWW globe lock.",
                    "Browsers surf it; Wi‑Fi connects to it.",
                    "Eight letters."
                ],
            },
        ],
    },
    "ancient_temple": {
        "title": "Egypt Temple",
        "tagline": "Sand seals every door. Decipher what the tomb shows you.",
        "cover_image": _img("egypt-cover"),
        "rooms": [
            {
                "name": "Sand Antechamber",
                "image": _img("egypt-r1"),
                "description": (
                    "Sand pours under the door. A carved wall shows camels crossing dunes. "
                    "The inscription says: **'Only those who name this dry sea of sand may pass.'**"
                ),
                "necessities": ["Brush", "Water flask", "Torch"],
                "question": "What place does the wall carving describe?",
                "answer": "desert",
                "hints": [
                    "Read the inscription about dry sand and dunes.",
                    "Sahara is one example.",
                    "Six letters."
                ],
            },
            {
                "name": "Pyramid Hall",
                "image": _img("egypt-r2"),
                "description": (
                    "Stone **triangles** tower above you. A floor panel is engraved: "
                    "**'Enter the name of the tomb shape built for pharaohs.'**"
                ),
                "necessities": ["Rope", "Torch oil", "Chisel"],
                "question": "What tomb shape is carved on the floor panel?",
                "answer": "pyramid",
                "hints": [
                    "Look at the stone triangles and the panel text.",
                    "Giza has famous ones.",
                    "Starts with 'pyra'."
                ],
            },
            {
                "name": "Burial Chamber",
                "image": _img("egypt-r3"),
                "description": (
                    "A wooden coffin lies open. Bandages lie on the floor. "
                    "Hieroglyphs read: **'The wrapped king — say our word for the preserved body.'**"
                ),
                "necessities": ["Amulet", "Papyrus", "Oil lamp"],
                "question": "What word do the hieroglyphs use for the wrapped preserved body?",
                "answer": "mummy",
                "hints": [
                    "Read the text above the coffin and bandages.",
                    "Horror films feature them.",
                    "Five letters."
                ],
            },
            {
                "name": "River Mural",
                "image": _img("egypt-r4"),
                "description": (
                    "A long blue mural shows boats on water. A cartouche says: "
                    "**'Life flows on the ___ — Egypt's great river.'**"
                ),
                "necessities": ["Boat model", "Coin offering", "Map shard"],
                "question": "What river name fills the cartouche blank?",
                "answer": "nile",
                "hints": [
                    "Read the mural caption about Egypt's great river.",
                    "Flows through Cairo.",
                    "Four letters."
                ],
            },
            {
                "name": "Sphinx Gate",
                "image": _img("egypt-r5"),
                "description": (
                    "A statue with a human head and lion body guards the exit. "
                    "A plaque asks for **'the creature we carved beside pharaohs — half lion, half human: the ___'**."
                ),
                "necessities": ["Scarab key", "Incense", "Sand scoop"],
                "question": "What is the statue called on the plaque?",
                "answer": "sphinx",
                "hints": [
                    "Read the plaque by the lion-bodied statue.",
                    "Famous one sits near Giza pyramids.",
                    "Six letters."
                ],
            },
        ],
    },
    "haunted_mansion": {
        "title": "Haunted House",
        "tagline": "Something watches from every corner. Solve what the room whispers.",
        "cover_image": _img("haunted-cover"),
        "rooms": [
            {
                "name": "Creaking Foyer",
                "image": _img("haunted-r1"),
                "description": (
                    "A **mirror** reflects nothing but cold mist. A note on the floor says: "
                    "**'I float without feet; the living cannot see me — I am a ___.'** "
                    "Footsteps echo though no one is there."
                ),
                "necessities": ["Candle", "Mirror", "Brass key"],
                "question": "What does the note call the invisible floating presence?",
                "answer": "ghost",
                "hints": [
                    "Read the note by the misty mirror.",
                    "Says 'boo' in stories.",
                    "Five letters."
                ],
            },
            {
                "name": "Dining Room",
                "image": _img("haunted-r2"),
                "description": (
                    "Rotten **pumpkins** sit on the table, carved with faces. "
                    "A menu card reads: **'Served every October 31 — our holiday: _______.'**"
                ),
                "necessities": ["Table cloth", "Silverware", "Lantern"],
                "question": "What holiday name is on the menu card?",
                "answer": "halloween",
                "hints": [
                    "Read the menu date — October 31.",
                    "Kids trick-or-treat.",
                    "Ends with -een."
                ],
            },
            {
                "name": "Attic Ladder",
                "image": _img("haunted-r3"),
                "description": (
                    "Something flutters above. A child's drawing is pinned to the beam: "
                    "a creature with wings, hanging upside down. Caption: **'Count Dracula's pet ___'**."
                ),
                "necessities": ["Rope ladder", "Dust mask", "Old toy"],
                "question": "What pet does the drawing caption name?",
                "answer": "bat",
                "hints": [
                    "Look at the drawing on the attic beam.",
                    "Flies at night; sleeps upside down.",
                    "Three letters."
                ],
            },
            {
                "name": "Kitchen Cauldron",
                "image": _img("haunted-r4"),
                "description": (
                    "A **broom** leans by a bubbling pot. A recipe card lists: "
                    "'Eye of newt, wing of bat, stirred by a ___ wearing a black hat.'"
                ),
                "necessities": ["Broom", "Cauldron", "Spell book"],
                "question": "Who does the recipe say stirs the pot (wears a black hat)?",
                "answer": "witch",
                "hints": [
                    "Read the recipe next to the broom.",
                    "Rides the broom in stories.",
                    "Five letters."
                ],
            },
            {
                "name": "Front Porch",
                "image": _img("haunted-r5"),
                "description": (
                    "The door is chained. A **jack-o'-lantern** glows on the step. "
                    "The lock plate is engraved: **'Carve the orange gourd — we call it a _______.'**"
                ),
                "necessities": ["Bolt cutters", "Porch light bulb", "Coat"],
                "question": "What gourd name is engraved on the lock plate?",
                "answer": "pumpkin",
                "hints": [
                    "Look at the glowing orange thing on the step.",
                    "Jack-o'-lantern is made from it.",
                    "Seven letters."
                ],
            },
        ],
    },
    "pirate_cove": {
        "title": "Pirate Ship",
        "tagline": "Shackled below deck. Follow the captain's clues to break free.",
        "cover_image": _img("pirate-cover"),
        "rooms": [
            {
                "name": "Main Deck",
                "image": _img("pirate-r1"),
                "description": (
                    "Waves slap the hull. A wanted poster shows a vessel with sails. "
                    "**'Stole the gold aboard my ___'** — the captain's handwriting."
                ),
                "necessities": ["Rope", "Spyglass", "Tricorn hat"],
                "question": "What vessel word completes the captain's poster?",
                "answer": "ship",
                "hints": [
                    "Read the wanted poster on the mast.",
                    "Pirates sail it; has sails.",
                    "Four letters."
                ],
            },
            {
                "name": "Captain's Map Table",
                "image": _img("pirate-r2"),
                "description": (
                    "A **map** has a red **X** and a chest drawn in ink. "
                    "The margin says: **'Dig here for the buried _______.'**"
                ),
                "necessities": ["Compass", "Quill", "Wax seal"],
                "question": "What does the map margin say is buried at X?",
                "answer": "treasure",
                "hints": [
                    "Read the words beside the red X.",
                    "Gold in a chest.",
                    "Eight letters."
                ],
            },
            {
                "name": "Anchor Chain Room",
                "image": _img("pirate-r3"),
                "description": (
                    "Heavy **chains** lead through a hole to the sea. A label on the iron reads: "
                    "**'Drop the ___ to stop drifting.'**"
                ),
                "necessities": ["Cutlass", "Gloves", "Oil can"],
                "question": "What iron object does the label tell you to drop?",
                "answer": "anchor",
                "hints": [
                    "Read the label on the chains going to the sea.",
                    "Heavy metal that holds the boat in place.",
                    "Six letters."
                ],
            },
            {
                "name": "Parrot Perch",
                "image": _img("pirate-r4"),
                "description": (
                    "A **cracker** lies on the perch. Feathers are scattered. "
                    "The perch sign jokes: **'Polly is a ___ — repeats every word.'**"
                ),
                "necessities": ["Bird cage", "Cracker", "Bandana"],
                "question": "What bird does the perch sign name?",
                "answer": "parrot",
                "hints": [
                    "Read the sign on the perch.",
                    "Colorful talking pirate pet.",
                    "Six letters."
                ],
            },
            {
                "name": "Treasury Hold",
                "image": _img("pirate-r5"),
                "description": (
                    "Bars guard yellow **ingots**. A ledger column header says **'DOUBLOONS & ___'** "
                    "with a shining metal every pirate steals."
                ),
                "necessities": ["Crowbar", "Lantern", "Empty sack"],
                "question": "What metal fills the ledger blank with doubloons?",
                "answer": "gold",
                "hints": [
                    "Look at the yellow ingots and ledger header.",
                    "Olympic medals use it.",
                    "Four letters."
                ],
            },
        ],
    },
    "secret_lab": {
        "title": "Science Lab",
        "tagline": "Locked after hours. Each lab station holds one clue to the exit.",
        "cover_image": _img("lab-cover"),
        "rooms": [
            {
                "name": "Chemistry Bench",
                "image": _img("lab-r1"),
                "description": (
                    "A **beaker** holds clear liquid. A safety sheet says: "
                    "**'Spill on skin? Rinse with H₂O — common name: ______.'**"
                ),
                "necessities": ["Goggles", "Beaker", "Apron"],
                "question": "What common name does the safety sheet use for H₂O?",
                "answer": "water",
                "hints": [
                    "Read the safety sheet by the beaker.",
                    "You drink it every day.",
                    "Five letters."
                ],
            },
            {
                "name": "Bunsen Station",
                "image": _img("lab-r2"),
                "description": (
                    "A **Bunsen burner** glows orange. The instruction taped to it says: "
                    "**'Never leave unattended while ___ is lit on the wick.'**"
                ),
                "necessities": ["Burner", "Gas valve", "Heat gloves"],
                "question": "What is lit on the wick, according to the taped warning?",
                "answer": "fire",
                "hints": [
                    "Read the tape on the Bunsen burner.",
                    "Hot and bright; put it out with an extinguisher.",
                    "Four letters."
                ],
            },
            {
                "name": "Microscope Desk",
                "image": _img("lab-r3"),
                "description": (
                    "A **microscope** points at a slide. A worksheet asks: "
                    "**'Name the tool that makes tiny cells look bigger: ___________.'**"
                ),
                "necessities": ["Slides", "Lens paper", "Lab coat"],
                "question": "What tool name fills the worksheet blank?",
                "answer": "microscope",
                "hints": [
                    "Look at the worksheet and the device on the desk.",
                    "Scientists peer through it.",
                    "Ten letters."
                ],
            },
            {
                "name": "Medicine Cabinet",
                "image": _img("lab-r4"),
                "description": (
                    "Locked cabinet of **pills** and syrup. A pharmacist note says: "
                    "**'Dispense the correct ___ for the patient.'**"
                ),
                "necessities": ["Thermometer", "Syringe", "Labels"],
                "question": "What word does the pharmacist note say to dispense?",
                "answer": "medicine",
                "hints": [
                    "Read the note on the pill cabinet.",
                    "Taken when you are sick.",
                    "Eight letters."
                ],
            },
            {
                "name": "Emergency Station",
                "image": _img("lab-r5"),
                "description": (
                    "A **stethoscope** hangs by a poster of a person in a white coat. "
                    "The poster title: **'Call the ___ when someone is ill.'**"
                ),
                "necessities": ["First aid kit", "Phone", "Bandages"],
                "question": "Who does the poster say to call?",
                "answer": "doctor",
                "hints": [
                    "Read the poster by the stethoscope.",
                    "Works at a hospital in a white coat.",
                    "Six letters."
                ],
            },
        ],
    },
}
