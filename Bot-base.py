import random
import discord
from discord import app_commands
from discord.ext import commands

# Crée une instance du bot avec intents par défaut
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Événement déclenché quand le bot est prêt
@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user} (ID: {bot.user.id})")
    try:
        synced = await bot.tree.sync()
        print(f"Commandes slash synchronisées : {len(synced)}")
    except Exception as e:
        print(f"Erreur de synchronisation : {e}")

# 🎲 Commande /roll : lance un dé de 1 à 6
@bot.tree.command(name="roll", description="Lance un dé à 6 faces") # nom et description
async def roll(interaction: discord.Interaction):
    result = random.randint(1, 6) # action
    await interaction.response.send_message(f"🎲 Tu as lancé un **{result}** !") # reponse

# 🔐 Démarre le bot avec ton token
bot.run("TON_TOKEN_ICI")
