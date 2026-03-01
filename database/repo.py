from sqlalchemy.ext.asyncio import AsyncSession
from database.models import User
from sqlalchemy import select, update, delete

class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
    
    async def create(self, tid, username):
        user = User(tid=tid, username=username)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

    async def select(self, tid):
        stmt = select(User).where(tid==tid)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def close(self):
        await self.session.close()