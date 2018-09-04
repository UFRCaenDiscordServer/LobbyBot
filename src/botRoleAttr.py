import discord
TOKEN="NDg2NTY1NDYwMzczMTQzNTU1.DnA_Hg.TTIrR3-XCl9oa8B48mHTb6F7pxw"
cours=("info","informatique","math")
level=("l1","l2","l3","m1","m2","doctorant")
class BotAttr(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
        for chan in client.get_all_channels():
            if chan.name=="général":
                self.mainChan=chan

    async def on_member_join(self,member):
        msg="hi,"+member.name+" pour te voir attribuer ton role, ecris simplement L1,L2...M1...doctorant"
        await client.send_message(self.mainChan,msg)
        print(member)

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.channel==self.mainChan:
            content=message.content.lower()
            msg="vos roles ont était attribuée bienvenue à vous {0.author.mention}".format(message)
            roleEtudiant=discord.utils.get(message.server.roles,name="etudiant")
            if(content=="l3"):
                role=discord.utils.get(message.server.roles,name="L3")
                await client.add_roles(message.author,role,roleEtudiant)
                await client.send_message(message.channel,msg)
            elif(content=="l2"):
                role=discord.utils.get(message.server.roles,name="L2")
                await client.add_roles(message.author,role,roleEtudiant)
                await client.send_message(message.channel,msg)
            elif(content=="l1"):
                role=discord.utils.get(message.server.roles,name="L1")
                await client.add_roles(message.author,role,roleEtudiant)
                await client.send_message(message.channel,msg)
            elif(content=="M1"):
                role=discord.utils.get(message.server.roles,name="M1")
                await client.add_roles(message.author,role,roleEtudiant)
                await client.send_message(message.channel,msg)
            elif(content=="M2"):
                role=discord.utils.get(message.server.roles,name="M2")
                await client.add_roles(message.author,role,roleEtudiant)
                await client.send_message(message.channel,msg)

    def treatment(self,message):
        if(message in cours):
            pass
        else:
            scores=score(message)

    def score(self,message):
        listescore=[]
        for cour in cours:
            listescore.append(getscore(cour,message))
        return listescore

    def getscore(self,cour,message):
        pass

client = BotAttr()
client.run(TOKEN)
