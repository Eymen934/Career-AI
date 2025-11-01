# Gereksinimler: pip install discord.py aiosqlite openai SpeechRecognition
import discord
from discord.ext import commands
from discord.ui import Button, View
import aiosqlite
from config import DISCORD_TOKEN
import speech_recognition as sr
import openai
import asyncio

# Bot ayarları
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

WELCOME_CHANNEL_ID = 1402284044489855039  # Mesaj gönderilecek kanal

# 🔹 OpenAI API Key
openai.api_key = "OPENAI_API_KEYİNİ_BURAYA_YAZ"

# 🔹 Yapay zekalı meslek tahmini
def meslek_tespiti(transcript: str) -> str:
    prompt = f"Bir kişi şöyle dedi: '{transcript}'. Bu kişi hangi meslekle ilgileniyor olabilir? Kısa ve net cevap ver."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return str(response.choices[0].message['content'])
    except Exception as e:
        print(f"OpenAI hatası: {e}")
        return "Meslek tahmini yapılamadı."

# 🔹 Kategoriler için butonlar
class MeslekCategoryButtons(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.categories = [
            ("Tasarım", "tasarim_meslekler"),
            ("Programlama", "programlama_meslekler"),
            ("Eğitim-Öğretim", "egitim_ogretim_meslekler"),
            ("Doktorluk", "doktorluk_kategorisinden_meslekler"),
            ("Mühendislik", "muhendislik_kategorisinden_meslekler"),
            ("Sanat", "sanat_meslekleri")
        ]
        for label, table_name in self.categories:
            button = Button(label=label, style=discord.ButtonStyle.primary)
            button.callback = self.create_callback(label, table_name)
            self.add_item(button)

    def create_callback(self, label, table_name):
        async def callback(interaction: discord.Interaction):
            async with aiosqlite.connect("meslekler.db") as db:
                cursor = await db.execute(f"SELECT meslek, aciklama FROM {table_name}")
                rows = await cursor.fetchall()
                await cursor.close()

            if not rows:
                await interaction.response.send_message(
                    f"Bu kategoride meslek bulunamadı.", ephemeral=True
                )
                return

            message = f"**{label} kategorisindeki meslekler:**\n\n"
            for meslek, aciklama in rows:
                message += f"**{meslek}:** {aciklama}\n"
            message += "\n**Diğerlerini de incelemeyi unutma!**"

            view = MeslekCategoryButtons()
            await interaction.response.send_message(message, view=view, ephemeral=True)

        return callback

# 🔹 Başlangıç Kılavuzu Butonu
class BaslangicKlavuzuButton(View):
    def __init__(self):
        super().__init__(timeout=None)
        button = Button(label="Başlangıç Kılavuzu İndir", style=discord.ButtonStyle.success)
        button.callback = self.download_pdf
        self.add_item(button)

    async def download_pdf(self, interaction: discord.Interaction):
        pdf_path = "Career AI - Meslek Seçiminde Önemli Unsurlar.pdf"
        try:
            # İlk olarak bir "düşünme" yanıtı gönder
            await interaction.response.defer(ephemeral=True)

            # PDF dosyasını gönder
            with open(pdf_path, "rb") as f:
                await interaction.followup.send(
                    content="📄 Başlangıç Kılavuzunu indiriyorsunuz...",
                    file=discord.File(f),
                    ephemeral=True
                )
        except Exception as e:
            await interaction.followup.send(
                content=f"❌ PDF dosyası bulunamadı: {e}",
                ephemeral=True
            )

# 🔹 Komut: kategorileri göster
@bot.command()
async def meslekler(ctx):
    view = MeslekCategoryButtons()
    await ctx.send("Bir kategori seçerek meslekleri görebilirsin:", view=view)

# 🔹 Meslek açıklaması fonksiyonu
async def meslek_aciklama_ara(channel, kelime):
    async with aiosqlite.connect("meslekler.db") as db:
        cursor = await db.execute(
            "SELECT aciklama FROM tasarim_meslekler WHERE meslek = ? "
            "UNION SELECT aciklama FROM programlama_meslekler WHERE meslek = ? "
            "UNION SELECT aciklama FROM egitim_ogretim_meslekler WHERE meslek = ? "
            "UNION SELECT aciklama FROM doktorluk_kategorisinden_meslekler WHERE meslek = ? "
            "UNION SELECT aciklama FROM muhendislik_kategorisinden_meslekler WHERE meslek = ? "
            "UNION SELECT aciklama FROM sanat_meslekleri WHERE meslek = ?",
            (kelime, kelime, kelime, kelime, kelime, kelime)
        )
        row = await cursor.fetchone()
        await cursor.close()

    if row:
        await channel.send(
            f"İlgilendiğiniz meslek: **{kelime}**\n"
            f"Açıklama: {row[0]}\n"
            f"💡 Bu mesleğe nasıl ilerleyebileceğinizi size gösterebilirim!"
        )
    else:
        await channel.send(
            f"İlgilendiğiniz meslek: **{kelime}**\n"
            "Üzgünüm, bu meslek hakkında bir bilgi bulamadım. Ama birlikte araştırabiliriz!"
        )

# 🔹 Ses dinleme fonksiyonu
def ses_dinle():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        transcript = recognizer.recognize_google(audio, language="tr-TR")
        return transcript
    except sr.UnknownValueError:
        return ""
    except Exception as e:
        print(f"Ses tanıma hatası: {e}")
        return ""

# 🔹 Sesli komut
@bot.command()
async def dinle(ctx):
    await ctx.send("🎤 Konuşun, sizi dinliyorum...")

    loop = asyncio.get_event_loop()
    transcript = await loop.run_in_executor(None, ses_dinle)

    if not transcript:
        await ctx.send("Sesi anlayamadım, lütfen tekrar deneyin.")
        return

    meslek = meslek_tespiti(transcript)
    await meslek_aciklama_ara(ctx.channel, meslek)

# 🔹 Bot hazır olduğunda
@bot.event
async def on_ready():
    print(f"✅ Bot aktif: {bot.user}")
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        try:
            view = BaslangicKlavuzuButton()  # PDF butonu
            await channel.send(
                "**Merhaba! Ben Career AI, kişisel kariyer rehberin.** 😎\n"
                "**Kullanım Talimatları:**\n"
                "1. Sesli komutlar için `!dinle` komutunu kullanın ve konuşun.\n"
                "2. Meslek kategorilerinden birini seçip kendine uygun meslekleri görmek için, `!meslekler` komutunu kullanın.\n\n"
                "Doğrudan bir meslek yazıp açıklamasını görebilirsin(Veri tabanında yazdığın meslek var ise)!\n\n"
                "**Başarılar dilerim!** 🎯",
                view=view
            )
        except Exception as e:
            print(f"❌ Mesaj gönderilemedi: {e}")
    else:
        print(f"❌ Kanal bulunamadı! Kanal ID'sini kontrol edin: {WELCOME_CHANNEL_ID}")

# 🔹 Botu başlat
bot.run(DISCORD_TOKEN)
