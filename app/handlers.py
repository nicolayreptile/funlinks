import fastapi_plugins
import aioredis
from time import time
from aioredis.commands import SortedSetCommandsMixin
from fastapi import APIRouter, Depends, Query

from app.consts import REDIS_KEY
from app.responses import Response
from app.models import UserData


router = APIRouter()


@router.post('/visited_links')
async def visited_links(user_data: UserData,
                        storage: aioredis.Redis = Depends(fastapi_plugins.depends_redis)):
    visited_time = time()
    links = user_data.links
    pairs = []
    for i, member in enumerate(links):
        score = visited_time + i / (10 ** 6)
        pairs.extend([score, '{}:{}'.format(member, score)])
    await storage.zadd(REDIS_KEY, *pairs, exist=SortedSetCommandsMixin.ZSET_IF_NOT_EXIST)

    return Response()


@router.get('/visited_domains')
async def visited_domains(from_: int = Query(..., alias='from'), to: int = Query(...),
                          storage: aioredis.Redis = Depends(fastapi_plugins.depends_redis)):
    result = await storage.zrangebyscore(REDIS_KEY, from_, to)
    domains = [link.decode().rsplit(':', maxsplit=1)[0] for link in result]
    return Response(domains=domains)
