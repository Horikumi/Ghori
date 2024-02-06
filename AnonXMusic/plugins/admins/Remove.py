from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message, CallbackQuery

import config
from config import BANNED_USERS, adminlist
from AnonXMusic import app, YouTube
from AnonXMusic.core.call import Anony
from AnonXMusic.misc import db, SUDOERS
from AnonXMusic.utils.database import get_loop, is_active_chat
from AnonXMusic.utils.decorators import languageCB 
from AnonXMusic.utils.stream.autoclear import auto_clean
from AnonXMusic.utils.inline import close_markup, stream_markup
from AnonXMusic.utils.thumbnails import get_thumb
                                              

@app.on_callback_query(filters.regex("ClearSong") & ~BANNED_USERS)
@languageCB
async def rm_song(client, CallbackQuery, _):
                callback_data = CallbackQuery.data.strip()
                callback_request = callback_data.split(None, 1)[1]
                musicid, user_id, chat_id = callback_request.split("|")
                mention = CallbackQuery.from_user.mention
                chat_id = int(chat_id)
                vid = str(musicid)
                if not await is_active_chat(chat_id):
                      return await CallbackQuery.answer(
                      _["general_5"], show_alert=True
                ) 
                if CallbackQuery.from_user.id not in SUDOERS:
                       if CallbackQuery.from_user.id != int(user_id):
                           admins = adminlist.get(CallbackQuery.message.chat.id)
                           if not admins:
                               return await CallbackQuery.answer(
                                  _["admin_13"], show_alert=True
                )
                           else:
                              if CallbackQuery.from_user.id not in admins:
                                  return await CallbackQuery.answer(
                                   _["remove_8"], show_alert=True
                    )   
                loop = await get_loop(chat_id)
                if loop != 0:
                    return await CallbackQuery.answer(_["admin_8"], show_alert=True)
                else:
                    pass
                check = db.get(chat_id)
                if check:
                        count = len(check)
                        acha = None               
                        try:
                             for help in range(count):
                               try:         
                                 if  vid == check[help]["musicid"]:
                                    acha = help
                               except:
                                  break
                        except:
                             return await CallbackQuery.answer(_["remove_10"], show_alert=True)
                else:
                      return await CallbackQuery.answer(_["remove_10"], show_alert=True)
                if acha == None:
                    return await CallbackQuery.answer(_["remove_10"], show_alert=True)
                elif acha > 0:
                    popped = None
                    try:                                   
                      popped = check.pop(acha)
                    except:
                        return await CallbackQuery.answer(
                    _["remove_1"], show_alert=True
                     )
                    if popped:
                          await auto_clean(popped)
                          await CallbackQuery.answer()
                          return  await CallbackQuery.message.edit_text(
                            _["remove_2"].format((popped['title']), mention)          
                          )
                    
                else:
                                   popped = None
                                   try:                                   
                                    popped = check.pop(0)
                                   except:
                                        return await CallbackQuery.answer(
                                   _["remove_1"], show_alert=True
                                    )
                                   if popped:
                                         await auto_clean(popped)
                                         await CallbackQuery.answer()
                                         await CallbackQuery.message.edit_text(
                                           _["remove_2"].format((popped['title']), mention)          
                                         )
                                   if not check:
                                         try:
                                              await CallbackQuery.answer()
                                              await CallbackQuery.message.reply_text(
                                              _["remove_3"].format(mention)
                                    )
                                              return await Anony.stop_stream(chat_id)
                                         except:
                                               return
                queued = check[0]["file"]
                title = (check[0]["title"]).title()
                user = check[0]["by"]
                streamtype = check[0]["streamtype"]
                videoid = check[0]["vidid"]
                userinfo = check[0]["userinfo"]
                musicid = check[0]["musicid"]
                status = True if str(streamtype) == "video" else None
                db[chat_id][0]["played"] = 0
                exis = (check[0]).get("old_dur")
                if exis:
                                db[chat_id][0]["dur"] = exis
                                db[chat_id][0]["seconds"] = check[0]["old_second"]
                                db[chat_id][0]["speed_path"] = None
                                db[chat_id][0]["speed"] = 1.0
                if "live_" in queued:
                                n, link = await YouTube.video(videoid, True)
                                if n == 0:
                                                return await message.reply_text(_["admin_7"].format(title))
                                try:
                                                image = await YouTube.thumbnail(videoid, True)
                                except:
                                                image = None
                                try:
                                                await Anony.skip_stream(chat_id, link, video=status, image=image)
                                except:
                                                return await CallbackQuery.message.reply_text(_["call_6"])
                                button = stream_markup(_, musicid, userinfo, chat_id)
                                img = await get_thumb(videoid)
                                run = await CallbackQuery.message.reply_photo(
                                                photo=img,
                                                caption=_["stream_1"].format(
                                                                f"https://t.me/{app.username}?start=info_{videoid}",
                                                                title[:23],
                                                                check[0]["dur"],
                                                                user,
                                                ),
                                                reply_markup=InlineKeyboardMarkup(button),
                                )
                                db[chat_id][0]["mystic"] = run
                                db[chat_id][0]["markup"] = "tg"
                elif "vid_" in queued:
                                mystic = await CallbackQuery.message.reply_text(_["call_7"], disable_web_page_preview=True)
                                try:
                                                file_path, direct = await YouTube.download(
                                                                videoid,
                                                                mystic,
                                                                videoid=True,
                                                                video=status,
                                                )
                                except:
                                                return await mystic.edit_text(_["call_6"])
                                try:
                                                image = await YouTube.thumbnail(videoid, True)
                                except:
                                                image = None
                                try:
                                                await Anony.skip_stream(chat_id, file_path, video=status, image=image)
                                except:
                                                return await mystic.edit_text(_["call_6"])
                                button = stream_markup(_, musicid, userinfo, chat_id)
                                img = await get_thumb(videoid)
                                run = await CallbackQuery.message.reply_photo(
                                                photo=img,
                                                caption=_["stream_1"].format(
                                                                f"https://t.me/{app.username}?start=info_{videoid}",
                                                                title[:23],
                                                                check[0]["dur"],
                                                                user,
                                                ),
                                                reply_markup=InlineKeyboardMarkup(button),
                                )
                                db[chat_id][0]["mystic"] = run
                                db[chat_id][0]["markup"] = "stream"
                                await mystic.delete()
                elif "index_" in queued:
                                try:
                                                await Anony.skip_stream(chat_id, videoid, video=status)
                                except:
                                                return await CallbackQuery.message.reply_text(_["call_6"])
                                button = stream_markup(_, musicid, userinfo, chat_id)
                                run = await CallbackQuery.message.reply_photo(
                                                photo=config.STREAM_IMG_URL,
                                                caption=_["stream_2"].format(user),
                                                reply_markup=InlineKeyboardMarkup(button),
                                )
                                db[chat_id][0]["mystic"] = run
                                db[chat_id][0]["markup"] = "tg"
                else:
                                if videoid == "telegram":
                                                image = None
                                elif videoid == "soundcloud":
                                                image = None
                                else:
                                                try:
                                                                image = await YouTube.thumbnail(videoid, True)
                                                except:
                                                                image = None
                                try:
                                                await Anony.skip_stream(chat_id, queued, video=status, image=image)
                                except:
                                                return await CallbackQuery.message.reply_text(_["call_6"])
                                if videoid == "telegram":
                                                button = stream_markup(_, musicid, userinfo, chat_id)
                                                run = await CallbackQuery.message.reply_photo(
                                                                photo=config.TELEGRAM_AUDIO_URL
                                                                if str(streamtype) == "audio"
                                                                else config.TELEGRAM_VIDEO_URL,
                                                                caption=_["stream_1"].format(
                                                                                config.SUPPORT_CHAT, title[:23], check[0]["dur"], user
                                                                ),
                                                                reply_markup=InlineKeyboardMarkup(button),
                                                )
                                                db[chat_id][0]["mystic"] = run
                                                db[chat_id][0]["markup"] = "tg"
                                elif videoid == "soundcloud":
                                                button = stream_markup(_, musicid, userinfo, chat_id)
                                                run = await CallbackQuery.message.reply_photo(
                                                                photo=config.SOUNCLOUD_IMG_URL
                                                                if str(streamtype) == "audio"
                                                                else config.TELEGRAM_VIDEO_URL,
                                                                caption=_["stream_1"].format(
                                                                                config.SUPPORT_CHAT, title[:23], check[0]["dur"], user
                                                                ),
                                                                reply_markup=InlineKeyboardMarkup(button),
                                                )
                                                db[chat_id][0]["mystic"] = run
                                                db[chat_id][0]["markup"] = "tg"
                                else:
                                                button = stream_markup(_, musicid, userinfo, chat_id)
                                                img = await get_thumb(videoid)
                                                run = await CallbackQuery.message.reply_photo(
                                                                photo=img,
                                                                caption=_["stream_1"].format(
                                                                                f"https://t.me/{app.username}?start=info_{videoid}",
                                                                                title[:23],
                                                                                check[0]["dur"],
                                                                                user,
                                                                ),
                                                                reply_markup=InlineKeyboardMarkup(button),
                                                )
                                                db[chat_id][0]["mystic"] = run
                                                db[chat_id][0]["markup"] = "stream"
