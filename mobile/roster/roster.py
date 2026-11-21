# Master roster of planned Chordoos. Generates roster.csv (python3 roster.py).
# Format per line: Name | rarity (C/U/R/E/L) | body type | look | personality
# Drawn ones are marked in DRAWN. Theme comes from the section header.

DRAWN = {"Bun Bun", "Sprig", "Pip", "Puddle", "Glimmer", "Volt", "Shade", "Geode", "Blaze King"}

ROSTER = """
## Fire
Blaze King | L | dragon | crowned dragon with bat wings and a flame-tipped tail | Only appears for the hardest workers
Cinder | C | four-legged | ember-orange puppy with a smoky puff tail | Wags so hard that sparks fly
Toastie | C | blob | marshmallow with a golden toasted top | Gets crispy when nervous
Wickit | C | two-legged | little candle sprite with a flame for a hat | Lights the way to the bathroom at night
Flarefin | U | fish | lava fish with glowing cracked scales | Swims laps in hot cocoa
Smolder | U | lizard | salamander with ember spots down its back | Naps on warm rocks all afternoon
Chili Pip | U | plant | red pepper creature with leafy hair | Spicy attitude, sweet heart
Kettlewick | R | object | teapot dragon with a spout snout | Whistles a tune when it's happy
Pyrowl | R | bird | owl with fiery wingtips and ember eyes | Stays up late reading by its own glow
Magmole | R | digger | mole with a lava-rock nose and claws | Tunnels under volcanoes for fun
Sunmane | E | four-legged | lion cub with a mane like a sunrise | Roars the sun up every morning
Phoenixa | E | bird | tiny phoenix with long ribbon feathers | Never, ever gives up
Volcanor | L | rock giant | walking volcano with a smoke crown | Rumbles like thunder when it laughs

## Water
Puddle | C | water creature | pink salamander with frilly gills | Blows bubbles when it's happy
Drip | C | blob | raindrop wearing a tiny umbrella | Always prepared for anything
Shellby | C | turtle | turtle with a swirly seashell on its back | Slow, steady, and never late
Splashpup | C | four-legged | otter pup hugging a starfish | Thinks bath time is the best time
Krilla | U | octopus | tiny octopus wearing mismatched socks | Gives eight hugs at once
Bubblun | U | fish | round pufferfish with polka dots | Puffs up when surprised
Seahop | U | seahorse | seahorse with a curly crown tail | Bounces along on the waves
Tidewing | R | ray | manta ray with wave patterns | Glides like a kite underwater
Coralie | R | water creature | coral sprite with branchy antlers | Keeps the reef neat and tidy
Gurgle | R | frog | pond frog wearing a lily-pad hat | Croaks lullabies at dusk
Nautilux | E | shell | glowing nautilus with a lantern shell | Lights up the deep, dark sea
Leviathorn | E | serpent | sea serpent with a frilled fin crest | Makes the biggest splashes ever
Abyssa | L | whale | star-speckled whale swimming through the sky | Sings to the moon every night

## Plant
Sprig | C | four-legged | fox with a big leaf for a tail | Grows a little every time it rains
Mossy | C | blob | mossy pebble with a mushroom cap | Loves quiet, shady corners
Sprout | C | two-legged | seedling kid with two big leaves | Stretches tall every morning
Acornelius | C | nut | acorn wearing a tiny beret | Collects lost buttons
Petalfly | U | bug | butterfly with flower-petal wings | Visits every garden in town
Thornby | U | hedgehog | hedgehog with rose-thorn quills | Prickly on the outside, polite inside
Pumpkid | U | plant | pumpkin with curly vine arms | Grows bigger every fall
Bloomoth | R | bug | moth whose wings bloom at night | Smells like lavender
Mushroomba | R | two-legged | dancing mushroom with polka dots | Can't stop dancing
Barkley | R | four-legged | puppy made of bark and leaves | Fetches pinecones all day
Willowisp | E | floating | willow spirit with glowing fronds | Whispers bedtime stories
Elderoak | E | rock giant | ancient tree guardian with a bird's nest | Very wise and very patient
Gaiaflora | L | deer | forest deer with flowers blooming on its antlers | Gardens grow wherever it steps

## Sky
Pip | C | bird | songbird with a sunset tail and cloud wings | Sings the wake-up song right on time
Nimbo | C | blob | fluffy cloud with rosy cheeks | Rains a little during sad movies
Kitezy | C | object | kite creature with a ribbon tail | Waits all week for windy days
Breezle | C | four-legged | flying squirrel with a leaf glider | Leaps from tree to tree
Hootsie | U | bird | sleepy owlet in a nightcap | Always up past bedtime
Zephyrin | U | floating | swirly wind sprite | Flips book pages for you
Balloonbo | U | object | hot-air balloon with a smiling basket | Floats off to new places
Rainbeaux | R | serpent | rainbow-striped sky snake | Appears right after storms
Gustav | R | bird | eagle chick wearing flight goggles | The bravest little flyer
Skyfoal | R | four-legged | winged foal with cloud hooves | Gallops across the clouds
Aerodon | E | dragon | cloud dragon with feathered wings | Rides the jet stream
Stormcrest | E | bird | great bird with a lightning crest | Brings rain to thirsty plants
Zenithia | L | bird | radiant sky queen with a comet tail | Seen only once in a hundred years

## Electric
Volt | U | bug | beetle with a lightning horn and bolt-marked shell | Runs on 100% kid energy
Zappy | C | blob | static fluff ball | Sticks to socks and won't let go
Glowbug | C | bug | firefly with a battery belly | Glows brighter when it's proud
Buzzby | C | bug | bumblebee with lightning stripes | Buzzes with excitement
Ampere | U | eel | electric eel with neon stripes | Lights up the whole aquarium
Bulbo | U | two-legged | lightbulb kid with a filament smile | Always has bright ideas
Joltlynx | R | four-legged | lynx kitten with storm-cloud fur | Pounces as fast as lightning
Teslo | R | floating | humming orb with orbiting sparks | Hums along to every song
Neonix | R | lizard | neon gecko that sticks to ceilings | The best night-light buddy
Thunderpaw | E | four-legged | big cat with lightning stripes | Fastest paws in the galaxy
Gigawatt | E | robot | lighthouse robot with a spinning beam | Guides ships home safely
Voltaros | L | dragon | storm dragon with a crackling crown | Commands the thunder

## Ice
Frostbite | C | blob | snowball with icicle teeth | Makes snowflakes when it sneezes
Pengwyn | C | bird | penguin chick in a knitted scarf | Slides everywhere on its tummy
Sleetle | C | bug | ladybug with snowflake spots | Ice-skates on frozen puddles
Mittsy | C | object | living mitten with a pompom | Keeps your hands toasty
Polarbit | U | four-legged | polar bear cub with frosty ears | Gives the warmest hugs
Glacio | U | rock giant | small ice cube golem | Melts a little when you smile at it
Snowl | U | bird | snowy owl with a frost crown | Can see through blizzards
Yetti | R | two-legged | fluffy yeti kid with blue horns | Builds amazing snow forts
Auroracub | R | four-legged | arctic fox with aurora-colored tail | Paints the night sky
Crystalisk | R | lizard | frost lizard with crystal spines | Leaves frosty footprints
Blizzaron | E | serpent | ice serpent made of swirling snow | Makes snow days happen
Frostfang | E | four-legged | white wolf with an icicle mane | Howls winter in
Glaciera | L | dragon | glacier dragon with crystal wings | Sleeps on top of the tallest mountain

## Crystal and Rock
Geode | E | rock giant | rock giant with a glowing crystal heart | Gentle, strong, and kind
Pebble | C | blob | round pebble with a moss hat | Can stay still longer than anyone
Gemmy | C | four-legged | puppy with gem spots | Digs up shiny treasures
Quartzy | C | bug | crab with a crystal shell | Walks sideways into everything
Rubbles | U | two-legged | rock kid with a pickaxe | Loves building things
Opalynn | U | snail | snail with an opal shell | Leaves a rainbow trail
Boulderdash | U | armadillo | armadillo that rolls into a boulder | Rolls downhill for fun
Amethyx | R | four-legged | wolf with amethyst crystals on its back | Guards the crystal caves
Obsidino | R | dino | little dinosaur made of shiny black stone | Super shiny, super proud
Prismara | R | floating | prism that splits light into rainbows | Makes rainbows on the walls
Diamondo | E | armadillo | armored beast with diamond plates | The toughest Chordoo around
Mountaine | L | rock giant | mountain giant with snowy peaks and a waterfall beard | Older than the hills

## Bug
Ladybop | C | bug | ladybug with heart-shaped spots | Counts its spots every morning
Wiggly | C | worm | inchworm in tiny glasses | Measures everything twice
Antsy | C | bug | ant carrying a crumb ten times its size | Never stops moving
Snailbert | C | snail | snail with a cupcake shell | Takes its time, and that's okay
Mantee | U | bug | praying mantis in karate gear | Practices kicks every day
Dragonfli | U | bug | dragonfly with stained-glass wings | Zips around the pond
Beetlejoy | U | bug | dung-ball beetle rolling a gumball | Collects colorful things
Webster | R | spider | friendly spider knitting a web scarf | Knits presents for everyone
Monarcha | R | bug | butterfly with royal orange wings | Travels thousands of miles
Scorpio | R | bug | sand scorpion with a heart-tipped tail | Looks tough, is a softie
Hivequeen | E | bug | bee queen with honeycomb crown | Runs the busiest hive
Lunamoth | L | bug | giant moon moth with glowing wing-eyes | Only flies on full moons

## Spooky
Drizzle | C | ghost | sleepy cloud ghost | Mostly harmless
Peekaberry | C | ghost | purple berry ghost with a leaf | Says boo, then says sorry
Batty | C | bat | round bat with oversized ears | Hangs upside down to think
Skelly | C | two-legged | tiny skeleton in a party hat | Rattles when it laughs
Pumpkinhead | U | two-legged | scarecrow with a jack-o-lantern grin | Scares away only the crows
Cobweb | U | spider | fuzzy spider with eight boots | Tap dances on its web
Wispurr | U | four-legged | ghost kitten with a wispy tail | Purrs you to sleep
Gloomsy | R | ghost | gentle ghost with a lantern eye | Guards your dreams
Hexie | R | two-legged | little witch frog with a pointy hat | Brews hot-chocolate potions
Vampurr | R | bat | bat-cat with a cape | Only drinks tomato juice
Mummo | E | two-legged | mummy wrapped in rainbow bandages | Gives the best bear hugs
Phantasma | E | ghost | ghost queen with a flowing veil | Throws midnight parties
Duskhorn | L | four-legged | shadow unicorn with a starlit mane | Chases bad dreams away

## Cosmic
Nova | U | blob | star-eyed purple puff | Born from a wish on a shooting star
Moonbeam | C | blob | sleepy crescent moon | Shows up after the bedtime routine
Astro | C | two-legged | kid astronaut with a fishbowl helmet | Wants to visit every planet
Starfry | C | fish | starfish that floats in space | Twinkles when you wave
Cometail | U | four-legged | space puppy with a comet tail | Zooms around the planets
Orbit | U | floating | little planet with a ring | Spins when it's dizzy with joy
Ufolo | U | object | flying saucer with an alien pilot | Beams up lost toys
Nebulynx | R | four-legged | cat made of nebula clouds | Purrs in stardust
Saturnine | R | floating | ringed planet creature with moon friends | Has the most friends in space
Galactopus | R | octopus | space octopus with star suckers | Juggles planets
Supernova | E | floating | exploding-star sprite | Bursts with energy
Cosmodrake | E | dragon | constellation dragon with star-dot body | Draws pictures in the night sky
Aurora | L | floating | fairy of the northern lights | Paints colors nobody has named yet

## Snack
Toasty | C | object | slice of toast with jam cheeks | Pops up at breakfast time
Marsh | C | blob | marshmallow with sleepy eyes | The best at hugs
Nibbles | C | four-legged | hamster holding a cracker | Trades any toy for a cracker
Puddin | C | blob | wobbly pudding cup | Jiggles when it giggles
Sushiro | U | fish | sushi roll fish | Rolls instead of swims
Pretzlette | U | serpent | pretzel snake with salt sprinkles | Ties itself in knots
Waffly | U | four-legged | waffle puppy with syrup drips | Sweetest pup on the block
Sir Sprinkles | R | two-legged | donut knight with a sprinkle shield | Royal ruler of Dessert Land
Cupcakey | R | blob | cupcake with a cherry hat | Throws surprise parties
Gumdrop | R | blob | gumdrop that bounces | Bounces higher than the house
Cocoabear | E | four-legged | hot cocoa bear with marshmallow ears | Warms you up on cold days
Sundaesaur | E | dino | ice-cream dinosaur with cone spikes | Melts hearts, not ice cream
Gingerking | L | two-legged | gingerbread king with an icing crown | Rules the candy castle

## Music
Drumbo | C | two-legged | drum with drumstick arms | Keeps the beat
Tootle | C | bird | flute bird with whistle beak | Whistles while it works
Maraca | C | two-legged | maraca twins | Shake shake shake!
Kazoo | C | bug | buzzy kazoo beetle | Hums silly songs
Pianopus | U | octopus | octopus playing eight keys | Plays duets with itself
Guitarmadillo | U | armadillo | armadillo with a guitar shell | Strums bedtime songs
Trumpetal | U | plant | trumpet flower | Toots a fanfare at sunrise
Harpy | R | bird | swan with harp-string wings | Plays the calmest melodies
Bassoon | R | serpent | bassoon snake with deep voice | Sings the low notes
Discodile | R | lizard | crocodile in a disco suit | Dance party every Friday
Maestro | E | four-legged | conductor cat with a baton tail | Leads the forest orchestra
Symphonix | E | bird | songbird with music-note feathers | Every chirp is a song
Melodia | L | floating | music fairy surrounded by floating notes | Hums the song of the stars

## Robot
Pixel | C | robot | square robot with a screen face | Beep boop means good job
Boltie | C | robot | wind-up robot with a key | Runs until it needs a nap
Gizmo | C | bug | clockwork ladybug | Tick-tocks when it walks
Sprocket | C | four-legged | robot puppy with gear ears | Fetches screws
Rustle | U | robot | little rusty robot with a flower | Loves gardening
Clank | U | rock giant | trash-can robot | Recycles everything
Drono | U | floating | propeller drone with puppy eyes | Delivers hugs by air
Mechanix | R | robot | robot with telescoping arms | Can reach the top shelf
Cyberpaw | R | four-legged | robot cat with LED whiskers | Purrs in binary
Rocketto | R | object | little rocket with fins | Counts down from ten
Megabyte | E | robot | big friendly mecha with a cockpit | Built to help
Steamdrake | E | dragon | steampunk dragon with gears | Puffs steam rings
Chronotron | L | robot | clock guardian with hands for wings | Knows exactly when bedtime is

## Fairy and Dream
Glimmer | U | blob | pink fairy drop with wings and a wand | Leaves a trail of glitter
Bun Bun | C | four-legged | peach bunny holding a carrot | Hops three times before every nap
Snuggle | C | blob | lavender cuddle cloud with a scarf | Keeps everyone cozy
Dewdrop | C | bug | tiny fairy with dewdrop wings | Waters flowers at dawn
Pillowpuff | C | blob | pillow creature with button eyes | Falls asleep anywhere
Sugarplum | U | two-legged | sugar fairy with candy wings | Dances on tiptoes
Dreamsheep | U | four-legged | sheep with a cloud fleece | Helps you count to sleep
Twinkle | U | floating | star fairy with sparkle trail | Grants tiny wishes
Unibun | R | four-legged | bunny with a unicorn horn | Hops over rainbows
Wishkit | R | four-legged | kitten with wishing-star tail | Makes wishes come true
Pegapony | R | four-legged | pony with butterfly wings | Flies over the clouds
Fairyqueen | E | two-legged | fairy queen with a flower crown | Rules the hidden garden
Sandmane | E | four-legged | dream lion with a sand mane | Sprinkles sleepy sand
Lullabelle | L | bird | dream swan with starry wings | Sings everyone to sleep

## Desert
Cactoo | C | plant | cactus with a flower hat | Gives careful hugs
Fennix | C | four-legged | fennec fox with giant ears | Hears everything
Sandy | C | blob | sand castle creature | Rebuilds after every wave
Camelot | U | four-legged | baby camel with a water-bottle hump | Never gets thirsty
Tumbleweed | U | blob | tumbleweed that rolls | Goes wherever the wind blows
Mirajj | U | floating | heat shimmer sprite | Plays hide and seek
Scarabelle | R | bug | golden scarab with a sun disk | Rolls the sun across the sky
Dunewyrm | R | serpent | sand serpent with dune ridges | Swims through sand
Sphinxie | R | four-legged | little sphinx cat | Loves riddles
Pharaowl | E | bird | owl in a golden headdress | Keeper of ancient stories
Oasira | L | four-legged | desert lion with an oasis mane | Brings water to the desert

## Street and Cool
Shade | R | blob | navy cool kid with shades and headphones on a skateboard | Too cool for bedtime
Ziggy | C | blob | yellow zigzag kid with a mohawk | Skates in the kitchen
Graffito | C | four-legged | paint-splattered raccoon | Paints murals on walls
Beatbox | C | object | boombox with legs | Drops beats on demand
Hoopster | U | two-legged | basketball kid | Never misses a shot
Skaterpillar | U | worm | caterpillar on a skateboard | Ollies over twigs
DJ Doodle | U | four-legged | poodle DJ with headphones | Spins the best tracks
Spinz | R | two-legged | breakdancing hedgehog | Spins on its quills
Rexy Kicks | R | dino | dino in high-top sneakers | Kicks with style
Neon Ninja | R | two-legged | ninja frog with glow headband | Sneaks snacks silently
Major Muffin | E | two-legged | superhero muffin with a cape | Saves the day one crumb at a time
Rockstarling | L | bird | rockstar bird with an electric guitar | Headlines every show
"""

import csv, re
rows = []
theme = None
for line in ROSTER.strip().splitlines():
    line = line.strip()
    if not line:
        continue
    if line.startswith("## "):
        theme = line[3:]
        continue
    parts = [p.strip() for p in line.split("|")]
    name = parts[0].split(";")[-1].split("?")[-1].strip()
    rows.append({
        "name": name, "rarity": {"C": "Common", "U": "Uncommon", "R": "Rare", "E": "Epic", "L": "Legendary"}[parts[1]],
        "theme": theme, "body": parts[2], "look": parts[3], "personality": parts[4],
        "status": "Drawn" if name in DRAWN else "Planned",
    })

if __name__ == "__main__":
    import collections, sys
    names = [r["name"] for r in rows]
    dupes = [n for n, c in collections.Counter(names).items() if c > 1]
    with open(__file__.replace("roster.py", "roster.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print(len(rows), "Chordoos;", collections.Counter(r["rarity"] for r in rows), "dupes:", dupes, file=sys.stderr)
