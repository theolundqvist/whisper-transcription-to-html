import glob
import os
import shutil
cwd = os.getcwd()


last_time = ""
dash_total = 0
dash_count = 0
await_dash = False
max_dash_join = 8


def format(line, path):
    global last_time, dash_count, dash_total, await_dash
    time = line.split("[")[1].split("]")[0].split()[0]
    h = last_time.split(":")[0] if last_time else 0
    m = last_time.split(":")[1] if last_time else 0
    s = last_time.split(":")[2].split(".")[0] if last_time else 0
    tot = int(h)*3600 + int(m)*60 + int(s)

    text = line.split("]")[1]
    link = f'<a href="#" onclick="playAudio(event, \'{path}\',{tot})">{last_time.split(".")[0][1:]}</a>'
    if '-' in text[0:5]:
        text = f'{link}<br/><br/>{text} ' if last_time != "" else text
        last_time = time
        dash_count = 0
        await_dash = True
        return text

    if dash_count > max_dash_join:
        await_dash = False
    else:
        dash_count += 1
    if not await_dash:
        text = f'{link}<br/><br/>{text} ' if last_time != "" else text
        last_time = time
    return text


for n in glob.glob(cwd+"/in/*.txt"):
    if "formatted" in n:
        continue
    last_time = ""
    dash_total = 0
    dash_count = 0
    await_dash = False
    max_dash_join = 5
    f = open(n)
    content = f.read().splitlines()
    res = """<head>
    <style>a,br{user-select: none;}</style>
    <meta charset=\"UTF-8\">
    <script>
        var current_playing = -1;
        var current_audio = undefined;
        function playAudio(event, path, time){
            event.preventDefault()
           if(current_audio && !current_audio.paused){
               current_audio.pause();
           }
           else{
               current_audio = new Audio(path+"#t="+time)
               current_audio.play()
               current_playing = time;
           }
        }
    </script>
    </head>
    <body style=\"max-width:800px;margin:auto;margin-top:100px !important;text-align:center;\">"""
    name = os.path.basename(n)
    person = name.split(".")[0]
    res += f'<h1>{person}</h1>'
    for line in content:
        res += format(line, f'./audio/{person}.m4a')
    res += '</body>'
    print(res[-200:])
    new = open(cwd+"/out/"+person+".html", "w")
    new.write(res)
    new.close()

shutil.make_archive("out", 'zip', "out")
