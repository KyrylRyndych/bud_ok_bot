from tg_bot.models.users import User
from asyncpg import UniqueViolationError

async def add_user(id:int, name:str, email:str = None):
    try:
        user = User(id=id, name= name, email=email)
        await user.create()
    except UniqueViolationError:
        pass
    
    
async def select_all_users():
    users = await User.query.gino.all()
    return users
        