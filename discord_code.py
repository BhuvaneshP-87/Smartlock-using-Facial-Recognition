import discord
from recognise_faces import *
from emergency_recorder import *

client = discord.Client()

isUltimate=True
isOpen=True

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
async def send_entry(entry_data):
        global isOpen
        channel=client.get_channel(847411536515301376)
        if entry_data[3]:
            msg = ''.join(["You had a visitor! ",str(entry_data[2])," checked in at ",str(entry_data[1])])
        else:
            msg = ''.join(["Unrecognised person attempted to enter at ",str(entry_data[1])])
        await channel.send(msg)
        await channel.send(file=discord.File(entry_data[0]))
        isOpen=True
        
async def send_emergency_recording(emergency_data):
        channel=client.get_channel(847395336367767572)
        msg="Recorded at, "+emergency_data[1]
        await channel.send(msg)
        await channel.send(file=discord.File(emergency_data[0]))
        
    
@client.event
async def on_message(message):
    
    global isOpen,isEmergency,isUltimate
    msg = message.content

    if message.author == client.user:
        return

    if msg.startswith('ALLOW'):
        isOpen=True
        await message.channel.send("Access granted. Welcome home and make yourself comfortable!")
        

    if msg.startswith('CLOSE'):
        isOpen=False
        await message.channel.send("Door locked. Don't worry, I've got your back!")
        if isUltimate and not isOpen:
            temp=await recognise_face()
            await send_entry(temp)
        

    if msg.startswith('EMERGENCY'):
        await message.channel.send("Alert! Someone suspicious lurks about- check the video sent to see if you recognise them.")
        temp=await emergency_recording()
        await send_emergency_recording(temp)
        

    if msg.startswith('ULTIMATE-ON'):
        isUltimate=True
        await message.channel.send("The face recognition feature at the door will be disabled until further notice.")
        

    if msg.startswith('ULTIMATE-OFF'):
        isUltimate=False
        await message.channel.send("The face recognition feature at the door has been successfully enabled.")
    
        
client.run(token)                                





