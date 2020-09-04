import discord
from message import Message
from discord.ext import commands
import settings
from card import Card, CardManager
from digit_to_emoji import toEmoji

class MyCommand:

    def __init__(self):

        self.bot = commands.Bot(command_prefix=settings.COMMAND_PREFIX, status=settings.BOT_STATUS,
                           activity=settings.BOT_ACTIVITY, help_command=settings.BOT_HELP_COMMAND)

        self.manager = CardManager()
        self.card = Card()
        
        @self.bot.command()
        async def 도움말(ctx):
            embed = discord.Embed(
                title=f':fire: 안녕하세요, 저는 {settings.BOT_NAME}입니다!', description=f'저는 이런 기능들을 가지고 있어요!\n궁금하신건 `{settings.DEVELOPER}`에게 물어봐주세요!', color=settings.MAIN_COLOR)
            embed.add_field(name='일반', value='`뽑기 <숫자>`')
            embed.add_field(name='운영진', value='`섞기`, `목록`, `설정`')
            await ctx.send(embed=embed)
        
        @self.bot.command()
        async def 뽑기(ctx, *args):
            if not args:
                await ctx.send('이런 식으로 해주세요! `!뽑기 <숫자>`')
            else:
                try:
                    choose = int(args[0])
                    name = ctx.message.author.name
                    user = discord.utils.get(ctx.guild.members, name=name)
                    await ctx.send(f'{user.mention} {self.card.play(choose)}')
                except ValueError:
                    await ctx.send('숫자를 입력해주세요!')

        @self.bot.command()
        @commands.has_role(settings.ADMIN_ROLE)
        async def 섞기(ctx):
            self.card = Card()
            name = ctx.message.author.name
            user = discord.utils.get(ctx.guild.members, name=name)
            cards = self.manager.getCards()
            await ctx.send(f'{toEmoji(len(cards))}개의 카드를 섞고 있습니다...🃏')
            await ctx.send(f'{user.mention} {self.card.shuffleCard()}')

        @self.bot.command()
        @commands.has_role(settings.ADMIN_ROLE)
        async def 목록(ctx):
            cards = self.manager.getCards()
            embed = discord.Embed(
                title=f'카드 목록', color=settings.MAIN_COLOR)
            card_list = ''
            for card in range(len(cards)):
                card_text = f'{toEmoji(card)} {cards[card]}'
                if card_list == '':
                    card_list = card_text
                else:
                    card_list += f'\n{card_text}'
            embed.add_field(name='🃏', value=card_list)
            await ctx.send(embed=embed)

        @self.bot.command()
        @commands.has_role(settings.ADMIN_ROLE)
        async def 설정(ctx, *args):
            if not args:
                await ctx.send('이런 식으로 해주세요! `!설정 A,B,C`')
            else:
                self.manager.setCards(args[0])
                await ctx.send('카드 목록을 변경했어요!')

        # @self.bot.command()
        # @commands.has_role(settings.ADMIN_ROLE)
        # async def 추가(ctx):
        #     pass

        # @self.bot.command()
        # @commands.has_role(settings.ADMIN_ROLE)
        # async def 삭제(ctx):
        #     pass