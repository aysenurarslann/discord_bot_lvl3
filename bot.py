import discord
from discord.ext import commands
from database import init_db, add_task, delete_task, get_all_tasks, complete_task
import os

# Bot tokenini environment variable'dan al (güvenlik için)
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if not TOKEN:
    raise ValueError("DISCORD_BOT_TOKEN environment variable is not set!")

# Bot başlatma
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    init_db()  # Bot başladığında veritabanını kontrol et
    print(f"{bot.user.name} is online and connected to Discord.")

# !add_task <description>
@bot.command(name="add_task")
async def add_task_cmd(ctx, *, description: str):
    #Görev ekleme komutu"
    if not description.strip():
        await ctx.send("❌ Görev açıklaması boş olamaz. Lütfen bir metin girin.")
        return

    task_id = add_task(description.strip())
    await ctx.send(f"✅ Task added! To list all tasks use !show_tasks")

# !delete_task <task_id>
@bot.command(name="delete_task")
async def delete_task_cmd(ctx, task_id: int):
    #Görev silme komutu
    if delete_task(task_id):
        await ctx.send(f"🗑️ Task {task_id} deleted.")
    else:
        await ctx.send(f"❌ Task {task_id} not found or already deleted.")

# !show_tasks
@bot.command(name="show_tasks")
async def show_tasks_cmd(ctx):
    #Tüm görevleri listeleme komutu
    tasks = get_all_tasks()
    if not tasks:
        await ctx.send("📋 You have no tasks.")
        return

    response = "📋 Here is the list of tasks.\n"
    for tid, desc, completed in tasks:
        status = "√" if completed else "×"
        response += f"{tid}: {desc} (Completed: {status})\n"

    await ctx.send(response)

# !complete_task <task_id>
@bot.command(name="complete_task")
async def complete_task_cmd(ctx, task_id: int):
    #Görevi tamamlanmış olarak işaretle
    if complete_task(task_id):
        await ctx.send(f"🎉 Task {task_id} marked as completed.")
    else:
        await ctx.send(f"❌ Task {task_id} not found.")

# Hatalı komutlara yanıt
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ Lütfen komutu doğru biçimde girin. Örneğiin: `!add_task Buy milk`")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("❌ Geçersiz ID. Lütfen bir sayı giriin.")
    else:
        await ctx.send("❌ Bir hata oluştu. Lütfen tekrar deneyin.")

# Botu çalıştır
if __name__ == "__main__":
    bot.run(TOKEN)