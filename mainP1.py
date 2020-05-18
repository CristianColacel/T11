import asyncio


async def calcul_suma(nr: int, time: int):
    s = 0
    for i in range(0, nr+1):
        s += i
    await asyncio.sleep(time)
    print(f'Suma primelor {nr} numere este: {s}')


async def rezultat_suma():
    coada = [1, 5, 10, 25]
    print('Calculez suma...')
    rezultat = await asyncio.gather(calcul_suma(coada.pop(0), 2),
                                    calcul_suma(coada.pop(0), 4),
                                    calcul_suma(coada.pop(0), 6),
                                    calcul_suma(coada.pop(0), 8))
    return rezultat

if __name__=='__main__':
    asyncio.get_event_loop().run_until_complete(rezultat_suma())
