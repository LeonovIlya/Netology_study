import aiohttp
import asyncio
import requests
import time
import sys
from more_itertools import chunked
from typing import Iterable
from sqlalchemy import insert
from aiopg.sa import create_engine
import config
from models import Person, get_async_session

r = requests.get('https://swapi.dev/api/people/')
q = (r.json()['count'])
print(f'Персонажей в БД ресурса - {q}')


async def get_persons(session: aiohttp.client.ClientSession, range_person_id: Iterable[int]):
    persons_list = []
    for person_id in range_person_id:
        res = await get_person(session, person_id)
        persons_list.append(res)
    for person_id_chunk in chunked(range_person_id, 10):
        get_person_tasks = [asyncio.create_task(get_person(session, person_id)) for person_id in person_id_chunk]
        await asyncio.gather(*get_person_tasks)
    return persons_list


async def get_person(session: aiohttp.client.ClientSession, person_id: int) -> dict:
    async with session.get(f'https://swapi.dev/api/people/{person_id}', ssl=False) as response:
        response_json = await response.json()
        try:
            response_json['id'] = person_id
            response_json.pop('created')
            response_json.pop('edited')
            response_json.pop('url')
        except KeyError:
            response_json['id'] = person_id
        return response_json


async def add_person(person):
    async with create_engine(config.db_link) as engine:
        async with engine.acquire() as conn:
            try:
                req = insert(Person).values(pers_id=person['id'], name=person['name'],
                                            height=person['height'], mass=person['mass'],
                                            hair_color=person['hair_color'], skin_color=person['skin_color'],
                                            eye_color=person['eye_color'], birth_year=person['birth_year'],
                                            gender=person['gender'], homeworld=person['homeworld'],
                                            films=person['films'], species=person['species'],
                                            vehicles=person['vehicles'], starships=person['starships'])
                await conn.execute(req)
            except KeyError:
                req = insert(Person).values()
                await conn.execute(req)
            except ValueError:
                req = insert(Person).values()
                await conn.execute(req)


async def add_persons():
    async with aiohttp.client.ClientSession() as session:
        persons_list = await get_persons(session, range(1, q))
        for person in persons_list:
            await add_person(person)


async def main():
    async with aiohttp.client.ClientSession() as session:
        await get_persons(session, range(1, q))
        await get_async_session(True, True)
        await add_persons()
        time.sleep(0.1)


if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(f'Добавлено записей в локальную БД: {q} , за {time.time() - start} секунд')
