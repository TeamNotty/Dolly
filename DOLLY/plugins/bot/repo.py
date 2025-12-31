from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DOLLY import app

start_txt = """
✰ 𝗪ᴇʟᴄᴏᴍᴇ ʜᴇ #ʀᴀɴᴅɪ ᴛᴇʀᴀ 
 
✰ 𝗥ᴇᴘᴏ ᴛᴏ 𝗡ʜɪ 𝗠ɪʟᴇɢᴀ 𝗬ʜᴀ
 
✰ 𝗣ᴀʜʟᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ 𝗥ᴇᴘᴏ 𝗢ᴡɴᴇʀ ᴋᴏ 

  
✰ || @INNOCENT_FUCKER ||
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""

@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔ᴅᴅ ᴍᴇ 𝗠ᴀʙʏ", url=f"https://t.me/{app.username}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛ᴇʟᴘ", url="https://t.me/NottySupport"),
          InlineKeyboardButton("⟵꯭꯭꯭꯭᪵〭〬𝐍ᴏᴛᴛʏ 𝐁ᴏʏ𓆪ꪾ !!͓", url="https://t.me/INNOCENT_FUCKER"),
          ],
               [
                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/NottySpace"),
],
[
InlineKeyboardButton("𝗠ᴀɪɴ 𝗕ᴏᴛ", url=f"https://t.me/DollyMusicBot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/c1ghwm.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
