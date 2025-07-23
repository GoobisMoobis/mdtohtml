# MdToHtml

After months of using my [converter I built](https://GoobisMoobis.github.io/mdtohtml/), I started to wonder if there was a way that I could open markdown files I had downloaded on my computer.

I didn't really want to download a program for it, because I didn't feel good knowing I could probably do it myself. It felt like a cop-out.

So, after 4 iterations of the script, I finally managed to get it to work.

## Functionality

1. Download the .exe file.
2. [Set it as the default program](https://support.microsoft.com/en-us/windows/change-default-apps-in-windows-e5d82cad-17d1-c53b-3505-f10a32e1894d) for md files
3. Double-click on any md file, and wait a few seconds.

**Windows Defender will oftentimes mark this file as a virus, even though it isn't. If you don't trust me, you can download the [raw .py file](https://github.com/GoobisMoobis/mdtohtml/blob/main/app/mdtohtml_v4.py) and use something like [pyinstaller](https://pyinstaller.org/en/stable/) or [py2exe](https://www.py2exe.org/) to make it into an executable file**

<hr>

Want to edit the code for yourself, or change anything? Download [mdtohtml_v4.py](https://github.com/GoobisMoobis/mdtohtml/blob/main/app/mdtohtml_v4.py) and edit it yourself, then use something like [pyinstaller](https://pyinstaller.org/en/stable/) or [py2exe](https://www.py2exe.org/) to make it back into an exe file!
