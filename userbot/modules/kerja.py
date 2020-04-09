import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP
from userbot.events import register



@register(outgoing=True, pattern='^.demo(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Untuk melihat List Demo`")
	sleep(2)
	await typew.edit("`demo.senturypanel.xyz`")
	sleep(1)
	await typew.edit("`Untuk melihat tampilan yang di inginkan\n Silahkan cek`\n https://demo.senturypanel.xyz \n#SenturyBot")


# Create by myself @JejakCheat

@register(outgoing=True, pattern='^.sibuk(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Sebentar Ya Gan`")
	sleep(2)
	await typew.edit("`Masih Ngecek`")
	sleep(1)
	await typew.edit("`Oh Ternyata Jefa Masih sibuk... Tunggu sebentar nanti akan dibaca \n#SenturyBot`")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.o(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Hai Halo Bosku`")
	sleep(2)
	await typew.edit("`Gw udah online`")
	sleep(1)
	await typew.edit("`Maaf baru online, ada apa bos?` \n#SenturyBot")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.oid(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Hai Halo Bosku`")
	sleep(2)
	await typew.edit("`Kalau mau Servis Web silahkan kirim OIDnya`")
	sleep(1)
	await typew.edit("`Kirim ORDER ID nya bos kalau mau servis/perpanjang` \nBot By : [#Jefanya](t.me/JejakCheat)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.bca(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Hai Halo Bosku`")
	sleep(2)
	await typew.edit("`Payment Via BCA YA`")
	sleep(1)
	await typew.edit("`BCA :`0901316839 `A/N PILU EFENDI` \nSertakan Bukti Transfer Ya (Wajib) Untuk melanjutkan transaksi \nBot By : [#JefanyaBot](t.me/JejakCheat)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.tsel(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Hai Halo Bosku`")
	sleep(2)
	await typew.edit("`Payment Via TELKOMSEL YA`")
	sleep(1)
	await typew.edit("`TELKOMSEL :`082247870713 `A/N -` \nSertakan Bukti Transfer Ya (Wajib) Untuk melanjutkan transaksi \nBot By : [#JefanyaBot](t.me/JejakCheat)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.bni(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Hai Halo Bosku`")
	sleep(2)
	await typew.edit("`Payment Via BNI YA`")
	sleep(1)
	await typew.edit("`BNI :`0830301026 `A/N Jefanya Efandchris` \nSertakan Bukti Transfer Ya (Wajib) Untuk melanjutkan transaksi \nBot By : [#JefanyaBot](t.me/JejakCheat)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.ovo(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Hai Halo Bosku`")
	sleep(2)
	await typew.edit("`Payment Via OVO YA`")
	sleep(1)
	await typew.edit("`OVO :`082247870713 `A/N NI KETUT SUERTI` \nSertakan Bukti Transfer Ya (Wajib) Untuk melanjutkan transaksi \nBot By : [#JefanyaBot](t.me/JejakCheat)")

# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.danaj(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Hai Halo Bosku`")
	sleep(2)
	await typew.edit("`Payment Via DANA YA`")
	sleep(1)
	await typew.edit("`DANA :`085320064310 `A/N Sutri nanda` \nSertakan Bukti Transfer Ya (Wajib) Untuk melanjutkan transaksi \nBot By : [#JefanyaBot](t.me/JejakCheat)")

# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.bcaj(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Hai Halo Bosku`")
	sleep(2)
	await typew.edit("`Payment Via BCA YA`")
	sleep(1)
	await typew.edit("`BCA :`3030634780 `A/N Sutri nanda` \nSertakan Bukti Transfer Ya (Wajib) Untuk melanjutkan transaksi \n[#JefanyaBot](t.me/JejakCheat)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.dana(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Hai Halo Bosku`")
	sleep(2)
	await typew.edit("`Payment Via DANA YA`")
	sleep(1)
	await typew.edit("`DANA :`082247870713` A/N Jefanya Efandchris` \nSertakan Bukti Transfer Ya (Wajib) Untuk melanjutkan transaksi \nBot By : [#JefanyaBot](t.me/JejakCheat)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.data(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Hai Halo Bosku`")
	sleep(2)
	await typew.edit("`Tolong Kirim Data Ya`")
	sleep(1)
	await typew.edit("`Kirim Email + Tampilan yang sudah di request di atas` (Sesuai nama di demo.senturypanel.xyz) \nBot By : [#JefanyaBot](t.me/JejakCheat)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.harga(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Hai Halo Bosku`")
	sleep(2)
	await typew.edit("`Saya Kirim Data Ya`")
	sleep(1)
	await typew.edit("`UPDATE HARGA HARI INI` \n\nDOMAIN : 150.000 (Bisa Request Nama Web) \nDOMAIN : 70.000 (Tidak Bisa Request Nama Web) \nSUBDOMAIN : 20.000 (SELAIN PULSA) \nSUBDOMAIN : 25.000 (Via Pulsa) \n\nSetuju ? Balas `yes` Tidak Setuju balas `no` \n\nBot By : [#JefanyaBot](t.me/JejakCheat)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.bug(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Starting Bot ...`\n#SenturyBot")
	sleep(2)
	await typew.edit("`Bot Is Online`\n#SenturyBot")
	sleep(1)
	await typew.edit("`JIKA ADA ERROR ATAU BUG DI TAMPILAN PHISING KALIAN TINGGAL SURUH TEMAN KALIAN UNTUK MEMBUKA WEB KALIAN ITU \n\nSyarat : \n1. BEDA HP \n2. BEDA SINYAL \n3. BELUM PERNAH BUKA WEB ITU`\nBot By : [#JefanyaBot](t.me/JejakCheat)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.exp(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Starting Bot ...`\n#SenturyBot")
	sleep(2)
	await typew.edit("`Bot Is Online`\n#SenturyBot")
	sleep(1)
	await typew.edit("**EXP TIME !!** \nMaaf bos, phising saya matikan atau saya alihkan ke `exp.senturypanel.xyz` \nDikarenakan Sudah melewati tanggal kadaluarsa \nDan jika mau perpanjang silahkan balas pesan ini dengan **Yes** \nDan jika tidak mau perpanjang silahkan balas **No** \nBot By : [#JefanyaBot](t.me/JejakCheat)")


# Create by myself @JejakCheat
CMD_HELP.update({
    "done":
    "`.domainanim` = `DOMAIN` PUBG Mobile Season 12 `Animation Version`\n"
    "`.domaintourney` = `DOMAIN` PUBG Mobile Season 12 `Tournament`\n"
    "`.subdomainanim` = `SUBDOMAIN` PUBG Mobile Season 12 `Animation Version`"
    "`.subdomaintourney` = `SUBDOMAIN` PUBG Mobile Season 12 `Tournament`"
    "`.subdomainbokep1` = `SUBDOMAIN` Facebok Bokep `V1`"
    
})

