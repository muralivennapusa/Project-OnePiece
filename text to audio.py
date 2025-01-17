import pyttsx3

def text_to_speech(text, output_file):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file)
    engine.runAndWait()

text = '''Episode 1

 Luffy is cast at sea in a barrel. Sailors on a passing cruise ship retrieve the barrel, but the ship is attacked with cannon fire by a nearby pirate ship, led by Alvida . The barrel is sent rolling into the kitchen. Once the cruise ship's sails have been destroyed, the Alvida Pirates board the ship to plunder its goods, and Alvida also forces one of her chore boys, Koby , to board the ship. Meanwhile, a girl takes advantage of the opportunity and sneaks aboard the Alvida Pirates' ship to steal its treasures . Koby and other pirates notice the barrel in the kitchen and find Luffy inside, who was sleeping. After Luffy defeats the hostile pirates, he goes with Koby to the pantry to eat the stored food . Luffy explains that he set sail to begin his pirating career, but his dinghy was destroyed by a whirlpool and he was left trapped at sea in a barrel. Koby explains that he was riding on a rowboat, but was kidnapped by the Alvida Pirates and forced to become a chore boy. He explains his desires to escape the Alvida Pirates some day and join the Marines . Alvida is informed of Luffy's presence, and, out of suspicion that he could be a bounty hunter , confronts him and Koby in the pantry. This triggers a battle on the ship, but Luffy defeats the pirates. Although Alvida is armed with a large spiked club, her attacks are rendered ineffective, as Luffy ate a Devil Fruit , granting him a superhuman ability that gives his body rubber-like properties . Using a Gomu Gomu no Pistol attack, Luffy defeats Alvida, sending her flying off the ship and into the sea. Having concluded the battle, Luffy boards a dinghy with Koby to continue his travels, catching a glimpse of the female burglar who was also departing the ship on her own dinghy. Luffy aims towards the Grand Line to search for the One Piece treasure but first looks to recruit the infamous Pirate Hunter Roronoa Zoro into his crew . 
'''
output_audio_file = text[:9]+".mp3"
print(output_audio_file)
text_to_speech(text, output_audio_file)
