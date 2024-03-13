import asyncio, random
from AnonXMusic.core.userbot import assistants
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
    FloodWait
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AnonXMusic import YouTube, app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import (
    get_assistant,
    net_assistant,
    get_assistant_number,
    get_cmode,
    get_lang,
    get_playmode,
    get_playtype,
    is_active_chat,
    is_maintenance,
)
from AnonXMusic.utils.inline import botplaylist_markup
from config import PLAYLIST_IMG_URL, SUPPORT_CHAT, adminlist
from strings import get_string

async def change_assistant(message, userbot, chat_id, app, _): 
    try:
        get = await app.get_chat_member(chat_id, userbot.id)
        if (
            get.status == ChatMemberStatus.BANNED
            or get.status == ChatMemberStatus.RESTRICTED
        ): 
            try:
              await app.unban_chat_member(chat_id, userbot.id)
              return await message.reply_text("Assistant Unbanned, Try Playing again now")
            except:
              return await message.reply_text(
                  _["call_2"].format(
                      app.mention, userbot.id, userbot.name, userbot.username
                  )
              )
    except ChatAdminRequired:
        return await message.reply_text(_["call_1"])
    except UserNotParticipant:
        if message.chat.username:
                  invitelink = message.chat.username
                  try:
                     await userbot.resolve_peer(invitelink)
                  except:
                      pass
        else:
              try:
                 invitelink = await app.export_chat_invite_link(chat_id)
              except ChatAdminRequired:
                    return await message.reply_text(_["call_1"])
              except Exception as e:
                    return await message.reply_text(
                          _["call_3"].format(app.mention, type(e).__name__)
                    )
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace("https://t.me/+", "https://t.me/joinchat/")
        try:
            await asyncio.sleep(2)
            await userbot.join_chat(invitelink)
        except InviteRequestSent:
            try:
                await app.approve_chat_join_request(chat_id, userbot.id)
            except Exception as e:
                return await message.reply_text(_["call_3"].format(app.mention, type(e).__name__))
            await asyncio.sleep(3)
        except UserAlreadyParticipant:
            pass
        except Exception as e:
            return await message.reply_text(
                _["call_3"].format(app.mention, type(e).__name__)
            )
        try:
            await userbot.resolve_peer(chat_id)
        except:
            pass



def PlayWrapper(command):
    async def wrapper(client, message):
        language = await get_lang(message.chat.id)
        _ = get_string(language)
        if message.sender_chat:
            upl = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ʜᴏᴡ ᴛᴏ ғɪx ?",
                            callback_data="AnonymousAdmin",
                        ),
                    ]
                ]
            )
            return await message.reply_text(_["general_3"], reply_markup=upl)

        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    text=f"{app.mention} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ, ᴠɪsɪᴛ <a href={SUPPORT_CHAT}>sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ</a> ғᴏʀ ᴋɴᴏᴡɪɴɢ ᴛʜᴇ ʀᴇᴀsᴏɴ.",
                    disable_web_page_preview=True,
                )
        audio_telegram = (
            (message.reply_to_message.audio or message.reply_to_message.voice)
            if message.reply_to_message
            else None
        )
        video_telegram = (
            (message.reply_to_message.video or message.reply_to_message.document)
            if message.reply_to_message
            else None
        )
        url = await YouTube.url(message)
        if audio_telegram is None and video_telegram is None and url is None:
            if len(message.command) < 2:
                if "stream" in message.command:
                    return await message.reply_text(_["str_1"])
                buttons = botplaylist_markup(_)
                return await message.reply_photo(
                    photo=PLAYLIST_IMG_URL,
                    caption=_["play_18"],
                    reply_markup=InlineKeyboardMarkup(buttons),
                )
        if message.command[0][0] == "c":
            chat_id = await get_cmode(message.chat.id)
            if chat_id is None:
                return await message.reply_text(_["setting_7"])
            try:
                chat = await app.get_chat(chat_id)
            except:
                return await message.reply_text(_["cplay_4"])
            channel = chat.title
        else:
            chat_id = message.chat.id
            channel = None
        playmode = await get_playmode(message.chat.id)
        playty = await get_playtype(message.chat.id)
        if playty != "Everyone":
            if message.from_user.id not in SUDOERS:
                admins = adminlist.get(message.chat.id)
                if not admins:
                    return await message.reply_text(_["admin_13"])
                else:
                    if message.from_user.id not in admins:
                        return await message.reply_text(_["play_4"])
        if message.command[0][0] == "v":
            video = True
        else:
            if "-v" in message.text:
                video = True
            else:
                video = True if message.command[0][1] == "v" else None
        if message.command[0][-1] == "e":
            if not await is_active_chat(chat_id):
                return await message.reply_text(_["play_16"])
            fplay = True
        else:
            fplay = None

        if not await is_active_chat(chat_id):
            userbot = await get_assistant(chat_id)
            try:                
                get = await app.get_chat_member(chat_id, userbot.id)
                if (
                    get.status == ChatMemberStatus.BANNED
                    or get.status == ChatMemberStatus.RESTRICTED
                ): 
                    try:
                      await app.unban_chat_member(chat_id, userbot.id)
                      return await message.reply_text("Assistant Unbanned, Try Playing again now")
                    except:
                      return await message.reply_text(
                          _["call_2"].format(
                              app.mention, userbot.id, userbot.name, userbot.username
                          )
                      )
            except ChatAdminRequired:
                return await message.reply_text(_["call_1"])
            except UserNotParticipant:                               
                if message.chat.username:
                        invitelink = message.chat.username
                        try:
                            await userbot.resolve_peer(invitelink)
                        except:
                            pass
                else:
                        try:
                            invitelink = await app.export_chat_invite_link(chat_id)
                        except ChatAdminRequired:
                            return await message.reply_text(_["call_1"])
                        except Exception as e:
                            return await message.reply_text(
                                _["call_3"].format(app.mention, type(e).__name__)
                            )

                if invitelink.startswith("https://t.me/+"):
                    invitelink = invitelink.replace(
                        "https://t.me/+", "https://t.me/joinchat/"
                    )
                myu = await message.reply_text(_["call_4"].format(app.mention))
                try:
                    await asyncio.sleep(2)
                    await userbot.join_chat(invitelink)
                except InviteRequestSent:
                    try:
                        await app.approve_chat_join_request(chat_id, userbot.id)
                    except Exception as e:
                        return await message.reply_text(
                            _["call_3"].format(app.mention, type(e).__name__)
                        )
                    await asyncio.sleep(3)
                    await myu.edit(_["call_5"].format(app.mention))
                except UserAlreadyParticipant:
                    pass
                except FloodWait:             
                       current_id = await get_assistant_number(chat_id)
                       different_assistants = [assistant_id for assistant_id in assistants if assistant_id != current_id]
                       new = random.choice(different_assistants)
                       ok = await net_assistant(new, chat_id)
                       await change_assistant(message, ok, chat_id, app, _)                   
                except Exception as e:
                    return await message.reply_text(
                        _["call_3"].format(app.mention, type(e).__name__)
                    )
                try:
                    await userbot.resolve_peer(chat_id)
                except:
                    pass

        return await command(
            client,
            message,
            _,
            chat_id,
            video,
            channel,
            playmode,
            url,
            fplay,
        )

    return wrapper
