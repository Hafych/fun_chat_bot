from prettytable import PrettyTable
from utils.style import colored_print, emoji_wrap
import random

MOVIES = {
    'action': [
        'Mad Max: Fury Road', 'John Wick', 'Die Hard', 'The Dark Knight',
        'Mission: Impossible – Fallout', 'Kingsman: The Secret Service',
        'Atomic Blonde', 'Nobody', 'The Raid', 'Sicario'
    ],
    'comedy': [
        'Superbad', 'Anchorman', 'The Hangover', 'Annie Hall',
        'Tropic Thunder', 'Bridesmaids', 'The Grand Budapest Hotel',
        'Step Brothers', 'Tropic Thunder', 'Dumb and Dumber'
    ],
    'horror': [
        'The Conjuring', 'Hereditary', 'Get Out', 'The Shining',
        'Insidious', 'A Quiet Place', 'The Babadook', 'Midsommar',
        'Sinister', 'The Witch'
    ],
    'drama': [
        'The Shawshank Redemption', 'Forrest Gump', 'Schindler’s List',
        'The Godfather', 'Good Will Hunting', 'Requiem for a Dream',
        'Manchester by the Sea', 'Moonlight', 'Marriage Story', 'Nomadland'
    ],
    'scifi': [
        'Blade Runner 2049', 'Interstellar', 'Arrival', 'Ex Machina',
        'The Matrix', 'Dune', 'Children of Men', 'Her', 'Gravity', 'Annihilation'
    ],
    'fantasy': [
        'The Lord of the Rings: The Fellowship of the Ring',
        'Pan’s Labyrinth', 'Stardust', 'The Chronicles of Narnia',
        'Harry Potter and the Prisoner of Azkaban', 'Spirited Away',
        'Coraline', 'The NeverEnding Story', 'Willow', 'The Green Knight'
    ],
    'animation': [
        'Spirited Away', 'Inside Out', 'Soul', 'Coco', 'Wall-E',
        'Spider-Man: Into the Spider-Verse', 'The Incredibles',
        'Howl’s Moving Castle', 'Kiki’s Delivery Service', 'Up'
    ],
    'thriller': [
        'Gone Girl', 'Prisoners', 'Zodiac', 'Nightcrawler',
        'The Silence of the Lambs', 'Oldboy', 'Shutter Island',
        'Parasite', 'Prisoners', 'The Girl with the Dragon Tattoo'
    ],
    'romance': [
        'Eternal Sunshine of the Spotless Mind', 'Before Sunrise',
        'La La Land', 'Amélie', 'The Notebook', 'Her', 'Call Me by Your Name',
        'Portrait of a Lady on Fire', 'Silver Linings Playbook', 'Notting Hill'
    ],
    'adventure': [
        'Indiana Jones and the Raiders of the Lost Ark',
        'Jurassic Park', 'Pirates of the Caribbean: The Curse of the Black Pearl',
        'Avatar', 'The Revenant', 'Jumanji: Welcome to Jungle',
        'National Treasure', 'The Mummy', 'Uncharted', 'Journey to the Center of the Earth'
    ]
}

MUSIC = {
    'rock': [
        'Bohemian Rhapsody — Queen',
        'Stairway to Heaven — Led Zeppelin',
        'Smells Like Teen Spirit — Nirvana',
        'Sweet Child O’ Mine — Guns N’ Roses',
        'Hotel California — Eagles',
        'Back in Black — AC/DC',
        'Purple Haze — Jimi Hendrix',
        'Comfortably Numb — Pink Floyd',
        'Enter Sandman — Metallica',
        'November Rain — Guns N’ Roses'
    ],
    'pop': [
        'Blinding Lights — The Weeknd',
        'Levitating — Dua Lipa',
        'Bad Guy — Billie Eilish',
        'Rolling in the Deep — Adele',
        'Uptown Funk — Mark Ronson ft. Bruno Mars',
        'Shape of You — Ed Sheeran',
        'Watermelon Sugar — Harry Styles',
        'Peaches — Justin Bieber',
        'As It Was — Harry Styles',
        'Toxic — Britney Spears'
    ],
    'jazz': [
        'Take Five — Dave Brubeck',
        'So What — Miles Davis',
        'What a Wonderful World — Louis Armstrong',
        'Autumn Leaves — Eva Cassidy',
        'My Favorite Things — John Coltrane',
        'Feeling Good — Nina Simone',
        'Sing, Sing, Sing — Benny Goodman',
        'Blue in Green — Miles Davis',
        'In a Sentimental Mood — Duke Ellington',
        'Cantaloupe Island — Herbie Hancock'
    ],
    'electronic': [
        'Strobe — Deadmau5',
        'Midnight City — M83',
        'Lean On — Major Lazer & DJ Snake',
        'Faded — Alan Walker',
        'Sun Models — ODESZA',
        'Wake Me Up — Avicii',
        'Adagio for Strings — Tiësto',
        'Around the World — Daft Punk',
        'Language — Porter Robinson',
        'Can’t Stop Playing — Laidback Luke'
    ],
    'hiphop': [
        'Lose Yourself — Eminem',
        'Juicy — The Notorious B.I.G.',
        'N.Y. State of Mind — Nas',
        'Alright — Kendrick Lamar',
        'Humility — Gorillaz',
        'Sicko Mode — Travis Scott',
        'God’s Plan — Drake',
        'Riptide — Vegyn',
        'Energy — The Internet',
        'Electric Relaxation — A Tribe Called Quest'
    ],
    'classical': [
        'Für Elise — Beethoven',
        'Nocturne in E-flat Major — Chopin',
        'The Four Seasons: Spring — Vivaldi',
        'Clair de Lune — Debussy',
        'Canon in D — Pachelbel',
        'Symphony No. 9 — Beethoven',
        'Air on the G String — Bach',
        'Moonlight Sonata — Beethoven',
        'Pavane — Fauré',
        'Sabre Dance — Khachaturian'
    ],
    'indie': [
        'Mr. Blue Sky — Electric Light Orchestra',
        'Skinny Love — Bon Iver',
        'Oxford Comma — Vampire Weekend',
        'Float On — Modest Mouse',
        'Cellophane — FKA twigs',
        'The Suburbs — Arcade Fire',
        'Dog Days Are Over — Florence + The Machine',
        'I Will Follow You into the Dark — Death Cab for Cutie',
        'Breezeblocks — alt-J',
        'Ride — Lana Del Rey'
    ],
    'metal': [
        'Master of Puppets — Metallica',
        'Walk — Pantera',
        'Chop Suey! — System of a Down',
        'Hallowed Be Thy Name — Iron Maiden',
        'Holy Wars... The Punishment Due — Megadeth',
        'Blackbird — Pearl Jam',
        'Duality — Slipknot',
        'Thunderkiss — Rob Zombie',
        'Cowboys from Hell — Pantera',
        'Cemetery Gates — Pantera'
    ]
}

GAMES = {
    'action': [
        'Call of Duty: Modern Warfare',
        'Assassin’s Creed Valhalla',
        'DOOM Eternal',
        'Cyberpunk 2077',
        'Red Dead Redemption 2',
        'Ghost of Tsushima',
        'Horizon Zero Dawn',
        'Devil May Cry 5',
        'Resident Evil Village',
        'Metal Gear Solid V: The Phantom Pain'
    ],
    'rpg': [
        'The Witcher 3: Wild Hunt',
        'Elden Ring',
        'Skyrim',
        'Final Fantasy VII Remake',
        'Disco Elysium',
        'Mass Effect: Legendary Edition',
        'Dragon Age: Inquisition',
        'Persona 5 Royal',
        'Baldur’s Gate 3',
        'Star Wars: Knights of the Old Republic'
    ],
    'strategy': [
        'Civilization VI',
        'XCOM 2',
        'Crusader Kings III',
        'Total War: WARHAMMER III',
        'Age of Empires IV',
        'Into the Breach',
        'Stellaris',
        'Northgard',
        'They Are Billions',
        'Supreme Commander 2'
    ],
    'survival': [
        'Valheim',
        'Rust',
        'Don’t Starve Together',
        'ARK: Survival Evolved',
        'The Forest',
        'Subnautica',
        'Green Hell',
        'Project Zomboid',
        '7 Days to Die',
        'Raft'
    ],
    'puzzle': [
        'Portal 2',
        'The Witness',
        'Return of the Obra Dinn',
        'Baba Is You',
        'Outer Wilds',
        'Gorogoa',
        'Tetris Effect: Connected',
        'Monument Valley',
        'The Talos Principle',
        'Stephen’s Sausage Roll'
    ],
    'adventure': [
        'The Last of Us Part I',
        'Life is Strange',
        'Firewatch',
        'What Remains of Edith Finch',
        'Gone Home',
        'Oxenfree',
        'Uncharted: The Lost Legacy',
        'Telling Lies',
        'Kentucky Route Zero',
        'Dear Esther'
    ],
    'simulation': [
        'The Sims 4',
        'Stardew Valley',
        'Microsoft Flight Simulator',
        'Euro Truck Simulator 2',
        'Planet Zoo',
        'Two Point Hospital',
        'Cities: Skylines',
        'Animal Crossing: New Horizons',
        'Cooking Simulator',
        'Farming Simulator 22'
    ],
    'multiplayer': [
        'Among Us',
        'Fortnite',
        'Apex Legends',
        'Overwatch 2',
        'Valorant',
        'Rocket League',
        'Minecraft',
        'Sea of Thieves',
        'Fall Guys',
        'Destiny 2'
    ]
}


def show_table(data, title):
    table = PrettyTable()
    table.field_names = ["Жанр", "Примеры"]
    for genre, items in data.items():
        table.add_row([genre.capitalize(), ", ".join(items[:2]) + "..."])
    table.align = "l"
    colored_print(f"\n{emoji_wrap(title, ':sparkles:')}", "magenta")
    print(table)


def get_choice(data, prompt):
    show_table(data, prompt)
    while True:
        choice = input(f"Выберите жанр: ").lower()
        if choice in data:
            return data[choice]
        colored_print("❌ Нет такого жанра!", "red")


def recommend_movie():
    result = random.choice(get_choice(MOVIES, "Фильмы"))
    colored_print(f"🎬 Рекомендую: {result}", "green")


def recommend_music():
    result = random.choice(get_choice(MUSIC, "Музыка"))
    colored_print(f"🎵 Попробуйте: {result}", "cyan")


def recommend_game():
    result = random.choice(get_choice(GAMES, "Игры"))
    colored_print(f"🎮 Поиграйте в: {result}", "blue")