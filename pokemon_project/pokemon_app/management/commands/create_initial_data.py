from typing import Any
from django.core.management.base import BaseCommand
from pokemon_app.models import PokemonCard, Trainer


class Command(BaseCommand):
    help = 'Creates initial data for the application'
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.pokemon_cards = []
        self.trainers = []
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        self.create_pokemon_cards()
        self.create_trainers()

        print("Pokemon Cards:")
        for card in self.pokemon_cards:
            #card.show_info()
            print("\n" + "=" * 30 + "\n")
            # Save the Pokemon card to the database
            card.save()
            self.stdout.write(self.style.SUCCESS('Successfully created Pokemon Cards.'))

        print("Trainers:")
        for trainer in self.trainers:
            #trainer.show_info()
            print("\n" + "=" * 30 + "\n")
            trainer.save()
            self.stdout.write(self.style.SUCCESS('Successfully Inserted trainers.'))

    def create_pokemon_cards(self):
        card1 = PokemonCard(name="Pikachu", rarity="Rare",hp=60, card_type="Electric", attack="Thunder Shock",
                            description="A mouse-like pokemon that can generate electricity.",
                            weakness="Ground", card_number=25, release_date="1996-02-27", evolution_stage="Basic",
                            abilities="Static")
        self.pokemon_cards.append(card1)
        card1.save()
        card2 = PokemonCard(name= "Charmeleon", rarity= "Rare",hp= 120, card_type= "Fire", attack= "Flamethrower", 
                            description= "It has a barbaric nature. In battle, it whips its fiery tail around and slashes away with sharp claws.", 
                            weakness= "Water",card_number= 5,release_date= "1996-02-27", evolution_stage= "Stage 2", abilities= "Solar Power")
        self.pokemon_cards.append(card2)
        card2.save()
        card3 = PokemonCard(name= "Mewtwo", rarity= "Uncommon",hp=  150, card_type= "Psychic", attack= "Psychic",
                            description= "A genetically engineered pokemon that has powerful psychic abilities.", 
                            weakness= "Dark",card_number= 10,release_date= "1996-02-27", evolution_stage= "Basic", abilities= "Pressure")
        self.pokemon_cards.append(card3)
        card3.save()
        card4 = PokemonCard(name= "Caterpie", rarity= "Common",hp= 45, card_type= "Grass", attack= "Bug Bite", 
                            description= "For protection, it releases a horrible stench from the antenna on its head to drive away enemies.", 
                            weakness= "Fire", card_number= 44, release_date= "1996-02-27", evolution_stage= "Basic", abilities= "Shield Dust")
        self.pokemon_cards.append(card4)
        card4.save()
        card5 = PokemonCard(name= "Squirtle", rarity= "Rare",hp= 40, card_type= "Water",attack=  "Bubble", 
                            description= "A turtle-like pokemon that can squirt water.", 
                            weakness= "Grass", card_number=  63, release_date= "1996-02-27", evolution_stage= "Basic", abilities= "Torrent")
        self.pokemon_cards.append(card5)
        card5.save()
        card6 = PokemonCard(name= "Eevee",rarity= "Rare", hp= 50, card_type= "Normal", attack= "Tackle", 
                            description= "A fox-like pokemon that can evolve into different types.", 
                            weakness= "Fighting", card_number= 51, release_date= "1996-02-27", evolution_stage= "Basic", abilities= "Adaptability")
        self.pokemon_cards.append(card6)
        card6.save()
        card7 = PokemonCard(name="Snorlax",rarity= "Uncommon",hp= 140,card_type= "Normal",attack= "Body Slam", 
                            description="A huge pokemon that likes to sleep and eat.",
                            weakness="Fighting",card_number= 27,release_date="1996-02-27", evolution_stage= "Final",abilities= "Thick Fat")
        self.pokemon_cards.append(card7)
        card7.save()
        card8 = PokemonCard(name="Raikou",rarity= "Rare", hp= 90,card_type= "Electric",attack= "Thunder Fang",
                            description="Raikou embodies the speed of lightning. The roars of this Pokémon send shock waves shuddering through the air and shake the ground as if lightning bolts had come crashing down.",
                            weakness="Ground",card_number= 243,release_date="1999-11-21", evolution_stage= "Basic",abilities= "Pressure")
        self.pokemon_cards.append(card8)
        card8.save()
        card9 = PokemonCard(name="Cryogonal",rarity= "Rare",hp= 80,card_type= "Ice",attack= "Aurora Beam",
                            description="Cryogonal appear during cold seasons. It is said that people and Pokémon who die on snowy mountains are reborn into these Pokémon.",
                            weakness= "Fire",card_number= 615,release_date="2010-09-18",evolution_stage= "Basic",abilities= "Levitate")
        self.pokemon_cards.append(card9)
        card9.save()
        card10 = PokemonCard(name="Pancham",rarity= "Uncommon",hp= 67,card_type= "Fighting",attack= "Circle Throw",
                            description= "It chooses a Pangoro as its master and then imitates its masters actions. This is how it learns to battle and hunt for prey",
                            weakness= "Fairy",card_number= 674, release_date="2013-08-12", evolution_stage= "Basic",abilities= "Mold Breaker")
        self.pokemon_cards.append(card10)
        card10.save()
        card11 = PokemonCard(name="Entei",rarity= "Rare",hp= 115,card_type= "Fire",attack= "Flame Wheel",
                            description= "Entei embodies the passion of magma. This Pokémon is thought to have been born in the eruption of a volcano. It sends up massive bursts of fire that utterly consume all that they touch." ,
                            weakness= "Water" ,card_number= 244,release_date= "1999-11-21", evolution_stage= "Basic" ,abilities= "Pressure")
        self.pokemon_cards.append(card11)
        card11.save()
        card12 = PokemonCard(name="Suicune",rarity= "Rare",hp= 100,card_type= "Water",attack= "Hydro Pump",
                            description= "Suicune embodies the compassion of a pure spring of water. It runs across the land with gracefulness. This Pokémon has the power to purify dirty water." ,
                            weakness= "Grass" ,card_number= 245 ,release_date="1999-11-21", evolution_stage= "Final Form" ,abilities= "Pressure")
        self.pokemon_cards.append(card12)
        card12.save()
        card13 = PokemonCard(name="Mudkip",rarity= "Common",hp= 50,card_type= "Water",attack= "Watergun",
                            description= "A small, ammphibious, quadrupedal Pokemon." ,
                            weakness= "Electric" ,card_number= 258  ,release_date="2001-03-19",evolution_stage= "Basic" ,abilities= "Torrent")
        self.pokemon_cards.append(card13)
        card13.save()
        card14 = PokemonCard(name="Meowth",rarity= "Rare",hp= 40,card_type= "Normmal",attack= "Fake out",
                            description= " A small, feline Pokemon with creamm0colored fur that turns brown at the tips of its hind paws and tail." ,
                            weakness= "Fighting"  ,card_number= 52,release_date= "1996-02-27",evolution_stage= "Basic" ,abilities= "Pickup")
        self.pokemon_cards.append(card14)
        card14.save()
        card15 = PokemonCard(name="Jigglypuf",rarity= "Rare",hp= 115,card_type= "Fairy",attack= "Disarming Voice",
                            description= "A pink pokemon with a spherical body" ,
                            weakness= "Dark" , card_number= 39 ,release_date= "1996-02-27", evolution_stage= "Basic" ,abilities= "Cute Charm")
        self.pokemon_cards.append(card15)
        card15.save()
        card16 = PokemonCard(name="Duskull",rarity= "Common",hp= 20,card_type= "Ghost",attack= "Payback",
                            description= "If it finds bad children who wont listen to their parents, it will spirit them away—or so its said." ,
                            weakness= "Dark" ,card_number= 355,release_date= "2002-11-21", evolution_stage= "Basic", abilities= "Levitate")
        self.pokemon_cards.append(card16)
        card16.save()
        card17 = PokemonCard(name="Wobbuffet",rarity= "Rare",hp= 190,card_type= "Pyschic",attack= "Destiny Bond",
                            description= "A tall, cyan Pokemon with a soft body." ,
                            weakness= "Dark" ,card_number= 202 ,release_date= "2002-11-21", evolution_stage= "Final Form" ,abilities= "Shadow Tag")
        self.pokemon_cards.append(card17)
        card17.save()
        card18 = PokemonCard(name="Darkrai",rarity= "Rare",hp= 70,card_type= "Dark",attack= "Dark Pulse",
                            description= "A black, shadow-like Pokemon. It has a small head with a white fog-like ghostly plume billowing from its head covering one of its bright blue eyes" ,
                            weakness= "Fairy" ,card_number= 491 ,release_date= "2004-11-18" ,evolution_stage= "Final Form" ,abilities= "Intimidate")
        self.pokemon_cards.append(card18)
        card18.save()
        card19 = PokemonCard(name= "Totodile",rarity= "Common",hp= 50,card_type= "Water",attack= "Water Gun",
                            description= "Is a bipedal, crocodilian Pokemon with well-developed jaws." ,
                            weakness= "Grass"  , card_number= 158,release_date="2001-03-19", evolution_stage= "Basic" ,abilities= "Torrent")
        self.pokemon_cards.append(card19)
        card19.save()
        card20 = PokemonCard(name= "Deoxys",rarity= "Rare",hp= 50,card_type= "Pyschic",attack= "Cosmic Power",
                            description= "An alien-like, bipedal Pokemon that has four forms. Each focused on a different stat." ,
                            weakness= "Dark" ,card_number= 186 ,release_date="2004-11-18", evolution_stage= "Basic" ,abilities= "Pressure")
        self.pokemon_cards.append(card20)
        card20.save()



    def create_trainers(self):

        trainer1 = Trainer(name="Ash", birthdate= "1987-05-22",location= "Pallet Town",email= "ash@pokemon.com")
        self.trainers.append(trainer1)
        trainer1.save()
        trainer2 = Trainer(name= "Gary",birthdate= "1984-08-06",location= "Pallet Town",email= "gary@pokemon.com")
        self.trainers.append(trainer2)
        trainer2.save()
        trainer3 = Trainer(name="Giovanni",birthdate= "1983-06-01",location= "Viridian City",email= "giovanni@teamrocket.com")
        self.trainers.append(trainer3)
        trainer3.save()
        trainer4 = Trainer(name="Silver",birthdate= "2007-12-24",location= "Johto City",email= "silver@pokemon.com")
        self.trainers.append(trainer4)
        trainer4.save()
        trainer5 = Trainer(name="Gold",birthdate= "2007-07-21",location= "Erika City",email= "Erika@pokemon.com")
        self.trainers.append(trainer5)
        trainer5.save()
        trainer6 = Trainer(name="Steven",birthdate= "1974-11-02",location= "Ever Grande City",email= "stevenstone@pokemon.com")
        self.trainers.append(trainer6)
        trainer6.save()
        trainer7 = Trainer(name="Roxanne",birthdate= "2005-07-02" ,location= "Rustboro City" ,email= "roxanne@pokemon.com" )
        self.trainers.append(trainer7)
        trainer7.save()
        trainer8 = Trainer(name="Aaron" ,birthdate= "2002-10-06" ,location= "Sinoh Region" ,email= "aaronelitefor@pokemon.com")
        self.trainers.append(trainer8)
        trainer8.save()
        trainer9 = Trainer(name="Ronald",birthdate= "2003-06-27",location= "Buncag Grounds",email= "ronaldpogi@pokemon.com")
        self.trainers.append(trainer9)
        trainer9.save()
        trainer10 = Trainer(name="Cedric" ,birthdate= "2004-06-02" ,location= "Bunkhose" ,email= "cedric@pokemon.com")
        self.trainers.append(trainer10)
        trainer10.save()

