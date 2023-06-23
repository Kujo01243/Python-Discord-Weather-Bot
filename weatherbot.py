import discord
from wetterabfrage import *
from globale_funktionen import *
from time import sleep
########################################################################################
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
commandstarter1 = weatherbotstarter()
pushstarter1 = pushbotstarter()


@client.event

async def on_message(message):
    if message.author == client.user:
        return
    ##########################################################################
    #pushbot
    if message.content.startswith(pushstarter1) and message.author != client.user:
        loop = 0
        pushort = message.content.replace(pushstarter1, "")
        if len(pushort) < 1:
            embed = discord.Embed(title="Error", description=errortext(), color=0xFF0000)
            await message.channel.send(embed=embed)
        else:
            temp = getWeather(pushort)[8]
            embed = discord.Embed(title="Pushbot acticated",description="Du wirst benachrichtigt, wenn die Temperatur in " + getWeather(pushort)[0] + " unter 0°C sinkt. Aktuell liegt die Termperatur bei: " + str(temp) + "°C" , url=getweathersource(getWeather(pushort)[9]), color=0x00ff00)
            embed.set_author(name="google maps", url=getgoogleplace(getWeather(pushort)[0]),icon_url=mapsicon())
            embed.set_footer(text=apisource())
            await message.channel.send(embed=embed)
            while loop == 0:
                temp = getWeather(pushort)[8]
                if temp < 0:
                    embed = discord.Embed(title="Minusgrade!!!",description="Hey, in " + getWeather(pushort)[0] + " ist die Temperatur unter 0°C gesunken. Die Pushmeldung wurde beendet. (aktuelle Temperatur: " + str(temp) + "°C)" ,url=getweathersource(getWeather(pushort)[9]), color=0x0088ff)
                    embed.set_author(name="google maps", url=getgoogleplace(getWeather(pushort)[0]),icon_url=mapsicon())
                    embed.set_footer(text=apisource())
                    await message.channel.send(embed=embed)
                    loop = 1
                else:
                    sleep(5)
                    await client.get_channel(timeoutchannel()).send("notimeout")



    ##########################################################################
    #help
    if message.content.startswith(help1()) or message.content.startswith(help2()) and message.author != client.user:
        embed = discord.Embed(title="Hilfe", color=0xffff00)
        embed.add_field(name="Hilfe erhalten:", value="Mit den beiden Eingaben \"" + help1() + "\" und \"" + help2() + "\" rufst du dir diese Nachricht auf.", inline=False)
        embed.add_field(name="Wetterabfrage:", value="Mit der Eingabe \"" + weatherbotstarter() + " <Ort>\" kannst du dir das Wetter für einen Ort anzeigen", inline=True)
        embed.add_field(name="Pushbenachrichtigung:", value="Mit der Eingabe \"" + pushbotstarter() + " <Ort>\" kannst du dich benachrichten lassen, wenn das Wetter an deinem Ort unter null Grad Celsius sinkt.", inline=True)
        await message.channel.send(embed=embed)


    ##########################################################################
    #weatherbot
    if message.content.startswith(commandstarter1) and message.author != client.user:       #in eine funktion packen und dann auf weitere Eingabemöglichkeiten überprüfen
        eingabeort = message.content.replace(commandstarter1, "")
        eingabeort = eingabeort.lower()
        if len(eingabeort) < 1:
            embed = discord.Embed(title="Error", description=errortext(), color=0xFF0000)
            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="Wetter", url=getweathersource(getWeather(eingabeort)[9]) , color=0x00ff00)
            embed.add_field(name="Ort und Land:", value=getWeather(eingabeort)[0] + ", " + getWeather(eingabeort)[1], inline=False)
            embed.add_field(name="Temperatur:", value=getWeather(eingabeort)[2] + "°C", inline=True)
            embed.add_field(name="Luftdruck:", value=getWeather(eingabeort)[3] + "mBar", inline=True)
            embed.add_field(name="Luftfäuchtigkeit:", value=getWeather(eingabeort)[4] + "%", inline=True)
            embed.add_field(name="Himmel:", value=getWeather(eingabeort)[5], inline=True)
            embed.add_field(name="Windgeschwindigkeit:", value=getWeather(eingabeort)[6] + "m/s", inline=True)
            embed.add_field(name="Windrichtung:", value=getWeather(eingabeort)[7] + "°", inline=True)
            embed.set_author(name="google maps", url=getgoogleplace(getWeather(eingabeort)[0]),icon_url=mapsicon())
            embed.set_footer(text=apisource())
            await message.channel.send(embed=embed)

client.run(get_token())
