import discord

#id = client.get_guild(927606253797126194)
#id = client.get_guild(919635005200793630)
import discord 
client = discord.Client()



@client.event
async def on_message(message):
    if message.content.find('what is vote coin') != -1:
        await message.channel.send("hello there,The goal of this standard is to make the knowledge based pure democracy reality. This standard defines specification on how organization can propose voting, how organization can create trusted list of voters, how person can cast votes and how person can delegate other persons to vote on his behalf.The goal of these conventions is to make any organization who seeks public voting the standard on how to vote.Even if this standard is meant to be for algorand for the effeciency of the transactions and low transaction costs, it is not limitted to this blockchain. It can be used with any blockchain who support self transactions with specific payment, note field with at least 1000 bytes long message, and ability to search the network for specific transactions indexed by the amount, start of the note field, and/or the account.")



@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel)== 'general':
            await client.send_message(f"""Welcome to the vote coin server {member.mention}for more insights about vote coin type the command what is vote coin""")
client.run('OTI3NTI3MTE3NzMyODY4MTY2.YdLg8Q.tiWePcwvFvTxvDKN5LNwohu20yI')