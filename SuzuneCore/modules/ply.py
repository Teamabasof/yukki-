from os import path

from pyrogram import Client
from pyrogram.types import Message, Voice
from pytgcalls import StreamType
from Attachments.callsmusic import callsmusic, queues
from pytgcalls.types.input_stream import AudioPiped
from Attachments.converter import converter
from Attachments.downloader import youtube
from SuzuneCore.callsmusic import calls
from SuzuneCore.config import BOT_NAME as bn, DURATION_LIMIT
from Attachments.devs.filters import command, other_filters
from Attachments.devs.decorators import errors
from Attachments.devs.errors import DurationLimitError
from Attachments.devs.gets import get_url, get_file_name
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(command("ply") & other_filters)
@errors
async def play(_, message: Message):

    lel = await message.reply("🔄 **Processing**")
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="𓆩𝐀ᴋ𝐀s𝐇𓆪™",
                        url="https://t.me/TheVenomXD")
                   
                ]
            ]
        )

    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"This Audio Is Larger Than {DURATION_LIMIT} minute(s)\n\n Be In Limits."
            )

        file_name = get_file_name(audio)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await lel.edit_text("Provide Me A Audio To Play !")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await lel.edit(f"#⃣ **Queued** at position {position}!")
    else:
        await calls.pytgcalls.join_group_call(message.chat.id, AudioPiped(audio), stream_type=StreamType().pulse_stream)
        await message.reply_photo(
        photo="https://telegra.ph/file/a7a5144ddd3214db6aebc.jpg",
        reply_markup=keyboard,
        caption="▶️ **Playing** here the song requested by🔥{}!".format(
        message.from_user.mention()
        ),
    )
        return await lel.delete()
