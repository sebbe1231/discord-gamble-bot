import discord
from discord.ext import commands
import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS()")