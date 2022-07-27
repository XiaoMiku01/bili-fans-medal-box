import os, re
import requests


def get_medal_list():
    try:
        cookie = os.environ.get('BILI_COOKIE', '')
        api = 'https://api.live.bilibili.com/xlive/web-ucenter/user/MedalWall'
        headers = {'cookie': cookie}
        target_id = re.search(r'DedeUserID=(\d+)', cookie).group(1)
        params = (('target_id', target_id),)
        response = requests.get(api, headers=headers, params=params)
        medal_list = response.json()['data']['list'][:5]
        return medal_list
    except Exception as e:
        raise Exception("get_medal_list error: {}".format(e))


def generate_bar_chart(percent, size):
    syms = "░▏▎▍▌▋▊▉█"
    frac = int(size * 8 * percent / 100)
    bars_full = int(frac / 8)
    if bars_full >= size:
        return syms[8:9] * size
    semi = frac % 8
    return "".join([syms[8:9] * bars_full, syms[semi : semi + 1]]).ljust(size, syms[0])


widths = [
    (126, 1),
    (159, 0),
    (687, 1),
    (710, 0),
    (711, 1),
    (727, 0),
    (733, 1),
    (879, 0),
    (1154, 1),
    (1161, 0),
    (4347, 1),
    (4447, 2),
    (7467, 1),
    (7521, 0),
    (8369, 1),
    (8426, 0),
    (9000, 1),
    (9002, 2),
    (11021, 1),
    (12350, 2),
    (12351, 1),
    (12438, 2),
    (12442, 0),
    (19893, 2),
    (19967, 1),
    (55203, 2),
    (63743, 1),
    (64106, 2),
    (65039, 1),
    (65059, 0),
    (65131, 2),
    (65279, 1),
    (65376, 2),
    (65500, 1),
    (65510, 2),
    (120831, 1),
    (262141, 2),
    (1114109, 1),
]


def get_width(str):
    l = 0
    for s in str:
        o = ord(s)
        """Return the screen column width for unicode ordinal o."""
        global widths
        if o == 0xE or o == 0xF:
            continue
        for num, wid in widths:
            if o <= num:
                l += wid
                break
    return l


medal_list = get_medal_list()

l2 = []
for m in medal_list:
    medal_info = m['medal_info']
    medal_name = medal_info['medal_name']
    target_name = m['target_name']
    level = str(medal_info['level']) + '级'
    schedule = medal_info['intimacy'] / medal_info['next_intimacy'] * 100
    schedule_bar = generate_bar_chart(schedule, 20)
    l2.append(
        "|{}{}| {}{} {}".format(
            medal_name + ' ' * (6 - get_width(medal_name)),
            level.rjust(4),
            schedule_bar,
            ('%.2f' % schedule + "%").rjust(7),
            target_name,
        )
    )

GH_GIST_ID = os.environ.get('GH_GIST_ID', '')
GH_TOKEN = os.environ.get('GH_TOKEN', '')


def update_gist(gist_id, token):
    url = 'https://api.github.com/gists/{}'.format(gist_id)
    headers = {'Authorization': 'token {}'.format(token)}
    data = {
        'description': 'bilibili fans medal list',
        'public': False,
        'files': {'bili-fans-medals': {'content': '\n'.join(l2)}},
    }
    requests.patch(url, headers=headers, json=data)


update_gist(gist_id=GH_GIST_ID, token=GH_TOKEN)
print('\n'.join(l2))
