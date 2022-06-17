from os import listdir, mkdir
from pyrogram import Client

from SuzuneCore import config
from SuzuneCore.callsmusic.queues import clear, get, is_empty, put, task_done
from SuzuneCore.callsmusic import queues
from SuzuneCore.callsmusic.youtube import download
from SuzuneCore.callsmusic.calls import run, pytgcalls
from SuzuneCore.callsmusic.calls import client

if "raw_files" not in listdir():
    mkdir("raw_files")

from SuzuneCore.callsmusic.convert import convert
