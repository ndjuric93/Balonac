import sqlite3
from collections import Counter

conn = sqlite3.connect(
    '/home/nemanjadjuric/Workspaces/Balonac/server/db.sqlite3')

with open('stats.csv', 'r') as f:
    data = f.readlines()
    data = [d.split(',') for d in data]


def load_players_table(data):
    names = list(filter(lambda name: name != '' and name != '\n', data[0]))[1:]
    print(names)
    stats = [d[1:] for d in data[2:]]

    apps = [Counter() for _ in range(0, len(stats[0]), 3)]
    for stat in stats[:4]:
        cnt = 0
        for i in range(0, len(stat), 3):
            apps[cnt].update(stat[i + 2].strip())
            cnt += 1

    statistics = [
        (stats[-1][i], stats[-1][i+1], stats[-1][i+2])
        for i in range(0, len(stats[-1]), 3)
    ]
    # names = [name.decode("utf-8", "strict") for name in names]
    values = [
        (name, int(stats[0]), int(stats[1]), 4 - apps['N'], apps['1'], apps['0'])
        for name, apps, stats in zip(names, apps, statistics)
    ]
    sql = ''' INSERT INTO players_player
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    for i, value in enumerate(values):
        data = [i, value[0], value[1], value[2], value[3], value[4], value[5]]
        print(data)
        cur.execute(sql, data)
    conn.commit()


def load_events_table(data):
    from collections import namedtuple, defaultdict
    names = list(filter(lambda name: name != '' and name != '\n', data[0]))[1:-1]
    dates = [d[0] for d in data][2:6]
    GameStats = namedtuple('GameStats', ['name', 'date', 'g', 'a', 'team'])
    game_stats = []
    dates = [date.replace('/', '-') + ' 14:00:00' for date in dates]
    for d in data[2:6]:
        date = d[0].replace('/', '-') + ' 14:00:00'
        cnt = 0
        for i in range(1, len(d[1:]), 3):
            if(d[i] != 'NI'):
                game_stats.append(
                    GameStats(
                        name=names[cnt],
                        date=date,
                        g=d[i],
                        a=d[i+1],
                        team=d[i+2]
                    )
                )
                cnt += 1
    scores = defaultdict(dict)
    curr = conn.cursor()
    for gs in game_stats:
        dat = gs.date.split(' ')
        tmp = dat[0].split('-')
        tmp[0] = '0' + tmp[0] if len(tmp[0]) == 1 else tmp[0]
        tmp[1] = '0' + tmp[1] if len(tmp[1]) == 1 else tmp[1]
        tmp = '-'.join([tmp[2], tmp[0], tmp[1]]) + ' ' + dat[1]
        print(tmp)

        # get_date_id_query = 'select id from events_event where date=\'f{tmp}\''
        # get_player_id_query = 'select distinct players_player.id from players_player inner join events_eventplayer on players_player.id = events_eventplayer.player_id where name=\'{gs.name}\''
        sql = f'''
        insert into events_event_players (event_id, eventplayer_id)
            VALUES(
                (select id from events_event where date='{tmp}'),
                (select distinct players_player.id from players_player 
                    inner join events_eventplayer on players_player.id = events_eventplayer.player_id
                    where name='{gs.name}'
                )
            );
        '''
        curr.execute(sql)
    conn.commit()
        # if gs.team in scores[gs.date]:
        #     scores[gs.date][gs.team] += int(gs.g)
        # else:
        #     scores[gs.date][gs.team] = int(gs.g)

    # cur = conn.cursor()
    # for date in dates:
    #     dat = date.split(' ')
    #     tmp = dat[0].split('-')
    #     tmp[0] = '0' + tmp[0] if len(tmp[0]) == 1 else tmp[0]
    #     tmp[1] = '0' + tmp[1] if len(tmp[1]) == 1 else tmp[1]
    #     tmp = '-'.join([tmp[2], tmp[0], tmp[1]]) + ' ' + dat[1]
    #     print(tmp)
    #     sql = 'insert into events_event (date, location, score_a, score_b, completed) values(?,?,?,?,?)'
    #     cur.execute(sql, [tmp, 'Zlatna lopta',scores[date]['0'], scores[date]['1'], True])
    # conn.commit()
# 27|2021-02-02 00:01:00|test|0|0|||0

load_events_table(data)

# load_players_table(data)

 