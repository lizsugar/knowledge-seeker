#!/bin/python3 

from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import os
import json

template_dir, template_file = os.path.split(sys.argv[1])

# Get our template json file
env = Environment(
  loader=FileSystemLoader(template_dir),
  trim_blocks=True,
  lstrip_blocks=True)

final = env.get_template(template_file)

# Empty dictionary ready for population from show data
generated_show = {
  "seasons": [ ]
}

videoLibrary = sys.argv[2] + "videos"
subtitleLibrary = sys.argv[2] + "subtitles"

# Walk our dir
for dirpath, dirs, files in os.walk(videoLibrary):
  dirs.sort()
  if dirpath != videoLibrary:
    seasonSlug = seasonName = dirpath.split("/")[-1]
    season = {
      "seasonSlug": seasonSlug,
      "seasonName": seasonName,
      "seasonIcon": "",
      "episodes": [ ] 
    }

    for a,b,myfiles in os.walk(dirpath):
      myfiles.sort()

      for episode in myfiles:
        episodeSlug = episode.split(" - ")[1]
        episodeName = episode.split(" - ")[2].split(".")[0]
        episodeSubtitleFile = episode.split(".")[0] + ".srt"
        newEpisode = {
          "episodeSlug": episodeSlug,
          "episodeName": episodeName,
          "videoFile": videoLibrary + "/" + episode,
          "subtitleFile": subtitleLibrary + "/" + episodeSubtitleFile
        }
        season["episodes"].append(newEpisode)

    generated_show["seasons"].append(season)

#pretty = json.dumps(generated_show, indent=2)
#print(type(pretty))
#print(pretty)

#print(final.render(generated_show))
output = (final.render(generated_show))
with open("test.json", "w") as outfile:
  #json.dump(output, outfile, indent=2)
  outfile.write(output)