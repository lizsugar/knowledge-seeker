import flask
import re

from datetime import timedelta

def strptimecode(td):
    atd = abs(td)
    milliseconds = round(atd.microseconds/1000)
    seconds = atd.seconds % 60
    minutes = atd.seconds // 60 % 60
    hours = atd.seconds // 60 // 60
    if hours > 0:
        string = '%02d:%02d:%02d.%03d' % (hours, minutes, seconds, milliseconds)
    else:
        string = '%02d:%02d.%03d' % (minutes, seconds, milliseconds)
    if td >= timedelta(0):
        return string
    else:
        return '-%s' % string

def strftimecode(tc):
    match = re.search(r'^(\d*:)?(\d+):(\d+\.?\d*)$', tc)
    if match is not None:
        groups = match.groups()
        if groups[0] is None:
            hours = 0
        else:
            hours = int(groups[0][:-1])
        minutes = int(groups[1])
        milliseconds = round(float(groups[2])*1000)
        return timedelta(hours=hours, minutes=minutes, milliseconds=milliseconds)
    else:
        raise ValueError('invalid timecode format: \'%s\'' % tc)

def find_episode(season, episode):
    seasons = [s for s in flask.current_app.library_data if s.slug == season]
    if len(seasons) == 0:
        return None, None
    else:
        episodes = [e for e in seasons[0].episodes if e.slug == episode]
        if len(episodes) == 0:
            return None, None
        else:
            return seasons[0], episodes[0]

def http_error(code, message):
    return flask.Response(message, status=code, mimetype='text/plain')

# https://stackoverflow.com/a/21303393
def grouper(input_list, n=2):
    for i in range(len(input_list) - (n - 1)):
        yield input_list[i:i + n]

