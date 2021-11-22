import moviepy.editor as mpe

cache = mpe.VideoFileClip(r'C:\Users\jonathan_wang\Videos\winwinwin.mp4').subclip(0, 30)
cache.write_gif(r'C:\Users\jonathan_wang\Videos\winwin.gif', fps=2)