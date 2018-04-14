import logging
import os
import sys

import discord
from discord.ext import commands
from discord.ext.commands.bot import _mention_pattern, _mentions_transforms

from . import colors, embeds
from .bot_utils import config
from .messages import Messages
import traceback, datetime