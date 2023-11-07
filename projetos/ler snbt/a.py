# class chapter:
# 	def __init__(self):
# 		self.id = 0
# 		self.title = ""
# 		self.quests = []
#
#
# class quest:
# 	def __init__(self):
# 		self.id = 0
# 		self.title = ""
# 		self.subtitle = ""
# 		self.description = ""
#
#
# def extrair_valor(linha, chapter):
# 	if (linha.find('	id: ') > -1):
# 		print(linha.strip())
# 	elif (linha.find('	title: ') > -1):
# 		print(linha.strip())
#
#
# file = ""
# indentações = 1
# capitulo = chapter()
#
# with open("chapter_0_beginnings.snbt", "r") as f:
# 	file = f.read()
#
# linhas = file.splitlines()
#
# # for i, linha in zip(range(len(linhas)), linhas):
# # 	if (i == 0 or i == len(linhas) - 1):
# # 		continue
# # 	if (indentações == 1):
# # 		extrair_valor(linha, capitulo)
# #
# # 	# if (linha)
#
# def tem_valor(linha):
# 	if ('\t\t' in linha):
# 		return False
# 	if ('\tid: ' in linha):
# 		return True
# 	if ('\ttitle: ' in linha):
# 		return True
# 	if ('\tsubtitle: ' in linha):
# 		return True
# 	return False
#
# filtrado = list(filter(tem_valor, linhas))
#
# print(*filtrado, sep='\n')
import re

# Função para processar um bloco de dados
def processar_bloco(bloco):
    data = {}
    for match in re.finditer(r'(\w+):', bloco):
        chave = match.group(1)
        inicio = match.end()
        fim = bloco.find('\n', inicio)
        if fim == -1:
            valor = bloco[inicio:].strip()
        else:
            valor = bloco[inicio:fim].strip()

        # Verifique se o valor não é um bloco de subdados
        if "{" not in valor:
            data[chave] = valor

    # Definir "title" e "subtitle" como strings vazias se não estiverem definidos
    if "title" not in data:
        data["title"] = ""
    if "subtitle" not in data:
        data["subtitle"] = ""

    return data

# Texto com os dados do banco de dados
dados_do_banco = """
{
	x: 1.5d
	y: 0.5d
	subtitle: "You know how to punch trees, right? Before you get too invested in all the mods, if you're not sure what you're doing, just play some Minecraft. Build a house, build a farm, do the usual."
	id: "2F63FB9E8EAC18BD"
	tasks: [{
		id: "4C7985B45293CFD6"
		type: "item"
		item: "minecraft:crafting_table"
	}]
}
{
	title: "I can't wait to be an engineer!"
	x: 1.5d
	y: -2.5d
	subtitle: "Fair enough, here is some stuff to gather."
	dependencies: ["2F63FB9E8EAC18BD"]
	id: "4DCF01FE026F9FE5"
	tasks: [{
		id: "22BBF3F52AA5FE8A"
		type: "checkmark"
		title: "Preparations for Chapter 1"
	}]
}
{
	title: "Your first tasks"
	icon: "trade:deforesting_task_import"
	x: 3.0d
	y: -1.0d
	shape: "diamond"
	subtitle: "Getting started on making money"
	description: ["Tasks are great! Completing them can help you make lots of money! \\n\\nBut be aware: They usually cost a few Silver Coins and you never know what task you may be given! \\nThis one is for free to get you started."]
	optional: true
	id: "3580485A369D2795"
	tasks: [{
		id: "3101D6B5FEAA8648"
		type: "checkmark"
		title: "I understand"
	}]
	rewards: [
		{
			id: "300DF14CB8C12731"
			type: "choice"
			exclude_from_claim_all: true
			table_id: 4160806329156671821L
		}
		{
			id: "637C63C4CACDDDA1"
			type: "choice"
			exclude_from_claim_all: true
			table_id: 4160806329156671821L
		}
	]
}
{
	title: "Item grinding, useful for a variety of things."
	x: -2.0d
	y: 2.0d
	dependencies: ["69C0AE6714182D7F"]
	id: "6EC5AFB16BA0E63B"
	tasks: [{
		id: "1F7C1E2996B4EE70"
		type: "item"
		item: "create:millstone"
	}]
}
{
	title: "OP Smelting, Smoking and Washing"
	x: -4.0d
	y: 1.5d
	dependencies: ["69C0AE6714182D7F"]
	id: "6C385B4921836314"
	tasks: [{
		id: "2E24A52D1049497C"
		type: "item"
		item: "create:encased_fan"
	}]
}
{
	title: "Some SU appliances."
	x: -3.0d
	y: -4.5d
	subtitle: "Power has to come from somewhere."
	dependencies: ["6BBE4CCFE07312A9"]
	id: "59386F705AAD3CFF"
	tasks: [
		{
			id: "39D184A28D530276"
			type: "item"
			item: "create:water_wheel"
		}
		{
			id: "314C226FD196205E"
			type: "item"
			item: "create:large_water_wheel"
		}
		{
			id: "1A0FFD52A4045161"
			type: "item"
			item: "create:hand_crank"
		}
	]
}
{
	x: 3.0d
	y: -3.5d
	subtitle: "A bit of copper."
	dependencies: ["4DCF01FE026F9FE5"]
	id: "7130663AECB4C8B1"
	tasks: [{
		id: "3154EF31014FD0D4"
		type: "item"
		item: "minecraft:raw_copper"
	}]
}
{
	x: 0.0d
	y: -3.5d
	subtitle: "A necessity for making Andesite Alloy"
	dependencies: ["4DCF01FE026F9FE5"]
	id: "4D32217601DA01D6"
	tasks: [{
		id: "19D45730C479D6EC"
		type: "item"
		item: "minecraft:andesite"
	}]
}
{
	x: 2.5d
	y: -4.5d
	subtitle: "Lots of iron."
	dependencies: ["4DCF01FE026F9FE5"]
	id: "769ACE88C21CA4F9"
	tasks: [{
		id: "422E89159276969C"
		type: "item"
		item: "minecraft:raw_iron"
	}]
}
{
	x: 3.0d
	y: -2.5d
	subtitle: "Some zinc."
	dependencies: ["4DCF01FE026F9FE5"]
	id: "21DF66C5B03C191D"
	tasks: [{
		id: "67FC02DEC768DE95"
		type: "item"
		item: "create:raw_zinc"
	}]
}
{
	title: "What are these mods!? Im scared!!"
	x: 3.5d
	y: 0.5d
	subtitle: "A list of some mods you may have never encountered before."
	dependencies: ["2F63FB9E8EAC18BD"]
	id: "10DADBB2E6B7B7B5"
	tasks: [{
		id: "1CF568C2ADEFE8D9"
		type: "checkmark"
		title: "Stuff to Ignore!"
	}]
}
{
	icon: "ars_nouveau:creative_spell_book"
	x: 4.5d
	y: -0.5d
	subtitle: "A spell based magic mod"
	description: [
		"Ars Nouveau is a mod dedicated to modern magic, featuring spells and familiars.\\n"
		"This mod will only become relevant in the later stages of the pack, and you won't need an in-depth understanding of its mechanics. \\n"
		"Some of its plants are useful in the early magic progression, like sourceberries and mageblooms. \\nYou'll figure out what they do later :)"
	]
	dependencies: ["10DADBB2E6B7B7B5"]
	id: "0F7ADBD455574DA8"
	tasks: [{
		id: "201D4D788B943D77"
		type: "checkmark"
		title: "Ars Nouveau"
	}]
}
{
	icon: "pneumaticcraft:thermopneumatic_processing_plant"
	x: 4.5d
	y: 1.5d
	subtitle: "Pressure driven technology"
	description: ["Pneumaticcraft centers around generating and utilizing pressure.\\n\\nThe significance of the mod will become apparent in later stages, but you won't have to worry about it for the first two chapters.\\n\\n\\nWhen you do start working with the mod, there are three things for you to remember:\\n\\n1. Do not let your machines reach a pressure too high for them if they are missing a security upgrade, or they may explode.\\n\\n2. Don't leave any open ends on your pressure tubes, or the pressure will escape instead of building up\\n\\n3. Blocks that aren't surrounded by others will be cooled down by the air temperature around them."]
	dependencies: ["10DADBB2E6B7B7B5"]
	id: "520425F3AFA5599F"
	tasks: [{
		id: "153B106F8A7C6DF8"
		type: "checkmark"
		title: "Pneumaticcraft"
	}]
	rewards: [{
		id: "18FDA15F78E05D25"
		type: "item"
		item: "pneumaticcraft:security_upgrade"
	}]
}
{
	icon: "kubejs:integrational_mechanism"
	x: 5.5d
	y: -0.5d
	subtitle: "The glue making this pack possible"
	description: [
		"KubeJS is a mod that significantly simplifies the process of creating a modpack by allowing creators to add custom items and unique interactions without the need for a full mod.\\n"
		"If you come across an item attributed to KubeJS, it's likely to be crucial for the packs progression."
	]
	dependencies: ["10DADBB2E6B7B7B5"]
	id: "34312A4E0AFAD769"
	tasks: [{
		id: "30B3270A916D1913"
		type: "checkmark"
		title: "KubeJS"
	}]
}
{
	icon: "cae:skystone_catalyst"
	x: 5.5d
	y: 1.5d
	subtitle: "Or short, CAE"
	description: [
		"Create Arcane Engineering is the name of the core mod of this modpack. "
		""
		"The mod features custom blocks for automating Skystone and Create Orestones. "
		""
		"Some of its content only becomes relevant for the end of the pack."
	]
	dependencies: ["10DADBB2E6B7B7B5"]
	id: "4BB71BE656192C7F"
	tasks: [{
		id: "712E9828CEC53555"
		type: "checkmark"
		title: "Create Arcane Engineering"
	}]
}
{
	x: 1.5d
	y: -5.0d
	subtitle: "Chapter 1 requires you to farm Menril Trees."
	dependencies: ["4DCF01FE026F9FE5"]
	id: "20B2A8D54DD091A1"
	tasks: [{
		id: "34055C39C54686D8"
		type: "item"
		item: "integrateddynamics:menril_sapling"
	}]
}
{
	x: 0.5d
	y: -4.5d
	subtitle: "You can make Andesite Alloy with it"
	dependencies: ["4DCF01FE026F9FE5"]
	id: "227004D221260FC2"
	tasks: [{
		id: "6EE07361D3AC8E90"
		type: "item"
		item: "integrateddynamics:crystalized_menril_chunk"
	}]
}
{
	x: 1.5d
	y: 2.5d
	subtitle: "Here are the items you'll need to get started, and once you begin, there's no turning back! 12121!!"
	dependencies: ["2F63FB9E8EAC18BD"]
	id: "749112B711CAB183"
	tasks: [{
		id: "54FF171FC21767DA"
		type: "checkmark"
		title: "I cant wait to become a cool mage!"
	}]
}
{
	x: 0.0d
	y: 0.5d
	dependencies: ["2F63FB9E8EAC18BD"]
	id: "438CB39142A72E71"
	tasks: [{
		id: "3309E6DC2F78649F"
		type: "checkmark"
		title: "Let's get a basic workshop going!"
	}]
}
{
	icon: "minecraft:chorus_fruit"
	x: 6.5d
	y: 1.5d
	subtitle: "More recipe utility"
	description: [
		"A utility mod for modpack devs that provides in-world recipes, like dropping items in fluids etc. "
		""
		"Nothing for you to worry about."
	]
	dependencies: ["10DADBB2E6B7B7B5"]
	id: "03A3E838913EDD49"
	tasks: [{
		id: "00CA845E07229A7E"
		type: "checkmark"
		title: "Lychee"
	}]
}
{
	icon: {
		id: "tconstruct:smeltery_controller"
		Count: 1b
		tag: {
			texture: "tconstruct:seared_bricks"
		}
	}
	x: 6.5d
	y: -0.5d
	subtitle: "Tool crafting and ore doubling"
	description: [
		"Tinker's Construct is a tool/equipment mod that revolves around smelteries and liquid metals.\\n"
		"It allows you to melt a variety of items and even entities into liquids. \\n"
		"Tinkers' Construct is primarily focused on creating highly useful tools by combining a diverse selection of materials.\\n"
		"It also allows you to double ores by melting their raw form.\\n"
		"This mod gains importance in Chapter 2, making it worth exploring."
	]
	dependencies: ["10DADBB2E6B7B7B5"]
	id: "4D411D9BCE1D33F2"
	tasks: [{
		id: "19A69F0A95E68D12"
		type: "checkmark"
		title: "Tinkers Construct"
	}]
}
{
	icon: "integrateddynamics:logic_programmer"
	x: 7.5d
	y: -0.5d
	subtitle: "A Solution to problems that didn't need solving"
	description: [
		"Integrated Dynamics is a magic-tech mod that primarily focuses on logic and offers a highly modular approach to programming. "
		""
		"There's no need for you to be concerned about its complex programming capabilities in this modpack though. "
		""
		"Here, Integrated Dynamics is mainly used for its Trees, and provides a storage solution before you unlock AE2."
	]
	dependencies: ["10DADBB2E6B7B7B5"]
	id: "74296D4CEDEA44AA"
	tasks: [{
		id: "633DC26121E79E2C"
		type: "checkmark"
		title: "Integrated Dynamics"
	}]
}
{
	icon: {
		id: "forbidden_arcanus:eternal_stella"
		Count: 1b
		tag: { }
	}
	x: 7.5d
	y: 1.5d
	subtitle: "Cool items utilized in progression"
	description: [
		"Forbidden and Arcanus is a magic mod that revolves around a wide range of magic-related items, each possessing their own unique quirks."
		""
		"Its most complicated feature is a multiblock called the \"Hephaestus Forge\". "
		"It will become relevant once you progress further in the game. "
		""
		"Rest assured that we provide comprehensive explanations for the mechanics and features when they come into play."
	]
	dependencies: ["10DADBB2E6B7B7B5"]
	id: "6FC749E2772DFD45"
	tasks: [{
		id: "13C0B18FD0FF6712"
		type: "checkmark"
		title: "Forbidden and Arcanus"
	}]
}
{
	title: "EZ Tree Chopping"
	x: -3.0d
	y: 2.0d
	dependencies: ["69C0AE6714182D7F"]
	id: "2E9BC6F50E8EAA67"
	tasks: [{
		id: "39DF16CAF546859B"
		type: "item"
		item: "create:mechanical_saw"
	}]
}
{
	x: -4.5d
	y: 0.5d
	dependencies: ["69C0AE6714182D7F"]
	id: "3109A6F2EA23F755"
	tasks: [{
		id: "07AD9B6C6DE070BC"
		type: "item"
		item: "create:mechanical_press"
	}]
}
{
	title: "Doubling Andesite Alloy rates."
	x: -4.5d
	y: -0.5d
	dependencies: ["69C0AE6714182D7F"]
	id: "7B1516AB858E84A1"
	tasks: [{
		id: "580C71401BD4E729"
		type: "item"
		item: "create:mechanical_mixer"
	}]
}
{
	x: 0.0d
	y: -2.5d
	subtitle: "You can make Andesite Alloy with it"
	dependencies: ["4DCF01FE026F9FE5"]
	id: "02EE7F0461B0DFBF"
	tasks: [{
		id: "43E18E94A86CB728"
		type: "item"
		item: "minecraft:diorite"
	}]
}
{
	x: 1.0d
	y: 3.5d
	dependencies: ["749112B711CAB183"]
	id: "3F2F651C5B2E8758"
	tasks: [{
		id: "1F8C791C489E3939"
		type: "item"
		item: "create:spout"
	}]
}
{
	x: 0.0d
	y: 3.5d
	dependencies: ["749112B711CAB183"]
	id: "16C84D39BB2CA23B"
	tasks: [{
		id: "2644512E661BB3A2"
		type: "item"
		title: "Any #quark:corundum"
		item: {
			id: "itemfilters:tag"
			Count: 1b
			tag: {
				value: "quark:corundum"
			}
		}
	}]
}
{
	x: 3.0d
	y: 3.5d
	dependencies: ["749112B711CAB183"]
	id: "159959902CC20D5F"
	tasks: [{
		id: "44787DDD37836FA1"
		type: "item"
		item: "forbidden_arcanus:rune"
	}]
}
{
	x: 2.0d
	y: 3.5d
	subtitle: "How do i get Brass!?"
	description: ["Chapter 1 will explain it to you :)"]
	dependencies: ["749112B711CAB183"]
	id: "17A07FB16A28912B"
	tasks: [{
		id: "3BD2EFBAAF31BF98"
		type: "item"
		item: "create:deployer"
	}]
}
{
	x: -1.5d
	y: -3.5d
	subtitle: "Better results from Mixing!"
	dependencies: [
		"4D32217601DA01D6"
		"02EE7F0461B0DFBF"
		"227004D221260FC2"
	]
	dependency_requirement: "one_completed"
	id: "6BBE4CCFE07312A9"
	tasks: [{
		id: "1CFC5555401D0935"
		type: "item"
		item: "create:andesite_alloy"
	}]
	rewards: [{
		id: "226094148D432E4A"
		type: "item"
		item: "create:andesite_alloy"
		count: 24
	}]
}
{
	title: "A Lootbox"
	icon: {
		id: "kubejs:lootbag_create_andesite"
		Count: 1b
		tag: {
			Damage: 0
		}
	}
	x: -3.0d
	y: -1.5d
	description: [
		"This pack often rewards you for completing a Quest."
		""
		"Rewards come in the form of Lootbags that can be opened by right clicking."
		""
		"Lootboxes can also be enchanted with Fortune for a great increase in loot"
	]
	dependencies: ["69C0AE6714182D7F"]
	id: "196FA47058E902CB"
	tasks: [{
		id: "276E7721997ED799"
		type: "checkmark"
		title: "Give me some loot!"
	}]
	rewards: [{
		id: "10A9565D6D029AC9"
		type: "item"
		item: {
			id: "kubejs:lootbag_create_andesite"
			Count: 1b
			tag: {
				Damage: 0
			}
		}
	}]
}
{
	x: -1.5d
	y: 0.5d
	description: [
		"These Mechanisms are only makeshift! "
		""
		"You won't be able to upgrade them to brass!"
	]
	dependencies: [
		"438CB39142A72E71"
		"6BBE4CCFE07312A9"
	]
	id: "3D141A6E5FFFA073"
	tasks: [{
		id: "2C0F62720CBB555B"
		type: "item"
		item: "kubejs:makeshift_kinetic_mechanism"
	}]
}
{
	title: "Your first Machine"
	x: -3.0d
	y: 0.5d
	subtitle: "Many more to come"
	dependencies: ["3D141A6E5FFFA073"]
	id: "69C0AE6714182D7F"
	tasks: [{
		id: "78342DA7ED9D039D"
		type: "item"
		item: "kubejs:andesite_machine"
	}]
}
{
	x: 0.0d
	y: -1.0d
	subtitle: "An easy way to find resources for Andesite Alloy"
	description: [
		"The Alloy Scanner looks for andesite and diorite in a chunk and reports their coordinates to you."
		""
		"But be aware: The scanner will give you the lowest position it found them on."
		"Manually looking may allow you to find them faster."
	]
	id: "7619CD089994659A"
	tasks: [{
		id: "3C549513F034D725"
		type: "item"
		item: "kubejs:alloy_radar"
	}]
}

"""

# Separar os blocos de dados
blocos = re.findall(r'{(.*?)}', dados_do_banco, re.DOTALL)

# Inicializar uma lista para armazenar os dados extraídos
lista_de_dados = []

# Processar cada bloco e extrair os valores
for bloco in blocos:
    data = processar_bloco(bloco)
    lista_de_dados.append(data)

# Imprimir a lista de dados extraídos
for item in lista_de_dados:
    print(item['id'], item['title'], item['subtitle'])
