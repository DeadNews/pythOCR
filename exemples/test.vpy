from vapoursynth import core

Clip = core.lsmas.LibavSMASHSource(
    source=r"/run/media/deadnews/data1/temp/temp/Hakumei to Mikochi/Hakumei to Mikochi - 01 [540p-RusSub].mp4"
)

if Clip.width != 1920 or Clip.height != 1080:
    Clip = core.resize.Lanczos(Clip, width=1920, height=1080)
    Clip.set_output()
